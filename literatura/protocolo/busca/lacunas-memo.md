# Memorando de busca dirigida — lacunas L1 a L5

Data da busca: 22/09/2026. Buscador dirigido (Claude Code, claude-sonnet-5), Fase 1, ondas de triagem já concluídas. Bases usadas: Crossref (API `works?query.bibliographic=`), arXiv (API `export.arxiv.org/api/query`, inclusive busca em texto completo `search_query=all:...`), busca web (WebSearch/WebFetch, equivalente a Google/Google Scholar, incluindo páginas oficiais de ICAPS/ICKEPS). Semantic Scholar foi tentado uma vez para L2 e devolveu HTTP 429 (limite de requisições) — não foi usado, conforme já esperado pelo protocolo (seção 2). Antes de registrar qualquer item, seu título foi conferido contra `literatura/protocolo/lista-consolidada.csv` (317 itens já triados); nenhum item novo registrado no CSV desta busca duplica um já existente.

---

## L1 — Métricas estruturais/quantitativas de modelos de domínio (PDDL ou UML/OO) para caracterizar domínios ou predizer desempenho

**Strings e bases (resultados examinados):**
- Crossref `PDDL domain complexity metrics` — 15 resultados examinados, nenhum relevante (métricas de software genéricas, ecologia, bibliometria).
- Crossref `planning domain software metrics UML` — 15 resultados, nenhum relevante (metrics data analysis de sinais, não de PDDL/planejamento).
- Crossref `structural complexity PDDL domain model` — 15 resultados, 1 tangencial (Helmert 2009, representações finitas de PDDL, já semente conhecida de E3, não é sobre métricas de qualidade).
- Crossref `coupling cohesion planning domain model` — 15 resultados, nenhum relevante (todos sobre coesão territorial europeia ou métricas de software genéricas).
- WebSearch `"domain model" quality metrics PDDL planning size complexity predict planner performance` — 9 resultados, achou "On the Effective Configuration of Planning Domain Models" (Vallati, já `E6-027` na lista) e o "General Approach for Configuring PDDL Problem Models" (ICAPS 2018).
- WebSearch `UML class diagram metrics applied planning domain itSIMPLE Genero Piattini` — confirma que os artigos originais de Genero & Piattini (usados na dissertação de 2010) são sobre UML genérico, nunca aplicados a modelos de planejamento.
- WebSearch `metrics predict planner performance domain size number of predicates actions correlation` — achou que "training metrics" não se correlacionam fortemente com desempenho em outro domínio (otimização, não planejamento clássico) e achados dispersos sobre contagem de ações não ser bom preditor isolado.
- WebSearch `domain model design choices affect planner performance PDDL encoding quality software engineering` — achou os dois itens novos mais relevantes: Vallati, Chrpa, McCluskey & Hutter (2021, JAR) e Vallati & Chrpa (2019, K-CAP), ambos sobre como a configuração/qualidade do modelo de domínio afeta o desempenho do planejador.
- WebSearch `composite metric quantify PDDL domain complexity structural semantic characteristics arxiv` e `"PDDL domain complexity" composite metric nine components actions predicates interdependency` — achou SPAR (Huang et al. 2025, arXiv 2509.13691), que propõe uma métrica composta de complexidade de domínios PDDL.
- arXiv, registros confirmados por `id_list` para os 4 itens novos (SPAR 2509.13691; "Understanding and Estimating Domain Complexity Across Domains" 2312.13487, descartado por não ser sobre modelos de planejamento; Energy Impact 2601.21967).

**Itens novos registrados (4, `L1-001` a `L1-004`):** ver `lacunas-bruta.csv`. Nenhum deles usa métricas de engenharia de software no estilo Genero & Piattini (contagem de classes, associações, generalizações, profundidade de herança) aplicadas a modelos UML de planejamento — o recorte exato de 2010. Os mais próximos tratam de configuração estrutural do modelo PDDL (ordem de elementos, acoplamento de ações) e seu efeito no desempenho ou no consumo de energia do planejador, e de uma métrica composta ad hoc de complexidade de PDDL usada para avaliar geração de domínios por LLM.

