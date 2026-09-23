"""Resume auditoria/afirmacoes.csv para o relatório de auditoria.

Uso: python auditoria/scripts/resumir_auditoria.py
"""
import csv
import collections
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CAPITULOS = [(60, 110, "Resumo"), (111, 188, "1 Introdução"), (189, 492, "2 Revisão bibliográfica"),
             (493, 603, "3 Planejadores"), (604, 847, "4 Domínios"), (848, 1277, "5 Características × técnicas"),
             (1278, 1795, "6 Testes e validações"), (1796, 1830, "7 Conclusões e trabalhos futuros")]


def capitulo(linha: int) -> str:
    return next(n for a, b, n in CAPITULOS if a <= linha <= b)


def main() -> None:
    with (RAIZ / "auditoria/afirmacoes.csv").open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"Total: {len(rows)}")
    print("Por classe:", dict(collections.Counter(r["classificacao"] for r in rows)))
    print("Por confiança:", dict(collections.Counter(r["confianca"] for r in rows)))
    print("Por tipo × classe:")
    for t, n in collections.Counter(r["tipo"] for r in rows).most_common():
        c = collections.Counter(r["classificacao"] for r in rows if r["tipo"] == t)
        print(f"  {t}: {n} {dict(c)}")
    print("Por capítulo × classe:")
    for _, _, cap in CAPITULOS:
        sel = [r for r in rows if capitulo(int(r["linha"])) == cap]
        print(f"  {cap}: {len(sel)} {dict(collections.Counter(r['classificacao'] for r in sel))}")
    print("Rótulos centrais (A1–A8) × classe:")
    for a in [f"A{i}" for i in range(1, 9)]:
        sel = [r for r in rows if a in r["rotulo_fase1"].replace(";", " ").split()]
        print(f"  {a}: {len(sel)} {dict(collections.Counter(r['classificacao'] for r in sel))}")
    print("Ações FASE3:", sum(r["acao"].startswith("FASE3") for r in rows))
    print("Ações CONFERIR:", sum(r["acao"].upper().startswith("CONFERIR") or "conferir na fonte" in r["acao"].lower() for r in rows))
    print("Revisões do Coordenador:", sum("REVISÃO DO COORDENADOR" in r["justificativa"] for r in rows))
    print("Divergências do insumo:", [r["id"] for r in rows if "DIVERGE DO INSUMO" in r["justificativa"]])
    print("Descarta:", [(r["id"], r["resumo"]) for r in rows if r["classificacao"] == "descarta"])


if __name__ == "__main__":
    main()
