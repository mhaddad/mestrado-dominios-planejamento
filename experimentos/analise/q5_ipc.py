"""EXP-21 (Fase 4B, Q5): características da tarefa × famílias de técnicas nas IPCs 2011 e 2018.

Q5: nos resultados publicados das IPCs posteriores a 2010, quais características estruturais do
domínio, extraídas do PDDL, explicam o desempenho relativo das famílias de técnicas?

Desenho: docs/fase4b-desenho.md (D1: portfólios; D2: recorte). Dados em data/ipc-2011-2023/:
  resultados   ipc2018_resultados.csv (execução) e ipc2011_resultados.csv (plano válido)
  ligação      ipc2011_arquivos.csv (problema do WebPlan -> arquivo PDDL)
  features     features_sas_ipc.csv (16 features SAS+ do extrator da Fase 3)
  técnicas     planejadores_4d.csv (taxonomia 4D)

Unidades: edição × trilha. 2018: ótima, satisficing e agile; os 10 domínios do placar, com as
formulações normal e split de caldera e organic-synthesis no lugar do `-combined` (D2, regra 2).
2011: ótima e satisficing; um problema resolvido = há plano válido no WebPlan.

Família = um valor da D1 ou da D2. Um planejador com vários valores pertence a várias famílias
(P1). A família "resolve" uma instância se algum planejador dela resolve.

Saídas (experimentos/analise/q5-ipc/):
  mapa_familias.csv  por edição, trilha, recorte, domínio e família: instâncias resolvidas pelo
                     melhor planejador da família e pelo melhor planejador geral
  modelos.csv        por edição, trilha, recorte e família: entre as instâncias com features que
                     algum planejador resolve, a família resolve? Regressão logística L2 com as
                     features padronizadas (log1p nas contagens) e árvore de profundidade 2,
                     validadas deixando um domínio de fora por vez. Medida: AUC das previsões
                     fora da amostra. Referências: AUC da taxa da família por domínio de treino
                     (= 0,5, sem informação) e AUC de um modelo só com o tamanho da tarefa
                     (variáveis, operadores), para separar "estrutura" de "tamanho".
                     Teste: permutação do rótulo entre as instâncias (hipótese nula: as features
                     não têm relação com o resultado), p unilateral da AUC da logística; 199
                     permutações e, se p < 0,05, 1.999 (semente 2010). Correção de Holm entre os
                     modelos de cada recorte (mesma função de correcao_multipla.py).
  importancias.csv   coeficientes da logística ajustada em todos os domínios

Recortes: "todos" e "sem-portfolios" (D4 diferente de Portfólio).

Uso: uv run --no-project --with scikit-learn --with numpy python experimentos/analise/q5_ipc.py
"""

import collections
import csv
import math
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data/ipc-2011-2023"
SAIDA = RAIZ / "experimentos/analise/q5-ipc"
FEATURES = ["variaveis", "dominio_medio", "dominio_max", "operadores", "metas", "axiomas",
            "cg_arestas", "cg_densidade", "cg_grau_max", "cg_aciclico", "cg_cfc",
            "cg_maior_cfc_frac", "cg_treewidth_sup", "dtg_arcos_medio",
            "dtg_fortemente_conexo_frac", "dtg_arcos_invertiveis_frac"]
CONTAGENS = {"variaveis", "dominio_max", "operadores", "metas", "axiomas", "cg_arestas",
             "cg_grau_max", "cg_cfc", "cg_treewidth_sup"}
TAMANHO = ["variaveis", "operadores"]
FORMULACOES_2018 = {"caldera", "caldera-split", "organic-synthesis", "organic-synthesis-split"}
MIN_POSITIVOS = 10  # família precisa resolver e falhar em pelo menos isto para ter modelo
PERMUTACOES = (199, 1999)


def ler(nome):
    return list(csv.DictReader((DADOS / nome).open(encoding="utf-8")))


def carregar_features():
    feats = {}
    for r in ler("features_sas_ipc.csv"):
        if r["status"] != "ok":
            continue
        v = []
        for f in FEATURES:
            x = 1.0 if r[f] == "True" else 0.0 if r[f] == "False" else float(r[f])
            v.append(math.log1p(x) if f in CONTAGENS else x)
        feats[(r["edicao"], r["trilha"], r["dominio"], r["problema"])] = v
    return feats


