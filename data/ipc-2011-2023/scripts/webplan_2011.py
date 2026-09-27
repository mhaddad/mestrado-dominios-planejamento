"""Resultados por instância da IPC 2011 a partir do arquivo do WebPlan (Fase 4B).

Os arquivos de resultados publicados pela IPC 2011 saíram do ar. O WebPlan
(Manuel Braun, 2012; https://web-plan.readthedocs.io) importou os resultados
da IPC 2011 para um banco Django e publicou o dump (`ipc.json`) no repositório
Mercurial `bitbucket.org/lohre/webplan_ipc_data`. O Bitbucket apagou os
repositórios Mercurial em 2020; o Software Heritage guardou uma cópia (visita
de 15/07/2020, revisão de 03/03/2012 "added database dump").

O dump tem, por problema (identificado por hash do conteúdo), os planos
válidos de cada planejador com o custo. Não tem tempo de execução nem motivo
de falha: um problema sem registro de um planejador é um problema que ele não
resolveu. Os problemas não resolvidos por ninguém também estão no dump.

Validação: o placar recalculado com a regra oficial de 2011 (custo do melhor
plano entre os participantes da trilha / custo do plano) tem de reproduzir a
ordem dos planejadores nas tabelas finais dos slides oficiais (p. 43 e 74),
e 9 planejadores da satisficing têm de superar o LAMA-2008 (coles2012survey).
A trilha multi-core não reproduz a ordem oficial e não é exportada.

Uso: python data/ipc-2011-2023/scripts/webplan_2011.py
Saídas: data/ipc-2011-2023/ipc2011_problemas.csv
        data/ipc-2011-2023/ipc2011_resultados.csv
"""

import collections
import csv
import json
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "brutos" / "2011" / "webplan"
SWH = "https://archive.softwareheritage.org/api/1/"
ORIGEM = "https://bitbucket.org/lohre/webplan_ipc_data"

DOMINIOS = ["barman", "elevators", "floortile", "nomystery", "openstacks", "parcprinter",
            "parking", "pegsol", "scanalyzer", "sokoban", "tidybot", "transport",
            "visitall", "woodworking"]
# Nome no dump -> nome oficial. Ordem = ordem das tabelas finais dos slides.
TRILHAS = {
    "seq-sat": [
        ("lama-2011", "LAMA-2011"), ("fdss-1_seq-sat", "FDSS-1"), ("fdss-2_seq-sat", "FDSS-2"),
        ("fd-autotune-1", "FD-Autotune-1"), ("roamer", "Roamer"), ("fd-autotune-2", "FD-Autotune-2"),
        ("forkuniform", "Fork Uniform"), ("probe", "Probe"), ("arvand", "Arvand"),
        ("lama-2008", "LAMA-2008"), ("lamar", "Lamar"), ("randward", "Randward"), ("brt", "BRT"),
        ("cbp2", "CBP2"), ("dae_yahsp_seq-sat", "DAE-YAHSP"), ("yahsp2_seq-sat", "YAHSP2"),
        ("yahsp2-mt_seq-sat", "YAHSP2-MT"), ("cbp", "CBP"), ("lprpgp", "LPRPG-P"),
        ("madagascar-p_seq-sat", "Madagascar-p"), ("popf2_seq-sat", "POPF2"),
        ("madagascar_seq-sat", "Madagascar"), ("cpt4_seq-sat", "CPT4"),
        ("satplanlm-c", "SATPLANLM-C"), ("sharaabi_seq-sat", "Sharaabi"),
        ("acoplan_seq-sat", "ACOPlan"), ("acoplan2", "ACOPlan2"),
    ],
    "seq-opt": [
        ("fdss-1_seq-opt", "FDSS-1"), ("fdss-2_seq-opt", "FDSS-2"), ("selmax", "Selective Max"),
        ("merge-and-shrink", "Merge and Shrink"), ("lmcut", "LM-cut"),
        ("fd-autotune", "FD-Autotune"), ("forkinit", "Fork Init"), ("bjolp", "BJOLP"),
        ("lmfork", "LMFork"), ("gamer", "Gamer"), ("iforkinit", "IFork Init"),
        ("cpt4_seq-opt", "CPT4"),
    ],
}


def swh(caminho):
    with urllib.request.urlopen(SWH + caminho) as r:
        return json.load(r)


