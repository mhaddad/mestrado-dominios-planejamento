CENTRO UNIVERSITÁRIO DA FEI

MATHEUS HADDAD

RELAÇÃO ENTRE CARACTERÍSTICAS DE DOMÍNIOS
 E TÉCNICAS DE PLANEJAMENTO

São Bernardo do Campo

2010

MATHEUS HADDAD

RELAÇÃO ENTRE CARACTERÍSTICAS DE DOMÍNIOS
 E TÉCNICAS DE PLANEJAMENTO

Dissertação de Mestrado apresentada ao Centro Universitário da FEI para obtenção do título de Mestre em Engenharia Elétrica, orientada pelo Prof. Dr. Flavio Tonidandel

São Bernardo do Campo

2010

Matheus Haddad

Relação entre características de domínios e técnicas de planejamento

Dissertação de Mestrado - Centro Universitário da FEI

Comissão julgadora

________________________________________

Prof. Dr. Flavio Tonidandel – FEI

________________________________________

Prof. Dr. Plínio Thomaz Aquino Junior – FEI

________________________________________

Profª. Drª. Leliane Nunes de Barros – IME-USP

São Bernardo do Campo

10/03/2010

Para minha amada esposa Daiana Haddad, meus pais e meus irmãos.

Agradecimentos

Ao Grande Arquiteto do Universo, que é Deus, por ter apresentado as oportunidades necessárias para a conquista do título de Mestre.

À minha esposa Daiana Haddad, pelo apoio, compreensão e incentivo nos momentos mais árduos desta pesquisa.

Ao meu professor Flavio Tonidandel, pela orientação, motivação e cobrança contínua por resultados.

Aos meus pais, Fuad Haddad e Tereza Haddad, e meus irmãos, Davi Haddad e Bárbara Haddad, por terem proporcionado uma vida repleta de alegrias e realizações.

Aos meus amigos da empresa WebGoal, pelo incentivo constante para a finalização deste trabalho e pelos momentos de descontração.

Aos meus alunos dos cursos de graduação e pós-graduação, pelo interesse em aprender sobre planejamento automático e pela oportunidade de ensiná-los.

Já determinamos que a origem de todos os outros movimentos é o que move a si mesmo, e que a origem disso é o imóvel, e que o primeiro motor deve ser necessariamente imóvel.

Aristóteles

Resumo

As competições internacionais de planejamento mostraram nos seus resultados desempenhos diferentes dos planejadores na resolução de problemas de certos domínios. Enquanto num determinado domínio um planejador se saía muito bem, em outro domínio ele não apresentava o mesmo desempenho. Esses planejadores utilizam técnicas diferentes, que são responsáveis pela eficiência de um planejador em resolver problemas de planejamento. Os domínios apresentam características diferentes, que também são responsáveis pelo desempenho de um planejador. Essas características podem ser identificadas modelando os domínios em diagramas da UML. A criação de uma relação entre características de domínios e técnicas de planejamento, baseada nos resultados da eficiência dos planejadores nas competições internacionais de planejamento, proporcionou um método para criar um ranking de planejadores que ajude a selecionar o planejador mais promissor para resolver problemas de planejamento de um determinado domínio.

Palavras-chave: Planejamento Automático. Domínios de Planejamento. UML.

Abstract

The International Planning Competition results showed different performances of the planners in solving problems of certain domains. While a given domain a planner went very well, in another domain it did not have the same performance. These planners use different techniques, which are responsible for the planner efficiency to solve planning problems. The domains have different features, which are also responsible for the planner performance. These features can be identified by modeling the domains in the UML diagrams. The creation of a relationship between domains features and planning techniques, based on the results of planners efficiency in the international planning competition, provided a method for creating a ranking of planners to help select the most promising planner to solve a given planning domain.

Key words: Automated Planning. Planning Domains. UML.

LISTA DE SIGLAS

ADL: Action Description Language (linguagem de descrição de ações)

DIT: Depth of Inheritance Tree (profundidade da ávore de herança)

GPS: General Problem Solver (solucionador geral de problemas)

HAgg: Height of Aggregation (altura da agregação)

HTN: Hierarchical Task Network (rede de tarefas hierárquicas)

itSIMPLE: Integrated Tools Software Interface for Modeling PLanning Environments (Ambiente Integrado de Modelagem e Análise de Domínios de Planejamento Automático)

OMT: Object Modeling Technique (técnica de modelagem de objetos)

PDDL: Planning Domain Definition Language (Linguagem de Definição de Domínios de Planejamento)

STRIPS: Stanford Research Institute Planning System (Sistema de Planejamento do Instituto de Pequisa de Stanford)

UML: Unified Modeling Language (Linguagem Unificada de Modelagem)

UML.P: Extensão da UML para planejamento

XML: eXtensible Markup Manguage (linguagem de marcação extensível)

LISTA DE TABELAS

LISTA DE ILUSTRAÇÕES

Sumário

# Introdução

Criar um plano, a partir de um processo de planejamento, pode ser muitas vezes uma tarefa simples para os seres humanos. Desde o final do século XX, principalmente na década de 1990, a criação automática de planos tem sido um grande desafio para os pesquisadores e seus softwares de planejamento.

Esse desafio se resume a responder a seguinte pergunta: partindo da descrição de um domínio de aplicação (por exemplo, uma descrição do plano de vôos de um aeroporto), da definição de um estado inicial (situação inicial das aeronaves, dos vôos e do aeroporto) e de um estado objetivo (situação desejada das aeronaves, dos vôos e do aeroporto), é possível criar uma seqüência de ações que faça a transição entre o estado inicial e o estado objetivo?

Para responder essa pergunta, diversas abordagens de planejamento automático, explicadas nesta dissertação, foram criadas. Essas abordagens partem do princípio que problemas de planejamento são problemas de busca e utilizam técnicas de busca para encontrar um plano ideal, ou seja, uma seqüência mínima de ações que faça a transição de uma situação inicial para uma situação desejada em um domínio.

A partir de 1998 passou a ser realizada uma competição internacional de planejamento (MCDERMOTT, 2008) onde os planejadores criados por pesquisadores de várias partes do mundo, puderam ser confrontados na resolução de problemas de planejamento em um grupo de domínios criados para esse fim. O principal objetivo dessas competições é permitir a evolução do planejamento automático e o aprimoramento das técnicas de planejamento.

Alguns planejadores de destacaram nestas competições. Entretanto, os melhores planejadores (KAUTZ e SELMAN, 1998) (KOEHLER, 1998) (HOFFMANN e NEBEL, 2001) (LIN, 2001) (GEREVINI e SERINA, 2002) (HELMERT, 2006) (VIDAL, 2002) (CHEN, HSU e WAH, 2004) (KAUTZ, SELMAN e HOFFMANN, 2006) (XING, CHEN e ZHANG, 2006) falharam em alguns domínios, enquanto outros planejadores, com desempenho pior, conseguiram resolver todos os problemas de planejamento desses mesmos domínios. Dois fatores principais causaram esse comportamento nos resultados das competições: as técnicas de planejamento utilizadas por cada planejador e as características presentes nos domínios.

O problema que motivou a pesquisa e a escrita desta dissertação é a possibilidade de encontrar uma relação entre características de domínio e técnicas de planejamento. Espera-se através desta relação compreender melhor como determinadas características de domínios afetam as técnicas de planejamento e estabelecer um método que, a partir das características de um domínio, seja capaz de elencar os melhores planejadores, de acordo com suas técnicas de planejamento, para resolver problemas de planejamento.

Estabelecer uma relação entre características de domínios e técnicas de planejamento também mostra ser um caminho promissor para descobrir o que afeta cada técnica de planejamento e como fazer planejadores melhores.

## Motivações

Há mais de uma década, é realizada, a cada dois anos, a Competição Internacional de Planejamento (MCDERMOTT, 2008). Essa competição tem como finalidade principal comparar a eficiência e a eficácia dos planejadores na resolução de problemas de planejamento em determinados domínios.

Analisando os resultados das cinco primeiras competições, é possível perceber a diferença de desempenho entre os planejadores. Na primeira edição da competição  (MCDERMOTT, 2008), realizada em 1998, participaram cinco sistemas de planejamento. Os planejadores IPP (KOEHLER, 1998) e BlackBox (KAUTZ e SELMAN, 1998) foram considerados vencedores. Entretanto, no domínio Logistic World, o planejador BlackBox teve um desempenho 40% melhor do que o IPP. Já no domínio Gripper, o planejador IPP teve um desempenho 150% melhor do que o BlackBox.

Já na segunda competição internacional de planejamento (BACCHUS, 2000), realizada em 2000, os sistemas de planejamento que se destacaram foram o FF (HOFFMANN e NEBEL, 2001) e o System R (LIN, 2001). No domínio Blocks World, o planejador System R foi 30% mais eficiente do que o FF, enquanto no domínio Depots, o planejador FF resolveu todos os problemas e o System R apenas 5%.

Na terceira edição da competição (FOX e LONG, 2002), realizada em 2002, os planejadores que obtiveram os melhores resultados foram o FF, LPG (GEREVINI e SERINA, 2002) e o MIPS (EDELKAMP e HELMERT, 2001). No domínio Depots, para um número pequeno de instâncias (objetos) dentro do problema, o planejador FF levou um tempo maior para gerar os planos, enquanto o planejador LPG foi mais rápido. Porém, para um número maior de instâncias, o FF mostrou um desempenho melhor em relação aos outros planejadores.

Em 2004, na quarta competição internacional de planejamento (EDELKAMP, HOFFMANN e LITTMAN, 2004), os sistemas de planejamento que mais se destacaram foram: Fast Downward (HELMERT, 2006), YAHSP (VIDAL, 2002), SGPlan (CHEN, HSU e WAH, 2004), LPG-TD, SATPLAN04 (KAUTZ, SELMAN e HOFFMANN, 2006) e CPT. Porém, os resultados desta competição também apresentaram características peculiares entre planejadores e domínios. No domínio Pipesworld, o SGPlan teve um desempenho 40% melhor do que o YAHSP. Já no domínio Satellite, ambos tiveram 100% de aproveitamento na resolução dos problemas.

Por fim, na quinta edição da competição internacional de planejamento (GEREVINI, BONET e GIVAN, 2006), realizada em 2006, os planejadores que obtiveram os melhores desempenhos foram o SATPLAN, MAXPLAN (XING, CHEN e ZHANG, 2006) e SGPLAN5. No domínio TPP, o planejador SATPLAN teve um desempenho 50% melhor do que o planejador MAXPLAN. Já no domínio Pathways, o planejador MAXPLAN teve um desempenho 40% melhor do que o planejador SATPLAN.

Da mesma forma que os domínios das competições de planejamento representam situações distintas do mundo real (empilhamento de blocos sobre uma mesa, distribuição logística de mercadorias, combinação moleculares, captação de imagens por satélites e outros), os planejadores que participaram destas competições também utilizam técnicas e estratégias diferentes de planejamento. Os cruzamentos entre domínios de características diferentes com as técnicas de planejamento existentes podem ajudar a compreender essa diferença de desempenho dos planejadores.

Assim, com base nos resultados das competições internacionais de planejamento, a motivação deste trabalho é mostrar que existe uma relação entre as características de domínios e as técnicas de planejamento para justificar essa diferença de desempenho.

## Objetivo e justificativa

O objetivo deste trabalho é identificar uma possível relação entre características de domínios e técnicas de planejamento, e a partir desta relação, criar um método que estabeleça um ranking de planejadores para auxiliar na escolha do melhor planejador para resolver um problema de planejamento num determinado domínio.

As características dos domínios são identificadas a partir da representação do domínio em UML (Unified Modeling Language – Linguagem Unificada de Modelagem), utilizando os diagramas de casos de uso, classes e estados. Já as técnicas de planejamento são definidas de acordo com a estratégia de geração de planos utilizada por cada planejador.

A partir desta relação, um ranking de planejadores é criado para ajudar na escolha do melhor planejador para um determinado problema de um domínio de planejamento, determinando assim quais técnicas de planejamento são melhores para quais características de domínio.

## Contribuições

Atingir o objetivo proposto por este trabalho implica também em contribuições importantes para a área de planejamento automático. Essas contribuições são:

Análise dos resultados das competições internacionais de planejamento;

Revisão sobre os planejadores e suas respectivas técnicas de planejamento;

Modelagem dos principais domínios das competições internacionais de planejamento em UML, utilizando a ferramenta itSIMPLE (Integrated Tools Software Interface for Modeling PLanning Environments - Ambiente Integrado de Modelagem e Análise de Domínios de Planejamento Automático);

Utilização de métricas extraídas dos diagramas de casos de uso, classes e estados da UML para identificar e definir características de domínios de planejamento;

Resultados dos processos de planejamento entre os planejadores e domínios selecionados que não são encontrados nas competições de planejamento;

Método para relacionar características de domínios com técnicas de planejamento baseado na eficiência dos planejadores para resolver problemas de planejamento;

Método para escolher o melhor planejador para resolver um problema de planejamento num determinado domínios a partir de suas características;

Início de uma nova linha de pesquisa dentro da sub-área de planejamento automático.

Esta última contribuição é inovadora por propor uma nova linha de pesquisa e sugerir que, a partir de novos estudos sobre o relacionamento entre características de domínios e técnicas de planejamento, planejadores mais eficientes e eficazes possam ser criados.

## Estrutura da dissertação

Esta dissertação sobre planejamento automático apresenta uma análise dos resultados das competições internacionais de planejamento, dos planejadores e suas técnicas de planejamento, dos domínios e suas características extraídas da UML. Também propõe um método para relacionar essas características com as técnicas de planejamento. Para esse fim, o conteúdo foi organizado da seguinte maneira:

Capítulo 2: este capítulo apresenta uma revisão bibliográfica sobre os principais temas abordados nesta dissertação. Ele é formado por uma introdução sobre a área de planejamento automático e sua evolução, pela análise dos resultados das competições de planejamento, pela revisão sobre as técnicas de planejamento e a modelagem de domínios, por estudos anteriores sobre técnicas de planejamento e seu desempenho nos domínios e por uma visão geral sobre o itSIMPLE, software utilizado neste trabalho como ferramenta para a modelagem de domínios em UML e obtenção de resultados de planejamento;

Capítulo 3: é o capítulo sobre os sistemas de planejamento. São apresentados os planejadores selecionados para este trabalho e uma relação dos planejadores com as respectivas técnicas de planejamento utilizadas por eles;

Capítulo 4: neste capítulo são apresentados os domínios utilizados neste trabalho. Também apresenta uma proposta de caracterização de domínios através de métricas extraídas de diagramas da UML e uma relação entre os domínios selecionados e suas respectivas características, estabelecidas a partir da contabilização das métricas.

Capítulo 5: é o principal capítulo desta dissertação. Neste capítulo é apresentada uma proposta de relação entre características de domínios e técnicas de planejamento, explicando-se o método utilizado. Também são apresentadas as características de domínios que mais criaram impacto em determinadas técnicas de planejamento e os testes e validações feitos a partir de três domínios diferentes.

Capítulo 6: neste capítulo são apresentadas as conclusões e também propostos trabalhos futuros que podem ser realizados a partir desta dissertação.

# Revisão Bibliográfica

Esta revisão bibliográfica apresenta uma introdução sobre a área de planejamento automático e sua evolução, mostrando os principais sistemas de planejamento. Traz ainda a análise dos resultados das cinco primeiras competições internacionais de planejamento e as principais técnicas de planejamento. Por fim, apresenta também uma introdução a duas linguagens de modelagem de domínios, PDDL (Planning Domain Definition Language - Linguagem de Definição de Domínios de Planejamento) e UML, estudos realizados anteriormente que se propuseram a comparar técnicas de planejamento e seu desempenho em domínios e uma visão geral sobre a ferramenta itSIMPLE.

## Planejamento automático

O planejamento de atividades e ações para alcançar um determinado objetivo é uma habilidade inerente a todos os seres humanos. O ato de planejar está ligado, principalmente, a dois conceitos: plano e planejamento.

De acordo com  (GHALLAB, NAU e TRAVERSO, 2004), um plano é um esquema, programa ou método construído de antemão para realizar um objetivo ou meta previamente estabelecidos. Já um planejamento pode ser definido como o processo de escolha e organização de ações através da antecipação de seus efeitos.

A primeira referência de estudo sobre planejamento surgiu na Grécia antiga. O filósofo Aristóteles, em sua obra De Motu Animalium (400 A.C.) (GRUYTER, 1960), discute o princípio dos movimentos dos animais e define um algoritmo de planejamento para representar esses movimentos. Esse algoritmo foi baseado no número de patas de um animal e no fato, observado por Aristóteles, que o movimento de um animal começa pelo lado direito do corpo.

Em ciência da computação, o estudo sobre planejamento concentrou-se na área de inteligência artificial, através de uma sub-área denominada planejamento automático. Esta sub-área estuda a automação do processo de criação de um plano no computador através de um software. O planejamento automático foi criado a partir de investigações de buscas em um espaço de estados, prova de teoremas matemáticos e robótica móvel (RUSSELL e NORVIG, 2002).

As principais pesquisas e trabalhos desenvolvidos na sub-bárea de planejamento automático têm sido direcionados para a criação de sistemas automáticos de planejamento, conhecidos como planejadores. Os planejadores utilizam diversas técnicas de planejamento para criarem planos em qualquer domínio. Essa generalização reflete a natureza complexa deste tipo de problema.

O desempenho de um planejador pode ser medido basicamente de duas formas. A primeira refere-se à eficiência na resolução de problemas, ou seja, se o planejador consegue ou não encontrar um plano que resolva um problema de planejamento. A segunda maneira refere-se à eficácia na geração do plano, ou seja, o tempo que o planejador levou para gerar um plano e a qualidade do plano gerado (medida em número de ações que compõe um plano – quanto menor, melhor).

Um sistema de planejamento necessita de uma apresentação do estado inicial do mundo, um objetivo e uma descrição das ações que podem ser realizadas. Realizar o planejamento para atingir o objetivo significa encontrar uma seqüência de ações que, quando executada, fará com que o executor do plano alcance esse objetivo. Assim, partindo de um estado inicial, o sistema de planejamento percorre os estados possíveis de um domínio através da execução de ações para alcançar um estado objetivo.

Um domínio é uma representação de uma situação ou processo do mundo real. Segundo Vaquero (2007, p. 13), esta representação é composta por “ações (com suas pré-condições e efeitos), restrições, recursos disponíveis, os objetos, os objetivos a serem atingidos (eventualmente com critérios de otimização) e o estado inicial de um problema de planejamento”.

Pode-se realizar um planejamento a partir de diversos domínios. As formas conhecidas de planejamento são (GHALLAB, NAU e TRAVERSO, 2004):

Planejamento de caminho e movimentação;

Planejamento de percepção;

Planejamento para recuperação de informação;

Planejamento de navegação;

Planejamento de manipulação;

Planejamento de comunicação.

A figura 1 ilustra o modelo conceitual de um sistema de planejamento simples. Este modelo é composto por um planejador, por um controlador e por um sistema de transição de estados.

Figura 1 - Modelo conceitual de um sistema de planejamento simples

Fonte: Autor “adaptado de” (GHALLAB, NAU e TRAVERSO, 2004, p. 9).

O sistema de transição de estados executa uma função de transição com base em eventos e ações, simulando a mudança de estados de acordo com os efeitos dessas ações. O controlador recebe do sistema de transição o estado atual do domínio e executa ações de acordo com o plano fornecido pelo planejador. Para gerar este plano, o planejador recebe como entrada uma descrição de estados do domínio, um estado inicial e um estado objetivo.

A grande parte das pesquisas na área de planejamento automático está voltada para os sistemas clássicos de planejamento. Sistemas clássicos de planejamento consideram a geração de planos a partir da representação das características mais importantes de um domínio e que o sucesso do planejamento não é afetado por mudanças neste domínio (YANG, 1997).

