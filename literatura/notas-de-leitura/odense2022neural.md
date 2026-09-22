---
tipo: nota-de-leitura
eixo: E2
citekey: odense2022neural
prioridade: C
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2207.14422
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A5]
fragilidades: []
perguntas: [Q2]
---

# Neural-Guided Runtime Prediction of Planners for Improved Motion and Task Planning with Graph Neural Networks

**Odense, S.; Gupta, K.; Macready, W. · 2022 · IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)**
**Link/DOI:** 10.1109/iros47612.2022.9981823

## Extração estruturada

- **Problema:** a relação entre a estrutura de um problema de planejamento (aqui, planejamento de movimento) e a eficácia de um método de solução específico é opaca; os autores buscam quantificar essa relação para prever o tempo de execução de algoritmos de planejamento de movimento baseados em amostragem (SBMP).
- **Método:** redes neurais em grafo (GNNs) treinadas sobre representações gráficas de problemas de planejamento de movimento (navegação 2D e manipulação de alta dimensão em 3D no simulador iGibson) para prever o tempo de conclusão esperado de um SBMP; uso de um portfólio de algoritmos guiado pelas previsões de tempo de execução da GNN.
- **Dados/benchmarks:** problemas de navegação 2D e de planejamento de manipulação com robô de 7 graus de liberdade em ambientes simulados (iGibson), com nós de grafo descritos por posição, orientação, dimensões e tipo do objeto.
- **Resultado principal:** as GNNs capturam a estrutura geométrica dos problemas de planejamento de movimento o suficiente para prever com boa acurácia o tempo de execução esperado de um dado SBMP, inclusive generalizando de problemas de navegação de baixa dimensão para manipulação de alta dimensão em 3D; a predição também pode ser invertida para identificar subproblemas mais fáceis para um SBMP específico.
- **Relação com a dissertação de 2010:** **confirma A1 e A5** por analogia direta, mas em planejamento de movimento (robótica), não em planejamento clássico simbólico como 2010: a estrutura do problema (aqui, geométrica; em 2010, UML) prediz o desempenho do método de solução, sustentando a ideia de que "complexidade estrutural do domínio afeta desempenho da técnica" é um princípio mais amplo do que o contexto específico de 2010.

## Pontos relevantes para o projeto

- Caso análogo relevante fora do planejamento clássico: mostra que a intuição de 2010 (estrutura do domínio → desempenho da técnica) se replica em planejamento de movimento com uma abordagem de representação totalmente diferente (grafos geométricos + GNN, não UML).
- A inversão da predição (identificar subproblemas mais fáceis para um SBMP) é uma ideia metodológica que poderia inspirar, em planejamento clássico, uma forma de "explicar" por que certos domínios favorecem certas técnicas — relevante para **Q2**.
- Fora do escopo direto do planejamento simbólico/PDDL do resto da revisão; a nota é breve por tratar de um subcampo adjacente (planejamento de movimento em robótica) lido apenas em resumo e introdução/conclusão.

## Trechos literais

> "We demonstrate that the geometric relationships of motion planning problems can be well captured by graph neural networks (GNNs) to predict SBMP runtime." (Resumo)

## Marcações

- `[FATO]` GNNs treinadas sobre grafos geométricos preveem o tempo de execução esperado de algoritmos de planejamento de movimento por amostragem, generalizando de navegação 2D para manipulação 3D (Resumo; Seção V).
- `[HIPÓTESE]` Esse resultado em planejamento de movimento reforça, por analogia de outro subcampo, a plausibilidade geral de A1/A5 de 2010 — mas não deve ser lido como confirmação direta, pois o tipo de "estrutura do domínio" (geometria física) e o tipo de "técnica" (SBMP) são categoricamente distintos dos de 2010 (UML de domínio PDDL; técnicas de busca simbólica).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://arxiv.org/pdf/2207.14422. Conferência humana: pendente.