def carregar_tecnicas():
    tec = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in ler("planejadores_4d.csv"):
        trilhas = ("seq-opt", "seq-sat", "seq-agl") if r["trilhas"] == "todas" else r["trilhas"].split(",")
        for t in trilhas:
            tec[(r["edicao"], t, r["planejador"])][r["dimensao"]].add(r["valor"])
    return tec


def resolvidos():
    """{(edição, trilha): {(domínio, problema_pddl): set(planejadores que resolvem)}} e planejadores."""
    res = collections.defaultdict(lambda: collections.defaultdict(set))
    plan = collections.defaultdict(set)
    for r in ler("ipc2018_resultados.csv"):
        d = r["dominio"]
        if not ((r["oficial"] == "sim" and not d.endswith("-combined")) or d in FORMULACOES_2018):
            continue
        u = ("2018", r["trilha"])
        plan[u].add(r["planejador"])
        res[u].setdefault((d, r["problema"]), set())
        if r["cobertura"] == "1":
            res[u][(d, r["problema"])].add(r["planejador"])
    arq = {(r["trilha"], r["problema"]): r for r in ler("ipc2011_arquivos.csv")}
    for r in ler("ipc2011_problemas.csv"):
        a = arq[(r["trilha"], r["problema"])]
        res[("2011", r["trilha"])].setdefault((r["dominio"], a["arquivo"]), set())
    for r in ler("ipc2011_resultados.csv"):
        a = arq[(r["trilha"], r["problema"])]
        u = ("2011", r["trilha"])
        plan[u].add(r["planejador"])
        res[u][(r["dominio"], a["arquivo"])].add(r["planejador"])
    return res, plan


def auc_lodo(X, y, grupos, modelo):
    """Previsões fora da amostra deixando um domínio de fora; AUC agregada."""
    p = np.zeros(len(y))
    for g in np.unique(grupos):
        te, tr = grupos == g, grupos != g
        if len(np.unique(y[tr])) < 2:
            p[te] = y[tr].mean()
            continue
        if modelo == "base":
            p[te] = y[tr].mean()
            continue
        mu, sd = X[tr].mean(0), X[tr].std(0)
        sd[sd == 0] = 1
        if modelo == "logistica":
            m = LogisticRegression(C=1.0, max_iter=2000).fit((X[tr] - mu) / sd, y[tr])
        else:
            m = DecisionTreeClassifier(max_depth=2, min_samples_leaf=20, random_state=2010).fit(X[tr], y[tr])
        p[te] = m.predict_proba((X[te] - mu) / sd if modelo == "logistica" else X[te])[:, 1]
    return roc_auc_score(y, p) if len(np.unique(y)) == 2 else float("nan")


def p_permutacao(X, y, grupos, observado, rng):
    maiores, n = 0, 0
    for total in PERMUTACOES:
        while n < total:
            maiores += auc_lodo(X, rng.permutation(y), grupos, "logistica") >= observado
            n += 1
        p = (1 + maiores) / (1 + n)
        if p >= 0.05:
            break
    return p, n


def holm(pvals):
    """p-valores ajustados por Holm (step-down), na ordem de entrada."""
    m = len(pvals)
    ordem = sorted(range(m), key=lambda i: pvals[i])
    ajust = [0.0] * m
    corrente = 0.0
    for k, i in enumerate(ordem):
        corrente = max(corrente, min(1.0, (m - k) * pvals[i]))
        ajust[i] = corrente
    return ajust


