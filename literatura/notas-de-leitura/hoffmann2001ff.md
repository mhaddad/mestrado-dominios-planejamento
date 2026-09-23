---
tipo: nota-de-leitura
eixo: E3
citekey: hoffmann2001ff
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/download/10276/24498
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026 (aprovação delegada ao Coordenador)
afirmacoes-2010: [A2, A6]
fragilidades: [F4]
perguntas: [Q1]
---

# The FF Planning System: Fast Plan Generation Through Heuristic Search

**Hoffmann, J.; Nebel, B. · 2001 · Journal of Artificial Intelligence Research 14, 253–302**
**Link/DOI:** https://doi.org/10.1613/jair.855

## Extração estruturada

- **Problema:** gerar planos rapidamente em domínios STRIPS por busca heurística no espaço de estados, sem assumir independência entre fatos (diferença em relação à heurística do HSP).
- **Método:** o planejador FF usa busca progressiva no espaço de estados do mundo (*forward state space search*), com uma heurística que estima a distância ao objetivo ignorando as listas de remoção das ações (*relaxed plan heuristic*), extraída de um grafo de planos construído para o problema relaxado. A busca principal é *enforced hill-climbing*, combinando busca local sistemática; quando falha, o sistema recorre a uma busca *best-first* completa.
- **Dados/benchmarks:** domínios da AIPS-2000 (onde FF foi o planejador automático mais bem-sucedido) e outros domínios de referência comparados ao HSP.
- **Resultado principal:** FF superou todos os sistemas totalmente automáticos na AIPS-2000 e foi indicado "Distinguished Performance Planning System".
- **Relação com a dissertação de 2010:**
  - **A6 (corrige):** 2010 classifica FF como State-Space, Total-order, Forward-chaining, Graph-based e Heurist Search (Tabela 4). A fonte confirma diretamente State-Space, Forward-chaining e Heuristic Search — mas o rótulo "Graph-based" é impreciso pelo mesmo motivo identificado na nota sobre Fast Downward (helmert2006fast): o grafo de planos (na verdade, um Graphplan aplicado ao problema *relaxado*) é usado só para calcular a heurística, não para a busca principal, que é *state-space* pura.
  - **A2 (confirma):** reforça *Heuristic Search* e *Forward-chaining* (aqui chamado de "forward state space search") como técnicas centrais de FF, consistente com a leitura de A2 em 2010.

## Pontos relevantes para o projeto

- Mesmo padrão de FD/Fast Downward: "Graph-based" aparece como mecanismo interno da heurística (grafo de planos relaxado), não como algoritmo de busca — evidência adicional de que a dimensão "algoritmo de busca" e a dimensão "tipo de heurística" da Fase 2 precisam ser separadas, porque 2010 as mistura em uma única coluna "Graph-based".
- FF é citado como base direta de YAHSP (Vidal, 2004) e de Metric-FF (usado dentro do SGPlan) — útil para a árvore genealógica de técnicas do eixo E3.

## Marcações

- `[FATO]` FF é descrito pelos próprios autores como planejador de busca progressiva no espaço de estados, guiado por heurística de plano relaxado, com *enforced hill-climbing* como busca principal (Resumo, p. 253).
- `[HIPÓTESE]` A classificação "Graph-based" de FF em 2010 provavelmente decorre da menção ao uso de um grafo de planos para calcular a heurística, sem distinguir esse uso do algoritmo de busca principal — o mesmo padrão de leitura superficial identificado para Fast Downward.

## Trechos literais

1. "Like the HSP system, FF relies on forward state space search, using a heuristic that estimates goal distances by ignoring delete lists." (Resumo, p. 253)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/download/10276/24498 (galley PostScript do JAIR, convertido a PDF com Ghostscript e extraído com `pdftotext -layout`; a conversão perdeu ligaturas tipográficas em parte do texto, evitadas no trecho citado). Metadados (DOI, páginas) verificados via Crossref. Conferência humana: pendente.
