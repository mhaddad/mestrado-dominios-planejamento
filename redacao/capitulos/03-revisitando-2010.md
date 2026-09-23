---
titulo: "Revisitando 2010: auditoria da dissertação original"
status: rascunho-de-ia
data: 2026-09-23
fonte: entregáveis da Fase 2 (auditoria/)
---

# Revisitando 2010: auditoria da dissertação original

> Rascunho gerado por IA a partir dos entregáveis da Fase 2 (`auditoria/relatorio-auditoria.md`, `auditoria/afirmacoes.csv`, `auditoria/achados-fase0.md`, `auditoria/taxonomia-tecnicas.md`). Os números vêm dos scripts em `auditoria/scripts/`; as citações usam só chaves do `literatura/referencias/referencias.bib`. É material de trabalho: o texto final é do autor.

Este capítulo examina a dissertação de 2010 [@haddad2010relacao] com os instrumentos de 2026: a literatura revista no capítulo anterior, as fontes primárias dos planejadores e das competições que ela usou, e os próprios dados e arquivos do trabalho, preservados no acervo. O objetivo não é refazer o estudo — isso é tarefa dos capítulos seguintes —, mas separar, afirmação por afirmação, o que continua de pé, o que precisa ser dito de outro modo e o que não se sustenta. A auditoria também produziu duas coisas que a revisão usa adiante: uma taxonomia de técnicas refeita a partir das fontes primárias e uma lista do que precisa ser reexecutado.

## O estudo de 2010 em síntese

A dissertação perguntava se características de um domínio de planejamento indicam quais técnicas, e portanto quais planejadores, terão melhor desempenho nele. A motivação vinha das Competições Internacionais de Planejamento (IPCs): planejadores que se destacavam em alguns domínios falhavam em outros, e a hipótese era que parte dessa variação se explicasse pelo encontro entre a técnica de cada planejador e as características de cada domínio [@haddad2010relacao].

O método tinha oito etapas. Os domínios eram modelados em UML.P no itSIMPLE, com diagramas de casos de uso, de classes e de estados; 17 métricas eram contadas à mão nesses diagramas e discretizadas em Alto, Médio e Baixo segundo a variância dos valores nos domínios estudados. A eficiência de cada planejador em cada domínio era a porcentagem de problemas resolvidos, tirada dos resultados das IPCs ou, quando faltava, de execução própria, com limite de 20 minutos por problema, em cerca de 2.000 execuções. As porcentagens viravam notas de 0 a 10. Cada planejador era associado às técnicas que usava, e a nota média de cada técnica sob cada característica dava a relação entre características e técnicas. Por fim, a média das notas das técnicas de um planejador, sob as características de um domínio novo, gerava um *ranking* de planejadores para esse domínio.

O estudo usou 10 planejadores (Blackbox, IPP, FF, System R, LPG, Fast Downward, YAHSP, SGPlan, SATPlan e MAXPLAN), 10 domínios de treino (Blocks World, Depots, DriverLog, Gripper, Logistics, Mystery, Pathways, Pipesworld, Satellite e TPP) e 3 de validação (Storage, Zeno-travel e Elevator). As conclusões afirmavam que existe relação entre características de domínio e técnicas de planejamento; que seis características e seis técnicas se destacam; e que o *ranking* permite escolher, só com as características do domínio, os planejadores de melhor desempenho, com margem de acerto de 50% nos domínios Storage e Elevator [@haddad2010relacao].

## Como a auditoria foi feita

O texto de 2010 foi dividido em blocos e dele foram extraídas 349 afirmações substantivas: resultados, decisões de método, classificações, afirmações sobre outras obras e sobre o estado do campo, contribuições e trabalhos futuros. Cada afirmação guarda o trecho literal e a linha de origem; um script confere que o trecho é cópia exata do original. Os números foram recalculados por script a partir das tabelas publicadas, e as afirmações sobre outras obras foram conferidas na fonte primária — os artigos que descrevem cada planejador e os relatórios oficiais de cada IPC [@mcdermott2000planning; @bacchus2001aips; @long2003third; @hoffmann2005deterministic].

