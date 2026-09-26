"""X4 (Fase 4): LLM + verificador (llm/x4-verificador/protocolo.md).

Para cada modelo do X3 e cada domínio de DOMINIOS, na instância p05 do Autoscale: pede um plano
com o prompt do X1 e valida com o VAL. Se o plano for inválido (ou ausente, ou mal formatado),
devolve ao modelo, na mesma conversa, o motivo e o trecho final da saída do VAL, e pede um plano
corrigido; até MAX_CORRECOES rodadas. Cada rodada é gravada em llm/registros/x4/<rodada>/.

Uso:
  python llm/x4-verificador/x4_verificador.py rodar --rodada p05
  python llm/x4-verificador/x4_verificador.py avaliar --rodada p05
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
sys.path.insert(0, str(RAIZ / "llm/x1-planejador"))
import x1_planejador as X1  # noqa: E402

X3 = X1.X3
X1.INSTANCIA = "p05"
DOMINIOS = ["blocksworld", "tpp", "floortile", "pipesworld-notankage"]
MAX_CORRECOES = 3
TETO_X4_USD = 8.90  # reserva o restante do teto de US$ 10 para o X2
REGISTROS = RAIZ / "llm/registros/x4"
RESULTADOS = RAIZ / "llm/x4-verificador/resultados"
LIMITE_VAL = 1500  # caracteres finais da saída do VAL devolvidos ao modelo
FEEDBACK = """The plan you gave is not valid. {motivo}

{detalhe}

