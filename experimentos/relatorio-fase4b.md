# Relatório da Fase 4B — panorama das IPCs 2011–2018, resposta a Q5 e síntese para a Ponte

> **Rascunho de IA; validado pelo autor em 28/09/2026** (resposta a Q5, leitura do R-29 por instância e síntese para a Ponte). Claude Code (claude-opus-5-5), 28/09/2026. Cada número vem de um registro de experimento (EXP-nn, em `experimentos/execucoes/`) ou de um arquivo de `data/ipc-2011-2023/`, com o script indicado. As decisões de desenho foram tomadas pelo Coordenador por delegação do autor (`docs/fase4b-desenho.md`). O texto da dissertação é do autor; este relatório é material de trabalho.

## 1. As perguntas

- **Q5.** Nos resultados publicados das IPCs posteriores a 2010, quais características estruturais do domínio, extraídas automaticamente do PDDL (sem UML.P), explicam o desempenho relativo das famílias de técnicas de planejamento?
- **R-29 por instância** (transferido da Fase 3; complementa Q1). Escolher o planejador por instância, pelas características da tarefa, ganha da escolha fixa do melhor planejador?

A Fase 3 respondeu Q1 e Q2 com o Planner Museum, por domínio. A 4B usa os resultados das próprias competições, por instância, e acrescenta propriedades com fundamento teórico às *features* sintáticas.

## 2. O caminho

| Etapa | O que foi feito | Onde |
|---|---|---|
| Levantamento | O que cada IPC de 2011 a 2023 publicou e o que ainda está acessível | `docs/resultados-ipc-2011-2023.md` |
| Dados de resultado | 2011: planos válidos por instância, recuperados do WebPlan no Software Heritage (560 problemas, 5.679 planos) e validados contra a ordem oficial. 2018: 17.640 execuções, validadas contra o relatório oficial | `data/ipc-2011-2023/` |
| Ligação ao PDDL | Os 560 problemas de 2011 ligados aos arquivos pelo SHA-1, sem divergência | `ipc2011_arquivos.csv` |
| Decisões de desenho | D1: regra dos portfólios (P1 + critério para áreas cinzentas). D2: recorte (2011 e 2018 na análise; 2014 e 2023 descritivas) | `docs/fase4b-desenho.md` |
| Técnicas | 78 planejadores × trilha de 2011 e 2018 na taxonomia 4D, a partir dos resumos oficiais | `planejadores_4d.csv` |
| Características | 16 *features* SAS+ (extrator da Fase 3; 2.026 de 2.136 tarefas) e 6 propriedades de topologia de busca (extrator novo, validado contra a Tabela 3 de [@hoffmann2011analyzing]; 1.793 de 1.824 tarefas) | `features_sas_ipc.csv`, `topologia_ipc.csv` |
| Análises | EXP-21 (Q5 com *features* SAS+), EXP-24 (R-29 por instância), EXP-25 (topologia na Q5 e no R-29) | `experimentos/execucoes/` |

**Unidade de análise.** Instância, agregada por domínio só no mapa. A validação é sempre fora do domínio: o modelo é treinado nos outros domínios da mesma edição e trilha. As comparações nunca juntam edições. Todo resultado sai em dois recortes, com todos os planejadores e sem portfólios. Os testes são de permutação ou Wilcoxon, com correção de Holm.

## 3. Resposta a Q5

**Há diferença entre famílias, mas concentrada em poucos lugares.** `[FATO]` (EXP-21, mapa)
- Na *satisficing* e na *agile*, de 2011 e de 2018, algum planejador de busca progressiva empata com o melhor em todos os domínios.
- Só na trilha ótima outra família supera a progressiva: a busca simbólica, em 4 dos 14 domínios de 2011 e em 3 dos 12 de 2018; e o CPT4 (planos parciais com restrições), no parcprinter de 2011.

**As 16 *features* SAS+ não antecipam, fora do domínio, qual família resolve a instância.** `[FATO]` (EXP-21)
- A AUC mediana da regressão logística é 0,59, contra 0,58 de um modelo só com o tamanho da tarefa; a árvore rasa fica em 0,49.
- Depois de Holm, sobrevivem 6 modelos por recorte, quase todos de famílias com 1 a 3 planejadores. Nesses casos, o sinal é do planejador, não da técnica.
- A única família ampla com sinal (*landmarks* na ótima de 2018, sem portfólios) aparece num só recorte e num só modelo.

