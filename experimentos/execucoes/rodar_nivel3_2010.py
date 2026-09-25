r"""Nível 3 da reexecução: os 10 planejadores de 2010 nos 10 domínios de treino, sob condições únicas.

Condições (decisões registradas no plano, ações 6 e 19):
- máquina OrbStack `fase3-amd64` (Ubuntu 22.04 amd64; binários de 2010 via QEMU i386);
- as chamadas dos scripts finais de 2010 (ver experimentos/planejadores/calibrar_2010.py);
- limite de tempo calibrado por planejador (experimentos/execucoes/fatores-2010.csv), sobre o
  tempo de relógio, com o grupo de processos morto no estouro;
- 4 execuções em paralelo, a mesma concorrência da calibração;
- LPG-TD com 3 sementes fixas (1, 2, 3), por ser estocástico;
- limites internos do LPG-TD (-cputime 1800 e -cputime_localsearch 1200), do MAXPLAN
  (-timeout 1800), do SGPlan (-cputime) e do SATPlan (-globaltime, em minutos) igualados ao
  limite calibrado: em 2010 nunca agiam; paradas por esses limites contam como "estourou";
- os problemas do acervo (subconjuntos de 2010, achado G14; Gripper gerado localmente, G15).

Retoma de onde parou: pula as execuções já registradas em experimentos/execucoes/nivel3-2010.csv.
Ordem: domínio por domínio, para cada domínio terminado já ser comparável com 2010.

Opções:
  --paralelos N   execuções simultâneas (padrão 4, a concorrência da calibração no OrbStack)
  --fatores F     limites calibrados do ambiente (padrão experimentos/execucoes/fatores-2010.csv)
  --resultados F  CSV de saída (padrão experimentos/execucoes/nivel3-2010.csv); use um
                  arquivo por ambiente para não misturar condições de medição
  --por-ultimo P  agenda esses planejadores depois de todos os outros (ex.: R)
  --adiar P1,P2   não agenda esses planejadores nesta rodada (decisão do autor, 24/09/2026:
                  o R fica para o fim, a decidir depois de todos os outros)
  --variante V    roda só as execuções da variante V (ver VARIANTES), com a chamada alterada;
                  use um --resultados próprio. blackbox-m8192: Blackbox no Satellite com
                  `-M 8192`, como nos logs de 2010 (achado G25; decisão do autor, 25/09/2026)
Parada suave: crie ~/fase3/nivel3/PARAR; o executor não inicia novas execuções, termina as
que estão em curso e sai. Apague o arquivo antes de reiniciar.

Uso, dentro da máquina (em segundo plano, independente da sessão):
  orb -m fase3-amd64 bash -c "cd <repo> && nohup python3 experimentos/execucoes/rodar_nivel3_2010.py \
      > ~/fase3/nivel3/execucao.log 2>&1 &"
Saídas brutas (log e plano de cada execução): ~/fase3/nivel3/brutos/ (não versionadas).
Para parar: `pkill` pelo nome não pega os processos emulados; mate pelo número:
  orb -m fase3-amd64 bash -c 'kill -9 $(ps -eo pid,args | grep -E "rodar_nivel3|qemu-i386|r.execute|/usr/bin/time" \
      | grep -v grep | awk "{print \$1}")'
e confira que nada sobrou antes de reiniciar (execuções órfãs disputam CPU e diretórios).
O Mac não pode dormir durante a rodada: `caffeinate -i` não impede o sono ao fechar a tampa,
e uma execução que atravessa o sono tem tempo de relógio e limite distorcidos (25/09/2026:
três execuções descartadas). Antes de retomar, impeça o sono (ex.: `sudo pmset -a
disablesleep 1`, revertido com `sudo pmset -a disablesleep 0`) ou mantenha a tampa aberta.
"""
import csv
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "experimentos/planejadores"))
import calibrar_2010 as C  # noqa: E402
import tempos_planejadores as T  # noqa: E402

