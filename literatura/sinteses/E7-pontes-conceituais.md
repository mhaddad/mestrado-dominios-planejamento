---
tipo: sintese-de-eixo
eixo: E7
obras: 20
data: 2026-09-22
---

# E7 — Pontes conceituais

## 1. Pergunta e resposta curta

Que arcabouços teóricos, fora do planejamento, sustentam a ideia de ajuste entre tarefa e técnica, e como o roteamento entre modelos de linguagem retoma a seleção de algoritmos? Cinco linhagens convergem para a mesma estrutura lógica — características de um problema predizem qual técnica funciona melhor: o teorema *No Free Lunch* [@wolpert1997no; @sterkenburg2021nofreelunch; @gomez2016empirical], a teoria da contingência organizacional [@lawrence1967differentiation; @donaldson2006contingency], o *task-technology fit* [@goodhue1995task; @furneaux2011task; @davern2007towards; @howard2019refining; @soodan2024ai; @passmore2025if], o problema de seleção de algoritmos de Rice — meta-aprendizado e *instance space analysis* [@smithmiles2009cross; @smithmiles2014towards; @smithmiles2023instance; @vanschoren2019metalearning] — e o roteamento de LLMs [@ong2024routellm; @hu2024routerbench; @chen2023frugalgpt; @moslem2026dynamic; @wu2024large]. Nenhum desses arcabouços, isoladamente, autoriza a Q4 (transferir o ajuste tarefa-técnica para a escolha de configurações de agentes de IA em desenvolvimento de software): cada um tem um alcance formal preciso, e a soma deles não fecha a lacuna entre "ajuste é um princípio geral plausível" e "existe uma métrica testada de ajuste tarefa-agente de IA". A ponte da Q4 é, neste eixo, inteiramente hipótese de trabalho.

## 2. Os arcabouços

### No Free Lunch (NFL)

Wolpert e Macready provam que o desempenho médio de qualquer par de algoritmos, somado sobre *todas* as funções de custo possíveis com *prior* uniforme, é idêntico [@wolpert1997no]. Os próprios autores alertam que nenhuma classe de problemas enfrentada na prática tem *prior* uniforme, e que desempenho bom depende do "alinhamento" entre algoritmo e a distribuição real dos problemas de interesse [@wolpert1997no]. Sterkenburg e Grünwald reforçam essa leitura no aprendizado supervisionado: algoritmos padrão são justificáveis em relação a um modelo/viés de entrada, não por uma equivalência cética universal [@sterkenburg2021nofreelunch]. Gómez e Rojas trazem evidência empírica de que o NFL, em classificação real, convive com diferenças relevantes de desempenho entre algoritmos [@gomez2016empirical].

### Teoria da contingência organizacional

Lawrence e Lorsch estudaram seis empresas químicas e mostraram, com testes estatísticos, que o desempenho está associado ao ajuste entre os atributos de cada subsistema organizacional e a certeza do respectivo subambiente, e que diferenciação e integração são antagônicas — as organizações de melhor desempenho conseguem as duas coisas [@lawrence1967differentiation]. Donaldson revisita os desafios da teoria da contingência e propõe os conceitos de *quasi-fit* e *hetero-performance*, mas essa nota foi lida apenas por resumo de terceiros, não confirmado na fonte primária [@donaldson2006contingency].

### Task-Technology Fit (TTF)

Goodhue e Thompson propõem que uma tecnologia de informação só afeta o desempenho individual se for utilizada **e** se tiver bom ajuste com as tarefas que apoia; o modelo recebeu suporte moderado em dados de mais de 600 indivíduos [@goodhue1995task]. Furneaux revisa essa literatura [@furneaux2011task] e Davern propõe uma teoria unificada de fit, criticando a fragmentação conceitual entre construtos como TTF e ajuste cognitivo [@davern2007towards]. Howard e Rose refinam o construto introduzindo o "desajuste" (*misfit*) bidirecional — tecnologia insuficiente ou excessiva para a tarefa [@howard2019refining]. Duas aplicações recentes testam TTF em ferramentas de IA: Soodan et al. encontram que TTF prevê a intenção de uso contínuo de chatbots por docentes [@soodan2024ai], e Passmore, Daly e Tee mostram, em entrevistas com doze gestores, que TTF sozinho não explica o valor de um agente de coaching de IA — fatores éticos, de percepção e organizacionais também importam [@passmore2025if].

