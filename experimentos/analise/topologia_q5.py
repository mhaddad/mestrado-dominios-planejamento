"""EXP-25 (Fase 4B): propriedades de topologia de busca (Hoffmann, 2011) na Q5 e no R-29 por instância.

Pergunta: as propriedades com fundamento teórico acrescentam, às 16 features SAS+, poder de
explicar qual família de técnica resolve a instância (Q5, como no EXP-21) e de escolher o
planejador por instância (Q1/R-29, como no EXP-24)?

Propriedades (data/ipc-2011-2023/topologia_ipc.csv, extrator validado em
experimentos/extratores/topologia-validacao/):
  basico, frac_inversiveis, log1p(hff_s0), de_taxa, sp_taxa e sp_dist_media (0 quando nenhuma
  saída foi achada). Entram só tarefas com status ok (10 amostras). Todas são calculadas antes de
  resolver a tarefa, sem usar resultado da competição.

  Uma primeira rodada (27/09/2026) incluiu também razao_hff = hff_custo_s0 / melhor custo
  conhecido da instância. Foi descartada: o melhor custo vem dos planos dos competidores, isto é,
  do próprio resultado que se quer explicar (vazamento), e um seletor não o teria na hora de
  escolher. Os resultados daquela rodada não são usados.

Conjuntos comparados, sempre nas mesmas instâncias (as que têm os dois tipos de features):
  tamanho (variáveis, operadores), sas (as 16 do EXP-21), topologia, sas+topologia.

Parte A (Q5): para cada edição × trilha × recorte × família, AUC da logística deixando um domínio
de fora, por conjunto. Teste do acréscimo da topologia: permutação das linhas do bloco de
topologia (as SAS+ ficam como estão), p unilateral da AUC de sas+topologia; 199 permutações,
1.999 se p < 0,05; Holm por recorte. Teste da topologia sozinha: permutação do rótulo, como no
EXP-21.
Parte B (Q1): seletores do EXP-24 (método de 2010 por planejador, 4D todas, kNN, random forest)
com cada conjunto; perda contra o VBS; Wilcoxon por domínio contra o SBS; Holm por edição × trilha
× recorte.

Uso: uv run --no-project --with scikit-learn --with scipy --with numpy python experimentos/analise/topologia_q5.py
Saídas: experimentos/analise/topologia-q5/{modelos.csv, seletores.csv}
"""

import csv
import math
import sys
from pathlib import Path

import numpy as np
from scipy.stats import wilcoxon

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "experimentos/analise"))
import q5_ipc as Q  # noqa: E402
import r29_instancias as R  # noqa: E402
from correcao_multipla import holm  # noqa: E402

DADOS = RAIZ / "data/ipc-2011-2023"
SAIDA = RAIZ / "experimentos/analise/topologia-q5"
TOPO = ["basico", "frac_inversiveis", "hff_s0", "de_taxa", "sp_taxa", "sp_dist_media"]


def carregar_topologia():
    topo = {}
    for r in Q.ler("topologia_ipc.csv"):
        if r["status"] != "ok":
            continue
        k = (r["edicao"], r["trilha"], r["dominio"], r["problema"])
        topo[k] = [1.0 if r["basico"] == "True" else 0.0, float(r["frac_inversiveis"]),
                   math.log1p(float(r["hff_s0"])), float(r["de_taxa"]), float(r["sp_taxa"]),
                   float(r["sp_dist_media"]) if r["sp_dist_media"] else 0.0]
    return topo


def p_bloco(X, bloco, y, grupos, observado, rng):
    """Permutação das linhas do bloco de colunas `bloco` (as outras ficam fixas)."""
    maiores, n = 0, 0
    for total in Q.PERMUTACOES:
        while n < total:
            Xp = X.copy()
            Xp[:, bloco] = X[rng.permutation(len(X))][:, bloco]
            maiores += Q.auc_lodo(Xp, y, grupos, "logistica") >= observado
            n += 1
        p = (1 + maiores) / (1 + n)
        if p >= 0.05:
            break
    return p, n