BASE = Path.home() / "fase3"
MODELO = BASE / "planners-2010"
BRUTOS = BASE / "nivel3/brutos"
PARAR = BASE / "nivel3/PARAR"
RESULTADOS = RAIZ / "experimentos/execucoes/nivel3-2010.csv"
PARALELOS = 4
SEMENTES_LPG = (1, 2, 3)
ORDEM_DOMINIOS = ["driverlog", "gripper", "sattelite", "depots", "logistic", "blocksworld",
                  "mystery", "tpp", "pathways", "pipesworld"]
PLANEJADORES = ["Blackbox", "IPP", "FF", "LPG", "YAHSP", "SGPlan", "SATPlan", "MaxPlan", "Fast Downward", "R"]
CAMPOS = ["planejador", "dominio", "problema", "semente", "situacao", "tempo_relogio_s", "tempo_planejador_s",
          "memoria_max_kb", "limite_s", "inicio", "slot"]
trava = threading.Lock()
# Mensagens com que os planejadores param pelo próprio limite de tempo
LIMITE_INTERNO = re.compile(r"Program Timeout|Max cpu time exceeded|Solver runs with time out", re.I)
slots_livres = []
# Variantes de chamada: (planejador, domínio) -> opções acrescentadas à chamada dos scripts finais
VARIANTES = {"blackbox-m8192": {("Blackbox", "sattelite"): ["-M", "8192"]}}
variante = {}


def preparar_slots():
    """Uma cópia dos planejadores por processo paralelo, com os caminhos do R ajustados."""
    for i in range(PARALELOS):
        w = BASE / f"slots/w{i}"
        if not w.exists():
            shutil.copytree(MODELO, w, symlinks=True)
        r = w / "r/r.execute"
        texto = r.read_text()
        texto = re.sub(r"^set PL .*$", f"set PL {w}/r/pl-3.2.9/src/pl", texto, flags=re.M)
        texto = re.sub(r"^set BIN .*$", f"set BIN {w}/r/bin", texto, flags=re.M)
        r.write_text(texto)
        slots_livres.append(w)


def problemas(dom):
    d = T.COMP / dom
    return sorted(f.name for f in d.iterdir()
                  if f.is_file() and f.name != "domain.pddl" and "(problem" in f.read_text(errors="replace").lower())


def limites(arquivo="experimentos/execucoes/fatores-2010.csv"):
    with (RAIZ / arquivo).open(encoding="utf-8") as f:
        return {r["planejador"]: int(r["limite_calibrado_min"]) * 60 for r in csv.DictReader(f)}


def ja_feitas():
    if not RESULTADOS.exists():
        return set()
    with RESULTADOS.open(encoding="utf-8") as f:
        return {(r["planejador"], r["dominio"], r["problema"], r["semente"]) for r in csv.DictReader(f)}


def registrar(linha):
    with trava:
        novo = not RESULTADOS.exists()
        with RESULTADOS.open("a", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS, lineterminator="\n")
            if novo:
                w.writeheader()
            w.writerow(linha)


