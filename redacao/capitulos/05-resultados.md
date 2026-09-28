---
titulo: "Resultados experimentais"
status: revisado-por-ia
data: 2026-09-28
fonte: experimentos/relatorio-fase3.md; experimentos/relatorio-fase4b.md; registros EXP-03 a EXP-25
---

# Resultados experimentais

Este capítulo apresenta os resultados que respondem a três perguntas. Q1 examina se características do domínio ou da instância permitem escolher um planejador melhor que uma referência fixa. Q2 compara as métricas de modelagem de 2010 com características extraídas automaticamente do PDDL. Q5 investiga se essas características explicam o desempenho relativo de famílias de técnicas nas IPCs posteriores. A sequência acompanha as camadas do método: reprodução, correções, reexecução homogênea, ampliação por domínio e análise por instância.

Três distinções orientam a leitura. Primeiro, **reproduzir** as tabelas de 2010 não equivale a validar sua recomendação. Segundo, **prever se uma família resolve uma instância** não equivale a escolher o melhor planejador entre alternativas. Terceiro, um ganho numérico sem diferença estatisticamente demonstrada não deve ser apresentado como equivalência nem como superioridade. Por isso, cada análise informa a unidade, a referência e o alcance do resultado.

## Reprodução: o cálculo publicado e o método descrito

O EXP-03 refez o cálculo de 2010 a partir das tabelas publicadas. O *script* reproduziu 220 das 221 classes de características, as 100 notas de eficiência e 535 das 539 células da relação característica × técnica. <!-- fonte: EXP-03 --> O resultado demonstra que o conteúdo numérico é amplamente recuperável. Ele também revelou que a regra efetivamente aplicada não coincide integralmente com a descrição metodológica.

A discretização publicada usa os extremos da amostra: o menor valor recebe a classe Baixo, o maior recebe Alto e os demais ficam em Médio. O texto de 2010 descrevia uma regra baseada na variância. Além disso, duas atribuições de técnicas foram empregadas em etapas diferentes, com o IPP dentro e fora de *Forward-chaining*. <!-- fonte: EXP-03; achados G23 e G24 --> A reprodução confirma, portanto, a origem da maior parte das tabelas, mas impede tratar a sequência descrita no texto como especificação suficiente e única do cálculo.

Essa diferença é material porque a classe da característica é a entrada da recomendação. O resultado do Nível 1 desloca a primeira questão: antes de perguntar se o método prevê bem, é preciso verificar se sua vantagem continua quando se usa uma regra explícita, uma taxonomia apoiada em fontes e uma referência que não consulta as características.

## Correções e comparação com uma referência sem características

O Nível 2 alterou uma decisão por vez. Aplicar a discretização descrita no texto elimina a distinção entre Alto, Médio e Baixo em sete ou oito das 17 métricas e muda a taxa de acerto em direções diferentes nos três domínios de validação. <!-- fonte: EXP-04 --> Corrigir Pathways, TPP, o rótulo da métrica de atores por caso de uso e as classes auxiliares altera classes, mas não muda os *rankings* previstos. <!-- fonte: EXP-08 --> A taxonomia em quatro dimensões muda os *rankings*, sem produzir vantagem consistente sobre a escolha fixa. <!-- fonte: EXP-06 -->

A referência fixa ordena os planejadores pela nota média nos dez domínios de treino e usa o primeiro colocado para todo domínio novo. Ela não observa as características do domínio de validação. A perda é a diferença entre a nota do melhor planejador observado no domínio e a nota do planejador recomendado; uma perda menor é melhor. Em Storage, único dos três domínios em que a escolha discrimina claramente os planejadores, a referência fixa perde menos que o método original.

| Domínio de validação | Método de 2010 | Perda do método | Referência fixa | Perda da referência |
|---|---|---:|---|---:|
| Storage | Fast Downward | 3 | YAHSP | 1 |
| Zeno-travel | recomendação empatada | 0 | recomendação empatada | 0 |
| Elevator | recomendação empatada | 0 | recomendação empatada | 0 |

: Método de 2010 e referência fixa nos três domínios de validação

::: fonte
Fonte: Autor, a partir do EXP-09.
:::