A proposta desta dissertação considera apenas os sistemas clássicos de planejamento e, conseqüentemente, suas suposições restritivas (GHALLAB, NAU e TRAVERSO, 2004):

Finito: o espaço de estados é finito;

Observável: o domínio é totalmente observável;

Determinístico: cada ação ou evento tem apenas uma saída possível;

Estático: nenhuma mudança ocorre, exceto aquelas efetuadas pelo controle;

Objetivos restritos: o objetivo é uma seqüência de transições de estados;

Planos seqüenciais: a solução é uma seqüência de ações ordenadas de forma linear;

Tempo implícito: as ações do domínio são executadas instantaneamente;

Planejamento off-line: a situação da execução do plano não é conhecida pelo planejador.

O primeiro planejador foi criado no início da década de 1970. O planejador STRIPS (Stanford Research Institute Planning System) (FIKES e NILSSON, 1971) foi projetado para ser utilizado como sistema de planejamento do robô Shakey (NILSSON, 1984), dando a ele a capacidade de “raciocinar” sobre suas próprias ações.

O STRIPS possui uma estrutura de controle global baseado no GPS (General Problem Solver) (NEWELL, SHAW e SIMON, 1959), um sistema de busca no espaço de estados que utiliza análise de meios-fins para encontrar soluções para vários tipos de problemas. A partir do STRIPS, os planejadores passaram a ser desenvolvidos com a intenção de descrever estados de um domínio ou mundo (TONIDANDEL, 2003). Este planejador marcou o início da era clássica do planejamento automático, que durou até o fim dos anos 90 (GHALLAB, NAU e TRAVERSO, 2004).

Porém, o STRIPS apresentava algumas deficiências, principalmente por considerar que os sub-objetivos de um plano são independentes. Então, foram criados os planejadores ABSTRIPS (SACERDOTI, 1974) e NOAH (SACERDOTI, 1977), que introduziram o conceito de planejamento hierárquico – HTN (Hierarchical Task Network).

O planejador NOAH utilizava planejamento não-linear, o que lhe permitia tratar a dependência entre sub-objetivos de um plano. A partir do NOAH, Tate criou o planejador NONLIN (TATE, 1977), com a intenção de melhorar a qualidade dos planos gerados utilizando backtracking, descrições mais formais das ações de um domínio (“task formalism”) e introduzindo operadores para alterar planos já construídos (TONIDANDEL, 2003).

Durante os anos 80 foram criados outros planejadores, como o SIPE (WILKINS, 1983), TWEAK (CHAPMAN, 1987), PRODIGY (MINTON, 1988) e ABTWEAK (YANG e TENENBERG, 1990). Entretanto, nenhum deles apresentava técnicas mais eficientes e eficazes para resolver problemas genéricos de planejamento.

No início dos anos 90, surgiram os planejadores O-PLAN (CURRIE e TATE, 1991), SNLP (MCALLESTER e ROSENBLITT, 1991), POP (BARRET e WELD, 1992) e UCPOP (PENBERTHY e WELD, 1992), ainda baseados nas técnicas utilizadas pelo STRIPS e no planejamento hierárquico, porém impulsionados pela criação ADL (Action Description Language) (PEDNAULT, 1989). A ADL é uma linguagem de representação de domínios que estende a descrição de ações do STRIPS, permitindo, por exemplo, representar condições e quantificadores universais sobre os objetos de um domínio.

Em 1992, Kaltz e Selman criaram o SATPLAN (SELMAN e KAUTZ, 1992), um planejador que traduz o problema de planejamento em um problema de satisfabilidade, resolvendo-o de acordo com as técnicas SAT (SELMAN, LEVESQUE e MITCHELL, 1992) (SELMAN, KAUTZ e COHEN, 1994).

Em 1995, Blum e Furst criaram o Graphplan (BLUM e FURST, 1995). O Graphplan constrói um grafo a partir de uma descrição STRIPS. A construção deste grafo, que acontece a partir do estado inicial do problema, reduz a representação do espaço de busca do problema tratando os conflitos entre as ações do domínio. A eficiência, eficácia e simplicidade do Graphplan estimularam a pesquisa e o desenvolvimento de novas técnicas de planejamento, dando início à era neoclássica do planejamento automático (GHALLAB, NAU e TRAVERSO, 2004).

Em 1998, Bonet e Geffner (BONET e GEFFNER, 1998) criaram o planejador HSP (Heuristic Search Planning), que é um planejador baseado em busca heurística. O HSP utiliza o grafo e o algoritmo do caminho mínimo de Dijkstra (DIJKSTRA, 1959), determinando o valor da heurística de cada nó através do algoritmo A* (HART, NILSSON e RAPHAEL, 1972).

Em 1999, Kautz e Selman criaram o Blackbox (KAUTZ e SELMAN, 1999), um planejador que utiliza a técnica do SATPLAN e do Graphplan em conjunto.

Em 2000, Hoffmann e Nebel criaram o planejador FF (Fast-Forward) (HOFFMANN e NEBEL, 2001), considerado o melhor sistema de planejamento até então. O FF utiliza o Graphplan, porém a heurística é calculada de forma mais detalhada, através de um plano relaxado. A busca heurística é feita através do algoritmo Enforced Hill-climbing ao invés do A*.

Em 2002, foram criados os planejadores LPG (GEREVINI e SERINA, 2002), que utiliza as técnicas do Graphplan em conjunto com busca heurística, e o METRIC-FF (HOFFMANN, 2002), uma evolução do planejador FF que trata restrições numéricas e funções de otimização.

Em 2004, Helmert criou o FAST DOWNWARD (HELMERT, 2006), que utiliza decomposição hierárquica de tarefas de planejamento para computar sua função heurística, diferente dos algoritmos baseados no HSP. Também foi criado o SGPLAN (CHEN, HSU e WAH, 2004), que cria plano dividindo um problema para resolvê-lo em partes.

Em 2006, último ano do período que compreende o surgimento dos domínios e planejadores estudados nesta dissertação, foi criado o MAXPLAN (XING, CHEN e ZHANG, 2006). Este planejador utiliza a exclusão mútua (ações de um plano que são conflitantes e que não podem ocorrer juntas) de longa distância (londex) para melhorar o processo de geração de planos.

## Competições internacionais de planejamento

Um grande estímulo para a criação e evolução dos planejadores da era neoclássica do planejamento automático veio das competições internacionais de planejamento. Essa competição coloca a prova sistemas de planejamento e suas técnicas, propondo a resolução de problemas em diversos tipos de domínios.

Como os resultados dessas competições internacionais de planejamento serviram de subsídio e incentivo para a proposta apresentada neste trabalho, foi realizada uma análise mais detalhada dos resultados de cada uma das competições.

Na primeira edição da competição internacional de planejamento, realizada em 1998, foram realizadas três rodadas (rounds) de planejamento. Os planejadores IPP e SGP competiram em domínios modelados em ADL. Quatro planejadores, Blackbox, HSP, IPP, e STAN competiram em domínios modelados em STRIPS.

Nos resultados desta competição (MCDERMOTT, 2008), ficou constatado que os dois sistemas de planejamento vencedores foram o IPP e o Blackbox. Entretanto, é importante ressaltar alguns fatos observados e analisados nos resultados de cada round.

No primeiro round, com domínios modelados em ADL, o planejador IPP venceu o planejador SGP em quase todos os problemas propostos nos domínios Gripper, Logistics, Movie, Mprime e Mystery. Porém, no problema MOVIE-X-5, o planejador SGP foi melhor do que o IPP, obtendo um plano do mesmo tamanho (sete passos) na metade do tempo (dez segundos).

Já no primeiro round com domínios modelados em STRIPS, o planejador HSP somou o maior número de pontos. Porém, em vários problemas nos domínios Assembly, Gripper, Logistics, Movie, Mprime e Mystery, o HSP foi superado por outros planejadores. Em problemas do domínio Gripper, o planejador HSP obteve seus melhores resultados. Entretanto, nos problemas STRIPS-GRIPPER-X-1 e STRIPS-GRIPPER-X-2 o planejador ficou na última e penúltima colocação, respectivamente.

No segundo round com domínios modelados em STRIPS, o grande vencedor foi o planejador IPP. Porém, apesar de ter somado mais pontos em relação aos outros planejadores, nos problemas do domínio Grid, este planejador não conseguiu gerar nenhum plano.

Dois anos depois, em 2000, na segunda competição internacional de planejamento (BACCHUS, 2000), participaram quinze sistemas de planejamento. Os resultados desta competição foram obtidos através de duas medidas: tempo de geração do plano e número de passos do plano gerado. Os sistemas de planejamento que se destacaram foram o FF e o System R.

No entanto, esses dois sistemas de planejamento tiveram comportamentos diferentes, em diferentes domínios. No domínio Logistics World, o planejador FF foi mais rápido, enquanto o planejador System R gerou planos num tempo consideravelmente maior. O gráfico da figura 2, divulgado nos resultados da competição, mostra essa diferença de desempenho entre os planejadores:

Figura 2 – Comparação de tempo para geração de planos no Logistics World.

Fonte: (BACCHUS, 2000)

Entretanto, no gráfico da figura 3, é fácil notar que o planejador System R apresentou um excelente desempenho no domínio do mundo de blocos, gerando planos num tempo razoável de acordo com o crescimento da dificuldade do problema. Em contrapartida, o planejador FF não conseguiu resolver alguns problemas no mesmo domínio, apesar de ter sido mais rápido nos problemas que conseguiu resolver.

Figura 3 – Comparação de tempo para geração de planos no Blocks World.

Fonte: (BACCHUS, 2000)

Apesar do planejador FF não ter conseguido gerar planos para todos os problemas propostos no mundo de blocos, os planos gerados por ele foram similares aos planos gerados pelo planejador System R. O gráfico da figura 4 mostra o número de passos que cada plano gerado contêm:

Figura 4 – Comparação do número de passos dos planos gerados no Blocks World.

Fonte: (BACCHUS, 2000)

Já na terceira edição da competição internacional de planejamento, realizada em 2002, os planejadores que obtiveram os melhores resultados foram o FF, LPG e o MIPS. Nos resultados desta competição (FOX e LONG, 2002), observou-se um equilíbrio um pouco maior na eficiência dos planejadores. O planejador FF foi o mais rápido na maior parte dos domínios, seguido sempre pelo LPG neste quesito de desempenho.

O gráfico da figura 5 mostra uma comparação do tempo que cada sistema de planejamento levou para gerar planos no domínio Depots. Para um número pequeno de instâncias, o planejador FF levou um tempo maior para gerar os planos, enquanto os planejadores LPG e Simplanner foram mais rápidos. Porém, para um número maior de instâncias dentro do domínio, o FF mostrou um desempenho melhor em relação aos outros planejadores.

Figura 5 – Comparação do tempo para geração de planos no domínio Depots.

Fonte: (FOX e LONG, 2002)

No domínio DriverLog, conforme mostra o gráfico da figura 6, o planejador FF teve um desempenho melhor que os outros planejadores até um certo número de instâncias (12). A partir deste ponto, o planejador LPG obteve um melhor desempenho, conseguindo também gerar planos para problemas com 17 e 18 instâncias, o que não aconteceu com o FF.

Figura 6 – Comparação do tempo para geração de planos no domínio DriverLog.

Fonte: (FOX e LONG, 2002)

Em 2004, foi realizada a quarta competição internacional de planejamento (EDELKAMP, HOFFMANN e LITTMAN, 2004). Os sistemas de planejamento que mais se destacaram foram: Fast Downward / Fast Diagonally Downward, YAHSP, SGPlan, LPG-TD, SATPLAN04 e CPT. Porém, os resultados desta competição também apresentaram características peculiares entre planejadores e domínios.

Figura 7 – Comparação de tempo para geração de planos no domínio Pipesworld.

Fonte: (EDELKAMP, HOFFMANN e LITTMAN, 2004)

No domínio Pipesworld, por exemplo, os planejadores Fast Downward / Fast Diagonally Downward foram mais eficientes na geração de planos do que o planejador LPG, conforme ilustra o gráfico da figura 7.

Na quinta edição da competição internacional de planejamento (GEREVINI, BONET e GIVAN, 2006), realizada em 2006, os planejadores que obtiveram melhor desempenho foram: SATPLAN, MAXPLAN e SGPLAN5. Assim como nas outras competições, também foi notado um comportamento diferente entre planejadores e domínios nos resultados da competição.

O gráfico da figura 8 mostra o comportamento dos planejadores no domínio TPP. Neste domínio, em 30 problemas, o planejador SATPLAN conseguiu resolver 24 problemas. Já o planejador MAXPLAN conseguiu resolver apenas 15 problemas. Da mesma forma, no gráfico da figura 9, em 30 problemas do domínio Pathways, o planejador MAXPLAN resolveu 15 problemas, enquanto o planejador SATPLAN resolveu apenas 9 problemas. Nesses dois domínios proposicionais, esses dois planejadores foram os que obtiveram os melhores resultados.

Figura 8 – Comparação de tempo para geração de planos no domínio TPP.

Fonte: (GEREVINI, BONET e GIVAN, 2006)

Figura 9 – Comparação de tempo para geração de planos no domínio Pathways.

Fonte: (GEREVINI, BONET e GIVAN, 2006)

A análise dos gráficos dos resultados mostra que, mesmo com novas técnicas, evolução dos planejadores já existentes, novos planejadores e a utilização de novos domínios nas competições internacionais de planejamento, a eficiência dos planejadores em resolver problemas de planejamento continua apresentando comportamento peculiar.

Além da influência dos domínios, a eficiência destes planejadores está relacionada com as técnicas utilizadas por eles para a criação dos planos. Essas técnicas caracterizam o processo de planejamento e representam o método para a criação automática de planos.

## Técnicas de planejamento

Do STRIPS até os planejadores mais recentes, como o FF e o MAXPLAN, diversas técnicas e estratégias de planejamento foram criadas. Sozinhas ou utilizadas em conjunto, essas técnicas foram concebidas e aprimoradas com um único intuito: gerar planos com eficiência, eficácia e em menos tempo.

De forma geral, essas técnicas estão relacionadas com o tipo de estrutura utilizada para representar o espaço de busca, com o conteúdo que forma o espaço de busca, com a direção de navegação (do estado inicial para o final ou do estado final para o inicial), estratégias e heurísticas usadas nas buscas e com a forma que o plano é construído durante o processo de planejamento.

O planejamento automático é essencialmente um problema de busca. Decidir como representar o espaço de busca é fundamental para facilitar a geração de planos.

Sistemas de planejamento que utilizam técnicas de representação Graph-based (baseada em grafos) constroem um grafo onde os nós são os estados do domínio e as arestas representam as ações que fazem a transição entre estados (BLUM e FURST, 1995). Se existir um plano que resolva o problema de planejamento, este será um sub-grafo do grafo construído.

Este grafo pode ser construído de duas maneiras. Planejadores state-space criam uma árvore de busca onde os nós e folhas (vértices) são estados do domínio e os ramos (arestas) são as ações que fazem a transição entre estados. Em contra partida, nos planejadores plan-space, os nós e folhas (vértices) da árvore de busca são planos parciais e os ramos (arestas) são procedimentos de refinamento desses planos (TONIDANDEL, 2003).

Existem também sistemas de planejamento que utilizam decomposição hierárquica de tarefas em sub-tarefas (Hierarchical Task Network - HTN), refinando o plano inicial para facilitar a busca pelo plano final. Neste trabalho são considerados apenas planejadores que não necessitam de uma representação hierárquica das tarefas de um domínio, mas que determinam a hierarquia das tarefas durante o processo de planejamento.

Já planejadores SAT-based, convertem um problema de planejamento em um problema de satisfabilidade, encontrando primeiro uma solução para este problema e depois convertendo novamente o resultado para gerar um plano (KAUTZ, SELMAN e HOFFMANN, 2006).

Em relação à forma como o plano é construído durante o processo de planejamento, existem duas técnicas. Um planejador de ordem total (total-order) não altera o plano já construído durante a execução do planejamento. As ações que já foram planejadas e seqüenciadas não são alteradas até o fim do planejamento. Novas ações podem ser adicionadas apenas no início ou no final do plano. Esta abordagem pode impedir que uma solução, ou as melhores soluções, sejam encontradas (TONIDANDEL, 2003).

Por outro lado, um planejador de ordem parcial (partial-order) insere, retira ou troca a ordem de ações de um plano enquanto o constrói. Essa capacidade é proporcionada pela lógica causal que relaciona as ações. Diferente dos sistemas de ordem total, onde as ações são seqüenciais, o sistema de planejamento de ordem parcial constrói um plano que é formado por passos (ações) e seus vínculos causais. Segundo Tonidandel (2003), “esses vínculos garantem que sub-objetivos satisfeitos permaneçam satisfeitos durante o restante do planejamento e do refinamento do plano parcial que está sendo construído”.

Também existem duas técnicas de geração de plano relacionadas a direção de navegação no espaço de busca. Sistemas de planejamento que utilizam forward-chaining (HOFFMANN e NEBEL, 2001) têm como estratégia de geração de plano executar ações a partir de um estado inicial, gerando novos estados até alcançar o estado objetivo. Já os planejadores que utilizam backward-chaining (LIN, 2001) partem da solução do problema (estado objetivo) e tentam descobrir as possíveis ações que levaram até aquele estado, definindo estados anteriores até atingir o estado inicial do problema.

Muitos planejadores utilizam busca heurística (heuristic search) para tornar o processo de descoberta de um plano mais rápido. Como foi visto, os planejadores HSP  (BONET e GEFFNER, 1998) e FF  (HOFFMANN e NEBEL, 2001) utilizam os algoritmos de busca heurística A* e Enforced Hill-climbing, respectivamente, para encontrar um plano direcionando a busca dentro de um espaço de estados possíveis.

Para finalizar essa relação das principais técnicas de planejamento, é importante citar também os planejadores knowledge-based (VIDAL, 2002), que utilizam qualquer conhecimento prévio de um domínio para resolver o problema de planejamento. Esse conhecimento pode incluir tarefas e estruturas de objetivos, vários tipos de restrições, técnicas de controle de busca e até interação com os seres humanos, quando necessário, para fazer uso de seus conhecimentos.

## Modelagem de domínios

Outra perspectiva determinante para o sucesso dos sistemas de planejamento é a representação do domínio e do problema a ser resolvido. Um domínio, que nada mais é do que uma representação do mundo real, pode ser descrito através de STRIPS, ADL, PDDL e UML. As duas últimas linguagens são detalhadas a seguir por serem as mais utilizadas e por fazerem parte do escopo desta pesquisa.

### PDDL

A linguagem de representação de domínios utilizada pelo STRIPS mostrou-se ineficiente para representar alguns domínios reais e proporcionou o surgimento de diversas outras linguagens de planejamento, como a ADL (TONIDANDEL, 2003). Essas linguagens possuem recursos mais poderosos para representar domínios, porém criaram outro problema: um domínio poderia ser representado de diversas formas, tornando difícil a avaliação de técnicas de planejamento.

Para resolver o problema de padronização de representação de domínios e também das restrições impostas pelo STRIPS, em 1998 foi criada a linguagem PDDL (Planning Domain Definition Language) (MCDERMOTT, GHALLAB, et al., 1998).

Figura 10 – O domínio mundo de blocos representado através da PDDL.

Fonte: Autor

A PDDL tem como principal objetivo representar um domínio através de uma estrutura que permita que este possa ser interpretado por um sistema de planejamento. Segundo Tonidandel (2003), a PDDL apresenta as seguintes características:

Representação direcionada às ações do domínio;

Representação de ações baseadas no modelo STRIPS;

Representação de efeitos condicionais nas ações, bem como qualificadores e quantificadores universais (características da linguagem ADL);

Definição de restrições;

Especificação de ações hierárquicas compostas por sub-ações.

