---
tipo: sintese-de-eixo
eixo: E3
obras: 18
data: 2026-09-22
---

# E3 — Evolução dos planejadores e heurísticas; resultados das IPCs 2008–2023

## 1. Pergunta e resposta curta

Que famílias de técnicas definem o estado da arte em cada trilha das IPCs de 2008 a 2023, e a taxonomia de técnicas de 2010 ainda descreve bem o campo? **[FATO]** Não. As 18 notas do eixo mostram uma trajetória dominada por busca heurística progressiva com *landmarks* (LAMA, 2008) [@richter2010lama; @coles2012survey], seguida da consolidação de heurísticas de abstração (*merge-and-shrink*, *cost partitioning*) [@helmert2009landmarks; @helmert2014merge; @sievers2016analysis; @seipp2020saturated], do surgimento da busca por largura/novidade (*width-based search*) a partir de 2012 [@lipovetzky2012width; @lipovetzky2017bestfirst], do amadurecimento da busca simbólica bidirecional [@torralba2017efficient; @bocchese2018performance] e, na década mais recente, da dominância de planejadores de *portfolio*, muitos deles orientados por aprendizado de máquina [@coles2012survey; @cenamor2019insights; @taitler2024international]. **[HIPÓTESE]** A taxonomia de seis categorias de 2010 (A2/A6) não descreve bem esse campo: ela mistura dimensões distintas — algoritmo de busca, tipo de heurística, arquitetura de sistema e representação de estado — e, mesmo nos casos em que 2010 tinha informação disponível na época (Fast Downward, SAT, SGPlan), a classificação diverge do que os próprios criadores dessas técnicas descrevem em fonte primária.

## 2. O que a literatura estabelece

### Busca heurística progressiva com *landmarks*

O núcleo da linhagem HSP → FF → Fast Downward → LAMA é descrito, em duas fontes primárias independentes, como busca heurística de progressão (*heuristic progression/forward search*), não como técnica hierárquica [@helmert2006fast; @richter2010lama]. LAMA combina heurística FF sensível a custo com uma pseudo-heurística de *landmarks* e busca *anytime* por A* ponderado, e venceu a trilha *satisficing* da IPC-2008 [@richter2010lama]. Quinze anos depois, essa mesma linhagem, usada apenas como referência, ainda superava a maioria dos competidores da IPC-2023 [@taitler2024international].

### Heurísticas admissíveis para planejamento ótimo: relaxação, caminhos críticos, abstrações e *landmarks*

Helmert e Domshlak [-@helmert2009landmarks] formalizam quatro famílias de heurísticas admissíveis e provam relações de dominância entre elas, dando origem à heurística *landmark cut* (hLM-cut). A família de abstrações se desdobra em *merge-and-shrink* [@helmert2014merge; @sievers2016analysis] e em esquemas de *cost partitioning*, incluindo o *saturated cost partitioning* [@seipp2020saturated]. Essas obras mostram que "heurística de busca" não é uma categoria única, mas um espaço de subtécnicas com identidade teórica própria — dimensão que a categoria "*Heuristic Search*" de 2010 (A2) não diferencia.

### Busca por largura e novidade (*width-based search*)

Lipovetzky e Geffner [-@lipovetzky2012width] definem a noção de *width* (largura) de um problema de planejamento e o algoritmo IW; em 2017, combinam essa exploração estrutural com busca heurística dirigida a objetivo no esquema *best-first width search* (BFWS) [@lipovetzky2017bestfirst]. É uma família de técnica inteiramente posterior a 2010 e ausente da taxonomia A2/A6.

### Busca por satisfatibilidade (SAT-based planning)

Rintanen [-@rintanen2012planning; -@rintanen2014madagascar] descreve o planejamento como redução a uma fórmula proposicional que codifica todas as transições possíveis entre todos os passos de tempo simultaneamente, decidida por um solver de SAT (DPLL/CDCL) com heurísticas de seleção de variável especializadas para planos. É uma família transversal (usada também em *model checking*, roteamento de FPGA), com identidade técnica própria, não redutível a busca progressiva nem a busca no espaço de planos.

### Busca simbólica

Torralba et al. [-@torralba2017efficient] tratam explicitamente **direção de busca** (progressão vs. regressão) e **representação de estado** (busca explícita vs. busca simbólica com *Binary Decision Diagrams*) como dimensões ortogonais. Busca simbólica bidirecional cega chegou a superar busca heurística explícita com LM-cut em muitos domínios — um resultado que os próprios autores descrevem como surpreendente [@torralba2017efficient]. A trilha ótima da IPC-2014 foi vencida por um planejador simbólico bidirecional (SymBA-2), com outro planejador simbólico (cGamer-bd) em segundo lugar [@bocchese2018performance].