**Veredito: parcial.**

[FATO] A busca achou quatro trabalhos que relacionam características estruturais do modelo de domínio (ordenação de elementos, acoplamento de ações, complexidade composta de PDDL) ao desempenho do planejador ou ao consumo de energia, nenhum deles já presente na lista consolidada. [FATO] Nenhum resultado, em nenhuma base, aplica explicitamente métricas de diagramas UML de classe/estado (Genero & Piattini ou equivalentes) a modelos de domínio de planejamento para caracterizá-los ou prever desempenho — o recorte específico usado em 2010 no itSIMPLE. [HIPÓTESE] A ausência sugere que a ponte entre métricas de engenharia de software (UML/OO) e modelos de planejamento automatizado, tal como feita na dissertação de 2010, continua pouco explorada pela comunidade de planejamento — que preferiu métricas ad hoc de PDDL (contagem de predicados, ações, interdependência) a arcabouços de métricas de UML estabelecidos.

---

## L2 — LLMs como seletores de planejador, algoritmo ou configuração de portfólio

**Strings e bases (resultados examinados):**
- WebSearch `large language model selects planner algorithm portfolio configuration` — 9 resultados, nenhum sobre LLM selecionando planejador; achados sobre LLM gerando ou avaliando portfólios de otimização (não seleção por instância).
- WebSearch `"LLM" recommends selects planning algorithm configuration per instance portfolio 2024 2025` — 9 resultados; o mais próximo é GRIMIP (Luo et al., arXiv 2606.23299), que usa LLM para configurar solvers de MIP por instância — não é sobre planejadores automatizados nem já está em `lista-consolidada.csv`.
- WebSearch `language model router select heuristic search planner automated planning task` — 9 resultados; achados sobre LLM *gerando* heurísticas (ex.: "Classical Planning with LLM-Generated Heuristics", já teria de ser novo item mas não é sobre *seleção*, é sobre *geração* de heurística) e sobre roteamento entre LLMs (não entre planejadores).
- arXiv (busca em texto completo) `"LLM" AND "planner selection"` — 4 resultados, nenhum relevante (QA de grafos de conhecimento, síntese de fala, orquestração de ferramentas).
- arXiv (texto completo) `"large language model" AND "algorithm selection" AND planning` — 4 resultados, nenhum relevante.
- arXiv (texto completo) `"large language model" AND "portfolio" AND planner` — 1 resultado, irrelevante (pesquisa de investimentos).
- Semantic Scholar `large language model planner selection algorithm configuration` — HTTP 429, não usado.
- Já presente em `lista-consolidada.csv`: `E7-037` "Large Language Model-Enhanced Algorithm Selection" — usa LLM para representar algoritmos dentro de um seletor tradicional, não como o mecanismo de seleção em si, e não é sobre planejamento.

**Nenhum item novo registrado no CSV** (GRIMIP e o E7-037 já existente são de domínios adjacentes — MIP e otimização combinatória geral — não respondem diretamente à pergunta sobre planejadores).

**Veredito: confirmada** — nas bases consultadas.

[FATO] Nenhuma busca (8 strings, 4 bases) encontrou um trabalho em que um LLM escolha o planejador, a heurística ou a configuração de portfólio para uma tarefa de planejamento automatizado. [FATO] Existe trabalho adjacente recente (2025-2026) em que LLMs configuram solvers de programação inteira mista por instância (GRIMIP) e em que LLMs enriquecem a representação de algoritmos para seleção em otimização combinatória geral (`E7-037`, já na lista). [HIPÓTESE] Isso sugere um veredito de ausência de evidência nas bases consultadas, não prova de inexistência: a proximidade temática de GRIMIP indica que a extensão para planejadores é tecnicamente plausível e pode já estar em preprint não indexado ainda pelas bases ou fora do vocabulário de busca usado.

---

## L3 — *Features* de sondagem (*probing features*) na predição de desempenho de planejadores

