---
titulo: "Resultados experimentais"
status: rascunho-de-ia
data: 2026-09-28
fonte: experimentos/relatorio-fase3.md; experimentos/relatorio-fase4b.md; registros EXP-03 a EXP-25
---

# Resultados experimentais

Este capítulo apresenta os resultados das quatro camadas de revisão do experimento de 2010 e da ampliação com dados das Competições Internacionais de Planejamento (IPCs) de 2011 e 2018. A organização acompanha as perguntas de pesquisa: Q1 trata da possibilidade de selecionar planejadores a partir de características do domínio; Q2, da contribuição das métricas de modelagem em comparação com *features* extraídas do PDDL; e Q5, da relação entre características estruturais e famílias de técnica nas IPCs posteriores. O método e as limitações de cada análise foram descritos no capítulo 4.

## Reprodução do método de 2010

O primeiro resultado é que as tabelas publicadas permitem reproduzir substancialmente o cálculo de 2010. O *script* do EXP-03 reproduziu 220 das 221 classes de características, as 100 notas de eficiência e 535 das 539 células da relação característica × técnica. <!-- fonte: EXP-03 --> A reprodução, contudo, revelou uma diferença decisiva entre o procedimento aplicado e sua descrição: a discretização que gera as tabelas usa os valores extremos da amostra — mínimo como Baixo, máximo como Alto e os demais como Médio —, e não a regra baseada em variância declarada no texto.

Essa diferença importa porque a classificação de uma característica é o primeiro passo da recomendação. Ela também mostra que o método não foi uma sequência inteiramente especificada e independente de interpretação: ao reconstruí-lo, foram identificadas duas taxonomias de técnicas aplicadas em partes distintas do cálculo. <!-- fonte: EXP-03; achados G23 e G24 --> A reprodução, portanto, confirma os números publicados, mas não confirma que eles resultem exatamente do método descrito.

## Correções e a linha de base sem características

As análises do Nível 2 testaram se as divergências encontradas explicariam a conclusão original. Não explicam. Aplicar a regra de discretização escrita no texto elimina a distinção entre Alto, Médio e Baixo em sete ou oito das 17 métricas, e altera os resultados de validação em sentidos diferentes nos três domínios de validação. <!-- fonte: EXP-04 --> A correção das contagens de Pathways e TPP, do rótulo da métrica de atores por caso de uso e da contagem de classes auxiliares altera classes, mas não altera os *rankings* previstos. <!-- fonte: EXP-08 --> A taxonomia em quatro dimensões muda os *rankings*, mas não produz ganho consistente diante de uma referência sem características. <!-- fonte: EXP-06 -->

A referência decisiva é o melhor planejador escolhido sem observar o domínio novo: aquele com maior nota média nos dez domínios de treino. A Tabela 1 contrasta essa linha de base com o método de 2010 nos três domínios usados como validação original. A perda é a diferença entre a nota do melhor planejador no domínio e a nota do planejador recomendado; por isso, menor valor é melhor.

| Domínio de validação | Método de 2010 | Perda do método | Linha de base | Perda da linha de base |
|---|---|---:|---|---:|
| Storage | Fast Downward | 3 | YAHSP | 1 |
| Zeno-travel | recomendação empatada | 0 | recomendação empatada | 0 |
| Elevator | recomendação empatada | 0 | recomendação empatada | 0 |

: Método de 2010 e linha de base nos domínios de validação

::: fonte
Fonte: Autor, a partir do EXP-09.
:::

Somente Storage diferencia as escolhas. Em Zeno-travel e Elevator, metade ou mais dos planejadores alcança a nota máxima; a coincidência de posições, medida usada em 2010, depende de um desempate arbitrário. <!-- fonte: EXP-09 --> Assim, a taxa de acerto de posições não fornece evidência de que as características acrescentem informação à escolha. Também não há base para atribuir essa limitação somente às duas contagens corrigidas ou à nova taxonomia: quando se acrescentam 18 domínios das IPCs de 1998 a 2008, a classe Alto, Médio ou Baixo de um domínio muda conforme a composição da amostra. <!-- fonte: EXP-10 -->

## Reexecução sob condição única

O Nível 3 retirou a mistura entre resultados de competição e execuções próprias que existe no conjunto de 2010. Entre os 63 pares planejador × domínio cuja contagem publicada provinha de execução própria, 50 resolvem exatamente o mesmo número de problemas na reexecução. Já 18 dos 38 pares herdados de competições mudam; algumas notas variam de cinco a dez pontos. <!-- fonte: EXP-05; EXP-19 --> Esse contraste mostra que o conjunto original combinava populações com condições de execução diferentes, ainda que a heterogeneidade não explique a conclusão de 2010 em uma direção única.

Com as notas homogêneas, o método de 2010 recomenda planejadores cuja perda nos três domínios de validação é, respectivamente, 3, 0 e 0. A correlação de postos no Elevator sobe de 0,61 para 0,84, mas a comparação continua incapaz de demonstrar ganho sobre a linha de base, pois dois domínios permanecem dominados por empates. <!-- fonte: EXP-19 --> A pergunta de 2010 não deixa de ser pertinente; o que não se sustenta é a inferência de que as 17 métricas permitam uma seleção superior.

