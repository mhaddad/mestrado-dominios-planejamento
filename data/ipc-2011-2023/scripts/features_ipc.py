"""Features SAS+ das tarefas das IPCs 2011, 2014, 2018 e 2023, trilhas clássicas (Fase 4B).

Reaproveita o extrator da Fase 3 (experimentos/extratores/features_sas.py, R-26): tradutor do
Fast Downward release-26.6.0 e as mesmas features de tamanho, grafo causal e DTG. Nada é
recalculado aqui; o script só escolhe as tarefas e junta as saídas.

Tarefas:
  2011  as 28 pastas *-opt11-* e *-sat11-* do downward-benchmarks incluído no Planner Museum
        (experimentos/ferramentas/planner-museum/benchmarks/downward-benchmarks). Os arquivos
        conferem por SHA-1 com os do WebPlan (webplan_2011_arquivos.py). O pddl-instances,
        usado na primeira versão, tem na pasta do floortile ótimo de 2011 uma cópia da
        satisficing (conferido em 27/09/2026) e foi abandonado aqui.
  2014  trilhas seq-opt, seq-sat e seq-agl do benchmarksV1.1.zip oficial (brutos/2014/),
        extraído para brutos/2014/benchmarksV1.1/ (na ótima, sem as tarefas insolúveis).
  2018  as 24 pastas *-opt18-* e *-sat18-* do mesmo downward-benchmarks. A agile usou
        as tarefas da satisficing: os limites de custo ótimo por instância no `properties` das
        duas trilhas são idênticos fora do `-combined` (conferido em 27/09/2026). Caldera e
        organic-synthesis têm duas formulações (normal e split); o `-combined` do placar
        oficial não tem PDDL próprio.
  2023  as 14 pastas *-opt23-* e *-sat23-* do mesmo downward-benchmarks (7 domínios). A agile
        de 2023 usou as tarefas da satisficing `[A CONFIRMAR]`.

Incremental e retomável: as tarefas com status ok na saída (ou no arquivo parcial de uma
execução interrompida) são mantidas, e só as que faltam ou falharam são processadas, com o
limite da execução corrente. Cada tarefa concluída é gravada na hora em
features_sas_ipc.parcial.csv, que é incorporado à saída no fim. Execuções de 27/09/2026:
2011, 2014 e 2018 com 300 s; depois 2023 e as falhas de 2018 com 1.800 s, o limite de tempo
da própria competição.

Uso: python data/ipc-2011-2023/scripts/features_ipc.py [--limite SEGUNDOS] [--processos N] [--pular-falhas] [--edicoes 2018,...]
Saída: data/ipc-2011-2023/features_sas_ipc.csv (uma linha por tarefa; `status` diz se o
tradutor terminou).
"""

import argparse
import csv
import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "experimentos" / "extratores"))
import features_sas  # noqa: E402

SAIDA = Path(__file__).resolve().parent.parent / "features_sas_ipc.csv"
PARCIAL = SAIDA.with_suffix(".parcial.csv")
DOWNWARD = RAIZ / "experimentos/ferramentas/planner-museum/benchmarks/downward-benchmarks"
ZIP2014 = Path(__file__).resolve().parent.parent / "brutos" / "2014" / "benchmarksV1.1.zip"
PDDL2014 = ZIP2014.with_suffix("")


