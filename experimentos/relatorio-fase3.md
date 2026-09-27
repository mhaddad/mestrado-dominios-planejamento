# Relatório da Fase 3 — replicação experimental e respostas a Q1 e Q2

> **Rascunho de IA; respostas a Q1 e Q2 validadas pelo autor em 27/09/2026.** Claude Code (claude-opus-5-5), 27/09/2026. Cada número vem de um registro de experimento (EXP-nn, em `experimentos/execucoes/`) e do script nele indicado. O texto da dissertação é do autor; este relatório é material de trabalho.

## 1. As perguntas

- **Q1.** As conclusões de 2010 se sustentam com mais planejadores, mais domínios e método estatístico adequado?
- **Q2.** Métricas estruturais de modelagem, no estilo orientado a objetos, acrescentam poder preditivo às *features* modernas extraídas de PDDL?

A conclusão central de 2010 é que as características dos domínios, medidas por métricas do modelo UML, indicam qual técnica de planejamento (e, por ela, qual planejador) terá melhor desempenho num domínio novo. A validação de 2010 é a taxa de acerto do ranking previsto em Storage, Zeno-travel e Elevator.

## 2. O caminho, em quatro níveis

| Nível | O que foi feito | Registros |
|---|---|---|
| 1. Reprodução | O método de 2010 recalculado por script a partir das tabelas publicadas | EXP-03 |
| 2. Correções | Os mesmos dados, com erros corrigidos e decisões de método alternativas | EXP-04, EXP-06, EXP-08, EXP-09, EXP-10 |
| 3. Reexecução | Os 10 planejadores de 2010 nos 10 domínios de treino, sob condição única | EXP-01, EXP-02, EXP-05, EXP-19, EXP-20 |
| 4. Ampliação | 41 domínios e 29 planejadores, com resultados publicados das IPCs; métricas de 2010 extraídas do PDDL e *features* SAS+ | EXP-07, EXP-11, EXP-12, EXP-13 |

## 3. Resposta a Q1: a conclusão de 2010 não se sustenta como método de seleção

**O método é reproduzível, mas não foi feito como o texto descreve.** `[FATO]` (EXP-03) A partir das tabelas publicadas, o script reproduz 220 de 221 classes, 100 de 100 notas e 535 de 539 células característica × técnica. Mas a discretização aplicada foi por extremos (o menor valor é Baixo, o maior é Alto, o resto é Médio), não a descrita no texto, e o mesmo método usou duas taxonomias (G23, G24).

**A validação de 2010 não mostra ganho sobre uma linha de base sem características.** `[FATO]` (EXP-09)
- Só o Storage discrimina: no Zeno-travel e no Elevator, metade ou mais dos planejadores tem a nota máxima, e qualquer escolha razoável acerta.
- No Storage, o método indica o Fast Downward (perda 3); a média simples das notas de treino, sem nenhuma característica, indica o YAHSP (perda 1).
- A taxa de acerto por posição exata, usada em 2010, é instável: muda em direções opostas entre domínios com qualquer correção (EXP-04, EXP-19).

**As correções não mudam esse quadro.** `[FATO]`
- Discretização pela regra do texto: elimina a distinção em 7 ou 8 das 17 métricas, e o efeito na validação é instável (EXP-04).
- Correções de contagem (G17) e classes auxiliares: mudam classes, nenhum ranking (EXP-08).
- Taxonomia em 4 dimensões, sustentada pelas fontes primárias: o ranking muda, mas sem ganho consistente sobre a linha de base (EXP-06).
- Com mais domínios, a classe Alto/Médio/Baixo de um domínio depende de quais outros estão na amostra (EXP-10).

**Os dados de 2010 se reproduzem; a mistura de fontes pesava.** `[FATO]` (EXP-05, EXP-19)
- Reexecutados sob condição única, 50 de 63 pares planejador × domínio com contagem própria de 2010 resolvem exatamente o mesmo número de problemas.
- Das notas herdadas de competições, 18 de 38 mudam, algumas de 5 a 10 pontos. Das de execução própria, só 5 de 62.
- Com as notas homogêneas, o método escolhe no 1.º lugar planejadores de mesma qualidade (perda 3 / 0 / 0) e a correlação de postos sobe no Elevator (0,61 → 0,84). A conclusão de 2010 não dependia da mistura, nem num sentido nem no outro.

**Numa amostra maior, o método perde para a escolha fixa do melhor planejador.** `[FATO]` (EXP-12, EXP-13)
- 41 domínios e 1.230 instâncias; o melhor planejador único (Levitron, IPC 2023) resolve 953, e o oráculo 1.096.
- O método de 2010 com as métricas do PDDL perde 160 instâncias contra 143 do melhor planejador único (p = 0,13). Nenhum seletor testado (kNN, *random forest*) supera o melhor planejador único.
- Agrupar por técnica piora: o método por técnica perde de 170 a 387.

**O fenômeno que motivou 2010 existe, mas as características não o antecipam.** `[FATO]` Planejadores antigos ainda são os melhores em alguns domínios: o System R em 8 dos 41 e o FF em 5, contando empates (EXP-12); o System R tem cobertura total no Blocks World e no TPP (EXP-13). `[HIPÓTESE]` Há ajuste entre técnica e domínio em poucos domínios, e a implementação e a época do planejador pesam mais que a família de técnica.

