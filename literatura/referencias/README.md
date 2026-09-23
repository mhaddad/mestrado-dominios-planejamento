# Referências

Base de referências do projeto, em BibTeX, citada no texto em Markdown por chave (`[@chave]`). **Sem Zotero** (decisão do autor, 23/09/2026): a revisão das referências é feita no próprio repositório.

## Regra central

**Só se cita uma chave que existe no `referencias.bib`.** Ele contém apenas obras com metadados conferidos na fonte primária **e** aprovadas pelo autor. Modelos de linguagem inventam citações plausíveis; o `referencias.bib` é a barreira contra isso.

## Fluxo

```
busca → triagem → verificação no registro primário → candidatas.bib
                                                       │
                                  revisão do autor em revisao-referencias.md
                                                       │
                              promover_referencias.py → referencias.bib → citável
```

1. **`candidatas.bib`**: obras cujos metadados foram conferidos por agente no registro primário (Crossref por DOI, arXiv, anais oficiais). O BibTeX vem do registro, não é digitado de memória. **Não é citável.**
2. **`revisao-referencias.md`**: lista de revisão do autor, com cada referência já formatada em ABNT, o status da confirmação da triagem e as discrepâncias encontradas na verificação. O autor marca `[x]` no que aprova.
3. **`referencias.bib`**: gerado por `python3 literatura/scripts/promover_referencias.py` a partir das marcas. **Não editar à mão**; o script o reescreve inteiro a cada execução.

Para conferir se um texto está citável: `python3 literatura/scripts/checar_citacoes.py ARQUIVO.md`. Chave `pendente-revisao` ainda não foi aprovada; chave `ausente` não existe em nenhum `.bib` e não pode ser usada.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `candidatas.bib` | Obras verificadas por agente, aguardando revisão (154 em 23/09/2026) |
| `revisao-referencias.md` | Lista de revisão do autor |
| `referencias.bib` | Obras aprovadas pelo autor — a única fonte citável. Ainda não gerado |
| `candidatas/` | Arquivos parciais gerados pelos verificadores na Fase 1 (histórico) |

## Convenções

- **Chaves estáveis** no formato `sobrenomeANOpalavra` (ex.: `rice1976algorithm`). Não renomear uma chave depois de usada no texto; se for inevitável, trocar em todos os arquivos e registrar em `literatura/protocolo/qc-coordenador.md`.
- **Correções vão para o `candidatas.bib`**, e depois se roda o script de promoção de novo. Nunca corrigir só o `referencias.bib`.
- **Campos completos** exigidos pela NBR 6023 para o tipo de obra. `[A CONFIRMAR]` os campos exatos na edição vigente da norma.
- **Siglas e nomes próprios no título entre chaves** (`{PDDL}`, `{IPC}`), e editoras com "and" no nome entre chaves duplas, para o Pandoc não as partir. Conferir a saída formatada, não só o `.bib`.
- Uma nota de leitura ([modelo](../../templates/nota-leitura.md)) por obra lida, em [../notas-de-leitura/](../notas-de-leitura/), com a mesma chave no campo `citekey`. Obra sem nota não é citável.

## Estilo de citação

Autor-data, como a versão de 2010. Estilo de trabalho: `redacao/estilos/abnt-ufpr.csl` (variante UFPR do CSL da ABNT; a variante genérica não imprime o nome do evento em trabalhos de conferência). Detalhes e limitações em `redacao/teste-abnt/relatorio-teste.md`.