### Planejadores de *portfolio*, com e sem aprendizado de máquina

A partir de 2011, planejadores de *portfolio* (que combinam ou selecionam entre várias técnicas) passam a vencer trilhas inteiras: Fast Downward Stone Soup venceu a trilha ótima da IPC-2011 [@coles2012survey]; o vencedor determinístico/ótimo da IPC-2018 foi um *portfolio* cuja seleção depende de classificador de ML treinado sobre instâncias de referência [@cenamor2019insights]; e o vencedor da trilha ótima da IPC-2023, Ragnarok, combina busca explícita, desacoplada, simbólica e planejamento *lifted* num único sistema, enquanto os dois primeiros da trilha *satisficing* (Scorpion Maidu, Levitron) também são *portfolios* [@taitler2024international].

### Planejamento *lifted*

Wichlacz, Höller e Hoffmann [-@wichlacz2022landmark] estendem heurísticas de *landmarks* ao cenário *lifted* (sem instanciação total do domínio), mostrando que a distinção instanciado/*lifted* é uma dimensão técnica ativa desde pelo menos 2022, ausente do escopo de 2010.

## 3. Percurso das IPCs 2008–2023

- **IPC-2008:** a página oficial de resultados não lista vencedores por trilha no material acessado [@ipc2008results]; o vencedor vem de fonte indireta: LAMA venceu a trilha *satisficing* sequencial [@richter2010lama].
- **IPC-2011:** LAMA-2011 venceu a trilha determinística/clássica; na ótima, Fast Downward Stone Soup 1 (*portfolio*) superou o vencedor de 2008 (Gamer, busca simbólica); na multicore, ArvandHerd; na de aprendizado, PBP2 [@coles2012survey].
- **IPC-2014:** trilha Optimal vencida por SymBA-2 (busca simbólica bidirecional cega, heurísticas de abstração por perímetro), com cGamer-bd em segundo; Agile vencida por Yahsp3 (*delete-relaxation*), com Madagascar-pC (SAT) em segundo [@bocchese2018performance].
- **IPC-2018:** trilha clássica/ótima vencida por *portfolio* orientado por classificador de ML, margem pequena (~1%); trilha probabilística vencida por PROST-DD [@cenamor2019insights].
- **IPC-2023:** ótima vencida por Ragnarok (*portfolio* híbrido); *satisficing* vencida por Scorpion Maidu e Levitron (*portfolios*); LAMA (2011), só como referência, superou todos os competidores da trilha *agile* [@taitler2024international].
- lequen2026planner não descreve uma IPC específica, mas reavalia 29 planejadores de todas as edições (1998–2023) em hardware uniforme: cobertura crescente das gerações recentes, com planejadores antigos (System R, SimPlanner) ainda competitivos em domínios específicos [@lequen2026planner].

## 4. A taxonomia de 2010 sob revisão (A6/F4)

**[FATO]** A afirmação A6 de 2010 classifica planejadores SAT como *forward-chaining*; SGPlan, SATPlan e MAXPLAN como *plan-space*; e Fast Downward como *Hierarchical*. As notas deste eixo, lidas contra fonte primária de cada técnica, corrigem as três atribuições:

- **Fast Downward = "Hierarchical" (2010) vs. busca heurística progressiva (fonte primária).** O próprio Helmert descreve o sistema como "heuristic progression planner" — busca por progressão de estados, igual a FF —, com a "decomposição hierárquica" restrita ao cálculo interno da heurística causal, não a uma técnica de planejamento hierárquico no sentido HTN/ABSTRIPS [@helmert2006fast]. Richter e Westphal confirmam, de forma independente, que LAMA, construído sobre Fast Downward, segue a mesma linhagem de busca heurística progressiva de HSP, FF e Fast Downward [@richter2010lama].
- **SAT = "forward-chaining" (2010) vs. redução a satisfatibilidade proposicional (fonte primária).** A codificação SAT representa todos os passos de tempo simultaneamente numa única fórmula, decidida por um *solver* de SAT; não há expansão sequencial de estados nem estrutura de planos parciais [@rintanen2014madagascar]. **[HIPÓTESE]** A classificação de 2010 provavelmente associou a direção temporal da codificação (do estado inicial ao horizonte) ao algoritmo de busca, quando o que roda de fato é busca de satisfatibilidade (DPLL/CDCL) sobre uma fórmula global [@rintanen2014madagascar].
- **SGPlan, SATPlan, MAXPLAN = "plan-space" (2010).** Nenhuma nota do eixo trata SGPlan diretamente; para SATPlan/MAXPLAN, vale a mesma correção de SAT-based planning — não são busca no espaço de planos (POCL) [@rintanen2014madagascar]. Torralba et al. mostram ainda que "*plan-space*"/regressão e "busca simbólica" são dimensões distintas, também confundidas em taxonomias planas como a de 2010 [@torralba2017efficient].

**[HIPÓTESE]** A raiz do problema é que a taxonomia de 2010 mistura, sob seis rótulos exclusivos, ao menos quatro dimensões que a literatura deste eixo trata separadamente: (1) **algoritmo de busca** — progressão, regressão, bidirecional, largura/novidade, satisfatibilidade proposicional [@torralba2017efficient; @lipovetzky2012width; @rintanen2014madagascar]; (2) **tipo de heurística** — relaxação *delete*, caminhos críticos, abstrações (*merge-and-shrink*, *pattern databases*), *landmarks*, particionamento de custo [@helmert2009landmarks; @helmert2014merge; @seipp2020saturated]; (3) **representação de estado** — explícita ou simbólica (BDD) [@torralba2017efficient]; (4) **arquitetura de sistema** — planejador único vs. *portfolio*, por regra fixa ou por classificador de ML [@coles2012survey; @cenamor2019insights; @taitler2024international].

**[HIPÓTESE — proposta a validar]** Uma taxonomia melhor separaria essas quatro dimensões em eixos independentes, em vez de forçar cada planejador a uma única categoria. Um planejador seria descrito por uma tupla (algoritmo de busca; família de heurística; representação de estado; arquitetura mono ou multi-planejador), o que permitiria, por exemplo, descrever Fast Downward como (progressão; causal-graph/FF; explícita; único) e um vencedor de 2023 como Ragnarok como (explícita + desacoplada + simbólica + *lifted*; múltiplas; mista; *portfolio*). Essa proposta não foi testada nem aplicada retroativamente aos dez planejadores de 2010 nesta síntese; é uma hipótese de trabalho para a Fase 3 avaliar.

## 5. Relação com a dissertação de 2010

| Rótulo | Veredito | O que a literatura mostra | Chaves |
|---|---|---|---|
| A2 | Amplia | *Heuristic Search* segue central (LAMA, Fast Downward), mas a lista de seis técnicas "promissoras" ficou incompleta: faltam busca por largura, abstrações/*cost partitioning* e *portfolios* | [@helmert2006fast; @richter2010lama; @lipovetzky2012width; @lipovetzky2017bestfirst; @helmert2009landmarks; @coles2012survey] |
| A6 | Corrige | Fast Downward não é *hierarchical* (é progressão heurística); SAT não é *forward-chaining* (é redução a satisfatibilidade); SGPlan/SATPlan/MAXPLAN não são uniformemente *plan-space* | [@helmert2006fast; @richter2010lama; @rintanen2014madagascar; @torralba2017efficient] |
| A1/A3 | Amplia (qualifica) | O fenômeno geral — desempenho depende do domínio — persiste décadas depois, mas nenhum planejador único domina todos os domínios mesmo dentro do mesmo ranking; a evidência é empírica (cobertura por domínio), não testada com o método preditivo de 2010 | [@lequen2026planner; @taitler2024international] |
| A4 | Confirma parcialmente | Mais planejadores e domínios (29 planejadores/28 anos; 33 domínios em 2023) tornam o quadro mais robusto, mas só dentro do mesmo formalismo (clássico determinístico) | [@lequen2026planner; @taitler2024international] |
| F1 | Confirma | LAMA (2008), IPC-2008 em diante e quinze anos de IPCs de 2008 a 2023 ficaram fora do corpus original | [@richter2010lama; @taitler2024international] |
| F4 | Confirma | Taxonomia mistura busca, heurística, representação e arquitetura; múltiplas famílias (largura, abstrações, SAT, simbólica, *portfolio*) não cabem nas seis categorias | [@helmert2006fast; @helmert2009landmarks; @helmert2014merge; @rintanen2012planning; @rintanen2014madagascar; @torralba2017efficient; @lipovetzky2012width; @lipovetzky2017bestfirst; @sievers2016analysis; @seipp2020saturated; @coles2012survey; @cenamor2019insights; @wichlacz2022landmark] |
| F5 | Confirma | Margens de vitória por cobertura podem ser pequenas (~1% em 2018) e sensíveis a hardware/software, questionando cobertura como métrica decisiva | [@cenamor2019insights; @bocchese2018performance] |
| F6 | Confirma | Resultados fora do ambiente oficial da IPC podem não ser comparáveis aos rankings publicados; IPCs recentes ampliaram domínios e formalismos muito além de 2010 | [@bocchese2018performance; @taitler2024international] |
| F2 | Confirma | Rankings mudam conforme o conjunto de domínios/instâncias considerado; amostra de 10 planejadores em 13 domínios (2010) é pequena frente às dezenas de planejadores e dezenas de domínios atuais | [@lequen2026planner; @taitler2024international] |

## 6. Divergências e pontos em disputa

Há tensão não resolvida entre as notas quanto a **como classificar planejadores de *portfolio*** na taxonomia revisada: cenamor2019insights [-@cenamor2019insights] relata debate na comunidade sobre se *portfolios* deveriam sequer contar como vencedores de competição, já que a contribuição técnica está mais no classificador de seleção do que numa técnica de planejamento propriamente dita — e observa que até LAMA já é um caso ambíguo de "quase-*portfolio*" (múltiplas filas de busca com heurísticas diferentes). Não há, nas 18 notas, consenso sobre se *portfolio* é uma "técnica" no mesmo sentido que busca por largura ou SAT, ou uma camada de meta-seleção sobre técnicas — ponto em aberto para a taxonomia da seção 4.

Outra divergência: lequen2026planner [-@lequen2026planner] e taitler2024international [-@taitler2024international] concordam que cobertura agregada cresce com o tempo, mas divergem no que isso implica para A1/A3 — o primeiro enfatiza que planejadores antigos ainda vencem em domínios específicos (favorável a A1), o segundo enfatiza que mesmo entre os mais recentes nenhum domina todos os domínios da mesma trilha (que qualifica A3 sem necessariamente sustentar um ranking fixo por características).

## 7. Lacunas

Nenhuma nota do eixo traz, com trecho citável, a lista completa de vencedores por trilha da IPC-2008 diretamente da fonte oficial [@ipc2008results]; a informação de LAMA como vencedor vem de fonte secundária (o próprio artigo do LAMA). Falta também uma fonte no lote sobre a IPC-2020/2021 (não representada nas 18 notas) e sobre a classificação técnica de SGPlan especificamente — nenhuma obra lida trata desse planejador em detalhe. Duas notas (seipp2020saturated, sievers2016analysis) foram lidas só em resumo, sem acesso ao PDF completo, o que limita a profundidade das afirmações sobre *cost partitioning* e estratégias de *merge*.

## 8. Insumos para as próximas fases

Para qualquer replicação de 2010 na Fase 3, os planejadores e trilhas mais bem documentados neste eixo são: **Fast Downward, LAMA (2008/2011)** e sua linhagem de busca heurística progressiva [@helmert2006fast; @richter2010lama; @coles2012survey]; **Madagascar** (SAT) [@rintanen2014madagascar]; **Gamer/cGamer/SymBA-2** (busca simbólica) [@torralba2017efficient; @bocchese2018performance]; e, para o estado da arte recente, os *portfolios* **Ragnarok, Scorpion Maidu e Levitron** da IPC-2023 [@taitler2024international]. A trilha determinística/clássica (satisficing e ótima) é a mais comparável ao desenho de 2010; as trilhas numérica, HTN, aprendizado e probabilística (introduzidas ou consolidadas depois de 2010) exigiriam adaptação do método original. O trabalho de lequen2026planner [-@lequen2026planner], que reexecuta 29 planejadores históricos em hardware uniforme, é a base mais direta para uma futura comparação com os dez planejadores de 2010 nos mesmos domínios — desde que se confirme antes a equivalência de formulação PDDL entre versões.

## 9. Obras usadas

- @bocchese2018performance
- @cenamor2019insights
- @coles2012survey
- @helmert2006fast
- @helmert2009landmarks
- @helmert2014merge
- @ipc2008results
- @lequen2026planner
- @lipovetzky2012width
- @lipovetzky2017bestfirst
- @richter2010lama
- @rintanen2012planning
- @rintanen2014madagascar
- @seipp2020saturated
- @sievers2016analysis
- @taitler2024international
- @torralba2017efficient
- @wichlacz2022landmark