**As propriedades de topologia acrescentam pouco, e de forma desigual.** `[FATO]` (EXP-25)
- Somadas às SAS+, elevam a AUC mediana de 0,03 a 0,06. O acréscimo passa no teste com Holm em cerca de um terço das famílias, inclusive famílias amplas:
  - busca progressiva (10 planejadores, 0,63 → 0,75) e *landmarks* (7, 0,68 → 0,80) na ótima de 2011;
  - busca por largura/novidade (12, 0,52 → 0,62) na *satisficing* de 2018.
- Em metade dos modelos, somar a topologia piora a previsão fora do domínio. Sozinha, ela fica abaixo das SAS+.
- Decomposição exploratória (EXP-25):
  - na ótima de 2011, o ganho vem do hFF no estado inicial, que mede o comprimento do plano relaxado, ou seja, a dificuldade;
  - na *satisficing* de 2018, vem das medidas de amostragem (becos sem saída, sucesso da sondagem), que são a topologia propriamente dita.

**Resposta a Q5** (validada pelo autor em 28/09/2026):
- Nas IPCs de 2011 e 2018, nenhuma característica estrutural extraída do PDDL explica de forma robusta o desempenho relativo das famílias de técnica fora do domínio.
- As que mais explicam não são estruturais no sentido estrito. São medidas que sondam a tarefa com a heurística de relaxação: o tamanho do plano relaxado e a paisagem de hFF em estados amostrados. Estão mais perto de executar uma busca curta do que de ler a estrutura do modelo.
- Mesmo com elas, o poder de explicar fica entre 0,6 e 0,8 de AUC, e só em parte das famílias.
- A diferença entre famílias que existe, a busca simbólica na trilha ótima, aparece no mapa por domínio, mas nenhuma das características a antecipa.
- Isso confirma, com dados de competição e duas edições, o que a Fase 3 viu no Planner Museum.
- Também é coerente com a afirmação de [@vallati2018what] (p. 34) de que não havia propriedades de domínio independentes de planejador aceitas para classificar modelos estaticamente.

## 4. R-29 por instância: a escolha por instância não ganha da escolha fixa

- **Com todos os planejadores, nenhum seletor supera o melhor planejador único** em nenhuma das 10 unidades (edição × trilha × recorte). `[FATO]` (EXP-24 e EXP-25)
  - Vale para o método de 2010, o método de 2010 pela taxonomia 4D, o kNN e o *random forest*, com *features* SAS+, com topologia e com as duas.
  - Nesse recorte, o melhor planejador único costuma ser um portfólio (Delfi1, Saarplan, FDSS-1) ou o LAMA-2011.
- **Sem portfólios, na *agile* de 2018, o método de 2010 pela taxonomia 4D fecha 42% da lacuna** em relação à linha de base LAMA 2011. O p de Holm é 0,047 dentro da unidade e 0,43 com as 60 comparações juntas. `[FATO]` (EXP-24)
- `[HIPÓTESE]` A escolha por instância só tem espaço quando a melhor escolha fixa é fraca. Com portfólios na disputa, o portfólio já absorve a complementaridade que o seletor tentaria explorar, em linha com [@cenamor2016ibacop].

## 5. Mapa característica × técnica (entregável)

O mapa tem duas partes.
- **Descritiva:** `experimentos/analise/q5-ipc/mapa_familias.csv`, com a melhor cobertura de cada família em cada domínio.
- **Explicativa:** `experimentos/analise/topologia-q5/modelos.csv`, com a AUC de cada conjunto por família.

As associações que resistem ao teste, lidas nos coeficientes da logística ajustada em todos os domínios (EXP-21 e EXP-25), são estas:

| Família (edição e trilha) | Resolve menos quando… | Tipo da característica |
|---|---|---|
| Busca progressiva e *landmarks* (2011, ótima) | o plano relaxado do estado inicial é longo; o grafo causal tem mais componentes fortemente conexas | dificuldade (hFF) e estrutura (grafo causal) |
| *Landmarks* (2018, ótima, sem portfólios) | há mais operadores e domínios de variável maiores | tamanho |
| Largura/novidade e contagem de metas (2018, *satisficing*) | os domínios das variáveis são maiores e há **mais** transições inversíveis (sentido contrário ao que a teoria de Hoffmann sugeriria) | estrutura (domínio de variável, inversibilidade) |

Nenhuma dessas associações vale para todas as trilhas ou edições. Os coeficientes vêm de *features* correlacionadas entre si e servem para descrever o modelo, não para atribuir efeito a uma característica isolada.

## 6. Síntese para a Ponte (Fase 5)

