"""R-26 (auditoria/reexecucao.md): features modernas das tarefas de planejamento, extraídas da
representação SAS+ (variáveis multivaloradas) produzida pelo tradutor do Fast Downward.

Features por instância, escolhidas antes de rodar a partir das estruturas que a literatura liga
à complexidade das tarefas (síntese E2: grafo causal e DTG em Helmert, 2009; topologia de busca
e invertibilidade em Hoffmann, 2011; treewidth do grafo causal em Domshlak e Nazarenko, 2013):

  tamanho       variáveis, tamanho médio e máximo do domínio das variáveis, operadores,
                metas, axiomas
  grafo causal  arestas u -> v quando um operador que altera v tem u na pré-condição, na
                condição de efeito ou também altera u (definição de Helmert, 2006/2009);
                densidade, grau máximo, acíclico (sem contar laços), número de componentes
                fortemente conexas e fração de variáveis na maior; treewidth (limite
                superior pela heurística de grau mínimo, no grafo não dirigido)
  DTG           um grafo por variável (valores como nós; arco de pré-valor a pós-valor;
                pré-valor indefinido gera arcos de todos os outros valores); média de arcos
                por variável, fração de variáveis com DTG fortemente conexo e fração de arcos
                invertíveis (existe o arco de volta), aproximações da reversibilidade

Ajuste: no Pathways, os problemas redeclaram em :objects constantes que o domínio já declara, e
o tradutor recusa a duplicata. O problema é copiado sem esses nomes em :objects, o que não muda
a tarefa; a coluna `ajuste` registra cada caso.

Instâncias (--conjunto): `2010` = as mesmas de 2010 (faixa `instancias_usadas` de
data/2010/benchmarks_ipc_mapa_final.csv); `autoscale` = os 42 domínios × 30 instâncias do
Autoscale de custo unitário do Planner Museum (experimentos/ferramentas/planner-museum), as
mesmas da cobertura publicada em data/planner-museum/ (Nível 4). No Autoscale, o tamanho cresce
com o número da instância e as maiores levam minutos para traduzir; usa-se uma amostra fixa de
10 instâncias por domínio espalhadas pela escala (p01, p04, ..., p28).
Tradutor: Fast Downward release-26.6.0 em experimentos/ferramentas/downward (ver README.md).

Uso: python experimentos/extratores/features_sas.py [--conjunto 2010|autoscale] [--limite SEGUNDOS] [--processos N]
Requer networkx. Saídas: experimentos/extratores/features-sas/ (2010) ou features-sas-autoscale/,
com instancias.csv e dominios.csv (mediana por domínio).
"""
import argparse
import csv
import os
import statistics
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import networkx as nx
from networkx.algorithms.approximation import treewidth_min_degree

RAIZ = Path(__file__).resolve().parents[2]
BENCH = RAIZ / "experimentos/benchmarks/ipc/pddl-instances"
FD = RAIZ / "experimentos/ferramentas/downward/src/translate"
SAIDA = RAIZ / "experimentos/extratores/features-sas"
AUTOSCALE = RAIZ / "experimentos/ferramentas/planner-museum/benchmarks/autoscale-unit-cost"
DOMINIO_POR_INSTANCIA = {"pathways"}


def tarefas():
    for r in csv.DictReader((RAIZ / "data/2010/benchmarks_ipc_mapa_final.csv").open(encoding="utf-8")):
        a, b = map(int, r["instancias_usadas"].split("-"))
        pasta = BENCH / f"ipc-{r['ipc']}/domains/{r['variante_repositorio']}"
        for n in range(a, b + 1):
            dom = pasta / (f"domains/domain-{n}.pddl" if r["dominio"] in DOMINIO_POR_INSTANCIA else "domain.pddl")
            yield r["dominio"], n, dom, pasta / f"instances/instance-{n}.pddl"


def tarefas_autoscale():
    for pasta in sorted(p for p in AUTOSCALE.iterdir() if p.is_dir()):
        for n in range(1, 31, 3):
            prob = pasta / f"p{n:02d}.pddl"
            dom = pasta / f"domain-{prob.name}"
            yield pasta.name, int(prob.stem[1:]), dom if dom.exists() else pasta / "domain.pddl", prob


def ler_sas(texto):
    linhas = iter(texto.splitlines())
    variaveis, operadores, metas, axiomas = [], [], 0, 0
    for l in linhas:
        if l == "begin_variable":
            next(linhas); next(linhas)
            variaveis.append(int(next(linhas)))
        elif l == "begin_goal":
            metas = int(next(linhas))
        elif l == "begin_operator":
            next(linhas)
            prevail = [tuple(map(int, next(linhas).split())) for _ in range(int(next(linhas)))]
            efeitos = []
            for _ in range(int(next(linhas))):
                x = list(map(int, next(linhas).split()))
                nc = x[0]
                conds = [(x[1 + 2 * i], x[2 + 2 * i]) for i in range(nc)]
                var, pre, post = x[1 + 2 * nc:4 + 2 * nc]
                efeitos.append((conds, var, pre, post))
            operadores.append((prevail, efeitos))
        elif l == "begin_rule":
            axiomas += 1
    return variaveis, operadores, metas, axiomas