### Seleção de algoritmos, meta-aprendizado e *instance space analysis*

Smith-Miles (2009) organiza, sob o arcabouço do *algorithm selection problem* de Rice (1976), desenvolvimentos paralelos e fragmentados em várias disciplinas que tentam prever, a partir de características do problema, qual algoritmo terá melhor desempenho [@smithmiles2009cross]. Vanschoren formaliza essa mesma lógica como meta-aprendizado: coleta sistemática de meta-dados (incluindo *meta-features* de tarefas) para acelerar o aprendizado em novas tarefas [@vanschoren2019metalearning]. Smith-Miles e colegas (2014) propõem a metodologia que seria formalizada como *Instance Space Analysis* (ISA), mapeando regiões do espaço de instâncias em que o desempenho de um algoritmo se afasta da média [@smithmiles2014towards]; o tutorial de 2023 consolida a ISA como forma de testar algoritmos objetivamente e avaliar a diversidade de conjuntos de teste, criticando a prática padrão de reportar apenas desempenho médio [@smithmiles2023instance].

### Roteamento de modelos de linguagem

RouteLLM treina roteadores binários entre um LLM forte e um fraco a partir de dados de preferência humana, alcançando redução de custo com qualidade equivalente em benchmarks [@ong2024routellm]. RouterBench propõe um benchmark padronizado com mais de 405 mil resultados de inferência para avaliar sistemas de roteamento por custo e desempenho [@hu2024routerbench]. FrugalGPT usa cascatas de LLMs, mostrando complementaridade de erros entre modelos baratos e caros [@chen2023frugalgpt]. A revisão de Moslem e Kelleher organiza esse campo em seis paradigmas e um "pipeline de controle" de três estágios [@moslem2026dynamic]. AS-LLM estende o problema de seleção de algoritmos usando LLMs para extrair *features* do próprio algoritmo (não só do problema), superando métodos que só caracterizam o problema em 8 de 10 cenários do ASLib [@wu2024large].

## 3. O que cada arcabouço autoriza e não autoriza afirmar

| Arcabouço | Autoriza afirmar | Não autoriza afirmar |
|---|---|---|
| No Free Lunch [@wolpert1997no; @sterkenburg2021nofreelunch] | Não existe algoritmo universalmente superior em média sobre *todas* as funções de custo com *prior* uniforme; desempenho bom exige "alinhamento" com a distribuição real de problemas | Que a distribuição real de domínios de planejamento (ou de tarefas de software) não é uniforme; que características observáveis de um domínio predizem qual técnica funciona melhor nele; qualquer conclusão sobre planejamento, UML, PDDL ou agentes de IA especificamente |
| Teoria da contingência [@lawrence1967differentiation; @donaldson2006contingency] | Em seis organizações da indústria química, em 1967, desempenho esteve associado ao ajuste entre atributos de subsistema e certeza do subambiente, medido com teste estatístico | Que a mesma estrutura se aplica a algoritmos, planejadores ou agentes de IA; é evidência sobre organizações humanas, uma única indústria, amostra pequena, e não uma teoria geral de sistemas técnicos |
| Task-Technology Fit [@goodhue1995task; @furneaux2011task; @davern2007towards; @howard2019refining] | Ajuste entre requisitos de uma tarefa e características de uma tecnologia **já em uso** está associado a desempenho individual (suporte moderado, dados de mais de 600 pessoas) | Escolha **prévia** entre alternativas de tecnologia para uma tarefa (é isso que TTF não modela: mede ajuste de uso, não seleção *ex ante*); qualquer aplicação a planejamento automatizado ou a agentes de IA de desenvolvimento de software, que nenhuma das obras testa |
| Seleção de algoritmos / meta-aprendizado / ISA [@smithmiles2009cross; @smithmiles2014towards; @smithmiles2023instance; @vanschoren2019metalearning] | Existe um arcabouço formal (espaço de problemas, de *features*, de algoritmos, de desempenho) amplamente aplicado em múltiplas disciplinas — classificação, otimização combinatória, coloração de grafos, *timetabling* — para prever desempenho de algoritmo a partir de características do problema, com metodologia para mapear e visualizar variação de desempenho no espaço de instâncias | Que esse arcabouço foi aplicado a planejamento automatizado (não foi, ver seção 7) ou a agentes de IA de desenvolvimento de software; a estrutura formal é genérica, mas cada aplicação exige dados e *features* próprios do domínio |
| Roteamento de LLMs [@ong2024routellm; @hu2024routerbench; @chen2023frugalgpt; @moslem2026dynamic; @wu2024large] | Roteadores/cascatas entre LLMs, treinados com dados de preferência humana ou de desempenho observado em benchmarks gerais (Chatbot Arena, MMLU, GSM8K, MT Bench), reduzem custo mantendo qualidade — é seleção de algoritmo operacional e testada, para modelos de linguagem em tarefas gerais | Que esse mecanismo funciona para tarefas de desenvolvimento de software especificamente (nenhum artigo testa isso); que o roteamento usa características estruturais explícitas da tarefa (usa preferência/desempenho observado, não *features* estruturais ao estilo das métricas UML de 2010) |

