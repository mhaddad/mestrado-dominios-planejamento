"""Planejadores das IPCs 2011 e 2018 na taxonomia em 4 dimensões (Fase 4B).

Codificação feita em 27/09/2026 pelo Coordenador (Claude Code, claude-opus-5-5), por delegação do
autor, com as regras de docs/fase4b-desenho.md (P1 + G1 + G2) e o vocabulário de
auditoria/taxonomia-tecnicas.md e do EXP-13 (valores N1–N6). Fontes primárias: os resumos
oficiais de cada IPC.
  2011  booklet "The 2011 International Planning Competition — Description of Participating
        Planners — Deterministic Track" (García-Olaya, Jiménez e Linares López, jun. 2011),
        cópia do Internet Archive em brutos/2011/resumos/ (SHA-256 cca9e023…e69897); a coluna
        `fonte` dá a página.
  2018  resumos em https://ipc2018-classical.bitbucket.io/planner-abstracts/ (cópias em
        brutos/2018/resumos/), e a página da competição para as linhas de base.

Os planejadores que o EXP-13 já codificou (auditoria/taxonomia/planejadores_museu_4d.csv) são
copiados de lá, com a mesma codificação: LAMA 2011, Saarplan, Fast Downward Remix e
LAPKT-BFWS-Preference.

Valor novo (N7, fora do EXP-13): "Programação linear (potenciais, contagem de operadores)" na
D2, para as heurísticas de potenciais e de contagem de operadores do MSP.

Uma linha por valor. Planejadores com codificação diferente por trilha (DecStar, Mercury) têm
linhas separadas por trilha. D2 "não determinado" = a fonte lida não diz qual heurística usa.

Uso: python data/ipc-2011-2023/scripts/taxonomia_4d.py
Saída: data/ipc-2011-2023/planejadores_4d.csv
"""

import csv
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MUSEU = Path(__file__).resolve().parents[3] / "auditoria/taxonomia/planejadores_museu_4d.csv"
SAIDA = RAIZ / "planejadores_4d.csv"

PROG = "Busca progressiva no espaço de estados"
LOCAL = "Busca local"
SAT = "Compilação para SAT/CSP"
POP = "Busca no espaço de planos parciais"
DEC = "Decomposição/particionamento"
SIMB = "Busca simbólica (BDD)"
NOV = "Busca por largura/novidade"
DESAC = "Busca desacoplada (topologia em estrela)"
SEM = "Sem heurística"
REL = "Heurísticas de relaxação"
CG = "Grafo causal"
LM = "Landmarks"
ABS = "Abstrações / pattern databases"
RB = "Relaxação parcial (red-black)"
SATH = "Heurística de SAT para planejamento"
GC = "Contagem de metas"
LP = "Programação linear (potenciais, contagem de operadores)"
ND = "não determinado"
PROP = "Proposicional / STRIPS clássico"
CNF = "Proposicional traduzido em SAT/CNF"
MV = "Variáveis multivaloradas"
BDD = "Simbólica (BDD)"
UNICO = "Planejador único"
PORT = "Portfólio"
DECOMP = "Decomposição interna com planejador base fixo"

B11 = "booklet IPC 2011, p. {}"
R18 = "https://ipc2018-classical.bitbucket.io/planner-abstracts/{}"
TODAS = "todas"