A representação de um domínio em PDDL é feita em duas partes. Na primeira parte está a definição do domínio e as ações possíveis no domínio, bem como a declaração dos tipos de objetos existentes. Na segunda parte estão as definições do problema de planejamento, dos estados iniciais e do objetivo a ser alcançado. A figura 10 exemplifica o uso da PDDL na modelagem do domínio do mundo de blocos. A codificação na coluna esquerda da figura representa o domínio como todo, com seus objetos e ações. Na coluna direita da figura 10, está a codificação de um problema deste domínio, onde existem três blocos.

Por ser uma linguagem padronizada, a representação de um domínio em PDDL possibilita que planejadores diferentes possam tratar o mesmo problema de planejamento. Isso propicia a comparação das técnicas e algoritmos de planejamento. Por essa razão, a PDDL é a linguagem de representação de domínios utilizada nas competições internacionais de planejamento.

### UML

A UML (Unified Modeling Language – linguagem de modelagem unificada) é uma linguagem de propósito geral para a especificação, visualização, construção e documentação de artefatos de sistemas complexos de software (RUMBAUGH, BOOCH e JACOBSON, 2006). A representação através da UML facilita a compreensão de um domínio ou processo a ser automatizado por um software.

Dentre os principais objetivos da UML, segundo a OMG (Object Modeling Group), está a possibilidade de fornecer ao usuário uma linguagem visual expressiva no desenvolvimento de modelos de negócio, mecanismos para extensões e mecanismos de especialização para apoiar os conceitos essenciais de um domínio. A UML apresenta três tipos básicos de blocos (RUMBAUGH, BOOCH e JACOBSON, 2006):

Itens: representam elementos comportamentais e estruturais;

Relacionamentos: especificam como os itens estão ligados;

Diagramas: agrupam coleções de itens e relacionamentos.

A UML, na versão 2.0, é formada por treze diagramas: diagrama de classes, diagrama de objetos, diagrama de componentes, diagrama de estruturas compostas, diagrama de casos de uso, diagrama de seqüências, diagrama de comunicações, diagrama de gráficos de estados, diagrama de atividades, diagrama de implantação, diagrama de pacote, diagrama de temporização e diagrama de visão geral da interação.

Entre esses diagramas, podemos destacar alguns que são importantes na representação de domínios de planejamento: diagrama de casos de uso, diagrama de classes, diagrama de objetos e diagrama de estados.

O diagrama de classes representa as entidades, mostrando os atributos (características) e métodos (ações) de cada classe de objeto que compõe um determinado domínio. Além disso, mostra o relacionamento entre essas classes, como por exemplo: composição (quando uma entidade é composta por outras entidades), agregação (quando uma entidade agrega outras entidades), dependência (quando a existência de uma entidade está condicionada a existência de outra entidade) e herança (quando uma entidade filha herda características e ações de uma entidade mãe) (LARMAN, 2007).

O diagrama de classes representa o aspecto estático de um domínio, mostrando as classes de objetos que o formam.

Figura 11 – Diagrama de classes do mundo de blocos.

Fonte: Autor

A figura 11 mostra o diagrama de classes do domínio mundo de blocos. Existem três classes de objetos: bloco, mesa e garra. Existe um relacionamento de agregação entre o bloco e a mesa, indicando que os blocos podem ser agregados sobre a mesa. Existe também uma relação de agregação entre os blocos, indicando que os blocos podem ser empilhados. Por fim, existe uma relação de associação simples entre a garra e o bloco, indicando que uma garra pode segurar um bloco.

O diagrama de objetos mostra uma determinada situação (snapshot) da execução de um domínio.  Este diagrama apresenta os objetos (instâncias das classes), mostrando os valores de seus atributos (estado) num determinado instante de tempo (RUMBAUGH, BOOCH e JACOBSON, 2006). É um diagrama que representa o aspecto dinâmico de um domínio, dado que está condicionado ao tempo. A estrutura deste diagrama, os objetos e seus relacionamentos respeitam as definições feitas no diagrama de classes.

A figura 12 mostra o diagrama de objetos do domínio mundo de blocos num determinado instante. Este diagrama indica que existem três blocos (A, B e C), uma garra e uma mesa. O bloco B está sobre a mesa e o bloco A está sobre o bloco B. A garra está segurando o bloco C.

Figura 12 – Diagrama de objetos do mundo de blocos.

Fonte: Autor

O diagrama de casos de uso mostra como os atores (agentes) atuam dentro de um domínio, relacionando-os com conjuntos de ações (casos de uso) que podem executar ou usufruir (LARMAN, 2007). Este diagrama também apresenta a relação entre os casos de uso, como por exemplo: inclusão (quando a execução de um caso de uso está condicionada obrigatoriamente a execução de outro caso de uso), extensão (quando a execução de um caso de uso pode ocasionar ou não a execução de outro caso de uso a partir de um ponto de extensão), dependência (a execução de um caso de uso depende de algum outro caso de uso) e herança (um caso de uso herda características de outro caso de uso).

O diagrama de casos de uso também representa o aspecto estático do domínio, porém do ponto de vista dos atores. A figura 13 representa o diagrama de casos de uso do domínio mundo de blocos. É simples notar que a Garra, que representa o agente atuante dentro do domínio, pode executar apenas quatro ações, por isso está relacionada com os quatro casos de uso.

Figura 13 – Diagrama de casos de uso do mundo de blocos.

Fonte: Autor

O diagrama de estados mostra todos os estados possíveis que um determinado objeto pode apresentar dentro do domínio. O estado (valores dos atributos) de um objeto é alterado a partir da execução de eventos e ações do domínio (RUMBAUGH, BOOCH e JACOBSON, 2006). O diagrama de estados é um grafo que representa uma máquina de estados, mostrando através de uma baixa granularidade a execução de ações no domínio.

Figura 14 – Diagrama de estados (objeto Garra) do mundo de blocos.

Fonte: Autor

A figura 14 mostra os estados em que a garra pode estar dentro do domínio mundo de blocos. A garra pode estar livre ou segurando um bloco. Dependendo das ações que são executadas pela garra, esses estados alternam.

A partir do trabalho de Vaquero (2007), comprovou-se que a UML satisfaz o processo de especificação e modelagem de domínios de problemas reais e complexos. Através de seus diagramas de representação estática ou dinâmica, a UML fornece um nível de abstração suficiente para a análise de requisitos e a modelagem de domínios de planejamento.

Neste mesmo trabalho, encontra-se a definição de uma extensão da UML para a representação de domínios de planejamento, denominada “UML.P”. Vaquero (2007) esclarece que “devido ao fato da UML ser de propósito geral, algumas características intrínsecas aos domínios de planejamento devem ser levadas em consideração no uso desta linguagem”. Desta forma, algumas alterações foram feitas nas representações dos itens e diagramas da UML para se adequarem ao planejamento automático.

A UML.P foi implementada e utilizada no itSIMPLE (integrated tools Software Interface for Modeling PLanning Environments) (VAQUERO, 2007). O itSIMPLE é um software que permite que um domínio de planejamento seja modelado através da UML. De acordo com o site do projeto (itSIMPLE Project, 2008), “o software itSIMPLE é uma ferramenta de engenharia do conhecimento para modelar domínios de planejamento. Esta ferramenta foi projetada para dar suporte a usuários durante a construção de um domínio de planejamento, principalmente nas fases iniciais do ciclo de vida de um projeto”.

O itSIMPLE ainda permite a exportação do domínio modelado em UML.P para a linguagem PDDL e Redes de Petri. Desta forma, cria-se uma ponte entre a modelagem de domínio em UML e sua utilização na criação de planos por diversos sistemas de planejamento através da PDDL.

A representação do modelo do domínio em UML é armazenada em um arquivo XML (extensible markup language), permitindo assim que o domínio possa ser interpretado de forma estruturada por uma ferramenta de análise de domínio. O itSIMPLE é uma ferramenta que possui o código-fonte aberto, desenvolvido na plataforma JAVA.

Os diagramas de casos de uso, classes e estado do domínio mundo de blocos aparecem modelados em UML.P dentro da ferramenta itSIMPLE nas figuras 15, 16 e 17 respectivamente. Essas figuras possuem o mesmo significado das figuras do domínio do mundo de blocos modelados em UML.

Figura 15 – Diagrama de casos de uso do mundo de blocos modelado no itSIMPLE.

Fonte: Autor

Figura 16 – Diagrama de classes do mundo de blocos modelado no itSIMPLE.

Fonte: Autor

Figura 17 – Diagrama de estados (objeto garra) do mundo de blocos modelado no itSIMPLE.

Fonte: Autor

## Trabalhos relacionados

Existem algumas pesquisas que tentaram criar algumas classificações e taxonomias relacionadas ao espaço de busca dos domínios e às heurísticas utilizadas para encontrar planos válidos nesses domínios. Nestes estudos, os domínios são representados pelos planejadores na forma de grafos (vértices e arestas). Esta representação pode criar estruturas cíclicas, mínimas locais e caminhos sem retorno, que afetam diretamente o cálculo da heurística feita pelos planejadores.

Hoffman (2001) analisou a topologia do domínio em que a busca local está sendo aplicada e o desempenho da heurística utilizada em espaços de busca com mínima local, contornos e bancos (local minima, contours and benches). A partir desta análise, criou uma taxonomia para domínios de planejamento, classificando-os em indireto, inofensivo, reconhecido e não reconhecido (undirected, harmless, recognized and unrecognized), de acordo com o impacto causado no desempenho de planejadores heurísticos. Entretanto, esta análise só foi feita para as heurísticas utilizadas nos planejadores FF e HSP.

Gerevini, Saetti e Serina (2004) fizeram um estudo experimental para compreender e avaliar o impacto das funções heurísticas no desempenho do planejador LPG. A partir desta avaliação, algumas técnicas foram propostas para restringir a busca pela vizinhança no algoritmo Walkplan. Uma análise das principais características heurísticas também foi feita com o intuito de compreender o impacto da busca local no planejador LPG.

# Planejadores

Este trabalho propõe criar uma relação entre características de domínio e técnicas de planejamento. Para isso, foi preciso selecionar alguns planejadores que implementam as técnicas estudadas.

De acordo com os resultados dessas competições, disponibilizados em (MCDERMOTT, 2008), (BACCHUS, 2000), (FOX e LONG, 2002), (EDELKAMP, HOFFMANN e LITTMAN, 2004) e (GEREVINI, BONET e GIVAN, 2006), os planejadores vencedores de cada edição estão relacionados na tabela 1.

Tabela 1 – Planejadores com melhor desempenho nas competições internacionais de planejamento.

[[TABELA 01: 6 linhas x 3 colunas]]
| Competições | Ano | Planejadores |
| IPC98 | 1998 | Blackbox (Henry Kautz e Bart Selman) IPP (Jana Koehler) |
| IPC2000 | 2000 | FF (J. Hoffmann) System R (Fangzhen Lin) |
| IPC2002 | 2002 | FF (J. Hoffmann) LPG (A. Gerevini, A. Saetti, I. Serina e P. Tonelli) |
| IPC2004 | 2004 | Fast Downward (Malte Helmert e Silvia Richter) Fast Diagonally Downward (Malte Helmert e Silvia Richter) YAHSP (Vincent Vidal) SGPlan (Yixin Chen, Chih-Wei Hsu e Benjamin W. Wah) LPG-TD (A. Gerevini, A. Saetti, I. Serina e P. Tonelli) SATPLAN04 (H. Kautz, D. Roznyai, F. Teydaye-Saheli, S. Neph, e M. Lindmark) CPT (Vincent Vidal e Hector Geffner) |
| IPC2006 | 2006 | MAXPLAN (Zhao Xing, Yixin Chen e Weixiong Zhang) SGPlan5 (Benjamin W. Wah, Chih-Wei Hsu, Yixin Chen e Ruoyun Huang) SATPLAN06 (Joerg Hoffmann, Henry Kautz, Shane Neph e Bart Selman) |

Fonte: Autor

Os planejadores selecionados foram aqueles que obtiveram os melhores resultados nas competições internacionais de planejamento: Blackbox, IPP, FF, System R, LPG, Fast Downward, YAHSP, SGPLAN, SATPLAN e MAXPLAN.

## Planejadores selecionados

O Blackbox (KAUTZ e SELMAN, 1998) é um sistema de planejamento que funciona convertendo problemas de planejamento especificados em STRIPS em problemas de satisfabilidade, e então resolve esses problemas utilizando os melhores sistemas de satisfabilidade. Utiliza grafos de planos (GraphPlan) e oferece a possibilidade da escolha do sistema de satisfabilidade para a resolução do problema.

Seu funcionamento é divido em duas partes: primeiro é construído um grafo de planos para reduzir o espaço de busca do problema e então este grafo é traduzido para uma instância SAT. Depois, na segunda parte, um solucionador SAT (SAT-Solver) é aplicado para obter o plano que resolve o problema.

O planejador IPP (KOEHLER, 1998) é um sistema de planejamento baseado no sistema de grafos de planos (GraphPlan) que utiliza verificação de tipos para aperfeiçoar o processo de busca pela solução.

O sistema de planejamento heurístico FF (Fast-Forward) (HOFFMANN e NEBEL, 2001) é baseado no sistema de planejamento HSP e utiliza a representação do domínio em grafos de planos para encontrar uma heurística melhor, utilizando o algoritmo de busca Enforced Hill-climbing.

O planejador System R (LIN, 2001) é baseado no sistema de planejamento STRIPS. A partir de um conjunto de objetivos simples, ele seleciona um objetivo para trabalhar. Se existe uma ação que se executada atinja esse objetivo, então ela é executada e o planejador seleciona um novo objetivo simples. Senão, um novo conjunto de objetivo é computado baseado nas ações que tem este objetivo simples com um de seus efeitos, e recursivamente tenta atingir o novo objetivo. Esse processo continua até que o objetivo original seja alcançado.

O LPG (Local search for Planning Graphs) (GEREVINI e SERINA, 2002) é um planejador baseado em busca local e grafos de planos (GraphPlan) que manipula domínios que envolvem quantidades numéricas e ações com duração ou não instantâneas. O LPG pode resolver problemas de geração ou adaptação de planos.

O funcionamento básico da busca deste planejador foi inspirado no Walksat, um procedimento eficiente para resolver problemas de satisfabilidade. O espaço de busca consiste em “grafos de ações”, um sub-grafo do grafo de planos que representa planos parciais.

O Fast Downward (HELMERT, 2006) é um sistema clássico de planejamento baseado em busca heurística. É capaz de lidar com problemas de planejamento determinísticos (onde todas as ações e suas conseqüência são conhecidas) em domínios modelados na linguagem PDDL 2.2, incluindo recursos avançados semelhantes as condições da linguagem ADL, efeitos e predicados derivados (axiomas).

Assim como os planejadores HSP e FF, o Fast Downward é um planejador progressivo. Entretanto, este sistema não utiliza a representação proposicional da PDDL para orientar o plano de tarefas diretamente. Em vez disso, a entrada é traduzida primeiro em uma representação alternativa chamada de planejamento de tarefas multivalorado, o que torna explícita muitas das restrições implícitas de um plano de tarefas proposicional.

Explorando essa alternativa de representação, o Fast Downward utiliza decomposição hierárquica de tarefas de planejamento para computar sua função heurística, chamada de “causal graph heuristic”, que é diferente das heurísticas utilizadas nos algoritmos baseados no HSP.

O YAHSP (Yet Another Heuristic Search Planner) (VIDAL, 2002) é um sistema de planejamento baseado no HSP, onde a heurística é computada de maneira similar ao planejador FF, mas utilizada de maneira diferente. Foi introduzida uma nova maneira para extrair informações a partir do cálculo da heurística, considerando planos de alta qualidade computados por funções heurísticas em vários domínios.

O planejador SGPLAN (CHEN, HSU e WAH, 2004) é um sistema de planejamento que divide um problema de planejamento em sub-problemas, cada um com seu próprio sub-objetivo, resolvendo eventuais conflitos entre as soluções parciais. Os sub-problemas são ordenados de forma que os mais difíceis são resolvidos primeiro.

O SATPLAN (KAUTZ, SELMAN e HOFFMANN, 2006) é um sistema de planejamento que constrói um grafo de planos, traduzindo as restrições em um conjunto de cláusulas SAT, onde cada instância específica de uma ação ou fato em um ponto do tempo é uma proposição.

Usando um solucionador SAT geral ele tenta encontrar uma solução que satisfaça as cláusulas. Por fim, através do processo inverso, traduz a solução SAT para o problema de planejamento original. Depois de encontrar a solução, ações desnecessárias são removidas do plano.

O MAXPLAN (XING, CHEN e ZHANG, 2006) é um sistema de planejamento similar ao SATPLAN. A diferença está no fato de que o MAXPLAN utiliza a exclusão mútua de longa distância (londex), uma generalização da exclusão mútua (mutex) utilizada no SATPLAN. Baseado em domínios multivalorados, o londex proporciona muito mais espaço de busca do que o mutex, uma vez que além de capturar restrições relacionadas a ações no mesmo passo da busca, pode também fazê-lo através de vários passos da busca.

## Planejadores versus técnicas de planejamento

Os planejadores selecionados utilizam mais de uma técnica para gerar planos. As tabelas 2 e 3 mostram a relação entre os planejadores selecionados e as técnicas utilizadas. O sinal “x” indica que um planejador utiliza uma determinada técnica. A tabela 4 consolida todas as técnicas de planejamento utilizadas por cada planejador.

Nesta pesquisa, os planejadores baseados em resolução de problemas de satisfabilidade são relacionados com a técnica Forward-chaining. Essa definição parte do princípio que esses planejadores sempre partem do estado inicial do problema de planejamento em busca do estado objetivo para criar a representação do problema em proposições SAT.

Tabela 2 – Relação entre planejadores e técnicas de planejamento.

[[TABELA 02: 12 linhas x 6 colunas]]
| Técnicas / Planejadores | Blackbox | IPP | FF | R | LPG |
| State-Space | x | x | x | x |  |
| Plan-Space |  |  |  |  | x |
| Partial-order |  |  |  | x | x |
| Total-order | x | x | x |  |  |
| Hierarchical |  |  |  |  |  |
| Forward-chaining | x | x | x | x | x |
| Backward-chaining |  |  |  | x |  |
| Graph-based | x | x | x |  | x |
| Knowledge-based |  |  |  |  |  |
| SAT-based | x |  |  |  |  |
| Heurist Search |  |  | x |  | x |

Fonte: Autor

Tabela 3 – Relação entre planejadores e técnicas de planejamento (cont.).

[[TABELA 03: 12 linhas x 6 colunas]]
| Técnicas / Planejadores | Fast Fownward | YAHSP | SGPlan | SATPlan | MAXPLAN |
| State-Space | x | x |  |  |  |
| Plan-Space |  |  | x | x | x |
| Partial-order |  |  | x | x | x |
| Total-order | x | x |  |  |  |
| Hierarchical | x |  |  |  |  |
| Forward-chaining | x | x | x | x | x |
| Backward-chaining |  |  |  |  |  |
| Graph-based |  | x |  | x | x |
| Knowledge-based |  | x |  |  |  |
| SAT-based |  |  |  | x | x |
| Heurist Search | x | x |  |  |  |

Fonte: Autor

Tabela 4 – Relação consolidada entre planejadores e técnicas de planejamento.

[[TABELA 04: 11 linhas x 2 colunas]]
| Planejadores | Técnicas de planejamento |
| Blackbox | State -Space, Total-order, Forward-chaining, Graph-based, SAT-based |
| IPP | State-Space, Total-order, Forward-chaining, Graph-based |
| FF | State-Space, Total-order, Forward-chaining, Graph-based, Heurist Search |
| R | State-Space, Partial-order, Forward-chaining, Backward-chaining |
| LPG | Plan-Space, Partial-order, Forward-chaining, Graph-based, Heurist Search |
| Fast Downward | State-Space, Total-order, Hierarchical, Forward-chaining, Heurist Search |
| YAHSP | State-Space, Total-order, Forward-chaining, Graph-based, Knowledge-based, Heurist Search |
| SGPlan | Plan-Space, Partial-order, Forward-chaining |
| SATPlan | Plan-Space, Partial-order, Forward-chaining, Graph-based, SAT-based |
| MAXPLAN | Plan-Space, Partial-order, Forward-chaining, Graph-based, SAT-based |

