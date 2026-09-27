"""Resumo do Nível 3 (EXP-05): problemas resolvidos por planejador e domínio, agora × 2010.

Entrada: experimentos/execucoes/nivel3-2010-gcp.csv (rodada no GCP) e
data/2010/problemas_resolvidos.csv (contagens de 2010).
LPG-TD (3 sementes): conta-se a mediana dos resolvidos nas sementes e também os problemas
resolvidos em ao menos uma semente.

Uso: python3 experimentos/analise/nivel3_resumo.py
Saída: experimentos/analise/nivel3/resolvidos.csv e resumo na saída padrão.
"""
import csv
import statistics
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ENTRADA = RAIZ / "experimentos/execucoes/nivel3-2010-gcp.csv"
SAIDA = RAIZ / "experimentos/analise/nivel3"
NOME_2010 = {"sattelite": "satellite", "logistic": "logistics"}  # pastas do acervo -> nomes de data/2010


def main():
    execucoes = list(csv.DictReader(ENTRADA.open(encoding="utf-8")))
    em_2010 = {(r["dominio"], r["planejador"]): r for r in csv.DictReader(
        (RAIZ / "data/2010/problemas_resolvidos.csv").open(encoding="utf-8"))}
    por = defaultdict(lambda: defaultdict(set))   # (pl, dom) -> semente -> problemas resolvidos
    problemas = defaultdict(set)
    situacoes = defaultdict(lambda: defaultdict(int))
    for r in execucoes:
        chave = (r["planejador"], r["dominio"])
        problemas[chave].add(r["problema"])
        situacoes[chave][r["situacao"]] += 1
        por[chave][r["semente"]]  # garante a semente mesmo sem resolvidos
        if r["situacao"] == "resolvido":
            por[chave][r["semente"]].add(r["problema"])
    linhas = []
    for (pl, dom), sementes in sorted(por.items()):
        contagens = [len(s) for s in sementes.values()]
        ref = em_2010.get((NOME_2010.get(dom, dom), pl), {})
        linhas.append({
            "planejador": pl, "dominio": NOME_2010.get(dom, dom), "problemas": len(problemas[(pl, dom)]),
            "resolvidos_agora": statistics.median(contagens),
            "resolvidos_alguma_semente": len(set().union(*sementes.values())),
            "estourou": situacoes[(pl, dom)]["estourou"], "sem_plano": situacoes[(pl, dom)]["sem-plano"],
            "resolvidos_2010": ref.get("resolvidos", ""),
            "celula_vazia_2010": ref.get("celula_vazia", ""),
        })
    SAIDA.mkdir(parents=True, exist_ok=True)
    with (SAIDA / "resolvidos.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    tot = defaultdict(int)
    for r in execucoes:
        tot[r["situacao"]] += 1
    print(f"execuções: {len(execucoes)}; " + ", ".join(f"{k}: {v}" for k, v in sorted(tot.items())))
    comparaveis = [l for l in linhas if l["celula_vazia_2010"] == "False"]
    iguais = sum(float(l["resolvidos_agora"]) == float(l["resolvidos_2010"]) for l in comparaveis)
    mais = sum(float(l["resolvidos_agora"]) > float(l["resolvidos_2010"]) for l in comparaveis)
    menos = sum(float(l["resolvidos_agora"]) < float(l["resolvidos_2010"]) for l in comparaveis)
    print(f"pares com valor de 2010: {len(comparaveis)}; iguais: {iguais}; mais agora: {mais}; menos agora: {menos}")
    for l in comparaveis:
        if float(l["resolvidos_agora"]) != float(l["resolvidos_2010"]):
            print(f"  {l['planejador']:14} {l['dominio']:12} agora {l['resolvidos_agora']:>5} × 2010 {l['resolvidos_2010']:>3}"
                  f"  (de {l['problemas']}; estourou {l['estourou']}, sem plano {l['sem_plano']})")


if __name__ == "__main__":
    main()
