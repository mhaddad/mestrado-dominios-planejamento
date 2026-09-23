---
tipo: nota-de-leitura
eixo: E8
citekey: hong2023metagpt
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2308.00352
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: []
perguntas: [Q4]
---

# MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework

**Hong, S.; Zhuge, M.; Chen, J.; Zheng, X.; Cheng, Y.; et al. · 2023 · ICLR 2024**
**Link/DOI:** https://arxiv.org/abs/2308.00352

## Extração estruturada

- **Problema:** sistemas multiagente baseados em LLM já resolvem tarefas de diálogo simples, mas soluções para tarefas mais complexas são prejudicadas por inconsistências lógicas decorrentes de alucinações em cascata causadas pelo encadeamento ingênuo de LLMs.
- **Método:** introduzem o MetaGPT, um framework de meta-programação que incorpora Procedimentos Operacionais Padronizados (SOPs) humanos em sequências de *prompt*, permitindo que agentes com "expertise" de domínio ao estilo humano verifiquem resultados intermediários e reduzam erros; usa um paradigma de linha de montagem, atribuindo papéis diversos a diferentes agentes, quebrando tarefas complexas em subtarefas que envolvem múltiplos agentes trabalhando juntos.
- **Dados/benchmarks:** benchmarks colaborativos de engenharia de software (não detalhados além do resumo e conclusão lidos).
- **Resultado principal:** em benchmarks colaborativos de engenharia de software, o MetaGPT gera soluções mais coerentes do que sistemas multiagente anteriores baseados em chat, alcançando desempenho de estado da arte em múltiplos benchmarks ao modelar o grupo de agentes como uma empresa de software simulada, análoga a cidades simuladas e ao sandbox de Minecraft do Voyager.
- **Relação com a dissertação de 2010:** sem relação direta com planejamento automatizado. **Q4** [HIPÓTESE] — MetaGPT introduz SOPs (procedimentos padronizados) como mecanismo para reduzir erros em tarefas complexas — um tipo de "técnica" de coordenação de agentes que poderia, em princípio, ser combinada com a Q4 (que tarefas se beneficiam mais de coordenação via SOP vs. um agente único), mas o artigo não testa essa variação por característica de tarefa; apenas compara MetaGPT com sistemas multiagente anteriores.

## Pontos relevantes para o projeto

- É um dos frameworks multiagente mais influentes do lote (companheiro de AutoGen), relevante como peça de infraestrutura/técnica para a Q4, mas sem análise de ajuste tarefa-técnica no próprio artigo.
- A analogia usada pelos autores (agentes como "empresa de software simulada") é conceitualmente próxima da ideia de modelar processos de desenvolvimento como domínios estruturados — ecoa, de forma distante e não intencional, a lógica de modelagem estrutural que 2010 aplicou a domínios de planejamento via UML.
- O mecanismo central (SOPs reduzindo alucinações em cascata) é uma solução de engenharia para um problema específico de sistemas multiagente, não uma evidência empírica de ajuste tarefa-configuração.

## Trechos literais

"MetaGPT, an innovative meta-programming framework incorporating efficient human workflows into LLM-based multi-agent collaborations [...] On collaborative software engineering benchmarks, MetaGPT generates more coherent solutions than previous chat-based multi-agent systems" (resumo).

## Marcações

- `[FATO]` O MetaGPT usa SOPs codificados em sequências de *prompt* para coordenar múltiplos agentes de LLM com papéis especializados, alcançando desempenho de estado da arte em benchmarks colaborativos de engenharia de software (resumo e conclusão).
- `[HIPÓTESE]` SOPs como mecanismo de coordenação são um tipo de "técnica" que poderia, em trabalho futuro, ser testada quanto ao ajuste com diferentes tipos de tarefa de desenvolvimento de software (Q4), mas essa análise não está no artigo.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://arxiv.org/abs/2308.00352 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