Cada afirmação recebeu uma de três classes. *Mantém*: correta e sustentada como está. *Reformula*: o núcleo se sustenta, mas precisa de correção, restrição, atualização ou de evidência que 2010 não deu. *Descarta*: errada, contrariada pela fonte primária ou pelos próprios dados de 2010. Uma descrição fiel de um método fraco foi classificada como *mantém*; a fraqueza foi atribuída às conclusões que se apoiam nele. A extração, a conferência e a classificação foram feitas com apoio de modelos de linguagem, sob coordenação e verificação registradas no repositório do projeto; o autor revisou as classificações de *reformula* e *descarta*.

## Resultado geral

Das 349 afirmações, 265 se mantêm, 80 precisam ser reformuladas e 4 são descartadas (Tabela 1).

**Tabela 1 – Classificação das afirmações da dissertação de 2010, por capítulo**

| Capítulo de 2010 | Afirmações | Mantém | Reformula | Descarta |
|---|---|---|---|---|
| Resumo | 6 | 4 | 2 | 0 |
| Introdução | 43 | 27 | 13 | 3 |
| Revisão bibliográfica | 145 | 122 | 23 | 0 |
| Planejadores | 20 | 18 | 1 | 1 |
| Domínios | 31 | 25 | 6 | 0 |
| Características × técnicas | 41 | 35 | 6 | 0 |
| Testes e validações | 42 | 30 | 12 | 0 |
| Conclusões e trabalhos futuros | 21 | 4 | 17 | 0 |
| **Total** | **349** | **265** | **80** | **4** |

Fonte: `auditoria/afirmacoes.csv`, gerado por `auditoria/scripts/resumir_auditoria.py`.

A distribuição tem um padrão claro. O que 2010 descreve — o método, os domínios, a história do campo — se sustenta quase todo. O que precisa mudar se concentra onde o texto tira conclusões: 33 das 69 afirmações de resultado e 17 das 21 afirmações das conclusões e trabalhos futuros são *reformula*. As quatro afirmações descartadas não são conclusões centrais: três são comparações numéricas entre planejadores nas IPCs, contrariadas pelos resultados oficiais, e a quarta é a convenção que sustenta a taxonomia de técnicas, examinada adiante.

## O que se sustenta

O princípio que motivou o trabalho é, hoje, o fundamento de um campo inteiro. A ideia de que características extraídas de um problema indicam o algoritmo de melhor desempenho é o problema de seleção de algoritmos formalizado por Rice [@rice1976algorithm] e desenvolvido, em planejamento, por *portfólios* e sistemas de seleção [@kerschke2019automated; @helmert2011fast; @cenamor2016ibacop]. A observação de partida — nenhum planejador domina todos os domínios — foi reafirmada pela literatura posterior com dados muito mais amplos [@nunez2015automatic; @lindauer2019algorithm].

A pergunta também tinha uma origem que o texto de 2010 não registrou. O artigo que apresentou o itSIMPLE, em 2005, já declarava como alvo classificar características de domínio para decidir qual técnica ou heurística se ajusta a cada domínio [@vaquero2005itsimple]. A dissertação foi, nesse sentido, a primeira execução de um objetivo do projeto itSIMPLE, por um caminho diferente do previsto em 2005 — contagens em diagramas UML, e não análise por redes de Petri.

A descrição das competições resistiu bem à conferência. Os destaques de cada edição citados em 2010 conferem com os relatórios oficiais: o IPP venceu a trilha ADL em 1998 [@mcdermott2000planning]; FF e System R se destacaram em 2000 [@bacchus2001aips]; FF, LPG e MIPS, em 2002 [@long2003third]; os seis planejadores citados para 2004 são exatamente os premiados daquela edição [@hoffmann2005deterministic]. As duas obras citadas como trabalhos relacionados também estão descritas corretamente na essência [@hoffmann2001topology; @gerevini2004heuristic].

