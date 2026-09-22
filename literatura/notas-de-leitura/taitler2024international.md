---
tipo: nota-de-leitura
eixo: E3
citekey: taitler2024international
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ai.dmi.unibas.ch/papers/taitler-et-al-aimag2024.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A2, A3, A4]
fragilidades: [F1, F2, F6]
perguntas: [Q1]
---

# The 2023 International Planning Competition

**Taitler, A.; Alford, R.; Espasa, J.; Behnke, G.; Fišer, D.; Gimelfarb, M.; Pommerening, F.; Sanner, S.; Scala, E.; Schreiber, D.; Segovia-Aguas, J.; Seipp, J. · 2024 · AI Magazine 45(2), 280–296**
**Link/DOI:** https://doi.org/10.1002/aaai.12169

## Extração estruturada

- **Problema:** documentar e analisar a edição de 2023 da International Planning Competition (IPC), que teve um número recorde de cinco faixas (clássica/determinística, numérica, HTN, aprendizado, e probabilística/aprendizado por reforço), avaliando métodos de ponta e explorando as fronteiras do planejamento em cada configuração.
- **Método:** artigo de relato (*meeting report*), com uma seção por faixa, descrevendo contexto histórico, domínios novos e recorrentes, metodologia de avaliação (cobertura, pontuação por domínio) e resultados dos planejadores participantes.
- **Dados/benchmarks:** faixa clássica com domínios novos (Folding, Labyrinth, Quantum, Recharging, Ricochet Robots, Rubik's Cube, Slitherlink) e formulações alternativas para testar suporte a características de PDDL (quantificadores, disjunções, condições negativas); faixas satisficing, agile e ótima com dezenas de planejadores competidores.
- **Resultado principal:** na faixa ótima, o planejador Ragnarok (portfólio combinando busca explícita, busca desacoplada, busca simbólica e planejamento *lifted*) venceu, resolvendo o maior número de tarefas em quatro de sete domínios. Na faixa *satisficing*, Scorpion Maidu e Levitron (ambos portfólios) venceram; LAMA — planejador-base de 2011 usado como referência de comparação, não como competidor — obteve pontuação muito alta na faixa *agile* (mais alta que todos os competidores) e ficou atrás de apenas três planejadores na *satisficing*, apesar de não contar para a classificação (Seção "Classical Track").
- **Relação com a dissertação de 2010:**
  - **A2 (confirma e ao mesmo tempo desatualiza):** confirma a continuidade da centralidade de busca heurística (LAMA/Fast Downward) mesmo treze anos depois de 2010 — LAMA de 2011 segue extremamente competitivo em 2023. Mas mostra que os planejadores vencedores atuais são **portfólios híbridos** que combinam várias técnicas ao mesmo tempo (Ragnarok: busca explícita + desacoplada + simbólica + *lifted*; Scorpion Maidu: busca por largura dentro do sistema Scorpion), o que não se encaixa em nenhuma das seis categorias exclusivas de A2 — um planejador vencedor de 2023 pertence simultaneamente a várias "técnicas" de 2010.
  - **A3 (desafia):** o desempenho por domínio varia muito entre planejadores mesmo dentro da mesma faixa — "planners in the second half of the leaderboard were able to achieve the highest (or close to the highest) score in some of the individual domains" — o que é compatível com a tese central de 2010 (características do domínio afetam a técnica vencedora), mas ao mesmo tempo mostra que nenhum planejador único domina todos os domínios, mesmo entre os mais bem ranqueados — um ranking fixo por características do domínio, independente do problema específico (A3), pode ser otimista demais diante dessa variabilidade observada treze anos depois.
  - **A4 (confirma parcialmente):** mais planejadores e domínios (33 domínios ao todo na faixa clássica) permitem observar melhor essa variabilidade fina, sustentando a tese de 2010 de que ampliar planejadores/domínios melhora o poder do ranking — mas a IPC 2023 usa cinco faixas com métricas e formalismos distintos (incluindo domínios numéricos, HTN, aprendizado), sugerindo que "mais planejadores e técnicas" (A4) só melhora o ranking se a comparação permanecer dentro do mesmo formalismo (clássico, determinístico).
  - **F1 (evidencia a lacuna):** confirma que a IPC 2008 (LAMA), a IPC 2023 e treze anos de evolução de competições ficaram fora do corpus de 2010 — reforça a lacuna de revisão já identificada no plano.
  - **F2/F6 (evidencia as fragilidades):** o artigo mostra a escala atual de comparação (dezenas de planejadores, cinco faixas, domínios desenhados especificamente para testar características de PDDL) muito além da amostra de 10 planejadores em 10+3 domínios de 2010 — quantifica concretamente o quanto a amostra de 2010 era pequena (F2) e como as IPCs de hoje ampliaram a cobertura de domínios e formalismos além do estudado em 2010 (F6).

## Pontos relevantes para o projeto

- Fonte robusta e recente (2024, com dados de 2023) para descrever o estado atual das IPCs na revisão — substitui a necessidade de extrapolar a partir de fontes de 2010.
- Mostra que planejadores vencedores atuais são majoritariamente portfólios/híbridos, o que é um achado estrutural importante para T3 (detalhar técnicas, subtécnicas) e para qualquer nova taxonomia proposta na revisão.
- Reporta que LAMA (2011), mesmo usado apenas como "baseline" e não como competidor, teria vencido a faixa *agile* de 2023 — achado forte para ilustrar a durabilidade de uma única técnica de busca heurística com *landmarks*, relevante para A2 e para o Q1 (as conclusões de 2010 se sustentam treze anos depois?).
- Explicita os cinco tipos de faixa da IPC atual (clássica, numérica, HTN, aprendizado, probabilística/RL) — útil para mapear o quanto o escopo de 2010 (só planejamento clássico determinístico com cobertura como métrica) é uma fatia estreita do campo atual.

## Marcações

- `[FATO]` O vencedor da faixa ótima de 2023, Ragnarok, é "a portfolio planner of an explicit state-space search, decoupled search, symbolic search, and a lifted planner with various heuristics" (Seção "Classical Track").
- `[FATO]` LAMA (2011), usado como planejador de referência (*baseline*) e não como competidor, obteve pontuação mais alta que todos os competidores da faixa *agile* de 2023 e ficou atrás de apenas três planejadores na faixa *satisficing* (Seção "Classical Track").
- `[HIPÓTESE]` A persistência do desempenho de LAMA treze anos depois sugere que a "categoria de técnica" vencedora pode ser menos volátil do que a implementação específica do planejador — um argumento a favor de A2 (heurística com *landmarks* continua promissora), mas que exige qualificar A3/A4 quanto à estabilidade do ranking ao longo do tempo, tema direto do Q1 desta revisão.

## Trechos literais

1. "Our baseline planner, LAMA (winner of IPC 2011) [...], surprisingly achieved very high scores in the agile and satisficing track. No planner scored higher in the agile track and only three competing planners scored higher in the satisficing track." (Seção "Classical Track")
2. "The winner of the optimal track, Ragnarok [...], is a portfolio planner of an explicit state-space search, decoupled search, symbolic search, and a lifted planner with various heuristics." (Seção "Classical Track")
3. "Even planners in the second half of the leaderboard were able to achieve the highest (or close to the highest) score in some of the individual domains." (Seção "Classical Track")

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ai.dmi.unibas.ch/papers/taitler-et-al-aimag2024.pdf. Conferência humana: pendente.
