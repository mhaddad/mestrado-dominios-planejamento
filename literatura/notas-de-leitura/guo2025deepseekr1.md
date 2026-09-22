---
tipo: nota-de-leitura
eixo: E5
citekey: guo2025deepseekr1
prioridade: C
status: lido
profundidade: resumo
fonte-lida: https://api.crossref.org/works/10.1038/s41586-025-09422-z
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: []
perguntas: [Q3]
---

# DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning

**DeepSeek-AI et al. · 2025 · Nature, v. 645, n. 8081, p. 633-638**
**Link/DOI:** https://doi.org/10.1038/s41586-025-09422-z

## Extração estruturada

- **Problema:** desenvolver capacidade de raciocínio em LLMs sem depender de exemplos de raciocínio anotados por humanos.
- **Método:** treinamento por aprendizado por reforço puro (sem dados supervisionados de raciocínio), permitindo o desenvolvimento espontâneo de táticas de raciocínio sofisticadas (autorreflexão, verificação, mudança adaptativa de estratégia).
- **Dados/benchmarks:** domínios verificáveis — matemática, competições de programação e disciplinas de ciências exatas (STEM).
- **Resultado principal:** o modelo treinado supera abordagens de aprendizado supervisionado convencional nesses domínios verificáveis; estratégias de raciocínio emergentes de modelos maiores podem ser transferidas sistematicamente para melhorar modelos menores.
- **Relação com a dissertação de 2010:** sem relação direta com A1–A8 (não trata de planejamento automatizado nem de domínios PDDL/UML). Alimenta **Q3** de forma indireta: é o modelo de raciocínio geral referenciado como base em avaliações de modelos de raciocínio aplicados a planejamento (citado no contexto de outros itens do eixo E5, ex. E5-004).

## Pontos relevantes para o projeto

- Não é um trabalho de planejamento automatizado; sua relevância para a revisão é indireta, como pano de fundo técnico (capacidades de raciocínio via RL) para trabalhos que avaliam modelos de raciocínio em tarefas de planejamento.
- Útil apenas como referência de contexto, não como fonte de dado sobre relação domínio×técnica.

## Trechos literais

"The method fosters spontaneous development of sophisticated reasoning tactics including self-reflection, verification, and adaptive strategy shifts" (resumo, via metadados Crossref).

## Marcações

- `[FATO]` o artigo relata treinamento de um LLM por aprendizado por reforço puro que desenvolve táticas de raciocínio emergentes, com ganhos em domínios verificáveis (matemática, código, STEM) (metadados Crossref).
- `[HIPÓTESE]` interpretação minha: por não tratar de planejamento automatizado, este trabalho tem relação apenas indireta com a linha de pesquisa de 2010; seu papel na revisão deve ser de referência de contexto técnico, não de evidência sobre domínios de planejamento.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo via metadados Crossref (https://api.crossref.org/works/10.1038/s41586-025-09422-z); o artigo completo está na Nature, atrás de paywall, e não foi possível localizar cópia aberta com o mesmo texto publicado (arXiv 2501.12948 é uma versão preprint anterior, não verificada como idêntica ao texto publicado, portanto não usada). Conferência humana: pendente.