Please provide a corrected, complete plan for the same problem, from the initial state,
between the lines BEGIN PLAN and END PLAN, one action per line in PDDL syntax."""


def saida_val(dominio, plano):
    dom, prob = X1.arquivos(dominio)
    with tempfile.NamedTemporaryFile("w", suffix=".plan", delete=False) as f:
        f.write("\n".join(plano) + "\n")
    r = subprocess.run([str(X1.VAL), "-v", str(dom), str(prob), f.name], capture_output=True, text=True)
    return (r.stdout + r.stderr).strip()


def diagnostico(dominio, texto):
    """(válido, rótulo, texto de retorno ao modelo)."""
    plano = X1.extrair_plano(texto)
    if plano is None:
        return False, "sem plano na resposta", FEEDBACK.format(
            motivo="No plan was found between the lines BEGIN PLAN and END PLAN.", detalhe="")
    if not plano:
        return False, "plano mal formatado", FEEDBACK.format(
            motivo="No action in PDDL syntax, such as (action-name object1 object2), was found in the plan.", detalhe="")
    ok, rotulo = X1.validar(dominio, plano)
    if ok:
        return True, rotulo, ""
    return False, rotulo, FEEDBACK.format(
        motivo="The plan validator VAL reports the following (last part of its output):",
        detalhe=saida_val(dominio, plano)[-LIMITE_VAL:])


def conversa(k, modelo, dominio, rodada):
    destino = REGISTROS / rodada / modelo.replace("/", "__") / f"{dominio}-{X1.INSTANCIA}.json"
    if destino.exists():
        return "já registrado"
    md = X1.PROMPT.read_text(encoding="utf-8")
    sistema, usuario = re.findall(r"```\n(.*?)```", md, re.S)
    dom, prob = X1.arquivos(dominio)
    usuario = usuario.replace("{dominio}", X3.ler(dom)[0]).replace("{instancia}", X3.ler(prob)[0])
    mensagens = [{"role": "system", "content": sistema.strip()}, {"role": "user", "content": usuario}]
    rodadas = []
    for n in range(MAX_CORRECOES + 1):
        if X3.uso_da_chave(k) >= TETO_X4_USD:
            rodadas.append({"rodada": n, "parada": "teto do X4 atingido"})
            break
        corpo = {"model": modelo, "messages": mensagens, **X3.CONFIG}
        inicio = time.time()
        for tentativa in range(3):
            try:
                resp = X3.http("https://openrouter.ai/api/v1/chat/completions", corpo, k)
                break
            except Exception as e:  # noqa: BLE001
                erro = repr(e)
                time.sleep(10 * (tentativa + 1))
        else:
            rodadas.append({"rodada": n, "parada": f"erro de rede: {erro[:200]}"})
            break
        texto = resp["choices"][0]["message"].get("content") if resp.get("choices") else None
        ok, rotulo, retorno = diagnostico(dominio, texto)
        rodadas.append({"rodada": n, "data_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        "segundos": round(time.time() - inicio, 1), "modelo_respondeu": resp.get("model"),
                        "provedor": resp.get("provider"), "uso": resp.get("usage"),
                        "fim": (resp.get("choices") or [{}])[0].get("finish_reason"),
                        "valido": ok, "diagnostico": rotulo, "resposta": texto, "retorno_enviado": retorno})
        if ok:
            break
        mensagens += [{"role": "assistant", "content": texto or ""}, {"role": "user", "content": retorno}]
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps({"modelo_pedido": modelo, "dominio": dominio, "instancia": X1.INSTANCIA,
                                   "config": X3.CONFIG, "max_correcoes": MAX_CORRECOES, "rodadas": rodadas},
                                  ensure_ascii=False, indent=1), encoding="utf-8")
    custo = sum(float((r.get("uso") or {}).get("cost") or 0) for r in rodadas)
    return " → ".join(r.get("diagnostico", r.get("parada", "")) for r in rodadas) + f" (US$ {custo:.4f})"


def rodar(a):
    k = X3.chave()
    print(f"uso da chave antes: US$ {X3.uso_da_chave(k):.4f}")

    def por_modelo(modelo):
        for d in DOMINIOS:
            print(f"{modelo:36s} {d:22s} {conversa(k, modelo, d, a.rodada)}", flush=True)
    with ThreadPoolExecutor(len(X3.MODELOS)) as ex:
        list(ex.map(por_modelo, X3.MODELOS))
    print(f"uso da chave depois: US$ {X3.uso_da_chave(k):.4f}")


def avaliar(a):
    ref = {r["dominio"]: r["passos_lama"] for r in
           csv.DictReader((X1.RESULTADOS / f"referencia-lama-{X1.INSTANCIA}.csv").open(encoding="utf-8"))}
    linhas = []
    for modelo in X3.MODELOS:
        for d in DOMINIOS:
            arq = REGISTROS / a.rodada / modelo.replace("/", "__") / f"{d}-{X1.INSTANCIA}.json"
            if not arq.exists():
                continue
            rs = [r for r in json.loads(arq.read_text(encoding="utf-8"))["rodadas"] if "valido" in r]
            valida_em = next((r["rodada"] for r in rs if r["valido"]), "")
            final = rs[-1] if rs else {}
            plano = X1.extrair_plano(final.get("resposta")) or []
            linhas.append({"modelo": modelo, "dominio": d, "valido_na_primeira": bool(rs and rs[0]["valido"]),
                           "valido_ao_final": bool(final.get("valido")), "valido_na_rodada": valida_em,
                           "rodadas": len(rs), "diagnosticos": " → ".join(r["diagnostico"] for r in rs),
                           "passos_final": len(plano) if final.get("valido") else "", "passos_lama": ref[d],
                           "custo_usd": round(sum(float((r.get("uso") or {}).get("cost") or 0) for r in rs), 4)})
    RESULTADOS.mkdir(parents=True, exist_ok=True)
    with (RESULTADOS / f"{a.rodada}.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    for l in linhas:
        print(l)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("acao", choices=("rodar", "avaliar"))
    ap.add_argument("--rodada", default="p05")
    a = ap.parse_args()
    {"rodar": rodar, "avaliar": avaliar}[a.acao](a)


if __name__ == "__main__":
    main()
