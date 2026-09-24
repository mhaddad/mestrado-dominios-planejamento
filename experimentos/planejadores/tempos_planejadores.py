"""Extrai, dos logs dos planejadores, o tempo que cada um registrou por problema resolvido.

Serve para os logs de 2010 (acervo) e para os de agora (mesmos planejadores, mesma saída).
O tempo é o que o próprio planejador imprime (não o tempo de relógio), para comparar a
mesma medida nas duas épocas. Só biblioteca padrão: roda no Mac e na máquina da Fase 3.

Uso:
  python3 experimentos/planejadores/tempos_planejadores.py 2010
      -> grava experimentos/planejadores/tempos_2010.csv a partir do acervo
"""
import csv
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
COMP = RAIZ / "acervo-2010/planejadores_analise_resultados/comp"
LOGS_2010 = COMP / "planners/resultados"
SCRIPTS_2010 = COMP / "planners/scripts"

# Nome do domínio nos arquivos de log -> pasta do domínio no acervo
PASTA = {"blocksworld": "blocksworld", "blockswolrd": "blocksworld", "depots": "depots", "depot": "depots",
         "driverlog": "driverlog", "gripper": "gripper", "logistic": "logistic", "logistics": "logistic",
         "mystery": "mystery", "pathway": "pathways", "pathways": "pathways", "pipesworld": "pipesworld",
         "satellite": "sattelite", "sattelite": "sattelite", "tpp": "tpp", "storage": "storage"}
PLANEJADOR = {"blackbox": "Blackbox", "ipp": "IPP", "ff": "FF", "lpg": "LPG", "yahsp": "YAHSP",
              "sgplan": "SGPlan", "satplan": "SATPlan", "maxplan": "MaxPlan", "fastdownward": "Fast Downward",
              "r": "R"}


def mapa_problemas(pasta: str) -> dict:
    """Nome do problema (minúsculas) -> arquivo, lendo '(problem NOME)' de cada PDDL da pasta."""
    mapa = {}
    d = COMP / pasta
    for f in sorted(d.iterdir()):
        if not f.is_file() or f.name == "domain.pddl":
            continue
        m = re.search(r"\(\s*problem\s+([^\s)]+)", f.read_text(errors="replace"), re.I)
        if m:
            nome = m.group(1).lower()
            mapa[nome] = None if nome in mapa else f.name  # None = nome repetido (ambíguo)
    return mapa


def blocos(texto: str, marca: str):
    """Divide o log em blocos que começam na linha que casa com `marca` (grupo 1 = nome)."""
    ms = list(re.finditer(marca, texto, re.I | re.M))
    for i, m in enumerate(ms):
        fim = ms[i + 1].start() if i + 1 < len(ms) else len(texto)
        yield m.group(1).strip().lower(), texto[m.start():fim]


# planejador -> (marca do início do problema, marca de sucesso, expressão do tempo)
FORMATOS = {
    "blackbox": (r"^Problem name:\s*(\S+)", r"Begin plan", r"Total elapsed time:\s*([\d.]+)"),
    "ipp": (r"problem '([^']+)' defined", r"found plan", r"([\d.]+) seconds total time"),
    "ff": (r"problem '([^']+)' defined", r"found legal plan", r"([\d.]+) seconds total time"),
    "lpg": (r"problem '([^']+)' defined", r"Solution found", r"^Total time:\s*([\d.]+)"),
    "yahsp": (r"Parsing problem\.+\s*([^.\s]+)", r"Valid plan", r"Total time\s*:\s*([\d.]+)"),
    "sgplan": (r"problem '([^']+)' defined", r"^; Time", r"^; Time\s+([\d.]+)"),
}


