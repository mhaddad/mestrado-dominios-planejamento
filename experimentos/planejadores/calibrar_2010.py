"""Calibra o limite de tempo da reexecução dos planejadores de 2010 (ação 19 do plano).

A emulação (QEMU i386 sobre Rosetta, no OrbStack) deixa os planejadores de 2010 mais lentos
que a máquina de 2010. Para cada planejador, este script roda uma amostra de problemas que ele
resolveu em 2010 levando entre 2 e 300 s, compara o tempo que o próprio planejador registra
agora com o de 2010 (experimentos/planejadores/tempos_2010.csv) e toma a mediana das razões
como fator de lentidão. O limite calibrado é 20 min × fator.

Uso, no macOS, a partir da raiz do repositório (depois de teste_2010.sh ter criado a cópia
de trabalho dos planejadores em ~/fase3/planners-2010):
  orb -m fase3-amd64 python3 experimentos/planejadores/calibrar_2010.py [paralelos]
  python3 experimentos/planejadores/calibrar_2010.py --resumir   (refaz os fatores a partir do CSV)

Critério do fator: o limite de 2010 (`timeout 1200`) cortava o tempo de relógio, então o fator
é a mediana de (tempo de relógio agora / tempo registrado em 2010). Casos cujo tempo de 2010,
depois de corrigida a leitura, fica fora da faixa da amostra são excluídos. Planejadores
estocásticos (LPG-TD) não têm fator próprio confiável: recebem a mediana dos fatores dos
planejadores determinísticos, porque o custo da emulação é do ambiente, não do planejador.

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


# Planejadores cujos scripts de 2010 no TPP usam tpp/Strips/ (o FF usava o binário ff2, que não
# está no acervo; aqui roda o ff). Os demais usaram a raiz ou não têm script de TPP em 2010.
STRIPS_TPP = {"Blackbox", "IPP", "LPG", "YAHSP", "FF"}


def comando(pl, dom, prob, base=None):
    """(diretório, comando) com as chamadas dos scripts finais de 2010 (ver teste_2010.sh).
    `base` troca a cópia de trabalho dos planejadores (uma por processo paralelo)."""
    W = base or globals()["W"]
    d = T.COMP / dom
    dominio = "domain.pddl"
    if dom == "pathways":
        # Pathways não tem domain.pddl: cada problema tem o seu domínio em Strips/, e os
        # scripts de 2010 usam Strips/domain_pNN.pddl com Strips/pNN.pddl (os arquivos da
        # raiz são outra versão). O R espera domain.pddl no diretório: fica para a decisão do R.
        d, dominio = d / "Strips", f"domain_{prob}"
    if dom == "tpp" and pl in STRIPS_TPP:
        # TPP: a raiz tem a versão Propositional da IPC 5 (tipos em hierarquia, que o Blackbox
        # não lê); em 2010 estes planejadores usaram as versões instanciadas de Strips/.
        d, dominio = d / "Strips", f"domain_{prob}"
    D, P = str(d / dominio), str(d / prob)
    return {
        "Blackbox": (W / "scripts/blackbox", ["./blackbox", "-o", D, "-f", P]),
        "IPP": (W / "scripts/ipp", ["./ipp", "-o", D, "-f", P]),
        "FF": (W / "scripts/ff", ["./ff", "-p", str(d) + "/", "-o", dominio, "-f", prob]),
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
        return T.segundos(t.group(1)) if t and re.search(ok, saida, re.I | re.M) else None
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
        # Linha de resultado do R: problema,tempo,100,(ação),(ação),...  Outras linhas com
        # vírgulas (ex.: exceção do Prolog que lista o plano parcial) não são resultado.
        t = re.search(r"^[^,\s]+,([\d.]+),\d+,\(", saida, re.M)
        return float(t.group(1)) if t else None
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
    global SAIDA_CAL, SAIDA_FAT
    paralelos = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    sufixo = sys.argv[2] if len(sys.argv) > 2 else ""  # ex.: "-gcp", para não sobrescrever a calibração do OrbStack
    SAIDA_CAL = RAIZ / f"experimentos/execucoes/calibracao-2010{sufixo}.csv"
    SAIDA_FAT = RAIZ / f"experimentos/execucoes/fatores-2010{sufixo}.csv"
    LOGS.mkdir(parents=True, exist_ok=True)
    sel = amostra()
    with ThreadPoolExecutor(max_workers=paralelos) as ex:
        resultados = [l for ls in ex.map(lambda kv: roda_planejador(*kv), sorted(sel.items())) for l in ls]
    with SAIDA_CAL.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(resultados[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(resultados)
    resumir(paralelos, sufixo)


ESTOCASTICOS = {"LPG"}


def resumir(paralelos=4, sufixo=""):
    with (RAIZ / f"experimentos/execucoes/calibracao-2010{sufixo}.csv").open(encoding="utf-8") as f:
        resultados = list(csv.DictReader(f))
    t2010 = {}
    with (RAIZ / "experimentos/planejadores/tempos_2010.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            t2010[(r["planejador"], r["dominio"], r["problema"])] = float(r["tempo_s_2010"])
    fatores, deterministicos = [], []
    for pl in sorted({r["planejador"] for r in resultados}):
        rs = []
        for r in resultados:
            if r["planejador"] != pl:
                continue
            t = t2010.get((pl, r["dominio"], r["problema"]), float(r["tempo_s_2010"]))
            if not FAIXA[0] <= t <= FAIXA[1]:
                continue  # fora da faixa depois de corrigida a leitura do tempo de 2010
            rs.append(float(r["relogio_s"]) / t)
        fator = statistics.median(rs) if rs else None
        if pl not in ESTOCASTICOS and fator:
            deterministicos.append(fator)
        fatores.append({"planejador": pl, "n_usados": len(rs),
                        "n_resolvidos": sum(r["planejador"] == pl and r["situacao"] == "ok" for r in resultados),
                        "razao_min": round(min(rs), 2) if rs else "", "fator_proprio": round(fator, 2) if fator else "",
                        "razao_max": round(max(rs), 2) if rs else "", "paralelos": paralelos})
    comum = statistics.median(deterministicos)
    for x in fatores:
        usado = comum if x["planejador"] in ESTOCASTICOS else float(x["fator_proprio"])
        x["fator_usado"] = round(usado, 2)
        x["origem_do_fator"] = "mediana dos determinísticos" if x["planejador"] in ESTOCASTICOS else "próprio"
        x["limite_calibrado_min"] = math.ceil(LIMITE_2010 * usado / 60)
    with (RAIZ / f"experimentos/execucoes/fatores-2010{sufixo}.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(fatores[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(fatores)
    for x in fatores:
        print(x)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--resumir"]:
        resumir(sufixo=sys.argv[2] if len(sys.argv) > 2 else "")
    else:
        main()