def features(variaveis, operadores, metas, axiomas):
    n = len(variaveis)
    cg = nx.DiGraph()
    cg.add_nodes_from(range(n))
    dtg = [nx.DiGraph() for _ in range(n)]
    for i, k in enumerate(variaveis):
        dtg[i].add_nodes_from(range(k))
    for prevail, efeitos in operadores:
        pre_vars = {v for v, _ in prevail} | {v for _c, v, p, _q in efeitos if p != -1}
        efe_vars = {v for _c, v, _p, _q in efeitos}
        for conds, v, pre, post in efeitos:
            for u in pre_vars | {c for c, _ in conds} | efe_vars:
                if u != v:
                    cg.add_edge(u, v)
            origens = [pre] if pre != -1 else [x for x in range(variaveis[v]) if x != post]
            for o in origens:
                if o != post:
                    dtg[v].add_edge(o, post)
    und = cg.to_undirected()
    tw = treewidth_min_degree(und)[0] if n else 0
    cfc = list(nx.strongly_connected_components(cg))
    arcos = [g.number_of_edges() for g in dtg]
    inv = sum(1 for g in dtg for u, v in g.edges if g.has_edge(v, u))
    return {
        "variaveis": n, "dominio_medio": round(statistics.mean(variaveis), 3) if n else 0,
        "dominio_max": max(variaveis, default=0), "operadores": len(operadores), "metas": metas,
        "axiomas": axiomas, "cg_arestas": cg.number_of_edges(),
        "cg_densidade": round(cg.number_of_edges() / (n * (n - 1)), 4) if n > 1 else 0,
        "cg_grau_max": max((d for _v, d in und.degree), default=0),
        "cg_aciclico": nx.is_directed_acyclic_graph(cg), "cg_cfc": len(cfc),
        "cg_maior_cfc_frac": round(max(len(c) for c in cfc) / n, 4) if n else 0,
        "cg_treewidth_sup": tw,
        "dtg_arcos_medio": round(statistics.mean(arcos), 3) if n else 0,
        "dtg_fortemente_conexo_frac": round(sum(nx.is_strongly_connected(g) for g in dtg if len(g)) / n, 4) if n else 0,
        "dtg_arcos_invertiveis_frac": round(inv / sum(arcos), 4) if sum(arcos) else 0,
    }


def sem_constantes_duplicadas(dom, prob, destino):
    """Copia o problema sem os objetos que já são constantes do domínio. Devolve quantos saíram."""
    import re
    import metricas_2010_pddl as X
    arvore = X.sexp(dom.read_text(encoding="utf-8", errors="replace"))
    const = {n for sec in arvore[2:] if isinstance(sec, list) and sec and sec[0] == ":constants"
             for n, _t in X.lista_tipada(sec[1:])}
    texto = prob.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"\(:objects(.*?)\)", texto, re.S | re.I)
    if not const or not m:
        return 0
    fichas = re.sub(r";[^\n]*", "", m.group(1)).split()
    saida, grupo, removidos = [], [], 0
    for f in fichas + ["-"]:  # agrupa "nomes - tipo"
        grupo.append(f)
        if len(grupo) >= 2 and grupo[-2] == "-":
            nomes = [x for x in grupo[:-2] if x.lower() not in const]
            removidos += len(grupo) - 2 - len(nomes)
            if nomes:
                saida += nomes + grupo[-2:]
            grupo = []
    resto = [x for x in grupo[:-1] if x.lower() not in const]
    removidos += len(grupo) - 1 - len(resto)
    saida += resto
    destino.write_text(texto[:m.start(1)] + " " + " ".join(saida) + texto[m.end(1):], encoding="utf-8")
    return removidos


def processar(args):
    dominio, n, dom, prob, limite = args
    base = {"dominio": dominio, "instancia": n}
    with tempfile.TemporaryDirectory() as tmp:
        sas = Path(tmp) / "output.sas"
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        copia = Path(tmp) / "problema.pddl"
        removidos = sem_constantes_duplicadas(dom, prob, copia)
        base["ajuste"] = f"{removidos} objetos que eram constantes do domínio retirados" if removidos else ""
        prob = copia if removidos else prob
        try:
            r = subprocess.run([sys.executable, "-m", "fast_downward.translate", str(dom), str(prob), "--sas-file", str(sas)],
                               cwd=tmp, env={**os.environ, "PYTHONPATH": str(FD)},
                               capture_output=True, text=True, timeout=limite)
        except subprocess.TimeoutExpired:
            return {**base, "status": f"tempo esgotado ({limite} s)"}
        if r.returncode != 0 or not sas.exists():
            return {**base, "status": f"falha do tradutor ({r.returncode})"}
        return {**base, "status": "ok", **features(*ler_sas(sas.read_text()))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--conjunto", choices=("2010", "autoscale"), default="2010")
    ap.add_argument("--limite", type=int, default=300)
    ap.add_argument("--processos", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    a = ap.parse_args()
    global SAIDA
    if a.conjunto == "autoscale":
        SAIDA = SAIDA.with_name("features-sas-autoscale")
    lista = [(*t, a.limite) for t in (tarefas() if a.conjunto == "2010" else tarefas_autoscale())]
    with ProcessPoolExecutor(a.processos) as ex:
        linhas = list(ex.map(processar, lista))
    campos = list(next(l for l in linhas if l["status"] == "ok"))
    SAIDA.mkdir(parents=True, exist_ok=True)
    with (SAIDA / "instancias.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    por_dom = {}
    for l in linhas:
        por_dom.setdefault(l["dominio"], []).append(l)
    resumo = []
    for d, ls in sorted(por_dom.items()):
        ok = [l for l in ls if l["status"] == "ok"]
        linha = {"dominio": d, "instancias": len(ls), "traduzidas": len(ok)}
        for c in campos[campos.index("status") + 1:]:
            vals = [float(l[c]) for l in ok]
            linha[c] = round(statistics.median(vals), 4) if vals else ""
        resumo.append(linha)
    with (SAIDA / "dominios.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(resumo[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(resumo)
    for r in resumo:
        print(r["dominio"], f"{r['traduzidas']}/{r['instancias']}")


if __name__ == "__main__":
    main()