Em Zeno-travel e Elevator, metade ou mais dos planejadores alcança a nota máxima. A coincidência exata de posições usada em 2010 depende de como esses empates são ordenados. <!-- fonte: EXP-09 --> A taxa de acerto de posições, portanto, não demonstra que as características acrescentem informação à escolha. Quando a discretização é recalculada com mais 18 domínios das IPCs de 1998 a 2008, a classe Alto, Médio ou Baixo de um domínio muda conforme a composição da amostra. <!-- fonte: EXP-10 --> O problema não se reduz às duas contagens corrigidas: a própria representação categórica é instável.

## Reexecução homogênea dos planejadores de 2010

O Nível 3 substituiu a mistura de resultados de competições e execuções próprias por uma rodada comum nos dez domínios de treino. Foram realizadas 3.390 execuções; 2.263 produziram plano, 734 atingiram o limite e 393 terminaram sem plano. <!-- fonte: EXP-05 --> Essa camada permite comparar a cobertura obtida no novo ambiente com as contagens recuperáveis do acervo e, separadamente, verificar como as novas notas afetam o método.

### Reprodução das contagens e mudança das notas

Há dois denominadores distintos. No EXP-05, 63 pares planejador × domínio possuem contagem própria de 2010 comparável: 50 resolvem exatamente o mesmo número de problemas, 9 resolvem mais e 4 resolvem menos. As diferenças são de um ou dois problemas, exceto o Satellite, cujo arquivo de domínio difere do usado em 2010. <!-- fonte: EXP-05 --> Esse resultado mede reprodução de **contagens de problemas resolvidos**.

O EXP-19 compara as **100 notas de treino** e preserva, para análise histórica, os rótulos publicados de origem: 38 de competição e 62 de execução própria. Mudam 18 das 38 notas rotuladas como competição e 5 das 62 rotuladas como execução própria; a diferença média é, respectivamente, 1,58 e 0,16 ponto. <!-- fonte: EXP-19 --> A auditoria demonstrou que quatro dos 38 valores rotulados como competição também vieram de execução própria, de modo que a origem factual é 34/66. Essa correção de proveniência não altera o cálculo do EXP-19, mas impede interpretar os dois grupos publicados como populações perfeitamente separadas.

Com as notas homogêneas, a perda do método nos três domínios de validação continua 3, 0 e 0. A correlação de Spearman no Elevator sobe de 0,61 para 0,84, mas dois domínios permanecem dominados por empates e a validação continua sem poder para demonstrar vantagem sobre a referência fixa. <!-- fonte: EXP-19 --> A mistura das fontes afetava as notas, sobretudo as herdadas de competições, mas não explica a conclusão original numa direção única.

### Cobertura, qualidade, tempo e memória

O resultado depende da medida adotada. A cobertura informa quantos problemas foram resolvidos; o comprimento do plano distingue a qualidade dos planos produzidos; o tempo mostra o custo para encontrá-los; a memória separa parte das falhas de busca das limitações dos binários antigos.

| Dimensão | Resultado observado | Consequência para a leitura |
|---|---|---|
| Cobertura | 2.263 planos em 3.390 execuções | Sustenta a comparação principal com 2010 |
| Qualidade | IPP e Blackbox produzem planos curtos quando resolvem; o System R resolve 133 de 255 problemas, mas tem planos muito longos em alguns casos | Maior cobertura não garante melhor plano |
| Tempo | Tempo e cobertura têm Spearman de 0,78 a 1,00 em 9 dos 10 domínios; Mystery tem 0,57 | Acrescentar tempo muda menos a ordem que acrescentar qualidade |
| Memória | 36 dos 393 casos sem plano decorrem do teto de memória dos binários de 32 bits | Parte das falhas não deve ser atribuída apenas à estratégia de busca |

: Medidas complementares da reexecução homogênea

::: fonte
Fonte: Autor, a partir dos EXP-05, EXP-20 e EXP-22.
:::

SATPlan e MAXPLAN incluem ações inúteis em parte dos planos; o System R chega a 100 ações no DriverLog pfile1, contra 7 ou 8 de outros planejadores. <!-- fonte: EXP-20 --> Esses casos tornam concreta uma limitação da eficiência de 2010: reduzir o resultado à porcentagem resolvida esconde diferenças que importam para o uso do plano. A conclusão sobre seleção continua baseada em cobertura para preservar comparabilidade, mas não deve ser lida como avaliação completa de desempenho.

## Ampliação por domínio: 41 domínios e 29 planejadores