def ordem_script(stem: str, pasta: str) -> list:
    """Problemas na ordem em que o script de 2010 de mesmo nome do log os executou."""
    for cand in list(SCRIPTS_2010.glob(f"*/{stem}.sh")) + list((COMP / "planners").glob(f"{stem}.sh~")):
        probs = []
        for linha in cand.read_text(errors="replace").splitlines():
            if linha.lstrip().startswith("#") or "domain.pddl" not in linha and "r.execute" not in linha:
                continue
            m = re.search(r"-(?:f|problem)\s+(\S+)", linha) or re.search(r"r\.execute\s+\S+\s+(\S+)", linha) \
                or re.search(r"(\S+)\s*$", linha)
            probs.append(os.path.basename(m.group(1)).rstrip(";"))
        if probs:
            return probs
    return []


def ler_log(planejador: str, texto: str, mapa: dict, ordem=None):
    """Pares (arquivo do problema, tempo) dos problemas resolvidos num log.

    Se `ordem` (problemas na ordem do script) tem o mesmo tamanho que o número de blocos
    do log, o i-ésimo bloco é o i-ésimo problema; senão, casa pelo nome do problema e
    descarta nomes repetidos no domínio (ambíguos).
    """
    if planejador in FORMATOS:
        inicio, ok, tempo = FORMATOS[planejador]
        bs = list(blocos(texto, inicio))
        usar_ordem = bool(ordem) and len(ordem) == len(bs)
        for i, (nome, bloco) in enumerate(bs):
            t = re.search(tempo, bloco, re.I | re.M)
            if not (re.search(ok, bloco, re.I | re.M) and t):
                continue
            if usar_ordem:
                yield ordem[i], float(t.group(1))
            elif nome in mapa and mapa[nome] is not None:
                yield mapa[nome], float(t.group(1))
    elif planejador == "r":
        for linha in texto.splitlines():
            p = linha.split(",")
            if len(p) > 3 and mapa.get(p[0].lower()):
                yield mapa[p[0].lower()], float(p[1])


def tempos_2010():
    linhas = []
    for pl in ["blackbox", "ipp", "ff", "lpg", "yahsp", "sgplan", "r"]:
        for log in sorted((LOGS_2010 / pl).glob("*.log")):
            dom = PASTA[re.sub(r"^[^_]+_", "", log.stem)]
            for arq, t in ler_log(pl, log.read_text(errors="replace"), mapa_problemas(dom), ordem_script(log.stem, dom)):
                linhas.append((PLANEJADOR[pl], dom, arq, t))
    for pl in ["satplan", "maxplan"]:  # um .soln por problema resolvido
        for dpasta in sorted(p for p in (LOGS_2010 / pl).iterdir() if p.is_dir()):
            dom = PASTA[dpasta.name]
            for soln in sorted(dpasta.glob("*.soln")):
                t = re.search(r"^; Time\s+([\d.]+)", soln.read_text(errors="replace"), re.M)
                if t:
                    linhas.append((PLANEJADOR[pl], dom, soln.stem, float(t.group(1))))
    for log in sorted((LOGS_2010 / "fastdownward").glob("*.log")):  # "Problema N" na ordem do script
        dom = PASTA[re.sub(r"^[^_]+_", "", log.stem)]
        script = SCRIPTS_2010 / "fastdownward" / f"{log.stem}.sh"
        ordem = [os.path.basename(m) for m in re.findall(r"translate\.py\s+\S+\s+(\S+)", script.read_text())]
        for num, bloco in blocos(log.read_text(errors="replace"), r"Problema\s+(\d+)"):
            t = re.search(r"Total time:\s*([\d.]+)", bloco)
            if re.search(r"Solution found", bloco) and t and int(num) <= len(ordem):
                linhas.append(("Fast Downward", dom, ordem[int(num) - 1], float(t.group(1))))
    return sorted(set(linhas))


if __name__ == "__main__":
    if sys.argv[1:] == ["2010"]:
        saida = RAIZ / "experimentos/planejadores/tempos_2010.csv"
        linhas = tempos_2010()
        with saida.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["planejador", "dominio", "problema", "tempo_s_2010"])
            w.writerows(linhas)
        from collections import Counter
        print(f"{len(linhas)} tempos -> {saida.relative_to(RAIZ)}")
        for pl, n in sorted(Counter(l[0] for l in linhas).items()):
            print(f"  {pl}: {n}")
    else:
        sys.exit(__doc__)
