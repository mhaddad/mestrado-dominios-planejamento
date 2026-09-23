<!-- Rascunho de IA para o autor revisar antes de enviar -->

# Revisão da dissertação de 2010: diagnóstico e perguntas de pesquisa revisadas

Material para a primeira conversa sobre a revisão da minha dissertação de 2010 (relação entre características de domínios de planejamento, medidas com UML.P no itSIMPLE, e técnicas de planejamento). Passei os últimos dias auditando o texto original contra as fontes primárias dos 10 planejadores e contra a literatura de 2008 a 2026, e o resultado muda mais do que eu esperava em alguns pontos, embora a pergunta de fundo continue de pé. Este documento resume o diagnóstico e termina nas decisões em que preciso da sua opinião.

## 1. Por que revisar agora

A pergunta de 2010 — nenhum planejador é melhor em todos os domínios, e características do domínio podem indicar a técnica mais promissora — não é mais uma hipótese isolada: é o fundamento de um campo que se consolidou depois de 2010, sob o nome de seleção de algoritmos e portfólios de planejadores [@rice1976algorithm]. Desde então, portfólios por regra fixa ou por classificador treinado passaram a vencer trilhas inteiras das IPCs [@helmert2011fast; @katz2018delfi; @cenamor2016ibacop], a unidade de previsão migrou do domínio para a instância [@kerschke2019automated], *features* automáticas de PDDL (grafo causal, DTG, *treewidth*) substituíram largamente a extração manual [@helmert2009concise; @hoffmann2011analyzing], e heurísticas aprendidas já superam LAMA em pelo menos um dos três domínios de validação de 2010 [@ferber2022neural; @toyer2020asnets]. Os LLMs são a novidade mais recente: como planejadores autônomos têm desempenho baixo, mas como tradutores para PDDL acoplados a um planejador clássico, o resultado sobe muito — o que reabre, de outro ângulo, a pergunta de 2010 sobre ajuste entre características e técnica.

## 2. Diagnóstico da versão de 2010

Extraí 349 afirmações substantivas do texto (frase a frase, com trecho literal conferido por script). Classificação: **268 mantém, 76 reformula, 5 descarta**. A leitura por capítulo é clara: a descrição de método, domínios e história do campo se sustenta quase toda; o que precisa mudar se concentra onde o texto **tira conclusões** — 32 das 69 afirmações de resultado são "reformula", e 17 das 21 afirmações de Conclusões e trabalhos futuros. Os oito vereditos centrais (A1–A8) ficam: **mantém** A1 (com reformulação) e A4 (com ressalva); **reformula** A2, A3, A5 e A7; **descarta** A6 (taxonomia) e A8 (trabalhos relacionados, na forma atual). Nenhuma das cinco afirmações descartadas por si sós é conclusão central: quatro são números da revisão histórica das competições, contrariados pelos resultados oficiais, e uma (AF-214, planejadores SAT como *forward-chaining*) é a base textual do problema da taxonomia.

Três achados pesam mais que os outros:

**A taxonomia de técnicas das Tabelas 2–4 não se sustenta contra as fontes primárias dos próprios planejadores.** O Fast Downward está descrito nas próprias palavras como "planejador de progressão heurística" [@helmert2006fast], não como *Hierarchical* — a decomposição hierárquica é só como se calcula a heurística causal. Os planejadores SAT (Blackbox, SATPlan, MaxPlan) não são *forward-chaining*: quem busca é o *solver* sobre uma codificação proposicional de horizonte fixo, e o próprio texto de 2010 declara essa equivalência como convenção própria, não como leitura das fontes. A raiz é estrutural, não pontual: os 11 rótulos de 2010 misturam pelo menos quatro dimensões independentes — algoritmo de busca, heurística, representação de estado e arquitetura do sistema —, e famílias inteiras de hoje (busca por largura/novidade, busca simbólica, portfólios) simplesmente não cabem nela [@rintanen2014madagascar; @torralba2017efficient; @coles2012survey].

**G20 — o *ranking* previsto quase não muda entre os três domínios de validação.** A correlação de postos entre os *rankings* previstos para Storage, Zeno-travel e Elevator é de 0,94 a 0,99. Uma linha de base sem nenhuma característica de domínio (a nota média de cada planejador nos 10 domínios de treino) acerta os mesmos cinco primeiros em Storage e Zeno-travel, e 4 de 5 no Elevator, com correlação de postos próxima da do método publicado (0,75×0,81 em Storage; 0,68×0,86 em Zeno; 0,65×0,65 no Elevator). `[HIPÓTESE]` Com 10 planejadores e 3 domínios de validação, essa diferença não sustenta a conclusão de que as características do domínio melhoram a escolha — boa parte da previsão parece refletir a qualidade geral dos planejadores, não o ajuste característica-técnica. Isso pesa direto sobre A3 (a promessa central do capítulo de validação).

**F3 — as métricas UML medem o modelo, não o problema, e dependem de convenções da UML.P.** Aqui quero ser preciso sobre o que a auditoria mostra, porque a UML.P é sua, não minha: não é um defeito do instrumento nem do seu desenho — é uma propriedade dele, que 2010 não tornou explícita. A contagem manual de classes de 2010 excluiu classes auxiliares (*Utility*, *Global*) sem documentar o critério; o artigo de 2005 do itSIMPLE mostra que a ferramenta **impõe** as classes `Planner`, `Environment` e `Agent` em todo modelo [@vaquero2005itsimple] — parte do que parecia "classe auxiliar" excluída por escolha do modelador é, na verdade, estrutura fixa da própria ferramenta. Separadamente, a literatura mostra que reordenar ou reconfigurar sintaticamente um modelo, sem mudar o que ele significa, muda o desempenho dos planejadores e inverte *rankings* — um mesmo planejador variou do 2º ao 11º lugar só por reordenação [@vallati2021importance]. `[HIPÓTESE]` Como 2010 não relata ter controlado a ordem com que o itSIMPLE serializa o PDDL exportado, parte da variação atribuída a "características do domínio" pode estar confundida com decisões de serialização do modelo — não é uma refutação, é uma lacuna de controle que a Fase 3 pode fechar.

