---
tipo: sintese-de-eixo
eixo: E2
obras: 15
data: 2026-09-22
---

# E2 — *Features* de tarefas de planejamento e predição de desempenho

## 1. Pergunta e resposta curta

Que características de tarefas de planejamento predizem o desempenho de planejadores, e como foram extraídas? [FATO] A literatura de 2008 a 2022 mostra uma progressão de famílias de *features* — sintáticas de PDDL, estruturais (grafo causal, DTG, *treewidth*, hipergrafo), de sondagem (*probing*) e de representação (FDR, SAT) —, com poder preditivo crescente nessa ordem [@roberts2009learning; @fawcett2014improved; @delarosa2017performance]. *Features* sintáticas simples discriminam bem entre domínios diferentes, mas quase nada dentro de um mesmo domínio [@delarosa2017performance]. Estruturas derivadas automaticamente do PDDL (grafo causal, DTG, *treewidth*) têm fundamentação formal, são reprodutíveis e afetam demonstravelmente o desempenho de heurísticas [@helmert2009concise; @hoffmann2011analyzing; @domshlak2013complexity]. Nenhuma nota encontrou trabalho aplicando métricas de diagramas UML (o recorte de 2010) a domínios de planejamento — lacuna confirmada por busca dirigida (ver seção 6).

## 2. O que a literatura estabelece

### Famílias de *features*

[FATO] Fawcett et al. (ICAPS 2014) organizam 311 *features* em oito grupos, taxonomia de referência do eixo: sintáticas de PDDL (extensão de Roberts & Howe, 2008); FDR; grafo causal/DTG (Cenamor et al.); pré-processamento do LPG; TorchLight (topologia sob h+); sondagem do Fast Downward (*probing*, 1s); representação SAT (SATzilla); custo/sucesso da extração [@fawcett2014improved]. Para Q2, quatro famílias importam: **sintáticas** (contagens de PDDL), **estruturais** (grafo causal/DTG, formalizados por Helmert [@helmert2009concise]), **de sondagem** (rodar o planejador por pouco tempo — introduzida em planejamento por Fawcett et al. [@fawcett2014improved], com precedente em SAT/MIP/TSP [@hutter2014algorithm]) e **de representação/modelo** (FDR, SAT, ou saída de modelo aprendido [@percassi2021improving]). De la Rosa et al. (2017) acrescentam *fact balance* e atributos do grafo de *landmarks*, com ganho de AUROC sobre o IBaCoP2 [@delarosa2017performance]. Abordagens recentes substituem *features* tabulares por grafos processados em redes neurais: PDDL [@ferber2019ipc], hipergrafos STRIPS [@shen2020learning], grafos geométricos [@odense2022neural], grafos de extração de proposições em CBP [@vallati2015identifying]. O paradigma *features* → modelo estatístico → predição vem de fora do planejamento, fundado em leilões combinatórios [@leytonbrown2009empirical] e otimizado para SAT/MIP/TSP [@hutter2014algorithm].

### O que confunde a predição

[FATO] De la Rosa et al. (2017) mostram que, controlando o domínio (200 instâncias homogêneas), nenhuma *feature* sintática de PDDL discrimina problemas fáceis de difíceis — "As expected, none of the PDDL features appear in the list" [@delarosa2017performance]. Distinguem três formas de discriminação que um modelo pode capturar sem isso ficar claro no agregado: por domínio, por tamanho e por espaço de busca — um modelo acurado pode estar só reconhecendo o domínio de origem [@delarosa2017performance]. [FATO] Fawcett et al. (2014) observam ainda que não há subconjunto único de *features* importantes comum a todos os planejadores [@fawcett2014improved]. [HIPÓTESE] Logo, "quais *features* predizem melhor" precisa ser condicionado ao nível da pergunta e ao planejador-alvo — o nível em que operam as métricas UML de 2010.

### *Features* estruturais do modelo: grafo causal, DTG, hipergrafo, *treewidth*

[FATO] Helmert (2009) define formalmente, via PDDL→FDR (SAS+), o grafo causal e o DTG, um grafo por variável [@helmert2009concise] — estruturas algorítmicas e reprodutíveis, ao contrário de um diagrama UML modelado à mão. Sem a tradução FDR concisa, a heurística de grafo causal do Fast Downward "não é competitiva com outras abordagens" [@helmert2009concise]. [FATO] Hoffmann (2011) liga ciclicidade/invertibilidade do grafo causal à ausência de mínimos locais sob h+: "At the level of their PDDL domain descriptions, the difference is not evident... What does the trick is to move to the finite-domain variable representation... and to consider the associated structures, notably the causal graph" [@hoffmann2011analyzing]. Sua crítica a Roberts & Howe — *features* "que dificilmente capturam uma estrutura independente de domínio relevante ao desempenho" [@hoffmann2011analyzing] — aplica-se por analogia às contagens de diagrama UML de 2010. [FATO] Domshlak & Nazarenko (2013) mostram que planejamento monotônico ótimo é difícil mesmo com grafos causais simples quando os domínios de variável são grandes, mas tratável em tempo exponencial só no *treewidth* do grafo causal, com domínios de tamanho constante [@domshlak2013complexity]. [FATO] Shen, Trevizan & Thiébaux (2020) generalizam para hipergrafo, para heurísticas que generalizam entre domínios nunca vistos [@shen2020learning].

