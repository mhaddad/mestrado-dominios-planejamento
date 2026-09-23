"""Consolida auditoria/extracao/bloco-*.csv em auditoria/afirmacoes.csv.

Confere que cada trecho é substring exata da linha indicada em
data/2010/extraido/texto.md, ordena as afirmações pela linha e atribui IDs
AF-NNN. Se afirmacoes.csv já existir, preserva as colunas de auditoria
(rotulo_fase1, classificacao, justificativa, acao, conferencia_numerica),
casando pela coluna `origem` (ID do bloco).

Uso: python auditoria/scripts/consolidar_extracao.py
"""
import csv
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TEXTO = RAIZ / "data/2010/extraido/texto.md"
EXTRACAO = RAIZ / "auditoria/extracao"
SAIDA = RAIZ / "auditoria/afirmacoes.csv"

CAMPOS_AUDITORIA = ["rotulo_fase1", "classificacao", "justificativa", "acao", "conferencia_numerica"]
CAMPOS = ["id", "origem", "linha", "secao", "tipo", "trecho", "resumo", "observacao"] + CAMPOS_AUDITORIA


def main() -> int:
    linhas = TEXTO.read_text(encoding="utf-8").splitlines()
    afirmacoes, falhas = [], []
    for arquivo in sorted(EXTRACAO.glob("bloco-*.csv")):
        with arquivo.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                n = int(r["linha"])
                if r["trecho"] not in linhas[n - 1]:
                    falhas.append(f"{arquivo.name}:{r['id']} (linha {n})")
                afirmacoes.append(r)
    if falhas:
        print("Trechos que não são substring exata da linha indicada:", *falhas, sep="\n  ")
        return 1

    anteriores = {}
    if SAIDA.exists():
        with SAIDA.open(encoding="utf-8") as f:
            anteriores = {r["origem"]: r for r in csv.DictReader(f) if r.get("origem")}

    afirmacoes.sort(key=lambda r: (int(r["linha"]), r["id"]))
    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, lineterminator="\n")
        w.writeheader()
        for i, r in enumerate(afirmacoes, 1):
            antigo = anteriores.get(r["id"], {})
            w.writerow({
                "id": f"AF-{i:03d}", "origem": r["id"], "linha": r["linha"], "secao": r["secao"],
                "tipo": r["tipo"], "trecho": r["trecho"], "resumo": r["resumo"],
                "observacao": r.get("observacao", ""),
                **{c: antigo.get(c, "") for c in CAMPOS_AUDITORIA},
            })
    print(f"{len(afirmacoes)} afirmações gravadas em {SAIDA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