def main():
    feats = carregar_features()
    tec = carregar_tecnicas()
    res, plan = resolvidos()
    SAIDA.mkdir(parents=True, exist_ok=True)
    mapa, modelos, imps = [], [], []
    rng = np.random.default_rng(2010)
    for (ed, tr), instancias in sorted(res.items()):
        trilha_feat = "seq-sat" if tr == "seq-agl" else tr
        for recorte in ("todos", "sem-portfolios"):
            ps = [p for p in plan[(ed, tr)]
                  if recorte == "todos" or "Portfólio" not in tec[(ed, tr, p)]["D4"]]
            familias = collections.defaultdict(set)
            for p in ps:
                for dim in ("D1", "D2"):
                    for v in tec[(ed, tr, p)][dim]:
                        if v != "não determinado":
                            familias[(dim, v)].add(p)
            # Mapa por domínio
            por_dom = collections.defaultdict(list)
            for (d, prob), quem in instancias.items():
                por_dom[d].append(quem & set(ps))
            for d, lst in sorted(por_dom.items()):
                melhor_geral = max(sum(p in q for q in lst) for p in ps)
                for (dim, v), membros in sorted(familias.items()):
                    melhor = max(sum(p in q for q in lst) for p in membros)
                    mapa.append({"edicao": ed, "trilha": tr, "recorte": recorte, "dominio": d,
                                 "dimensao": dim, "familia": v, "planejadores": len(membros),
                                 "instancias": len(lst), "melhor_da_familia": melhor,
                                 "melhor_geral": melhor_geral})
            # Modelos por instância
            chaves = [(d, prob) for (d, prob), quem in instancias.items()
                      if quem & set(ps) and (ed, trilha_feat, d, prob) in feats]
            sem_feat = sum(1 for (d, prob), quem in instancias.items()
                           if quem & set(ps) and (ed, trilha_feat, d, prob) not in feats)
            X = np.array([feats[(ed, trilha_feat, d, prob)] for d, prob in chaves])
            grupos = np.array([d for d, _ in chaves])
            idx_tam = [FEATURES.index(f) for f in TAMANHO]
            for (dim, v), membros in sorted(familias.items()):
                y = np.array([1 if instancias[k] & membros else 0 for k in chaves])
                linha = {"edicao": ed, "trilha": tr, "recorte": recorte, "dimensao": dim, "familia": v,
                         "planejadores": len(membros), "instancias": len(y), "sem_features": sem_feat,
                         "dominios": len(np.unique(grupos)), "taxa": round(y.mean(), 3) if len(y) else ""}
                if y.sum() < MIN_POSITIVOS or (len(y) - y.sum()) < MIN_POSITIVOS:
                    linha.update(auc_base="", auc_tamanho="", auc_logistica="", auc_arvore="",
                                 p_permutacao="", permutacoes="", p_holm="", obs="sem variação suficiente")
                else:
                    linha.update(
                        auc_base=round(auc_lodo(X, y, grupos, "base"), 3),
                        auc_tamanho=round(auc_lodo(X[:, idx_tam], y, grupos, "logistica"), 3),
                        auc_logistica=round(auc_lodo(X, y, grupos, "logistica"), 3),
                        auc_arvore=round(auc_lodo(X, y, grupos, "arvore"), 3))
                    pp, n = p_permutacao(X, y, grupos, auc_lodo(X, y, grupos, "logistica"), rng)
                    linha.update(p_permutacao=round(pp, 4), permutacoes=n, p_holm="", obs="")
                    mu, sd = X.mean(0), X.std(0)
                    sd[sd == 0] = 1
                    m = LogisticRegression(C=1.0, max_iter=2000).fit((X - mu) / sd, y)
                    for f, c in zip(FEATURES, m.coef_[0]):
                        imps.append({"edicao": ed, "trilha": tr, "recorte": recorte, "dimensao": dim,
                                     "familia": v, "feature": f, "coeficiente": round(c, 3)})
                modelos.append(linha)
    for recorte in ("todos", "sem-portfolios"):
        testados = [l for l in modelos if l["recorte"] == recorte and l["p_permutacao"] != ""]
        for l, a in zip(testados, holm([l["p_permutacao"] for l in testados])):
            l["p_holm"] = round(a, 4)
    for nome, linhas in (("mapa_familias.csv", mapa), ("modelos.csv", modelos), ("importancias.csv", imps)):
        with (SAIDA / nome).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)
        print(f"{len(linhas)} linhas -> {nome}")
    print("\nAUC fora da amostra (deixando um domínio de fora), recorte 'todos':")
    for l in modelos:
        if l["recorte"] == "todos" and l["auc_logistica"] != "":
            print(f"  {l['edicao']} {l['trilha']} {l['dimensao']} {l['familia'][:40]:40s} "
                  f"n={l['instancias']:4d} taxa={l['taxa']:.2f} tam={l['auc_tamanho']:.2f} "
                  f"log={l['auc_logistica']:.2f} arv={l['auc_arvore']:.2f} p={l['p_permutacao']} holm={l['p_holm']}")


if __name__ == "__main__":
    main()
