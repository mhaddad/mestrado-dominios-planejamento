---
tipo: nota-de-leitura
eixo: E1
citekey: vatter2026beyond
prioridade: C
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/download/42845/50405/46946
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1]
fragilidades: [F4]
perguntas: [Q2, Q3]
---

# Beyond Message Passing: Modern GNN Architectures for Online Planner Selection

**Vatter, J.; Mayer, R.; Jacobsen, H.; Samulowitz, H.; Katz, M. · 2026 · Proceedings of the International Conference on Automated Planning and Scheduling (ICAPS 2026)**
**Link/DOI:** 10.1609/icaps.v36i1.42845

## Extração estruturada

- **Problema:** o trabalho anterior sobre seleção online de planejador com GNNs (ma2020online) explora apenas grafos homogêneos e foca no modelo, deixando de lado a estrutura tipicamente heterogênea das tarefas de planejamento (nós que são constantes, ações ou efeitos) e a análise do lado dos dados (quais planejadores realmente contribuem ao portfólio).
- **Método:** análise do desempenho dos planejadores via valores de Shapley para reduzir o portfólio de 17 para 6 planejadores; modelagem das tarefas como grafos heterogêneos com Relational Graph Convolutional Network (RGCN) e Relational Graph Attention Network (RGAT); abordagem híbrida combinando representações de GNN com XGBoost.
- **Dados/benchmarks:** portfólio de planejadores de custo-ótimo (originalmente 17, reduzido a 6 via Shapley); grafos de tarefas de planejamento (representações fundamentadas/*grounded* e liftadas), comparando com métodos anteriores baseados em GNN homogênea e em CNN.
- **Resultado principal:** o melhor modelo (RGCN + XGBoost) atinge 91,7% de acurácia, superando o estado da arte anterior de 87% (GNN homogênea) e 82,1%–86,1% (CNN), com menor custo computacional.
- **Relação com a dissertação de 2010:** **confirma A1** de forma moderna e indireta — mostra que representar melhor a estrutura da tarefa (heterogênea versus homogênea) aumenta o poder preditivo sobre qual planejador funciona melhor, reforçando que características estruturais do domínio/tarefa importam. Toca **F4** (taxonomia de técnicas discutível): o próprio artigo argumenta que arquiteturas de GNN "não são adaptadas" à seleção automática de planejador, sugerindo que taxonomias genéricas (de técnicas de aprendizado ou de planejamento) tendem a subestimar ganhos possíveis com especialização.

## Pontos relevantes para o projeto

- Publicação mais recente do lote (ICAPS 2026), útil para ancorar o estado da arte atual do eixo E1 (seleção de planejador) na revisão.
- A técnica de valores de Shapley para reduzir um portfólio de 17 para 6 planejadores é uma metodologia concreta e citável para T4 (pesos por característica) se a revisão quiser aplicar algo análogo às características de domínio de 2010.
- Relevante para **Q3** (onde entram os LLMs): o artigo é puramente baseado em GNN/XGBoost, sem menção a LLMs, o que mostra que a fronteira de pesquisa em seleção de planejador em 2026 ainda não incorporou LLMs como seletores — um espaço em aberto que a revisão pode apontar.

## Trechos literais

> "Our best model (RGCN+XGBoost) achieves 91.7% accuracy, a substantial improvement over previous methods with 87%, while requiring fewer computational resources." (Resumo)

## Marcações

- `[FATO]` O modelo RGCN+XGBoost atinge 91,7% de acurácia na seleção de planejador, ante 87% do método homogêneo anterior e 82,1%-86,1% de métodos baseados em CNN (Resumo; Seção de resultados).
- `[HIPÓTESE]` A ausência de LLMs neste trabalho de 2026 sobre seleção de planejador sugere que a integração de LLMs como seletores (Q3) ainda é uma lacuna de pesquisa, não uma prática consolidada, mesmo na fronteira mais recente do eixo E1.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://ojs.aaai.org/index.php/ICAPS/article/download/42845/50405/46946. Conferência humana: pendente.