Fonte: Autor

# Domínios

Após selecionar os planejadores, foi necessário elencar os domínios dos quais algumas características seriam extraídas. Esses domínios deveriam ser modelados corretamente em UML.P e deveriam ser de propósitos diferentes, ou seja, representar situações diferentes do mundo real para propiciar uma comparação consistente de suas características.

Todos os domínios selecionados participaram das competições internacionais de planejamento. Esses domínios foram criados especificamente para validarem a eficiência e a eficácia dos planejadores e suas técnicas de planejamento. Portanto, selecionar domínios criados para essas circunstâncias significou optar por um conhecimento prévio qualificado utilizado para comparar planejadores, e seus respectivos comportamentos, através de diferentes características.

A qualidade da modelagem em UML.P dos domínios selecionados foi garantida com a ajuda da ferramenta itSIMPLE. Após modelar um domínio em UML.P, o itSIMPLE é capaz de gerar sua representação em PDDL. Os modelos criados foram validados comparando a representação em PDDL gerada pelo itSIMPLE com os arquivos PDDL dos domínios selecionados encontrados nas competições internacionais de planejamento.

## Domínios selecionados

Neste trabalho são considerados os domínios das competições internacionais de planejamento nos quais a eficiência e eficácia dos planejadores foi muito destoante, indicando que esses domínios possuem características que afetam o desempenho de determinadas técnicas de planejamento. Os domínios selecionados foram: Gripper, Mystery, Logistic World, Blocks World, Depots, DriverLog, Satellite, Pipes World, TPP e Pathways. Todos esses domínios foram modelados na ferramenta itSIMPLE e estão disponíveis como parte integrante do projeto (itSIMPLE Project, 2008).

No domínio Gripper existe um robô com duas garras, que pode levar uma bola em cada garra (MCDERMOTT, 2008). O objetivo é transportar n bolas de uma sala para outra, onde a dificuldade do problema aumenta com o número de bolas. Alguns planejadores tratam as duas garras de forma assimétrica, gerando uma explosão combinatória desnecessária. A figura 18 mostra o diagrama de casos de uso deste domínio modelado no itSIMPLE.

Figura 18 – Diagrama de casos de uso do domínio Gripper modelado no itSIMPLE.

Fonte: Autor

No domínio Mystery existe um gráfico plano de nós (MCDERMOTT, 2008). Em cada nó estão veículos, itens de carga e certa quantidade de combustível. Itens de carga podem ser carregados nos veículos até o limite das suas capacidades. Os veículos podem deslocar-se entre os nós, porém um veículo só pode deixar o nó se existir uma quantidade de combustível disponível no nó (diminuindo em uma unidade a quantidade de combustível quando este existir). O objetivo é levar itens de carga de diversos nós para outros nós.

O mistério deste domínio está na forma como ele é apresentado: os nós foram chamados de emoções, os itens de carga foram chamados de dores, os veículos chamados de prazeres e o combustível e a capacidade de carga foram codificados em entidades geográficas (cidades e planetas). A figura 19 mostra o diagrama de classes deste domínio modelado no itSIMPLE.

Figura 19 – Diagrama de classes do domínio Mystery modelado no itSIMPLE.

Fonte: Autor

No domínio Logistics World o objetivo é mover um conjunto de pacotes entre localidades utilizando caminhões dentro da mesma cidade e aviões entre cidades diferentes (MCDERMOTT, 2008). Existe também um limite de interações entre objetivos. A figura 20 mostra o diagrama de classes deste domínio modelado no itSIMPLE. Esse diagrama modela com clareza o relacionamento de generalização existentes nos objetos Place e Vehicle.

Figura 20 – Diagrama de classes do domínio Logistics World modelado no itSIMPLE.

Fonte: Autor

O domínio Blocks World consiste em empilhar um conjunto de blocos numa determinada ordem (BACCHUS, 2000). Existe um alto grau de interação entre os objetivos. É um domínio simples para pessoas, porém pode ser muito difícil para planejadores. A figura 21 mostra o diagrama de estados deste domínio modelado no itSIMPLE. Neste digrama é possível ver quais são os estados em que um bloco pode estar: sobre a mesa, segurado pela garra ou sobre outro bloco.

Figura 21 – Diagrama de estados do domínio Blocks World modelado no itSIMPLE.

Fonte: Autor

O domínio Depots foi concebido para verificar o que aconteceria se dois domínios anteriormente bem pesquisados fossem unidos (FOX e LONG, 2002). Esse dois domínios são o mundo de blocos e o mundo da logística. Eles foram combinados em um domínio no qual caminhões transportam caixotes e estes caixotes precisam ser empilhados em paletes nos seus destinos. Guinchos, que substituem a garra do mundo de blocos, organizam os caixotes. Os caminhões podem ser vistos como mesas, uma vez que os paletes possuem limitações de número de caixotes.

A figura 22 mostra o digrama de classes deste domínio modelado no itSIMPLE. Para contabilizar o gasto de combustível, que é uma variável global neste domínio não pertencendo a nenhuma outra classe, foi criada uma classe chamada Utility com o atributo fuelCost. Esse atributo é atualizado de acordo com as ações executadas no domínio e representa o valor total do combustível gasto.

Figura 22 – Diagrama de classes do domínio Depots modelado no itSIMPLE.

Fonte: Autor

O domínio DriverLog consiste em conduzir caminhões para entregar pacotes entre localizações (FOX e LONG, 2002). A complicação está na ordenação da alocação de motoristas que devem conduzir os caminhões. Os caminhos percorridos pelos motoristas entre os caminhões e as estradas percorridas pelos caminhões entre as localidades formam mapas diferentes. A figura 23 mostra o diagrama de casos de uso deste domínio modelado no itSIMPLE. A partir deste digrama é possível observar quais são as ações que podem ser executadas pelo caminhão (truck) e pelo motorista (driver).

Figura 23 – Diagrama de casos de uso do domínio DriverLog modelado no itSIMPLE.

Fonte: Autor

Satellite é o primeiro dos domínios inspirado por aplicações espaciais (FOX e LONG, 2002). Trata-se de planejamento e programação de um conjunto de tarefas de observação (captura de imagens) entre múltiplos satélites, cada um equipado de forma ligeiramente diferente. A figura 24 mostra o diagrama de casos de uso deste domínio modelado no itSIMPLE. Neste diagrama é possível observar uma relação de dependência entre os casos de uso: para capturar uma imagem, antes é necessário calibrar o instrumento de captura, que precisa primeiro estar ligado.

Figura 24 – Diagrama de casos de uso do domínio Satellite modelado no itSIMPLE.

Fonte: Autor

O domínio Pipes World tem como objetivo controlar o fluxo de derivados de petróleo através de uma rede de dutos, obedecendo algumas restrições como a compatibilidade do produto, restrições do tanque e prazos (EDELKAMP, HOFFMANN e LITTMAN, 2004). Um aspecto interessante deste domínio é que o estado de um derivado que está entrando é diferente do estado de um derivado que está saindo do duto. Essa situação dá origem a fenômenos sutis na geração do plano. A figura 25 mostra o diagrama de classes deste domínio modelado no itSIMPLE. A classe Product, por exemplo, representa a relação dos tipos de produtos possíveis dentro dos dutos.

Figura 25 – Diagrama de classes do domínio Pipes World modelado no itSIMPLE.

Fonte: Autor

O domínio TPP é baseado no problema do caixeiro viajante, que consiste em viajar e comprar produtos em supermercados selecionados para minimizar os custos (menor rota e economia de dinheiro) (GEREVINI, BONET e GIVAN, 2006). A figura 26 mostra o diagrama de classes deste domínio modelado no itSIMPLE.

Figura 26 – Diagrama de classes do domínio TPP modelado no itSIMPLE.

Fonte: Autor

Por fim, o domínio Pathways é inspirado no campo da biologia molecular e consiste em encontrar uma seqüência de reações químicas em um organismo, mapeando cada reação como uma ação do domínio (GEREVINI, BONET e GIVAN, 2006).

Muitas doenças podem ser explicadas por defeitos nestas seqüências de reações. Conseqüentemente, novos tratamentos e remédios podem ser criados com base nos planos encontrados pelos planejadores. A figura 27 mostra o diagrama de classes deste domínio modelado no itSIMPLE.

Figura 27 – Diagrama de classes do domínio Pathways modelado no itSIMPLE.

Fonte: Autor

## Características de domínios

Dentre os métodos e linguagens de modelagem de domínios orientados a objetos, a UML é a que possui maior riqueza de representação. De acordo com (SIAU e CAO, 2006), a expressividade da UML é maior do que a de métodos como OMT (RUMBAUGH, BLAHA, et al., 1994) e Yourdon (YOURDON, 1996), o que favorece a identificação de características de domínios através de seus diagramas.

Como já foi visto, a ferramenta itSIMPLE implementa a modelagem de domínios através da UML.P, uma extensão da UML adaptada para o planejamento. Assim, podemos representar os domínios modelando os diagramas de casos de uso, classes e estados. Foram extraídas 17 (dezessete) métricas para caracterizar domínios a partir desses diagramas.

No diagrama de casos de uso é possível extrair métricas relativas ao número de atores e ações que podem ser executadas. Em (IN, KIM e BARRY, 2003), são definidas as seguintes métricas elencadas na tabela 5:

Tabela 5 - Métricas extraídas do Diagrama de Casos de Uso

[[TABELA 05: 4 linhas x 2 colunas]]
| Métricas | Definição |
| Número de atores | somatório do número de atores |
| Número de casos de uso | somatório do número de casos de uso |
| Número de casos de uso por atores | somatória da razão do número de casos de uso por atores |

Fonte: Autor “adaptado de” (IN, KIM e BARRY, 2003)

Essas métricas podem ser utilizadas para representar características de um determinado domínio. Por exemplo, podemos dizer que um domínio possui um número de atores alto, um número de casos de uso alto e um número casos de uso por atores baixo. Essas características mostram que, apesar deste domínio ter muitos atores e casos de uso, os atores estão relacionados a poucos casos de uso.

Não são consideradas as métricas referentes às relações de inclusão, extensão e dependência entre os casos de uso. Essas relações representariam ligações entre ações de um domínio, detalhando como uma ação está condicionada a execução de outra ação. Como este trabalho trata apenas de sistemas clássicos de planejamento, onde cada ação deve ter apenas uma saída possível e um comportamento determinístico, esses relacionamentos entre casos de usos não foram considerados.

A partir do diagrama de classes também é possível extrair algumas métricas para caracterizar os domínios. No trabalho (GENERO e PIATTINI, 2001), estão definidas métricas que estabelecem a complexidade estrutural dos diagramas de classes, considerando o uso de associações, generalizações, agregações e dependências. Essas métricas estão relacionadas na tabela 6. DIT (Depth of Inheritance Tree) é a sigla utilizada pelos autores do trabalho para representar a profundidade da árvore de herança, enquanto HAgg (Height of Aggregation) foi a sigla utilizada para representar a profundidade de uma agregação entre classes.

Tabela 6 - Métricas extraídas do Diagrama de Classes

[[TABELA 06: 11 linhas x 2 colunas]]
| Métricas | Definição |
| Número total de Classes | Somatório do número de classes |
| Número total de Atributos | Somatório do número de atributos |
| Número total de Métodos | Somatório do número de métodos |
| Número total de Associações | Somatório do número de associações |
| Número total de Agregação | Somatório do número de relacionamentos de agregação (cada par todo-parte) |
| Número total de Generalização | Somatório do número de relacionamentos de generalização (cada par pai-filho) |
| Métricas | Definição |
| Número total de Hierarquias | Somatório do número de hierarquias |
| DIT Máximo | É o valor que representa o caminho mais longo (profundidade da herança) entre uma classe e sua classe pai. |
| HAgg Máximo | É o valor que representa o caminho mais longo (profundidade da agregação) entre uma classe e sua classe agregadora. |

Fonte: Autor “adaptado de” (GENERO e PIATTINI, 2001)

Da mesma forma, podemos caracterizar um determinado domínio de acordo com as métricas extraídas do diagrama de classes. Por exemplo, um domínio pode ter um número de classes baixo, número de atributos alto e número de métodos baixo.

Por fim, no diagrama de estados existem métricas que revelam características do comportamento dinâmico de um domínio através dos diferentes elementos que compõe esse tipo de diagrama: estados, transições, atividades e ações. De acordo com (GENERO, MIRANDA e PIATTINI, 2002), as métricas relacionadas na tabela 7 podem ser extraídas de um diagrama de estados:

Tabela 7 - Métricas extraídas do Diagrama de Estados

[[TABELA 07: 6 linhas x 2 colunas]]
| Métricas | Definição |
| Número total de estados | Somatório do número de estados |
| Número total de ações de entrada | Somatório do número de ações de entrada, isto é, as ações que são executadas cada vez que o domínio assume um novo estado. |
| Número total de ações de saída | Somatório do número de ações de saída, isto é, as ações que são executadas cada vez que o domínio deixa ter um estado. |
| Número total de ações | Somatório do número total de ações |
| Número total de transições | Somatório do número de transições |

Fonte: Autor “adaptado de” (GENERO, MIRANDA e PIATTINI, 2002)

Assim, podemos dizer que um domínio tem, por exemplo, um número total de estados alto, número total de ações baixo e um número total de transições baixo.

## Domínios versus características

Os valores das métricas foram obtidos a partir de uma contagem manual dos elementos e relacionamentos presentes nos domínios selecionados e modelados em UML.P no itSIMPLE. As métricas contabilizadas para cada domínio estão nas tabelas 8 e 9. Os valores representam a contagem de cada métrica nos domínios selecionados.

Tabela 8 - Métricas dos domínios selecionados

[[TABELA 08: 19 linhas x 6 colunas]]
| Métricas / Domínios | Blocks W. | Depots | DriverLog | Gripper | Logistic W. |
| Número de Atores | 1,00 | 2,00 | 2,00 | 1,00 | 2,00 |
| Número de Casos de Uso | 4,00 | 5,00 | 6,00 | 3,00 | 6,00 |
| Número de Casos de Uso por Atores | 0,25 | 0,40 | 0,33 | 0,33 | 0,33 |
| Número total de Classes | 3,00 | 9,00 | 5,00 | 4,00 | 8,00 |
| Número total de Atributos | 5,00 | 8,00 | 8,00 | 4,00 | 7,00 |
| Métricas / Domínios | Blocks W. | Depots | DriverLog | Gripper | Logistic W. |
| Número total de Métodos | 4,00 | 5,00 | 6,00 | 3,00 | 6,00 |
| Número total de Associações | 3,00 | 3,00 | 5,00 | 3,00 | 4,00 |
| Número total de Agregação | 2,00 | 1,00 | 2,00 | 1,00 | 4,00 |
| Número total de Generalização | 0,00 | 7,00 | 3,00 | 0,00 | 4,00 |
| Número total de Hierarquias | 0,00 | 3,00 | 1,00 | 0,00 | 2,00 |
| DIT Máximo | 0,00 | 2,00 | 1,00 | 0,00 | 1,00 |
| HAgg Máximo | 2,00 | 1,00 | 1,00 | 1,00 | 2,00 |
| Número total de estados | 5,00 | 6,00 | 4,00 | 5,00 | 5,00 |
| Número total de ações de entrada | 8,00 | 8,00 | 4,00 | 4,00 | 4,00 |
| Número total de ações de saída | 8,00 | 8,00 | 4,00 | 4,00 | 4,00 |
| Número total de ações | 4,00 | 5,00 | 6,00 | 3,00 | 6,00 |
| Número total de transições | 10,00 | 13,00 | 11,00 | 9,00 | 12,00 |

Fonte: Autor

Tabela 9 - Métricas dos domínios selecionados (cont.)

[[TABELA 09: 18 linhas x 6 colunas]]
| Métricas / Domínios | Mystery | Pathways | Pipes W. | Satellite | TPP |
| Número de Atores | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| Número de Casos de Uso | 3,00 | 5,00 | 6,00 | 5,00 | 4,00 |
| Número de Casos de Uso por Atores | 0,33 | 0,20 | 0,17 | 0,20 | 0,25 |
| Número total de Classes | 6,00 | 5,00 | 5,00 | 4,00 | 7,00 |
| Número total de Atributos | 7,00 | 5,00 | 11,00 | 9,00 | 6,00 |
| Número total de Métodos | 3,00 | 5,00 | 6,00 | 5,00 | 4,00 |
| Número total de Associações | 7,00 | 4,00 | 4,00 | 4,00 | 3,00 |
| Número total de Agregação | 3,00 | 0,00 | 1,00 | 2,00 | 2,00 |
| Número total de Generalização | 2,00 | 2,00 | 0,00 | 0,00 | 2,00 |
| Número total de Hierarquias | 1,00 | 1,00 | 0,00 | 0,00 | 2,00 |
| DIT Máximo | 1,00 | 1,00 | 0,00 | 0,00 | 1,00 |
| HAgg Máximo | 1,00 | 1,00 | 1,00 | 2,00 | 2,00 |
| Número total de estados | 3,00 | 4,00 | 4,00 | 5,00 | 4,00 |
| Número total de ações de entrada | 2,00 | 5,00 | 4,00 | 6,00 | 3,00 |
| Número total de ações de saída | 2,00 | 4,00 | 4,00 | 6,00 | 3,00 |
| Número total de ações | 3,00 | 5,00 | 6,00 | 5,00 | 4,00 |
| Número total de transições | 7,00 | 7,00 | 8,00 | 13,00 | 7,00 |

Fonte: Autor

Utilizando os valores das métricas, para facilitar a caracterização dos domínios, foi estabelecida uma discretização dos valores. Cada valor de métrica foi classificado como Alto, Médio ou Baixo, considerando os valores dessas métricas nos 10 domínios estudados.

O procedimento adotado para criar essa classificação foi baseado no cálculo simples da variância dos valores de cada métrica em todos os domínios. Por exemplo, o domínio Depots apresentou o maior valor na métrica Número total de classes (9); já o domínio Blocks World apresentou o menor valor de Número total de classes (3); a variância aproximada dos valores nesta faixa foi de 3,5. Portando, a métrica Número total de classes é classificada como Alto se seu valor for maior que 7; como Médio se o seu valor é menor ou igual a 7 e maior que 3,5; e como Baixo se o seu valor é menor ou igual a 3,5. A partir desta convenção, as tabelas 10 e 11 foram geradas:

Tabela 10 – Discretização dos valores das Métricas dos domínios selecionados

[[TABELA 10: 18 linhas x 6 colunas]]
| Métricas / Domínios | Blocks W. | Depots | DriverLog | Gripper | Logistic W. |
| Número de Atores | Baixo | Alto | Alto | Baixo | Alto |
| Número de Casos de Uso | Médio | Médio | Alto | Baixo | Alto |
| Número de Casos de Uso por Atores | Médio | Alto | Médio | Médio | Médio |
| Número total de Classes | Baixo | Alto | Médio | Médio | Médio |
| Número total de Atributos | Médio | Médio | Médio | Baixo | Médio |
| Número total de Métodos | Médio | Médio | Alto | Baixo | Alto |
| Número total de Associações | Baixo | Baixo | Médio | Baixo | Médio |
| Número total de Agregação | Médio | Médio | Médio | Médio | Alto |
| Número total de Generalização | Baixo | Alto | Médio | Baixo | Médio |
| Número total de Hierarquias | Baixo | Alto | Médio | Baixo | Médio |
| DIT Máximo | Baixo | Alto | Médio | Baixo | Médio |
| HAgg Máximo | Alto | Baixo | Baixo | Baixo | Alto |
| Número total de estados | Médio | Alto | Médio | Médio | Médio |
| Número total de ações de entrada | Alto | Alto | Médio | Médio | Médio |
| Número total de ações de saída | Alto | Alto | Médio | Médio | Baixo |
| Número total de ações | Médio | Médio | Alto | Baixo | Alto |
| Número total de transições | Médio | Alto | Médio | Médio | Médio |

