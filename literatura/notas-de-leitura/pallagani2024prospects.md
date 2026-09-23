---
tipo: nota-de-leitura
eixo: E5
citekey: pallagani2024prospects
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2401.02500 (PDF baixado, lidos resumo e introdução)
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: []
perguntas: [Q3]
---

# On the Prospects of Incorporating Large Language Models (LLMs) in Automated Planning and Scheduling (APS)

**Pallagani, V.; Muppasani, B. C.; Roy, K.; Fabiano, F.; Loreggia, A.; Murugesan, K.; Srivastava, B.; Rossi, F.; Horesh, L.; Sheth, A. · 2024 · ICAPS 2024**
**Link/DOI:** https://doi.org/10.1609/icaps.v34i1.31503

## Extração estruturada

- **Problema:** mapear como LLMs estão sendo aplicados a diferentes aspectos de problemas de planejamento e escalonamento automatizado (APS).
- **Método:** revisão sistemática de 126 artigos, organizados em oito categorias de aplicação: tradução de linguagem, geração de plano, construção de modelo, planejamento multiagente, planejamento interativo, otimização de heurísticas, integração de ferramentas e planejamento inspirado no cérebro.
- **Dados/benchmarks:** não é estudo empírico; é revisão bibliográfica.
- **Resultado principal:** o potencial real dos LLMs se manifesta quando integrados a planejadores simbólicos tradicionais (abordagem neurossimbólica), combinando os aspectos generativos dos LLMs com o raciocínio formal dos planejadores clássicos, em vez de LLMs substituírem planejadores.
- **Relação com a dissertação de 2010:** sem relação direta com A1–A8 (não usa métricas UML nem cobertura de planejadores clássicos). Alimenta **Q3**: a categoria "construção de modelo" desta revisão é o análogo, na era LLM, do problema de modelagem de domínio que está no centro da dissertação de 2010 (via itSIMPLE).

## Pontos relevantes para o projeto

- Panorama amplo (126 trabalhos) útil como mapa de literatura para orientar quais subtemas de LLM+planejamento merecem nota própria na revisão.
- A conclusão central — "neurossimbólico supera LLM puro" — é um contraponto importante à narrativa de que LLMs substituiriam planejadores clássicos, relevante para Q3.
- Estrutura em 8 categorias pode servir de referência organizacional para a seção da dissertação revisada sobre LLMs em planejamento.

## Trechos literais

"A critical insight resulting from our review is that the true potential of LLMs unfolds when they are integrated with traditional symbolic planners, pointing towards a promising neuro-symbolic approach" (resumo, p. 1).

## Marcações

- `[FATO]` a revisão sistematiza 126 artigos em oito categorias de aplicação de LLMs em APS e conclui que a integração neurossimbólica (LLM + planejador simbólico) é mais promissora que o uso isolado de LLMs (resumo).
- `[HIPÓTESE]` interpretação minha: essa conclusão neurossimbólica é compatível com a manutenção da relevância dos planejadores clássicos estudados em 2010 (A2), desde que integrados a componentes de LLM em papéis específicos (tradução, construção de modelo) — a explorar em Q3.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução do PDF em https://arxiv.org/pdf/2401.02500. Conferência humana: pendente.
