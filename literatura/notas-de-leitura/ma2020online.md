---
tipo: nota-de-leitura
eixo: E1
citekey: ma2020online
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/AAAI/article/view/5949/5805
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1]
fragilidades: [F5]
perguntas: [Q2, Q3]
---

# Online Planner Selection with Graph Neural Networks and Adaptive Scheduling

**Ma, T.; Ferber, P.; Huo, S.; Chen, J.; Katz, M. · 2020 · Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-20)**
**Link/DOI:** 10.1609/aaai.v34i04.5949

## Extração estruturada

- **Problema:** selecionar online, para cada tarefa de planejamento, qual planejador de um portfólio provavelmente a resolverá, explorando representações estruturais em grafo das tarefas em vez de *features* manuais.
- **Método:** rede neural em grafo (GNN) para prever o planejador candidato a partir da representação estrutural da tarefa; complementada por um escalonamento adaptativo de dois estágios, que pode trocar de planejador na metade do tempo conforme o desempenho observado do primeiro.
- **Dados/benchmarks:** tarefas de planejamento clássico usadas para comparar contra Delfi (vencedor da Trilha Ótima da IPC 2018, que trata a tarefa como imagem e usa CNN) e outras linhas de base com e sem aprendizado profundo.
- **Resultado principal:** o escalonamento adaptativo aumenta consistentemente o percentual de tarefas resolvidas nas duas arquiteturas de GNN testadas, elevando o melhor resultado de 87,6% (Tabela 2) para 89,7% na divisão Delfi.
- **Relação com a dissertação de 2010:** **confirma, em espírito, A1** — características estruturais do domínio/tarefa (aqui, extraídas automaticamente via GNN de um grafo, não via UML) predizem qual técnica/planejador funciona melhor — mas por um caminho totalmente diferente de 2010 (aprendizado automático de representação, não métricas UML discretizadas manualmente). Relevante para **F5** (eficiência = cobertura): o artigo também usa cobertura/percentual resolvido como métrica principal, mesma simplificação de 2010.

## Pontos relevantes para o projeto

- Evidência direta e atual de que características estruturais da tarefa de planejamento (aqui aprendidas automaticamente via GNN) têm poder preditivo sobre qual planejador funciona melhor — alimenta diretamente **Q2** (métricas estruturais de modelagem acrescentam poder preditivo às *features* de PDDL?).
- Ilustra onde LLMs/aprendizado profundo entram no pipeline de seleção de planejador (não como planejador, mas como seletor) — relevante para **Q3**.
- Mesma limitação metodológica de 2010: eficiência medida apenas por cobertura/percentual resolvido, sem tempo ou qualidade do plano (F5/A7).

## Trechos literais

> "Owing to the recent development of structural graph representations of planning tasks, we propose a graph neural network (GNN) approach to selecting candidate planners." (Resumo)

## Marcações

- `[FATO]` O escalonamento adaptativo eleva o melhor resultado de 87,6% para 89,7% de tarefas resolvidas na divisão Delfi, comparado ao escalonamento fixo (Seção de resultados, Figura 4).
- `[HIPÓTESE]` O sucesso de representações estruturais automáticas (GNN) para prever desempenho de planejador sugere que as métricas manuais de UML de 2010 (A1) podem ser um caso particular, menos expressivo, de um princípio mais geral — características estruturais do domínio predizem desempenho —, o que fortalece a pergunta Q2 da revisão.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e trecho de resultados/conclusão em https://ojs.aaai.org/index.php/AAAI/article/view/5949/5805. Conferência humana: pendente.