def tarefas():
    if not PDDL2014.exists():
        import zipfile
        zipfile.ZipFile(ZIP2014).extractall(PDDL2014)
    for trilha in ("seq-agl", "seq-opt", "seq-sat"):
        for pasta in sorted((PDDL2014 / "TESTING" / trilha).iterdir()):
            for prob in sorted(p for p in pasta.glob("*.pddl") if not p.name.startswith("domain")):
                dom = pasta / f"domain_{prob.name}"
                yield "2014", trilha, pasta.name.lower(), prob.name, dom if dom.exists() else pasta / "domain.pddl", prob
    for pasta in sorted([*DOWNWARD.glob("*-opt11-*"), *DOWNWARD.glob("*-sat11-*"),
                         *DOWNWARD.glob("*-opt18-*"), *DOWNWARD.glob("*-sat18-*"),
                         *DOWNWARD.glob("*-opt23-*"), *DOWNWARD.glob("*-sat23-*")]):
        edicao = {"11": "2011", "18": "2018", "23": "2023"}[pasta.name.rsplit("-", 2)[1][3:]]
        dominio, trilha = pasta.name.rsplit("-", 2)[0], "seq-opt" if "-opt" in pasta.name else "seq-sat"
        for prob in sorted(p for p in pasta.glob("*.pddl")
                           if not p.name.startswith("domain") and not p.stem.endswith("-domain")):
            candidatos = [pasta / f"domain-{prob.name}", pasta / f"domain_{prob.name}",
                          pasta / f"{prob.stem}-domain.pddl"]
            dom = next((d for d in candidatos if d.exists()), pasta / "domain.pddl")
            yield edicao, trilha, dominio, prob.name, dom, prob


def processar(args):
    edicao, trilha, dominio, problema, dom, prob, limite = args
    r = features_sas.processar((dominio, 0, dom, prob, limite))
    del r["dominio"], r["instancia"]
    return {"edicao": edicao, "trilha": trilha, "dominio": dominio, "problema": problema, **r}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limite", type=int, default=300)
    ap.add_argument("--processos", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    ap.add_argument("--pular-falhas", action="store_true", help="não tenta de novo as que já falharam")
    ap.add_argument("--edicoes", default="2011,2014,2018,2023", help="edições a processar nesta execução")
    a = ap.parse_args()
    chave = lambda l: (l[0], l[1], l[2], l[3]) if isinstance(l, tuple) else (l["edicao"], l["trilha"], l["dominio"], l["problema"])
    todas = list(tarefas())
    for t in todas:
        if not t[4].exists():
            raise SystemExit(f"domínio não encontrado: {t[4]}")
    anteriores = {}
    for arq in (SAIDA, PARCIAL):
        if arq.exists():
            for l in csv.DictReader(arq.open(encoding="utf-8")):
                if l["status"] == "ok" or chave(l) not in anteriores:
                    anteriores[chave(l)] = l
    prontas = {k: l for k, l in anteriores.items() if l["status"] == "ok"}
    # Tarefas nunca tentadas primeiro; as que já falharam (em geral, as mais pesadas) no fim.
    lista = sorted(((*t, a.limite) for t in todas if chave(t) not in prontas
                    and not (a.pular_falhas and chave(t) in anteriores)
                    and t[0] in a.edicoes.split(",")),
                   key=lambda t: chave(t) in anteriores)
    print(f"{len(todas)} tarefas, {len(prontas)} já traduzidas; processando {len(lista)} com "
          f"{a.processos} processos e limite de {a.limite} s", flush=True)
    campos = ["edicao", "trilha", "dominio", "problema", "ajuste", "status"] + list(features_sas.features([2], [], 1, 0))
    novas = {}
    novo_parcial = not PARCIAL.exists()
    with PARCIAL.open("a", newline="", encoding="utf-8") as fp, ProcessPoolExecutor(a.processos) as ex:
        wp = csv.DictWriter(fp, fieldnames=campos, lineterminator="\n")
        if novo_parcial:
            wp.writeheader()
        for fut in as_completed([ex.submit(processar, t) for t in lista]):
            l = fut.result()
            novas[chave(l)] = l
            wp.writerow(l)
            fp.flush()
    linhas = [prontas.get(chave(t)) or novas.get(chave(t)) or anteriores[chave(t)] for t in todas]
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
    PARCIAL.unlink(missing_ok=True)
    print(f"{len(linhas)} linhas -> {SAIDA.name}")


if __name__ == "__main__":
    main()