O Nível 4 usa 29 planejadores, 41 domínios e 1.230 instâncias da coleção Autoscale. O *single best solver* (SBS), Levitron, resolve 953 instâncias; o *virtual best solver* (VBS), que escolhe retrospectivamente o melhor planejador em cada domínio, resolve 1.096. A lacuna máxima disponível para a seleção por domínio é, portanto, 143 instâncias. <!-- fonte: EXP-12 --> A existência dessa lacuna demonstra complementaridade, mas não que as características testadas consigam antecipá-la.

A tabela seguinte preserva a unidade de cada comparação. A perda total é medida em instâncias que o seletor deixa de resolver em relação ao VBS. O teste de Wilcoxon é pareado por domínio contra o SBS. O p ajustado usa Holm nas sete comparações do EXP-12; valores maiores de perda indicam resultado descritivamente pior, enquanto o teste informa se essa diferença foi demonstrada na amostra.

| Seletor e características | Perda total | p bruto × SBS | p ajustado (Holm) |
|---|---:|---:|---:|
| SBS — Levitron | 143 | — | — |
| Método de 2010 — métricas do PDDL | 160 | 0,1261 | 0,3784 |
| kNN — métricas do PDDL | 228 | 0,0595 | 0,2467 |
| kNN — SAS+ | 231 | 0,0089 | 0,0621 |
| kNN — PDDL + SAS+ | 220 | 0,0493 | 0,2467 |
| *Random forest* — métricas do PDDL | 151 | 0,5277 | 1,0000 |
| *Random forest* — SAS+ | 189 | 0,0113 | 0,0679 |
| *Random forest* — PDDL + SAS+ | 148 | 0,5702 | 1,0000 |

: Seletores por domínio comparados com o melhor planejador único

::: fonte
Fonte: Autor, a partir do EXP-12 e de `experimentos/analise/correcao-multipla/holm.csv`.
:::

Nenhum seletor apresenta perda menor que o SBS, e nenhuma diferença permanece significativa nessa família de sete testes. A combinação PDDL + SAS+ reduz numericamente a perda do *random forest* de 151 ou 189 para 148, mas continua acima das 143 instâncias do SBS. Os testes realizados comparam cada seletor com o SBS; eles não demonstram equivalência entre os conjuntos de características nem ausência de informação complementar entre eles.

As versões do método por técnica foram avaliadas numa família mais ampla de 16 comparações. Usar todas as dimensões produz perda 170; usar somente D1, 387; usar somente D2, 277. As versões D1 e D2 são significativamente piores que o SBS após Holm, com p ajustado de 0,0001 e 0,0219. <!-- fonte: EXP-13; experimentos/analise/correcao-multipla/holm.csv --> A taxonomia melhora a descrição dos planejadores, mas agregar desempenho por seus valores não produz, nesse desenho, uma regra melhor de escolha.

O resultado global não elimina a heterogeneidade. O System R empata com o melhor em oito dos 41 domínios, e o FF, em cinco; o System R alcança cobertura total em Blocks World e TPP. <!-- fonte: EXP-12; EXP-13 --> A questão que motivou 2010 continua visível: planejadores antigos ainda vencem em regiões específicas. O que falha é transformar as medidas disponíveis numa previsão superior à escolha fixa.

## Métricas de modelagem e características SAS+

Das 17 métricas UML.P de 2010, 11 possuem uma aproximação operacional no PDDL. Contagens ligadas à hierarquia de tipos e às ações apresentam correlações de postos de 0,69 a 0,92 com as contagens UML; atributos, associações e atores ficam entre 0,31 e 0,51. Agregação foi contada visualmente em 2010, sem regra operacional registrada. <!-- fonte: EXP-07; EXP-08 --> As aproximações extraídas do PDDL não devem, por isso, ser tratadas como reprodução integral do instrumento UML original.

Nos 13 domínios originais, nenhuma correlação entre as métricas de 2010 e as 16 características SAS+ superou o esperado ao acaso; os valores de p ficam entre 0,21 e 0,95. <!-- fonte: EXP-11 --> Com apenas 13 unidades agregadas, isso não demonstra independência entre as famílias. Demonstra apenas que a amostra não sustenta uma relação entre elas.

Na ampliação, nenhum seletor construído com as aproximações do PDDL, com SAS+ ou com a combinação supera o SBS, como mostra a tabela anterior. A resposta a Q2 precisa permanecer nesse alcance: **não foi demonstrado ganho de seleção sobre a referência fixa**. A melhora numérica da combinação no *random forest* impede concluir, somente a partir desses testes, que um conjunto não acrescente qualquer informação ao outro. As métricas UML completas existem apenas nos 13 domínios originais, amostra insuficiente para repetir a avaliação preditiva do Nível 4.

