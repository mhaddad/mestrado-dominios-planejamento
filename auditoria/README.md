# Fase 2 — Auditoria da versão original

**Objetivo:** classificar criticamente cada afirmação substantiva da dissertação como **mantém / reformula / descarta**, com justificativa. Roda em paralelo à Fase 1.
**Critério de conclusão:** todas as afirmações classificadas e plano de reexecução definido.

## Arquivos previstos

| Arquivo | Conteúdo |
|---|---|
| `afirmacoes.csv` | Tabela de auditoria: `id` (AF-NNN), `origem` (ID no bloco de extração), `linha` e `secao` (local em `data/2010/extraido/texto.md`), `tipo`, `trecho` (cópia literal), `resumo`, `observacao`, `rotulo_fase1` (A1–A8, T1–T6), `classificacao` (mantém / reformula / descarta), `justificativa`, `acao`, `conferencia_numerica`. Gerada por `scripts/consolidar_extracao.py` a partir de `extracao/bloco-*.csv` |
| `extracao/` | Extração por bloco do texto (Onda 1 da Fase 2) e conferência numérica (Onda 2) |
| `taxonomia-tecnicas.md` | Nova taxonomia de técnicas, compatível com a literatura atual (F4) |
| `condicoes-de-execucao-2010.md` | Como os dados da 5ª etapa foram obtidos (F6). **Feito na Fase 0.** |
| `achados-fase0.md` | Pontos a examinar, levantados ao extrair e conferir o dataset (G1–G10). **Feito na Fase 0.** |
| `reexecucao.md` | O que precisa ser reexecutado na Fase 3 |
| `m1-orientador.md` | Material do Marco M1 |

Enquanto `afirmacoes.csv` não existir, a tabela de auditoria semente (A1–A4) fica na seção 7 do [plano](../plan/plano-revisao-dissertacao.md). Ao criar o CSV, mova as linhas para lá e deixe um ponteiro no plano.

Os IDs AF-NNN seguem a ordem das linhas no texto. Depois que a classificação começar, **não acrescente blocos novos sem renumerar com cuidado**: o script preserva a classificação pela coluna `origem`, mas os AF-NNN mudam se entrarem afirmações no meio.
