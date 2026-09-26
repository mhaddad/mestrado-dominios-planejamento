"""R-16 (auditoria/reexecucao.md): robustez da discretização Baixo/Médio/Alto com mais domínios.

Pergunta: as classes que os 13 domínios de 2010 recebem mudam quando a população de
referência da discretização cresce? Em 2010, os limites vieram só dos 10 domínios de treino.

Como não há contagem UML para outros domínios, usam-se as 11 métricas extraídas do PDDL pelo
extrator do R-25 (experimentos/extratores/metricas_2010_pddl.py), nos 13 domínios e em até 20
domínios adicionais das IPCs 1998–2008 (18 depois da revisão abaixo). Regra de seleção dos adicionais, fixada antes de
rodar: uma variante por família de domínio que não esteja entre as 13, na edição mais antiga;
só variantes clássicas (sem ações durativas, fluentes numéricos, preferências nem
net-benefit), preferindo STRIPS a ADL e, em 2008, a trilha sequencial satisficing. Sem um
`domain.pddl` único, usa-se o domínio da primeira instância, como no Pathways.

Revisão da regra depois da primeira execução (registrada no EXP-10): várias variantes STRIPS
com domínio por instância são compilações aterradas (ações sem parâmetros; 96.942 no
Cyber Security), que não se comparam com modelos em nível de tipos. A variante passa a ser
aceita só se for *lifted* (no máximo metade das ações sem parâmetros); se não for, tenta-se a
próxima variante clássica da família, na ordem da lista. Família sem variante *lifted* fica de
fora.

Duas regras de discretização, as mesmas do Nível 2:
  extremos   a aplicada em 2010 (G23): o menor valor da população é Baixo, o maior é Alto;
  texto      a escrita no texto (EXP-04): Baixo <= v, Médio <= 2v, Alto > 2v, v = variância
             amostral da população.
Populações: "treino" (os 10 de 2010) e "ampliada" (os 10 + os adicionais aceitos).

Uso: python experimentos/analise/robustez_discretizacao.py
Saídas: experimentos/analise/robustez-discretizacao/{dominios-adicionais.csv, classes.csv, resumo.csv}
"""
import csv
import re
import statistics
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "experimentos/extratores"))
import metricas_2010_pddl as X  # noqa: E402

SAIDA = RAIZ / "experimentos/analise/robustez-discretizacao"
ADICIONAIS = [  # (família, edição, variantes candidatas em ordem de preferência)
    ("grid", 1998, ["grid-round-2-strips"]),
    ("movie", 1998, ["movie-round-1-strips"]),
    ("mystery-prime", 1998, ["mystery-prime-round-1-strips"]),
    ("assembly", 1998, ["assembly-round-1-adl"]),
    ("freecell", 2000, ["freecell-strips-typed"]),
    ("schedule", 2000, ["schedule-adl-typed"]),
    ("rovers", 2002, ["rovers-strips-automatic"]),
    ("airport", 2004, ["airport-nontemporal-strips", "airport-nontemporal-adl"]),
    ("promela-dining-philosophers", 2004, ["promela-dining-philosophers-strips", "promela-dining-philosophers-adl"]),
    ("promela-optical-telegraph", 2004, ["promela-optical-telegraph-strips", "promela-optical-telegraph-adl"]),
    ("psr", 2004, ["psr-small-strips", "psr-middle-compiled-adl"]),
    ("openstacks", 2006, ["openstacks-propositional-strips", "openstacks-propositional"]),
    ("trucks", 2006, ["trucks-propositional-strips", "trucks-propositional"]),
    ("cyber-security", 2008, ["cyber-security-sequential-satisficing-strips"]),
    ("parc-printer", 2008, ["parc-printer-sequential-satisficing-strips"]),
    ("peg-solitaire", 2008, ["peg-solitaire-sequential-satisficing-strips"]),
    ("scanalyzer", 2008, ["scanalyzer-3d-sequential-satisficing-strips"]),
    ("sokoban", 2008, ["sokoban-sequential-satisficing-strips"]),
    ("transport", 2008, ["transport-sequential-satisficing-strips"]),
    ("woodworking", 2008, ["woodworking-sequential-satisficing-strips"]),
]