## 4. Roteamento de modelos de linguagem como seleção de algoritmos

O que se repete: a estrutura formal é a mesma do *algorithm selection problem* de Rice — um espaço de tarefas de entrada, um conjunto de "técnicas" (aqui, LLMs), uma medida de desempenho e um mecanismo que escolhe a técnica para cada entrada [@hu2024routerbench; @wu2024large]. Como em meta-aprendizado, nenhum LLM domina em todas as consultas: FrugalGPT mostra complementaridade de erros entre modelos baratos e caros — GPT-3 acerta 13% dos casos em que GPT-4 erra em COQA [@chen2023frugalgpt] — o mesmo fenômeno, em outro domínio, que justifica a busca por seleção condicional em vez de uma técnica universal.

O que muda: primeiro, o sinal de treino. RouteLLM aprende com dados de preferência humana (Chatbot Arena) e desempenho em benchmarks gerais, não com características estruturais explícitas da tarefa de entrada [@ong2024routellm] — diferente de 2010, que usa métricas estruturais de UML como *features* explícitas do domínio. Segundo, a direção da caracterização: AS-LLM caracteriza tanto o problema quanto o próprio algoritmo (a partir do código-fonte), tratando a relação como bidirecional, e mostra que essa informação adicional é o principal fator de ganho de desempenho — a maior perda no estudo de ablação vem de remover justamente as *features* do algoritmo [@wu2024large]. 2010 caracteriza apenas o domínio, nunca a técnica em si além de um rótulo de taxonomia. Terceiro, a maturidade do aparato avaliativo: RouterBench formaliza um benchmark padronizado com mais de 405 mil execuções [@hu2024routerbench], ordens de grandeza acima da amostra de 13 domínios de 2010, e a revisão de Moslem e Kelleher nota que mesmo essa literatura mais recente sofre de falta de métrica, conjunto de modelos e base de custo compartilhados entre estudos — o mesmo problema, em escala diferente, da fragilidade F6 de 2010 (dados fora das competições) [@moslem2026dynamic].

## 5. Relação com a dissertação de 2010 e com a Q4