## Os dados de 2010: origem e consistência

A auditoria encontrou quatro problemas nos dados que sustentam os resultados. Nenhum muda a ordem de nenhum *ranking*, mas todos precisam ser corrigidos ou documentados.

**Duas populações de dados.** A eficiência de cada par planejador × domínio vinha ou dos resultados de uma IPC ou de execução própria. Segundo as tabelas publicadas, eram 38 pares de competição e 62 de execução própria. A conferência mostrou que quatro dos 38 — System R e Fast Downward nos domínios Depots e DriverLog — não podem vir de competição: esses domínios só estiveram na IPC de 2002 [@long2003third], da qual nenhum dos dois participou, e a IPC de 2004 não os reusou [@hoffmann2005deterministic]. O acervo guarda os registros de execução própria desses quatro pares, e só deles, e os planos ali registrados dão exatamente os percentuais publicados (1 de 22, 5 de 20, 19 de 22 e 20 de 20). A divisão correta é, portanto, 34 pares de competição e 66 de execução própria. A diferença importa porque as duas populações foram obtidas em condições distintas — equipamento e limites de cada competição, de um lado; oito computadores idênticos e limite de 20 minutos, de outro — e as tabelas de 2010 as combinam sem distinção.

**Subconjuntos de instâncias.** Em três domínios, o acervo usa só os primeiros problemas de cada conjunto da IPC: 35 de 102 no Blocks World, 28 de 84 no Logistics e 20 de 36 no Satellite. O critério, segundo o autor, foi reproduzir o subconjunto usado nos resultados publicados. A escolha é coerente com a prática da época: o artigo do Fast Downward avalia exatamente 35 tarefas de Blocks World e 28 de Logistics da IPC de 2000 [@helmert2006fast].

**Médias com pequenos erros.** Das 64 médias publicadas nas tabelas de validação, recalculadas por script, 9 foram truncadas em vez de arredondadas e 5 divergem além disso. O texto dá 6,17 para a nota do Blackbox no Storage; a média das cinco técnicas que a dissertação lhe atribui é 6,07, e as Tabelas 29 e 30 publicam 6,1 e 6,2. Nenhuma dessas diferenças altera a ordem dos planejadores.

**Métricas com definição a precisar.** O rótulo "Número de Casos de Uso por Atores" está invertido: os valores publicados são atores divididos por casos de uso. A contagem de classes excluiu classes auxiliares criadas pelo modelador (como `Utility`, para variáveis globais); a contagem de agregações não é reproduzível a partir dos modelos, o que indica um critério não documentado; e duas contagens publicadas divergem dos diagramas (associações no Pathways, generalizações no TPP). São problemas de instrumento, tratados na seção sobre as métricas UML.

## A taxonomia de técnicas

A relação entre características e técnicas dependia de atribuir a cada planejador as técnicas que ele usa. A dissertação usou onze rótulos — *State-Space*, *Plan-Space*, *Partial-order*, *Total-order*, *Hierarchical*, *Forward-chaining*, *Backward-chaining*, *Graph-based*, *Knowledge-based*, *SAT-based* e *Heuristic Search* — e atribuiu a cada planejador um subconjunto deles [@haddad2010relacao]. Confrontada com a descrição que cada planejador dá de si na fonte primária, essa atribuição não se sustenta como sistema, por dois motivos.

O primeiro é que os rótulos misturam dimensões independentes. Alguns descrevem a direção da busca (*Forward-chaining*, *Backward-chaining*); outros, o espaço em que ela ocorre (*State-Space*, *Plan-Space*); outros, uma propriedade do plano produzido (*Partial-order*, *Total-order*); outros, o tipo de heurística ou a fonte de conhecimento. Um planejador pode ter vários rótulos ao mesmo tempo sem que isso diga como ele funciona.

