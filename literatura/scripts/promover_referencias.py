"""Promove para o referencias.bib as entradas aprovadas pelo autor.

Uso: python literatura/scripts/promover_referencias.py

Lê as marcas `- [x] `chave`` de literatura/referencias/revisao-referencias.md,
copia as entradas correspondentes de candidatas.bib e reescreve referencias.bib
inteiro (é idempotente: rodar de novo reflete as marcas atuais).
"""

import re
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
REFS = RAIZ / "literatura" / "referencias"
REVISAO = REFS / "revisao-referencias.md"
CANDIDATAS = REFS / "candidatas.bib"
DESTINO = REFS / "referencias.bib"

MARCA = re.compile(r"^- \[([ xX])\] `([^`]+)`", re.MULTILINE)
ENTRADA = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")


def sem_comentarios_finais(bloco):
    """Tira do fim do bloco as linhas de comentário que precedem a próxima entrada."""
    linhas = bloco.rstrip().split("\n")
    while linhas and (not linhas[-1].strip() or linhas[-1].lstrip().startswith("%")):
        linhas.pop()
    return "\n".join(linhas)


def main():
    if len(sys.argv) > 1:
        sys.exit(__doc__)
    marcas = MARCA.findall(REVISAO.read_text(encoding="utf-8"))
    aprovadas = [k for m, k in marcas if m.lower() == "x"]
    recusadas = [k for m, k in marcas if m == " "]

    entradas = {}
    for bloco in re.split(r"(?m)^(?=@)", CANDIDATAS.read_text(encoding="utf-8")):
        m = ENTRADA.match(bloco)
        if m:
            entradas[m.group(1)] = sem_comentarios_finais(bloco.strip())

    faltando = [k for k in aprovadas if k not in entradas]
    if faltando:
        sys.exit(f"Chaves aprovadas que não existem no candidatas.bib: {faltando}")

    cabecalho = (
        f"% referencias.bib — obras verificadas e aprovadas pelo autor.\n"
        f"% Gerado por literatura/scripts/promover_referencias.py em {date.today():%d/%m/%Y}.\n"
        f"% Não edite à mão: corrija em candidatas.bib e rode o script de novo.\n\n"
    )
    corpo = "\n\n".join(entradas[k] for k in sorted(aprovadas))
    DESTINO.write_text(cabecalho + corpo + "\n", encoding="utf-8")
    print(f"{len(aprovadas)} promovidas, {len(recusadas)} não promovidas -> {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
