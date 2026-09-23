# Fase 2 — Auditoria da versão original

**Objetivo:** classificar criticamente cada afirmação substantiva da dissertação como **mantém / reformula / descarta**, com justificativa. Roda em paralelo à Fase 1.
**Critério de conclusão:** todas as afirmações classificadas e plano de reexecução definido.

## Arquivos previstos

| Arquivo | Conteúdo |
|---|---|
| `afirmacoes.csv` | Tabela de auditoria: `id` (AF-NNN), `origem` (ID no bloco de extração), `linha` e `secao` (local em `data/2010/extraido/texto.md`), `tipo`, `trecho` (cópia literal), `resumo`, `observacao`, `rotulo_fase1` (A1–A8, T1–T6), `classificacao` (mantém / reformula / descarta), `justificativa`, `acao`, `conferencia_numerica`. Gerada por `scripts/consolidar_extracao.py` a partir de `extracao/bloco-*.csv` |
| `extracao/` | Extração por bloco do texto (Onda 1 da Fase 2) e conferência numérica (Onda 2) |
| `taxonomia-tecnicas.md` | Nova taxonomia de técnicas em quatro dimensões (F4). **Feito na Fase 2.** |
| `condicoes-de-execucao-2010.md` | Como os dados da 5ª etapa foram obtidos (F6). **Feito na Fase 0.** |
| `achados-fase0.md` | Pontos a examinar, levantados ao extrair e conferir o dataset (G1–G10). **Feito na Fase 0.** |
| `reexecucao.md` | O que precisa ser reexecutado na Fase 3 (R-01 a R-31). **Feito na Fase 2.** |
| `relatorio-auditoria.md` | Relatório de auditoria (entregável da Fase 2) |
| `taxonomia/fontes-planejadores.csv` | O que cada um dos 10 planejadores de 2010 diz de si na fonte primária |
| `scripts/` | `consolidar_extracao.py` (gera `afirmacoes.csv`), `conferir_medias.py`, `conferir_rankings.py`, `resumir_auditoria.py` |
| `m1-orientador.md` | Material do Marco M1 (rascunho para o autor revisar) |

A tabela semente do plano foi substituída por `afirmacoes.csv` em 23/09/2026; o plano deixa um ponteiro.

Os IDs AF-NNN seguem a ordem das linhas no texto. Depois que a classificação começar, **não acrescente blocos novos sem renumerar com cuidado**: o script preserva a classificação pela coluna `origem`, mas os AF-NNN mudam se entrarem afirmações no meio.
