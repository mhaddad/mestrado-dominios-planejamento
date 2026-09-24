"""Calibra o limite de tempo da reexecução dos planejadores de 2010 (ação 19 do plano).

A emulação (QEMU i386 sobre Rosetta, no OrbStack) deixa os planejadores de 2010 mais lentos
que a máquina de 2010. Para cada planejador, este script roda uma amostra de problemas que ele
resolveu em 2010 levando entre 2 e 300 s, compara o tempo que o próprio planejador registra
agora com o de 2010 (experimentos/planejadores/tempos_2010.csv) e toma a mediana das razões
como fator de lentidão. O limite calibrado é 20 min × fator.

Uso, no macOS, a partir da raiz do repositório (depois de teste_2010.sh ter criado a cópia
de trabalho dos planejadores em ~/fase3/planners-2010):
  orb -m fase3-amd64 python3 experimentos/planejadores/calibrar_2010.py [paralelos]

Saídas (versionadas): experimentos/execucoes/calibracao-2010.csv e fatores-2010.csv.
Logs brutos: ~/fase3/calibracao-2010/ dentro da máquina.
"""
import csv
import math
import os
import re
import statistics
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tempos_planejadores as T  # noqa: E402

RAIZ = T.RAIZ
W = Path.home() / "fase3/planners-2010"
LOGS = Path.home() / "fase3/calibracao-2010"
FAIXA = (2.0, 300.0)   # tempos de 2010 usados na amostra (s)
POR_PLANEJADOR = 6
LIMITE_CAL = 3600      # teto de cada execução de calibração (s)
LIMITE_2010 = 1200     # limite de 2010 (s)

CHAVE = {"Blackbox": "blackbox", "IPP": "ipp", "FF": "ff", "LPG": "lpg", "YAHSP": "yahsp", "SGPlan": "sgplan",
         "SATPlan": "satplan", "MaxPlan": "maxplan", "Fast Downward": "fastdownward", "R": "r"}


def comando(pl, dom, prob):
    """(diretório, comando) com as chamadas dos scripts finais de 2010 (ver teste_2010.sh)."""
    d = T.COMP / dom
    D, P = str(d / "domain.pddl"), str(d / prob)
    return {
        "Blackbox": (W / "scripts/blackbox", ["./blackbox", "-o", D, "-f", P]),
        "IPP": (W / "scripts/ipp", ["./ipp", "-o", D, "-f", P]),
        "FF": (W / "scripts/ff", ["./ff", "-p", str(d) + "/", "-o", "domain.pddl", "-f", prob]),
        "LPG": (W / "scripts/lpg", ["./lpg-td-1.0", "-o", D, "-f", P, "-speed", "-noout"]),
        "YAHSP": (W / "scripts/yahsp", ["./yahsp", D, P]),
        "SGPlan": (W, ["./sgplan6", "-o", D, "-f", P]),
        "SATPlan": (W / "satplan", ["./satplan", "-domain", D, "-problem", P]),
        "MaxPlan": (W / "scripts/maxplan", ["./maxplan", "-o", D, "-f", P]),
        "Fast Downward": (W / "fastdownward", ["bash", "-c",
                          f"python2 translate/translate.py '{D}' '{P}' && ./preprocess/preprocess < output.sas"
                          " && ./search/search cCfF < output"]),
        "R": (W / "r", ["tclsh", "./r.execute", str(d), prob]),
    }[pl]


def tempo_agora(pl, cwd, saida, prob):
    """Tempo registrado pelo planejador nesta execução (mesma medida de 2010), ou None."""
    chave = CHAVE[pl]
    if chave in T.FORMATOS:
        _, ok, tempo = T.FORMATOS[chave]
        t = re.search(tempo, saida, re.I | re.M)
        return float(t.group(1)) if t and re.search(ok, saida, re.I | re.M) else None
    if chave in ("satplan", "maxplan"):
        solns = sorted(Path(cwd).glob("*.soln"), key=os.path.getmtime)
        if solns:
            t = re.search(r"^; Time\s+([\d.]+)", solns[-1].read_text(errors="replace"), re.M)
            return float(t.group(1)) if t else None
        return None
    if chave == "fastdownward":
        t = re.search(r"Total time:\s*([\d.]+)", saida)
        return float(t.group(1)) if t and "Solution found" in saida else None
    if chave == "r":
        for linha in saida.splitlines():
            p = linha.split(",")
            if len(p) > 3:
                return float(p[1])
    return None