**O que se transfere, como hipótese de trabalho:**
1. **A heterogeneidade existe, mas concentrada.** Nas IPCs, a família de técnica importa em poucas trilhas e domínios. `[HIPÓTESE]` Em desenvolvimento com IA, a diferença entre configurações de agente pode ser igualmente concentrada em alguns tipos de tarefa. O primeiro passo é medir onde ela está, não prever para todas.
2. **Uma linha de base fixa forte absorve a complementaridade.** Com portfólios, a seleção não ganhou. `[HIPÓTESE]` Uma configuração fixa robusta, de agente ou de modelo, pode ser difícil de superar por roteamento. Qualquer proposta de roteamento precisa ser comparada com ela.
3. **Sondar informa mais que ler a estrutura.** O que mais explicou foram medidas que executam um pouco da heurística sobre a tarefa, e não métricas sintáticas. `[HIPÓTESE]` Em software, uma tentativa curta e barata (rodar os testes, um primeiro passo do agente) pode dizer mais sobre a configuração adequada do que métricas estáticas do repositório.
4. **O protocolo de avaliação.** Transfere-se como exigência, não como hipótese:
   - validar fora do grupo observado (domínio, aqui; repositório ou projeto, lá);
   - comparar com a melhor escolha fixa;
   - separar efeito de família e de implementação;
   - corrigir para comparações múltiplas;
   - checar vazamento. A primeira rodada do EXP-25 usou, sem perceber, uma medida derivada do resultado dos competidores, e a correção foi descartar a rodada.

**O que não se transfere:**
- As características específicas (SAS+, hFF, sondagem sob hFF) e os tamanhos de efeito: são próprios do planejamento clássico.
- A taxonomia 4D como classificação de agentes de software.
- Qualquer afirmação de que a seleção por tarefa funciona. O resultado aqui é o contrário, com um único indício local.
- Conclusões sobre qualidade, segurança ou manutenção de software. A 4B mede só cobertura.

`[HIPÓTESE]` **Ajuste sugerido à síntese já escrita da Ponte** (`ponte-software/relatorio/sintese-exploratoria.md`, seção 7), a fazer na sessão da Fase 5: a síntese integrou o EXP-21 e o EXP-24 e não presumia nada das propriedades teóricas. O EXP-25 mostra que elas acrescentam um sinal modesto e desigual, que vem de sondar a tarefa (pontos 1 e 3 acima), e não muda a conclusão sobre seleção.

## 7. Limites

- **Duas edições** (2011 e 2018), 12 a 14 domínios por trilha. A validação fora do domínio tem pouco poder, e as AUCs são ruidosas.
- **Só cobertura.** Qualidade dos planos e tempo, que definem os placares da *satisficing* e da *agile*, ficam fora.
- **2014 e 2023 só descritivos.** Não há resultados por domínio de 2014. De 2023, só por domínio e 7 domínios; o autor decidiu não pedir os dados por instância.
- **Seleção de instâncias pelas próprias competições.** Em 2014, as instâncias foram escolhidas pelo desempenho dos competidores [@vallati2018what]. As edições usadas aqui não foram auditadas quanto a isso `[A CONFIRMAR]`.
- **Classificação das técnicas** a partir de resumos, com regra própria para portfólios. Famílias com um só planejador confundem técnica e implementação.
- **Topologia medida sob hFF**, com 10 amostras por tarefa. Ela é mais próxima das famílias de busca heurística do que das outras.
- **Tarefas sem características:** 32 de 2018 sem *features* SAS+ (tradução acima de 1.800 s) e 31 sem topologia completa ficaram fora.

## 8. O que isto muda na dissertação

- **Capítulo de resultados:** a 4B passa a ser a evidência principal de que a pergunta de 2010 continua pertinente, mas sem resposta preditiva. Com dados de competição e por instância, nem as *features* modernas nem as propriedades de topologia antecipam a técnica adequada de forma robusta.
- **Revisão da literatura:** [@hoffmann2011analyzing] deixa de ser só referência conceitual e passa a ser método aplicado e validado. A afirmação de [@vallati2018what] sobre a falta de propriedades estáticas aceitas ganha apoio empírico.
- **Ponte:** os quatro pontos transferíveis da seção 6 alimentam o capítulo da Ponte como hipóteses e salvaguardas, não como resultados.

## 9. Pendências

- ~~Validação do autor~~ — feita em 28/09/2026: resposta a Q5 (seção 3), leitura do R-29 (seção 4) e síntese para a Ponte (seção 6).
- ~~Ajuste na síntese da Ponte~~ — feito em 28/09/2026 (síntese e dossiê da Fase 5 com o EXP-25).
- ~~Correção do EXP-13~~ — feita em 28/09/2026: o Stone Soup 2011 *satisficing* não usa *landmarks*; o EXP-13 rodado de novo deu saídas idênticas.
- As *features* das 78 tarefas de 2023 que estouraram 300 s não serão extraídas (decisão do autor, 28/09/2026); 2023 fica descritiva com as tarefas que já têm *features*.
