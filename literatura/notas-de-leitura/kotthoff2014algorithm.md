---
tipo: nota-de-leitura
eixo: E1
citekey: kotthoff2014algorithm
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2460/2438
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1]
fragilidades: [F1, F4]
perguntas: [Q1, Q2]
---

# Algorithm Selection for Combinatorial Search Problems: A Survey

**Kotthoff, L. · 2014 · AI Magazine 35(3), 48–60**
**Link/DOI:** https://doi.org/10.1609/aimag.v35i3.2460

## Extração estruturada

- **Problema:** revisar de forma unificada e organizada toda a literatura de seleção de algoritmo para problemas de busca combinatória (SAT, CSP, planejamento etc.) até 2014.
- **Método:** *survey* narrativo organizado por critérios que determinam sistemas de seleção de algoritmo na prática — portfólios estáticos vs. dinâmicos, o que selecionar (algoritmo único vs. escalonamento), quando selecionar (offline vs. online), modelos de desempenho (por portfólio, por algoritmo, híbridos) e tipos de *features* (estáticas, dinâmicas, de baixo/alto conhecimento de domínio).
- **Dados/benchmarks:** não aplicável (*survey*); usa contagem de publicações por ano como evidência do crescimento do campo (dados de `4c.ucc.ie/~larsko/assurvey`).
- **Resultado principal:** reproduz e usa como ponto de partida o modelo original de Rice (1976, Figura 1 do artigo); mapeia dezenas de sistemas (SATzilla, ISAC, 3S, CSHC etc.) segundo os critérios propostos; conclui que o campo é fragmentado, com reinvenção frequente de técnicas por falta de comunidade unificada.
- **Relação com a dissertação de 2010:**
  - **A1 (confirma o princípio geral):** reproduz literalmente o diagrama e a formalização de Rice (1976) como base de todo o campo — o mesmo princípio subjacente a A1 (características de domínio/instância predizem técnica de melhor desempenho), generalizado para além de planejamento.
  - **F1 (evidencia a lacuna, quantitativamente):** o gráfico de publicações por ano do artigo (Figura 3) mostra crescimento acentuado do campo de seleção de algoritmo a partir de 2007 (após o sucesso de SATzilla na Competição SAT) — ou seja, entre 2007 e 2010 (ano da dissertação) já havia literatura substancial e crescente sobre seleção de algoritmo por características, da qual 2010 não cita nenhuma obra.
  - **F4 (evidencia a fragilidade da taxonomia, de forma indireta):** o *survey* desaconselha explicitamente usar "*portfolio*" como sinônimo livre de "*algorithm selector*" por gerar confusão — o mesmo tipo de cuidado terminológico que falta na taxonomia de técnicas de 2010 (A6), sugerindo que imprecisão terminológica é um problema conhecido e recorrente na área, não uma falha isolada de 2010.

## Pontos relevantes para o projeto

- O artigo já observa (em 2014) que outros sistemas raramente reaproveitam as ideias de SATzilla diretamente, apesar de sua proeminência — evidência de fragmentação da literatura, relevante para contextualizar (não desculpar) por que 2010 pode ter perdido essa linha de pesquisa.
- A classificação dos "tipos de predição" (categórica única, tempo de execução por algoritmo, ordenação completa) é vocabulário técnico útil para precisar o que exatamente o "ranking de planejadores por domínio" de 2010 está tentando prever.
- O autor disponibiliza uma tabela viva de publicações (nota de rodapé), sinal de que a área valoriza rastreabilidade e atualização contínua — coerente com a prática da própria revisão em curso.

## Trechos literais

1. "The original description of the algorithm selection problem was published by Rice (1976). The basic model described in the article is very simple — given a space of instances and a space of algorithms, map each instance-algorithm pair to its performance." (texto principal, junto à Figura 1)
2. "there is no algorithm selection community in the same sense in which there is for example a SAT community. As a result, publications are fragmented and scattered throughout different areas of AI." (Algorithm Selection in Practice)
3. "Despite the theoretical difficulty of algorithm selection, dozens of systems have demonstrated that it can be done in practice with great success." (Summary)

## Marcações

- `[FATO]` O artigo reproduz o modelo original de Rice (1976) como ponto de partida de todo o campo de seleção de algoritmo (Figura 1; texto introdutório).
- `[FATO]` A Figura 3 do artigo mostra crescimento acentuado do número de publicações em seleção de algoritmo a partir de 2007.
- `[HIPÓTESE]` A fragmentação da literatura de seleção de algoritmo, reconhecida pelo próprio autor, é uma explicação plausível — mas não uma justificativa metodológica — para a ausência dessas referências em 2010 (F1).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2460/2438. Conferência humana: pendente.
