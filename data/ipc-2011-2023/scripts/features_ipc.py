"""Features SAS+ das tarefas das IPCs 2011, 2014 e 2018, trilhas clássicas (Fase 4B).

Reaproveita o extrator da Fase 3 (experimentos/extratores/features_sas.py, R-26): tradutor do
Fast Downward release-26.6.0 e as mesmas features de tamanho, grafo causal e DTG. Nada é
recalculado aqui; o script só escolhe as tarefas e junta as saídas.

Tarefas:
  2011  trilhas seq-opt e seq-sat de experimentos/benchmarks/ipc/pddl-instances/ipc-2011
  2014  trilhas seq-opt, seq-sat e seq-agl de .../ipc-2014 (na ótima, sem as tarefas
        insolúveis, como no benchmarksV1.1.zip oficial)
  2018  as 24 pastas *-opt18-* e *-sat18-* do downward-benchmarks incluído no Planner Museum
        (experimentos/ferramentas/planner-museum/benchmarks/downward-benchmarks). A agile usou
        as tarefas da satisficing: os limites de custo ótimo por instância no `properties` das
        duas trilhas são idênticos fora do `-combined` (conferido em 27/09/2026). Caldera e
        organic-synthesis têm duas formulações (normal e split); o `-combined` do placar
        oficial não tem PDDL próprio.

Uso: python data/ipc-2011-2023/scripts/features_ipc.py [--limite SEGUNDOS] [--processos N]
Saída: data/ipc-2011-2023/features_sas_ipc.csv (uma linha por tarefa; `status` diz se o
tradutor terminou).
"""

import argparse
import csv
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "experimentos" / "extratores"))
import features_sas  # noqa: E402

SAIDA = Path(__file__).resolve().parent.parent / "features_sas_ipc.csv"
PDDL_INSTANCES = RAIZ / "experimentos/benchmarks/ipc/pddl-instances"
DOWNWARD = RAIZ / "experimentos/ferramentas/planner-museum/benchmarks/downward-benchmarks"
TRILHAS = {"sequential-optimal": "seq-opt", "sequential-satisficing": "seq-sat",
           "sequential-agile": "seq-agl"}


def tarefas():
    for edicao, trilhas in [("2011", ("seq-opt", "seq-sat")), ("2014", ("seq-opt", "seq-sat", "seq-agl"))]:
        for pasta in sorted((PDDL_INSTANCES / f"ipc-{edicao}" / "domains").iterdir()):
            sufixo = next((s for s in TRILHAS if pasta.name.endswith(s)), None)
            if not sufixo or TRILHAS[sufixo] not in trilhas:
                continue
            dominio = pasta.name.removesuffix("-" + sufixo)
            for prob in sorted((pasta / "instances").glob("instance-*.pddl"), key=lambda p: int(p.stem[9:])):
                n = int(prob.stem[9:])
                dom = pasta / "domains" / f"domain-{n}.pddl"
                yield edicao, TRILHAS[sufixo], dominio, prob.name, dom if dom.exists() else pasta / "domain.pddl", prob
    for pasta in sorted(DOWNWARD.glob("*18-*")):
        dominio, trilha = pasta.name.rsplit("-", 2)[0], "seq-opt" if "-opt18-" in pasta.name else "seq-sat"
        for prob in sorted(p for p in pasta.glob("*.pddl") if not p.name.startswith("domain")):
            dom = pasta / f"domain-{prob.name}"
            if not dom.exists():
                dom = pasta / f"domain_{prob.name}"
            yield "2018", trilha, dominio, prob.name, dom if dom.exists() else pasta / "domain.pddl", prob


def processar(args):
    edicao, trilha, dominio, problema, dom, prob, limite = args
    r = features_sas.processar((dominio, 0, dom, prob, limite))
    del r["dominio"], r["instancia"]
    return {"edicao": edicao, "trilha": trilha, "dominio": dominio, "problema": problema, **r}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limite", type=int, default=300)
    ap.add_argument("--processos", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    a = ap.parse_args()
    lista = [(*t, a.limite) for t in tarefas()]
    for t in lista:
        if not t[4].exists():
            raise SystemExit(f"domínio não encontrado: {t[4]}")
    print(f"{len(lista)} tarefas; {a.processos} processos; limite {a.limite} s por tradução", flush=True)
    with ProcessPoolExecutor(a.processos) as ex:
        linhas = list(ex.map(processar, lista, chunksize=1))
    campos = list(next(l for l in linhas if l["status"] == "ok"))
    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    contagem = {}
    for l in linhas:
        k = (l["edicao"], l["trilha"])
        ok, tot = contagem.get(k, (0, 0))
        contagem[k] = (ok + (l["status"] == "ok"), tot + 1)
    for k, (ok, tot) in sorted(contagem.items()):
        print(*k, f"{ok}/{tot} traduzidas")
    print(f"{len(linhas)} linhas -> {SAIDA.name}")


if __name__ == "__main__":
    main()
