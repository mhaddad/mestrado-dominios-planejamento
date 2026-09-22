---
tipo: nota-de-leitura
eixo: E8
citekey: liang2024largescale
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2303.17125
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: []
perguntas: [Q4]
---

# A Large-Scale Survey on the Usability of AI Programming Assistants: Successes and Challenges

**Liang, J. T.; Yang, C.; Myers, B. A. · 2024 · ICSE 2024**
**Link/DOI:** https://doi.org/10.1145/3597503.3608128 (texto lido via arXiv:2303.17125)

## Extração estruturada

- **Problema:** apesar da ampla adoção de assistentes de programação com IA (como GitHub Copilot), desenvolvedores não aceitam as sugestões iniciais desses assistentes com alta frequência, deixando em aberto questões sobre a usabilidade real dessas ferramentas na prática.
- **Método:** levantamento (survey) com uma população ampla de desenvolvedores, obtendo respostas de um conjunto diverso de 410 desenvolvedores, com análise mista qualitativa e quantitativa.
- **Dados/benchmarks:** 410 respostas de desenvolvedores; não é benchmark computacional, é dado de pesquisa de usabilidade.
- **Resultado principal:** desenvolvedores são motivados a usar assistentes de IA principalmente para reduzir digitação, terminar tarefas mais rápido e relembrar sintaxe, mas ressoam menos com o uso desses assistentes para gerar ideias de solução; as razões mais importantes para não usar as ferramentas envolvem limitações não detalhadas no trecho lido.
- **Relação com a dissertação de 2010:** sem relação direta com planejamento automatizado. **Q4** [HIPÓTESE] — o achado de que desenvolvedores usam assistentes de IA mais para tarefas mecânicas (sintaxe, digitação) do que para geração de ideias (raciocínio de mais alto nível) sugere uma primeira "característica de tarefa" relevante para a Q4: tarefas mecânicas/rotineiras podem ter melhor ajuste com assistentes de IA do que tarefas que exigem raciocínio criativo ou de projeto — mas essa distinção não é formalizada nem testada estatisticamente pelo artigo, é inferência minha a partir dos motivos de uso relatados.

## Pontos relevantes para o projeto

- Amostra grande (410 desenvolvedores) e metodologia mista (qualitativa + quantitativa) tornam este um dos estudos de usabilidade mais robustos do lote sobre assistentes de código.
- Estrutura o problema de usabilidade em três blocos (padrões de uso, usabilidade dos assistentes, feedback adicional — ver Figura 1 do artigo), o que pode servir de estrutura de referência para futuras entrevistas/surveys sobre ajuste tarefa-agente na Q4.
- Não caracteriza tarefas por métricas estruturais nem mede desempenho objetivo; é inteiramente baseado em autorrelato de desenvolvedores, uma limitação a declarar caso a Q4 use este artigo como evidência.

## Trechos literais

"we found that developers are most motivated to use AI programming assistants because they help developers reduce key-strokes, finish programming tasks quickly, and recall syntax, but resonate less with using them to help brainstorm potential solutions" (resumo).

## Marcações

- `[FATO]` Em survey com 410 desenvolvedores, os motivos mais citados para uso de assistentes de IA foram redução de digitação, velocidade e lembrança de sintaxe, com menor ressonância para geração de ideias de solução (resumo).
- `[HIPÓTESE]` Esse padrão de uso sugere que tarefas mecânicas/rotineiras podem ter melhor ajuste com assistentes de IA do que tarefas de concepção/projeto — hipótese minha para alimentar a Q4, não uma conclusão testada estatisticamente pelo artigo.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução em https://arxiv.org/abs/2303.17125 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