## IPCs de 2011 e 2018: da diferença entre famílias à possibilidade de escolha

A Fase 4B desloca a unidade para a instância. Em 2011, foram recuperados 560 problemas e 5.679 planos válidos do WebPlan preservado no Software Heritage; em 2018, foram usadas 17.640 execuções publicadas. Os conjuntos foram validados contra os placares oficiais. <!-- fonte: data/ipc-2011-2023/README.md; EXP-21; EXP-24 --> As análises permanecem separadas por edição, trilha e recorte com ou sem portfólios.

A resposta a Q5 tem três degraus. O primeiro descreve **onde as famílias diferem**. O segundo avalia se características predizem **a resolução por uma família** fora do domínio observado. O terceiro testa se essa informação permite **escolher um planejador** melhor que o SBS. Só o terceiro degrau demonstra utilidade decisória.

### Onde as famílias diferem

Na *satisficing* e na *agile* de 2011 e 2018, algum planejador de busca progressiva empata com o melhor em todos os domínios. Na trilha ótima, a busca simbólica supera a progressiva em quatro dos 14 domínios de 2011 e em três dos 12 de 2018; o CPT4 também se destaca no parcprinter de 2011. <!-- fonte: EXP-21 --> A diferença entre famílias existe, mas está concentrada por trilha e domínio.

### Previsão de resolução por família

Para cada família, uma regressão logística e uma árvore rasa predizem se algum planejador da família resolve a instância. A validação deixa um domínio inteiro fora. A AUC mede ordenação entre casos resolvidos e não resolvidos; não é porcentagem de problemas resolvidos e não compara diretamente duas famílias concorrentes.

| Recorte | Famílias modeladas | AUC mediana: logística | AUC mediana: árvore | AUC mediana: só tamanho | Modelos com Holm < 0,05 |
|---|---:|---:|---:|---:|---:|
| Todos os planejadores | 40 | 0,59 | 0,49 | 0,58 | 6 |
| Sem portfólios | 35 | 0,57 | 0,43 | 0,52 | 7 |

: Predição de resolução por família com características SAS+

::: fonte
Fonte: Autor, a partir do EXP-21.
:::

Outras dez famílias por recorte ficaram sem modelo por falta de variação: resolviam quase tudo ou quase nada entre as instâncias elegíveis. <!-- fonte: EXP-21 --> Entre os modelos significativos, várias famílias têm somente um a três planejadores; nesses casos, técnica e implementação não podem ser separadas. O caso mais claro de família ampla, *landmarks* na ótima de 2018 sem portfólios, alcança AUC 0,77 contra 0,52 usando só tamanho, mas o sinal não se mantém com portfólios nem na árvore rasa. <!-- fonte: EXP-21 -->

As seis propriedades de topologia acrescentam sinal em parte das famílias. A análise usa somente tarefas com ambos os conjuntos de características, razão pela qual o número de modelos é menor que no EXP-21.

| Recorte | Modelos | Só tamanho | SAS+ | Só topologia | SAS+ + topologia | Acréscimo com Holm < 0,05 | Combinação abaixo de SAS+ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Todos os planejadores | 39 | 0,56 | 0,58 | 0,52 | 0,61 | 14 | 20 |
| Sem portfólios | 34 | 0,51 | 0,56 | 0,52 | 0,62 | 15 | 15 |

: Acréscimo das propriedades de topologia à previsão por família

::: fonte
Fonte: Autor, a partir do EXP-25.
:::

Na ótima de 2011, busca progressiva sobe de 0,63 para 0,75 e *landmarks*, de 0,68 para 0,80. Na *satisficing* de 2018, largura/novidade sobe de 0,52 para 0,62. <!-- fonte: EXP-25 --> Em 20 dos 39 modelos com todos os planejadores, porém, acrescentar topologia reduz a AUC fora do domínio. A decomposição realizada depois da análise principal sugere duas fontes: hFF no estado inicial em 2011 e amostragem de becos sem saída e sondagem em 2018. Essa decomposição é exploratória e não recebeu nova correção por comparações múltiplas. <!-- fonte: EXP-25 -->

