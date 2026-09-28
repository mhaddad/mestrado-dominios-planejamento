"""Gera o modelo .docx com os estilos do guia da FEI (redacao/README.md, "Padrão da FEI").

Parte do modelo padrão do Pandoc e ajusta página, margens e estilos: Times New Roman 12, entrelinhas 1,5,
recuo de 1,25 cm, texto justificado; títulos na hierarquia do guia (p. 34); fonte 10 em citação longa,
notas, legendas e fontes; referências em espaço simples com uma linha em branco entre elas.

Uso: uv run --no-project --with python-docx python redacao/montagem/gerar_modelo.py
Saída: redacao/montagem/modelo-fei.docx
"""
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.shared import Cm, Pt, RGBColor

AQUI = Path(__file__).resolve().parent
SAIDA = AQUI / "modelo-fei.docx"
FONTE = "Times New Roman"
PRETO = RGBColor(0, 0, 0)


def estilo(doc, nome, tipo=WD_STYLE_TYPE.PARAGRAPH, base=None):
    try:
        return doc.styles[nome]
    except KeyError:
        s = doc.styles.add_style(nome, tipo)
        if base:
            s.base_style = doc.styles[base]
        return s


def fonte(s, tamanho=12, negrito=None, italico=None, caixa_alta=None):
    f = s.font
    f.name = FONTE
    f.size = Pt(tamanho)
    f.color.rgb = PRETO
    if negrito is not None:
        f.bold = negrito
    if italico is not None:
        f.italic = italico
    if caixa_alta is not None:
        f.all_caps = caixa_alta
    # nome da fonte também para o texto do leste asiático e o complexo, como o Word espera
    rpr = s.element.get_or_add_rPr()
    rfonts = rpr.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts")
    if rfonts is not None:
        for a in ("ascii", "hAnsi", "eastAsia", "cs"):
            rfonts.set(f"{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}{a}", FONTE)
        for a in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
            rfonts.attrib.pop(f"{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}{a}", None)


def paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.JUSTIFY, entrelinhas=1.5, recuo=None, recuo_esq=None,
              antes=0, depois=0, quebra_antes=False, manter=False):
    p = s.paragraph_format
    p.alignment = alinhamento
    if entrelinhas == 1:
        p.line_spacing_rule = WD_LINE_SPACING.SINGLE
    else:
        p.line_spacing = entrelinhas
    p.first_line_indent = Cm(recuo) if recuo is not None else Cm(0)
    p.left_indent = Cm(recuo_esq) if recuo_esq is not None else Cm(0)
    p.space_before = Pt(antes)
    p.space_after = Pt(depois)
    p.page_break_before = quebra_antes
    p.keep_with_next = manter


