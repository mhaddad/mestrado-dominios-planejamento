---
tipo: nota-de-leitura
eixo: E8
citekey: becker2025measuring
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2507.09089
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A3]
fragilidades: []
perguntas: [Q4]
---

# Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity

**Becker, J.; Rush, N.; Barnes, E.; Rein, D. (METR) · 2025 · arXiv**
**Link/DOI:** https://arxiv.org/abs/2507.09089 (10.48550/arxiv.2507.09089)

## Extração estruturada

- **Problema:** medir o efeito causal de ferramentas de IA de fronteira do início de 2025 sobre a produtividade de desenvolvedores experientes de código aberto, em tarefas reais (não sintéticas), e investigar por que o efeito pode divergir das expectativas.
- **Método:** ensaio controlado randomizado (RCT) de fevereiro a junho de 2025. 16 desenvolvedores experientes (em média 10+ anos de experiência, 5 anos e 1.500 *commits* no repositório específico, representando 59% da vida do repositório) completaram 246 tarefas reais (2,0 horas em média) em repositórios de código aberto maduros e populares que já contribuíam ativamente (em média 23.000 estrelas, 1.100.000 linhas de código, 4.900 *forks*, 20.000 *commits*, 710 *committers*). Cada tarefa foi aleatoriamente designada para permitir ou não uso de IA (principalmente Cursor Pro com Claude 3.5/3.7 Sonnet); pagamento de US$150/hora. Após o estudo, os autores analisaram manualmente 143 horas de gravação de tela (29% do total) e realizaram entrevistas para investigar 21 fatores hipotéticos que poderiam explicar o resultado.
- **Dados/benchmarks:** 246 tarefas reais em repositórios de código aberto de grande porte e alta maturidade; previsões de especialistas em economia e ML coletadas separadamente como comparação.
- **Resultado principal:** ao contrário da previsão dos desenvolvedores (redução de 24% no tempo, antes do estudo) e da estimativa pós-hoc (redução de 20%), permitir uso de IA **aumentou** o tempo de conclusão em 19% — "we find that allowing AI actually increases completion time by 19%—AI tooling slowed developers down" (resumo). Especialistas em economia e ML previram reduções de 39% e 38%, respectivamente, também na direção oposta ao observado. Análise de 21 fatores (Tabela 1 do artigo) aponta 5 fatores com evidência de contribuição à lentidão, incluindo dois ligados diretamente a características do ambiente/tarefa: "Large and complex repositories" (repositórios com média de 10 anos de idade e mais de 1.100.000 linhas de código, em que desenvolvedores relatam que a IA "performa pior") e "High developer familiarity with repositories" (desenvolvedores mais familiarizados com o código desaceleraram mais ao usar IA).
- **Relação com a dissertação de 2010:** **A1** e **A3** [confirma por analogia direta, HIPÓTESE] — o próprio artigo isola, entre 21 fatores testados, características do repositório/tarefa (tamanho, complexidade, maturidade, familiaridade do desenvolvedor) como causas mais prováveis da lentidão observada, e alerta explicitamente que o resultado **não generaliza** para outros cenários: "our results are consistent with small greenfield projects or development in unfamiliar codebases seeing substantial speedup from AI assistance" (Discussão, ressalvas). Isso é, na prática, a mesma lógica de 2010 — desempenho da "técnica" (aqui, uso de IA) depende de características mensuráveis do "domínio" (aqui, tamanho/maturidade/familiaridade do repositório) — mas aplicada a repositórios de software em vez de domínios de planejamento.

## Pontos relevantes para o projeto

- É a evidência central do lote para "efeito nulo/negativo": RCT rigoroso mostrando que IA pode *piorar* produtividade em certas condições, contra a intuição dominante — essencial para a Q4 não assumir que agentes de IA sempre ajudam.
- Metodologicamente é o estudo mais forte do lote para a pergunta "o efeito varia com a tarefa/repositório/desenvolvedor": os autores testam 21 hipóteses de forma sistemática e relatam evidência a favor, contra ou mista para cada uma (Tabela 1 do corpo do artigo, com detalhe no Apêndice C).
- Ressalva explícita dos próprios autores de que o efeito é específico ao cenário (repositórios grandes, maduros, alta familiaridade do desenvolvedor) — ponto de rigor metodológico que evita generalização indevida, algo a se espelhar na revisão de 2010.
- Nomeiam limitações da própria IA como fator ("Low AI reliability": desenvolvedores aceitam menos de 44% das gerações da IA; "Implicit repository context": IA não usa conhecimento tácito do repositório) — dimensão que 2010 não tinha, pois a "técnica" era um planejador determinístico, não um modelo com taxa de aceitação variável.

## Marcações

- `[FATO]` "Surprisingly, we find that allowing AI actually increases completion time by 19%—AI tooling slowed developers down. This slowdown also contradicts predictions from experts in economics (39% shorter) and ML (38% shorter)" (resumo).
- `[FATO]` "Large and complex repositories (C.1.3) [Æ] Developers report AI performs worse in large and complex environments... Repositories average 10 years old with >1,100,000 lines of code" e "High developer familiarity with repositories (C.1.2) Developers slowed down more on issues they are more familiar with" (Tabela 1, Seção 3.3).
- `[FATO]` "our results are consistent with small greenfield projects or development in unfamiliar codebases seeing substantial speedup from AI assistance" (Seção 4.1, Setting-specific factors).
- `[HIPÓTESE]` O fato de os próprios autores atribuírem o efeito a características do repositório/tarefa e alertarem contra a generalização é a confirmação mais forte do lote, entre os estudos empíricos com desenvolvedores reais, de que a tese de 2010 — desempenho de uma técnica depende de características mensuráveis do domínio/tarefa — se sustenta também no domínio de agentes de IA para desenvolvimento de software.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2507.09089 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
