---
tipo: nota-de-leitura
eixo: E3
citekey: rintanen2014madagascar
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://users.aalto.fi/~rintanj1/papers/Rintanen14IPC.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# Madagascar: Scalable Planning with SAT

**Rintanen, J. · 2014 · IPC 2014 Planner Abstracts**
**Link/DOI:** https://users.aalto.fi/~rintanj1/papers/Rintanen14IPC.pdf

## Extração estruturada

- **Problema:** como tornar o planejamento como satisfabilidade proposicional (*Planning as Satisfiability*, SAT) escalável a problemas grandes, superando as limitações das implementações da década de 1990 (Kautz & Selman 1996).
- **Método:** o planejador Madagascar (M, Mp ou MpC) traduz a tarefa de planejamento clássico em uma fórmula proposicional Φt = I ∧ T(0,1) ∧ T(1,2) ∧ ... ∧ T(t−1,t) ∧ G, onde cada T(i,i+1) representa as transições possíveis entre os passos de tempo i e i+1 para **todos os fatos e ações simultaneamente**; a fórmula inteira (para um horizonte t) é entregue a um solver de SAT. O artigo discute três componentes: (1) codificações compactas de planos paralelos (∃-step), (2) estratégias de escalonamento dos testes de satisfabilidade para múltiplos valores de t (Algoritmo B, com solvers rodando em paralelo com taxas de CPU geométricas), e (3) heurísticas de SAT especializadas para planejamento.
- **Dados/benchmarks:** não há uma seção de experimentos com tabelas de cobertura no artigo (é um resumo de planejador para o *booklet* da IPC); o texto reporta resultados qualitativos e cita trabalhos anteriores do autor com dados de desempenho.
- **Resultado principal:** a combinação de escalonamento paralelizado dos testes de SAT com codificações compactas de planos paralelos ∃-step eleva a eficiência e escalabilidade do planejamento como SAT a um nível próximo dos melhores planejadores modernos de outros paradigmas de busca, e claramente superior aos planejadores SAT anteriores a ~2004.
- **Relação com a dissertação de 2010:**
  - **A6 (corrige):** 2010 classificou planejadores SAT como *forward-chaining* e SATPlan/MAXPLAN como *plan-space*. A própria obra não descreve o planejamento como SAT nem como busca progressiva (*forward-chaining*, que avança estado a estado a partir do estado inicial) nem como busca no espaço de planos (*plan-space*, que refina planos parciais por ameaças e ordenação causal, à la POCL). O método é fundamentalmente diferente de ambos: a fórmula Φt codifica **todos os passos de tempo de 0 a t de uma vez** e a decide um solver de SAT por busca de atribuição de variáveis — não há uma "cadeia" de estados sendo expandida progressivamente nem uma estrutura explícita de planos parciais sendo refinada. É uma redução do problema de planejamento a um problema de satisfabilidade proposicional, resolvido por algoritmos de SAT (como DPLL/CDCL) que operam sobre a fórmula inteira. Chamar isso de *forward-chaining* confunde a direção "temporal" da codificação (do estado inicial ao horizonte t) com o algoritmo de busca de fato executado (busca de satisfabilidade sobre uma fórmula global, não expansão sequencial de estados).
  - **F4 (evidencia a fragilidade):** a obra situa a família SAT como uma abordagem transversal — usada também em model checking, roteamento de FPGA, geração de padrões de teste e diagnóstico —, reforçando que "Planning as Satisfiability" é uma categoria de técnica com identidade própria (redução a SAT + escalonamento de solvers), incompatível com o enquadramento de 2010 em seis categorias que não incluem SAT como classe própria.

## Pontos relevantes para o projeto

- Fonte primária direta para corrigir a taxonomia de SAT em A6/F4: o mecanismo central é "SAT-based planning" (redução a satisfabilidade proposicional com codificação de passos paralelos), não *forward-chaining* nem *plan-space*.
- O artigo é curto (resumo de planejador da IPC, 5 páginas na fonte), então a leitura cobre o artigo inteiro — não há seções de introdução/método/resultados/conclusão tão separadas quanto em um artigo de periódico; a nota reflete essa limitação de formato.
- Detalha o papel dos *mutexes* (invariantes binários), herdados do GraphPlan, como acelerador do SAT-solving — ponto de conexão histórica entre a família SAT e a família de grafos de planejamento (GraphPlan), relevante para reconstruir a árvore de técnicas do eixo E3.
- Não fornece números de cobertura próprios com trecho citável neste artigo; qualquer número de desempenho do Madagascar/Mp/MpC precisaria vir de outra fonte (ex.: resultados de IPC) antes de entrar no texto da dissertação revisada.

## Marcações

- `[FATO]` A codificação SAT do problema de planejamento representa transições entre todos os passos de tempo simultaneamente em uma única fórmula Φt, decidida por um solver de SAT — não é uma expansão progressiva de estados nem um refinamento de planos parciais (Seção "Background").
- `[FATO]` O planejador Madagascar combina codificações de planos paralelos ∃-step, escalonamento paralelizado de solvers de SAT (Algoritmo B) e heurísticas de SAT especializadas para planejamento (Resumo; "Scheduling the Solution of the SAT Instances").
- `[HIPÓTESE]` A classificação de 2010 (SAT = *forward-chaining*; SATPlan/MAXPLAN = *plan-space*) provavelmente decorre de associar a direção temporal da codificação SAT (do estado inicial ao horizonte) à busca *forward*, e a existência de múltiplas ações candidatas por passo à ideia de "espaço de planos" — uma leitura que confunde a estrutura da codificação com o algoritmo de busca real (SAT solving).

## Trechos literais

1. "Planning therefore can be reduced to a sequence of satisfiability tests." (Seção "Background")
2. "The planning system Madagascar [...] implements several of the innovations in planning with SAT, including compact and efficient encodings based on ∃-step plans [...], parallelized/interleaved search strategies [...], powerful invariant algorithms [...], SAT heuristics specialized for planning." (Resumo/Introdução)
3. "[This] lifts the efficiency and scalability of SAT-based planning close to the level of the best modern planners that use other search paradigms, and clearly past planners prior to about 2004." (Seção final, antes das referências)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://users.aalto.fi/~rintanj1/papers/Rintanen14IPC.pdf. Conferência humana: pendente.
