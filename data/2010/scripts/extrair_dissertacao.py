"""Extrai o texto e as tabelas da dissertação de 2010 (docx) para inspeção.

Saídas (em data/2010/extraido/):
  texto.md          parágrafos e tabelas, na ordem do documento
  tabela_NN.csv     cada tabela do docx, na ordem em que aparece (NN = índice, base 1)

O número NN é o índice físico da tabela no docx; NÃO é necessariamente o número
da tabela na legenda da dissertação. O mapeamento está em indice_tabelas.csv.
"""
import csv
import re
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

RAIZ = Path(__file__).resolve().parents[3]
DOCX = RAIZ / "acervo-2010/dissertacao/dissertacao-haddad-2010.docx"
SAIDA = RAIZ / "data/2010/extraido"


def itera_blocos(doc):
    corpo = doc.element.body
    for filho in corpo.iterchildren():
        if filho.tag.endswith("}p"):
            yield Paragraph(filho, doc)
        elif filho.tag.endswith("}tbl"):
            yield Table(filho, doc)


def celulas(tabela):
    return [[c.text.strip().replace("\n", " ") for c in linha.cells] for linha in tabela.rows]


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    doc = Document(DOCX)
    md, indice = [], []
    n_tab = 0
    ultimo_par = ""
    for bloco in itera_blocos(doc):
        if isinstance(bloco, Paragraph):
            t = bloco.text.strip()
            if not t:
                continue
            estilo = bloco.style.name if bloco.style is not None else ""
            m = re.match(r"Heading (\d)", estilo)
            md.append(("#" * int(m.group(1)) + " " + t) if m else t)
            md.append("")
            ultimo_par = t
        else:
            n_tab += 1
            linhas = celulas(bloco)
            nome = f"tabela_{n_tab:02d}.csv"
            with open(SAIDA / nome, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows(linhas)
            indice.append([n_tab, nome, len(linhas), len(linhas[0]) if linhas else 0, ultimo_par[:90]])
            md.append(f"[[TABELA {n_tab:02d}: {len(linhas)} linhas x {len(linhas[0]) if linhas else 0} colunas]]")
            for l in linhas:
                md.append("| " + " | ".join(l) + " |")
            md.append("")
    (SAIDA / "texto.md").write_text("\n".join(md), encoding="utf-8")
    with open(SAIDA / "indice_tabelas.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["indice_fisico", "arquivo", "linhas", "colunas", "paragrafo_anterior"])
        w.writerows(indice)
    print(f"{n_tab} tabelas; {len(md)} linhas de texto -> {SAIDA}")


if __name__ == "__main__":
    main()