## 3. Percurso 2008–2026

[FATO] Roberts & Howe (2008/2009), obra semente, aprendem modelos de sucesso e tempo a partir de *features* sintáticas de PDDL [@roberts2009learning]. Leyton-Brown, Nudelman & Shoham (2009) fundam, em paralelo, a metodologia de cinco passos em leilões combinatórios [@leytonbrown2009empirical]. Hoffmann (2011) formaliza a ligação entre grafo causal e topologia de busca, criticando a pobreza das *features* de Roberts & Howe [@hoffmann2011analyzing]. Hutter et al. (2014) otimizam a modelagem estatística (*random forests*) para SAT/MIP/TSP, referência adotada em planejamento [@hutter2014algorithm]. Fawcett et al. (2014), ponto de inflexão, introduzem sondagem e representação SAT em 311 *features*, superando Roberts & Howe [@fawcett2014improved]. Vallati, Chrpa & Kitchin (2014, ASAP) deslocam o foco para conhecimento operacional de planos de treino, mostrando que a codificação do domínio pesa tanto quanto o algoritmo [@vallati2014asap]. Ferber et al. (2019) fornecem dados em grafo para GNNs [@ferber2019ipc]. De la Rosa et al. (2017) isolam o efeito de granularidade domínio vs. instância [@delarosa2017performance]. Vallati et al. (2015/2016) aplicam *features* de grafo à recuperação de planos em CBP [@vallati2015identifying]. Shen, Trevizan & Thiébaux (2020) levam a estrutura ao hipergrafo [@shen2020learning]; Percassi et al. (2021) integram a predição de custo à própria heurística de busca [@percassi2021improving]; Odense, Gupta & Macready (2022) replicam a lógica em robótica via GNNs [@odense2022neural]; Muñoz et al. (2017/2018) fundam a *instance space analysis* fora do planejamento [@munoz2017instance]. [HIPÓTESE] A trajetória mostra tendência dupla: de *features* tabulares para grafos/hipergrafos com aprendizado profundo, e de "prever se/quando" para "prever quanto" dentro do próprio mecanismo de busca — nenhum dos dois movimentos está presente em 2010.

## 4. Relação com a dissertação de 2010

| Rótulo | Confirma/corrige/obsoleta/amplia | O que a literatura mostra | Chaves |
|---|---|---|---|
| A1 | Corrige/refina | Contagens sintáticas (comparáveis à UML) só discriminam entre domínios, não dentro deles; grafo causal/DTG e sondagem predizem muito melhor | [@delarosa2017performance; @fawcett2014improved; @roberts2009learning; @vallati2015identifying; @odense2022neural] |
| A2 | Amplia | Técnicas listadas como promissoras seguem ativas — heurísticas hoje podem ser aprendidas (hipergrafos) e generalizar entre domínios | [@shen2020learning] |
| A3 | Corrige | Dentro de um domínio fixo, *features* de nível de domínio não discriminam nada; é preciso recorrer a *features* de instância/espaço de busca | [@delarosa2017performance] |
| A4 | Amplia (ressalva) | Mais *features* melhoram a predição, mas não há subconjunto único comum a todos os planejadores — relação específica por planejador | [@fawcett2014improved] |
| A5 | Corrige | O determinante formal da dificuldade é grafo causal, DTG e *treewidth*, extraídos automaticamente, não contagens de diagrama | [@helmert2009concise; @hoffmann2011analyzing; @domshlak2013complexity] |
| A6 | Corrige | A "técnica" de um planejador não é propriedade fixa: muda de posição no *ranking* conforme a codificação do domínio | [@vallati2014asap] |
| A7 | Corrige | Desempenho já era multidimensional (sucesso e tempo) desde 2008/2009; hoje soma-se o custo do plano, dentro do próprio mecanismo de busca | [@roberts2009learning; @ferber2019ipc; @percassi2021improving] |
| A8 | Amplia/atualiza | 2010 cita só Hoffmann (2001) e Gerevini et al. (2004); Roberts & Howe (2009), contemporânea e sobre o mesmo tema, não é citada, nem sua evolução formal em Hoffmann (2011) | [@roberts2009learning; @hoffmann2011analyzing] |
| F1 | Confirma | Lacuna concreta: Roberts & Howe (2009) não é citada em 2010, apesar da mesma pergunta um ano antes | [@roberts2009learning; @hoffmann2011analyzing] |
| F2 | Confirma | Amostras pequenas continuam comuns mesmo em 2017 (6 domínios, 3 planejadores) | [@delarosa2017performance] |
| F3 | Confirma | Grafo causal/DTG são reprodutíveis e determinísticos, ao contrário de métricas UML dependentes do modelador; *features* sintáticas também são manipuláveis sem alterar o desempenho real | [@helmert2009concise; @delarosa2017performance] |
| F4 | Confirma | Taxonomia de técnicas fixa é discutível: codificação do domínio e algoritmo interagem | [@vallati2014asap] |
| F5 | Confirma (superação parcial) | Já existe trabalho que otimiza custo de plano dentro da própria heurística, além da cobertura | [@percassi2021improving] |
| F6 | Confirma (aponta solução) | Existe hoje infraestrutura de dados consolidada de IPCs que resolve o problema de dados fora de competições | [@ferber2019ipc] |

