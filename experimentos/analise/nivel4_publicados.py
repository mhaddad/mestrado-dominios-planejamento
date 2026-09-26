"""Nível 4 (auditoria/reexecucao.md §6), só com dados publicados (decisão do autor, 26/09/2026).

Desempenho: cobertura por domínio do Planner Museum (data/planner-museum/cobertura_por_dominio.csv;
29 planejadores × 42 domínios Autoscale, 30 instâncias cada, 30 min e 4 GiB).
Características, por domínio, extraídas do PDDL das mesmas instâncias Autoscale:
  (a) as 11 métricas de 2010 extraíveis do PDDL (extrator do R-25; arquivo de domínio único ou,
      com domínio por instância, o da primeira instância);
  (b) as 17 features SAS+ (R-26; mediana das 30 instâncias);
  (c) (a) + (b).

Tarefa: para cada domínio, escolher um planejador. Perda = cobertura do melhor planejador no
domínio menos a do escolhido (medida principal, decisão G19). Validação leave-one-domain-out:
cada domínio é previsto por um modelo treinado nos demais. Domínios em que nenhum planejador
resolve nada ficam fora (não há escolha a avaliar).

Seletores:
  vbs            virtual best (perda 0 por definição)
  sbs            single best: maior cobertura total nos domínios de treino
  acaso          perda esperada de uma escolha uniforme
  metodo-2010    o método de 2010 com o planejador no lugar da técnica: cada característica
                 (feature + classe Baixo/Médio/Alto) recebe a cobertura média de cada
                 planejador nos domínios de treino com aquela classe; o domínio novo soma as
                 médias das suas características e escolhe o maior. Discretização pelos
                 tercis do treino (a regra dos extremos de 2010 deixa quase tudo em Médio com
                 41 domínios; EXP-10)
  knn            3 vizinhos mais próximos (features padronizadas pelo treino); escolhe o
                 planejador de maior cobertura somada nos vizinhos
  rf             random forest de regressão por planejador (cobertura ~ features; 300
                 árvores, semente 2010); escolhe o maior previsto

Comparação com o SBS: diferença de perda domínio a domínio, teste de Wilcoxon pareado.

Uso: python experimentos/analise/nivel4_publicados.py
Requer scikit-learn e scipy. Saídas: experimentos/analise/nivel4-publicados/
  {caracteristicas.csv, escolhas.csv, resumo.csv}
"""
import csv
import statistics
import sys
from pathlib import Path

import numpy as np
from scipy.stats import wilcoxon
from sklearn.ensemble import RandomForestRegressor

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "experimentos/extratores"))
import metricas_2010_pddl as X  # noqa: E402

AUTOSCALE = RAIZ / "experimentos/ferramentas/planner-museum/benchmarks/autoscale-unit-cost"
SAIDA = RAIZ / "experimentos/analise/nivel4-publicados"
# Nomes da Tabela 1 do Planner Museum -> pastas do Autoscale
PASTA = {"Grid": "grid", "Gripper": "gripper", "Logistics": "logistics", "MPrime": "mprime",
         "Blocks": "blocksworld", "Freecell": "freecell", "Miconic": "miconic", "Depots": "depots",
         "Driverlog": "driverlog", "Rovers": "rovers", "Satellite": "satellite", "Zenotravel": "zenotravel",
         "Airport": "airport", "Pipeswrldnt": "pipesworld-notankage", "Pipeswrldt": "pipesworld-tankage",
         "Openstacks": "openstacks", "Pathways": "pathways", "Storage": "storage", "TPP": "tpp",
         "Elevators": "elevators", "Parcprinter": "parcprinter", "Pegsol": "pegsol", "Scanalyzer": "scanalyzer",
         "Sokoban": "sokoban", "Transport": "transport", "Visitall": "visitall", "Woodworking": "woodworking",
         "Barman": "barman", "Floortile": "floortile", "NoMystery": "nomystery", "Parking": "parking",
         "Tidybot": "tidybot", "Childsnack": "childsnack", "GED": "ged", "Hiking": "hiking", "Tetris": "tetris",
         "Thoughtful": "thoughtful", "Agricola": "agricola", "Datanet": "data-network",
         "Organicsynth": "organic-synthesis-split", "Snake": "snake", "Termes": "termes"}