| Rótulo/pergunta | O que a literatura permite | Marcação | Chaves |
|---|---|---|---|
| A1 | O NFL, a contingência, o TTF, a seleção de algoritmos e o roteamento de LLMs compartilham a mesma lógica estrutural de A1 (características predizem desempenho de técnica) — mas nenhum confirma A1 empiricamente para planejamento automatizado | [HIPÓTESE] | @wolpert1997no, @sterkenburg2021nofreelunch, @gomez2016empirical, @smithmiles2009cross, @vanschoren2019metalearning, @hu2024routerbench, @wu2024large |
| A3 | ISA problematiza A3: desempenho médio por classe de característica pode esconder variação relevante dentro da classe; a diversidade real das instâncias precisaria ser mapeada, não assumida | [HIPÓTESE] (leitura crítica, não teste direto em planejamento) | @smithmiles2023instance, @smithmiles2014towards, @wu2024large |
| A4 | Meta-aprendizado sustenta, por analogia, que mais meta-dados melhoram a capacidade preditiva — mesma lógica de A4 | [HIPÓTESE] | @vanschoren2019metalearning |
| A6/F4 | O roteamento de LLMs mostra, por contraste, como construir uma taxonomia sistemática (seis paradigmas, dimensões explícitas) — modelo metodológico, não correção direta da taxonomia de 2010 | [HIPÓTESE] | @moslem2026dynamic |
| A7/F5 | ISA e RouteLLM (métrica APGR) criticam, por analogia, a redução de "eficiência" a um único número agregado como a cobertura de 2010 | [HIPÓTESE] | @smithmiles2023instance, @ong2024routellm |
| F1 | Smith-Miles (2009) é a ponte formal entre 2010 e a literatura de seleção de algoritmos que 2010 nunca cita | [FATO] (a lacuna de citação é fato; a adequação da ponte é leitura) | @smithmiles2009cross |
| F2 | ISA e RouterBench evidenciam, por contraste de escala, a fragilidade de amostra pequena de 2010 (13 domínios vs. mapeamento de espaço de instâncias ou 405 mil execuções) | [HIPÓTESE] | @smithmiles2014towards, @smithmiles2023instance, @hu2024routerbench |
| Q4 | Nenhuma obra testa ajuste tarefa-agente de IA em desenvolvimento de software; TTF aplicado a IA (coaching, chatbots) mostra que ajuste sozinho não basta — fatores éticos, de percepção e organizacionais também pesam | [HIPÓTESE] (a própria Q4 é hipótese; a literatura só a informa, não a confirma) | @goodhue1995task, @furneaux2011task, @davern2007towards, @howard2019refining, @passmore2025if, @soodan2024ai, @lawrence1967differentiation |

## 6. Divergências e pontos em disputa

Há uma disputa real sobre o que o NFL autoriza dizer. A leitura cética radical ("nenhum algoritmo é melhor que outro, ponto final") é a que mais aparece em usos informais do teorema; Sterkenburg e Grünwald argumentam explicitamente contra essa leitura, defendendo justificativa relativa a modelo [@sterkenburg2021nofreelunch], e os próprios Wolpert e Macready já delimitam esse alcance no artigo original [@wolpert1997no]. Isso importa para este eixo porque o exagero mais comum é justamente invocar o NFL como se ele *provasse* que ajuste tarefa-técnica funciona — quando, na melhor leitura, ele apenas remove o obstáculo de um "algoritmo universal" sem estabelecer o argumento positivo.

Há também uma tensão entre o TTF clássico e a Q4 que nenhuma nota resolve completamente: Goodhue e Thompson [@goodhue1995task] e Furneaux [@furneaux2011task] descrevem ajuste no uso de uma tecnologia já adotada por uma pessoa; a Q4 quer um construto de seleção prévia entre alternativas. Isso não é uma diferença de detalhe — é uma diferença de o que está sendo medido (ajuste de uso vs. critério de escolha), mais próxima estruturalmente do problema de seleção de algoritmos de Rice do que do TTF propriamente dito. A nota sobre @goodhue1995task já registra essa distinção.

Por fim, há divergência sobre se ajuste tarefa-tecnologia é suficiente para explicar o valor de um agente de IA: Soodan et al. encontram TTF como preditor positivo da intenção de uso contínuo [@soodan2024ai], enquanto Passmore, Daly e Tee encontram que TTF precisa ser combinado com percepção, ética e contexto organizacional para explicar o valor de um agente de coaching [@passmore2025if] — leituras não necessariamente contraditórias (uma mede intenção de uso, a outra valor percebido), mas que ilustram que "ajuste" não é um construto fechado nem consensual, um alerta reforçado pela própria crítica de fragmentação de Davern [@davern2007towards].

## 7. Lacunas

