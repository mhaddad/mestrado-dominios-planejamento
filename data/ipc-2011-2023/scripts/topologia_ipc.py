"""Propriedades de topologia de busca das tarefas das IPCs (Fase 4B).

Aplica experimentos/extratores/topologia_sas.py (resultado básico de Hoffmann, 2011; fração de
transições inversíveis; hFF no estado inicial; taxa de becos sem saída e de sucesso da sondagem
em 10 estados amostrados) às mesmas tarefas de features_ipc.py. O extrator foi validado contra a
Tabela 3 de Hoffmann (2011): experimentos/extratores/topologia-validacao/.

Tarefas que o tradutor não conseguiu traduzir em features_sas_ipc.csv não são tentadas de novo.
Limites: 300 s para a tradução e 120 s para as medidas de cada tarefa (as amostras que não cabem
no tempo ficam de fora; status "parcial").

Incremental e retomável, como features_ipc.py: cada tarefa concluída vai para
topologia_ipc.parcial.csv, incorporado à saída no fim.

Uso: uv run --no-project --with numpy --with networkx python data/ipc-2011-2023/scripts/topologia_ipc.py [--edicoes 2011,2018] [--processos N]
Saída: data/ipc-2011-2023/topologia_ipc.csv
"""

import argparse
import csv
import os
import sys
import zlib
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(RAIZ / "experimentos" / "extratores"))
sys.path.insert(0, str(AQUI))
import features_ipc  # noqa: E402
import topologia_sas as T  # noqa: E402

DADOS = AQUI.parent
SAIDA = DADOS / "topologia_ipc.csv"
PARCIAL = SAIDA.with_suffix(".parcial.csv")
CAMPOS = ["edicao", "trilha", "dominio", "problema", "status", "variaveis", "operadores", "axiomas", "basico",
          "frac_inversiveis", "hff_s0", "hff_custo_s0", "amostras", "de_taxa", "sp_taxa", "sp_limite",
          "sp_dist_media", "tempo_s"]


def rodar(t):
    ed, tr, dom_nome, prob_nome, dom, prob = t
    base = {"edicao": ed, "trilha": tr, "dominio": dom_nome, "problema": prob_nome}
    txt, st = T.traduzir(dom, prob, 300)
    if txt is None:
        return {**base, "status": st}
    semente = zlib.crc32(f"{ed}/{tr}/{dom_nome}/{prob_nome}".encode())
    return {**base, **T.analisar(txt, amostras=10, semente=semente, limite_total_s=120.0)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edicoes", default="2011,2014,2018")
    ap.add_argument("--processos", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    a = ap.parse_args()
    chave = lambda x: tuple(x[:4]) if isinstance(x, tuple) else (x["edicao"], x["trilha"], x["dominio"], x["problema"])
    traduzidas = {chave(r) for r in csv.DictReader((DADOS / "features_sas_ipc.csv").open(encoding="utf-8"))
                  if r["status"] == "ok"}
    todas = [t for t in features_ipc.tarefas() if t[0] in a.edicoes.split(",") and chave(t) in traduzidas]
    feitas = {}
    for arq in (SAIDA, PARCIAL):
        if arq.exists():
            for r in csv.DictReader(arq.open(encoding="utf-8")):
                feitas[chave(r)] = r
    lista = [t for t in todas if chave(t) not in feitas]
    print(f"{len(todas)} tarefas; {len(todas) - len(lista)} já feitas; processando {len(lista)}", flush=True)
    novo = not PARCIAL.exists()
    with PARCIAL.open("a", newline="", encoding="utf-8") as fp, ProcessPoolExecutor(a.processos) as ex:
        w = csv.DictWriter(fp, fieldnames=CAMPOS, lineterminator="\n", extrasaction="ignore")
        if novo:
            w.writeheader()
        for f in as_completed([ex.submit(rodar, t) for t in lista]):
            r = f.result()
            feitas[chave(r)] = r
            w.writerow(r)
            fp.flush()
    linhas = sorted(feitas.values(), key=chave)
    with SAIDA.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)
    PARCIAL.unlink(missing_ok=True)
    cont = {}
    for r in linhas:
        k = (r["edicao"], r["trilha"], r["status"].split(" (")[0])
        cont[k] = cont.get(k, 0) + 1
    for k, v in sorted(cont.items()):
        print(*k, v)
    print(f"{len(linhas)} linhas -> {SAIDA.name}")


if __name__ == "__main__":
    main()
