"""Levantamento das fontes de resultados das IPCs 2011-2023 (Fase 4B, atividade 1).

Baixa o que está publicado on-line e conta execuções, planejadores, domínios e
limites. Não monta o dataset da Fase 4B; só confere o que cada fonte contém.

Fontes baixadas (para `../brutos/`, fora do Git):
- IPC 2018: resultados por instância das trilhas ótima, satisficing e agile
  (JSON do downward lab, `properties`).
- IPC 2023: `index.md` do site, com as tabelas por domínio das três trilhas.
- IBM/IPC-graph-data (Ferber et al., 2019): nomes dos problemas por partição.

IPC 2011 e 2014 não têm resultados por instância acessíveis (ver
docs/resultados-ipc-2011-2023.md); não entram aqui.

Uso: python data/ipc-2011-2023/scripts/levantar_fontes.py
Saída: data/ipc-2011-2023/resumo_fontes.csv
"""

import collections
import csv
import json
import re
import tarfile
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "brutos"
SAIDA = RAIZ / "resumo_fontes.csv"

URL_2018 = "https://ipc2018-classical.bitbucket.io/results/{trilha}-results.tar.bz2"
URL_2023 = (
    "https://raw.githubusercontent.com/ipc2023-classical/"
    "ipc2023-classical.github.io/master/index.md"
)
URL_IBM = (
    "https://raw.githubusercontent.com/IBM/IPC-graph-data/master/"
    "problems/problem-names-{particao}.txt"
)


def baixar(url, destino):
    if not destino.exists():
        destino.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, destino)
    return destino


def ipc2018():
    linhas = []
    for trilha in ["optimal", "satisficing", "agile"]:
        arq = baixar(URL_2018.format(trilha=trilha), BRUTOS / "2018" / f"{trilha}-results.tar.bz2")
        with tarfile.open(arq) as tar:
            props = json.load(tar.extractfile(f"{trilha}-results/properties"))
        execs = list(props.values())
        planejadores = {e["algorithm"] for e in execs}
        linhas_base = {p for p in planejadores if "baseline" in p}
        dominios = {e["domain"] for e in execs}
        variantes = {d for d in dominios if d.endswith(("-split", "-combined"))}
        limites = collections.Counter((e.get("time_limit"), e.get("memory_limit")) for e in execs)
        (tempo, memoria), _ = limites.most_common(1)[0]
        por_dom = collections.Counter(e["domain"] for e in execs if e["algorithm"] == min(planejadores))
        linhas.append({
            "edicao": 2018,
            "trilha": trilha,
            "granularidade": "instância",
            "execucoes": len(execs),
            "planejadores": len(planejadores) - len(linhas_base),
            "linhas_de_base": len(linhas_base),
            "dominios_com_variantes": len(dominios),
            "dominios_sem_variantes": len(dominios - variantes),
            "tarefas_por_dominio": "/".join(sorted({str(v) for v in por_dom.values()})),
            "limite_tempo_s": tempo,
            "limite_memoria_mib": memoria // 1024 if memoria else "",
            "execucoes_resolvidas": sum(1 for e in execs if e.get("coverage")),
        })
    return linhas


def ipc2023():
    texto = baixar(URL_2023, BRUTOS / "2023" / "index.md").read_text(encoding="utf-8")
    linhas = []
    # As três primeiras tabelas do index.md são os resultados das trilhas
    # ótima, satisficing e agile, nessa ordem.
    tabelas = re.findall(r"\n(\| *\|folding.*?)\n\n", texto, flags=re.S)
    for trilha, tabela in zip(["optimal", "satisficing", "agile"], tabelas[:3]):
        cab, _, *corpo = tabela.strip().splitlines()
        dominios = [c.strip() for c in cab.strip("|").split("|")][1:-1]
        nomes = [r.strip("|").split("|")[0].strip() for r in corpo]
        base = [n for n in nomes if n.startswith("baseline")]
        linhas.append({
            "edicao": 2023,
            "trilha": trilha,
            "granularidade": "domínio",
            "execucoes": "",
            "planejadores": len(nomes) - len(base),
            "linhas_de_base": len(base),
            "dominios_com_variantes": len(dominios),
            "dominios_sem_variantes": len(dominios),
            "tarefas_por_dominio": 20,
            "limite_tempo_s": 300 if trilha == "agile" else 1800,
            "limite_memoria_mib": 8192,
            "execucoes_resolvidas": "",
        })
    return linhas


def ibm2019():
    tarefas, dominios = 0, set()
    for particao in ["train", "valid", "test"]:
        arq = baixar(URL_IBM.format(particao=particao), BRUTOS / "ibm" / f"problem-names-{particao}.txt")
        for linha in arq.read_text().split("\n"):
            if linha.strip():
                tarefas += 1
                dominios.add(linha.split()[0])
    return [{
        "edicao": "1998-2018 (IBM)",
        "trilha": "optimal (portfólio do Delfi)",
        "granularidade": "instância",
        "execucoes": tarefas * 17,
        "planejadores": 17,
        "linhas_de_base": 0,
        "dominios_com_variantes": len(dominios),
        "dominios_sem_variantes": "",
        "tarefas_por_dominio": "variável",
        "limite_tempo_s": 1800,
        "limite_memoria_mib": "",
        "execucoes_resolvidas": "",
    }]


def main():
    linhas = ipc2018() + ipc2023() + ibm2019()
    with SAIDA.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    for l in linhas:
        print(l)


if __name__ == "__main__":
    main()