A busca dirigida documentada em `literatura/protocolo/busca/lacunas-memo.md` testou cinco lacunas (L1 a L5) com Crossref, arXiv (inclusive busca em texto completo) e WebSearch. A relevante para este eixo é L5: em quatro strings de busca e três bases, incluindo busca em texto completo no arXiv (que devolveu zero resultados), não foi localizado nenhum trabalho que aplique *Instance Space Analysis* a planejamento automatizado ou clássico. A metodologia está bem estabelecida — o tutorial de 2023 já lido neste eixo é a peça de referência [@smithmiles2023instance] — e já foi aplicada a *job shop scheduling*, *timetabling*, *car sequencing* e *batch scheduling*, mas não a planejamento. O memorando classifica esse veredito como "confirmada" nas bases consultadas, mas registra explicitamente que é ausência de evidência, não prova de inexistência, e que a proximidade entre ISA e a própria pergunta desta dissertação sugere uma lacuna real e uma possível contribuição original da revisão — não apenas um efeito de busca malfeita, mas algo que merece nova verificação antes de qualquer afirmação categórica no texto final.

Uma segunda lacuna correlata (L2) buscou LLMs como seletores de planejador, heurística ou configuração de portfólio: nenhuma das oito strings em quatro bases encontrou esse trabalho especificamente para planejamento — o mais próximo é um LLM configurando solvers de MIP por instância (GRIMIP), tecnicamente adjacente mas fora do escopo de planejamento clássico. Isso significa que a ponte da Q4 (roteamento de LLM aplicado a agentes de desenvolvimento de software, informada pela lógica de seleção de algoritmos aplicada a planejamento) não tem, hoje, nenhum elo intermediário publicado: nem "ISA aplicada a planejamento" nem "LLM selecionando planejador" existem nas bases consultadas. A Q4 salta diretamente de arcabouços gerais (NFL, contingência, TTF, seleção de algoritmos) e de aplicações em domínios distantes (chatbots, coaching, MIP) para uma proposta sobre desenvolvimento de software, sem nenhum degrau intermediário testado.

## 8. Insumos para as próximas fases

Para a Fase 5 formular hipóteses falseáveis em vez de analogias, três insumos deste eixo são diretamente utilizáveis. Primeiro, o arcabouço formal de Rice/Smith-Miles [@smithmiles2009cross] oferece um vocabulário preciso — espaço de problemas, espaço de *features*, espaço de algoritmos, espaço de desempenho — que permite formular uma hipótese testável do tipo "para um conjunto definido de tarefas de desenvolvimento de software T, um conjunto de *features* estruturais F extraídas de T, e um conjunto de agentes A, existe um mapeamento S: T→A cujo desempenho preditivo excede a linha de base aleatória com significância estatística" — em vez da analogia difusa "ajuste tarefa-técnica funciona para agentes de IA também". Segundo, a metodologia ISA [@smithmiles2014towards; @smithmiles2023instance] dá um modelo concreto de como mapear e visualizar o espaço de tarefas de software, incluindo teste objetivo de se uma amostra de tarefas é representativa — respondendo de antemão à fragilidade F2 que already atinge 2010. Terceiro, a bidirecionalidade de AS-LLM (caracterizar também o "algoritmo"/agente, não só a tarefa) [@wu2024large] sugere que qualquer hipótese da Fase 5 deveria especificar *features* do próprio agente (arquitetura, ferramentas disponíveis, *prompt* de sistema), não apenas da tarefa — e o alerta de Howard e Rose sobre desajuste bidirecional (agente pequeno/barato demais vs. grande/caro demais) [@howard2019refining] dá uma variável dependente concreta para testar (tipo de erro por sub- ou superdimensionamento), em vez de uma noção vaga de "ajuste". Por fim, o achado de Passmore, Daly e Tee de que TTF sozinho não basta [@passmore2025if] é um lembrete de que qualquer hipótese da Fase 5 sobre agentes de IA precisaria de variáveis de controle além de características técnicas da tarefa — percepção de quem usa, confiança, contexto organizacional — sob risco de subespecificar o modelo.

## 9. Obras usadas

- @chen2023frugalgpt
- @davern2007towards
- @donaldson2006contingency
- @furneaux2011task
- @gomez2016empirical
- @goodhue1995task
- @howard2019refining
- @hu2024routerbench
- @lawrence1967differentiation
- @moslem2026dynamic
- @ong2024routellm
- @passmore2025if
- @smithmiles2009cross
- @smithmiles2014towards
- @smithmiles2023instance
- @soodan2024ai
- @sterkenburg2021nofreelunch
- @vanschoren2019metalearning
- @wolpert1997no
- @wu2024large
