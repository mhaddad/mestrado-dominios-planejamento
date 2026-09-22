---
tipo: nota-de-leitura
eixo: E2
citekey: delarosa2017performance
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/download/13848/13697
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A3]
fragilidades: [F2, F3]
perguntas: [Q1, Q2]
---

# Performance Modelling of Planners from Homogeneous Problem Sets

**De la Rosa, T.; Cenamor, I.; Fernández, F. · 2017 · Proceedings of ICAPS 2017, pp. 425–433**
**Link/DOI:** https://doi.org/10.1609/icaps.v27i1.13848

## Extração estruturada

- **Problema:** verificar se os modelos empíricos de desempenho (EPMs) de planejadores realmente aprendem a diferenciar instâncias pela sua dificuldade intrínseca de busca (*search space discrimination*), e não apenas pelo domínio a que pertencem (*domain discrimination*) ou pelo tamanho do problema (*size discrimination*) — as três formas de discriminação que os autores distinguem explicitamente.
- **Método:** treina EPMs usando **conjuntos de problemas homogêneos**: 200 instâncias por domínio geradas com os mesmos parâmetros de entrada de um gerador aleatório (mesma distribuição de objetos, estado inicial e metas), o que elimina a discriminação por domínio e por tamanho, isolando o efeito de *features* de espaço de busca. Usa como base as *features* do IBaCoP2 (heurísticas do estado inicial, incluindo *red-black*) e propõe *features* novas: (a) *fact balance* (equilíbrio de fatos no plano relaxado, calculado camada a camada do *relaxed planning graph*); (b) *features* do grafo de *landmarks* (nº de nós, arestas, nós-pai/filho, razões). Classificadores (Naive Bayes, árvore de decisão, *random forest*, *rotation forest*) preveem se um problema é "fácil" ou "difícil" por percentil de tempo de execução, avaliados por AUROC.
- **Dados/benchmarks:** planejadores LAMA, Mercury e Probe; domínios Barman, Depots, Elevators, Floortile, Satellite e TPP (selecionados por maior coeficiente de variação do tempo de execução entre os candidatos de IPC-2011/2014); 200 problemas por domínio.
- **Resultado principal:** os modelos treinados superam sistematicamente um classificador aleatório (AUROC > 0,5), confirmando que existe discriminação por espaço de busca mesmo dentro de um único domínio homogêneo; as novas *features* (grafo de *landmarks*, *fact balance*) melhoram o AUROC frente ao conjunto IBaCoP2; e nenhuma *feature* PDDL (sintática) contribuiu para a discriminação.
- **Relação com a dissertação de 2010:**
  - **A3 (corrige/limita):** 2010 afirma que, só com as características do domínio (independente do problema), o *ranking* já escolhe os melhores planejadores. Este artigo mostra que, quando o domínio é fixado (problemas homogêneos do mesmo domínio), as *features* de nível de domínio/PDDL **não têm nenhum poder discriminativo** — "As expected, none of the PDDL features appear in the list" (Seção *Ranking of Features*, p. 431) — e é preciso recorrer a *features* do espaço de busca de cada instância (heurísticas, grafo de *landmarks*, equilíbrio de fatos) para diferenciar problemas fáceis de difíceis dentro do mesmo domínio. Isso é evidência direta contra a suficiência de características de domínio isoladas do problema, tal como postulado em A3.
  - **A1 (corrige/refina):** reforça que "características do domínio" no sentido de contagens sintáticas (comparáveis às métricas UML de 2010) só discriminam entre domínios diferentes, não dentro de um domínio — os autores chamam isso de "domain discrimination" e a tratam como um viés indesejado de modelos anteriores: "there is no justified correlation between shallow features such as the number of PDDL actions and the difficulty of a planning task" (Introdução).
  - **F3 (evidencia):** ao mostrar que características sintáticas simples "poderiam ser artificialmente modificadas na descrição PDDL sem alterar em nada o desempenho de um planejador", corrobora, por analogia direta, a fragilidade das métricas de diagrama UML de 2010, que também dependem de decisões superficiais de modelagem sem relação causal garantida com desempenho.
  - **F2 (evidencia):** o desenho experimental — conjuntos homogêneos de apenas 6 domínios e 3 planejadores — é reconhecido pelos próprios autores como limitado; ilustra como mesmo trabalhos de 2017 lidam com amostras pequenas nesse tipo de estudo, o que contextualiza (sem justificar) a fragilidade F2 de 2010.

## Pontos relevantes para o projeto

- Distinção conceitual explícita entre três tipos de discriminação que um EPM pode capturar — domínio, tamanho, espaço de busca — é uma ferramenta analítica útil para reformular A1/A3 numa versão revisada da dissertação: a afirmação "características do domínio preveem desempenho" precisa dizer *qual* dos três tipos de discriminação está em jogo.
- Related Work do artigo resume a evolução direta da linha de pesquisa que 2010 não cita: Roberts et al. (2008/2009) → Cenamor et al. (2012/2013, grafo causal/DTG) → Fawcett et al. (2014, sondagem e SAT) → este trabalho (*fact balance* e grafo de *landmarks*). Boa base para reconstruir a árvore genealógica do eixo E2.
- Resultado por domínio é heterogêneo: em Elevators, todas as *features* têm contribuição nula (Tabela 4) — mostra que mesmo a discriminação por espaço de busca não é garantida em todo domínio, o que é relevante para Q1 (as conclusões de 2010 se sustentam com mais dados?).

## Marcações

- `[FATO]` Nenhuma *feature* sintática de PDDL apareceu entre as *features* relevantes para discriminar problemas fáceis/difíceis dentro de conjuntos homogêneos de um mesmo domínio (Seção *Ranking of Features*, Tabela 7, p. 431).
- `[FATO]` As *features* de grafo de *landmarks* e de equilíbrio de fatos (propostas neste artigo) aumentaram o AUROC em relação ao conjunto de base IBaCoP2 em quase todos os domínios testados (Seção *Performance Modelling*, p. 429–431).
- `[HIPÓTESE]` A dependência entre "nível de granularidade das características" (domínio vs. instância) e "tipo de discriminação possível" sugere que a metodologia de 2010 — que usa só características de domínio via UML — está estruturalmente limitada à discriminação entre domínios, não podendo, por desenho, capturar a variação de dificuldade dentro de um mesmo domínio.

## Trechos literais

1. "there is no clear evidence that EPMs are able to classify planning tasks by their intrinsic difficulty and not by other properties that make them different from other examples of the training set" (Introdução, p. 425)
2. "As expected, none of the PDDL features appear in the list." (Seção *Ranking of Features*, p. 431)
3. "Roberts et al. 2008; 2009 trained EPMs on known benchmarks up to 2008... The features used to generate their models were from the domain and problem definition. Therefore, this set of features is not useful for models trained with homogenous problem sets given that they will produce the same values." (Related Work, p. 426)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/ICAPS/article/download/13848/13697 (baixado com `curl`, extraído com `pdftotext -layout`). Conferência humana: pendente.
