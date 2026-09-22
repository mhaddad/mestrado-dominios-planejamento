---
tipo: nota-de-leitura
eixo: E2
citekey: roberts2009learning
prioridade: A
status: lido
profundidade: resumo
fonte-lida: https://www.sciencedirect.com/science/article/pii/S0004370208001896
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A7, A8]
fragilidades: [F1]
perguntas: [Q1, Q2]
---

# Learning from Planner Performance

**Roberts, M.; Howe, A.E. · 2008 (publicado 2009) · Artificial Intelligence 173(5-6), 536–561**
**Link/DOI:** https://doi.org/10.1016/j.artint.2008.11.009

## Extração estruturada

- **Problema:** a comunidade de planejamento acumulou grande quantidade de problemas públicos em uma linguagem de entrada padronizada e planejadores que a aceitam; o artigo aproveita isso para coletar dados sobre como diversos planejadores se saem nesses problemas de referência e aprender sobre o estado da arte em planejamento clássico.
- **Método (pelo resumo):** análises retrospectivas, prescritivas e prospectivas. Primeiro, caracterizam problemas e planejadores em termos de dificuldade, diversidade e tendências ao longo do tempo, confirmando estatisticamente que os conjuntos de problemas ficaram mais difíceis e que planejadores novos são geralmente mais capazes; visualizam o sucesso dos planejadores por domínio. Segundo, aprendem automaticamente modelos de sucesso e de tempo para cada planejador, construídos a partir de *features* facilmente extraídas de problemas e domínios, usando técnicas de aprendizado de máquina prontas ("*off-the-shelf*"). Terceiro, aplicam os dados a um modelo explicativo já existente que liga espaço de busca e desempenho do planejador (a topologia de Hoffmann), validando essa ligação em um conjunto mais amplo de planejadores. Por fim, constroem novos problemas para preencher lacunas observadas nos *benchmarks* existentes.
- **Dados/benchmarks:** não determinado nesta leitura (resumo apenas); pelo contexto citado por outras obras do lote, o conjunto é conhecido na literatura como "Roberts et al. (2008)" ou "challenge 3", com 32 *features* PDDL de domínio/instância/requisitos de linguagem.
- **Resultado principal (pelo resumo):** os modelos de sucesso mostraram-se extremamente precisos; os modelos de tempo, menos. O estudo valida resultados anteriores ligando topologia de busca a desempenho de planejadores em um conjunto mais amplo de planejadores que o estudo original.
- **Relação com a dissertação de 2010:**
  - **F1 (evidencia lacuna):** a dissertação de 2010 lista, como únicos trabalhos relacionados citados (A8), Hoffmann (2001, topologia do espaço de busca) e Gerevini, Saetti e Serina (2004, heurísticas do LPG) — **não cita Roberts & Howe (2009)**, apesar de ser um trabalho quase contemporâneo (publicado um ano antes da dissertação) e diretamente sobre o mesmo tema central de 2010: prever, a partir de características de problemas/domínios, qual planejador terá melhor desempenho. Esta é uma lacuna de revisão concreta e verificável.
  - **A1 (confirma em espírito, corrige na operacionalização):** confirma a ideia geral de que características de domínio/problema predizem desempenho de planejador — mas opera com *features* extraídas automaticamente do PDDL (não com diagramas UML modelados manualmente) e usa aprendizado de máquina supervisionado para construir o modelo preditivo, em vez de um *ranking* direto por característica discretizada.
  - **A7 (corrige):** 2010 reduz eficiência a cobertura (percentual de problemas resolvidos). Este artigo já modela, em 2008/2009, **dois** alvos de previsão — sucesso (análogo a cobertura) **e** tempo de execução — mostrando que a comunidade já tratava desempenho como multidimensional antes de 2010.
- **Features por classe (para Q2):** sintáticas de PDDL (32 *features* de domínio/instância/requisitos de linguagem, segundo a caracterização feita por Fawcett et al. 2014 e De la Rosa et al. 2017, que leem e estendem este trabalho — não confirmado diretamente nesta leitura de resumo).

## Pontos relevantes para o projeto

- É a obra "semente" do eixo E2 e, por não estar entre as fontes citadas em 2010 (A8), constitui a evidência mais direta e concreta da fragilidade F1 encontrada neste lote.
- Todas as demais obras lidas neste lote (Fawcett et al. 2014, De la Rosa et al. 2017, Hoffmann 2011) citam este trabalho como ponto de partida ou baseline a ser superado — over o campo inteiro de EPMs para planejamento se define em relação a ele.
- Não foi possível obter o texto integral (ScienceDirect bloqueou o acesso automatizado); a leitura ficou restrita ao resumo, recuperado de uma cópia arquivada da página do editor. Uma leitura de texto integral (via acesso institucional) é recomendada antes de qualquer citação textual mais detalhada na dissertação revisada.

## Marcações

- `[FATO]` O artigo aprende modelos de sucesso e de tempo de planejadores a partir de *features* de problemas/domínios, usando aprendizado de máquina supervisionado pronto, e relata que os modelos de sucesso são "extremamente precisos" e os de tempo, "menos precisos" (Resumo).
- `[FATO]` A dissertação de 2010 (A8) não cita esta obra entre seus trabalhos relacionados, apesar de tratar do mesmo problema central um ano antes.
- `[HIPÓTESE]` A ausência desta citação em 2010 pode ter contribuído para a taxonomia de técnicas mais simples e a métrica de eficiência restrita à cobertura (A6, A7) — se 2010 tivesse incorporado esta linha, provavelmente teria adotado tempo de execução como segunda variável de desempenho e talvez já tivesse usado *features* extraídas automaticamente do PDDL em paralelo à UML.

## Trechos literais

1. "The planning community has amassed a large body of publicly available problems in a standardized input language and planners that accept the language. We seized this remarkable opportunity to collect data about how some of these planners perform on the benchmark problems." (Resumo)
2. "The second analyses automatically learn models of success and time for each planner. The models are constructed from easily extracted features of problems and domains and use off-the-shelf Machine Learning techniques. We find the models of success to be extremely accurate, but the models of time to be less so." (Resumo)
3. "Our study validates previous results linking search topology with planner performance on a wider set of planners than the original study." (Resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://www.sciencedirect.com/science/article/pii/S0004370208001896 (texto integral bloqueado por controle de acesso do editor; resumo recuperado de cópia arquivada da página, Wayback Machine, snapshot de 18/04/2024). Conferência humana: pendente — recomenda-se nova tentativa de leitura de texto integral via acesso institucional.