**Resposta a Q1** (validada pelo autor em 27/09/2026): a pergunta de 2010 (que técnica funciona em que tipo de domínio) continua pertinente, mas a conclusão de que as métricas de modelagem permitem escolher o planejador não se sustenta. O resultado de 2010 é reproduzível, mas equivale ao de uma linha de base sem características na amostra de 2010 e fica abaixo da escolha fixa do melhor planejador numa amostra quatro vezes maior. Com 3 domínios de validação, e só 1 discriminante, a validação de 2010 não tinha poder para mostrar o contrário.

## 4. Resposta a Q2: as métricas UML não acrescentam poder preditivo, mas as *features* modernas também não

**Parte das métricas de 2010 mede o modelo, não o domínio.** `[FATO]` (EXP-07, EXP-08)
- 11 das 17 métricas têm correspondente no PDDL. As da hierarquia de tipos e das ações se reproduzem (correlação de postos de 0,69 a 0,92); atributos, associações e atores, não (0,31 a 0,51).
- A Agregação foi contada visualmente, sem regra escrita, e não é reproduzível.
- A característica que 2010 apontou como a de maior impacto tem o nome invertido (G1): é "Número Médio de Atores por Caso de Uso".

**As métricas UML não se relacionam com a estrutura SAS+.** `[FATO]` (EXP-11) Nenhuma das métricas de 2010 se correlaciona com as 17 *features* SAS+ acima do acaso (p entre 0,21 e 0,95), em 13 domínios. Não são redundantes; também não há sinal de que meçam a estrutura que a literatura liga à dificuldade [@hoffmann2011analyzing].

**Como preditores, nenhum conjunto supera a escolha fixa.** `[FATO]` (EXP-12) Com *random forest*, por domínio: métricas do PDDL perdem 151 instâncias, *features* SAS+ perdem 189 (significativamente pior que o melhor planejador único, p = 0,011) e as duas juntas perdem 148, contra 143 do melhor planejador único.

**Resposta a Q2** (validada pelo autor em 27/09/2026): nesta amostra, as métricas estruturais de 2010 não acrescentam poder preditivo às *features* SAS+, e estas não acrescentam às métricas de 2010; nenhum conjunto ajuda a escolher o planejador por domínio. Com planejadores recentes, vários deles portfólios, o melhor planejador único já resolve 87% do que o oráculo resolve, e o espaço para a seleção por domínio encolheu, em linha com [@cenamor2016ibacop]. A permanência de planejadores antigos como melhores em alguns domínios é o mesmo fenômeno descrito em [@lequen2026planner].

## 5. Achados novos sobre o material de 2010 (Fase 3)

| Achado | Resumo |
|---|---|
| G22 | O Blackbox rodou sem limite de tempo no Depots e no DriverLog; o DriverLog seria 11 de 20, não 12 |
| G23 | Discretização aplicada por extremos, não pela variância descrita |
| G24 | Duas taxonomias no mesmo método (IPP dentro e fora de *Forward-chaining*) |
| G25 | O Satellite de 2010 rodou com outro arquivo de domínio (hoje em `antigo/`) e com `-M 8192` no Blackbox |
| G26 | No TPP e no Pathways, 2010 usou versões instanciadas (`Strips/`); o binário `ff2` do TPP não está no acervo |

## 6. Medidas que 2010 não tinha

- **Qualidade dos planos** (EXP-20): cobertura e qualidade não andam juntas. IPP e Blackbox fazem os planos mais curtos quando resolvem; o R resolve 133 de 255 problemas com os planos mais longos (100 ações no DriverLog pfile1, contra 7 a 8). SATPlan e MAXPLAN incluem ações inúteis. A nota de 2010, só por cobertura, esconde isso.
- **Tempo por execução e memória máxima** estão em `experimentos/execucoes/nivel3-2010-gcp.csv` e não foram analisados.

## 7. Limites

- **Amostra de validação de 2010:** 3 domínios, 1 discriminante. Nenhum resultado dos Níveis 1 a 3 tem poder estatístico para distinguir o método da linha de base; as diferenças estão dentro do acaso.
- **Validação não reexecutada:** o ranking real de Storage, Zeno-travel e Elevator é o de 2010 (decisão do autor, 27/09/2026).
- **Nível 4 só por domínio e só cobertura:** a seleção por instância, onde a literatura mostra ganhos, não foi testada.
- **Versões dos binários:** parte das notas do Nível 3 mede limitações das versões de 2010 (ex.: o Blackbox declara insolúveis todos os problemas do Logistics e do Depots) `[HIPÓTESE]`.
- **Satellite** (G25) e **R no Pathways** (G26) ficam fora da comparação célula a célula com 2010.

## 8. O que isto muda na dissertação

Proposta, para decisão do autor:

1. A contribuição de 2010 passa a ser a **pergunta** e o **mapa** de desempenho por técnica e domínio, não o método de seleção.
2. A validação de 2010 é reapresentada com a linha de base sem características ao lado e com a perda em relação ao melhor planejador, não com a taxa de acerto por posição.
3. As métricas UML são discutidas como medidas do modelo, com as 6 que não existem sem o UML.P e as 3 dependentes de escolha de modelagem destacadas.
4. Os achados G22 a G26 entram na seção de método como limitações do experimento original.

## 9. Pendências da Fase 3

- Relatório por instância (R-29): passa para a Fase 4B, que levanta os resultados por execução das IPCs.
