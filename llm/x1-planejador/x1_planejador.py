"""X1 (Fase 4): LLM como planejador (llm/x1-planejador/protocolo.md).

Para cada instância (p01 do Autoscale em 8 domínios) e cada modelo do X3, pede um plano ao
OpenRouter com o prompt de llm/prompts/x1-planejador-v1.md, grava a resposta bruta em
llm/registros/x1/<rodada>/ e valida o plano com o VAL. `referencia` gera os planos do
Fast Downward (lama-first) para comparação de comprimento.

Uso:
  python llm/x1-planejador/x1_planejador.py referencia
  python llm/x1-planejador/x1_planejador.py rodar --rodada principal
  python llm/x1-planejador/x1_planejador.py avaliar --rodada principal
  python llm/x1-planejador/x1_planejador.py referencia --instancia p05   (instâncias maiores, X4)
"""
import argparse
import csv
import json
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "llm/x3-seletor"))
import x3_seletor as X3  # noqa: E402  (chave, http, uso_da_chave, ler, MODELOS, CONFIG, TETO_USD)

AUTOSCALE = X3.AUTOSCALE
PROMPT = RAIZ / "llm/prompts/x1-planejador-v1.md"
REGISTROS = RAIZ / "llm/registros/x1"
RESULTADOS = RAIZ / "llm/x1-planejador/resultados"
VAL = RAIZ / "experimentos/ferramentas/planner-museum/tools/VAL/build/mac/bin/Validate"
FD = RAIZ / "experimentos/ferramentas/downward/fast-downward.py"
DOMINIOS = ["blocksworld", "tpp", "floortile", "pipesworld-notankage", "gripper", "logistics", "miconic", "rovers"]
INSTANCIA = "p01"


def arquivos(dominio):
    pasta = AUTOSCALE / dominio
    dom = pasta / "domain.pddl" if (pasta / "domain.pddl").exists() else pasta / f"domain-{INSTANCIA}.pddl"
    return dom, pasta / f"{INSTANCIA}.pddl"


def extrair_plano(texto):
    m = re.search(r"BEGIN PLAN\s*(.*?)\s*END PLAN", texto or "", re.S | re.I)
    if not m:
        return None
    return [l.strip() for l in m.group(1).splitlines() if re.match(r"^\s*\(.+\)\s*$", l)]


def validar(dominio, plano):
    """Devolve (válido, mensagem resumida do VAL)."""
    dom, prob = arquivos(dominio)
    with tempfile.NamedTemporaryFile("w", suffix=".plan", delete=False) as f:
        f.write("\n".join(plano) + "\n")
    r = subprocess.run([str(VAL), "-v", str(dom), str(prob), f.name], capture_output=True, text=True)
    saida = r.stdout + r.stderr
    valido = "Plan valid" in saida
    if valido:
        return True, "válido"
    for padrao, rotulo in (("unsatisfied precondition", "pré-condição não satisfeita"),
                           ("Goal not satisfied", "meta não alcançada"),
                           ("Bad operator", "ação inexistente ou mal formada"),
                           ("Type-checking", "erro de tipos")):
        if padrao.lower() in saida.lower():
            return False, rotulo
    return False, "inválido (outro)"


def referencia(_a):
    linhas = []
    with tempfile.TemporaryDirectory() as tmp:
        for d in DOMINIOS:
            dom, prob = arquivos(d)
            subprocess.run([sys.executable, str(FD), "--overall-time-limit", "300", "--alias", "lama-first",
                            str(dom), str(prob)], cwd=tmp, capture_output=True, text=True)
            arq = Path(tmp) / "sas_plan"
            if not arq.exists():
                linhas.append({"dominio": d, "instancia": INSTANCIA, "passos_lama": "", "val": "LAMA sem plano em 300 s"})
                continue
            plano = [l for l in arq.read_text().splitlines() if l.startswith("(")]
            ok, msg = validar(d, plano)
            linhas.append({"dominio": d, "instancia": INSTANCIA, "passos_lama": len(plano), "val": msg})
            arq.unlink()
    RESULTADOS.mkdir(parents=True, exist_ok=True)
    nome = "referencia-lama.csv" if INSTANCIA == "p01" else f"referencia-lama-{INSTANCIA}.csv"
    with (RESULTADOS / nome).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    for l in linhas:
        print(l)


