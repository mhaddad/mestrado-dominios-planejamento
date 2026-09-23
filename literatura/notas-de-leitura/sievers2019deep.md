---
tipo: nota-de-leitura
eixo: E1
citekey: sievers2019deep
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/AAAI/article/view/4767/4645
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A7]
fragilidades: [F2, F5]
perguntas: [Q1, Q2]
---

# Deep Learning for Cost-Optimal Planning: Task-Dependent Planner Selection

**Sievers, S.; Katz, M.; Sohrabi, S.; Samulowitz, H.; Ferber, P. · 2019 · Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-19)**
**Link/DOI:** 10.1609/aaai.v33i01.33017715

## Extração estruturada

- **Problema:** como usar aprendizado profundo para selecionar, por tarefa, qual planejador de custo-ótimo resolverá uma dada instância, evitando o trabalho de projetar *features* manuais — revisitando e generalizando as decisões do sistema Delfi (vencedor da IPC 2018).
- **Método:** representar tarefas de planejamento como imagens (via grafos de estrutura) e aplicar convolução de imagem; exploração sistemática de três eixos de decisão: nível de abstração da predição (regressão vs. classificação), número de planejadores no portfólio, e generalização a tarefas fora da distribuição de treino.
- **Dados/benchmarks:** conjunto de planejadores do Delfi acrescido dos planejadores da IPC 2018; comparação de divisões de dados (*data splits*) manuais versus aleatórias, preservando ou não o domínio.
- **Resultado principal:** nenhuma receita única funciona bem para todos os métodos testados; mesmo a melhor configuração dos autores não alcançou o desempenho médio do Delfi1 original, e a divisão de dados aleatória (não preservando domínio) piora significativamente a cobertura média em relação à divisão manual do Delfi1.
- **Relação com a dissertação de 2010:** **confirma A1** de forma indireta — o próprio fato de que a divisão dos dados "preservando o domínio" (ou seja, respeitando a estrutura por domínio) é crucial para o desempenho reforça que características por domínio importam para a seleção de técnica. Também **confirma A7** (eficiência = cobertura): os autores usam cobertura como métrica central. O artigo discute explicitamente que dados de planejamento não são i.i.d. entre domínios — ponto que toca **F2** (amostra pequena) e **Q1**, pois a quantidade de dados de treino é descrita como "relativamente pequena pelos padrões de aprendizado de máquina".

## Pontos relevantes para o projeto

- Discussão explícita sobre a não-independência (não-i.i.d.) dos dados de planejamento entre domínios é diretamente relevante para qualquer réplica estatística de 2010 (**T6**, **Q1**): reforça que agrupar por domínio, como 2010 fez implicitamente, é metodologicamente necessário, não apenas conveniente.
- Reconhece que a quantidade de dados de treino disponível em planejamento é pequena para os padrões de aprendizado de máquina — mesma fragilidade estrutural de **F2** em 2010, mas em um contexto totalmente diferente (redes neurais versus discretização UML).
- Nenhuma "receita única" (nem mesmo a do vencedor da IPC, Delfi1) generaliza bem — eco moderno de A2/A3 (não existe uma técnica universalmente melhor; a escolha depende do domínio/tarefa).

## Trechos literais

> "Our results show that there is no single recipe that works well for all tested methods. [...] the amount of training data used in this work is relatively small by machine learning standards." (Seção "Discussion and Future Work")

## Marcações

- `[FATO]` A divisão de dados aleatória (sem preservar domínio) resulta em cobertura média significativamente pior que a divisão manual preservando domínio do Delfi1 (Seção "Discussion and Future Work").
- `[HIPÓTESE]` A necessidade de preservar a estrutura por domínio nos dados de treino é um argumento indireto, mas forte, a favor da premissa central de 2010 (A1): o domínio de origem de uma tarefa é uma variável relevante para prever qual técnica funciona melhor nela.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e seção de discussão/conclusão em https://ojs.aaai.org/index.php/AAAI/article/view/4767/4645. Conferência humana: pendente.
