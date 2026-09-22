---
tipo: nota-de-leitura
eixo: E3
citekey: torralba2017efficient
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://homes.cs.aau.dk/~alto/papers/aij17.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# Efficient Symbolic Search for Cost-Optimal Planning

**Torralba, Á.; Alcázar, V.; Kissmann, P.; Edelkamp, S. · 2017 · Artificial Intelligence 248, 1–44**
**Link/DOI:** https://doi.org/10.1016/j.artint.2016.10.001

## Extração estruturada

- **Problema:** o desenvolvimento de heurísticas explícitas cada vez mais precisas fez a busca simbólica (com *Binary Decision Diagrams*, BDDs) perder espaço na pesquisa de planejamento ótimo; o artigo busca melhorar a eficiência da busca simbólica em dois pontos: computação de imagem (geração de sucessores) e uso de restrições de invariantes de estado para poda.
- **Método:** busca simbólica com BDDs representa **conjuntos** de estados (não estados individuais), permitindo busca bidirecional (progressão e regressão simultâneas) e uniforme por custo. Os autores propõem três métodos de computação de imagem (TR1+, CT, UT) para as relações de transição codificadas como BDDs, e dois métodos (MBDD, e-del) para codificar restrições de invariantes de estado (mutexes) como poda. Implementam essas melhorias no planejador Gamer, resultando em cGamer (*constrained Gamer*), com busca bidirecional por custo uniforme.
- **Dados/benchmarks:** domínios padrão de IPC para planejamento ótimo (custo mínimo); comparação com busca explícita (A* com LM-cut) e com o planejador Gamer original.
- **Resultado principal:** cGamer com busca bidirecional por custo uniforme supera a busca heurística explícita com LM-cut em muitos domínios; a busca simbólica cega (sem heurística) ainda supera planejadores heurísticos em vários domínios, o que os autores descrevem como surpreendente após anos de pesquisa em heurísticas refinadas; cGamer ficou em segundo lugar na IPC 2014 entre planejadores baseados em busca simbólica.
- **Relação com a dissertação de 2010:**
  - **A6 (detalha/corrige):** a obra descreve busca simbólica como uma família de técnicas ortogonal às categorias de busca no espaço de estados descritas em 2010. O próprio artigo classifica os algoritmos de busca no espaço de estados por **direção** — "progression" (estado inicial → objetivo, equivalente ao *forward-chaining* de 2010) e "regression" (objetivo → estado inicial, próxima do *plan-space*/*backward-chaining*) — e por **representação**: busca explícita (estado a estado) vs. busca simbólica (conjuntos de estados via BDD). A taxonomia de 2010 mistura essas duas dimensões (direção da busca e representação/estrutura de dados) em seis categorias planas, sem espaço para "busca simbólica" como dimensão própria. Um planejador simbólico bidirecional como o cGamer não se encaixa em nenhuma das seis categorias de A2/A6 sem forçar a classificação.
  - **F4 (evidencia a fragilidade):** o artigo mostra que regressão e busca bidirecional, tratadas em 2010 sob a categoria ampla "*Plan-Space*"/"*Total-order*", têm, na prática de 2017, formulações e desempenho muito distintos dependendo de estarem associadas a busca explícita ou simbólica — outro indício de que a taxonomia de seis categorias de 2010 é discutível e demanda subtécnicas mais finas.

## Pontos relevantes para o projeto

- Fonte de referência da busca simbólica para planejamento ótimo em custo, citada como família central do eixo E3; útil para qualquer nota futura sobre planejadores simbólicos ou sobre Gamer/MIPS.
- Fornece definição explícita e citável das direções de busca "progression" e "regression" em planejamento clássico — útil para justificar, com trecho literal, a distinção entre *forward-chaining* e *plan-space*/*backward-chaining* usada (de forma imprecisa) em 2010.
- Mostra evidência empírica de que busca cega (sem heurística) pode superar busca heurística em vários domínios quando bem implementada simbolicamente — ponto relevante para F5 (eficiência reduzida a cobertura), pois reforça que comparações de "técnica vencedora por domínio" dependem fortemente de detalhes de implementação, não só da categoria abstrata de técnica.
- Conecta-se à nota sobre lequen2026planner (Planner Museum), que também situa símbolos de busca simbólica/portfólios híbridos entre os planejadores mais competitivos das IPCs recentes.

## Marcações

- `[FATO]` A obra define progressão e regressão como as duas direções clássicas de busca no espaço de estados, e busca bidirecional como uma terceira opção que combina ambas (Seção 1, Introdução).
- `[FATO]` cGamer, com busca simbólica bidirecional por custo uniforme, supera a busca heurística explícita com LM-cut em muitos domínios testados, e obteve o segundo lugar na IPC 2014 (Resumo; Seção 7, Discussão).
- `[HIPÓTESE]` A categoria "*Plan-Space*" de 2010, ao agrupar SGPlan, SATPlan e MAXPLAN, provavelmente não distinguia direção de busca (regressão) de representação de estado (simbólica vs. explícita) — dimensões que esta obra trata como ortogonais e que ajudam a explicar por que planejadores tão diferentes (SAT, busca simbólica, POCL) acabaram sob o mesmo rótulo em 2010.

## Trechos literais

1. "State-space search algorithms can be classified by the direction in which they traverse the search space: progression or regression. In progression, search is performed in forward direction, from the initial state towards the goal. In regression, backward search is performed from the set of goal states towards the initial state." (Seção 1, Introdução)
2. "With these enhancements, the best variant of cGamer, which uses bidirectional uniform-cost search, outperforms current explicit-state heuristic search in most domains." (Resumo)
3. "The good results of symbolic blind search are especially surprising as after many years of research of finding refined heuristics for AI planning, this form of blind search still outperforms heuristic search planners on many domains." (Seção 7, Discussão)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://homes.cs.aau.dk/~alto/papers/aij17.pdf. Conferência humana: pendente.