def executar(tarefa, limite):
    pl, dom, prob, semente = tarefa
    if PARAR.exists():
        return
    with trava:
        w = slots_livres.pop()
    try:
        cwd, cmd = C.comando(pl, dom, prob, base=w)
        if (pl, dom) in variante:
            cmd = cmd[:1] + variante[(pl, dom)] + cmd[1:]
        # Limites internos que em 2010 nunca agiam (o timeout de 20 min vinha antes) e que,
        # sob emulação, cortariam antes do limite calibrado: igualados ao limite calibrado.
        if pl == "LPG":
            cmd = cmd + ["-seed", str(semente), "-cputime", str(limite), "-cputime_localsearch", str(limite)]
        if pl == "MaxPlan":
            cmd = cmd + ["-timeout", str(limite)]
        if pl == "SGPlan":
            cmd = cmd + ["-cputime", str(limite)]
        if pl == "SATPlan":
            cmd = cmd + ["-globaltime", str(limite // 60)]
        for s in Path(cwd).glob("*.soln"):
            s.unlink()
        destino = BRUTOS / C.CHAVE[pl] / dom
        destino.mkdir(parents=True, exist_ok=True)
        nome = prob + (f".s{semente}" if semente else "")
        inicio = time.strftime("%Y-%m-%dT%H:%M:%S")
        t0 = time.time()
        proc = subprocess.Popen(["/usr/bin/time", "-f", "__MEMKB %M"] + cmd, cwd=cwd, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, errors="replace", start_new_session=True)
        try:
            saida, _ = proc.communicate(timeout=limite)
            situacao = "terminou"
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, 9)
            saida, _ = proc.communicate()
            situacao = "estourou"
        relogio = time.time() - t0
        (destino / f"{nome}.log").write_text(saida)
        for s in Path(cwd).glob("*.soln"):
            shutil.copy(s, destino / f"{nome}.soln")
        t = C.tempo_agora(pl, cwd, saida, prob) if situacao == "terminou" else None
        if situacao == "terminou":
            situacao = "resolvido" if t is not None else "sem-plano"
        if situacao == "sem-plano" and LIMITE_INTERNO.search(saida):
            situacao = "estourou"  # parou pelo limite interno, igualado ao calibrado
        mem = re.search(r"__MEMKB (\d+)", saida)
        registrar({"planejador": pl, "dominio": dom, "problema": prob, "semente": semente or "",
                   "situacao": situacao, "tempo_relogio_s": round(relogio, 2),
                   "tempo_planejador_s": "" if t is None else round(t, 3),
                   "memoria_max_kb": mem.group(1) if mem else "", "limite_s": limite, "inicio": inicio,
                   "slot": w.name})
    finally:
        with trava:
            slots_livres.append(w)


def opcao(nome, padrao):
    return sys.argv[sys.argv.index(nome) + 1] if nome in sys.argv else padrao


def main():
    global PARALELOS, RESULTADOS
    PARALELOS = int(opcao("--paralelos", PARALELOS))
    RESULTADOS = Path(opcao("--resultados", RESULTADOS))
    if not RESULTADOS.is_absolute():
        RESULTADOS = RAIZ / RESULTADOS
    adiados = set()
    if "--adiar" in sys.argv:
        adiados = set(sys.argv[sys.argv.index("--adiar") + 1].split(","))
    if "--variante" in sys.argv:
        variante.update(VARIANTES[opcao("--variante", "")])
    preparar_slots()
    lim = limites(opcao("--fatores", "experimentos/execucoes/fatores-2010.csv"))
    feitas = ja_feitas()
    tarefas = []
    for dom in ORDEM_DOMINIOS:
        for prob in problemas(dom):
            for pl in [p for p in PLANEJADORES if p not in adiados]:
                if variante and (pl, dom) not in variante:
                    continue
                for s in (SEMENTES_LPG if pl == "LPG" else ("",)):
                    if (pl, dom, prob, str(s)) not in feitas:
                        tarefas.append((pl, dom, prob, s))
    ultimos = set(opcao("--por-ultimo", "").split(",")) - {""}
    tarefas.sort(key=lambda t: t[0] in ultimos)  # estável: mantém a ordem por domínio dentro de cada grupo
    print(f"{len(tarefas)} execuções pendentes ({len(feitas)} já registradas); adiados: {sorted(adiados) or '-'}",
          flush=True)
    def seguro(t):
        try:
            executar(t, lim[t[0]])
        except Exception:  # registra e segue: uma falha não pode parar a rodada
            import traceback
            print(f"ERRO em {t}:\n{traceback.format_exc()}", flush=True)

    with ThreadPoolExecutor(max_workers=PARALELOS) as ex:
        for t in tarefas:
            ex.submit(seguro, t)
    print("fim", flush=True)


if __name__ == "__main__":
    main()