**Strings e bases (resultados examinados):**
- WebSearch `"probing features" OR "probing runs" algorithm selection planning performance prediction` — 9 resultados; confirma o conceito geral de *probing features* na literatura de seleção de algoritmos.
- WebSearch `Fawcett Vallati Hutter Hoffmann Hoos 2014 "Improved Features for Runtime Prediction of Domain-Independent Planners" probing features` — 10 resultados; **confirma que o item já presente em `lista-consolidada.csv` como `E2-002` (semente do eixo E2) usa exatamente *probing features*** — 16 features extraídas de execuções de sondagem de 1 segundo do Fast Downward, além de outras features de sondagem de LPG-TD e TORCHLIGHT.
- WebSearch `"probing" features short run planner classical planning performance prediction Cenamor de la Rosa` — 9 resultados; confirma que Fawcett et al. (2014) estendeu features de sondagem propostas antes por Cenamor et al., e que "Explainable Planner Selection for Classical Planning" (já `E2-035` na lista) usa features de tarefa interpretáveis para seleção de planejador.
- WebSearch `probing features planner selection portfolio 2020 2021 2022 classical planning short run heuristic` — 9 resultados; nenhum item novo de sondagem pós-2014 fora do que já está na lista (Ferber & Seipp 2022 já `E2-035`; abordagens por GNN/imagem já `E2-006`, `E2-021`, `E2-025`).
- Crossref `probing features planner selection performance prediction` — 15 resultados, nenhum relevante a planejamento (todos de outras áreas: sensores, doenças, seleção de características em ML genérico).

**Nenhum item novo registrado no CSV**: o único item que responde diretamente à lacuna (`E2-002`, Fawcett et al. 2014) já está em `lista-consolidada.csv` como semente do eixo E2, e a regra de não duplicação impede reinserção.

**Veredito: não confirmada** — há literatura, já presente na lista consolidada.

[FATO] O item semente `E2-002` (Fawcett, Vallati, Hutter, Hoffmann, Hoos & Leyton-Brown, ICAPS 2014, já na lista consolidada) usa explicitamente *probing features*: 16 características extraídas de sondagens de 1 segundo do planejador Fast Downward, para predizer o tempo de execução de planejadores independentes de domínio. [FATO] Buscas adicionais por trabalho pós-2014 no mesmo recorte não acharam item novo fora do que já está triado (`E2-009`, `E2-011`, `E2-012`, `E2-035`). [HIPÓTESE] A lacuna apontada pelos triadores provavelmente refletia o fato de o item semente estar registrado sob o rótulo genérico de "features de runtime", sem destacar que uma parte delas é de sondagem — vale marcar isso explicitamente no capítulo, citando `E2-002`, para que o texto não seja lido como se a lacuna fosse real.

---

## L4 — ICKEPS depois de 2017 e retrospectivas das competições de engenharia do conhecimento para planejamento

**Strings e bases (resultados examinados):**
- Página oficial `icaps-conference.org/competitions/` (WebFetch) — lista as cinco edições do ICKEPS (2005, 2007, 2009, 2012, 2016/2017) e não menciona nenhuma edição posterior a 2016.
- WebSearch `ICKEPS 2019 sixth International Competition Knowledge Engineering Planning Scheduling` — 9 resultados; não achou uma "sexta edição"; achou apenas o workshop KEPS de 2019 (sem competição associada) e o artigo "Food for Thoughts (and Call to Action)" (Vallati & Chrpa, já `E6-022` na lista, excluído por redundância na triagem), que é justamente um apelo para reviver a competição.
- WebSearch `"ICKEPS" 2023 OR 2024 OR 2025 sixth competition knowledge engineering planning revival` — 9 resultados; nenhuma evidência de uma sexta edição da competição; o resumo automático da busca chegou a sugerir "ICKEPS 2024 hospedado", mas a checagem direta da página oficial do KEPS 2024 (abaixo) contradisse isso.
- WebFetch da página `icaps24.icaps-conference.org/program/workshops/keps/` — confirma que o workshop KEPS de 2024 apenas cita que "continua a tradição de várias competições ICKEPS e workshops KEPS anteriores", sem anunciar uma nova edição da competição nem relatar resultados.
- Crossref `ICKEPS knowledge engineering competition planning scheduling` — 20 resultados; o mais recente item específico de ICKEPS é o resumo da 5ª edição (2017, já `E6-020`); os demais resultados são sobre planejamento e agendamento em geral, não sobre a competição.

