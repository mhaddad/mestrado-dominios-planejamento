"""X2: motivo de cada checagem de solidez ou completude reprovada (só pares com assinatura igual).

A validade vem do VAL sem -v (a mesma chamada da avaliação principal). Para achar o motivo das
reprovações, roda o VAL com -v, com limite de 60 s (em um caso do Barman, o modo detalhado
passou de 8 minutos). Ordem da classificação: linha exata "Plan valid"; erro de tipos (mensagens
de erro, não o registro "Type-checking ..." que o -v imprime sempre); pré-condição; meta.

Uso: python llm/x2-tradutor/motivos.py   Saída: llm/x2-tradutor/resultados/principal-motivos.csv
"""
import collections
import csv
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "llm/x2-tradutor"))
import x2_tradutor as X  # noqa: E402


def motivo(dom, prob, plano):
    if X.val(dom, prob, plano):
        return "válido"
    with tempfile.NamedTemporaryFile("w", suffix=".plan", delete=False) as f:
        f.write(plano)
    try:
        s = subprocess.run([str(X.VAL), "-v", str(dom), str(prob), f.name], capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return "inválido (VAL -v passou de 60 s)"
    o = (s.stdout + s.stderr).lower()
    if "error in type-checking" in o or "unknown type" in o:
        return "erro de tipos (VAL)"
    if "unsatisfied precondition" in o:
        return "pré-condição"
    if "goal not satisfied" in o:
        return "meta"
    return "inválido (outro)"


def main():
    rows = list(csv.DictReader((X.RESULTADOS / "principal.csv").open(encoding="utf-8")))
    falhas = [r for r in rows if r["assinatura_igual"] == "True" and "False" in (r["solidez"], r["completude"])]
    por, ref = collections.defaultdict(collections.Counter), {}
    with tempfile.TemporaryDirectory() as tmp:
        for r in falhas:
            m, d, p = r["modelo"], r["dominio"], r["problema"]
            t = json.loads((X.REGISTROS / "principal" / m.replace("/", "__") / f"{d}.json").read_text(encoding="utf-8"))["resposta"]
            g = Path(tmp) / "g.pddl"
            g.write_text(X.extrair_dominio(t), encoding="utf-8")
            prob = X.LLMP / d / f"{p}.pddl"
            if r["completude"] == "False":
                if (d, p) not in ref:
                    ref[(d, p)] = X.planejar(X.LLMP / d / "domain.pddl", prob, tmp)[1]
                por[(m, d)]["completude: " + motivo(g, prob, ref[(d, p)])] += 1
            if r["solidez"] == "False":
                pl = X.planejar(g, prob, tmp)[1]
                por[(m, d)]["solidez: " + (motivo(X.LLMP / d / "domain.pddl", prob, pl) if pl else "sem plano nesta execução")] += 1
            print(m.split("/")[1][:14], d, p, dict(por[(m, d)]), flush=True)
    saida = []
    for (m, d), c in sorted(por.items()):
        for k, v in c.items():
            saida.append({"modelo": m, "dominio": d, "checagem": k.split(": ")[0], "motivo": k.split(": ", 1)[1], "problemas": v})
    with (X.RESULTADOS / "principal-motivos.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(saida[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(saida)


if __name__ == "__main__":
    main()
