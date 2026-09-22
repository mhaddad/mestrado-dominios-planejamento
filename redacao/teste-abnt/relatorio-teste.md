# Teste da cadeia Markdown → Pandoc → ABNT (ação 7 do plano)

Executado em 22/09/2026 pelo Coordenador (Claude Code, claude-opus-5). Arquivo de teste: `teste-conversao.md`, com 10 citações reais de obras verificadas em `literatura/referencias/candidatas.bib`.

## O que foi usado

| Item | Versão / origem |
|---|---|
| Pandoc | 3.11, instalado com Homebrew em 22/09/2026 |
| Estilos CSL | Repositório oficial `citation-style-language/styles`, commit `c7de5be` (15/05/2025): variante genérica da ABNT e as variantes UFPR, UFRGS e UFS, em `redacao/estilos/` |
| Bibliografia | `literatura/referencias/candidatas.bib` (metadados conferidos por agente; **não** é o `referencias.bib` do Zotero) |

Comando:

```
pandoc redacao/teste-abnt/teste-conversao.md --citeproc \
  --bibliography=literatura/referencias/candidatas.bib \
  --csl=redacao/estilos/<estilo>.csl -o saida.docx
```

## Resultado

**A cadeia funciona.** O `.docx` foi gerado, as citações no texto saíram no formato autor-data e a lista de referências foi montada em ordem alfabética, com sobrenome em maiúsculas, `et al.`, volume, número e páginas.

## Problemas encontrados

| # | Problema | Onde | Encaminhamento |
|---|---|---|---|
| 1 | O estilo **genérico** da ABNT **não imprime o nome do evento** em trabalhos de conferência: sai "In: 2024." mesmo com `booktitle` preenchido. Atinge muitas obras deste projeto (ICLR, NeurIPS, ICAPS, AAAI) | Estilo genérico | Usar a variante **UFPR**, que imprime o evento e o "Anais..."; ela tem, em troca, falhas de espaçamento (".Anais... ,") |
| 2 | Citação entre parênteses sai como "(Rice, 1976)". A NBR 10520 pede o sobrenome em maiúsculas quando a citação está dentro dos parênteses. Nenhuma das quatro variantes testadas faz isso | Todas as variantes | `[A CONFIRMAR]` na norma pelo autor. Se confirmado, é ajuste no CSL ou no acabamento final |
| 3 | O próprio arquivo do estilo genérico declara seguir a **NBR 6023 de 2002**; a edição vigente é posterior | `associacao-brasileira-de-normas-tecnicas.csl` | `[A CONFIRMAR]` a edição vigente e o quanto a diferença importa |
| 4 | O Pandoc converte títulos do BibTeX para caixa de sentença, salvo o que estiver entre chaves. Siglas já estão protegidas (`{PDDL}`, `{ICLR}`), mas nomes de eventos perdem maiúsculas em alguns estilos | Conversão | Manter a proteção por chaves; conferir na saída, não no `.bib` |
| 5 | Obras sem editora ou local saem com `[S.l.]` | Estilo genérico | Completar os campos quando a fonte primária tiver |

## Recomendação

Corpo em Markdown e conversão com Pandoc **dão conta do texto e das referências**. O acabamento final (capa, folha de rosto, sumário, listas, numeração de seções segundo a NBR 6024) ainda não foi testado e é o ponto em que o Word deve entrar. Sugestão para a Fase 6: gerar o corpo com Pandoc usando a variante UFPR, revisar a lista de referências à mão contra a norma e montar os elementos pré-textuais no Word.

**Pendência que bloqueia o uso real:** o `referencias.bib` do Zotero não existe. Este teste usou o `candidatas.bib`, e por isso o script `literatura/scripts/checar_citacoes.py` classifica as 10 chaves como `pendente-zotero` e marca o texto como não citável — comportamento correto.