def lifted(d):
    return sum(1 for a in d["acoes"] if not a["parametros"]) <= len(d["acoes"]) / 2


def arquivo_dominio(pasta):
    if (pasta / "domain.pddl").exists():
        return pasta / "domain.pddl"
    arqs = sorted((pasta / "domains").glob("*.pddl"), key=lambda p: [int(n) for n in re.findall(r"\d+", p.name)])
    return arqs[0]


def extremos(v, pop):
    lo, hi = min(pop), max(pop)
    return "Baixo" if v <= lo else "Alto" if v >= hi else "Médio"


def texto(v, pop):
    c = statistics.variance(pop)
    return "Baixo" if v <= c else "Médio" if v <= 2 * c else "Alto"


def main():
    mapa = {r["dominio"]: r for r in csv.DictReader((RAIZ / "data/2010/benchmarks_ipc_mapa_final.csv").open(encoding="utf-8"))}
    papel = {r["dominio"]: r["papel"] for r in csv.DictReader((RAIZ / "data/2010/metricas_dominios.csv").open(encoding="utf-8"))}
    valores, dominios_ad = {}, []
    for dom, r in mapa.items():
        pasta = X.BENCH / f"ipc-{r['ipc']}/domains/{r['variante_repositorio']}"
        valores[dom] = X.metricas(X.ler_dominio(pasta / X.ARQUIVO_DOMINIO.get(dom, "domain.pddl")))
    for fam, ano, variantes in ADICIONAIS:
        recusadas = []
        for var in variantes:
            arq = arquivo_dominio(X.BENCH / f"ipc-{ano}/domains/{var}")
            d = X.ler_dominio(arq)
            if lifted(d):
                valores[fam] = X.metricas(d)
                dominios_ad.append({"familia": fam, "ipc": ano, "variante": var, "arquivo": str(arq.relative_to(X.BENCH)),
                                    "variantes_recusadas_aterradas": " ".join(recusadas), **valores[fam]})
                break
            recusadas.append(var)
        else:
            dominios_ad.append({"familia": fam, "ipc": ano, "variante": "", "arquivo": "",
                                "variantes_recusadas_aterradas": " ".join(recusadas),
                                **{k: "" for k in valores["blocksworld"]}})
    treino = [d for d in mapa if papel[d] == "treino"]
    ampliada = treino + [f for f, _a, _v in ADICIONAIS if f in valores]
    print(f"população ampliada: {len(ampliada)} domínios ({len(ampliada) - len(treino)} adicionais)")

    classes, resumo = [], []
    for m in valores[treino[0]]:
        linha = {"metrica": m}
        for regra, f in (("extremos", extremos), ("texto", texto)):
            pops = {"treino": [float(valores[d][m]) for d in treino],
                    "ampliada": [float(valores[d][m]) for d in ampliada]}
            c = {p: {d: f(float(valores[d][m]), pop) for d in mapa} for p, pop in pops.items()}
            for d in sorted(mapa):
                classes.append({"metrica": m, "regra": regra, "dominio": d, "valor": valores[d][m],
                                "classe_treino": c["treino"][d], "classe_ampliada": c["ampliada"][d]})
            linha[f"{regra}_mudam"] = sum(c["treino"][d] != c["ampliada"][d] for d in mapa)
            linha[f"{regra}_classes_distintas_treino"] = len(set(c["treino"].values()))
            linha[f"{regra}_classes_distintas_ampliada"] = len(set(c["ampliada"].values()))
        resumo.append(linha)

    SAIDA.mkdir(parents=True, exist_ok=True)
    for nome, linhas in (("dominios-adicionais.csv", dominios_ad), ("classes.csv", classes), ("resumo.csv", resumo)):
        with (SAIDA / nome).open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(linhas[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)
    for r in resumo:
        print(r)
    tot = len(resumo) * len(mapa)
    print(f"extremos: {sum(r['extremos_mudam'] for r in resumo)} de {tot} classes mudam; "
          f"texto: {sum(r['texto_mudam'] for r in resumo)} de {tot}")


if __name__ == "__main__":
    main()
