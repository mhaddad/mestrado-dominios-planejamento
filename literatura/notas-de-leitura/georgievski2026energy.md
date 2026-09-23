---
tipo: nota-de-leitura
eixo: E6
citekey: georgievski2026energy
prioridade: C
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2601.21967 (PDF baixado, lidos resumo, introdução e conclusão - seção 5)
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5]
fragilidades: [F5]
perguntas: [Q2]
---

# The Energy Impact of Domain Model Design in Classical Planning

**Georgievski, I.; Tekin, S.; Aiello, M. · 2026 · preprint (arXiv), DOI 10.1145/3793653.3793791**
**Link/DOI:** https://doi.org/10.1145/3793653.3793791 (preprint: arXiv:2601.21967)

## Extração estruturada

- **Problema:** a eficiência energética do planejamento automatizado tem recebido pouca atenção, apesar da alta demanda computacional; como o *design* do modelo de domínio (independente do algoritmo) afeta o consumo de energia dos planejadores clássicos.
- **Método:** introduzem um *framework* de configuração de modelo de domínio que permite variação controlada de características como ordenação de elementos, aridade de ações e estados sem saída (*dead-end states*); analisam impactos de energia e tempo de execução em 32 variantes de domínio por *benchmark*, usando cinco domínios de referência e cinco planejadores do estado da arte.
- **Dados/benchmarks:** cinco domínios de *benchmark* clássicos, cinco planejadores (incluindo variantes baseadas em Fast Downward e LAPKT), 32 variantes de configuração de domínio por *benchmark*.
- **Resultado principal:** modificações no nível do domínio produzem diferenças de energia mensuráveis entre planejadores, e o consumo de energia nem sempre se correlaciona com o tempo de execução; aridade de ação redundante aumenta consumo de energia por fatores de 2 a 12 e pode levar a falhas; introdução de estados sem saída (*dead ends*) tem efeitos que vão de desprezíveis a catastróficos, dependendo mais da estrutura do domínio do que da arquitetura do planejador.
- **Relação com a dissertação de 2010:** **confirma e amplia A5** (diagramas/características do domínio afetam o desempenho das técnicas), mas trocando a métrica de desempenho: em vez de cobertura (2010, A7/F5), usa consumo de energia como dimensão de desempenho — mostrando explicitamente que a "eficiência" de um planejador é multidimensional e que **reduzir eficiência a cobertura (F5) esconde efeitos importantes** (ex.: uma configuração pode manter cobertura, mas consumir muito mais energia).

## Pontos relevantes para o projeto

- É o achado mais direto do lote para reforçar, com dado quantitativo recente, a crítica à fragilidade F5 (eficiência = cobertura) de 2010: mostra concretamente que tempo de execução e energia podem divergir, então nenhuma métrica única captura todo o desempenho.
- O *framework* de configuração controlada de características estruturais do domínio (ordenação, aridade, *dead ends*) é conceitualmente próximo ao espírito de medir "características do domínio" de 2010, mas manipulando-as experimentalmente em vez de apenas observá-las — desenho mais forte para causalidade.
- Preprint recente (janeiro de 2026); ainda sem publicação formal confirmada (DOI aponta para ACM, mas não foi verificado se já publicado ou apenas registrado).

## Trechos literais

"Redundant action arity consistently increases energy consumption across planners by factors of 2-12 and can lead to failures; and dead-end introduction produces effects ranging from negligible to catastrophic, driven primarily by domain structure rather than planner architecture" (seção 5, Conclusão).

## Marcações

- `[FATO]` o artigo mede, em cinco domínios e cinco planejadores, que variações controladas no *design* do modelo de domínio produzem diferenças de energia de até 12x, nem sempre correlacionadas com tempo de execução (seção 5).
- `[HIPÓTESE]` interpretação minha: este resultado fortalece a crítica a F5 de forma quantitativa — se cobertura e tempo já eram insuficientes segundo a crítica de 2010, este artigo mostra que nem tempo é suficiente, pois energia pode variar independentemente dele; relevante para propor, na revisão, uma discussão sobre métricas de eficiência multidimensionais (Q2).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e seção 5 (Conclusão) do PDF em https://arxiv.org/pdf/2601.21967 (prioridade C, nota curta). Conferência humana: pendente.