Fonte: Autor

Tabela 11 - Discretização dos valores das Métricas dos domínios selecionados (cont.)

[[TABELA 11: 18 linhas x 6 colunas]]
| Métricas / Domínios | Mystery | Pathways | Pipes W. | Satellite | TPP |
| Número de Atores | Baixo | Baixo | Baixo | Baixo | Baixo |
| Número de Casos de Uso | Baixo | Médio | Alto | Médio | Médio |
| Número de Casos de Uso por Atores | Médio | Médio | Baixo | Médio | Médio |
| Número total de Classes | Médio | Médio | Médio | Médio | Médio |
| Número total de Atributos | Médio | Médio | Alto | Médio | Médio |
| Número total de Métodos | Baixo | Médio | Alto | Médio | Médio |
| Número total de Associações | Alto | Médio | Médio | Médio | Baixo |
| Número total de Agregação | Médio | Baixo | Médio | Médio | Médio |
| Número total de Generalização | Médio | Médio | Baixo | Baixo | Médio |
| Número total de Hierarquias | Médio | Médio | Baixo | Baixo | Médio |
| DIT Máximo | Médio | Médio | Baixo | Baixo | Médio |
| HAgg Máximo | Baixo | Baixo | Baixo | Alto | Alto |
| Número total de estados | Baixo | Médio | Médio | Médio | Médio |
| Número total de ações de entrada | Baixo | Médio | Médio | Médio | Médio |
| Número total de ações de saída | Baixo | Médio | Médio | Médio | Médio |
| Número total de ações | Baixo | Médio | Alto | Médio | Médio |
| Número total de transições | Baixo | Baixo | Médio | Alto | Baixo |

Fonte: Autor

Esta estratégia simplificada de discretização foi adotada devido ao pequeno número de domínios relevantes para esta pesquisa que estavam disponíveis nas competições internacionais de planejamento. Entretanto, com a adição de mais domínios neste estudo, os valores de Baixo, Médio e Alto podem ser reclassificados para representarem adequadamente a variação dos valores das métricas de todos os domínios. Futuramente, quando uma quantidade razoável de domínios estiver sendo considerada, uma abordagem estatística poderá ser utilizada na discretização dos valores para refinar esta classificação.

# Características de domínios versus técnicas de planejamento

## Método

Com o propósito de estabelecer uma relação entre características de domínios e técnicas de planejamento é proposto neste trabalho um cruzamento entre as métricas extraídas da modelagem dos domínios em UML.P com a eficiência (número de problemas resolvidos) dos planejadores selecionados na resolução de problemas nos domínios escolhidos. A qualidade de um plano e o tempo necessário para gerá-lo não foram considerados no método utilizado para identificar essa relação, que é composto por oito etapas:

1ª etapa: modelagem dos domínios selecionados em UML.P utilizando o diagrama de casos de uso, o diagrama de classes e o diagrama de estados;

2ª etapa: contagem visual e manual das métricas extraídas da UML nos modelos dos domínios selecionados;

3ª etapa: discretização das métricas, considerando a variância entre os valores para classificá-los como Alto, Médio e Baixo. Esses valores estabelecem as características do domínio;

4ª etapa: obter os valores de eficiência dos planejadores, nos domínios selecionados, nos resultados das competições internacionais de planejamento;

5ª etapa: obter os valores de eficiência dos planejadores nos domínios selecionados que não foram encontrados nos resultados das competições;

6ª etapa: obter uma relação entre planejadores e técnicas de planejamento.

7ª etapa: obter uma relação entre características de domínios e técnicas de planejamento a partir dos resultados dos planejamentos (planejador x domínio).

8ª etapa: identificar quais são as características mais relevantes, ou seja, aquelas que causam maior diferença no desempenho dos planejadores.

### Resultados da eficiência dos planejadores

De acordo com o método proposto, a quarta e quinta etapas dependem dos resultados da eficiência dos planejadores em resolver problemas nos domínios estudados. A partir da análise dos resultados das competições internacionais de planejamento, foi possível construir as tabelas 12 e 13. Os valores representam a porcentagem de problemas resolvidos pelo planejador nos domínios selecionados nesta pesquisa.

Tabela 12 – Eficiência dos planejadores nos domínios selecionados – resultados das competições.

[[TABELA 12: 11 linhas x 6 colunas]]
|  | Blocks W. | Depots | DriverLog | Gripper | Logistic W. |
| Blackbox | 25% |  |  | 10% | 100% |
| IPP | 27% |  |  | 25% | 64% |
| FF | 73% | 100% | 75% |  | 100% |
| R | 100% | 5% | 25% |  | 96% |
| LPG |  |  |  |  |  |
| Fast Downward |  | 86% | 100% |  |  |
| YAHSP |  |  |  |  |  |
| SGPlan |  |  |  |  |  |
| SATPlan |  |  |  |  |  |
| MAXPLAN |  |  |  |  |  |

Fonte: Autor

Tabela 13 – Eficiência dos planejadores nos domínios selecionados – resultados das competições (cont.)

[[TABELA 13: 11 linhas x 6 colunas]]
|  | Mystery | Pathways | Pipes W. | Satellite | TPP |
| Blackbox | 44% |  |  |  |  |
| IPP | 43% |  |  |  |  |
| FF |  |  |  | 100% |  |
| R |  |  |  |  |  |
| LPG |  |  | 68% | 100% |  |
| Fast Downward |  | 100% | 38% | 100% | 100% |
| YAHSP |  |  | 86% | 100% |  |
| SGPlan |  | 100% | 66% | 83% | 100% |
| SATPlan |  | 30% | 24% | 31% | 80% |
| MAXPLAN |  | 50% | 16% |  | 50% |

Fonte: Autor

Entretanto, não foi possível obter nos resultados das competições internacionais de planejamento todos os valores das eficiências dos planejadores nos domínios selecionados, uma vez que os domínios e planejadores foram criados em anos diferentes e participaram de edições diferentes da competição internacional de planejamento. Para obter esses valores, assim como é feito nas competições, foi necessário executar processos de planejamento para cada par de planejador x domínio faltantes.

Os planejadores, obtidos nos websites ou através de contatos com os seus autores na versão original utilizada nas competições internacionais de planejamento, foram executados em oito computadores com a mesma configuração de hardware (Intel Core 2 Duo 2.5 GHz com 4 GB de memória RAM) e software (Linux Ubuntu 9.04). O tempo máximo (timeout) para um planejador resolver um problema de planejamento foi de 20 (vinte) minutos.

Foram executados cerca de 2.000 (dois mil) processos de planejamento. Para cada par planejador x domínio foi criado um arquivo contendo os planos gerados e o tempo para gerar cada um dos planos. Os resultados obtidos e analisados ajudaram a completar os dados faltantes e deram origem as tabelas 14 e 15.

Tabela 14 – Eficiência dos planejadores nos domínios selecionados – dados completos.

[[TABELA 14: 11 linhas x 6 colunas]]
|  | Blocks W. | Depots | DriverLog | Gripper | Logistic W. |
| Blackbox | 25% | 0% | 60% | 10% | 100% |
| IPP | 27% | 45% | 65% | 25% | 64% |
| FF | 73% | 100% | 75% | 100% | 100% |
| R | 100% | 5% | 25% | 100% | 96% |
| LPG | 100% | 100% | 90% | 100% | 96% |
| Fast Downward | 100% | 86% | 100% | 100% | 96% |
| YAHSP | 100% | 86% | 100% | 100% | 96% |
| SGPlan | 94% | 95% | 85% | 100% | 96% |
| SATPlan | 97% | 73% | 80% | 20% | 96% |
| MAXPLAN | 37% | 50% | 55% | 15% | 96% |

Fonte: Autor

Tabela 15 – Eficiência dos planejadores nos domínios selecionados – dados completos (cont.)

[[TABELA 15: 11 linhas x 6 colunas]]
|  | Mystery | Pathways | Pipes W. | Satellite | TPP |
| Blackbox | 44% | 13% | 10% | 95% | 27% |
| IPP | 43% | 17% | 16% | 35% | 27% |
| FF | 53% | 33% | 40% | 100% | 40% |
| R | 13% | 0% | 0% | 100% | 67% |
| LPG | 60% | 100% | 68% | 100% | 47% |
| Fast Downward | 63% | 100% | 38% | 100% | 100% |
| YAHSP | 53% | 67% | 86% | 100% | 100% |
| SGPlan | 53% | 100% | 66% | 83% | 100% |
| SATPlan | 57% | 30% | 24% | 31% | 80% |
| MAXPLAN | 50% | 50% | 16% | 30% | 50% |

Fonte: Autor

Para simplificar a análise e a comparação entre os planejadores, os valores percentuais foram convertidos para valores entre 0 (zero) e 10 (dez). Esses valores representam a nota da eficiência do planejador em resolver problemas de um determinado domínio. Esses valores são mostrados nas tabelas 16 e 17.

Tabela 16 – Nota de eficiência dos planejadores nos domínios selecionados

[[TABELA 16: 11 linhas x 6 colunas]]
|  | Blocks W. | Depots | DriverLog | Gripper | Logistic W. |
| Blackbox | 3 | 0 | 6 | 1 | 10 |
| IPP | 3 | 5 | 7 | 3 | 6 |
| FF | 7 | 10 | 8 | 10 | 10 |
| R | 10 | 0 | 3 | 10 | 10 |
| LPG | 10 | 10 | 9 | 10 | 10 |
| Fast Downward | 10 | 9 | 10 | 10 | 10 |
| YAHSP | 10 | 9 | 10 | 10 | 10 |
| SGPlan | 9 | 10 | 9 | 10 | 10 |
| SATPlan | 10 | 7 | 8 | 2 | 10 |
| MAXPLAN | 4 | 5 | 6 | 2 | 10 |

Fonte: Autor

Tabela 17 – Nota de eficiência dos planejadores nos domínios selecionados (cont.)

[[TABELA 17: 11 linhas x 6 colunas]]
|  | Mystery | Pathways | Pipes W. | Satellite | TPP |
| Blackbox | 4 | 1 | 1 | 10 | 3 |
| IPP | 4 | 2 | 2 | 4 | 3 |
| FF | 5 | 3 | 4 | 10 | 4 |
| R | 1 | 0 | 0 | 10 | 7 |
| LPG | 6 | 10 | 7 | 10 | 5 |
| Fast Downward | 6 | 10 | 4 | 10 | 10 |
| YAHSP | 5 | 7 | 9 | 10 | 10 |
| SGPlan | 5 | 10 | 7 | 8 | 10 |
| SATPlan | 6 | 3 | 2 | 3 | 8 |
| MAXPLAN | 5 | 5 | 2 | 3 | 5 |

Fonte: Autor

## Relação entre características de domínios e técnicas de planejamento

Para obter a relação entre características de domínios e técnicas de planejamento, o primeiro passo foi encontrar o desempenho médio de uma característica de domínio para uma determinada técnica. Na tabela 18 está o exemplo da relação entre a característica HAgg Máximo Alto (valor mais alto de profundidade de uma agregação) com a técnica de planejamento Forward-chaining:

Tabela 18 – Média de desempenho entre uma técnica de planejamento x característica de domínio.

[[TABELA 18: 39 linhas x 3 colunas]]
| Domínio | Planejador | Nota |
| Blocks World | LPG | 10 |
| Blocks World | Fast Downward | 10 |
| Blocks World | R | 10 |
| Blocks World | YAHSP | 10 |
| Blocks World | MAXPlan | 4 |
| Blocks World | SGPlan | 9 |
| Blocks World | FF | 7 |
| Blocks World | Blackbox | 3 |
| Blocks World | SATPlan | 10 |
| TPP | LPG | 5 |
| TPP | Fast Downward | 10 |
| TPP | R | 7 |
| TPP | YAHSP | 10 |
| TPP | MAXPlan | 5 |
| TPP | SGPlan | 10 |
| TPP | FF | 4 |
| TPP | Blackbox | 3 |
| TPP | SATPlan | 8 |
| Satellite | LPG | 10 |
| Satellite | Fast Downward | 10 |
| Satellite | R | 10 |
| Satellite | YAHSP | 10 |
| Domínio | Planejador | Nota |
| Satellite | MAXPlan | 3 |
| Satellite | SGPlan | 8 |
| Satellite | FF | 10 |
| Satellite | Blackbox | 10 |
| Satellite | SATPlan | 3 |
| Logistic World | LPG | 10 |
| Logistic World | Fast Downward | 10 |
| Logistic World | R | 10 |
| Logistic World | YAHSP | 10 |
| Logistic World | MAXPlan | 10 |
| Logistic World | SGPlan | 10 |
| Logistic World | FF | 10 |
| Logistic World | Blackbox | 10 |
| Logistic World | SATPlan | 10 |
| Media | Media | 8 |

Fonte: Autor

A média das notas resultante significa que, quando a característica HAgg Máximo Alto está presente no domínio, a técnica Forward-chaining tem uma eficiência em torno de 80% para resolver problemas deste domínio. O cálculo desta média foi feito para todos os demais pares de característica de domínio x técnica de planejamento.

O segundo passo foi compor todas essas médias resultantes nas tabelas 19 e 20, quantificando todas as relações técnicas de planejamento x características de domínios:

Tabela 19 – Relação entre características de domínio x técnicas de planejamento.

[[TABELA 19: 51 linhas x 6 colunas]]
| Características de domínios | Backward chaining | Forward chaining | Hierarchical | Partial order | Total order |
| HAgg Máximo Alto | 9 | 8 | 10 | 8 | 8 |
| HAgg Máximo Baixo | 2 | 6 | 8 | 6 | 6 |
| DIT Máximo Alto | 0 | 7 | 9 | 6 | 7 |
| DIT Máximo Baixo | 8 | 7 | 9 | 6 | 7 |
| DIT Máximo Medio | 4 | 7 | 9 | 7 | 7 |
| Número de Atores Alto | 4 | 8 | 10 | 8 | 8 |
| Número de Atores Baixo | 5 | 6 | 9 | 6 | 6 |
| Número de Casos de Uso Alto | 4 | 7 | 8 | 7 | 7 |
| Número de Casos de Uso Baixo | 6 | 6 | 8 | 6 | 6 |
| Número de Casos de Uso Medio | 5 | 7 | 10 | 7 | 7 |
| Número médio de Atores por Caso de Uso Alto | 0 | 7 | 9 | 6 | 7 |
| Número médio de Atores por Caso de Uso Baixo | 0 | 4 | 4 | 4 | 4 |
| Número médio de Atores por Caso de Uso Medio | 6 | 7 | 10 | 7 | 7 |
| Número total de ações Alto | 4 | 7 | 8 | 7 | 7 |
| Número total de ações Baixo | 6 | 6 | 8 | 6 | 6 |
| Número total de ações Medio | 5 | 7 | 10 | 7 | 7 |
| Número total de ações de entrada Alto | 5 | 7 | 10 | 8 | 7 |
| Número total de ações de entrada Baixo | 1 | 5 | 6 | 5 | 5 |
| Número total de ações de entrada Medio | 6 | 7 | 9 | 7 | 7 |
| Número total de açoes de saída Alto | 5 | 7 | 10 | 8 | 7 |
| Número total de açoes de saída Baixo | 6 | 7 | 8 | 7 | 7 |
| Número total de açoes de saída Medio | 5 | 7 | 9 | 6 | 6 |
| Número total de Agregação (pares todo-parte) Alto | 10 | 10 | 10 | 10 | 9 |
| Número total de Agregação (pares todo-parte) Baixo | 0 | 5 | 10 | 6 | 5 |
| Número total de Agregação (pares todo-parte) Medio | 5 | 7 | 9 | 6 | 6 |
| Número total de Associações Alto | 1 | 5 | 6 | 5 | 5 |
| Número total de Associações Baixo | 7 | 7 | 10 | 7 | 7 |
| Número total de Associações Medio | 5 | 7 | 9 | 7 | 7 |
| Número total de Atributos Alto | 0 | 4 | 4 | 4 | 4 |
| Número total de Atributos Baixo | 10 | 7 | 10 | 7 | 7 |
| Número total de Atributos Medio | 5 | 7 | 9 | 7 | 7 |
| Número total de Classes Alto | 0 | 7 | 9 | 6 | 7 |
| Número total de Classes Baixo | 10 | 8 | 10 | 9 | 7 |
| Número total de Classes Medio | 5 | 7 | 9 | 6 | 7 |
| Características de domínios | Backward chaining | Forward chaining | Hierarchical | Partial order | Total order |
| Número total de estados Alto | 0 | 7 | 9 | 6 | 7 |
| Número total de estados Baixo | 1 | 5 | 6 | 5 | 5 |
| Número total de estados Medio | 6 | 7 | 9 | 7 | 7 |
| Número total de Generalização (pares pai-filho) Alto | 0 | 7 | 9 | 6 | 7 |
| Número total de Generalização (pares pai-filho) Baixo | 8 | 7 | 9 | 6 | 7 |
| Número total de Generalização (pares pai-filho) Medio | 4 | 7 | 9 | 7 | 7 |
| Número total de Hierarquias Alto | 0 | 7 | 9 | 6 | 7 |
| Número total de Hierarquias Baixo | 8 | 7 | 9 | 6 | 7 |
| Número total de Hierarquias Medio | 4 | 7 | 9 | 7 | 7 |
| Número total de Métodos Alto | 4 | 7 | 8 | 7 | 7 |
| Número total de Métodos Baixo | 6 | 6 | 8 | 6 | 6 |
| Número total de Métodos Medio | 5 | 7 | 10 | 7 | 7 |
| Número total de transições Alto | 5 | 7 | 10 | 7 | 8 |
| Número total de transições Baixo | 3 | 6 | 9 | 6 | 5 |
| Número total de transições Medio | 7 | 7 | 9 | 7 | 7 |

Fonte: Autor

Tabela 20 – Relação entre características de domínio x técnicas de planejamento (cont.)