def chamar(k, modelo, dominio, rodada):
    destino = REGISTROS / rodada / modelo.replace("/", "__") / f"{dominio}-{INSTANCIA}.json"
    if destino.exists():
        return "já registrado"
    if X3.uso_da_chave(k) >= X3.TETO_USD:
        return "teto atingido"
    md = PROMPT.read_text(encoding="utf-8")
    sistema, usuario = re.findall(r"```\n(.*?)```", md, re.S)
    dom, prob = arquivos(dominio)
    usuario = usuario.replace("{dominio}", X3.ler(dom)[0]).replace("{instancia}", X3.ler(prob)[0])
    corpo = {"model": modelo, "messages": [{"role": "system", "content": sistema.strip()},
                                           {"role": "user", "content": usuario}], **X3.CONFIG}
    inicio = time.time()
    for tentativa in range(3):
        try:
            resp = X3.http("https://openrouter.ai/api/v1/chat/completions", corpo, k)
            break
        except Exception as e:  # noqa: BLE001
            erro = repr(e)
            time.sleep(10 * (tentativa + 1))
    else:
        return f"erro de rede, sem registro: {erro[:120]}"
    texto = resp["choices"][0]["message"].get("content") if resp.get("choices") else None
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps({
        "modelo_pedido": modelo, "modelo_respondeu": resp.get("model"), "provedor": resp.get("provider"),
        "dominio": dominio, "instancia": INSTANCIA, "data_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "config": X3.CONFIG, "prompt": PROMPT.name, "segundos": round(time.time() - inicio, 1),
        "uso": resp.get("usage"), "resposta": texto, "bruto": resp}, ensure_ascii=False, indent=1), encoding="utf-8")
    plano = extrair_plano(texto)
    return f"{'sem plano' if plano is None else f'{len(plano)} passos'} (US$ {((resp.get('usage') or {}).get('cost') or 0):.4f})"


def rodar(a):
    k = X3.chave()
    print(f"uso da chave antes: US$ {X3.uso_da_chave(k):.4f}")

    def por_modelo(modelo):
        for d in DOMINIOS:
            r = chamar(k, modelo, d, a.rodada)
            print(f"{modelo:36s} {d:22s} {r}", flush=True)
            if r == "teto atingido":
                return
    with ThreadPoolExecutor(len(X3.MODELOS)) as ex:
        list(ex.map(por_modelo, X3.MODELOS))
    print(f"uso da chave depois: US$ {X3.uso_da_chave(k):.4f}")


def avaliar(a):
    nome = "referencia-lama.csv" if INSTANCIA == "p01" else f"referencia-lama-{INSTANCIA}.csv"
    ref = {r["dominio"]: int(r["passos_lama"]) if r["passos_lama"] else None
           for r in csv.DictReader((RESULTADOS / nome).open(encoding="utf-8"))}
    linhas = []
    for modelo in X3.MODELOS:
        for d in DOMINIOS:
            arq = REGISTROS / a.rodada / modelo.replace("/", "__") / f"{d}-{INSTANCIA}.json"
            if not arq.exists():
                continue
            r = json.loads(arq.read_text(encoding="utf-8"))
            plano = extrair_plano(r["resposta"])
            ok, msg = (False, "sem plano na resposta") if not plano else validar(d, plano)
            linhas.append({"modelo": modelo, "dominio": d, "passos": len(plano or []), "valido": ok, "val": msg,
                           "passos_lama": ref[d], "razao_comprimento": round(len(plano) / ref[d], 2) if ok and ref[d] else "",
                           "custo_usd": round(float((r.get("uso") or {}).get("cost") or 0), 4),
                           "fim": (r["bruto"].get("choices") or [{}])[0].get("finish_reason")})
    RESULTADOS.mkdir(parents=True, exist_ok=True)
    saida = RESULTADOS / f"{a.rodada}.csv"
    with saida.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    for l in linhas:
        print(l)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("acao", choices=("referencia", "rodar", "avaliar"))
    ap.add_argument("--rodada", default="principal")
    ap.add_argument("--instancia", default="p01", help="instância do Autoscale (p01 no X1; p05 no X4)")
    a = ap.parse_args()
    global INSTANCIA
    INSTANCIA = a.instancia
    {"referencia": referencia, "rodar": rodar, "avaliar": avaliar}[a.acao](a)


if __name__ == "__main__":
    main()
