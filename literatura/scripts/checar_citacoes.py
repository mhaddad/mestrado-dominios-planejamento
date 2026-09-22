"""Confere as chaves citadas em arquivos Markdown contra os .bib do projeto.

Uso: python literatura/scripts/checar_citacoes.py ARQUIVO.md [ARQUIVO.md ...]

Status por chave:
  verificada        está em referencias.bib (exportação do Zotero)
  pendente-zotero   só está em candidatas.bib (metadados conferidos por agente)
  ausente           não está em nenhum .bib: não pode ser citada
Também avisa quando a chave não tem nota em literatura/notas-de-leitura/.
Sai com código 1 se houver chave ausente.
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
REFS = RAIZ / "literatura" / "referencias"
NOTAS = RAIZ / "literatura" / "notas-de-leitura"

CHAVE_BIB = re.compile(r"^\s*@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
CITACAO = re.compile(r"(?<![\w@.])-?@([A-Za-z0-9_][A-Za-z0-9_:.\-]*[A-Za-z0-9_])")


def chaves_bib(nome):
    caminho = REFS / nome
    if not caminho.exists():
        return set()
    return set(CHAVE_BIB.findall(caminho.read_text(encoding="utf-8")))


def main(arquivos):
    verificadas = chaves_bib("referencias.bib")
    candidatas = chaves_bib("candidatas.bib")
    citadas = {}
    for arq in arquivos:
        texto = Path(arq).read_text(encoding="utf-8")
        texto = re.sub(r"```.*?```", "", texto, flags=re.DOTALL)
        for chave in CITACAO.findall(texto):
            citadas.setdefault(chave, set()).add(arq)

    contagem = {"verificada": 0, "pendente-zotero": 0, "ausente": 0}
    for chave in sorted(citadas):
        if chave in verificadas:
            status = "verificada"
        elif chave in candidatas:
            status = "pendente-zotero"
        else:
            status = "ausente"
        contagem[status] += 1
        sem_nota = "" if (NOTAS / f"{chave}.md").exists() else "  [sem nota de leitura]"
        if status != "verificada" or sem_nota:
            print(f"{status:16} {chave}{sem_nota}")

    print(f"\n{len(citadas)} chaves: " + ", ".join(f"{k} {v}" for k, v in contagem.items()))
    if contagem["pendente-zotero"] or contagem["ausente"]:
        print("Texto NÃO citável: há chaves fora do referencias.bib.")
    return 1 if contagem["ausente"] else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