def carregar():
    with (RAIZ / "data/planner-museum/cobertura_por_dominio.csv").open(encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    planejadores = list(linhas[0])[2:]
    cob = {PASTA[r["dominio"]]: np.array([int(r[p]) for p in planejadores]) for r in linhas}
    sas = {}
    with (RAIZ / "experimentos/extratores/features-sas-autoscale/dominios.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            sas[r["dominio"]] = {f"sas:{k}": float(v) for k, v in r.items()
                                 if k not in ("dominio", "instancias", "traduzidas") and v != ""}
    pddl = {}
    for d in cob:
        pasta = AUTOSCALE / d
        arq = pasta / "domain.pddl" if (pasta / "domain.pddl").exists() else pasta / "domain-p01.pddl"
        pddl[d] = {f"pddl:{k}": float(v) for k, v in X.metricas(X.ler_dominio(arq)).items()}
    return planejadores, cob, pddl, sas


def tercis(treino_vals, v):
    a, b = np.quantile(treino_vals, [1 / 3, 2 / 3])
    return 0 if v <= a else 1 if v <= b else 2


def seletor_2010(Xtr, Ytr, x):
    pont = np.zeros(Ytr.shape[1])
    for j in range(Xtr.shape[1]):
        c_tr = np.array([tercis(Xtr[:, j], v) for v in Xtr[:, j]])
        c = tercis(Xtr[:, j], x[j])
        mask = c_tr == c
        if mask.any():
            pont += Ytr[mask].mean(axis=0)
    return int(np.argmax(pont))


def seletor_knn(Xtr, Ytr, x, k=3):
    mu, sd = Xtr.mean(axis=0), Xtr.std(axis=0)
    sd[sd == 0] = 1
    dist = np.linalg.norm((Xtr - mu) / sd - (x - mu) / sd, axis=1)
    viz = np.argsort(dist)[:k]
    return int(np.argmax(Ytr[viz].sum(axis=0)))


def seletor_rf(Xtr, Ytr, x):
    rf = RandomForestRegressor(n_estimators=300, random_state=2010, n_jobs=-1)
    rf.fit(Xtr, Ytr)  # multi-saída: uma cobertura por planejador
    return int(np.argmax(rf.predict(x.reshape(1, -1))[0]))


def main():
    planejadores, cob, pddl, sas = carregar()
    doms = sorted(d for d in cob if cob[d].max() > 0 and d in sas)
    fora = sorted(set(cob) - set(doms))
    conjuntos = {"pddl": lambda d: pddl[d], "sas": lambda d: sas[d], "pddl+sas": lambda d: {**pddl[d], **sas[d]}}
    Y = np.array([cob[d] for d in doms])
    melhor = Y.max(axis=1)

    with (SAIDA.mkdir(parents=True, exist_ok=True) or SAIDA / "caracteristicas.csv").open("w", encoding="utf-8", newline="") as f:
        cols = sorted({**pddl[doms[0]], **sas[doms[0]]})
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["dominio"] + cols)
        for d in doms:
            w.writerow([d] + [{**pddl[d], **sas[d]}[c] for c in cols])

    escolhas, perdas = [], {}
    perdas["vbs"] = np.zeros(len(doms))
    perdas["acaso"] = melhor - Y.mean(axis=1)
    sbs = []
    for i in range(len(doms)):
        tr = [k for k in range(len(doms)) if k != i]
        sbs.append(int(np.argmax(Y[tr].sum(axis=0))))
    perdas["sbs"] = melhor - Y[np.arange(len(doms)), sbs]
    for i, d in enumerate(doms):
        escolhas.append({"dominio": d, "seletor": "sbs", "caracteristicas": "-", "escolhido": planejadores[sbs[i]],
                         "cobertura": int(Y[i, sbs[i]]), "melhor": int(melhor[i])})
    for nome_c, feat in conjuntos.items():
        cols = sorted(feat(doms[0]))
        Xall = np.array([[feat(d)[c] for c in cols] for d in doms])
        for nome_s, sel in (("metodo-2010", seletor_2010), ("knn", seletor_knn), ("rf", seletor_rf)):
            esc = []
            for i, d in enumerate(doms):
                tr = [k for k in range(len(doms)) if k != i]
                j = sel(Xall[tr], Y[tr], Xall[i])
                esc.append(j)
                escolhas.append({"dominio": d, "seletor": nome_s, "caracteristicas": nome_c,
                                 "escolhido": planejadores[j], "cobertura": int(Y[i, j]), "melhor": int(melhor[i])})
            perdas[f"{nome_s} ({nome_c})"] = melhor - Y[np.arange(len(doms)), esc]

    resumo = []
    for nome, p in perdas.items():
        linha = {"seletor": nome, "perda_media": round(float(p.mean()), 2), "perda_total": round(float(p.sum()), 1),
                 "dominios_perda_zero": int((p == 0).sum()), "dominios": len(doms),
                 "fracao_da_lacuna_sbs_fechada": round(1 - float(p.sum()) / float(perdas["sbs"].sum()), 3)}
        if nome not in ("vbs", "sbs", "acaso"):
            dif = perdas["sbs"] - p
            linha["wilcoxon_p_vs_sbs"] = round(float(wilcoxon(dif).pvalue), 3) if np.any(dif != 0) else ""
        resumo.append(linha)
    campos = list(resumo[-1])
    for nome, linhas in (("escolhas.csv", escolhas), ("resumo.csv", resumo)):
        with (SAIDA / nome).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=campos if nome == "resumo.csv" else list(linhas[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)
    print(f"{len(doms)} domínios avaliados; fora (nenhum planejador resolve nada ou sem features): {fora}")
    for r in resumo:
        print(r)


if __name__ == "__main__":
    main()