O resultado é mais forte como descrição do **tipo de informação** do que como política pronta. hFF e as amostragens executam uma heurística sobre a tarefa; aproximam-se de uma exploração curta, e não apenas de uma leitura estática do PDDL. Ainda assim, a melhoria é desigual entre famílias e recortes.

### Seleção por instância

O R-29 testa a etapa decisória. Entram instâncias que possuem características e que algum planejador do recorte resolve. Em cada partição, o seletor é treinado nos outros domínios; o SBS também é escolhido no treino, podendo variar entre partições. A perda conta instâncias resolvidas pelo VBS e perdidas pela escolha.

| Edição e trilha, todos os planejadores | Instâncias | SBS | Método 2010 | Método 4D | kNN | *Random forest* |
|---|---:|---:|---:|---:|---:|---:|
| 2011 ótima | 203 | 18 | 18 | 34 | 45 | 23 |
| 2011 *satisficing* | 267 | 17 | 17 | 35 | 82 | 50 |
| 2018 ótima | 174 | 36 | 50 | 46 | 43 | 62 |
| 2018 *satisficing* | 188 | 52 | 49 | 35 | 53 | 51 |
| 2018 *agile* | 170 | 40 | 42 | 40 | 54 | 62 |

: Perda por instância dos seletores com características SAS+

::: fonte
Fonte: Autor, a partir do EXP-24. As colunas 4D, kNN e *random forest* mostram a configuração principal de cada família no registro.
:::

Há ganhos numéricos em alguns recortes, como 35 contra 52 na *satisficing* de 2018, mas nenhum seletor demonstrou ganho significativo sobre o SBS quando todos os planejadores estão disponíveis. <!-- fonte: EXP-24 --> Acrescentar topologia também não produz vantagem significativa de seleção em nenhuma unidade. <!-- fonte: EXP-25 --> Uma característica pode, portanto, ajudar a ordenar a probabilidade de resolução de uma família sem ser suficiente para escolher um planejador melhor que a referência fixa.

Sem portfólios, na *agile* de 2018, o método 4D perde 53 instâncias contra 91 do LAMA-2011 e fecha 42% da lacuna para o VBS. O p ajustado é 0,047 dentro daquela unidade e 0,43 quando se corrigem as 60 comparações do experimento. <!-- fonte: EXP-24 --> O kNN perde 51 instâncias no mesmo recorte, sem diferença significativa após Holm. O caso fornece uma hipótese localizada: a seleção pode ter mais espaço quando a melhor opção fixa é fraca. Ele não demonstra uma regra geral.

## Respostas às perguntas de pesquisa

**Q1 — Replicação e seleção.** O fenômeno que motivou 2010 permanece: planejadores, domínios e instâncias apresentam desempenho heterogêneo. A conclusão de que as métricas de modelagem permitem escolher o planejador não se sustenta. A validação original não supera uma referência sem características; na ampliação por domínio, todos os seletores têm perda igual ou maior que o SBS; por instância, há ganhos numéricos localizados, mas nenhum ganho significativo no recorte completo. <!-- fonte: EXP-09; EXP-12; EXP-13; EXP-24; EXP-25 -->

**Q2 — Características de modelagem e SAS+.** As aproximações das métricas de 2010 extraídas do PDDL reproduzem somente parte do instrumento UML. Nenhum seletor baseado nelas, nas características SAS+ ou na combinação demonstrou superar o SBS. A combinação apresenta melhora numérica no *random forest*, mas os testes realizados não estabelecem ganho incremental robusto nem equivalência entre as famílias. <!-- fonte: EXP-07; EXP-11; EXP-12 -->

**Q5 — Características e famílias nas IPCs posteriores.** Há diferenças localizadas entre famílias. SAS+ antecipa a resolução de algumas delas fora do domínio, e a topologia acrescenta sinal em parte dos casos, sobretudo por medidas próximas de sondagem heurística. O sinal é desigual, frequentemente piora fora da amostra e não se converte em ganho significativo de seleção. <!-- fonte: EXP-21; EXP-24; EXP-25 -->

Os resultados substituem uma regra de recomendação por requisitos de avaliação: preservar o grupo de domínio fora do treinamento, comparar com uma referência fixa forte, separar técnica de implementação, informar o universo elegível e corrigir comparações múltiplas. O capítulo seguinte aplica a mesma distinção entre heterogeneidade observada e capacidade de escolha aos modelos de linguagem.