O Nível 3 também evidencia que cobertura não esgota desempenho. IPP e Blackbox produziram os planos mais curtos quando resolvem os problemas, enquanto o System R, embora resolva 133 de 255 problemas, tem planos particularmente longos em alguns casos. SATPlan e MAXPLAN também produzem ações inúteis em parte dos planos. <!-- fonte: EXP-20 --> Tempo e cobertura, por sua vez, ordenam os planejadores de modo semelhante em nove dos dez domínios, com correlação de Spearman entre 0,78 e 1,00; Mystery é a exceção, com 0,57. <!-- fonte: EXP-22 --> A qualidade do plano altera mais a interpretação do que a omissão do tempo. Além disso, 36 dos 393 casos sem plano decorrem do teto de memória dos binários de 32 bits, e não necessariamente da busca. <!-- fonte: EXP-22 -->

## Ampliação para 41 domínios e 29 planejadores

O Nível 4 testa a escolha em uma amostra maior e sob condições de execução uniformes: 29 planejadores, 41 domínios e 1.230 instâncias da coleção Autoscale. O melhor planejador único, Levitron, resolve 953 instâncias; o *virtual best*, que escolhe retrospectivamente o melhor planejador para cada domínio, resolve 1.096. <!-- fonte: EXP-12 --> A distância entre esses números mostra que há complementaridade potencial, mas ela não implica que as características disponíveis consigam aproveitá-la.

| Estratégia | Perda em relação ao melhor por domínio | Situação estatística |
|---|---:|---|
| Melhor planejador único | 143 | referência |
| Método de 2010 com métricas extraídas do PDDL | 160 | p = 0,13 contra a referência |
| *Random forest* com métricas do PDDL | 151 | não significativo após Holm |
| *Random forest* com *features* SAS+ | 189 | p = 0,068 após Holm |
| *Random forest* com os dois conjuntos | 148 | não significativo após Holm |
| Método por técnica | 170 a 387 | pior que a referência em parte dos recortes |

: Seletores por domínio na ampliação do Nível 4

::: fonte
Fonte: Autor, a partir dos EXP-12 e EXP-13. Os valores de *random forest* são perdas em instâncias; a correção de Holm considera as sete comparações do EXP-12.
:::

Nenhum seletor supera o melhor planejador único. As diferenças do EXP-12 que parecem relevantes antes da correção para comparações múltiplas não permanecem significativas depois dela; o agrupamento por técnica continua pior em parte dos recortes. <!-- fonte: EXP-12; EXP-13; experimentos/analise/correcao_multipla.py --> Isso não significa que todos os planejadores se comportem de modo idêntico. O System R é o melhor, contando empates, em oito dos 41 domínios; o FF, em cinco. O System R alcança cobertura total em Blocks World e TPP. <!-- fonte: EXP-12; EXP-13 --> Há, portanto, heterogeneidade de desempenho, mas as medidas testadas não a transformam em recomendação preditiva confiável.

## Métricas de modelagem e *features* modernas

Das 17 métricas UML de 2010, apenas 11 têm correspondente especificável no PDDL. As contagens relacionadas à hierarquia de tipos e às ações têm correlações de postos entre 0,69 e 0,92 com as contagens UML; atributos, associações e atores ficam entre 0,31 e 0,51. A agregação foi contada visualmente em 2010, sem regra operacional registrada. <!-- fonte: EXP-07; EXP-08 --> Parte do que o experimento original denomina característica de domínio mede, portanto, decisões de modelagem UML e não uma propriedade reproduzível da tarefa em PDDL.

Também não há evidência de que as métricas UML e as 16 *features* SAS+ descrevam a mesma estrutura: nas 13 tarefas originais, as correlações não excedem o que seria esperado ao acaso, com valores de p entre 0,21 e 0,95. <!-- fonte: EXP-11 --> A amostra é pequena demais para estabelecer que as famílias sejam independentes; ela apenas não sustenta uma relação entre elas. Na ampliação do Nível 4, combiná-las tampouco supera a referência fixa, como mostra a Tabela 2.

Em consequência, a resposta a Q2 é negativa e limitada ao conjunto analisado: as métricas de 2010 que podem ser extraídas do PDDL não acrescentam poder preditivo às *features* SAS+, e as *features* SAS+ não acrescentam poder preditivo a elas para escolher um planejador por domínio. Esse resultado não transforma métricas de modelagem em medidas inúteis para outros propósitos; apenas não confirma sua utilidade como seletor nesse desenho.

## IPCs de 2011 e 2018: características e famílias de técnica

A Fase 4B desloca a unidade de análise do domínio para a instância. Foram usados 560 problemas e 5.679 planos válidos da IPC 2011, recuperados do WebPlan preservado no Software Heritage, e 17.640 execuções da IPC 2018. Os dois conjuntos foram validados contra os placares oficiais. <!-- fonte: data/ipc-2011-2023/README.md; EXP-21; EXP-24 --> As comparações permanecem separadas por edição e trilha, com e sem portfólios.

