# Referências

Base de referências do projeto. O **Zotero** é a fonte; o que entra aqui é a **exportação em BibTeX** (`.bib`), que o texto em Markdown cita por chave (`[@chave]`).

## Regra central

**O `.bib` contém só referências verificadas na fonte primária.** Uma referência "a verificar" não entra aqui: fica na lista da seção 13 do [plano](../../plan/plano-revisao-dissertacao.md) até ser conferida. Modelos de linguagem inventam citações plausíveis; o `.bib` verificado é a barreira contra isso.

Consequência para quem escreve (pessoa ou agente): **só se cita uma chave que existe no `.bib`.** Se a obra não está lá, ela não foi verificada e não pode ser citada no texto.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `referencias.bib` | Exportação do Zotero com as referências verificadas. Um único arquivo, para o Pandoc. |

O arquivo ainda não existe: é criado quando a primeira referência for verificada (Fase 1).

## Convenções

- **Chaves de citação estáveis**, no formato do Zotero com Better BibTeX se disponível (por exemplo `rice1976algorithm`). Não renomear uma chave depois que ela for usada no texto.
- **Campos completos** exigidos pela NBR 6023 para o tipo de obra: autores, título, veículo, ano, volume, páginas, DOI ou URL. `[A CONFIRMAR]` os campos exatos, na edição vigente da norma.
- **Nomes de autores** e **títulos com maiúsculas a proteger** (siglas como IPC, PDDL) com o mesmo cuidado que a norma exigir; conferir a saída formatada, não só o `.bib`.
- **Nunca editar o `.bib` à mão** para "arrumar" a saída formatada. Corrigir no Zotero e exportar de novo, para que Zotero e repositório não divirjam.
- Uma nota de leitura ([modelo](../../templates/nota-leitura.md)) por obra lida, em [../notas-de-leitura/](../notas-de-leitura/), com a mesma chave no campo `citekey`.

## Estilo de citação

O texto usa citação autor-data, como a versão de 2010 (`(SIAU e CAO, 2006)`). O estilo é definido por um arquivo CSL aplicado na conversão. `[A CONFIRMAR]` Existência e adequação de um CSL para a ABNT vigente (NBR 10520 e 6023): testar com 5 a 10 referências reais antes de adotar.