# (edição, planejador, trilhas, D1, D2, D3, D4, tipo de portfólio, fonte, observação)
TABELA = [
    # ---------------- IPC 2011 ----------------
    ("2011", "LAMA-2011", TODAS, "museu:LAMA11", None, None, None, "", B11.format(51), "igual ao LAMA11 do EXP-13"),
    ("2011", "LAMA-2008", TODAS, "museu:LAMA08", None, None, None, "", B11.format(51), "igual ao LAMA08 do EXP-13"),
    ("2011", "FDSS-1", "seq-sat", [PROG], [REL, CG], [MV], [PORT], "fixo", B11.format("38–45, Tabela 2"),
     "componentes com tempo > 0: hFF, hadd, hCG, hcea; sem landmarks (corrige a suposição M2 do EXP-13 para esta versão)"),
    ("2011", "FDSS-2", "seq-sat", [PROG], [REL, CG], [MV], [PORT], "fixo", B11.format("38–45, Tabela 3"), "variante 2; mesmos tipos de componente"),
    ("2011", "FDSS-1", "seq-opt", [PROG], [LM, ABS], [MV], [PORT], "fixo", B11.format("38–45, Tabela 1"), "LM-cut, BJOLP e duas variantes de merge-and-shrink"),
    ("2011", "FDSS-2", "seq-opt", [PROG], [LM, ABS], [MV], [PORT], "fixo", B11.format("38–45"), "variante 2; mesmos tipos de componente [A CONFIRMAR] na tabela da variante"),
    ("2011", "FD-Autotune-1", "seq-sat", [PROG], [REL, CG, GC], [MV], [UNICO], "", B11.format("31–37, Tabelas 3–4"),
     "configuração do Fast Downward por ParamILS: hFF, hCG, hcea e contagem de metas habilitadas; EHC e busca preguiçosa"),
    ("2011", "FD-Autotune-2", "seq-sat", [PROG], [REL, CG, GC], [MV], [UNICO], "", B11.format("31–37, Tabelas 3–4"),
     "G1: fase inicial dentro da mesma execução (hFF), depois hadd, hCG, hcea e contagem de metas"),
    ("2011", "FD-Autotune", "seq-opt", [PROG], [REL, LM], [MV], [UNICO], "", B11.format("31–37, Tabela 2"), "A* com hmax e LM-cut habilitados"),
    ("2011", "Roamer", "seq-sat", [PROG, LOCAL], [REL, LM], [MV], [UNICO], "", B11.format(73), "base LAMA; passeios aleatórios para sair de platôs"),
    ("2011", "Fork Uniform", "seq-sat", [PROG], [ABS], [MV], [UNICO], "", B11.format(46), "WA* iterado com abstrações implícitas (forks)"),
    ("2011", "Probe", "seq-sat", [PROG], [REL, LM], [PROP], [UNICO], "", B11.format(71), "GBFS com hadd e sondas guiadas por landmarks"),
    ("2011", "Arvand", "seq-sat", [PROG, LOCAL], [REL], [MV], [UNICO], "", B11.format(15), "passeios aleatórios de Monte Carlo com hFF; base Fast Downward"),
    ("2011", "Lamar", "seq-sat", [PROG], [REL, LM], [MV], [UNICO], "", B11.format(55), "LAMA com hFF aleatorizado"),
    ("2011", "Randward", "seq-sat", [PROG], [REL], [MV], [UNICO], "", B11.format(55), "Fast Downward com hFF aleatorizado"),
    ("2011", "BRT", "seq-sat", [DEC, PROG], [LM], [MV], [DECOMP], "", B11.format(17),
     "árvore aleatória (RRT) com viés calculado a partir de landmarks; Fast Downward como planejador base (heurística do base não informada)"),
    ("2011", "CBP", "seq-sat", [PROG], [REL], [PROP], [UNICO], "", B11.format(21), "BFS com lookahead; grafo de planejamento relaxado com custos"),
    ("2011", "CBP2", "seq-sat", [PROG], [REL], [PROP], [UNICO], "", B11.format(21), "segunda versão: propagação aditiva de custos"),
    ("2011", "DAE-YAHSP", "seq-sat", [DEC, PROG], [REL], [PROP], [DECOMP], "", B11.format(29), "algoritmo evolutivo decompõe em submetas; YAHSP resolve cada uma"),
    ("2011", "YAHSP2", "seq-sat", [PROG], [REL], [PROP], [UNICO], "", B11.format(83), "lookahead a partir de planos relaxados"),
    ("2011", "YAHSP2-MT", "seq-sat", [PROG], [REL], [PROP], [UNICO], "", B11.format(83), "versão paralelizada do YAHSP2 (não é portfólio)"),
    ("2011", "LPRPG-P", "seq-sat", [PROG], [REL], [PROP], [UNICO], "", B11.format(58), "grafo de planejamento relaxado com programação linear para recursos"),
    ("2011", "Madagascar-p", "seq-sat", [SAT], [SATH], [CNF], [UNICO], "", B11.format(61), "Mp: heurística de SAT específica para planejamento (N3)"),
    ("2011", "Madagascar", "seq-sat", [SAT], [SEM], [CNF], [UNICO], "", B11.format(61), "M: sem a heurística específica do Mp"),
    ("2011", "POPF2", "seq-sat", [PROG, POP], [REL], [PROP], [UNICO], "", B11.format(65), "busca progressiva que expande planos de ordem parcial"),
    ("2011", "CPT4", TODAS, [POP, SAT], [ND], [PROP], [UNICO], "", B11.format(25), "planos parciais com propagação de restrições; heurística não descrita no resumo"),
    ("2011", "SATPLANLM-C", "seq-sat", [SAT], [SEM], [CNF], [UNICO], "", B11.format(77), "SatPlan com landmarks codificados como cláusulas (restrições, não heurística)"),
    ("2011", "Sharaabi", "seq-sat", [PROG], [ND], [PROP], [UNICO], "", B11.format(79), "planejador temporal derivado do DRIPS/SAPA"),
    ("2011", "ACOPlan", "seq-sat", [PROG], [REL], [PROP], [UNICO], "", B11.format(11), "colônia de formigas: construção estocástica progressiva com heurística de plano relaxado"),
    ("2011", "ACOPlan2", "seq-sat", [PROG], [REL], [PROP], [UNICO], "", B11.format(11), "mesmo algoritmo do ACOPlan, outra implementação"),
    ("2011", "Selective Max", "seq-opt", [PROG], [LM], [MV], [UNICO], "", B11.format(108), "escolhe por estado entre LM-cut e hLA numa única busca (G1)"),
    ("2011", "Merge and Shrink", "seq-opt", [PROG], [ABS], [MV], [PORT], "fixo", B11.format(106),
     "G1, área cinzenta: duas execuções separadas de A*, cada uma com uma estratégia de merge-and-shrink"),
    ("2011", "LM-cut", "seq-opt", [PROG], [LM], [MV], [UNICO], "", B11.format(103), "A* com LM-cut"),
    ("2011", "Fork Init", "seq-opt", [PROG], [ABS], [MV], [UNICO], "", B11.format(46), "A* com abstrações implícitas (forks)"),
    ("2011", "IFork Init", "seq-opt", [PROG], [ABS], [MV], [UNICO], "", B11.format(46), "A* com abstrações implícitas (forks invertidos)"),
    ("2011", "LMFork", "seq-opt", [PROG], [ABS, LM], [MV], [UNICO], "", B11.format(46), "LM-A* com forks sobre a tarefa enriquecida por landmarks"),
    ("2011", "BJOLP", "seq-opt", [PROG], [LM], [MV], [UNICO], "", B11.format(91), "LM-A* com heurística admissível de landmarks"),
    ("2011", "Gamer", "seq-opt", [SIMB], [ABS], [BDD], [UNICO], "", B11.format(96), "busca simbólica com PDBs simbólicos"),
    # ---------------- IPC 2018 ----------------
    ("2018", "lama11", TODAS, "museu:LAMA11", None, None, None, "", "https://ipc2018-classical.bitbucket.io/ (linhas de base)", "linha de base LAMA 2011; na agile, para no primeiro plano"),
    ("2018", "blind", "seq-opt", [PROG], [SEM], [MV], [UNICO], "", "https://ipc2018-classical.bitbucket.io/ (linhas de base)", "linha de base: A* com heurística cega"),
    ("2018", "sbd", "seq-opt", [SIMB], [SEM], [BDD], [UNICO], "", "https://ipc2018-classical.bitbucket.io/ (linhas de base)", "linha de base: busca simbólica bidirecional de custo uniforme"),
    ("2018", "Saarplan", TODAS, "museu:Saar", None, None, None, "fixo", R18.format("team7.pdf"), "igual ao EXP-13; tipo: sequência fixa (decoupled, grey planning, hCFF)"),
    ("2018", "Fast Downward Remix", TODAS, "museu:FDRemix", None, None, None, "fixo", R18.format("team43.pdf"), "igual ao EXP-13"),
    ("2018", "LAPKT-BFWS-Preference", TODAS, "museu:LAPKT", None, None, None, "", R18.format("teams_1_20_30_31_36_47.pdf"), "igual ao EXP-13"),
    ("2018", "Fast Downward Stone Soup 2018", "seq-sat", [PROG], [REL, CG, LM], [MV], [PORT], "fixo", R18.format("team45.pdf"),
     "componentes dos portfólios Cedalion, Stone Soup 2014 e Uniform e variantes do LAMA 2011 (mesma origem do FD Remix)"),
    ("2018", "fs-blind", TODAS, [NOV, PROG], [GC], [MV], [UNICO], "", R18.format("teams_1_20_30_31_36_47.pdf"), "BFWS com simulador (caixa-preta sobre o gerador de sucessores do Fast Downward)"),
    ("2018", "fs-sim", TODAS, [NOV, PROG], [GC], [MV], [UNICO], "", R18.format("teams_1_20_30_31_36_47.pdf"), "como o fs-blind, com informação de metas obtida por IW(1) e IW(2)"),
    ("2018", "LAPKT-DUAL-BFWS", TODAS, [NOV, PROG], [GC, LM, REL], [PROP], [UNICO], "", R18.format("teams_1_20_30_31_36_47.pdf"), "1-BFWS e, se falhar, BFWS(f6) com hL e hFF (G1: segunda fase)"),
    ("2018", "LAPKT-POLYNOMIAL-BFWS", TODAS, [NOV, PROG], [GC, REL], [PROP], [UNICO], "", R18.format("teams_1_20_30_31_36_47.pdf"), "k-BFWS(f5) polinomial"),
    ("2018", "LAPKT-DFS+", TODAS, [NOV, PROG], [GC, REL], [PROP], [UNICO], "", R18.format("teams_1_20_30_31_36_47.pdf"), "extensão do SIW+"),
    ("2018", "alien", TODAS, [NOV, PROG], [REL], [ND], [UNICO], "", R18.format("team33.pdf"), "quase o BFWS de Lipovetzky (2017) com hFF; representação não descrita"),
    ("2018", "DecStar", "seq-opt", [DESAC, PROG], [ABS, LM], [MV], [UNICO], "", R18.format("team2.pdf"),
     "busca desacoplada com busca explícita como alternativa (G1); PDB, LM-cut, merge-and-shrink e contagem de landmarks"),
    ("2018", "DecStar", "seq-sat,seq-agl", [DESAC, PROG], [REL, LM], [MV], [UNICO], "", R18.format("team2.pdf"), "busca desacoplada; hFF e configuração parecida com a do LAMA"),
    ("2018", "Symple-1", TODAS, [SIMB], [ND], [BDD], [UNICO], "", R18.format("teams_3_10.pdf"), "busca simbólica bidirecional com EVMDDs (diagramas de decisão)"),
    ("2018", "Symple-2", TODAS, [SIMB], [ND], [BDD], [UNICO], "", R18.format("teams_3_10.pdf"), "como o Symple-1, com outra tradução"),
    ("2018", "freelunch-madagascar", TODAS, [SAT], [SEM], [CNF], [UNICO], "", R18.format("teams_4_34.pdf"), "codificação do Madagascar e resolvedor SAT genérico (Lingeling)"),
    ("2018", "freelunch-doubly-relaxed", TODAS, [SAT, PROG], [ND], [CNF], [UNICO], "", R18.format("teams_4_34.pdf"),
     "tenta uma busca heurística simples antes da codificação em SAT (G1: fase dentro do mesmo sistema)"),
    ("2018", "mercury2014", "seq-sat", [PROG], [RB, LM], [MV], [UNICO], "", R18.format("team6.pdf"), "red-black e contagem de landmarks em filas alternadas"),
    ("2018", "mercury2014", "seq-agl", [PROG], [RB], [MV], [UNICO], "", R18.format("team6.pdf"), "na agile, só a heurística red-black"),
    ("2018", "MERWIN", TODAS, [NOV, PROG], [RB], [MV], [UNICO], "", R18.format("team14.pdf"), "novidade sobre a heurística red-black"),
    ("2018", "Cerberus", TODAS, [NOV, PROG], [RB, LM], [MV], [UNICO], "", R18.format("teams_15_16.pdf"), "red-black com efeitos condicionais, novidade e contagem de landmarks"),
    ("2018", "Cerberus-gl", TODAS, [NOV, PROG], [RB, LM], [MV], [UNICO], "", R18.format("teams_15_16.pdf"), "difere do Cerberus só na construção da tarefa red-black"),
    ("2018", "OLCFF", TODAS, [PROG], [RB, LM], [MV], [UNICO], "", R18.format("team8.pdf"), "hCFF (relaxação parcial, como no EXP-13) com EHC e fase tipo LAMA"),
    ("2018", "IBaCoP-2018", TODAS, [PROG, NOV, LOCAL], [REL, CG, LM, RB], [MV, PROP], [PORT], "fixo", R18.format("teams_18_35.pdf"),
     "seleção de Pareto: jasper, mercury, BFS(f), SIW, FDSS-2, probe, yahsp2-mt, lama-2011, lamar, arvand"),
    ("2018", "IBaCoP2-2018", TODAS, [PROG, NOV, LOCAL], [REL, CG, LM, RB], [MV, PROP], [PORT], "selecao", R18.format("teams_18_35.pdf"),
     "cinco planejadores escolhidos por tarefa por um modelo treinado sobre features da tarefa"),
    ("2018", "Delfi1", "seq-opt", [PROG, SIMB], [SEM, LM, ABS], [MV, BDD], [PORT], "selecao", R18.format("teams_23_24.pdf"),
     "17 planejadores (SymBA* e 16 A* do Fast Downward: cega, LM-cut, PDBs, merge-and-shrink); rede convolucional escolhe um por tarefa"),
    ("2018", "Delfi2", "seq-opt", [PROG, SIMB], [SEM, LM, ABS], [MV, BDD], [PORT], "selecao", R18.format("teams_23_24.pdf"), "difere do Delfi1 só na imagem da tarefa (aterrada)"),
    ("2018", "MSP", "seq-opt", [PROG, SIMB], [SEM, LM, ABS, LP], [MV, BDD], [PORT], "selecao", R18.format("team5.pdf"),
     "meta-busca por tarefa entre representações, FD ótimo (potenciais, contagem de operadores, iPDB, LM-cut, cega) e SymBA*; N7"),
    ("2018", "Complementary1", "seq-opt", [PROG], [ABS], [MV], [UNICO], "", R18.format("team9.pdf"), "A* com PDBs complementares"),
    ("2018", "Complementary2", "seq-opt", [PROG], [ABS], [MV], [UNICO], "", R18.format("team32.pdf"), "A* com PDBs simbólicos (CPC)"),
    ("2018", "Planning-PDBs", "seq-opt", [PROG], [ABS], [MV], [UNICO], "", R18.format("team40.pdf"), "variação do Complementary na seleção de padrões"),
    ("2018", "Scorpion", "seq-opt", [PROG], [ABS], [MV], [UNICO], "", R18.format("team44.pdf"), "abstrações combinadas por particionamento saturado de custos"),
    ("2018", "FDMS1", "seq-opt", [PROG], [ABS], [MV], [UNICO], "", R18.format("teams_26_27.pdf"), "A* com merge-and-shrink"),
    ("2018", "FDMS2", "seq-opt", [PROG], [ABS], [MV], [UNICO], "", R18.format("teams_26_27.pdf"), "A* com merge-and-shrink"),
    ("2018", "Metis1", "seq-opt", [PROG], [LM], [MV], [UNICO], "", R18.format("teams_21_22.pdf"), "A* com LM-cut, simetrias e redução de ordem parcial"),
    ("2018", "Metis2", "seq-opt", [PROG], [LM], [MV], [UNICO], "", R18.format("teams_21_22.pdf"), "máximo de LM-cut e heurística de landmarks"),
    ("2018", "maplan-1", "seq-opt", [PROG], [LM], [MV], [UNICO], "", R18.format("teams_13_17.pdf"), "A* com LM-cut e reduções por fam-groups"),
    ("2018", "maplan-2", "seq-opt", [PROG], [ABS], [MV], [UNICO], "", R18.format("teams_13_17.pdf"), "A* com abstração por fusão de fam-groups"),
]