def main():
    feats, topo = Q.carregar_features(), carregar_topologia()
    tec = Q.carregar_tecnicas()
    res, plan = Q.resolvidos()
    rng = np.random.default_rng(2010)
    SAIDA.mkdir(parents=True, exist_ok=True)
    nsas = len(Q.FEATURES)
    i_tam = [Q.FEATURES.index(f) for f in Q.TAMANHO]
    conjuntos = {"tamanho": i_tam, "sas": list(range(nsas)), "topologia": list(range(nsas, nsas + len(TOPO))),
                 "sas+topologia": list(range(nsas + len(TOPO)))}
    modelos, seletores = [], []
    for (ed, tr), instancias in sorted(res.items()):
        tf = "seq-sat" if tr == "seq-agl" else tr
        for recorte in ("todos", "sem-portfolios"):
            ps = sorted(p for p in plan[(ed, tr)]
                        if recorte == "todos" or "Portfólio" not in tec[(ed, tr, p)]["D4"])
            chaves = sorted(k for k, quem in instancias.items()
                            if quem & set(ps) and (ed, tf, *k) in feats and (ed, tf, *k) in topo)
            sem = sum(1 for k, quem in instancias.items() if quem & set(ps) and (ed, tf, *k) in feats
                      and (ed, tf, *k) not in topo)
            X = np.array([feats[(ed, tf, *k)] + topo[(ed, tf, *k)] for k in chaves])
            dom = np.array([k[0] for k in chaves])
            # ---- Parte A: famílias
            familias = {}
            for p in ps:
                for dim in ("D1", "D2"):
                    for v in tec[(ed, tr, p)][dim]:
                        if v != "não determinado":
                            familias.setdefault((dim, v), set()).add(p)
            for (dim, v), membros in sorted(familias.items()):
                y = np.array([1 if instancias[k] & membros else 0 for k in chaves])
                l = {"edicao": ed, "trilha": tr, "recorte": recorte, "dimensao": dim, "familia": v,
                     "planejadores": len(membros), "instancias": len(y), "sem_topologia": sem}
                if y.sum() < Q.MIN_POSITIVOS or len(y) - y.sum() < Q.MIN_POSITIVOS:
                    modelos.append({**l, "obs": "sem variação suficiente"})
                    continue
                for nome, cols in conjuntos.items():
                    l[f"auc_{nome}"] = round(Q.auc_lodo(X[:, cols], y, dom, "logistica"), 3)
                bloco = conjuntos["topologia"]
                p_ac, n_ac = p_bloco(X, bloco, y, dom, l["auc_sas+topologia"], rng)
                p_so, n_so = Q.p_permutacao(X[:, bloco], y, dom, l["auc_topologia"], rng)
                l.update(p_acrescimo=round(p_ac, 4), perm_acrescimo=n_ac, p_topologia=round(p_so, 4),
                         perm_topologia=n_so, obs="")
                modelos.append(l)
            # ---- Parte B: seletores
            Y = np.array([[1 if p in instancias[k] else 0 for p in ps] for k in chaves])
            doms = sorted(set(dom))
            tec_de = [{f"{d}: {v}" for d in ("D1", "D2", "D3", "D4") for v in tec[(ed, tr, p)][d]
                       if v != "não determinado"} for p in ps]
            sels = {"metodo-2010-planejador": R.metodo_2010, "metodo-2010-4d-todas":
                    lambda a, b, c: R.metodo_2010_tecnica(a, b, c, tec_de), "knn": R.knn, "rf": R.rf}
            perda_sbs = np.zeros(len(chaves))
            for d in doms:
                te, trn = dom == d, dom != d
                perda_sbs[te] = 1 - Y[te, int(Y[trn].sum(axis=0).argmax())]
            sbs_d = np.array([perda_sbs[dom == d].sum() for d in doms])
            grupo = []
            for nome_c, cols in conjuntos.items():
                if nome_c == "tamanho":
                    continue
                for nome_s, sel in sels.items():
                    perda = np.zeros(len(chaves))
                    for d in doms:
                        te, trn = dom == d, dom != d
                        esc = sel(X[trn][:, cols], Y[trn], X[te][:, cols])
                        perda[te] = 1 - Y[te][np.arange(te.sum()), esc]
                    dif = sbs_d - np.array([perda[dom == d].sum() for d in doms])
                    grupo.append({"edicao": ed, "trilha": tr, "recorte": recorte, "instancias": len(chaves),
                                  "dominios": len(doms), "caracteristicas": nome_c, "seletor": nome_s,
                                  "perda_total": round(float(perda.sum()), 1), "perda_sbs": round(float(perda_sbs.sum()), 1),
                                  "wilcoxon_p_vs_sbs": round(float(wilcoxon(dif).pvalue), 4) if np.any(dif != 0) else 1.0})
            for g, a in zip(grupo, holm([g["wilcoxon_p_vs_sbs"] for g in grupo])):
                g["p_holm"] = round(a, 4)
            seletores += grupo
            print(f"{ed} {tr} [{recorte}] {len(chaves)} instâncias ({sem} sem topologia)", flush=True)
    for recorte in ("todos", "sem-portfolios"):
        for chave in ("p_acrescimo", "p_topologia"):
            testados = [l for l in modelos if l["recorte"] == recorte and l.get(chave) is not None and l.get("obs") == ""]
            for l, a in zip(testados, holm([l[chave] for l in testados])):
                l[chave.replace("p_", "holm_")] = round(a, 4)
    campos_m = ["edicao", "trilha", "recorte", "dimensao", "familia", "planejadores", "instancias", "sem_topologia",
                "auc_tamanho", "auc_sas", "auc_topologia", "auc_sas+topologia", "p_acrescimo", "perm_acrescimo",
                "holm_acrescimo", "p_topologia", "perm_topologia", "holm_topologia", "obs"]
    for nome, linhas, campos in (("modelos.csv", modelos, campos_m), ("seletores.csv", seletores, None)):
        with (SAIDA / nome).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=campos or list(linhas[0]), lineterminator="\n", extrasaction="ignore")
            w.writeheader()
            w.writerows(linhas)
        print(f"{len(linhas)} linhas -> {nome}")


if __name__ == "__main__":
    main()