**Nenhum item novo registrado no CSV**: os únicos itens diretamente relevantes (resumo da 5ª edição `E6-020`, e o apelo à ação `E6-022`) já estão em `lista-consolidada.csv`.

**Veredito: parcial.**

[FATO] Não foi localizada, em nenhuma das quatro buscas nem na página oficial de competições da ICAPS, uma sexta edição do ICKEPS (competição) depois da 5ª (2016, resumida em 2017 em `E6-020`); o workshop KEPS continuou a acontecer anualmente na ICAPS, mas sem competição associada, segundo as páginas de 2019, 2024 e 2025 consultadas. [FATO] Existe uma retrospectiva/chamada à ação sobre o formato do ICKEPS pós-2017 (`E6-022`, Vallati & Chrpa, 2020), já presente na lista consolidada, embora excluída da triagem final por redundância com `E6-020`. [HIPÓTESE] A combinação — nenhuma nova competição, mas uma retrospectiva pedindo sua retomada — sugere que a lacuna dos triadores está parcialmente correta: não há o que citar sobre uma "sexta edição", mas o texto pode e deve citar `E6-022` ao descrever o estado do ICKEPS depois de 2017, evitando a afirmação "não há nada" sobre o tema.

---

## L5 — *Instance space analysis* aplicada a planejamento automatizado

**Strings e bases (resultados examinados):**
- WebSearch `"instance space analysis" automated planning classical planning footprint algorithm selection` — 9 resultados; confirma aplicações de ISA a *scheduling* paralelo em lote, *timetabling*, *job shop scheduling*, *car sequencing* e SAT/CSP — nenhuma a planejamento clássico/automatizado (PDDL).
- Crossref `instance space analysis automated planning PDDL` — 15 resultados; nenhum item relevante (todos sobre variantes de PDDL+ ou temas não relacionados a ISA).
- arXiv, busca em texto completo `"instance space analysis" AND planning` — **0 resultados**.
- Itens já na lista consolidada (`E7-025` a `E7-029`, `E2-020`): fundam e aplicam a metodologia ISA a classificação de aprendizado de máquina, *job shop scheduling* e *timetabling* — nenhum a planejamento automatizado.

**Nenhum item novo registrado no CSV**: a busca não encontrou nenhum trabalho, novo ou já catalogado, que aplique ISA a planejamento automatizado.

**Veredito: confirmada** — nas bases consultadas.

[FATO] Em quatro strings e três bases (WebSearch, Crossref, arXiv, incluindo busca em texto completo no arXiv, que devolveu zero resultados), não foi localizado nenhum trabalho que aplique *instance space analysis* a planejamento automatizado ou clássico. [FATO] A metodologia de ISA está bem estabelecida e documentada (tutorial abrangente `E7-027`, já na lista) e já foi aplicada a diversos problemas de otimização combinatória adjacentes — *job shop scheduling*, *timetabling*, *car sequencing*, *batch scheduling* —, mas não a planejamento automatizado nas bases consultadas. [HIPÓTESE] Esta é uma ausência de evidência nas bases e strings usadas, não uma prova de inexistência: a proximidade entre ISA e a própria pergunta central desta dissertação revisada (relação entre características de domínio e desempenho de técnica) sugere que aplicar ISA a planejamento é uma lacuna real e potencialmente uma contribuição original da revisão, não apenas um efeito de busca malfeita — mas a ausência deveria ser verificada de novo antes de qualquer afirmação categórica no texto final.

---

## Resumo dos vereditos

| Lacuna | Veredito | Itens novos no CSV |
|---|---|---|
| L1 — métricas estruturais/UML em modelos de domínio | Parcial | 4 |
| L2 — LLM como seletor de planejador/algoritmo/portfólio | Confirmada | 0 |
| L3 — *probing features* na predição de desempenho | Não confirmada (já na lista, `E2-002`) | 0 |
| L4 — ICKEPS pós-2017 e retrospectivas | Parcial | 0 |
| L5 — *instance space analysis* em planejamento | Confirmada | 0 |
