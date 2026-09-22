---
tipo: nota-de-leitura
eixo: E3
citekey: helmert2006fast
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/view/10457/25067
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A2, A6]
fragilidades: [F4]
perguntas: [Q1]
---

# The Fast Downward Planning System

**Helmert, M. · 2006 · Journal of Artificial Intelligence Research 26, 191–246**
**Link/DOI:** https://doi.org/10.1613/jair.1705

## Extração estruturada

- **Problema:** como resolver tarefas de planejamento clássico (PDDL2.2 proposicional, incluindo ADL e axiomas) com eficiência competitiva, explorando estrutura causal do domínio em vez de tratar o problema como um conjunto plano de proposições.
- **Método:** o planejador Fast Downward traduz a tarefa PDDL para uma representação de variáveis multivaloradas (*multi-valued planning tasks*, MPT), compila grafos causais e grafos de transição de domínio, e busca no espaço de estados do mundo ("progression") usando uma heurística nova (*causal graph heuristic*) computada por decomposição hierárquica do grafo causal. A busca principal é *greedy best-first search*; há também *multi-heuristic best-first search* (combinando heurística causal e heurística FF) e um algoritmo não heurístico, *focused iterative-broadening search*.
- **Dados/benchmarks:** 1442 tarefas proposicionais das quatro primeiras IPCs (AIPS 1998, 2000, 2002; ICAPS 2004), divididas em domínios STRIPS, ADL e PDDL2.2 completo (Seção 7.1).
- **Resultado principal:** Fast Downward venceu a faixa clássica não otimizante da IPC-4 (2004) e superou FF e LPG nos *benchmarks* das três primeiras IPCs (citando Helmert 2004); bom desempenho em quase todo o conjunto de *benchmarks* testado (Seção 7).
- **Relação com a dissertação de 2010:**
  - **A6 (corrige):** 2010 classificou Fast Downward como técnica *Hierarchical*. A própria obra descreve o planejador como "a classical planning system based on the ideas of heuristic forward search and hierarchical problem decomposition" e explicita que, "like FF, Fast Downward is a heuristic progression planner, i. e., it computes plans by heuristic search in the space of world states reachable from the initial situation" (Seção 3, p. 202). Ou seja: a busca central é *forward/progression* guiada por heurística — a mesma família de FF e LAMA —, e a "decomposição hierárquica" é usada apenas para **calcular a heurística** (o grafo causal), não é uma técnica hierárquica de planejamento no sentido HTN/ABSTRIPS. Rotular Fast Downward como *Hierarchical* tout court, sem essa distinção, mistura o papel do grafo causal (auxiliar da heurística) com o algoritmo de busca (heurístico progressivo). A obra também situa criticamente o próprio uso do termo: "the heuristic evaluator proceeds 'downward' in so far as it tries to solve planning tasks in the hierarchical fashion" — o nome do planejador é uma metáfora para o cálculo da heurística, não uma alegação de que a busca de planos é hierárquica.
  - **A2 (confirma parcialmente):** reforça a centralidade de *Heuristic Search* como categoria de técnica (Fast Downward é heurística progressiva), mas mostra que essa categoria e "Hierarchical" não são mutuamente exclusivas nem bem definidas em 2010 — Fast Downward é heurística **e** usa decomposição hierárquica só na heurística, o que 2010 não distingue.
  - **F4 (evidencia a fragilidade):** confirma que a taxonomia de técnicas usada em 2010 é discutível, pois um mesmo planejador combina elementos de mais de uma "técnica" citada em A2, dependendo de qual componente (busca vs. heurística) se olha.

## Pontos relevantes para o projeto

- Distinção clara, na própria fonte primária, entre "busca por progressão heurística" (algoritmo de busca) e "decomposição hierárquica do grafo causal" (mecanismo interno da heurística) — corrige a base para revisar A6/F4.
- Fast Downward é explicitamente apresentado como sucessor de FF ("Fast" vem de FF) e antecessor da linhagem que leva a LAMA — útil para reconstruir a árvore genealógica de técnicas do eixo E3.
- A arquitetura em três fases (tradução → compilação de conhecimento → busca) é uma boa base para descrever "como a própria obra descreve a técnica" em qualquer nota futura sobre planejadores derivados de Fast Downward.
- O artigo já assinala, na seção de trabalhos futuros, interesse em revisitar a abordagem hierárquica "since the work of Knoblock (1994) and Bacchus and Yang (1994), little work has been published" — mostra que a linha "hierárquica" clássica (HTN) é uma tradição distinta da que Fast Downward ocupa.

## Marcações

- `[FATO]` Fast Downward é descrito pelos próprios autores como planejador de busca heurística progressiva ("heuristic progression planner"), com decomposição hierárquica restrita ao cálculo da heurística causal (Seção 3, p. 202).
- `[FATO]` Fast Downward venceu a faixa clássica da IPC-4 (2004) e superou FF/LPG nos *benchmarks* das IPCs 1–3 (Resumo; Seção 7).
- `[HIPÓTESE]` A classificação de 2010 ("Hierarchical") provavelmente decorre do nome do planejador e da menção a "hierarchical decompositions" no resumo, sem diferenciar heurística de algoritmo de busca — um erro de leitura superficial da fonte primária, não uma leitura equivocada de terceiros.

## Trechos literais

1. "Fast Downward is a classical planning system based on the ideas of heuristic forward search and hierarchical problem decomposition." (Seção 3, p. 202)
2. "Like FF, Fast Downward is a heuristic progression planner, i. e., it computes plans by heuristic search in the space of world states reachable from the initial situation." (Seção 3, p. 202)
3. "The other central idea is the use of hierarchical decompositions within a heuristic planning framework." (Seção 8, Summary and Discussion, p. 242)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/view/10457/25067 (recuperado como PostScript via `curl`, convertido a PDF com Ghostscript e extraído com `pdftotext -layout`). Conferência humana: pendente.
