---
tipo: nota-de-leitura
eixo: E1
citekey: kerschke2019automated
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/pdf/1811.11597
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A3]
fragilidades: [F1, F3]
perguntas: [Q1, Q2]
---

# Automated Algorithm Selection: Survey and Perspectives

**Kerschke, P.; Hoos, H. H.; Neumann, F.; Trautmann, H. · 2019 · Evolutionary Computation (pré-print arXiv:1811.11597)**
**Link/DOI:** https://doi.org/10.1162/evco_a_00242

## Extração estruturada

- **Problema:** revisar e unificar o estado da arte em seleção automática de algoritmo por instância (*per-instance algorithm selection*), cobrindo problemas discretos e contínuos, e mapear os conjuntos de *features* usados em cada domínio de aplicação.
- **Método:** *survey* estruturado: define formalmente o problema de seleção por instância generalizando Rice (1976), distingue-o de problemas correlatos (configuração de algoritmo, portfólios paralelos, escalonamento de algoritmo), revisa conjuntos de *features* por problema (SAT, planejamento, TSP, MIP etc.) e sistemas de seleção representativos, discente e continuum.
- **Dados/benchmarks:** não aplicável (*survey*); cita *benchmarks* de referência de cada sistema revisado (ASLib etc.).
- **Resultado principal:** mapeia a evolução dos conjuntos de *features* para planejamento — de Howe et al. (1999, cinco *features* simples) a Roberts et al. (2008, 41 *features* incluindo grafo causal) a Cenamor et al. (2013, 47 *features* de grafo causal/grafos de transição de domínio) a Fawcett et al. (2014, 311 *features*, a coleção mais extensa) — e dos sistemas de seleção por domínio (PbP/PbP2, ASAP) e por instância (IBaCoP2, Planzilla) em planejamento.
- **Relação com a dissertação de 2010:**
  - **F1 (evidencia a lacuna de forma abrangente):** a linhagem completa de *features* de planejamento traçada pelo *survey* (Howe et al. 1999 → Roberts et al. 2008 → Cenamor et al. 2013 → Fawcett et al. 2014) já estava, em sua maior parte, publicada e ativa **antes** de 2010; nenhuma dessas obras é citada na dissertação, que usa como alternativa uma linha isolada de modelagem UML/itSIMPLE. Confirma, com evidência bibliográfica direta, que F1 (lacunas de revisão, incluindo Roberts & Howe) é procedente.
  - **Q2 (resposta da literatura, útil para contextualizar 2010):** o *survey* mostra que a comunidade de planejamento convergiu para *features* derivadas de PDDL, do grafo causal e de representações SAS+/FDR (Fast Downward) como base de seleção de planejador — não para métricas de diagramas UML de casos de uso/classes/estados como em 2010. Isso não invalida a pergunta de 2010, mas mostra que a resposta dominante do campo, entre 1999 e 2019, veio de outra família de características.
  - **A3 (corrige, com base agregada):** ao descrever PbP/ASAP (seleção por domínio) e IBaCoP2/Planzilla (seleção por instância) lado a lado, o *survey* mostra que a comunidade migrou progressivamente de seleção por domínio para seleção por instância, e que a seleção por instância tende a superar a seleção só por domínio — evidência agregada contra a suficiência de "só características do domínio, independentemente do problema" (A3).
  - **A1 (confirma o princípio, generalizado):** reafirma, com a formalização mais recente do campo, que características de instâncias (não necessariamente do domínio inteiro) sustentam a seleção eficaz de algoritmo/planejador, alinhado ao princípio geral de A1, mas deslocando a granularidade de "domínio" para "instância".

## Pontos relevantes para o projeto

- A distinção formal entre VBS (*virtual best solver*/oráculo), SBS (*single best solver*) e o "*VBS-SBS gap*" dá vocabulário preciso para medir o ganho potencial de um ranking de planejadores por domínio — útil para reformular quantitativamente a proposta de 2010.
- A seção de *features* de planejamento (Roberts et al. 2008; Cenamor et al. 2013; Fawcett et al. 2014) é, dentro deste lote, o resumo mais completo e mais recente do "estado da arte" de *features* estruturais de domínio/instância em planejamento — referência central para qualquer comparação futura com as métricas UML de 2010.
- O *survey* explicitamente desaconselha usar "*portfolio*" como sinônimo de "seletor de algoritmo por instância", alertando para confusão terminológica — reforça a fragilidade F4 sobre imprecisão de taxonomia, agora generalizada para além de planejamento.

## Trechos literais

1. "This problem has already been considered in the seminal work by Rice (1976), but it took several decades before practical per-instance algorithm selection methods became available" (Seção 1, Introdução)
2. "Howe et al. (1999) were among the first to characterise AI planning instances by simple features, namely, the number of actions, predicates, objects, goals, as well as the number of predicates used to specify the initial state." (Seção 3, AI planning)
3. "IBACOP2 uses 12 component planners... A random forest model... forms the core of the algorithm selection strategy. This model is used to predict whether a component planner will solve a given problem instance within a fixed time limit, based on a set of 35 cheaply computable, domain-specific features" (Seção 4, IBaCoP2)

## Marcações

- `[FATO]` O *survey* traça uma linhagem contínua de conjuntos de *features* para planejamento entre 1999 (Howe et al.) e 2014 (Fawcett et al., 311 *features*), nenhuma delas baseada em UML (Seção 3, "AI planning").
- `[FATO]` Sistemas de seleção por instância em planejamento (IBaCoP2, Planzilla) surgiram depois dos sistemas por domínio (PbP, ASAP) e, segundo o *survey*, tendem a se aproximar mais do desempenho do oráculo (Seção 4).
- `[HIPÓTESE]` A convergência da comunidade para *features* de PDDL/grafo causal/SAS+, e não para diagramas UML, sugere que a proposta de 2010 (usar métricas de modelagem UML) foi uma escolha de engenharia legítima, mas isolada da corrente principal da área de seleção de algoritmo em planejamento — não claramente pior a priori, mas nunca comparada empiricamente a ela.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral das Seções 1 (Introdução), 2 (Algorithm Selection and Related Problems), das partes de SAT e AI planning da Seção 3 (Features), da parte de planejamento da Seção 4 (Applications) e da Seção 6 (Perspectives and Open Problems), em https://arxiv.org/pdf/1811.11597. As partes da Seção 3 relativas a *features* de TSP/otimização contínua e a Seção 5 (aplicações em otimização contínua) foram apenas percorridas por relevância, não lidas linha a linha, por não tratarem de planejamento nem de domínios discretos comparáveis. Conferência humana: pendente.
