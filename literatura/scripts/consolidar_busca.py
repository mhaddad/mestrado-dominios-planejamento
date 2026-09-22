"""Junta as listas brutas por eixo e remove duplicatas entre eixos.

Uso: python literatura/scripts/consolidar_busca.py
Lê literatura/protocolo/busca/E*-bruta.csv e grava
literatura/protocolo/lista-consolidada.csv. Duplicata = mesmo DOI, mesmo
arXiv id ou mesmo título normalizado. Fica a primeira ocorrência; as demais
vão para as colunas eixos e ids_origem.
"""

import csv
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BUSCA = RAIZ / "literatura" / "protocolo" / "busca"
SAIDA = RAIZ / "literatura" / "protocolo" / "lista-consolidada.csv"


def norm_titulo(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def norm_doi(d):
    d = (d or "").strip().lower()
    return re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", d)


def norm_arxiv(a):
    a = (a or "").strip().lower()
    a = re.sub(r"^(arxiv:|https?://arxiv\.org/abs/)", "", a)
    return re.sub(r"v\d+$", "", a)


def main():
    itens, indice = [], {}
    campos = None
    for arq in sorted(BUSCA.glob("E*-bruta.csv")):
        with arq.open(encoding="utf-8", newline="") as f:
            leitor = csv.DictReader(f)
            campos = campos or leitor.fieldnames
            for linha in leitor:
                chaves = [k for k in (
                    "doi:" + norm_doi(linha.get("doi")) if norm_doi(linha.get("doi")) else "",
                    "arxiv:" + norm_arxiv(linha.get("arxiv_id")) if norm_arxiv(linha.get("arxiv_id")) else "",
                    "tit:" + norm_titulo(linha.get("titulo", "")),
                ) if k and k != "tit:"]
                existente = next((indice[k] for k in chaves if k in indice), None)
                if existente is None:
                    linha["eixos"] = linha["eixo"]
                    linha["ids_origem"] = linha["id"]
                    itens.append(linha)
                    existente = linha
                else:
                    if linha["eixo"] not in existente["eixos"].split(";"):
                        existente["eixos"] += ";" + linha["eixo"]
                    existente["ids_origem"] += ";" + linha["id"]
                    if linha.get("semente") == "sim":
                        existente["semente"] = "sim"
                for k in chaves:
                    indice.setdefault(k, existente)

    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=list(campos) + ["eixos", "ids_origem"])
        escritor.writeheader()
        escritor.writerows(itens)
    total = sum(1 for _ in BUSCA.glob("E*-bruta.csv"))
    print(f"{total} listas; {len(itens)} itens únicos -> {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