def amostra():
    por = {}
    with (RAIZ / "experimentos/planejadores/tempos_2010.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            t = float(r["tempo_s_2010"])
            if FAIXA[0] <= t <= FAIXA[1]:
                por.setdefault(r["planejador"], []).append((t, r["dominio"], r["problema"]))
    sel = {}
    for pl, v in por.items():
        v.sort()
        k = min(POR_PLANEJADOR, len(v))
        idx = sorted({round(i * (len(v) - 1) / (k - 1)) for i in range(k)}) if k > 1 else [0]
        sel[pl] = [v[i] for i in idx]
    return sel


def roda_planejador(pl, casos):
    linhas = []
    for t2010, dom, prob in casos:
        cwd, cmd = comando(pl, dom, prob)
        for s in Path(cwd).glob("*.soln"):
            s.unlink()
        ini = time.time()
        # Grupo de processos próprio: no estouro, mata também os filhos (bash -c, Prolog do R).
        proc = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, errors="replace", start_new_session=True)
        try:
            saida, _ = proc.communicate(timeout=LIMITE_CAL)
            situacao = "ok"
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, 9)
            saida, _ = proc.communicate()
            situacao = "estourou"
        relogio = time.time() - ini
        (LOGS / f"{CHAVE[pl]}_{dom}_{prob}.log").write_text(saida)
        t = tempo_agora(pl, cwd, saida, prob) if situacao == "ok" else None
        if situacao == "ok" and t is None:
            situacao = "sem-plano"
        razao = t / t2010 if t else (LIMITE_CAL / t2010 if situacao == "estourou" else None)
        linhas.append({"planejador": pl, "dominio": dom, "problema": prob, "tempo_s_2010": t2010,
                       "tempo_s_agora": "" if t is None else round(t, 2), "relogio_s": round(relogio, 1),
                       "razao": "" if razao is None else round(razao, 2), "situacao": situacao})
        print(f"{pl:14} {dom:11} {prob:26} 2010={t2010:7.2f}  agora={t if t else '-':>8}  {situacao}", flush=True)
    return linhas


def main():
    paralelos = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    LOGS.mkdir(parents=True, exist_ok=True)
    sel = amostra()
    with ThreadPoolExecutor(max_workers=paralelos) as ex:
        resultados = [l for ls in ex.map(lambda kv: roda_planejador(*kv), sorted(sel.items())) for l in ls]
    saida = RAIZ / "experimentos/execucoes/calibracao-2010.csv"
    with saida.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(resultados[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(resultados)
    fatores = []
    for pl in sorted(sel):
        rs = [float(r["razao"]) for r in resultados if r["planejador"] == pl and r["razao"] != ""]
        validos = [r for r in resultados if r["planejador"] == pl and r["situacao"] == "ok"]
        fator = statistics.median(rs) if rs else None
        fatores.append({"planejador": pl, "n_amostra": len(sel[pl]), "n_resolvidos": len(validos),
                        "razao_min": round(min(rs), 2) if rs else "", "fator_mediana": round(fator, 2) if fator else "",
                        "razao_max": round(max(rs), 2) if rs else "",
                        "limite_calibrado_min": math.ceil(LIMITE_2010 * fator / 60) if fator else "",
                        "paralelos": paralelos})
    with (RAIZ / "experimentos/execucoes/fatores-2010.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(fatores[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(fatores)
    for x in fatores:
        print(x)


if __name__ == "__main__":
    main()
