"""Parte descritiva do R-26: quanto as métricas UML de 2010 se sobrepõem às features SAS+?

Para cada métrica de 2010 (valores publicados com as correções aprovadas) e cada feature SAS+
(mediana por domínio, experimentos/extratores/features-sas/dominios.csv), calcula a correlação
de postos de Spearman nos 13 domínios. Não mede poder preditivo (isso é o R-27, que depende dos
dados de desempenho do Nível 4); mede redundância: uma métrica UML com correlação alta com
alguma feature SAS+ carrega informação que o PDDL já dá sem modelagem.

Com 13 domínios e 17 × 17 pares, correlações altas por acaso são esperadas; o resumo mostra só
a maior correlação absoluta de cada métrica e deve ser lido como exploratório. Para dar a
escala do acaso, o resumo traz também o percentil 95 da maior correlação absoluta quando os
valores da métrica são embaralhados entre os domínios (2.000 permutações, semente fixa).

Uso: python experimentos/analise/uml_x_sas.py
Saídas: experimentos/analise/uml-x-sas/{correlacoes.csv, resumo.csv}
"""
import csv
import random
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "experimentos/analise"))
import nivel2  # noqa: E402

SAIDA = RAIZ / "experimentos/analise/uml-x-sas"


def main():
    uml = {}
    for r in csv.DictReader((RAIZ / "data/2010/metricas_dominios.csv").open(encoding="utf-8")):
        uml.setdefault(r["metrica"], {})[r["dominio"]] = float(r["valor_corrigido"] or r["valor"])
    sas_linhas = list(csv.DictReader((RAIZ / "experimentos/extratores/features-sas/dominios.csv").open(encoding="utf-8")))
    feats = [c for c in sas_linhas[0] if c not in ("dominio", "instancias", "traduzidas")]
    sas = {f: {r["dominio"]: float(r[f]) for r in sas_linhas if r[f] != ""} for f in feats}
    corr, resumo = [], []
    rng = random.Random(2010)

    def maior_abs(vm):
        out = 0.0
        for vf in sas.values():
            doms = sorted(set(vm) & set(vf))
            rho = nivel2.spearman([vm[d] for d in doms], [vf[d] for d in doms])
            if rho == rho:
                out = max(out, abs(rho))
        return out

    for m, vm in uml.items():
        melhor = ("", 0.0)
        for f, vf in sas.items():
            doms = sorted(set(vm) & set(vf))
            rho = nivel2.spearman([vm[d] for d in doms], [vf[d] for d in doms])
            if rho != rho:  # feature constante
                continue
            corr.append({"metrica_uml": m, "feature_sas": f, "dominios": len(doms), "spearman": round(rho, 2)})
            if abs(rho) > abs(melhor[1]):
                melhor = (f, rho)
        doms, vals = list(vm), list(vm.values())
        nulos = []
        for _ in range(2000):
            rng.shuffle(vals)
            nulos.append(maior_abs(dict(zip(doms, vals))))
        nulos.sort()
        p = sum(x >= abs(melhor[1]) for x in nulos) / len(nulos)
        resumo.append({"metrica_uml": m, "feature_mais_correlacionada": melhor[0], "spearman": round(melhor[1], 2),
                       "acaso_p95": round(nulos[int(0.95 * len(nulos))], 2), "p_permutacao": round(p, 3)})
    SAIDA.mkdir(parents=True, exist_ok=True)
    for nome, linhas in (("correlacoes.csv", corr), ("resumo.csv", resumo)):
        with (SAIDA / nome).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)
    for r in sorted(resumo, key=lambda r: -abs(r["spearman"])):
        print(r)


if __name__ == "__main__":
    main()
