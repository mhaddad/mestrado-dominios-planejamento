---
tipo: nota-de-leitura
eixo: E1
citekey: ferber2022explainable
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/AAAI/article/view/21209/20958
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: [F3, F4]
perguntas: [Q2]
---

# Explainable Planner Selection for Classical Planning

**Ferber, P.; Seipp, J. · 2022 · Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-22)**
**Link/DOI:** 10.1609/aaai.v36i9.21209

## Extração estruturada

- **Problema:** as abordagens mais fortes de seleção de planejador usam redes neurais convolucionais/em grafo, cujos modelos aprendidos são complexos e não interpretáveis; o artigo busca um pequeno conjunto de *features* simples e interpretáveis que atinjam desempenho comparável.
- **Método:** identificação de um conjunto pequeno de *features* simples da tarefa de planejamento e aplicação de técnicas elementares e interpretáveis de aprendizado de máquina (regressão linear, árvore de decisão, *random forest*, MLP como comparação) para selecionar um único planejador por tarefa (seleção de portfólio, não escalonamento).
- **Dados/benchmarks:** tarefas de planejamento clássico, incluindo as da IPC 2018; comparação contra Delfi1 (estado da arte baseado em CNN sobre imagem) e um oráculo por domínio (seleciona o planejador com maior cobertura naquele domínio).
- **Resultado principal:** o modelo de regressão linear simples resolve aproximadamente o mesmo número de tarefas que o Delfi1, sendo interpretável e rápido de treinar; selecionar um único planejador por domínio (oráculo) já resolve quase todas as tarefas de teste, à exceção de uma.
- **Relação com a dissertação de 2010:** **confirma fortemente A1** — o próprio experimento do oráculo por domínio ("selecionar o planejador com maior cobertura no domínio resolve quase tudo") é evidência direta e atual de que a identidade do domínio, por si, já carrega grande poder preditivo sobre qual planejador funciona melhor, tese central de 2010. Toca **F3** (métricas UML dependem do modelador) e **F4** (taxonomia discutível): aqui as *features* usadas são simples e extraídas automaticamente do PDDL, não da UML, sugerindo um caminho alternativo às métricas de 2010.

## Pontos relevantes para o projeto

- O achado de que "selecionar um planejador por domínio" quase resolve tudo é uma réplica conceitual, com dados de 2022, da intuição central de 2010 — cita explicitamente Roberts et al. (2008) como precedente empírico de que é "possível e benéfico" que modelos de aprendizado de máquina identifiquem domínios.
- *Features* simples e interpretáveis (não redes neurais) bastam para acompanhar o estado da arte — relevante para **Q2**: sugere que talvez não seja necessário todo o aparato de GNN/CNN para obter poder preditivo a partir de características estruturais do domínio, o que barateia uma eventual réplica de 2010 com features modernas.
- Não usa métricas UML nem menciona 2010 ou trabalhos correlatos de modelagem UML — é um universo metodológico paralelo (features de PDDL) que a revisão pode comparar diretamente com as métricas de 2010.

## Trechos literais

> "These findings align with an earlier empirical analysis by Roberts et al. (2008) who showed that it is both possible and beneficial for machine learning models to identify domains." (Seção de resultados, antes da Conclusão)

## Marcações

- `[FATO]` Selecionar, por um oráculo, o planejador com maior cobertura em cada domínio resolve todas as tarefas de teste menos uma (Seção de resultados).
- `[HIPÓTESE]` Esse resultado é uma confirmação empírica moderna e independente da tese A1 de 2010 — embora obtida com *features* de PDDL simples, não com métricas UML — reforçando que a pergunta de 2010 continua válida mesmo fora do aparato metodológico original.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://ojs.aaai.org/index.php/AAAI/article/view/21209/20958. Conferência humana: pendente.