Ainda em aberto: 38 afirmações de confiança baixa (a maioria pede conferência de fonte, sem afetar as conclusões centrais); 11 fontes novas (as de 9 planejadores e dos dois trabalhos relacionados) ainda estão em verificação antes de entrar nas referências; e **G10** — o segundo bloco de 20 características do `script.sql`, nunca publicado, com valores diferentes do bloco 1 em 43 de 85 pares — segue sem explicação.

## 3. O que a revisão propõe

**Perguntas de pesquisa revisadas:**

- **Q1.** As conclusões de 2010 se sustentam com mais planejadores, mais domínios e método estatístico adequado?
- **Q2.** As métricas estruturais de modelagem orientada a objetos acrescentam poder preditivo às *features* modernas extraídas de PDDL (grafo causal, DTG)?
- **Q3.** Onde os LLMs entram no mapa das técnicas: como planejador, como tradutor de domínio ou como seletor?
- **Q4.** O princípio de ajuste entre características da tarefa e estratégia de solução ajuda a escolher configurações de agente de IA no desenvolvimento de software?

**Nova taxonomia em quatro dimensões**, reclassificando os 10 planejadores pela fonte primária de cada um (`auditoria/taxonomia-tecnicas.md`):

| Planejador | (1) Busca | (2) Heurística | (3) Representação | (4) Arquitetura |
|---|---|---|---|---|
| Blackbox | grafo de planejamento → SAT/CSP | sem heurística própria | SAT/CNF | único, SAT-solver plugável |
| IPP | grafo de planejamento (extração) | sem heurística | STRIPS/ADL sobre grafo | único |
| FF | progressiva no espaço de estados | relaxação (*delete relaxation*) | STRIPS proposicional | único |
| System R | decomposição recursiva por metas | sem heurística numérica | STRIPS proposicional | único |
| LPG(-TD) | busca local em planos parciais | avaliação heurística de vizinhos | grafos de ação | único |
| Fast Downward | progressiva no espaço de estados | grafo causal | variáveis multivaloradas | único |
| YAHSP | progressiva com *lookahead* | relaxação (herdada do FF) | STRIPS proposicional | único |
| SGPlan | decomposição/particionamento | relaxação do Metric-FF | PDDL2.2 particionado | decomposição interna, base fixa |
| SATPlan | grafo de planejamento → SAT/CSP | sem heurística própria | SAT/CNF | único |
| MaxPlan | SAT/CSP com decomposição por subobjetivo | sem heurística própria | SAT (MDF) | único |

Oito pontos dessa reclassificação ainda são decisões minhas em aberto (onde fica System R, se SGPlan conta como portfólio, etc. — lista completa na seção 7 de `taxonomia-tecnicas.md`), mas a estrutura de quatro dimensões já está decidida.

**Desenho da Fase 3, em níveis** (`auditoria/reexecucao.md`): Nível 1 reproduz fielmente o método de 2010 sobre os mesmos dados, sem correção nenhuma; Nível 2 aplica sobre os mesmos dados as correções já decididas (taxonomia de 4 dimensões, rótulo invertido, contagens corrigidas, medidas de acerto que tratem empates); Nível 3 reexecuta os planejadores sob condições padronizadas (mesmo hardware, timeout, memória — hoje 38 pares vêm de competição e 62 de execução própria, com condições diferentes); Nível 4 amplia para *benchmarks* 1998–2023, extratores automáticos de *features* (UML e PDDL) e os dois níveis de análise, por domínio e por instância, reportados separadamente. Cada nível isolado do seguinte, para que uma mudança de número tenha causa rastreável.

## 4. Onde preciso da sua opinião

1. **A nova taxonomia em quatro dimensões faz sentido para você?** Ela substitui os 11 rótulos de 2010, que misturam dimensões e em vários casos não têm apoio na fonte primária do planejador, por algoritmo/espaço de busca, heurística, representação e arquitetura. Já decidi tratar *Partial-order* e *Total-order* como atributo do plano, fora das técnicas; outras sete escolhas menores estão registradas como provisórias (seção 7 de `taxonomia-tecnicas.md`) e gostaria da sua opinião sobre elas.
2. **Métricas UML × *features* de PDDL (Q2):** proponho testar as duas, nos mesmos domínios, controlando a ordem de serialização do modelo — resultado negativo também é resultado. Sabendo que a tradução PDDL→UML.P impõe convenções da própria ferramenta (classes fixas, ordem de exportação), essa comparação lhe parece justa com o instrumento, ou há um ajuste metodológico que eu deveria fazer antes?
3. **G10:** o `script.sql` de 2010 guarda um segundo bloco de 20 características para os domínios 6 a 10, com valores diferentes do bloco 1 em 43 de 85 pares e 3 características sem definição, nunca publicado. Você lembra o que eram?
4. **Escopo:** incluir LLMs (Q3) e abrir uma ponte hipotética com desenvolvimento de software dirigido por IA (Q4) é expansão de escopo em relação a 2010. Faz sentido para você, ou prefere que eu mantenha a revisão mais perto do trabalho original?
5. **Artigo além da dissertação:** o produto principal será a dissertação revisada em padrão ABNT. Vale também preparar um artigo com os resultados da Fase 3 (por exemplo, o teste de métricas UML contra *features* de PDDL)? Se sim, para qual veículo?
