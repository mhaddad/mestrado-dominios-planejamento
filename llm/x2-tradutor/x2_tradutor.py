"""X2 (Fase 4): LLM como tradutor de linguagem natural para PDDL (llm/x2-tradutor/protocolo.md).

Para cada domínio do LLM+P (experimentos/ferramentas/llm-pddl, commit f5f897c) e cada modelo do
X3, pede o domínio PDDL a partir de domain.nl e do problema p01, e avalia o domínio gerado nos
problemas p01–p05 em três níveis:
  sintaxe     o tradutor do Fast Downward aceita domínio gerado + problema;
  solidez     o plano do Fast Downward (lama-first) com o domínio gerado é válido (VAL) no
              domínio de referência;
  completude  o plano do Fast Downward com o domínio de referência é válido (VAL) no domínio gerado.

Uso:
  python llm/x2-tradutor/x2_tradutor.py rodar --rodada principal
  python llm/x2-tradutor/x2_tradutor.py avaliar --rodada principal
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
import x3_seletor as X3  # noqa: E402

LLMP = RAIZ / "experimentos/ferramentas/llm-pddl/domains"
PROMPT = RAIZ / "llm/prompts/x2-tradutor-v1.md"
REGISTROS = RAIZ / "llm/registros/x2"
RESULTADOS = RAIZ / "llm/x2-tradutor/resultados"
VAL = RAIZ / "experimentos/ferramentas/planner-museum/tools/VAL/build/mac/bin/Validate"
FD = RAIZ / "experimentos/ferramentas/downward/fast-downward.py"
# Tyreworld fora: o domínio de referência usa o objeto `wrench` sem declará-lo, e o tradutor do
# Fast Downward o recusa (sem referência válida não há solidez nem completude a medir)
DOMINIOS = ["barman", "blocksworld", "floortile", "grippers", "storage", "termes"]
PROBLEMAS = ["p01", "p02", "p03", "p04", "p05"]


def extrair_dominio(texto):
    m = re.search(r"BEGIN DOMAIN\s*(.*?)\s*END DOMAIN", texto or "", re.S | re.I)
    if not m:
        return None
    return re.sub(r"^```[a-z]*\s*|\s*```$", "", m.group(1).strip())


def chamar(k, modelo, dominio, rodada):
    destino = REGISTROS / rodada / modelo.replace("/", "__") / f"{dominio}.json"
    if destino.exists():
        return "já registrado"
    if X3.uso_da_chave(k) >= X3.TETO_USD:
        return "teto atingido"
    md = PROMPT.read_text(encoding="utf-8")
    sistema, usuario = re.findall(r"```\n(.*?)```", md, re.S)
    usuario = usuario.replace("{descricao}", (LLMP / dominio / "domain.nl").read_text(encoding="utf-8")) \
                     .replace("{problema}", (LLMP / dominio / "p01.pddl").read_text(encoding="utf-8"))
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
    if (resp.get("choices") or [{}])[0].get("finish_reason") == "error":
        # erro do provedor no meio da resposta (sem cobrança): tratado como erro de rede, sem registro
        return "erro do provedor (finish_reason = error), sem registro; rodar de novo tenta outra vez"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps({
        "modelo_pedido": modelo, "modelo_respondeu": resp.get("model"), "provedor": resp.get("provider"),
        "dominio": dominio, "data_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "config": X3.CONFIG, "prompt": PROMPT.name, "segundos": round(time.time() - inicio, 1),
        "uso": resp.get("usage"), "resposta": texto, "bruto": resp}, ensure_ascii=False, indent=1), encoding="utf-8")
    return f"{'sem domínio' if extrair_dominio(texto) is None else 'domínio gerado'} (US$ {((resp.get('usage') or {}).get('cost') or 0):.4f})"


def planejar(dominio_pddl, problema, tmp):
    """Plano do Fast Downward (lama-first) ou None; também diz se a tradução falhou."""
    sas = Path(tmp) / "sas_plan"
    sas.unlink(missing_ok=True)
    r = subprocess.run([sys.executable, str(FD), "--overall-time-limit", "120", "--alias", "lama-first",
                        str(dominio_pddl), str(problema)], cwd=tmp, capture_output=True, text=True)
    traduziu = "translate exit code: 0" in (r.stdout + r.stderr) or "Done!" in (r.stdout + r.stderr) or sas.exists()
    return traduziu, (sas.read_text() if sas.exists() else None)


def val(dominio_pddl, problema, plano_txt):
    with tempfile.NamedTemporaryFile("w", suffix=".plan", delete=False) as f:
        f.write(plano_txt)
    r = subprocess.run([str(VAL), str(dominio_pddl), str(problema), f.name], capture_output=True, text=True)
    return re.search(r"^Plan valid\s*$", r.stdout + r.stderr, re.M) is not None


def avaliar(a):
    linhas = []
    with tempfile.TemporaryDirectory() as tmp:
        ref_planos = {}
        for d in DOMINIOS:
            for p in PROBLEMAS:
                _t, ref_planos[(d, p)] = planejar(LLMP / d / "domain.pddl", LLMP / d / f"{p}.pddl", tmp)
        for modelo in X3.MODELOS:
            for d in DOMINIOS:
                arq = REGISTROS / a.rodada / modelo.replace("/", "__") / f"{d}.json"
                if not arq.exists():
                    continue
                r = json.loads(arq.read_text(encoding="utf-8"))
                gerado = extrair_dominio(r["resposta"])
                base = {"modelo": modelo, "dominio": d, "custo_usd": round(float((r.get("uso") or {}).get("cost") or 0), 4)}
                if gerado is None:
                    linhas += [{**base, "problema": p, "extraido": False, "sintaxe": False, "solidez": "",
                                "completude": "", "plano_referencia": ref_planos[(d, p)] is not None} for p in PROBLEMAS]
                    continue
                dom_gerado = Path(tmp) / f"gerado-{modelo.replace('/', '_')}-{d}.pddl"
                dom_gerado.write_text(gerado, encoding="utf-8")
                for p in PROBLEMAS:
                    prob = LLMP / d / f"{p}.pddl"
                    traduziu, plano = planejar(dom_gerado, prob, tmp)
                    solidez = "" if plano is None else val(LLMP / d / "domain.pddl", prob, plano)
                    completude = "" if ref_planos[(d, p)] is None else val(dom_gerado, prob, ref_planos[(d, p)])
                    linhas.append({**base, "problema": p, "extraido": True, "sintaxe": traduziu,
                                   "plano_gerado": plano is not None, "solidez": solidez, "completude": completude,
                                   "plano_referencia": ref_planos[(d, p)] is not None})
    RESULTADOS.mkdir(parents=True, exist_ok=True)
    campos = ["modelo", "dominio", "problema", "extraido", "sintaxe", "plano_gerado", "solidez", "completude",
              "plano_referencia", "custo_usd"]
    with (RESULTADOS / f"{a.rodada}.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n", restval="")
        w.writeheader()
        w.writerows(linhas)
    for modelo in X3.MODELOS:
        ls = [l for l in linhas if l["modelo"] == modelo]
        print(modelo, {"problemas": len(ls), "sintaxe": sum(l["sintaxe"] is True for l in ls),
                       "solidez": sum(l["solidez"] is True for l in ls), "completude": sum(l["completude"] is True for l in ls)})


def rodar(a):
    k = X3.chave()
    print(f"uso da chave antes: US$ {X3.uso_da_chave(k):.4f}")

    def por_modelo(modelo):
        for d in DOMINIOS:
            print(f"{modelo:36s} {d:12s} {chamar(k, modelo, d, a.rodada)}", flush=True)
    with ThreadPoolExecutor(len(X3.MODELOS)) as ex:
        list(ex.map(por_modelo, X3.MODELOS))
    print(f"uso da chave depois: US$ {X3.uso_da_chave(k):.4f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("acao", choices=("rodar", "avaliar"))
    ap.add_argument("--rodada", default="principal")
    a = ap.parse_args()
    {"rodar": rodar, "avaliar": avaliar}[a.acao](a)


if __name__ == "__main__":
    main()
