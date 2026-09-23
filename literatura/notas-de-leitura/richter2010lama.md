---
tipo: nota-de-leitura
eixo: E3
citekey: richter2010lama
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/view/10667/25495
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A2, A6]
fragilidades: [F1, F4]
perguntas: [Q1]
---

# The LAMA Planner: Guiding Cost-Based Anytime Planning with Landmarks

**Richter, S.; Westphal, M. · 2010 · Journal of Artificial Intelligence Research 39, 127–177**
**Link/DOI:** https://doi.org/10.1613/jair.2972

## Extração estruturada

- **Problema:** como usar *landmarks* (fórmulas proposicionais que precisam ser verdadeiras em todo plano solução) para guiar busca heurística sensível a custo de ação, produzindo planos de boa qualidade dentro do tempo disponível (planejamento *anytime*).
- **Método:** LAMA constrói-se sobre o Fast Downward, substituindo a heurística de grafo causal por uma combinação da heurística FF (variante sensível a custo) com uma pseudo-heurística derivada de *landmarks*; usa variáveis de domínio finito (não binárias) e *multi-heuristic search*. A busca inicial é *greedy best-first*; depois disso, uma sequência de buscas A* ponderado com pesos decrescentes é reiniciada a partir do estado inicial cada vez que uma solução melhor é encontrada (busca *anytime*).
- **Dados/benchmarks:** domínios da IPC 2008 (Elevators, Cyber Security, Openstacks, PARC Printer, Peg Solitaire, Scanalyzer, Sokoban, Transport, Woodworking) e domínios de competições anteriores (Seção 7).
- **Resultado principal:** LAMA venceu a faixa satisficing sequencial da IPC 2008 por margem substancial, resultado não esperado pelos autores; o uso de *landmarks* melhora o desempenho, mas a incorporação de custo de ação na heurística por si só reduz cobertura — o ganho vem da combinação de *landmarks* com a estimativa de custo e da busca A* iterada com pesos decrescentes (Resumo; Seção 7.1).
- **Relação com a dissertação de 2010:**
  - **F1 (evidencia a fragilidade — lacuna de revisão):** LAMA está listado explicitamente como uma das lacunas de revisão de 2010 (plano, seção 4). A leitura confirma que LAMA é um planejador de busca heurística *state-of-the-art* desde 2008/2010, construído diretamente sobre Fast Downward — ou seja, uma extensão direta de uma das dez técnicas já estudadas em 2010, publicada no mesmo ano da dissertação. Sua ausência é uma lacuna real e concreta, não hipotética.
  - **A6 (reforça a correção de Fast Downward):** LAMA é descrito como "a classical planning system based on heuristic forward search" que "follows in the footsteps of HSP, FF, and Fast Downward". Isso corrobora, por uma segunda fonte primária independente, que a linhagem Fast Downward → LAMA pertence à família de busca heurística progressiva (*forward/progression search*), não à categoria "Hierarchical" isolada usada em 2010 para Fast Downward.
  - **A2 (confirma):** reforça *Heuristic Search* como categoria dominante e ainda mostra a importância de *landmarks* como fonte adicional de controle de busca — um elemento de "técnica" que a taxonomia A2/F4 de 2010 (seis categorias fixas) não captura como dimensão própria.
  - **F4 (evidencia a fragilidade):** landmarks aparecem tanto como heurística quanto como mecanismo de controle de busca (via "preferred operators"), o que não se encaixa perfeitamente em nenhuma das seis categorias de A2 — mais um indício de que a taxonomia de 2010 precisa de subtécnicas (ligação com T3 dos trabalhos futuros de 2010, fora do escopo desta nota).

## Pontos relevantes para o projeto

- Confirma, com uma segunda fonte independente de Helmert (2006), que a classificação de Fast Downward como "Hierarchical" em 2010 não reflete como os próprios criadores da linhagem descrevem a técnica: é busca heurística progressiva.
- Descreve landmarks como mecanismo de dupla função (heurística + controle de busca via *preferred operators*), relevante para detalhar a taxonomia de técnicas (T3 nos trabalhos futuros de 2010).
- A seção 7.2 discute o domínio "Elevators" da IPC 2008 — mesmo nome do domínio de validação Elevator usado em 2010, mas **atenção**: é a formulação de 2008 (com custos de ação e variantes específicas da competição), não necessariamente idêntica à formulação usada em 2010; qualquer comparação direta exigiria conferir se são a mesma codificação PDDL.
- IPC 2008 já discutia explicitamente os limites de usar só cobertura (IPC score) vs. qualidade de plano — tema direto de A7/F5 de 2010, embora este não seja o foco desta nota (LAMA está fora do escopo A7/F5 do lote atual).

## Marcações

- `[FATO]` LAMA venceu a faixa satisficing sequencial da IPC 2008 e é descrito como planejador de busca heurística progressiva construído sobre Fast Downward (Resumo; Introdução).
- `[FATO]` O uso de *landmarks* melhora desempenho, mas a heurística sensível a custo isoladamente reduz cobertura; a combinação de ambos com busca iterada por pesos decrescentes recupera o desempenho (Seção 7.1, "Overview of Results").
- `[HIPÓTESE]` A ausência de LAMA no corpus de 2010, sendo publicada no mesmo ano da dissertação, provavelmente reflete o momento de corte da pesquisa bibliográfica de 2010, não uma omissão deliberada — mas isso é uma lacuna real que a revisão atual deve preencher (ligação com F1 e Q1).

## Trechos literais

1. "LAMA is a classical planning system based on heuristic forward search. [...] It follows in the footsteps of HSP, FF, and Fast Downward and uses their earlier work in many respects." (Seção 1, p. 127/191)
2. "LAMA showed best performance among all planners in the sequential satisficing track of the International Planning Competition 2008." (Resumo)
3. "Overall, we find that using landmarks improves performance, whereas the incorporation of action costs into the heuristic estimators proves not to be beneficial." (Resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/view/10667/25495 (recuperado como PostScript via `curl`, convertido a PDF com Ghostscript e extraído com `pdftotext -layout`). Conferência humana: pendente.
