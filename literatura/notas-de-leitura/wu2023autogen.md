---
tipo: nota-de-leitura
eixo: E8
citekey: wu2023autogen
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2308.08155
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: []
perguntas: [Q4]
---

# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

**Wu, Q.; Bansal, G.; Zhang, J.; Wu, Y.; Li, B.; et al. · 2023 · COLM 2024**
**Link/DOI:** https://arxiv.org/abs/2308.08155

## Extração estruturada

- **Problema:** construir aplicações de LLM de próxima geração exige compor múltiplos agentes conversacionais que combinem capacidades de LLMs, ferramentas e, quando necessário, humanos, de forma flexível e customizável — mas faltava um framework genérico para isso.
- **Método:** apresentam o AutoGen, um framework de código aberto para permitir aplicações de LLM via conversação entre múltiplos agentes; os agentes conversáveis podem ser customizados para integrar LLMs, ferramentas (por exemplo, execução de código) e humanos, combinando capacidades por meio de conversas automatizadas entre agentes (não lido em detalhe além do resumo e introdução; o restante do artigo cobre casos de uso e avaliação em diferentes domínios, incluindo desenvolvimento de software).
- **Dados/benchmarks:** não detalhado na leitura de resumo/introdução (o artigo cobre múltiplos domínios de aplicação de exemplo).
- **Resultado principal:** o AutoGen é apresentado como framework amplamente adotado que permite aplicações via conversação entre agentes, incluindo tarefas de desenvolvimento de software, com exemplos ilustrando fluxos como geração e correção iterativa de código a partir de erros de execução (ver exemplo de gráfico de ações de mercado com correção de pacote ausente, na própria figura do artigo).
- **Relação com a dissertação de 2010:** sem relação direta com planejamento automatizado. **Q4** [HIPÓTESE] — AutoGen é infraestrutura de coordenação multiagente (companheira de MetaGPT), que poderia sustentar experimentos futuros de ajuste tarefa-configuração de agente (por exemplo, quantos agentes, que papéis), mas a leitura de resumo/introdução não encontrou nenhuma análise desse tipo no próprio artigo.

## Pontos relevantes para o projeto

- Framework amplamente adotado (base de muitos outros sistemas multiagente citados na survey liu2026large deste mesmo lote) — relevante como infraestrutura comum de referência para a Q4.
- Exemplifica de forma concreta (no corpo do artigo) um padrão de interação agente-ferramenta-humano com correção iterativa por *feedback* de erro — padrão de "tentativa e correção" que poderia ser característica de tarefa relevante para pensar ajuste tarefa-agente na Q4.
- Leitura restrita a resumo e introdução; não é possível, com essa profundidade, avaliar a robustez dos resultados de avaliação ou o desenho experimental completo.

## Trechos literais

"AutoGen, a generalized multi-agent conversation framework [...] Agents in AutoGen are customizable, i.e., they can be based on LLMs, tools, humans, or even a combination of them" (introdução, paráfrase próxima do texto lido).

## Marcações

- `[FATO]` O AutoGen é um framework de código aberto que permite compor agentes conversáveis customizáveis (LLM, ferramentas, humanos) via conversação multiagente, com exemplos de aplicação em tarefas de código (resumo e introdução).
- `[HIPÓTESE]` Como infraestrutura de coordenação multiagente, AutoGen é uma base plausível para futuros experimentos de ajuste tarefa-configuração de agente relevantes à Q4, mas essa análise não está no artigo, apenas na minha leitura do potencial de uso.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução em https://arxiv.org/abs/2308.08155 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
