---
tipo: nota-de-leitura
eixo: E2
citekey: ferber2019ipc
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/1905.06393
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A7]
fragilidades: [F2, F5, F6]
perguntas: [Q1, Q2]
---

# IPC: A Benchmark Data Set for Learning with Graph-Structured Data

**Ferber, P.; Ma, T.; Huo, S.; Chen, J.; Katz, M. · 2019 · ICML 2019 Workshop on Learning and Reasoning with Graph-Structured Data (também em arXiv:1905.06393)**
**Link/DOI:** não informado no lote (arXiv:1905.06393)

## Extração estruturada

- **Problema:** faltava um conjunto de dados de referência (*benchmark*) adequado para avaliar métodos de aprendizado de máquina sobre dados estruturados em grafo (grafos, *kernels* de grafo, GNNs) no contexto de planejamento automatizado.
- **Método:** construção de um novo conjunto de dados, IPC, compilado a partir de tarefas de Competições Internacionais de Planejamento (IPC) descritas em PDDL, representando cada tarefa como grafo dirigido (duas versões: fundamentada/*grounded* e liftada/*lifted*), com nós dotados de *features* e valores-alvo (tempo de CPU de 17 planejadores de custo-ótimo, com *timeout* de 1800s).
- **Dados/benchmarks:** 2439 tarefas de planejamento, pré-divididas em treino/validação/teste, com dois esquemas de divisão (preservando domínio vs. aleatória); resultados de desempenho de CNN, GCN e GG-NN comparados em ambas as versões do grafo (fundamentada e liftada).
- **Resultado principal:** a versão liftada dos grafos produz acurácia bem maior que a fundamentada (ex.: GCN atinge 87,6% na versão liftada vs. 80,7% na fundamentada, no percentual de tarefas resolvidas do conjunto de teste), e GCN supera CNN e GG-NN nas comparações reportadas.
- **Relação com a dissertação de 2010:** **confirma A1** de forma indireta — o conjunto de dados IPC foi desenhado justamente para testar se representações estruturais da tarefa/domínio predizem desempenho de planejadores, ecoando a pergunta central de 2010, mas com uma infraestrutura de dados que 2010 não tinha (o que toca **F6**, dados fora das competições, resolvido aqui ao consolidar dados oficiais de IPC). O uso de tempo de CPU como alvo (não só cobertura) contrasta com **A7/F5** (2010 usou só cobertura): aqui o tempo de CPU é usado tanto como alvo de regressão quanto convertido para classificação, uma abordagem mais rica.

## Pontos relevantes para o projeto

- É a base de dados usada por vários outros trabalhos deste lote (ma2020online, sievers2019deep, vatter2026beyond), funcionando como infraestrutura compartilhada do eixo E1/E2 — análogo ao papel do ASlib (bischl2016aslib) para seleção de algoritmo em geral.
- A distinção entre divisão "preservando domínio" e "aleatória" reforça, de novo, que a identidade do domínio de origem de uma tarefa é uma variável estruturalmente relevante para desempenho de planejador (achado replicado em sievers2019deep) — evidência direta para **Q1** e **Q2**.
- O conjunto é extensível programaticamente (gerador de grafos automatizado), o que é relevante para **T2** (agregação automática de novos resultados) e **T5** (domínios artificiais) de 2010.

## Trechos literais

> "The graphs are constructed from AI planning tasks appearing in International Planning Competitions, without requiring human efforts for labeling, and may be extended with random instances of planning problems." (Seção 5, Conclusions)

## Marcações

- `[FATO]` A versão liftada dos grafos produz acurácia consistentemente maior que a fundamentada nos três modelos testados (CNN, GCN, GG-NN), com GCN liftado atingindo 87,6% de tarefas resolvidas no teste (Tabela 2, Seção 4/5).
- `[HIPÓTESE]` A disponibilidade de um *benchmark* padronizado e extensível como o IPC é o tipo de infraestrutura que, se existisse em 2010, teria permitido tratar diretamente T2 e T5 (agregação automática de resultados e domínios artificiais) propostos como trabalhos futuros na dissertação original.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://arxiv.org/pdf/1905.06393. Conferência humana: pendente.
