"""Método de 2010 com as notas do Nível 3 (EXP-05): dados de treino homogêneos.

Em 2010, as notas dos planejadores nos 10 domínios de treino misturavam resultados de
competições da IPC (34 pares) e execução própria (66 pares) (G9, G21). Aqui as notas vêm todas
da reexecução do Nível 3 (experimentos/analise/nivel3/resolvidos.csv), pela regra de 2010:
nota = porcentagem de problemas resolvidos ÷ 10, arredondada com o meio para cima (G6).
LPG-TD: mediana dos resolvidos nas 3 sementes. R × Pathways não rodou (G26): mantém-se a nota
de 2010 (0), marcada na saída.

O ranking real dos domínios de validação (Storage, Zeno-travel, Elevator) continua o de 2010
(data/2010/validacao_ranking.csv), por decisão do autor (27/09/2026).

Cenários (métodos e medidas de experimentos/analise/nivel2.py):
  notas-2010            referência do Nível 2 (notas publicadas, aritmética corrigida)
  notas-nivel3          notas do Nível 3; classes e taxonomias como na referência
  notas-nivel3-sat2010  idem, mas com as notas de 2010 no Satellite, cujo arquivo de domínio
                        de 2010 difere do usado no Nível 3 (G25)
  notas-nivel3-tabela4  notas do Nível 3, uma só atribuição de técnicas (Tabela 4, sem G24)
  notas-nivel3-4d       notas do Nível 3, taxonomia em 4 dimensões
  linha-de-base-2010 / linha-de-base-nivel3   média das notas de treino de cada planejador (G20)

Uso: python3 experimentos/analise/nivel3_metodo.py   (rode antes nivel3_resumo.py)
Saída: experimentos/analise/nivel3/notas.csv, cenarios.csv, rankings.csv e resumo na saída padrão.
"""
import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nivel2 as N  # noqa: E402
import reproducao_2010 as R  # noqa: E402

SAIDA = R.RAIZ / "experimentos/analise/nivel3"


def notas_nivel3():
    notas, marcas = {}, {}
    with (SAIDA / "resolvidos.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            pct = 100 * float(r["resolvidos_agora"]) / int(r["problemas"])
            notas[(r["dominio"], r["planejador"])] = int(R.meio_para_cima(pct / 10))
            marcas[(r["dominio"], r["planejador"])] = round(pct, 2)
    return notas, marcas


def main():
    metricas = R.ler("metricas_dominios.csv")
    ef2010 = {(r["dominio"], r["planejador"]): r for r in R.ler("eficiencia_planejadores.csv")}
    n2010 = {k: int(r["nota"]) for k, r in ef2010.items()}
    n3, pct3 = notas_nivel3()
    faltam = sorted(set(n2010) - set(n3))
    for k in faltam:
        n3[k] = n2010[k]
    sat2010 = {k: (n2010[k] if k[0] == "satellite" else v) for k, v in n3.items()}

    tecnicas = R.ler("planejadores_tecnicas.csv")
    tabela4 = N.conjunto(tecnicas)
    relacao_2010 = N.conjunto([r for r in tecnicas
                               if not (r["planejador"] == "IPP" and r["tecnica"] == "Forward-chaining")])
    t4d = N.taxonomia_4d()
    classes = N.classes_publicadas(metricas)
    observado, desempate = defaultdict(dict), defaultdict(dict)
    for r in R.ler("validacao_ranking.csv"):
        observado[r["dominio"]][r["planejador"]] = (int(r["posicao_real"]), float(r["nota_real"]))
        desempate[r["dominio"]][r["planejador"]] = int(r["posicao_proposta"])

    cenarios = {
        "notas-2010": (n2010, relacao_2010, tabela4),
        "notas-nivel3": (n3, relacao_2010, tabela4),
        "notas-nivel3-sat2010": (sat2010, relacao_2010, tabela4),
        "notas-nivel3-tabela4": (n3, tabela4, tabela4),
        "notas-nivel3-4d": (n3, t4d, t4d),
    }
    resumo, rankings = [], []

    def registrar(nome, previsto, diag):
        aval = N.avaliar(previsto, observado, desempate)
        rankings.extend({"cenario": nome, **a} for a in aval)
        resumo.append({"cenario": nome, **diag,
                       **{f"perda_{a['dominio']}": a["perda_vbs"] for a in aval},
                       **{f"acerto_{a['dominio']}": a["acerto_posicao_exata"] for a in aval},
                       **{f"spearman_{a['dominio']}": a["spearman"] for a in aval}})

    for nome, (notas, tec_rel, tec_pl) in cenarios.items():
        previsto, diag, _rel = N.metodo(classes, notas, tec_rel, tec_pl)
        registrar(nome, previsto, {"metricas_com_mais_de_uma_classe": diag["metricas_com_mais_de_uma_classe"]})
    for nome, notas in (("linha-de-base-2010", n2010), ("linha-de-base-nivel3", n3)):
        por = defaultdict(list)
        for (_d, p), n in notas.items():
            por[p].append(n)
        registrar(nome, {d: {p: statistics.mean(v) for p, v in por.items()} for d in N.VALIDACAO},
                  {"metricas_com_mais_de_uma_classe": ""})

    linhas_notas = [{"dominio": d, "planejador": p, "origem_2010": ef2010[(d, p)]["origem_do_dado"],
                     "eficiencia_2010_pct": ef2010[(d, p)]["eficiencia_completa_pct"], "nota_2010": n2010[(d, p)],
                     "eficiencia_nivel3_pct": pct3.get((d, p), ""), "nota_nivel3": n3[(d, p)],
                     "observacao": "sem execução no Nível 3; nota de 2010" if (d, p) in faltam else ""}
                    for (d, p) in sorted(n2010)]
    SAIDA.mkdir(parents=True, exist_ok=True)
    for arq, linhas in (("notas.csv", linhas_notas), ("cenarios.csv", resumo), ("rankings.csv", rankings)):
        with (SAIDA / arq).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)

    mudam = [l for l in linhas_notas if l["nota_2010"] != l["nota_nivel3"]]
    print(f"notas diferentes de 2010: {len(mudam)} de {len(linhas_notas)}", end="; ")
    for origem in ("competicao", "execucao_propria"):
        grupo = [l for l in linhas_notas if l["origem_2010"] == origem]
        dif = [abs(l["nota_2010"] - l["nota_nivel3"]) for l in grupo]
        print(f"{origem}: {sum(d > 0 for d in dif)} de {len(grupo)} mudam (média |Δ| {statistics.mean(dif):.2f})", end="; ")
    print()
    for r in resumo:
        print(r)


if __name__ == "__main__":
    main()