def baixar_dump():
    destino = BRUTOS / "ipc.json"
    if not destino.exists():
        BRUTOS.mkdir(parents=True, exist_ok=True)
        visita = swh(f"origin/{ORIGEM}/visit/latest/?require_snapshot=true")
        snap = swh(f"snapshot/{visita['snapshot']}/")
        ramo = snap["branches"]["HEAD"]
        if ramo["target_type"] == "alias":
            ramo = snap["branches"][ramo["target"]]
        rev = swh(f"revision/{ramo['target']}/")
        raiz = swh(f"directory/{rev['directory']}/")
        alvo = next(e["target"] for e in raiz if e["name"] == "ipc.json")
        with urllib.request.urlopen(SWH + f"content/sha1_git:{alvo}/raw/") as r:
            destino.write_bytes(r.read())
        (BRUTOS / "PROVENIENCIA.txt").write_text(
            f"origem: {ORIGEM}\nvisita: {visita['date']}\nsnapshot: {visita['snapshot']}\n"
            f"revisao: {ramo['target']} ({rev['date']}, {rev['message'].strip()})\n"
            f"ipc.json: sha1_git {alvo}\n")
    return json.loads(destino.read_text())


def main():
    dump = baixar_dump()
    por_modelo = collections.defaultdict(list)
    for o in dump:
        por_modelo[o["model"]].append(o)
    upload = {o["pk"]: o["fields"]["name"] for o in por_modelo["app.resultupload"]}
    planejador = {o["pk"]: o["fields"]["name"] for o in por_modelo["app.planner"]}
    etiqueta = {o["pk"]: o["fields"]["name"] for o in por_modelo["app.tag"]}
    etiquetas = collections.defaultdict(set)
    numero = {}
    for o in por_modelo["app.tagtoproblem"]:
        f = o["fields"]
        etiquetas[f["problem"]].add(etiqueta[f["tag"]])
        if f["number"] is not None:
            numero[(f["problem"], etiqueta[f["tag"]])] = f["number"]

    problemas, resultados = [], []
    for trilha, lista in TRILHAS.items():
        nomes = dict(lista)
        dominio_de = {}
        for p, tags in etiquetas.items():
            ds = [d for d in DOMINIOS if f"{d} {trilha}" in tags]
            if len(ds) > 1:
                raise SystemExit(f"problema {p} com mais de um domínio em {trilha}: {ds}")
            if ds:
                dominio_de[p] = ds[0]
                problemas.append({"trilha": trilha, "dominio": ds[0], "problema": p,
                                  "numero": numero.get((p, f"{ds[0]} {trilha}"), "")})
        regs = [o["fields"] for o in por_modelo["app.problemresult"]
                if upload[o["fields"]["upload"]] == "ipc11" and planejador[o["fields"]["planner"]] in nomes]
        melhor = {}
        for r in regs:
            melhor[r["problem"]] = min(melhor.get(r["problem"], float(r["costs"])), float(r["costs"]))
        placar = collections.Counter()
        for r in regs:
            if r["problem"] not in dominio_de:
                raise SystemExit(f"resultado sem domínio de {trilha}: {r}")
            custo = float(r["costs"])
            nota = 1.0 if custo == 0 else melhor[r["problem"]] / custo
            n = planejador[r["planner"]]
            placar[n] += nota
            resultados.append({"trilha": trilha, "dominio": dominio_de[r["problem"]],
                               "problema": r["problem"], "planejador": nomes[n],
                               "planejador_webplan": n, "custo": r["costs"],
                               "melhor_custo_trilha": f"{melhor[r['problem']]:.4f}",
                               "nota_ipc2011": f"{nota:.4f}"})
        # Validação contra a ordem oficial (empates aceitos em qualquer ordem).
        ordem_oficial = [n for n, _ in lista]
        valores = [round(placar[n], 2) for n in ordem_oficial]
        if valores != sorted(valores, reverse=True):
            raise SystemExit(f"{trilha}: ordem recalculada não reproduz a oficial: {valores}")
        print(f"{trilha}: ordem oficial reproduzida ({len(lista)} planejadores); "
              + ", ".join(f"{nomes[n]} {placar[n]:.2f}" for n in ordem_oficial[:3]) + " ...")
        if trilha == "seq-sat":
            acima = sum(1 for n in ordem_oficial if placar[n] > placar["lama-2008"])
            assert acima == 9, acima
            print("seq-sat: 9 planejadores acima do LAMA-2008, como em coles2012survey")

    for nome, linhas in [("ipc2011_problemas.csv", problemas), ("ipc2011_resultados.csv", resultados)]:
        linhas.sort(key=lambda l: tuple(l.values()))
        with (RAIZ / nome).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)
        print(f"{len(linhas)} linhas -> {nome}")
    por_trilha = collections.Counter((p["trilha"], p["dominio"]) for p in problemas)
    assert set(por_trilha.values()) == {20}, por_trilha


if __name__ == "__main__":
    main()