O segundo é que várias atribuições contrariam as fontes. O texto de 2010 trata todos os planejadores baseados em satisfatibilidade como *Forward-chaining* "por partirem do estado inicial", por convenção própria; nas fontes do Blackbox, do SATPlan e do MAXPLAN, quem busca é o resolvedor SAT, sobre uma codificação de horizonte fixo [@kautz1999unifying; @kautz2006satplan; @xing2006maxplan]. O Fast Downward aparece como *Hierarchical*, mas a decomposição hierárquica está só no cálculo da heurística de grafo causal; a busca é progressiva no espaço de estados [@helmert2006fast]. O YAHSP aparece como *Knowledge-based*, mas reaproveita informação calculada pela própria heurística, não conhecimento de domínio fornecido por fora [@vidal2004lookahead]. O caso do System R é mais sutil: o rótulo *Backward-chaining* tem base parcial, porque o planejador regride metas e progride o estado, uma versão do STRIPS recursivo [@lin2001planner; @bacchus2001aips], mas não faz busca regressiva no espaço de estados.

A revisão substitui a taxonomia de 2010 por outra em quatro dimensões: (1) algoritmo e espaço de busca, (2) heurística, (3) representação do estado ou do problema e (4) arquitetura do sistema, isto é, planejador único ou *portfólio*. *Partial-order* e *Total-order* deixam de ser técnicas e passam a atributo do plano. A Tabela 2 reclassifica os dez planejadores.

**Tabela 2 – Os planejadores de 2010 na nova taxonomia**

| Planejador | Algoritmo e espaço de busca | Heurística | Representação | Arquitetura |
|---|---|---|---|---|
| Blackbox | Grafo de planejamento compilado para SAT | Sem heurística própria | Proposicional, em SAT | Único |
| IPP | Extração de plano do grafo de planejamento | Sem heurística | STRIPS/ADL sobre grafo de planos | Único |
| FF | Progressiva no espaço de estados (*enforced hill-climbing*) | Relaxação (*delete relaxation*) | STRIPS proposicional | Único |
| System R | Decomposição recursiva por metas (regressão de metas, progressão de estado) | Sem heurística numérica | STRIPS proposicional | Único |
| LPG | Busca local no espaço de planos parciais | Avaliação heurística dos vizinhos | Grafos de ação | Único |
| Fast Downward | Progressiva no espaço de estados (melhor primeiro) | Grafo causal | Variáveis multivaloradas | Único |
| YAHSP | Progressiva no espaço de estados, com *lookahead* | Relaxação (a do FF) | STRIPS proposicional | Único |
| SGPlan | Particionamento por subobjetivo, com Metric-FF em cada parte | Relaxação | Restrições particionadas | Único |
| SATPlan | Grafo de planejamento compilado para SAT | Sem heurística própria | Proposicional, em SAT | Único |
| MAXPLAN | SAT com decomposição por subobjetivo | Sem heurística própria | Proposicional, com formulação multivalorada | Único |

Fonte: `auditoria/taxonomia-tecnicas.md` e `auditoria/taxonomia/fontes-planejadores.csv`, a partir de [@kautz1999unifying; @koehler1997extending; @hoffmann2001ff; @lin2001planner; @gerevini2004lpgtd; @helmert2006fast; @vidal2004lookahead; @chen2006temporal; @kautz2006satplan; @xing2006maxplan].

A primeira consequência é que a coluna de arquitetura, ausente em 2010, não distingue nenhum dos dez planejadores: todos são sistemas únicos. Essa dimensão passou a importar depois, quando portfólios e sistemas compostos dominaram as competições [@nunez2015automatic; @helmert2011fast]. A segunda é que as relações entre características e técnicas publicadas em 2010 foram calculadas com os rótulos antigos. `[HIPÓTESE]` Parte delas deve mudar quando recalculada com a nova taxonomia; quanto, só o recálculo dirá.

## A validação do *ranking*

A validação de 2010 comparava, em três domínios novos, o *ranking* previsto pelo método com o desempenho observado. O texto informa 50% de acerto no Storage e no Elevator, sem definir a medida. A auditoria reproduziu esses valores como coincidência exata de posição: em 5 das 10 posições, o planejador previsto é o observado, e o autor confirmou que foi essa a regra. Pela mesma regra, o Zeno-travel, cujo acerto o texto não informa, dá 40%.