def main():
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "ref.docx"
        subprocess.run(["pandoc", "-o", str(base), "--print-default-data-file", "reference.docx"], check=True)
        doc = Document(base)

    for sec in doc.sections:
        sec.page_width, sec.page_height = Cm(21), Cm(29.7)
        sec.top_margin, sec.left_margin = Cm(3), Cm(3)
        sec.bottom_margin, sec.right_margin = Cm(2), Cm(2)

    # texto corrido (guia, p. 3-4)
    for nome in ("Normal", "Body Text", "First Paragraph"):
        s = estilo(doc, nome)
        fonte(s, 12)
        paragrafo(s, recuo=1.25)
    for nome in ("Compact",):
        s = estilo(doc, nome)
        fonte(s, 12)
        paragrafo(s, recuo=0)

    # títulos (guia, p. 4 e 34); linha de 1,5 (18 pt) antes e depois
    hierarquia = {
        "Heading 1": dict(negrito=True, italico=False, caixa_alta=True, quebra=True),
        "Heading 2": dict(negrito=False, italico=False, caixa_alta=True, quebra=False),
        "Heading 3": dict(negrito=True, italico=False, caixa_alta=False, quebra=False),
        "Heading 4": dict(negrito=True, italico=True, caixa_alta=False, quebra=False),
        "Heading 5": dict(negrito=False, italico=True, caixa_alta=False, quebra=False),
    }
    for nome, h in hierarquia.items():
        s = estilo(doc, nome)
        fonte(s, 12, negrito=h["negrito"], italico=h["italico"], caixa_alta=h["caixa_alta"])
        paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.LEFT, entrelinhas=1.5, recuo=0,
                  antes=0 if h["quebra"] else 18, depois=18, quebra_antes=h["quebra"], manter=True)

    # títulos sem indicativo numérico: centralizados, maiúsculas e negrito (guia, p. 4)
    s = estilo(doc, "Titulo sem numero", base="Normal")
    fonte(s, 12, negrito=True, caixa_alta=True)
    paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.CENTER, recuo=0, depois=18, quebra_antes=True, manter=True)

    # citação longa: fonte 10, espaço simples, recuo de 4 cm (guia, p. 3-4)
    s = estilo(doc, "Block Text")
    fonte(s, 10)
    paragrafo(s, entrelinhas=1, recuo=0, recuo_esq=4, antes=12, depois=12)

    # notas de rodapé: fonte 10, espaço simples
    s = estilo(doc, "Footnote Text")
    fonte(s, 10)
    paragrafo(s, entrelinhas=1, recuo=0)

    # identificação de tabela e de figura: em cima, fonte 12, à esquerda (guia, p. 5 e 8)
    for nome in ("Table Caption", "Legenda de figura", "Legenda de quadro"):
        s = estilo(doc, nome, base="Normal")
        fonte(s, 12, negrito=False, italico=False)
        paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.LEFT, entrelinhas=1, recuo=0, antes=12, depois=0, manter=True)

    # fonte e legenda, embaixo: fonte 10, espaço simples (guia, p. 5-6 e 8)
    for nome in ("Fonte", "Image Caption"):
        s = estilo(doc, nome, base="Normal")
        fonte(s, 10, italico=False)
        paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.LEFT, entrelinhas=1, recuo=0, antes=0, depois=12)

    s = estilo(doc, "Captioned Figure")
    paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.CENTER, entrelinhas=1, recuo=0)
    s = estilo(doc, "Figure")
    paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.CENTER, entrelinhas=1, recuo=0)

    # referências: à esquerda, espaço simples, uma linha em branco entre elas (guia, p. 4 e 38)
    s = estilo(doc, "Bibliography")
    fonte(s, 12)
    paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.LEFT, entrelinhas=1, recuo=0, depois=12)

    # resumo e abstract: um parágrafo, 1,5 (guia, p. 26)
    s = estilo(doc, "Abstract")
    fonte(s, 12)
    paragrafo(s, recuo=1.25)

    # texto das tabelas
    s = estilo(doc, "Tabela", base="Normal")
    fonte(s, 10)
    paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.LEFT, entrelinhas=1, recuo=0)

    # sumário (guia, p. 34): mesma hierarquia tipográfica dos títulos
    for n, (neg, ita, alta) in enumerate([(True, False, True), (False, False, True), (True, False, False),
                                          (True, True, False), (False, True, False)], start=1):
        s = estilo(doc, f"toc {n}", base="Normal")
        fonte(s, 12, negrito=neg, italico=ita, caixa_alta=alta)
        paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.LEFT, entrelinhas=1.5, recuo=0)

    for nome in ("Title", "Subtitle", "Author", "Date"):
        s = estilo(doc, nome)
        fonte(s, 12, negrito=(nome == "Title"), italico=False)
        paragrafo(s, alinhamento=WD_ALIGN_PARAGRAPH.CENTER, recuo=0)

    # hiperlinks em preto (texto na cor preta, guia p. 3)
    try:
        s = doc.styles["Hyperlink"]
        s.font.color.rgb = PRETO
        s.font.underline = False
    except KeyError:
        pass

    doc.save(SAIDA)
    print(f"modelo gravado em {SAIDA}")


if __name__ == "__main__":
    main()
