---
tipo: nota-de-leitura
eixo: E2
citekey: fawcett2014improved
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/download/13680/13529
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A5, A7]
fragilidades: [F3, F5]
perguntas: [Q2]
---

# Improved Features for Runtime Prediction of Domain-Independent Planners

**Fawcett, C.; Vallati, M.; Hutter, F.; Hoffmann, J.; Hoos, H.H.; Leyton-Brown, K. · 2014 · Proceedings of ICAPS 2014, pp. 355–359**
**Link/DOI:** https://doi.org/10.1609/icaps.v24i1.13680

## Extração estruturada

- **Problema:** planejadores de última geração exibem grande variação de tempo de execução entre instâncias; o artigo quer prever esse tempo (*runtime*) com precisão a partir de características extraídas automaticamente de cada instância, construindo *empirical performance models* (EPMs).
- **Método:** define um conjunto de 311 *features* organizadas em 8 grupos — (1) PDDL (domínio, instância, requisitos da linguagem — extensão das 32 *features* de Roberts et al. 2008); (2) FDR (tradução para representação de domínio finito do Fast Downward: variáveis, grupos *mutex*, efeitos); (3) grafo causal e DTG (*domain transition graph*, os 41 atributos de Cenamor et al. 2012/2013); (4) pré-processamento do LPG; (5) *Torchlight* (topologia de busca local sob h+, Hoffmann 2011); (6) sondagem do Fast Downward (*FD probing*: rodar o planejador por 1 segundo e medir estatísticas da trajetória); (7) representação SAT (115 *features* via SATzilla 2012, a partir de uma codificação SAT da tarefa); (8) sucesso e tempo de extração de cada extrator. Treina *random forests* (e compara com regressão linear, redes neurais, processos gaussianos, árvores de regressão) sobre 7571 instâncias, com validação cruzada 10-*fold* e *leave-one-domain-out* (180 domínios).
- **Dados/benchmarks:** 7571 instâncias de PDDL de IPC'98–IPC'11 (faixas determinísticas e de aprendizado), bibliotecas de *benchmark* do FF e do Fast Downward, UCPOP Strict, e os domínios Sodor/Stek de Roberts et al. (2008); 7 planejadores (Arvand, Fast Downward, FF v2.3, FF-X, LAMA, LPG, LPG-contra, Metric-FF, Mp, Probe).
- **Resultado principal:** as *features* novas superam substancialmente as 32 *features* PDDL de Roberts et al. (2008) e o conjunto combinado com as *features* de grafo causal/DTG de Cenamor et al., tanto em validação cruzada aleatória quanto em *leave-one-domain-out* (mais difícil); para LAMA, 90,5% das previsões ficam a um fator de 2 do tempo real com o conjunto completo, contra 83,1% usando só as *features* PDDL de Roberts et al.
- **Relação com a dissertação de 2010:**
  - **A1 (corrige/refina):** 2010 relaciona características de domínio (extraídas de UML) a desempenho de técnicas. Este artigo mostra, em domínio de planejamento clássico, que as características que realmente carregam poder preditivo não são contagens sintáticas simples (nº de classes/atributos análogo às *features* PDDL) mas estruturas derivadas — grafo causal, DTG, sondagem de busca e codificação SAT. "Predicting performance is an important research direction... Improvements in prediction depend critically on stronger features, which we consider to be a gaping hole in the planning literature" (Conclusões). Ou seja, a intuição de A1 (características → desempenho) é validada, mas a base de características de 2010 (UML) é, por analogia direta com as *features* PDDL aqui testadas, do tipo mais fraco.
  - **A5 (corrige):** 2010 afirma que diagramas UML medem a complexidade do domínio e essa complexidade afeta o desempenho. Este artigo mostra empiricamente que a complexidade relevante para desempenho está em estruturas de grafo (causal/DTG) e em sondagem de busca, não em contagens de elementos de diagrama; as *features* de grafo causal/DTG (Cenamor et al.) já superam as puramente sintáticas, e a adição de sondagem/SAT supera ambas.
  - **A7 (corrige):** 2010 reduz eficiência a cobertura. Este artigo prevê diretamente o tempo de execução (log-*runtime*) como variável contínua, não apenas sucesso/fracasso — mostrando que a comunidade já ia além da cobertura binária em 2014 (e a rigor desde Roberts et al. 2008/2009, citados aqui).
- **Features por classe (para Q2):** sintáticas de PDDL (domínio/instância/requisitos, 42 *features* — extensão de Roberts et al. 2008); estruturais de grafo causal/DTG (41 *features*, de Cenamor et al.); de sondagem (*probing*: FD probing, 16 *features*; Torchlight, 10 *features*, baseado em topologia de busca sob h+); de modelo/representação (FDR, 19 *features*; SAT, 115 *features* via SATzilla).

## Pontos relevantes para o projeto

- É a obra central do eixo E2 para a pergunta Q2: contrasta explicitamente 4 famílias de *features* (sintáticas PDDL, estruturais de grafo causal/DTG, de sondagem, de representação SAT) e mede a contribuição marginal de cada uma via seleção progressiva (*forward selection*) e custo computacional (Tabela 1, classes "trivial/cheap/moderate/expensive").
- Mostra que "cheap" *features* já superam o estado da arte anterior e "moderate" chegam perto do modelo completo — achado útil para qualquer proposta de extensão de 2010 que precise justificar custo/benefício de novas métricas.
- Cita diretamente Roberts et al. (2008) e Roberts & Howe (2009) como linha de base, e Cenamor et al. (2012, 2013) como extensão intermediária — dá a genealogia completa da linha de pesquisa que 2010 não menciona (A8).
- Não há uma única *feature* mais importante entre planejadores — "there is not a unique subset of important features shared by all planners" — relevante para A4 (mais características melhoram o *ranking*), mostrando que a relação característica→planejador é específica por planejador, não universal.

## Marcações

- `[FATO]` O conjunto de 311 *features* supera, em RMSE de log-tempo de execução, tanto as 32 *features* PDDL de Roberts et al. (2008) quanto essas somadas às 41 *features* de grafo causal/DTG de Cenamor et al., em validação cruzada aleatória e *leave-one-domain-out* (Tabelas 3 e 4).
- `[FATO]` As *features* de sondagem (FD probing) e de codificação SAT são introduzidas nesta obra pela primeira vez na literatura de planejamento, adaptadas respectivamente de Fast Downward e de SATzilla (Seção "Features").
- `[HIPÓTESE]` Se a dissertação de 2010 tivesse acesso a esta linha de pesquisa, a UML provavelmente seria substituída ou complementada por métricas de grafo causal/DTG extraídas automaticamente do PDDL, já que estas mostraram poder preditivo muito superior a contagens sintáticas comparáveis às da UML.

## Trechos literais

1. "We propose a new, extensive set of instance features for planning, and investigate its effectiveness across a range of model families." (Resumo)
2. "Our new feature set derives 311 values from a given PDDL domain and instance file." (Seção *Features*, p. 355)
3. "Improvements in prediction depend critically on stronger features, which we consider to be a gaping hole in the planning literature." (Conclusões, p. 358)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/ICAPS/article/download/13680/13529 (baixado com `curl`, extraído com `pdftotext -layout`). Conferência humana: pendente.
