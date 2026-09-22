---
tipo: nota-de-leitura
eixo: E5
citekey: aghzal2025survey
prioridade: C
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2502.12435 (PDF baixado, lidos resumo e introdução)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: []
perguntas: [Q3]
---

# A Survey on Large Language Models for Automated Planning

**Aghzal, M.; Plaku, E.; Stein, G. J.; Yao, Z. · 2025 · arXiv preprint**
**Link/DOI:** https://doi.org/10.48550/arxiv.2502.12435

## Extração estruturada

- **Problema:** revisar criticamente a pesquisa existente sobre uso de LLMs em planejamento automatizado, contrastando visões otimistas e céticas sobre suas capacidades.
- **Método:** revisão de literatura (survey), sem detalhamento metodológico adicional na leitura de resumo/introdução.
- **Dados/benchmarks:** não é estudo empírico próprio.
- **Resultado principal:** segundo o resumo, embora LLMs mostrem alguma promessa em planejamento de curto horizonte, seu desempenho tende a degradar significativamente em cenários de raciocínio de longo horizonte, tornando-os pouco confiáveis nesses casos; mesmo quando bem-sucedidos, o custo dos planos gerados pode ser arbitrariamente alto.
- **Relação com a dissertação de 2010:** sem relação direta com A1–A8. Alimenta **Q3**, com um recorte específico e recente (2025) sobre planejamento automatizado com LLMs, escolhido pelo Coordenador como revisão geral representativa da área.

## Pontos relevantes para o projeto

- Survey recente (2025) que resume o estado da arte e as limitações de longo horizonte de LLMs em planejamento, útil como referência-âncora para a seção de LLMs da revisão.
- A limitação de "custo de plano arbitrariamente alto" mesmo em casos de sucesso conecta-se de forma indireta com a simplificação de 2010 (F5: eficiência = cobertura), já que sugere que sucesso binário não captura toda a qualidade do plano.

## Trechos literais

"While LLM agents show some promise in high-level short-horizon planning, they often fail to yield correct plans in long-horizon scenarios, where their performance can degrade significantly" (introdução, primeiras linhas do corpo do texto).

## Marcações

- `[FATO]` o survey aponta degradação de desempenho de LLMs em planejamento de longo horizonte e custos de plano potencialmente altos mesmo em casos de sucesso (introdução).
- `[HIPÓTESE]` não há interpretação adicional a registrar; leitura limitada ao resumo e início da introdução (prioridade C, nota curta).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução do PDF em https://arxiv.org/pdf/2502.12435 (prioridade C, nota curta). Conferência humana: pendente.