Duas observações mudam a leitura desse resultado. A primeira é que a medida é sensível a empates. No Zeno-travel, seis planejadores resolveram todos os problemas, e no Elevator, cinco; a ordem entre eles no *ranking* observado é arbitrária, e a taxa de acerto depende de como se desempata.

A segunda observação é mais séria. Os três *rankings* previstos são quase iguais entre si: a correlação de postos entre eles vai de 0,94 a 0,99. Se as características do domínio pesassem na previsão, os *rankings* deveriam variar de um domínio para outro. Para testar isso, a auditoria comparou o método com uma linha de base que ignora as características: ordenar os planejadores pela nota média nos dez domínios de treino (Tabela 3).

**Tabela 3 – *Ranking* de 2010 e linha de base sem características, nos domínios de validação**

| Domínio | Correlação de postos com o observado: 2010 | Correlação de postos: linha de base | Cinco primeiros certos: 2010 | Cinco primeiros certos: linha de base |
|---|---|---|---|---|
| Storage | 0,81 | 0,75 | 5 de 5 | 5 de 5 |
| Zeno-travel | 0,86 | 0,68 | 5 de 5 | 5 de 5 |
| Elevator | 0,65 | 0,65 | 4 de 5 | 4 de 5 |

Fonte: `auditoria/extracao/conferencia-rankings.csv`, gerado por `auditoria/scripts/conferir_rankings.py` a partir das Tabelas 30, 31, 36, 37, 42 e 43 de 2010.

O método de 2010 fica à frente da linha de base em dois dos três domínios e empata no terceiro, mas a linha de base acerta os mesmos cinco primeiros planejadores. `[HIPÓTESE]` Boa parte do que o *ranking* previa refletia a qualidade geral dos planejadores, não o ajuste entre técnica e domínio. Com dez planejadores e três domínios de validação, a diferença a favor do método não permite concluir que as características do domínio melhoraram a escolha. A literatura atual trata exatamente esse ponto ao comparar métodos de seleção com o melhor planejador único e com o oráculo que escolhe o melhor para cada caso [@bischl2016aslib; @lindauer2019algorithm].

## As métricas UML como instrumento

As métricas de 2010 foram contadas em modelos UML.P, a notação do itSIMPLE. A própria definição da notação mostra que parte do que as métricas contam é convenção de modelagem, e não propriedade do domínio. Na tradução de um domínio PDDL para UML.P, cada ação vira método da classe do seu primeiro parâmetro, que passa a ser subclasse de `Agent`; toda classe que não age é agregada ao `Environment`; e toda associação recebe multiplicidade 0..*, porque o PDDL não informa quantidades [@tonidandel2006reading]. A estrutura geral com as classes `Agent`, `Environment` e `Planner` é imposta pela ferramenta a todo modelo [@vaquero2005itsimple]. `[HIPÓTESE]` Contagens como as de métodos por classe, agregações e associações refletem em parte essas convenções e a ordem em que o modelador escreveu as ações.

A literatura posterior reforça a preocupação por outro caminho. Reordenar um modelo de domínio sem mudar seu significado altera o desempenho dos planejadores e pode inverter *rankings* [@vallati2021importance; @vallati2015effective]. E as estruturas com efeito demonstrado sobre a dificuldade de uma tarefa — o grafo causal, os grafos de transição de domínio e a largura de árvore do grafo causal — são extraídas automaticamente do PDDL, não contadas à mão em diagramas [@helmert2009concise; @hoffmann2011analyzing; @domshlak2013complexity]. As contagens sintáticas, as mais próximas das contagens de 2010, são a família de *features* que menos acrescenta à predição de desempenho [@fawcett2014improved].

Isso não prova que as métricas UML sejam inúteis: nenhum trabalho revisado as comparou com *features* de PDDL nos mesmos domínios. É essa comparação, com controle da ordem de escrita do modelo, que a revisão propõe como segunda pergunta de pesquisa.

