"""R-29 por instância (Fase 4B; Q1): escolha de planejador por instância com dados das IPCs 2011 e 2018.

Continuação do R-28/R-29 da Fase 3 (EXP-12 e EXP-13, por domínio, com o Planner Museum), agora
por instância e com resultados de competição (decisão do autor, 27/09/2026). Mesmos seletores
de experimentos/analise/nivel4_publicados.py, adaptados à instância.

Dados (data/ipc-2011-2023/, ver o README de lá): cobertura por instância de 2018 (execuções) e
de 2011 (planos válidos do WebPlan, ligados aos PDDL), features SAS+ por tarefa e taxonomia 4D.
O carregamento é o mesmo do EXP-21 (experimentos/analise/q5_ipc.py): 2018 com os 10 domínios do
placar e as formulações normal e split de caldera e organic-synthesis no lugar do `-combined`.

Unidades: edição × trilha. Instâncias: as que têm features e que algum planejador do recorte
resolve (nas outras não há escolha a avaliar).

Tarefa: para cada instância, escolher um planejador. Perda = 1 se o escolhido não resolve (o VBS
resolve por construção). Validação: deixando um domínio de fora; o modelo é treinado nas
instâncias dos outros domínios.

Seletores (fixados antes de rodar):
  vbs, acaso (perda esperada de uma escolha uniforme), sbs (maior cobertura no treino)
  metodo-2010-planejador   o método de 2010 com o planejador no lugar da técnica, tercis do treino
  metodo-2010-4d-{todas,D1,D2}   o método de 2010 por técnica (EXP-13), com planejadores_4d.csv
  knn                      5 vizinhos (features padronizadas pelo treino); maior cobertura somada
  rf                       random forest multi-saída (300 árvores, semente 2010); maior previsão
Features: as 16 SAS+ (log1p nas contagens). As métricas de 2010 não entram: saem do arquivo de
domínio e são constantes dentro de cada domínio.

Comparação com o SBS: soma da perda por domínio, Wilcoxon pareado sobre a diferença; correção de
Holm entre os seletores de cada edição × trilha × recorte.

Recortes: "todos" e "sem-portfolios".

Uso: uv run --no-project --with scikit-learn --with scipy --with numpy python experimentos/analise/r29_instancias.py
Saídas: experimentos/analise/r29-instancias/{resumo.csv, perdas_por_dominio.csv}
"""

import csv
import sys
import warnings
from pathlib import Path

import numpy as np
from scipy.stats import wilcoxon
from sklearn.ensemble import RandomForestRegressor

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "experimentos/analise"))
import q5_ipc as Q  # noqa: E402
from correcao_multipla import holm  # noqa: E402

SAIDA = RAIZ / "experimentos/analise/r29-instancias"
warnings.filterwarnings("ignore", message="Mean of empty slice")  # classe de tercil vazia: tratada como NaN
K_VIZINHOS = 5


def tercis_tabela(Xtr, Ytr):
    """Limites dos tercis por feature e cobertura média de cada planejador por (feature, classe)."""
    lim = np.quantile(Xtr, [1 / 3, 2 / 3], axis=0)
    classes = np.where(Xtr <= lim[0], 0, np.where(Xtr <= lim[1], 1, 2))
    tab = np.full((Xtr.shape[1], 3, Ytr.shape[1]), np.nan)
    for j in range(Xtr.shape[1]):
        for c in range(3):
            m = classes[:, j] == c
            if m.any():
                tab[j, c] = Ytr[m].mean(axis=0)
    return lim, tab


def classes_de(lim, Xte):
    return np.where(Xte <= lim[0], 0, np.where(Xte <= lim[1], 1, 2))


def metodo_2010(Xtr, Ytr, Xte):
    lim, tab = tercis_tabela(Xtr, Ytr)
    c = classes_de(lim, Xte)
    notas = np.nansum(tab[np.arange(Xtr.shape[1])[None, :], c], axis=1)  # instâncias × planejadores
    return np.nan_to_num(notas, nan=-np.inf).argmax(axis=1)


def metodo_2010_tecnica(Xtr, Ytr, Xte, tec_de):
    """Por técnica (EXP-13): nota do planejador = média, sobre as suas técnicas, da média sobre as
    características da cobertura média dos pares (instância de treino com a característica,
    planejador que usa a técnica)."""
    tecnicas = sorted({t for ts in tec_de for t in ts})
    usa = [np.array([t in ts for ts in tec_de]) for t in tecnicas]
    lim, tab = tercis_tabela(Xtr, Ytr)  # tab: feature × classe × planejador
    tab_tec = np.stack([np.nanmean(tab[:, :, u], axis=2) for u in usa], axis=2)  # feature × classe × técnica
    c = classes_de(lim, Xte)
    media_tec = np.nanmean(tab_tec[np.arange(Xtr.shape[1])[None, :], c], axis=1)  # instâncias × técnicas
    notas = np.full((len(Xte), len(tec_de)), -1.0)
    for k, ts in enumerate(tec_de):
        idx = [i for i, t in enumerate(tecnicas) if t in ts]
        if idx:
            notas[:, k] = media_tec[:, idx].mean(axis=1)
    return np.nan_to_num(notas, nan=-np.inf).argmax(axis=1)


