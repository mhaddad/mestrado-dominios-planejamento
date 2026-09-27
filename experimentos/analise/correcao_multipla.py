"""Correção de Holm para as comparações com o single best (SBS) do EXP-12/EXP-13 e do X3 (EXP-14/EXP-15).

Os scripts originais (`nivel4_publicados.py`, `llm/x3-seletor/x3_seletor.py`) testam cada seletor contra o SBS
com o Wilcoxon pareado sobre a diferença de perda por domínio, sem corrigir para comparações múltiplas.
Este script recalcula os mesmos p-valores a partir das escolhas por domínio (mesma chamada do `scipy`) e aplica
a correção de Holm por família de comparações. Não altera os resultados originais.

Famílias:
  - nivel4-exp12: os seletores da tabela do EXP-12 (método de 2010 por planejador, kNN, random forest × pddl, sas,
    pddl+sas), subconjunto "todos";
  - nivel4-todas: todas as comparações do subconjunto "todos" (EXP-12 mais as variantes por técnica do EXP-13);
  - x3-<rodada>: os 4 modelos de cada rodada do X3 (principal-grupo, principal-exata, nomes-exata).

Uso: uv run --no-project --with scipy --with numpy python experimentos/analise/correcao_multipla.py
Saída: experimentos/analise/correcao-multipla/holm.csv
"""

import csv
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import wilcoxon

RAIZ = Path(__file__).resolve().parents[2]
NIVEL4 = RAIZ / "experimentos/analise/nivel4-publicados/escolhas.csv"
X3 = RAIZ / "llm/x3-seletor/resultados"
SAIDA = RAIZ / "experimentos/analise/correcao-multipla/holm.csv"
EXP12 = {f"{s} ({c})" for s in ("metodo-2010-planejador", "knn", "rf") for c in ("pddl", "sas", "pddl+sas")}


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


def perdas_nivel4():
    perdas = defaultdict(dict)  # seletor -> dominio -> perda
    with open(NIVEL4, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["subconjunto"] != "todos":
                continue
            nome = r["seletor"] if r["caracteristicas"] == "-" else f"{r['seletor']} ({r['caracteristicas']})"
            perdas[nome][r["dominio"]] = float(r["melhor"]) - float(r["cobertura"])
    return perdas


def testar(perdas_sbs, perdas_sel):
    doms = [d for d in perdas_sbs if d in perdas_sel]
    dif = np.array([perdas_sbs[d] - perdas_sel[d] for d in doms])
    if len(dif) <= 5 or not np.any(dif != 0):
        return None, len(doms), float(sum(perdas_sel[d] for d in doms))
    return float(wilcoxon(dif).pvalue), len(doms), float(sum(perdas_sel[d] for d in doms))


def main():
    p4 = perdas_nivel4()
    sbs = p4["sbs"]
    linhas = []
    comparacoes = []
    for nome, pd in p4.items():
        if nome in ("sbs", "vbs", "acaso"):
            continue
        p, n, total = testar(sbs, pd)
        if p is not None:
            comparacoes.append((nome, p, n, total))
    for familia, filtro in (("nivel4-exp12", lambda n: n in EXP12), ("nivel4-todas", lambda n: True)):
        fam = [c for c in comparacoes if filtro(c[0])]
        for (nome, p, n, total), pa in zip(fam, holm([c[1] for c in fam])):
            linhas.append({"familia": familia, "comparacao": nome, "dominios": n, "perda_total": total,
                           "perda_total_sbs": sum(sbs.values()), "p": round(p, 4), "p_holm": round(pa, 4),
                           "tamanho_familia": len(fam)})

    for rodada in ("principal-grupo", "principal-exata", "nomes-exata"):
        por_modelo = defaultdict(dict)
        with open(X3 / rodada / "escolhas.csv", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r["perda"] not in ("", "nan"):
                    por_modelo[r["modelo"]][r["dominio"]] = float(r["perda"])
        fam = []
        for modelo, pd in por_modelo.items():
            p, n, total = testar(sbs, pd)
            fam.append((modelo, p, n, total))
        for (modelo, p, n, total), pa in zip(fam, holm([c[1] for c in fam])):
            linhas.append({"familia": f"x3-{rodada}", "comparacao": modelo, "dominios": n, "perda_total": total,
                           "perda_total_sbs": sum(sbs[d] for d in por_modelo[modelo]), "p": round(p, 4),
                           "p_holm": round(pa, 4), "tamanho_familia": len(fam)})

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    with open(SAIDA, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    for l in linhas:
        marca = "*" if l["p_holm"] < 0.05 else ""
        print(f"{l['familia']:22} {l['comparacao']:38} perda {l['perda_total']:6.1f} × {l['perda_total_sbs']:5.1f}"
              f"  p {l['p']:.4f}  holm {l['p_holm']:.4f} {marca}")


if __name__ == "__main__":
    main()