## As conclusões de 2010 à luz da revisão

A Tabela 4 resume o veredito sobre as oito afirmações centrais da dissertação, combinando a literatura revista no capítulo anterior com os achados desta auditoria.

**Tabela 4 – Veredito sobre as afirmações centrais de 2010**

| Afirmação de 2010 | Veredito | Por quê |
|---|---|---|
| Existe relação entre características de domínio e técnicas de planejamento | Mantém, com reformulação | O princípio é o da seleção de algoritmos [@rice1976algorithm; @kerschke2019automated]; mas os dados de 2010 não separam o efeito das características do efeito da qualidade geral dos planejadores. |
| As técnicas mais promissoras são *Heuristic Search*, *Hierarchical*, *Knowledge-based*, *Forward-chaining*, *Plan-Space* e *Total-order* | Reformula | A lista usa rótulos que a nova taxonomia desfaz e não inclui o aprendizado de máquina, que produz heurísticas competitivas em domínios usados em 2010 [@ferber2022neural; @toyer2020asnets]. |
| Só com as características do domínio, independentemente do problema, o *ranking* escolhe os melhores planejadores | Reformula | Sistemas por instância escolhem planejadores diferentes dentro do mesmo domínio [@cenamor2016ibacop]; a configuração por domínio continua competitiva quando há treino no domínio [@nunez2015automatic]; e a validação de 2010 não se distingue de uma linha de base sem características. |
| Mais características, planejadores e técnicas melhoram o *ranking* | Mantém, com ressalva | Vale como tendência, mas não há subconjunto de *features* bom para todos os planejadores [@fawcett2014improved]. |
| Diagramas UML medem a complexidade do domínio, que afeta o desempenho | Reformula | A complexidade estrutural afeta o desempenho, mas os determinantes demonstrados vêm do PDDL; as métricas UML dependem de convenções de modelagem [@helmert2009concise; @tonidandel2006reading]. |
| Taxonomia de técnicas (Tabelas 2 a 4 de 2010) | Descarta | Mistura dimensões e contraria as fontes primárias; substituída pela taxonomia em quatro dimensões. |
| Eficiência é a porcentagem de problemas resolvidos | Reformula | A cobertura é uma medida legítima, mas não a única: as competições medem também tempo e qualidade do plano [@hoffmann2005deterministic; @nunez2015automatic]. |
| Trabalhos relacionados: Hoffmann (2001) e Gerevini, Saetti e Serina (2004) | Descarta como revisão suficiente | As duas obras estão bem descritas, mas a seção ignora a seleção de algoritmos e a origem da pergunta no itSIMPLE [@rice1976algorithm; @roberts2009learning; @vaquero2005itsimple]. |

Os trabalhos futuros propostos em 2010 tiveram destinos diferentes. A extração automática das métricas e a atribuição de pesos às características foram realizadas pela comunidade por outros caminhos: *features* automáticas de PDDL e modelos de desempenho aprendidos [@fawcett2014improved; @hutter2014algorithm]. O detalhamento das técnicas em heurística, busca e subtécnicas é o que a nova taxonomia faz. A análise estatística da discretização foi, na prática, superada pela decisão de não discretizar e usar as características como valores contínuos [@fawcett2014improved].

## O que a revisão precisa testar

A auditoria deixa três tarefas para os capítulos seguintes. A primeira é reproduzir o método de 2010 por script, sobre os mesmos dados, e medir o efeito de cada correção — a nova taxonomia, as métricas corrigidas, a separação das duas populações de dados — isoladamente. A segunda é reexecutar os planejadores sob condições únicas, com validação dos planos, e comparar o método de 2010 com o melhor planejador único e com o oráculo. A terceira é responder à pergunta que 2010 deixou implícita: se métricas estruturais de modelagem acrescentam algo às *features* extraídas automaticamente do PDDL. O plano completo está em `auditoria/reexecucao.md`.