O mapa descritivo mostra que a busca progressiva empata com o melhor desempenho em todos os domínios das trilhas *satisficing* e *agile* de 2011 e 2018. Na trilha ótima, busca simbólica supera a progressiva em quatro dos 14 domínios de 2011 e em três dos 12 de 2018; o CPT4 também se destaca no parcprinter de 2011. <!-- fonte: EXP-21 --> Essa diferença entre famílias é localizada, e não uma regra transversal.

As 16 *features* SAS+ não antecipam, quando o domínio de teste fica fora do treinamento, qual família resolverá uma instância. A regressão logística tem AUC mediana de 0,59; o modelo que recebe apenas o tamanho da tarefa alcança 0,58; a árvore rasa, 0,49. Depois da correção de Holm, sobrevivem seis modelos por recorte, quase todos para famílias de um a três planejadores, situação em que não se separa efeito de técnica e efeito de implementação. <!-- fonte: EXP-21 -->

As propriedades de topologia de busca acrescentam um sinal modesto e desigual. Somadas às SAS+, elevam a AUC mediana entre 0,03 e 0,06 e passam na correção de Holm em cerca de um terço das famílias. Entre os resultados de maior amplitude estão busca progressiva, de 0,63 para 0,75, e *landmarks*, de 0,68 para 0,80, na trilha ótima de 2011; busca por largura e novidade sobe de 0,52 para 0,62 na *satisficing* de 2018. <!-- fonte: EXP-25 --> Em aproximadamente metade dos modelos, porém, adicionar topologia piora a previsão fora do domínio, e a topologia isolada fica abaixo das *features* SAS+.

O resultado é mais informativo sobre o tipo de sinal do que sobre um seletor pronto. Na ótima de 2011, o ganho vem sobretudo de hFF no estado inicial, que aproxima o comprimento do plano relaxado; na *satisficing* de 2018, vem de amostragens de becos sem saída e sucesso de sondagem. <!-- fonte: EXP-25 --> São medidas que executam parcialmente uma heurística sobre a tarefa, e não somente leituras estáticas do arquivo PDDL. Ainda assim, nenhuma característica explica de maneira robusta o desempenho relativo das famílias fora do domínio. Essa conclusão converge com a observação de que não havia propriedades de domínio independentes de planejador aceitas para classificar modelos estaticamente [@vallati2018what].

## Seleção por instância

A análise R-29 aplica, por instância, o método de 2010, sua versão com taxonomia em quatro dimensões, kNN e *random forest*, usando *features* SAS+, topologia e os dois conjuntos. Em todas as dez unidades de comparação — edição, trilha e recorte de portfólios — nenhum seletor supera o melhor planejador único quando todos os planejadores são incluídos. <!-- fonte: EXP-24; EXP-25 --> Nesses casos, a referência costuma ser um portfólio, como Delfi1, Saarplan, FDSS-1, ou o LAMA-2011.

Há um indício local, não uma conclusão geral. Sem portfólios, na trilha *agile* de 2018, o método de 2010 reescrito com a taxonomia em quatro dimensões fecha 42% da lacuna entre o LAMA-2011 e o *virtual best*. O valor de p corrigido por Holm é 0,047 dentro daquela unidade, mas 0,43 quando se consideram as 60 comparações. <!-- fonte: EXP-24 --> O resultado deve ser tratado como hipótese para investigação posterior, pois não resiste à família mais ampla de testes.

## Respostas às perguntas

**Q1.** A pergunta de 2010 permanece pertinente: o desempenho não é uniforme entre planejadores, domínios e instâncias. Contudo, a conclusão de que métricas de modelagem permitem escolher o planejador não se sustenta. A validação original não supera uma linha de base sem características, e os seletores testados ficam abaixo ou não diferem do melhor planejador único nas amostras ampliadas. <!-- fonte: EXP-09; EXP-12; EXP-13; EXP-24; EXP-25 -->

**Q2.** As métricas UML que podem ser extraídas do PDDL não melhoram a escolha quando combinadas às *features* SAS+; estas também não melhoram as métricas UML nesse problema de seleção. A conclusão é restrita às amostras, às medidas e à validação usadas, e não afirma que métricas de modelagem sejam irrelevantes para outros objetivos. <!-- fonte: EXP-07; EXP-11; EXP-12 -->

**Q5.** Nas IPCs de 2011 e 2018, características estruturais extraídas do PDDL não explicam de forma robusta o desempenho relativo de famílias de técnica fora do domínio. Sinais de sondagem heurística acrescentam informação em parte dos casos, mas são desiguais e insuficientes para uma política de seleção generalizável. <!-- fonte: EXP-21; EXP-25 -->

Esses resultados delimitam a contribuição da revisão. Eles preservam a pergunta sobre ajuste entre problema e técnica, mas substituem uma regra de recomendação por requisitos para qualquer proposta futura: comparação com uma referência fixa forte, validação fora do domínio, separação entre técnica e implementação e correção para múltiplas comparações. O capítulo seguinte aplica essa mesma cautela à discussão dos modelos de linguagem.