[[TABELA 20: 50 linhas x 7 colunas]]
| Características de domínios | Plan Space | State Space | Graph based | Heuristc search | SAT based | Knowledge based |
| HAgg Máximo Alto | 8 | 8 | 7 | 9 | 7 | 10 |
| HAgg Máximo Baixo | 7 | 5 | 6 | 8 | 4 | 8 |
| DIT Máximo Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| DIT Máximo Baixo | 6 | 7 | 6 | 9 | 4 | 10 |
| DIT Máximo Medio | 8 | 6 | 6 | 8 | 6 | 8 |
| Número de Atores Alto | 9 | 7 | 8 | 10 | 7 | 10 |
| Número de Atores Baixo | 6 | 6 | 5 | 8 | 4 | 9 |
| Número de Casos de Uso Alto | 8 | 7 | 7 | 8 | 6 | 10 |
| Número de Casos de Uso Baixo | 6 | 6 | 5 | 8 | 3 | 8 |
| Número de Casos de Uso Medio | 7 | 6 | 6 | 9 | 5 | 9 |
| Número médio de Atores por Caso de Uso Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| Número médio de Atores por Caso de Uso Baixo | 5 | 3 | 4 | 6 | 2 | 9 |
| Número médio de Atores por Caso de Uso Medio | 7 | 7 | 6 | 9 | 5 | 9 |
| Número total de ações Alto | 8 | 7 | 7 | 8 | 6 | 10 |
| Número total de ações Baixo | 6 | 6 | 5 | 8 | 3 | 8 |
| Número total de ações Medio | 7 | 6 | 6 | 9 | 5 | 9 |
| Número total de ações de entrada Alto | 8 | 6 | 7 | 9 | 5 | 10 |
| Número total de ações de entrada Baixo | 6 | 4 | 5 | 6 | 5 | 5 |
| Número total de ações de entrada Medio | 7 | 7 | 6 | 9 | 5 | 9 |
| Número total de açoes de saída Alto | 8 | 6 | 7 | 9 | 5 | 10 |
| Número total de açoes de saída Baixo | 8 | 7 | 7 | 8 | 8 | 8 |
| Número total de açoes de saída Medio | 6 | 6 | 6 | 8 | 4 | 9 |
| Número total de Agregação (pares todo-parte) Alto | 10 | 9 | 9 | 10 | 10 | 10 |
| Número total de Agregação (pares todo-parte) Baixo | 7 | 4 | 4 | 8 | 3 | 7 |
| Número total de Agregação (pares todo-parte) Medio | 7 | 6 | 6 | 8 | 4 | 9 |
| Número total de Associações Alto | 6 | 4 | 5 | 6 | 5 | 5 |
| Número total de Associações Baixo | 7 | 7 | 6 | 9 | 4 | 10 |
| Número total de Associações Medio | 7 | 7 | 7 | 9 | 5 | 9 |
| Número total de Atributos Alto | 5 | 3 | 4 | 6 | 2 | 9 |
| Número total de Atributos Baixo | 6 | 7 | 5 | 10 | 2 | 10 |
| Número total de Atributos Medio | 7 | 7 | 7 | 9 | 6 | 9 |
| Número total de Classes Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| Número total de Classes Baixo | 8 | 7 | 7 | 9 | 6 | 10 |
| Número total de Classes Medio | 7 | 6 | 6 | 8 | 5 | 9 |
| Número total de estados Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| Número total de estados Baixo | 6 | 4 | 5 | 6 | 5 | 5 |
| Número total de estados Medio | 7 | 7 | 6 | 9 | 5 | 10 |
| Número total de Generalização (pares pai-filho) Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| Número total de Generalização (pares pai-filho) Baixo | 6 | 7 | 6 | 9 | 4 | 10 |
| Número total de Generalização (pares pai-filho) Medio | 8 | 6 | 6 | 8 | 6 | 8 |
| Número total de Hierarquias Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| Número total de Hierarquias Baixo | 6 | 7 | 6 | 9 | 4 | 10 |
| Número total de Hierarquias Medio | 8 | 6 | 6 | 8 | 6 | 8 |
| Número total de Métodos Alto | 8 | 7 | 7 | 8 | 6 | 10 |
| Número total de Métodos Baixo | 6 | 6 | 5 | 8 | 3 | 8 |
| Número total de Métodos Medio | 7 | 6 | 6 | 9 | 5 | 9 |
| Número total de transições Alto | 7 | 7 | 7 | 10 | 5 | 10 |
| Número total de transições Baixo | 7 | 5 | 5 | 7 | 4 | 7 |
| Número total de transições Medio | 7 | 7 | 7 | 9 | 5 | 10 |

Fonte: Autor

### Características de domínios relevantes

Algumas características causaram maior diferença na eficiência dos planejadores, sendo classificadas como mais relevantes na relação criada. As características que tiveram uma variação de até 3 (três) pontos foram consideradas não relevantes. As que obtiveram uma variação de 4 (quatro) a 5 (cinco) pontos foram consideradas pouco relevantes. E as características que obtiveram uma variação acima de 6 (seis) pontos foram consideradas muito relevantes. A tabela 21 relaciona as características não relevantes. A tabela 22 mostra as características pouco relevantes. Por fim, a tabela 22 mostra as características mais relevantes para as técnicas de planejamento.

Tabela 21 – Características de domínios não relevantes para as técnicas de planejamento.

[[TABELA 21: 4 linhas x 5 colunas]]
| Características não relevantes | Variância | Menor | Maior | Diferença |
| Número total de Agregação (pares todo-parte) Alto | 0,23 | 9 | 10 | 1 |
| Número total de açoes de saída Baixo | 0,40 | 6 | 8 | 2 |
| HAgg Máximo Alto | 0,90 | 7 | 10 | 3 |

Fonte: Autor

Tabela 22 – Características de domínios pouco relevantes para as técnicas de planejamento.

[[TABELA 22: 27 linhas x 5 colunas]]
| Características pouco relevantes | Variância | Menor | Maior | Diferença |
| Número total de ações de entrada Medio | 1,47 | 5 | 9 | 4 |
| Número total de Associações Medio | 1,64 | 5 | 9 | 4 |
| Número total de Atributos Medio | 1,36 | 5 | 9 | 4 |
| Número total de Classes Baixo | 1,86 | 6 | 10 | 4 |
| Número total de Classes Medio | 1,69 | 5 | 9 | 4 |
| DIT Máximo Medio | 1,58 | 4 | 9 | 5 |
| Número de Atores Baixo | 2,23 | 4 | 9 | 5 |
| Número de Casos de Uso Baixo | 1,81 | 3 | 8 | 5 |
| Número de Casos de Uso Medio | 2,24 | 5 | 10 | 5 |
| Número médio de Atores por Caso de Uso Medio | 1,86 | 5 | 10 | 5 |
| Número total de ações Baixo | 1,81 | 3 | 8 | 5 |
| Número total de ações Medio | 2,24 | 5 | 10 | 5 |
| Número total de ações de entrada Alto | 2,60 | 5 | 10 | 5 |
| Número total de ações de entrada Baixo | 1,64 | 1 | 6 | 5 |
| Número total de açoes de saída Alto | 2,60 | 5 | 10 | 5 |
| Número total de açoes de saída Medio | 2,10 | 4 | 9 | 5 |
| Número total de Agregação (pares todo-parte) Medio | 2,10 | 4 | 9 | 5 |
| Número total de Associações Alto | 1,64 | 1 | 6 | 5 |
| Número total de estados Baixo | 1,64 | 1 | 6 | 5 |
| Número total de estados Medio | 1,86 | 5 | 10 | 5 |
| Número total de Generalização (pares pai-filho) Medio | 1,58 | 4 | 9 | 5 |
| Número total de Hierarquias Medio | 1,58 | 4 | 9 | 5 |
| Número total de Métodos Baixo | 1,81 | 3 | 8 | 5 |
| Número total de Métodos Medio | 2,24 | 5 | 10 | 5 |
| Número total de transições Alto | 2,77 | 5 | 10 | 5 |
| Número total de transições Medio | 1,59 | 5 | 10 | 5 |

Fonte: Autor

Tabela 23 – Características de domínios muito relevantes para as técnicas de planejamento.

[[TABELA 23: 21 linhas x 5 colunas]]
| Características muito relevantes | Variância | Menor | Maior | Diferença |
| HAgg Máximo Baixo | 2,83 | 2 | 8 | 6 |
| DIT Máximo Baixo | 2,58 | 4 | 10 | 6 |
| Número de Atores Alto | 2,58 | 4 | 10 | 6 |
| Número de Casos de Uso Alto | 1,81 | 4 | 10 | 6 |
| Número total de ações Alto | 1,81 | 4 | 10 | 6 |
| Número total de Associações Baixo | 2,56 | 4 | 10 | 6 |
| Número total de Generalização (pares pai-filho) Baixo | 2,58 | 4 | 10 | 6 |
| Número total de Hierarquias Baixo | 2,58 | 4 | 10 | 6 |
| Número total de Métodos Alto | 1,81 | 4 | 10 | 6 |
| Número total de transições Baixo | 2,36 | 3 | 9 | 6 |
| Número total de Atributos Baixo | 5,40 | 2 | 10 | 8 |
| Número médio de Atores por Caso de Uso Baixo | 4,24 | 0 | 9 | 9 |
| Número total de Atributos Alto | 4,24 | 0 | 9 | 9 |
| DIT Máximo Alto | 6,42 | 0 | 10 | 10 |
| Número médio de Atores por Caso de Uso Alto | 6,42 | 0 | 10 | 10 |
| Número total de Agregação (pares todo-parte) Baixo | 6,09 | 0 | 10 | 10 |
| Número total de Classes Alto | 6,42 | 0 | 10 | 10 |
| Número total de estados Alto | 6,42 | 0 | 10 | 10 |
| Número total de Generalização (pares pai-filho) Alto | 6,42 | 0 | 10 | 10 |
| Número total de Hierarquias Alto | 6,42 | 0 | 10 | 10 |

Fonte: Autor

Algumas características causaram mais impacto em determinadas técnicas de planejamento, fazendo com que a variação de desempenho fosse maior. As tabelas 24 e 25 apresentam uma relação completa das características que causaram maior variação no desempenho das técnicas de planejamento. O sinal “x” indica que a variação de uma determinada característica de domínio influencia no desempenho de um planejador que utiliza uma determinada técnica de planejamento.

Tabela 24 – Características de maior impacto no desempenho das técnicas de planejamento.

[[TABELA 24: 18 linhas x 6 colunas]]
| Características | Backward chaining | Forward chaining | Hierarchical | Partial order | Total order |
| Número de Atores |  |  |  |  |  |
| Número de Casos de Uso |  |  |  |  |  |
| Número de Casos de Uso por Atores | x | x | x | x | x |
| Número total de Classes |  |  |  | x |  |
| Número total de Atributos |  | x | x | x | x |
| Número total de Métodos |  |  |  |  |  |
| Número total de Associações | x |  | x |  |  |
| Número total de Agregação |  | x |  | x | x |
| Número total de Generalização |  |  |  |  |  |
| Número total de Hierarquias | x |  |  |  |  |
| DIT Máximo | x |  |  |  |  |
| HAgg Máximo | x |  |  |  |  |
| Número total de estados |  |  |  |  |  |
| Número total de ações de entrada | x |  | x | x |  |
| Número total de ações de saída |  |  |  |  |  |
| Número total de ações |  |  |  |  |  |
| Número total de transições | x |  |  |  | x |

Fonte: Autor

Tabela 25 – Características de maior impacto no desempenho das técnicas de planejamento (cont.).

[[TABELA 25: 18 linhas x 7 colunas]]
| Características | Plan Space | State Space | Graph based | Heuristc search | SAT based | Knowledge based |
| Número de Atores |  |  |  |  | x |  |
| Número de Casos de Uso |  |  |  |  | x |  |
| Número de Casos de Uso por Atores | x | x | x | x | x |  |
| Número total de Classes |  |  |  |  |  |  |
| Número total de Atributos |  | x | x | x | x |  |
| Número total de Métodos |  |  |  |  | x |  |
| Número total de Associações |  | x |  | x |  | x |
| Número total de Agregação | x | x | x |  | x | x |
| Número total de Generalização |  |  |  |  |  |  |
| Número total de Hierarquias |  |  |  |  |  |  |
| DIT Máximo |  |  |  |  |  |  |
| HAgg Máximo |  | x |  |  | x |  |
| Número total de estados |  | x |  | x |  | x |
| Número total de ações de entrada |  | x |  | x |  | x |
| Número total de ações de saída |  |  |  |  | x |  |
| Número total de ações |  |  |  |  | x |  |
| Número total de transições |  |  |  | x |  | x |

Fonte: Autor

Analisando esta relação, algumas considerações podem ser feitas. A característica Número de Casos de Uso por Atores impacta em quase todas as técnicas de planejamento. A relação entre o número de atores e o número de casos de uso (ou ações), interfere diretamente nas técnicas de planejamento.  O mesmo acontece para as características Número total de Agregação e Número total de atributos.

Outra análise que pode ser feita é a comparação de duas técnicas: Partial-order e Total-order. Nos resultados obtidos, a variação do Número total de Classes de um domínio afeta diretamente a técnica Partial-order. Já a técnica Total-order é afetada diretamente pela característica Número total de Transições.

## Testes e validações

Para validar a relação estabelecida foram utilizados três outros domínios presentes nas competições internacionais de planejamento: Storage, Zeno-travel e Elevator.

O objetivo dos testes é criar um ranking de planejadores que terão melhor desempenho na resolução de problemas nestes domínios com base na relação criada entre características de domínios e técnicas de planejamento.

O ranking é confrontado e validado com os resultados dos processos de planejamento dos dez planejadores estudados. A execução dos testes nos domínios propostos é feita através de seis passos:

1° passo: o domínio é modelado em UML.P a partir da ferramenta itSIMPLE;

2° passo: identificação e contabilização das métricas/características do domínio;

3° passo: cálculo da média de eficiência das técnicas de planejamento nas características encontradas no domínio, com base na relação de características de domínios e técnicas de planejamento criada neste trabalho;

4° passo: cálculo da média das médias de desempenho das técnicas de planejamento relacionadas aos planejadores que farão parte do ranking, estabelecendo assim um índice de desempenho para cada planejador;

5° passo: estabelecer o ranking de planejadores que melhor resolvem problemas no domínio em questão a partir dos índices de desempenho;

6° passo: validação do ranking de planejadores com os resultados reais da execução dos processos de planejamento.

### Domínio Storage

O domínio Storage envolve raciocínio espacial. Este domínio é sobre a movimentação de caixotes de alguns contêineres para depósitos utilizando guinchos. Cada guincho pode se mover de acordo com um mapa espacial que conecta diferentes áreas do depósito. Os problemas deste domínio envolvem números diferentes de depósitos, caixotes, contêineres, guinchos e áreas de depósito.

1° passo: as figuras 28, 29 e 30 mostram modelagem do domínio em UML.P nos diagramas de casos de uso, classes e estados, respectivamente;

Figura 28 – Diagrama de casos de uso do domínio Storage modelado no itSIMPLE.

Fonte: Autor

Figura 29 – Diagrama de classes do domínio Storage modelado no itSIMPLE.

Fonte: Autor

Figura 30 – Diagramas de estados do domínio Storage modelado no itSIMPLE.

Fonte: Autor

2° passo: a tabela 26 mostra a identificação e contabilização das características do domínio Storage. Por exemplo, o domínio possui um único ator (Número de Atores = 1) e possui nove classes (Número total de Classes = 9);

Tabela 26 – Métricas e características do domínio Storage.

[[TABELA 26: 18 linhas x 3 colunas]]
| Características | Storage | Classificação |
| Número de Atores | 1 | Baixo |
| Número de Casos de Uso | 5 | Médio |
| Número de Casos de Uso por Atores | 0,2 | Médio |
| Número total de Classes | 9 | Alto |
| Número total de Atributos | 9 | Médio |
| Número total de Métodos | 5 | Médio |
| Número total de Associações | 7 | Alto |
| Número total de Agregação | 2 | Médio |
| Número total de Generalização | 6 | Médio |
| Número total de Hierarquias | 3 | Alto |
| DIT Máximo | 2 | Alto |
| HAgg Máximo | 1 | Baixo |
| Número total de estados | 6 | Alto |
| Número total de ações de entrada | 6 | Médio |
| Número total de ações de saída | 6 | Médio |
| Número total de ações | 5 | Médio |
| Número total de transições | 9 | Médio |

Fonte: Autor

3° passo: as tabelas 27 e 28 mostram os resultados dos cálculos das médias de eficiência das técnicas de planejamento com base nos valores obtidos nas tabelas 19 e 20. Por exemplo, o domínio Storage possui a característica Número de Atores Baixo. Para essa característica, com base nas tabelas 19 e 20, a nota de eficiência dos planejadores que utilizam a técnica Foward chaining foi 6. A média geral das notas de eficiência dos planejadores que utilizam a técnica Foward chaining para todas as características presentes no domínio Storage é 6,76.

Tabela 27 – Média de eficiência das técnicas de planej. nas características do domínio Storage.

[[TABELA 27: 20 linhas x 7 colunas]]
| Características | Características | Backward chaining | Forward chaining | Hierarchical | Partial order | Total order |
| Número de Atores | Baixo | 5 | 6 | 9 | 6 | 6 |
| Número de Casos de Uso | Médio | 5 | 7 | 10 | 7 | 7 |
| Número de Casos de Uso por Atores | Médio | 6 | 7 | 10 | 7 | 7 |
| Número total de Classes | Alto | 0 | 7 | 9 | 6 | 7 |
| Número total de Atributos | Médio | 5 | 7 | 9 | 7 | 7 |
| Número total de Métodos | Médio | 5 | 7 | 10 | 7 | 7 |
| Número total de Associações | Alto | 1 | 5 | 6 | 5 | 5 |
| Características | Características | Backward chaining | Forward chaining | Hierarchical | Partial order | Total order |
| Número total de Agregação | Médio | 5 | 7 | 9 | 6 | 6 |
| Número total de Generalização | Médio | 4 | 7 | 9 | 7 | 7 |
| Número total de Hierarquias | Alto | 0 | 7 | 9 | 6 | 7 |
| DIT Máximo | Alto | 0 | 7 | 9 | 6 | 7 |
| HAgg Máximo | Baixo | 2 | 6 | 8 | 6 | 6 |
| Número total de estados | Alto | 0 | 7 | 9 | 6 | 7 |
| Número total de ações de entrada | Médio | 6 | 7 | 9 | 7 | 7 |
| Número total de ações de saída | Médio | 5 | 7 | 9 | 6 | 6 |
| Número total de ações | Médio | 5 | 7 | 10 | 7 | 7 |
| Número total de transições | Médio | 7 | 7 | 9 | 7 | 7 |
| MÉDIA | MÉDIA | 3,59 | 6,76 | 9,00 | 6,41 | 6,65 |

Fonte: Autor

Tabela 28 – Média de eficiência das técnicas de planej. nas características do domínio Storage (cont.)

[[TABELA 28: 19 linhas x 8 colunas]]
| Características | Características | Plan Space | State Space | Graph based | Heuristc search | SAT based | Knowledge based |
| Número de Atores | Baixo | 6 | 6 | 5 | 8 | 4 | 9 |
| Número de Casos de Uso | Médio | 7 | 6 | 6 | 9 | 5 | 9 |
| Número de Casos de Uso por Atores | Médio | 7 | 7 | 6 | 9 | 5 | 9 |
| Número total de Classes | Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| Número total de Atributos | Médio | 7 | 7 | 7 | 9 | 6 | 9 |
| Número total de Métodos | Médio | 7 | 6 | 6 | 9 | 5 | 9 |
| Número total de Associações | Alto | 6 | 4 | 5 | 6 | 5 | 5 |
| Número total de Agregação | Médio | 7 | 6 | 6 | 8 | 4 | 9 |
| Número total de Generalização | Médio | 8 | 6 | 6 | 8 | 6 | 8 |
| Número total de Hierarquias | Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| DIT Máximo | Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| HAgg Máximo | Baixo | 7 | 5 | 6 | 8 | 4 | 8 |
| Número total de estados | Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| Número total de ações de entrada | Médio | 7 | 7 | 6 | 9 | 5 | 9 |
| Número total de ações de saída | Médio | 6 | 6 | 6 | 8 | 4 | 9 |
| Número total de ações | Médio | 7 | 6 | 6 | 9 | 5 | 9 |
| Número total de transições | Médio | 7 | 7 | 7 | 9 | 5 | 10 |
| MÉDIA | MÉDIA | 7,12 | 6,06 | 6,24 | 8,76 | 4,65 | 8,71 |

Fonte: Autor

4° passo: a tabela 29 mostra o cálculo da média das médias de desempenho dos planejadores com base nas técnicas de planejamento. Partindo das médias das notas obtidas pelas técnicas de planejamento na tabela 28, calcula-se a nota de desempenho da cada planejador a partir da média das notas de cada técnica que este planejador utiliza. Por exemplo, o planejador Blackbox utiliza as técnicas state-space, total-order,  forward-chaning, graph-based e SAT-based. Calculando a média das notas dessas técnicas de planejamento, obtemos a nota do planejador (6,17) para o domínio Storage.

Tabela 29 – Média das médias da eficiência dos planejadores para o domínio Storage.