def knn(Xtr, Ytr, Xte):
    mu, sd = Xtr.mean(0), Xtr.std(0)
    sd[sd == 0] = 1
    A, B = (Xtr - mu) / sd, (Xte - mu) / sd
    dist = np.linalg.norm(B[:, None, :] - A[None, :, :], axis=2)
    viz = np.argsort(dist, axis=1)[:, :K_VIZINHOS]
    return Ytr[viz].sum(axis=1).argmax(axis=1)


def rf(Xtr, Ytr, Xte):
    m = RandomForestRegressor(n_estimators=300, random_state=2010, n_jobs=-1).fit(Xtr, Ytr)
    pred = m.predict(Xte)
    return (pred if pred.ndim == 2 else pred[:, None]).argmax(axis=1)


def main():
    feats = Q.carregar_features()
    tec = Q.carregar_tecnicas()
    res, plan = Q.resolvidos()
    SAIDA.mkdir(parents=True, exist_ok=True)
    resumo, por_dom = [], []
    for (ed, tr), instancias in sorted(res.items()):
        tf = "seq-sat" if tr == "seq-agl" else tr
        for recorte in ("todos", "sem-portfolios"):
            ps = sorted(p for p in plan[(ed, tr)]
                        if recorte == "todos" or "Portfólio" not in tec[(ed, tr, p)]["D4"])
            chaves = sorted(k for k, quem in instancias.items() if quem & set(ps) and (ed, tf, *k) in feats)
            X = np.array([feats[(ed, tf, *k)] for k in chaves])
            Y = np.array([[1 if p in instancias[k] else 0 for p in ps] for k in chaves])
            dom = np.array([k[0] for k in chaves])
            doms = sorted(set(dom))
            tec_dims = {rot: [{f"{d}: {v}" for d in dims for v in tec[(ed, tr, p)][d] if v != "não determinado"}
                              for p in ps]
                        for rot, dims in (("4d-todas", ("D1", "D2", "D3", "D4")), ("4d-D1", ("D1",)), ("4d-D2", ("D2",)))}
            seletores = {"metodo-2010-planejador": metodo_2010, "knn": knn, "rf": rf}
            for rot, tec_de in tec_dims.items():
                seletores[f"metodo-2010-{rot}"] = lambda a, b, c, t=tec_de: metodo_2010_tecnica(a, b, c, t)
            perda = {"vbs": np.zeros(len(chaves)), "acaso": 1 - Y.mean(axis=1)}
            escolha_sbs = {}
            perda["sbs"] = np.zeros(len(chaves))
            for nome in seletores:
                perda[nome] = np.zeros(len(chaves))
            for d in doms:
                te, trn = dom == d, dom != d
                j = int(Y[trn].sum(axis=0).argmax())
                escolha_sbs[d] = ps[j]
                perda["sbs"][te] = 1 - Y[te, j]
                for nome, sel in seletores.items():
                    esc = sel(X[trn], Y[trn], X[te])
                    perda[nome][te] = 1 - Y[te][np.arange(te.sum()), esc]
            por_d = {n: np.array([perda[n][dom == d].sum() for d in doms]) for n in perda}
            linhas, pvals = [], []
            for n, p in perda.items():
                l = {"edicao": ed, "trilha": tr, "recorte": recorte, "planejadores": len(ps),
                     "instancias": len(chaves), "dominios": len(doms), "seletor": n,
                     "perda_total": round(float(p.sum()), 1),
                     "fracao_da_lacuna_sbs_fechada": round(1 - float(p.sum()) / float(perda["sbs"].sum()), 3)
                     if perda["sbs"].sum() else "",
                     "wilcoxon_p_vs_sbs": "", "p_holm": ""}
                if n not in ("vbs", "sbs", "acaso"):
                    dif = por_d["sbs"] - por_d[n]
                    l["wilcoxon_p_vs_sbs"] = round(float(wilcoxon(dif).pvalue), 4) if np.any(dif != 0) else 1.0
                    pvals.append(l)
                linhas.append(l)
            for l, a in zip(pvals, holm([l["wilcoxon_p_vs_sbs"] for l in pvals])):
                l["p_holm"] = round(a, 4)
            resumo += linhas
            for i, d in enumerate(doms):
                por_dom.append({"edicao": ed, "trilha": tr, "recorte": recorte, "dominio": d,
                                "instancias": int((dom == d).sum()), "sbs_escolhido": escolha_sbs[d],
                                **{f"perda_{n}": round(float(por_d[n][i]), 2) for n in perda}})
            sbs_total = Y.sum(axis=0)
            print(f"{ed} {tr} [{recorte}] {len(ps)} planejadores, {len(chaves)} instâncias, {len(doms)} domínios; "
                  f"SBS geral = {ps[int(sbs_total.argmax())]}; perdas: "
                  + ", ".join(f"{n} {perda[n].sum():.0f}" for n in perda))
    for nome, linhas in (("resumo.csv", resumo), ("perdas_por_dominio.csv", por_dom)):
        with (SAIDA / nome).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)
        print(f"{len(linhas)} linhas -> {nome}")


if __name__ == "__main__":
    main()