def main():
    museu = {}
    for r in csv.DictReader(MUSEU.open(encoding="utf-8")):
        museu.setdefault(r["sigla"], {}).setdefault(r["dimensao"], []).append(r["valor"])
    linhas = []
    for ed, nome, trilhas, d1, d2, d3, d4, tipo, fonte, obs in TABELA:
        if isinstance(d1, str) and d1.startswith("museu:"):
            m = museu[d1.removeprefix("museu:")]
            d1, d2, d3, d4 = m["D1"], m.get("D2", [ND]), m.get("D3", [ND]), m["D4"]
            fonte = fonte + "; auditoria/taxonomia/planejadores_museu_4d.csv"
        for dim, valores in (("D1", d1), ("D2", d2), ("D3", d3), ("D4", d4)):
            for v in valores:
                linhas.append({"edicao": ed, "planejador": nome, "trilhas": trilhas, "dimensao": dim,
                               "valor": v, "portfolio_tipo": tipo if PORT in d4 else "",
                               "fonte": fonte, "observacao": obs})
    # Todo planejador dos resultados tem de estar codificado, em toda trilha em que aparece.
    codificados = {(l["edicao"], l["planejador"], t) for l in linhas
                   for t in (("seq-opt", "seq-sat", "seq-agl") if l["trilhas"] == TODAS else l["trilhas"].split(","))}
    faltam = set()
    for ed, arq in (("2011", "ipc2011_resultados.csv"), ("2018", "ipc2018_resultados.csv")):
        for r in csv.DictReader((RAIZ / arq).open(encoding="utf-8")):
            if (ed, r["planejador"], r["trilha"]) not in codificados:
                faltam.add((ed, r["planejador"], r["trilha"]))
    if faltam:
        raise SystemExit(f"planejadores sem codificação: {sorted(faltam)}")
    with SAIDA.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    entradas = {(l["edicao"], l["planejador"], l["trilhas"]) for l in linhas}
    port = {(l["edicao"], l["planejador"], l["portfolio_tipo"]) for l in linhas if l["portfolio_tipo"]}
    print(f"{len(entradas)} codificações ({len(linhas)} linhas); portfólios: {sorted(port)}")


if __name__ == "__main__":
    main()
