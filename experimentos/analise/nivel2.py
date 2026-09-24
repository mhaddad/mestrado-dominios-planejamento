"""Nível 2 da reexecução (auditoria/reexecucao.md): correções sobre os dados de 2010.

Recalcula o método de 2010 inteiro (relação característica × técnica, notas por técnica e
por planejador nos domínios de validação, ranking, taxa de acerto) sob cenários de
correção, e compara cada cenário com a reprodução do Nível 1 (classes publicadas).

Cenários implementados:
  referencia            classes publicadas (o que 2010 calculou; Nível 1)
  texto-amostral        regra de discretização escrita no texto de 2010: Baixo <= v,
                        Médio <= 2v, Alto > 2v, com v = variância amostral dos 10 domínios
                        de treino (decisão do autor, 24/09/2026: aplicar como cenário)
  texto-populacional    idem, com variância populacional

Uso: python experimentos/analise/nivel2.py
Saída: experimentos/analise/nivel2/cenarios.csv, rankings.csv e resumo na saída padrão.
"""
import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reproducao_2010 as R  # noqa: E402

SAIDA = R.RAIZ / "experimentos/analise/nivel2"
VALIDACAO = ["storage", "zenotravel", "elevator"]


def classes_publicadas(metricas):
    return {(r["dominio"], r["metrica"]): r["classe"] for r in metricas}


def classes_texto(metricas, variancia):
    treino = defaultdict(list)
    for r in metricas:
        if r["papel"] == "treino":
            treino[r["metrica"]].append(R.num(r["valor"]))
    v = {m: variancia(vals) for m, vals in treino.items()}
    out = {}
    for r in metricas:
        x, c = R.num(r["valor"]), v[r["metrica"]]
        out[(r["dominio"], r["metrica"])] = "Baixo" if x <= c else "Médio" if x <= 2 * c else "Alto"
    return out


def conjunto(tecnicas):
    tec_de = defaultdict(set)
    for r in tecnicas:
        tec_de[r["planejador"]].add(r["tecnica"])
    return tec_de


def metodo(classes, notas, tec_relacao, tec_planejador):
    """O método de 2010 de ponta a ponta. `tec_relacao` é a atribuição de técnicas usada na
    relação característica × técnica; `tec_planejador`, a usada para compor a nota de cada
    planejador (em 2010 elas diferem no IPP, achado G24). Devolve notas previstas por
    planejador em cada domínio de validação e dados de diagnóstico."""
    tec_de = tec_relacao
    treino = {d for (d, _m) in classes} - set(VALIDACAO)
    # relação característica × técnica, arredondada para inteiro como nas Tabelas 19–20
    rel = {}
    for m in {m for (_d, m) in classes}:
        for c in ("Baixo", "Médio", "Alto"):
            doms = {d for d in treino if classes[(d, m)] == c}
            for t in {t for ts in tec_de.values() for t in ts}:
                vals = [n for (d, p), n in notas.items() if d in doms and t in tec_de[p]]
                if vals:
                    rel[(m, c, t)] = R.meio_para_cima(statistics.mean(vals))
    metricas_vivas = {m for (m, _c, _t) in rel
                      if len({c for (m2, c, _t) in rel if m2 == m}) > 1}
    previsto = {}
    for d in VALIDACAO:
        media_tec = {}
        for t in {t for ts in tec_de.values() for t in ts}:
            vals = [rel[(m, classes[(d, m)], t)] for m in {m for (_d, m) in classes}
                    if (m, classes[(d, m)], t) in rel]
            if vals:
                media_tec[t] = statistics.mean(vals)
        previsto[d] = {p: statistics.mean([media_tec[t] for t in ts if t in media_tec])
                       for p, ts in tec_planejador.items()}
    return previsto, {"metricas_com_mais_de_uma_classe": len(metricas_vivas),
                      "metricas_total": len({m for (_d, m) in classes})}


def avaliar(previsto, observado, desempate):
    """Mesmas medidas de auditoria/scripts/conferir_rankings.py. Como em 2010, as notas
    previstas são comparadas com duas casas decimais; empates seguem a ordem publicada em
    2010 (`desempate`), igual em todos os cenários."""
    linhas = []
    for d in VALIDACAO:
        prev = sorted(previsto[d], key=lambda p: (-round(previsto[d][p], 2), desempate[d][p]))
        obs = observado[d]
        ordem_obs = sorted(obs, key=lambda p: (-obs[p][1], obs[p][0]))  # nota real, desempate da tabela publicada
        exata = sum(a == b for a, b in zip(prev, ordem_obs)) / len(prev)
        top5 = len(set(prev[:5]) & set(ordem_obs[:5])) / 5
        pp = [previsto[d][p] for p in prev]
        po = [obs[p][1] for p in prev]
        linhas.append({"dominio": d, "acerto_posicao_exata": round(exata, 2), "top5": round(top5, 2),
                       "spearman": round(spearman(pp, po), 2), "ranking_previsto": " > ".join(prev)})
    return linhas


def postos(v):
    ordem = sorted(range(len(v)), key=lambda i: -v[i])
    r = [0.0] * len(v)
    i = 0
    while i < len(ordem):
        j = i
        while j + 1 < len(ordem) and v[ordem[j + 1]] == v[ordem[i]]:
            j += 1
        for k in range(i, j + 1):
            r[ordem[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(a, b):
    ra, rb = postos(a), postos(b)
    ma, mb = statistics.mean(ra), statistics.mean(rb)
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** 0.5
    return cov / den if den else float("nan")


def main():
    metricas = R.ler("metricas_dominios.csv")
    notas = {(r["dominio"], r["planejador"]): int(r["nota"]) for r in R.ler("eficiencia_planejadores.csv")}
    tecnicas = R.ler("planejadores_tecnicas.csv")
    observado, desempate = defaultdict(dict), defaultdict(dict)
    for r in R.ler("validacao_ranking.csv"):
        observado[r["dominio"]][r["planejador"]] = (int(r["posicao_real"]), float(r["nota_real"]))
        desempate[r["dominio"]][r["planejador"]] = int(r["posicao_proposta"])
    tabela4 = conjunto(tecnicas)
    relacao_2010 = conjunto([r for r in tecnicas  # G24: nas Tabelas 19–20, IPP fora de Forward-chaining
                             if not (r["planejador"] == "IPP" and r["tecnica"] == "Forward-chaining")])
    cenarios = {
        "referencia": classes_publicadas(metricas),
        "texto-amostral": classes_texto(metricas, statistics.variance),
        "texto-populacional": classes_texto(metricas, statistics.pvariance),
    }
    resumo, rankings = [], []
    for nome, classes in cenarios.items():
        previsto, diag = metodo(classes, notas, relacao_2010, tabela4)
        aval = avaliar(previsto, observado, desempate)
        for a in aval:
            rankings.append({"cenario": nome, **a})
        resumo.append({"cenario": nome, **diag,
                       **{f"acerto_{a['dominio']}": a["acerto_posicao_exata"] for a in aval},
                       **{f"spearman_{a['dominio']}": a["spearman"] for a in aval}})
    SAIDA.mkdir(parents=True, exist_ok=True)
    for arq, linhas in (("cenarios.csv", resumo), ("rankings.csv", rankings)):
        with (SAIDA / arq).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)
    for r in resumo:
        print(r)


if __name__ == "__main__":
    main()
