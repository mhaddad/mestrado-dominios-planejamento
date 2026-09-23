---
tipo: nota-de-leitura
eixo: E8
citekey: pan2024training
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2412.21139
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: []
perguntas: [Q4]
---

# Training Software Engineering Agents and Verifiers with SWE-Gym

**Pan, J.; Wang, X.; Neubig, G.; Jaitly, N.; Ji, H.; Suhr, A.; Zhang, Y. · 2024 · arXiv (ICML 2025)**
**Link/DOI:** https://arxiv.org/abs/2412.21139

## Extração estruturada

- **Problema:** não existia um ambiente de treinamento dedicado para agentes de engenharia de software (SWE) baseados em modelos de linguagem, o que limitava o treinamento e a verificação sistemática desses agentes.
- **Método:** apresentam o SWE-Gym, o primeiro ambiente para treinar agentes de SWE, com 2.438 instâncias de tarefas reais (cada uma com um repositório Python, ambiente de execução, testes unitários e uma tarefa especificada em linguagem natural); usam o SWE-Gym para treinar agentes de SWE baseados em LLM e experimentam com escalonamento em tempo de inferência através de verificadores treinados sobre trajetórias de agentes.
- **Dados/benchmarks:** SWE-Gym (2.438 instâncias reais); avaliação em SWE-Bench Verified e SWE-Bench Lite.
- **Resultado principal:** obtêm ganhos absolutos de até 19% na taxa de resolução nos conjuntos de teste populares SWE-Bench Verified e Lite, ao treinar agentes com o SWE-Gym, com ganhos adicionais via escalonamento em tempo de treino (mais trajetórias de treinamento) e em tempo de inferência (verificadores).
- **Relação com a dissertação de 2010:** sem relação direta com planejamento automatizado. **Q4** [HIPÓTESE] — SWE-Gym é a infraestrutura de treinamento que poderia, em trabalho futuro, ser usada para testar se características do repositório/tarefa (analogia às características de domínio de 2010) predizem o ganho de desempenho ao treinar ou usar um agente específico — mas o artigo não realiza essa análise desagregada por característica de tarefa, apenas relata ganho agregado.

## Pontos relevantes para o projeto

- Fornece a infraestrutura de treinamento (não só avaliação) para agentes de SWE, complementar ao OpenHands (avaliação/execução) e ao Agentless (abordagem sem agente) do mesmo lote — os três formam um conjunto coerente de infraestrutura E8 relevante à Q4.
- O escalonamento em tempo de inferência via verificadores é conceitualmente parecido com "usar mais recursos computacionais para melhorar o ranking", ecoando de forma distante a lógica de A4 de 2010 (mais dados/recursos melhoram o resultado) — mas aplicado a agentes treináveis, não a um ranking estático de planejadores.
- Não há, no texto lido, qualquer caracterização de tarefas por métricas estruturais nem análise de que tipo de repositório/tarefa se beneficia mais do treinamento — é relevante como infraestrutura, não como evidência substantiva para a Q4.

## Trechos literais

"We present SWE-Gym, the first environment for training software engineering (SWE) agents [...] We use SWE-Gym to train language model based SWE agents, and achieve up to 19% absolute gains in resolution rate on the popular SWE-Bench Verified and Lite test sets" (resumo).

## Marcações

- `[FATO]` O SWE-Gym é apresentado como o primeiro ambiente de treinamento dedicado a agentes de SWE, com ganhos de até 19 pontos percentuais absolutos em SWE-Bench Verified/Lite (resumo).
- `[HIPÓTESE]` Essa infraestrutura de treinamento é uma peça útil para, em trabalho futuro, testar a Q4 de forma desagregada por características de tarefa/repositório — mas isso não é feito pelo artigo.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução em https://arxiv.org/abs/2412.21139 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