## 5. Divergências e pontos em disputa

[FATO] Há divergência sobre em que nível medir a "estrutura do domínio". Uma linha (Helmert, Hoffmann, Domshlak & Nazarenko) defende estruturas formais do PDDL — grafo causal, DTG, *treewidth* — com efeito causal demonstrado sobre heurísticas [@helmert2009concise; @hoffmann2011analyzing; @domshlak2013complexity]. Outra (Fawcett et al., De la Rosa et al.) testa empiricamente qual família prediz melhor, concluindo que sondagem supera grafos estáticos, a maior custo computacional [@fawcett2014improved; @delarosa2017performance]. [HIPÓTESE] As duas respondem perguntas diferentes — por que a estrutura afeta o desempenho vs. quanto ela ajuda a prever. [FATO] Há também disputa sobre se a "técnica" de um planejador é propriedade fixa: 2010 assume que sim (A6); Vallati, Chrpa & Kitchin (2014) mostram o contrário, já que a codificação do domínio desloca o desempenho do mesmo planejador [@vallati2014asap]. [HIPÓTESE] Não há, nas notas, disputa explícita sobre substituir *features* tabulares por representações aprendidas em grafo/hipergrafo — as obras recentes simplesmente adotam a segunda, possível lacuna de leitura, não ausência de disputa na literatura.

## 6. Lacunas

[FATO] A busca dirigida (`literatura/protocolo/busca/lacunas-memo.md`, lacuna L1) não encontrou, em quatro bases e sete *strings*, nenhum trabalho aplicando métricas de diagramas UML de classe/estado — o recorte do itSIMPLE em 2010 — a modelos de domínio de planejamento. Os itens mais próximos tratam de configuração estrutural de PDDL e de uma métrica ad hoc de complexidade, não de métricas UML/OO estabelecidas. [HIPÓTESE] O memorando registra que isso é ausência de evidência nas bases consultadas, não prova de inexistência. Cautela análoga vale para a lacuna L3 (*probing features*): a busca concluiu que a lacuna apontada por triadores anteriores era ilusória, pois a obra semente do eixo, Fawcett et al. (2014), já usa *features* de sondagem [@fawcett2014improved] — achado já incorporado na seção 2. [FATO] Há também lacuna de leitura, não de literatura: as notas de Roberts & Howe (2009), Muñoz et al. (2017/2018) e Percassi et al. (2021) vêm apenas de resumo, por bloqueio de acesso ao texto integral [@roberts2009learning; @munoz2017instance; @percassi2021improving]. Nenhuma detalha, em texto integral, as *features* de entrada de seus modelos — informação central para Q2, pendente de nova leitura.

## 7. Insumos para as próximas fases

[HIPÓTESE] Um experimento de Fase 3 para Q2 poderia: (a) reconstruir, para os domínios de 2010, tanto as métricas UML do itSIMPLE quanto *features* modernas replicáveis — sintáticas e estruturais de grafo causal/DTG, extraíveis com o tradutor do Fast Downward [@helmert2009concise]; (b) treinar modelos de cobertura (comparável a 2010) e, se possível, de custo de plano (F5), com e sem as métricas UML, medindo ganho marginal por seleção progressiva de *features* [@hutter2014algorithm; @fawcett2014improved]; (c) reportar separadamente discriminação entre domínios e dentro de domínio, seguindo De la Rosa et al. (2017), para não confundir um resultado agregado com validação real da UML [@delarosa2017performance]. [HIPÓTESE] Também é preciso decidir se remodela os domínios manualmente (repetindo a subjetividade de F3) ou extrai proxies estruturais automáticos do PDDL — convertendo a pergunta em uma sobre grafo causal/DTG. Nenhuma nota encontrou aplicação de UML a planejamento, então o experimento seria original, mas exige poder estatístico maior que o de 2010 (mais domínios e planejadores, respondendo também a Q1), para que ausência de ganho não seja confundida com amostra insuficiente [@delarosa2017performance].

## 8. Obras usadas

- @delarosa2017performance
- @domshlak2013complexity
- @fawcett2014improved
- @ferber2019ipc
- @helmert2009concise
- @hoffmann2011analyzing
- @leytonbrown2009empirical
- @hutter2014algorithm
- @odense2022neural
- @percassi2021improving
- @munoz2017instance
- @roberts2009learning
- @shen2020learning
- @vallati2014asap
- @vallati2015identifying