[[TABELA 29: 13 linhas x 11 colunas]]
|  | Blackbox | IPP | FF | R | LPG | Fast D. | YAHSP | SGPlan | SatPlan | MaxPlan |
| State-Space | 6,06 | 6,06 | 6,06 | 6,06 |  | 6,06 | 6,06 |  |  |  |
| Plan-Space |  |  |  |  | 7,12 |  |  | 7,12 | 7,12 | 7,12 |
| Partial-order |  |  |  | 6,41 | 6,41 |  |  | 6,41 | 6,41 | 6,41 |
| Total-order | 6,65 | 6,65 | 6,65 |  |  | 6,65 | 6,65 |  |  |  |
| Hierarchical |  |  |  |  |  | 9,00 |  |  |  |  |
| Forward-chaining | 6,76 | 6,76 | 6,76 | 6,76 | 6,76 | 6,76 | 6,76 | 6,76 | 6,76 | 6,76 |
| Backward-chaining |  |  |  | 3,59 |  |  |  |  |  |  |
| Graph-based | 6,24 | 6,24 | 6,24 |  | 6,24 |  | 6,24 |  | 6,24 | 6,24 |
| Knowledge-based |  |  |  |  |  |  | 8,71 |  |  |  |
| SAT-based | 4,65 |  |  |  |  |  |  |  | 4,65 | 4,65 |
| Heurist Search |  |  | 8,76 |  | 8,76 | 8,76 | 8,76 |  |  |  |
| MÉDIA | 6,1 | 6,4 | 6,85 | 5,7 | 7,05 | 7,4 | 7,19 | 6,76 | 6,23 | 6,23 |

Fonte: Autor

5° passo: a tabela 30 mostra o ranking dos planejadores mais promissores para resolução de problemas no domínio Storage. Esse ranking foi criado com base nas médias calculadas na tabela 29.

Tabela 30 – Ranking dos planejadores proposto para resolver problemas no domínio Storage.

[[TABELA 30: 11 linhas x 3 colunas]]
| Posição | Planejador | Média |
| 1° | Fast Downward | 7,4 |
| 2° | YAHSP | 7,2 |
| 3° | LPG | 7,0 |
| 4° | FF | 6,9 |
| 5° | SGPlan | 6,8 |
| 6° | IPP | 6,5 |
| 7° | SatPlan | 6,3 |
| 8° | MaxPlan | 6,3 |
| 9° | Blackbox | 6,2 |
| 10° | R | 5,7 |

Fonte: Autor

6° passo: a tabela 31 mostra o real desempenho dos planejadores no domínio Storage. O domínio LPG obteve uma eficiência de 90% e o IPP apenas de 40%.

Tabela 31 – Resultado da eficiência dos planejadores no domínio Storage.

[[TABELA 31: 11 linhas x 3 colunas]]
| Posição | Planejador | Nota |
| 1° | LPG | 9 |
| 2° | YAHSP | 8 |
| 3° | FF | 6 |
| 4° | Fast Downward | 6 |
| 5° | SGPlan | 6 |
| 6° | MaxPlan | 6 |
| 7° | SatPlan | 5 |
| 8° | IPP | 4 |
| 9° | Blackbox | 0 |
| 10° | R | 0 |

Fonte: Autor

Para o domínio Storage, o ranking de planejadores criado demonstrou uma margem de acerto de 50%. Apesar do melhor planejador neste domínio (LPG) não ter ficado em primeiro lugar do ranking, os cinco primeiros planejadores do ranking foram os que apresentaram os melhores resultados. Pela quantidade de domínios e planejadores considerados no método que cria o ranking de planejadores, esse resultado mostra-se satisfatório.

### Domínio Zeno-travel

O domínio Zeno-travel envolve transportar pessoas em aviões, usando duas formas de movimento: rápido e lento. O movimento rápido dos aviões consome mais combustível que o movimento lento. Esse detalhe faz com que a busca por um plano de boa qualidade seja mais difícil.

1° passo: modelagem do domínio em UML.P. As figuras 31, 32 e 33 mostram os diagrama de casos de uso, classes e estados.

Figura 31 – Diagrama de casos de uso do domínio Zeno-travel modelado no itSIMPLE.

Fonte: Autor

Figura 32 – Diagrama de classes do domínio Zeno-travel modelado no itSIMPLE.

Fonte: Autor

Figura 33 – Diagramas de estados do domínio Zeno-travel modelado no itSIMPLE.

Fonte: Autor

2° passo: identificação e contabilização das características do domínio Zeno-travel. A tabela 32 relaciona as características encontradas, seus valores e classificação.

Tabela 32 – Métricas e características do domínio Zeno-travel.

[[TABELA 32: 18 linhas x 3 colunas]]
| Características | Zeno-travel | Classificação |
| Número de Atores | 2,00 | Alto |
| Número de Casos de Uso | 5,00 | Médio |
| Número de Casos de Uso por Atores | 0,40 | Alto |
| Número total de Classes | 4,00 | Médio |
| Número total de Atributos | 6,00 | Médio |
| Número total de Métodos | 5,00 | Médio |
| Número total de Associações | 2,00 | Baixo |
| Número total de Agregação | 2,00 | Médio |
| Número total de Generalização | 2,00 | Médio |
| Número total de Hierarquias | 1,00 | Médio |
| DIT Máximo | 1,00 | Médio |
| HAgg Máximo | 1,00 | Baixo |
| Número total de estados | 3,00 | Baixo |
| Número total de ações de entrada | 2,00 | Baixo |
| Número total de ações de saída | 2,00 | Baixo |
| Número total de ações | 5,00 | Médio |
| Número total de transições | 5,00 | Baixo |

Fonte: Autor

3° passo: cálculo da média de eficiência de cada técnica de planejamento considerando os valores obtidos nas as tabelas 19 e 20. As tabelas 33 e 34 mostram os valores e as médias de eficiência das técnicas de planejamento no domínio Zeno-travel.

Tabela 33 – Média de eficiência das técnicas de planej. nas características do domínio Zeno-travel.

[[TABELA 33: 19 linhas x 7 colunas]]
| Características | Características | Backward chaining | Forward chaining | Hierarchical | Partial order | Total order |
| Número de Atores | Alto | 4 | 8 | 10 | 8 | 8 |
| Número de Casos de Uso | Médio | 5 | 7 | 10 | 7 | 7 |
| Número de Casos de Uso por Atores | Alto | 0 | 7 | 9 | 6 | 7 |
| Número total de Classes | Médio | 5 | 7 | 9 | 6 | 7 |
| Número total de Atributos | Médio | 5 | 7 | 9 | 7 | 7 |
| Número total de Métodos | Médio | 5 | 7 | 10 | 7 | 7 |
| Número total de Associações | Baixo | 7 | 7 | 10 | 7 | 7 |
| Número total de Agregação | Médio | 5 | 7 | 9 | 6 | 6 |
| Número total de Generalização | Médio | 4 | 7 | 9 | 7 | 7 |
| Número total de Hierarquias | Médio | 4 | 7 | 9 | 7 | 7 |
| DIT Máximo | Médio | 4 | 7 | 9 | 7 | 7 |
| HAgg Máximo | Baixo | 2 | 6 | 8 | 6 | 6 |
| Número total de estados | Baixo | 1 | 5 | 6 | 5 | 5 |
| Número total de ações de entrada | Baixo | 1 | 5 | 6 | 5 | 5 |
| Número total de ações de saída | Baixo | 6 | 7 | 8 | 7 | 7 |
| Número total de ações | Médio | 5 | 7 | 10 | 7 | 7 |
| Número total de transições | Baixo | 3 | 6 | 9 | 6 | 5 |
| MÉDIA | MÉDIA | 3,88 | 6,71 | 8,82 | 6,53 | 6,59 |

Fonte: Autor

Tabela 34 – Média de eficiência das técnicas de planej. das características do domínio Zeno-travel (cont.)

[[TABELA 34: 19 linhas x 8 colunas]]
| Características | Características | Plan Space | State Space | Graph based | Heuristc search | SAT based | Knowledge based |
| Número de Atores | Alto | 9 | 7 | 8 | 10 | 7 | 10 |
| Número de Casos de Uso | Médio | 7 | 6 | 6 | 9 | 5 | 9 |
| Número de Casos de Uso por Atores | Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| Número total de Classes | Médio | 7 | 6 | 6 | 8 | 5 | 9 |
| Número total de Atributos | Médio | 7 | 7 | 7 | 9 | 6 | 9 |
| Número total de Métodos | Médio | 7 | 6 | 6 | 9 | 5 | 9 |
| Número total de Associações | Baixo | 7 | 7 | 6 | 9 | 4 | 10 |
| Número total de Agregação | Médio | 7 | 6 | 6 | 8 | 4 | 9 |
| Número total de Generalização | Médio | 8 | 6 | 6 | 8 | 6 | 8 |
| Número total de Hierarquias | Médio | 8 | 6 | 6 | 8 | 6 | 8 |
| DIT Máximo | Médio | 8 | 6 | 6 | 8 | 6 | 8 |
| HAgg Máximo | Baixo | 7 | 5 | 6 | 8 | 4 | 8 |
| Número total de estados | Baixo | 6 | 4 | 5 | 6 | 5 | 5 |
| Número total de ações de entrada | Baixo | 6 | 4 | 5 | 6 | 5 | 5 |
| Número total de ações de saída | Baixo | 8 | 7 | 7 | 8 | 8 | 8 |
| Número total de ações | Médio | 7 | 6 | 6 | 9 | 5 | 9 |
| Número total de transições | Baixo | 7 | 5 | 5 | 7 | 4 | 7 |
| MÉDIA | MÉDIA | 7,29 | 5,88 | 6,12 | 8,24 | 5,24 | 8,24 |

Fonte: Autor

4° passo: cálculo da média das médias de desempenho dos planejadores com base nas médias das técnicas de planejamento obtidas nas tabelas 33 e 34. A tabela 35 mostra o índice de desempenho da cada planejador.

Tabela 35 – Média das médias da eficiência dos planejadores para o domínio Zeno-travel.

[[TABELA 35: 13 linhas x 11 colunas]]
|  | Blackbox | IPP | FF | R | LPG | Fast D. | YAHSP | SGPlan | SatPlan | MaxPlan |
| State-Space | 5,88 | 5,88 | 5,88 | 5,88 |  | 5,88 | 5,88 |  |  |  |
| Plan-Space |  |  |  |  | 7,29 |  |  | 7,29 | 7,29 | 7,29 |
| Partial-order |  |  |  | 6,53 | 6,53 |  |  | 6,53 | 6,53 | 6,53 |
| Total-order | 6,59 | 6,59 | 6,59 |  |  | 6,59 | 6,59 |  |  |  |
| Hierarchical |  |  |  |  |  | 8,82 |  |  |  |  |
| Forward-chaining | 6,71 | 6,71 | 6,71 | 6,71 | 6,71 | 6,71 | 6,71 | 6,71 | 6,71 | 6,71 |
| Backward-chaining |  |  |  | 3,88 |  |  |  |  |  |  |
| Graph-based | 6,12 | 6,12 | 6,12 |  | 6,12 |  | 6,12 |  | 6,12 | 6,12 |
| Knowledge-based |  |  |  |  |  |  | 8,24 |  |  |  |
| SAT-based | 5,24 |  |  |  |  |  |  |  | 5,24 | 5,24 |
| Heurist Search |  |  | 8,24 |  | 8,24 | 8,24 | 8,24 |  |  |  |
| MÉDIA | 6,10 | 6,32 | 6,70 | 5,75 | 6,90 | 7,24 | 6,90 | 6,84 | 6,40 | 6,40 |

Fonte: Autor

5° passo: criação do ranking dos planejadores para resolução de problemas no domínio Zeno-travel. A tabela 36 representa o ranking dos planejadores, criado com base nas médias calculadas na tabela 35.

Tabela 36 – Ranking dos planejadores proposto para resolver problemas no domínio Zeno-travel.

[[TABELA 36: 11 linhas x 3 colunas]]
| Posição | Planejador | Média |
| 1° | Fast Downward | 7,24 |
| 2° | YAHSP | 6,90 |
| 3° | LPG | 6,90 |
| 4° | SGPlan | 6,84 |
| 5° | FF | 6,70 |
| 6° | SatPlan | 6,40 |
| 7° | MaxPlan | 6,40 |
| 8° | IPP | 6,32 |
| 9° | Blackbox | 6,10 |
| 10° | R | 5,75 |

Fonte: Autor

6° passo: validação do ranking com os resultados reais do planejamento. A tabela 37 representa os valores de desempenho dos planejadores obtidos na resolução dos problemas de planejamento do domínio Zeno-travel.

Tabela 37 – Resultado da eficiência dos planejadores no domínio Zeno-travel.

[[TABELA 37: 11 linhas x 3 colunas]]
| Posição | Planejador | Nota |
| 1° | LPG | 10 |
| 2° | YAHSP | 10 |
| 3° | FF | 10 |
| 4° | Fast Downward | 10 |
| 5° | SGPlan | 10 |
| 6° | MaxPlan | 10 |
| 7° | SatPlan | 8 |
| 8° | IPP | 8 |
| 9° | Blackbox | 7 |
| 10° | R | 5 |

Fonte: Autor

O domínio Zeno-travel é um domínio mais simples em relação ao domínio Storage. A maioria dos planejadores conseguiu resolver todos os problemas deste domínio. Em relação ao ranking de planejadores, ficou comprovado que os planejadores indicados como sendo os piores para resolver problemas do Zeno-travel, realmente tiveram os piores desempenhos.

### Domínio Elevator

O domínio Elevator é baseado no controlador de elevadores Miconic-10, desenvolvido pela Schindler Elevadores. O problema consiste em controlar um sofisticado elevador para transportar seus passageiros aos seus destinos. Porém, existem algumas restrições na movimentação do elevador. O movimento do elevador deve considerar a prioridade dos passageiros, os passageiros que precisam ser transportados sem paradas até os seus destinos e passageiros que precisam estar acompanhados para serem transportados.

1° passo: as figuras 34, 35 e 35 mostram a modelagem do domínio Elevator em UML.P através dos diagrama de casos de uso, classes e estados.

Figura 34 – Diagrama de casos de uso do domínio Elevator modelado no itSIMPLE.

Fonte: Autor

Figura 35 – Diagrama de classes do domínio Elevator modelado no itSIMPLE.

Fonte: Autor

Figura 36 – Diagrama de estados do domínio Elevator modelado no itSIMPLE.

Fonte: Autor

2° passo: a tabela 38 mostra as características identificadas no domínio Elevator e seus respectivos valores e classificação.

Tabela 38 – Métricas e características do domínio Elevator.

[[TABELA 38: 18 linhas x 3 colunas]]
| Características | Elevator | Classificação |
| Número de Atores | 2,0 | Alto |
| Número de Casos de Uso | 6,0 | Alto |
| Número de Casos de Uso por Atores | 0,3 | Médio |
| Número total de Classes | 3,0 | Baixo |
| Número total de Atributos | 13,0 | Alto |
| Número total de Métodos | 9,0 | Alto |
| Número total de Associações | 3,0 | Baixo |
| Número total de Agregação | 1,0 | Médio |
| Número total de Generalização | 0,0 | Baixo |
| Número total de Hierarquias | 0,0 | Baixo |
| DIT Máximo | 0,0 | Baixo |
| HAgg Máximo | 1,0 | Baixo |
| Número total de estados | 7,0 | Alto |
| Número total de ações de entrada | 8,0 | Alto |
| Número total de ações de saída | 8,0 | Alto |
| Número total de ações | 10,0 | Alto |
| Número total de transições | 15,0 | Alto |

Fonte: Autor

3° passo: cálculo da média de eficiência das técnicas de planejamento com base nos valores obtidos nas tabelas 19 e 20. As tabelas 39 e 40 relacionam os valores de eficiência das técnicas de planejamento em cada uma das características do domínio Elevator, exibindo no fim as médias de eficiência.

Tabela 39 – Média de eficiência das técnicas de planej. nas características do domínio Elevator.

[[TABELA 39: 19 linhas x 7 colunas]]
| Características | Características | Backward chaining | Forward chaining | Hierarchical | Partial order | Total order |
| Número de Atores | Alto | 4 | 8 | 10 | 8 | 8 |
| Número de Casos de Uso | Alto | 4 | 7 | 8 | 7 | 7 |
| Número de Casos de Uso por Atores | Médio | 6 | 7 | 10 | 7 | 7 |
| Número total de Classes | Baixo | 10 | 8 | 10 | 9 | 7 |
| Número total de Atributos | Alto | 0 | 4 | 4 | 4 | 4 |
| Número total de Métodos | Alto | 4 | 7 | 8 | 7 | 7 |
| Número total de Associações | Baixo | 7 | 7 | 10 | 7 | 7 |
| Número total de Agregação | Médio | 5 | 7 | 9 | 6 | 6 |
| Número total de Generalização | Baixo | 8 | 7 | 9 | 6 | 7 |
| Número total de Hierarquias | Baixo | 8 | 7 | 9 | 6 | 7 |
| DIT Máximo | Baixo | 8 | 7 | 9 | 6 | 7 |
| HAgg Máximo | Baixo | 2 | 6 | 8 | 6 | 6 |
| Número total de estados | Alto | 0 | 7 | 9 | 6 | 7 |
| Número total de ações de entrada | Alto | 5 | 7 | 10 | 8 | 7 |
| Número total de ações de saída | Alto | 5 | 7 | 10 | 8 | 7 |
| Número total de ações | Alto | 4 | 7 | 8 | 7 | 7 |
| Número total de transições | Alto | 5 | 7 | 10 | 7 | 8 |
| MÉDIA | MÉDIA | 5,00 | 6,88 | 8,88 | 6,76 | 6,82 |

Fonte: Autor

Tabela 40 – Média de eficiência das técnicas de planej. nas características do domínio Elevator (cont.)

[[TABELA 40: 19 linhas x 8 colunas]]
| Características | Características | Plan Space | State Space | Graph based | Heuristc search | SAT based | Knowledge based |
| Número de Atores | Alto | 9 | 7 | 8 | 10 | 7 | 10 |
| Número de Casos de Uso | Alto | 8 | 7 | 7 | 8 | 6 | 10 |
| Número de Casos de Uso por Atores | Médio | 7 | 7 | 6 | 9 | 5 | 9 |
| Número total de Classes | Baixo | 8 | 7 | 7 | 9 | 6 | 10 |
| Número total de Atributos | Alto | 5 | 3 | 4 | 6 | 2 | 9 |
| Número total de Métodos | Alto | 8 | 7 | 7 | 8 | 6 | 10 |
| Número total de Associações | Baixo | 7 | 7 | 6 | 9 | 4 | 10 |
| Número total de Agregação | Médio | 7 | 6 | 6 | 8 | 4 | 9 |
| Número total de Generalização | Baixo | 6 | 7 | 6 | 9 | 4 | 10 |
| Número total de Hierarquias | Baixo | 6 | 7 | 6 | 9 | 4 | 10 |
| DIT Máximo | Baixo | 6 | 7 | 6 | 9 | 4 | 10 |
| HAgg Máximo | Baixo | 7 | 5 | 6 | 8 | 4 | 8 |
| Número total de estados | Alto | 8 | 6 | 7 | 10 | 4 | 9 |
| Número total de ações de entrada | Alto | 8 | 6 | 7 | 9 | 5 | 10 |
| Número total de ações de saída | Alto | 8 | 6 | 7 | 9 | 5 | 10 |
| Número total de ações | Alto | 8 | 7 | 7 | 8 | 6 | 10 |
| Número total de transições | Alto | 7 | 7 | 7 | 10 | 5 | 10 |
| MÉDIA | MÉDIA | 7,24 | 6,41 | 6,47 | 8,71 | 4,76 | 9,65 |

Fonte: Autor

4° passo: cálculo da média das médias de desempenho dos planejadores com base nas médias das técnicas de planejamento obtidas nas tabelas 39 e 40. A tabela 41 mostra o índice de desempenho de cada planejador.

Tabela 41 – Média das médias da eficiência dos planejadores para o domínio Elevator.

[[TABELA 41: 13 linhas x 11 colunas]]
|  | Blackbox | IPP | FF | R | LPG | Fast D. | YAHSP | SGPlan | SatPlan | MaxPlan |
| State-Space | 6,41 | 6,41 | 6,41 | 6,41 |  | 6,41 | 6,41 |  |  |  |
| Plan-Space |  |  |  |  | 7,24 |  |  | 7,24 | 7,24 | 7,24 |
| Partial-order |  |  |  | 6,76 | 6,76 |  |  | 6,76 | 6,76 | 6,76 |
| Total-order | 6,82 | 6,82 | 6,82 |  |  | 6,82 | 6,82 |  |  |  |
| Hierarchical |  |  |  |  |  | 8,88 |  |  |  |  |
| Forward-chaining | 6,88 | 6,88 | 6,88 | 6,88 | 6,88 | 6,88 | 6,88 | 6,88 | 6,88 | 6,88 |
| Backward-chaining |  |  |  | 5,00 |  |  |  |  |  |  |
| Graph-based | 6,47 | 6,47 | 6,47 |  | 6,47 |  | 6,47 |  | 6,47 | 6,47 |
| Knowledge-based |  |  |  |  |  |  | 9,65 |  |  |  |
| SAT-based | 4,76 |  |  |  |  |  |  |  | 4,76 | 4,76 |
| Heurist Search |  |  | 8,71 |  | 8,71 | 8,71 | 8,71 |  |  |  |
| MÉDIA | 6,26 | 6,64 | 7,05 | 6,26 | 7,21 | 7,54 | 7,49 | 6,96 | 6,42 | 6,42 |

Fonte: Autor

5° passo: criação do ranking dos planejadores para resolução de problemas no domínio Elevator. A tabela 42 representa o ranking dos planejadores, criado com base nas médias calculadas na tabela 41.

Tabela 42 – Ranking dos planejadores proposto para resolver problemas no domínio Elevator.

[[TABELA 42: 11 linhas x 3 colunas]]
| Posição | Planejador | Média |
| 1° | Fast Downward | 7,54 |
| 2° | YAHSP | 7,49 |
| 3° | LPG | 7,21 |
| 4° | FF | 7,05 |
| 5° | SGPlan | 6,96 |
| 6° | IPP | 6,64 |
| 7° | SatPlan | 6,42 |
| 8° | MaxPlan | 6,42 |
| 9° | R | 6,26 |
| 10° | Blackbox | 6,26 |

Fonte: Autor

6° passo: validação do ranking com os resultados reais do planejamento. A tabela 43 representa os valores de desempenho dos planejadores obtidos na resolução dos problemas de planejamento do domínio Elevator.

Tabela 43 – Resultado da eficiência dos planejadores no domínio Elevator.

[[TABELA 43: 11 linhas x 3 colunas]]
| Posição | Planejador | Nota |
| 1° | Fast Downward | 10 |
| 2° | YAHSP | 10 |
| 3° | LPG | 10 |
| 4° | FF | 10 |
| 5° | R | 10 |
| 6° | SGPlan | 8 |
| 7° | IPP | 8 |
| 8° | SatPlan | 7 |
| 9° | MaxPlan | 7 |
| 10° | Blackbox | 1 |

Fonte: Autor

No domínio Elevator, o ranking obteve uma taxa de acerto de 50%. Entretanto, o planejador R apresentou um desempenho totalmente diferente do previsto. Da mesma forma que ocorreu em problemas do domínio mundo de blocos, o System R conseguiu resolver todos os problemas do domínio Elevator mantendo uma taxa constante de aumento de tempo na resolução de problemas cada vez mais complexos.

A tabela 44 compara as características do domínio Mundo de Bloco com as características do domínio Elevator. A comparação mostra que os domínios são muito similares em relação as suas características (mais da metade das características são iguais). As técnicas de planejamento utilizadas pelo planejador R são eficientes em domínios com essas características e a distorção criada no ranking de planejadores (tabela 42) se deve, principalmente, pela falta de dados de desempenho de planejadores similares ao planejador R, que é o único planejador estudado que utiliza a técnica backward-chaning.

Tabela 44 – Comparação entre características dos domínios Mundo de Blocos e Elevator.

[[TABELA 44: 18 linhas x 3 colunas]]
| Métricas / Domínios | Blocks W. | Elevator |
| Número de Atores | Baixo | Alto |
| Número de Casos de Uso | Médio | Alto |
| Número de Casos de Uso por Atores | Médio | Médio |
| Número total de Classes | Baixo | Baixo |
| Número total de Atributos | Médio | Alto |
| Número total de Métodos | Médio | Alto |
| Número total de Associações | Baixo | Baixo |
| Número total de Agregação | Médio | Médio |
| Número total de Generalização | Baixo | Baixo |
| Número total de Hierarquias | Baixo | Baixo |
| DIT Máximo | Baixo | Baixo |
| HAgg Máximo | Alto | Baixo |
| Número total de estados | Médio | Alto |
| Número total de ações de entrada | Alto | Alto |
| Número total de ações de saída | Alto | Alto |
| Número total de ações | Médio | Alto |
| Número total de transições | Médio | Alto |

Fonte: Autor

# Conclusões e trabalhos futuros

## Conclusões

Os resultados deste trabalho mostraram que existe uma relação entre características de domínios e técnicas de planejamento. Algumas características extraídas da UML.P demonstram ser mais relevantes e ter mais impacto sobre as técnicas de planejamento: essas características são: Número de Casos de Uso por Atores, Número total de Atributos, Número total de Agregação, Número total de ações de entrada, Número total de Associações e Número total de transições.

Em relação às técnicas de planejamento, um grupo seleto obteve os melhores desempenhos em relação às características de domínios estudadas. Novos planejadores serão mais promissores, de acordo com o método, se possuírem uma ou mais destas técnicas: Heuristic Search, Hierarchical, Knowledge-based, Forward-chaining, Plan-Space e Total-order.

A utilização do ranking de planejadores também demonstrou ser uma boa ferramenta para auxiliar na escolha do planejador para resolver um problema de um determinado domínio. Independente do problema, apenas com as características do domínio, é possível escolher através do método proposto os planejadores que terão melhor desempenho.

Os resultados também mostraram que, quanto mais características de domínios forem extraídas e mais planejadores e técnicas de planejamento incluídas no método, melhor será o resultado do ranking de planejadores.

Portanto, da mesma forma que é fácil perceber que um domínio trivial, com apenas um único objeto, por exemplo, terá seus problemas resolvidos por todos planejadores, ficou demonstrado que os diagramas da UML podem fornecer características que demonstram a complexidade de um domínio através da quantidade de classes, atributos e relações de agregação, associação e herança entre os objetos. Essa complexidade afeta o desempenho das técnicas de planejamento, e conseqüentemente, dos planejadores.

## Trabalhos futuros

Novos trabalhos podem ser desenvolvidos para agregar mais valor à pesquisa feita nesta dissertação. As principais sugestões são:

Implementação no itSIMPLE da identificação e contabilização automática das métricas, geração do ranking e sugestão de planejadores para resolução de problemas em quaisquer domínios;

Implementação no itSIMPLE da agregação automática de mais resultados na tabela de características de domínios x técnicas de planejamento. Esses novos dados seriam obtidos de todos os resultados de planejamentos executados dentro da ferramenta;

Maior detalhamento das técnicas de planejamento para fazer um cruzamento melhor com as características de domínios. Esses detalhes poderiam envolver a heurística utilizada pelo planejador, o processo de construção da árvore de busca e até mesmo a quebra de uma técnica de planejamento em sub-técnicas e algoritmos;

Estabelecer pesos para diferentes características de domínios para tentar melhorar o índice de acerto na escolha do melhor planejador;

Utilizar domínios artificiais (BARRETT e WELD, 1994) para construir diversos tipos de domínios, com várias combinações de características, para melhorar o método e o resultado do ranking de planejadores;

A partir de um banco de dados maior de planejadores, técnicas de planejamento, domínios, características de domínios e resultados de planejamento, fazer uma análise estatística para definir melhor a discretização dos valores das características em Alto, Médio e Baixo;

Utilizar aprendizado indutivo para gerar regras (árvore de decisão) sobre a tabela de características de domínios para classificar as características em Alto, Médio e Baixo;

Análise aprofundada do impacto das características dos domínios nas técnicas de planejamento. Sabendo qual é o impacto que cada característica promove em cada uma das técnicas, seria possível criar novas técnicas de planejamento e planejadores mais eficientes e eficazes.

Referências

BACCHUS, F. Resultados da segunda competição internacional de planejamento. AIPS2000, 2000. Disponivel em: <http://www.cs.toronto.edu/aips2000/SelfContainedAIPS-2000.ppt>. Acesso em: 14 dez. 2009.

BARRET, A.; WELD, D. Partial Order Planning: Evaluation Possible Efficiency Gains. Universidade de Washington. Washington. 1992.

BARRETT, A.; WELD, D. S. Partial-order planning. Evaluating possible efficiency gains. Artificial Intelligence, 67, Maio 1994. 71-112.

BLUM, A.; FURST, M. Fast planning through planning graph analysis. Anais do International Joint Conference on Artificial Intelligence, Montreal, Agosto 1995. 1636-1642.

BONET, B.; GEFFNER, H. HSP: Planning as heuristic search. AIPS-98 Planning Competition, Pittsburgh, Junho 1998. 5-33.

CHAPMAN, D. Planning for Conjunctive Goals. Artificial Intelligence, 32, 1987. 333-377.

CHEN, Y.; HSU, C.; WAH, B. W. SGPlan: Subgoal Partitioning and Resolution in Planning. Benjamin W. Wah Homepage, 2004. Disponivel em: <http://manip.crhc.uiuc.edu/programs/SGPlan/>. Acesso em: 02 nov. 2008.

CURRIE, K.; TATE, A. O-Plan: the Open Planning Architecture. Artificial Intelligence, 52, 1991. 49-86.

DIJKSTRA, E. A note on two problems in connexion with graphs. Numerische Mathematik, Heidelberg, 1, Dezembro 1959. 269-271.

EDELKAMP, S.; HELMERT, M. MIPS The Model-Checking Integrated Planning System. AI Magazine, 22, n. 3, 2001. 67-71.

EDELKAMP, S.; HOFFMANN, J.; LITTMAN, M. Resultados da quarta competição internacional de planejamento. AIPS2004, 2004. Disponivel em: <http://ls5-www.cs.tu-dortmund.de/~edelkamp/ipc-4/results.html>. Acesso em: 14 dez. 2009.

FIKES, R.; NILSSON, N. Strips: A new approach to the application of theorem proving to problem solving. Journal of Artificial Intelligence, 1971. 2(3-4).

FOX, M.; LONG, D. Resultados da terceira competição internacional de planejamento. AIPS2002, 2002. Disponivel em: <http://planning.cis.strath.ac.uk/competition/results.html>. Acesso em: 14 dez. 2009.

GENERO, M.; MIRANDA, D.; PIATTINI, M. Defining and Validating Metrics for UML Statechart Diagrams. Universidade de Castilla - La Mancha. Cidade Real. 2002.

GENERO, M.; PIATTINI, M. Empirical validation of measures for class diagram structural complexity. Universidade de Castilla - La Mancha. Cidade Real. 2001.

GEREVINI, A.; BONET, B.; GIVAN, B. Resultados da quinta competição internacional de planejamento. AIPS2006, 2006. Disponivel em: <http://zeus.ing.unibs.it/ipc-5/icaps06-ipc-slides.pdf>. Acesso em: 14 dez. 2009.

GEREVINI, A.; SAETTI, A.; SERINA, I. An Empirical Analysis of Some Heuristic Features for Local Search in LPG. Proceedings of the Fourteenth International Conference on Automated Planning and Scheduling, Whistler, 2004. 171-180.

GEREVINI, A.; SERINA, I. LPG: a Planner based on Local Search for Planning Graphs. Proceedings of the Sixth International Conference on Artificial Intelligence Planning and Scheduling (AIPS02), Toulouse, 2002. Disponivel em: <http://prometeo.ing.unibs.it/lpg/>. Acesso em: 02 nov. 2008.

GHALLAB, M.; NAU, D.; TRAVERSO, P. Automated Planning: Theory and Practice. [S.l.]: Morgan Kaufmann, 2004.

GRUYTER, W. D. De motu animalium. In: Aristotelis Opera. Berlim: Ed. de I. Bekkeri, v. I, 1960.

HART, P.; NILSSON, N.; RAPHAEL, B. A Formal Basis for the Heuristic Determination of Minimum Cost Paths. Boletim ACM SIGART, Nova Iorque, Dezembro 1972. 28-29.

HELMERT, M. The Fast Downward Planning System. Journal of Artificial Intelligence Research, 2006. 191-246. Disponivel em: <http://www.informatik.uni-freiburg.de/~helmert/publications.htm>. Acesso em: 02 nov. 2008.

HOFFMANN, J. FF Local Search Topology in Planning Benchmarks: An Empirical Analysis. Universidade Albert Ludwigs. [S.l.], p. 453-458. 2001. ftp://ftp.informatik.uni-freiburg.de/documents/papers/ki/hoffmann-ijcai-01.pdf.

HOFFMANN, J. Extending FF to numerical state variables. Anais da15º Conferência Européia sobre Inteligência Artificial (ECAI-02), Lyon, 2002. 571-575.

HOFFMANN, J.; NEBEL, B. The FF planning system: Fast plan generation through heuristic search. Journal of Artificial Intelligence Research, 14, 2001. 253-302.

HOFFMANN, J.; NEBEL, B. The FF planning system: fast plan generation through heuristic search. Journal of Artificial Intelligence Research, 14, Janeiro 2001. 253-302. Disponivel em: <http://members.deri.at/~joergh/ff.html>. Acesso em: 02 nov. 2008.

IN, P.; KIM, S.; BARRY, M. UML-based Object-Oriented Metrics for Architecture Complexity Analysis. Texas. 2003.

ITSIMPLE Project. Design Lab. Universidade de São Paulo, 2008. Disponivel em: <http://designlab.grupoe.com.br/itSIMPLE>. Acesso em: 14 dez. 2009.

KAUTZ, H. A.; SELMAN, B.; HOFFMANN, J. SatPlan: Planning as satisfiability. Anais da 5º Competição Internacional de Planejamento. [S.l.]: [s.n.]. 2006.

KAUTZ, H.; SELMAN, B. BlackBox - a SAT technology planning system. BlackBox, 1998. Disponivel em: <http://www.cs.rochester.edu/u/kautz/satplan/blackbox/index.html>. Acesso em: 02 nov. 2008.

KAUTZ, H.; SELMAN, B. Unifying sat-based and graph-based planning. Anais da International Joint Conferences on Artificial Intelligence, Stockholm, 1999. 318-325.

KOEHLER, J. IPP. IPP Homepage, 1998. Disponivel em: <http://www.informatik.uni-freiburg.de/~koehler/ipp.html>. Acesso em: 02 nov. 2008.

LARMAN, C. Utilizando UML e Padrões. 3° edição. ed. São Paulo: Editora Bookman Companhia, 2007.

LIN, F. A Planner Called R. AI Magazine, 2001. 73-76.

MCALLESTER, D.; ROSENBLITT, D. Systematic Nonlinear Planning. American Association for Artificial Intelligence - AAAI, 1991.

MCDERMOTT, D. AIPS98 Planning Competition Results. AIPS98 Planning Competition, 2008. Disponivel em: <http://ipc.icaps-conference.org/>. Acesso em: 14 dez. 2009.

MCDERMOTT, D. et al. PDDL - The Planning Domain Definition Langage. Centro de Controle e Visão Computacional de Yale. [S.l.]. 1998.

MINTON, S. Learning effective search control knowledge: an explanation approach. [S.l.]: Kluwer Academic Publishers, 1988.

NEWELL, A.; SHAW, J. C.; SIMON, H. Report on a general problem-solving program. Anais da Conferência Internacional de Processamento de Informações. [S.l.]: [s.n.]. 1959. p. 256-264.

NILSSON, N. J. Shakey the robot. SRI AI Center. Menlo Park. 1984.

PEDNAULT, E. ADL: Exploring the middle ground between STRIPS and situation calculus. Anais da Primeira Conferência Internacional sobre princípios da representação do conhecimento e raciocínio, 1989. 324-332.

PENBERTHY, J. S.; WELD, D. UCPOP: A sound, complete, partial order planner for ADL. Anais da Tereceira Conferência Internacional sobre representação do conhecimento e raciocínio, Boston, 1992. 103-114.

RUMBAUGH, J. et al. Modelagem e Projeto de Sistemas Baseados em Objetos. Rio de Janeiro: Editora Campus, 1994.

RUMBAUGH, J.; BOOCH, G.; JACOBSON, I. UML - Guia do Usuário. 2° edição. ed. São Paulo: Editora Campus, 2006.

RUSSELL, S.; NORVIG, P. Artificial Intelligence: A Modern Approach. [S.l.]: Prentice Hall, 2002.

SACERDOTI, E. Planning in a Hierarchy of Abstraction Spaces. Artificial Intelligence, 1974. 115-135.

SACERDOTI, E. A Structure for Plans and Bahaviors. New York: North Holland, 1977.

SELMAN, B.; KAUTZ, H. A. Planning as satisfiability. Anais da 10º Conferência Européia sobre Inteligência Artificial, Vienna, 1992. 359-363.

SELMAN, B.; KAUTZ, H. A.; COHEN, B. Noise strategies for improving local search. Anais da 12º Conferência Nacional sobre Inteligência Artificial (AAAI), Seattle, Julho 1994. 337-343.

SELMAN, B.; LEVESQUE, H.; MITCHELL, D. A new method for solving hard satisfiability problems. Anais da Décima Conferência Nacional sobre Inteligência Artificial, San Jose, Julho 1992. 440-446.

SIAU, K.; CAO, Q. Unified Modeling Language (UML) - A Complexity Analysis. Universidade de Nebraska-Lincoln. Tese de Doutorado. Hershey. 2006.

TATE, A. Generalizing project networks. Anais da First International Joint Conference on Artificial Intelligence, 1977. 888-893.

TONIDANDEL, F. Implementação e Desenvolvimento de um Sistema de Planejamento Baseado em Casos. Universidade de São Paulo.Tese de Doutorado. São Paulo. 2003.

VAQUERO, T. S. ITSIMPLE: ambiente integrado de modelagem e análise de domínios de planejamento automático. Universidade de São Paulo. Dissertação de Mestrado. São Paulo. 2007.

VIDAL, V. A lookahead strategy for solving large planning problems. Universidade Pau Sabatier. Toulouse, p. http://www.cril.univ-artois.fr/~vidal/yahsp.html. 2002. (2002-35-R).

WILKINS, D. E. Representation in a domain-independent planner. Anais da International Joint Conferences on Artificial Intelligence, Karlsruhe, 1983.

XING, Z.; CHEN, Y.; ZHANG, W. MaxPlan: Optimal Planning by Decomposed Satisfiability and Backward Reduction. Quinta Competição Internacional de Planejamento. [S.l.]: [s.n.]. 2006. p. 53-56.

YANG, Q. Intelligente Planning: A Decomposition and Abstraction Based Approach. Berlin: Springer-Verlag, 1997.

YANG, Q.; TENENBERG, J. ABTWEAK: Abstracting a Nonlinear, Least Commitment Planner. Anais da Conferência Internacional sobre Inteligência Artificial (AAAI), Boston, 1990. 204-209.

YOURDON, E. Análise Estruturada Moderna. Rio de Janeiro: Editora Campus, 1996.
