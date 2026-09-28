---
tipo: sintese-de-eixo
eixo: E8
obras: 20
data: 2026-09-22
---

# E8 — IA no desenvolvimento de software

## 1. Pergunta e resposta curta

O que a evidência empírica mostra sobre agentes e assistentes de código (desempenho em *benchmarks*, estudos com equipes reais), e há trabalho sobre escolher a estratégia ou o agente conforme a tarefa?

[FATO] A evidência é consistente num ponto, dividida em outro. É consistente em mostrar que o desempenho de agentes e assistentes de IA varia fortemente com características observáveis da tarefa — tipo de *bug*, repositório, contexto, riqueza da descrição —, retomando, com dados de 2023–2026, a lógica de ajuste investigada em 2010 [@rondon2025evaluating; @takerngsaksiri2025humanintheloop; @yang2024sweagent; @zhou2026agentasarouter]. É dividida quanto ao efeito líquido em equipes reais: ganho robusto [@peng2023impact; @cui2024effects], efeito nulo [@stray2025developer] e efeito negativo [@becker2025measuring]. Há propostas e provas de conceito de roteamento (Triage, SWE-Router e Agent-as-a-Router) e uma arquitetura composta em produção (HULA); esses níveis de evidência não são equivalentes [@madeyski2026triage; @son2026swerouter; @zhou2026agentasarouter; @takerngsaksiri2025humanintheloop]. Nenhuma obra cita 2010; toda ligação é analogia [HIPÓTESE].

## 2. Benchmarks e agentes

[FATO] SWE-bench é a referência do campo: 2.294 *issues* reais do GitHub em 12 repositórios Python, avaliadas por *patch* contra a suíte de testes real; em 2023, o melhor modelo (Claude 2) resolve só 1,96% com recuperação BM25 [@jimenez2024swebench]. SWE-agent, com interface agente-computador dedicada, eleva o estado da arte a 12,5% em SWE-bench e 87,7% em HumanEvalFix (GPT-4 Turbo/Claude 3 Opus, mar/2024) [@yang2024sweagent]. SWE-Gym acrescenta a peça de treino (2.438 instâncias reais, ganhos de até 19 pontos absolutos) [@pan2024training]; OpenHands padroniza a execução em *sandbox* [@wang2024openhands]; MetaGPT e AutoGen dão a coordenação multiagente, sem medir ajuste tarefa-configuração [@hong2023metagpt; @wu2023autogen].

[FATO] Esses *benchmarks* medem resolução binária por instância ("% Resolved"), análoga à cobertura de 2010 (A7/F5); não medem qualidade, eficiência ou legibilidade — os próprios autores reconhecem: "relying solely on this method is insufficient to guarantee reliable performance of model generations" [@jimenez2024swebench]. Xia et al. mostram uma abordagem sem agente, de três fases fixas, superando agentes complexos em desempenho e custo (32,00% no SWE-bench Lite a US$0,70/instância, referência adotada pela OpenAI) [@xia2025demystifying], corrigindo a suposição de 2010 (A2) de que técnicas mais sofisticadas vencem. Padrão recorrente: queda de desempenho do *benchmark* aberto para o industrial — de 86%/45% (*recall*/similaridade) para 30%/30% na Atlassian [@takerngsaksiri2025humanintheloop]; de 78% para 25,6% de *patch* plausível entre bugs automáticos e humanos no Google [@rondon2025evaluating]. Duas revisões sistemáticas (395 e 124 artigos) mapeiam onde LLMs foram aplicados em SE sem quantificar por que uma tarefa favorece um modelo — isso só aparece nos trabalhos de 2025–2026 [@hou2023large; @liu2026large].

## 3. Estudos com desenvolvedores e equipes reais

[FATO] Quatro desenhos, quatro resultados. Peng et al. (RCT, 95 desenvolvedores Upwork, tarefa única de servidor HTTP, mai–jun/2022, Copilot pré-lançamento geral): redução de 55,8% no tempo (71,17 min vs. 160,89 min; IC 95% [21%, 89%]; p=0,0017) [@peng2023impact]. Cui et al. (três RCTs de campo combinados, 4.867 desenvolvedores, Microsoft/Accenture/Fortune 100): aumento de 26,08% (erro-padrão 10,3%) em tarefas concluídas [@cui2024effects]. Stray et al. (estudo de caso longitudinal observacional, NAV IT/Noruega, 26.317 *commits* de 703 repositórios em dois anos, 25 usuários do Copilot vs. 14 não usuários): sem mudança significativa na atividade de *commit* — "we did not find any statistically significant changes in commit-based activity for Copilot users after they adopted the tool" [@stray2025developer]. Becker et al. (RCT, METR, fev–jun/2025, 16 desenvolvedores experientes de OSS, 246 tarefas reais em repositórios maduros, Cursor Pro com Claude 3.5/3.7 Sonnet): o oposto do esperado — "allowing AI actually increases completion time by 19%" [@becker2025measuring].

[FATO] A contradição não é ruído; os desenhos diferem em cinco eixos. Causalidade: os três primeiros são RCTs; Stray é observacional, com autosseleção reconhecida — "Copilot adopters were already significantly more active developers to begin with... indicating a self-selection effect" (p<0,00555) [@stray2025developer]. Maturidade do repositório: Peng usa tarefa nova isolada; Becker usa repositórios com média de 10 anos e >1,1 milhão de linhas, atribuindo parte da lentidão a essa maturidade [@becker2025measuring]. Experiência: Cui encontra maior ganho para menos experientes; Becker, maior lentidão para os mais experientes/familiarizados — direções opostas, só explicáveis lendo os dois juntos. Métrica: quatro operacionalizações distintas de "produtividade" (tempo, tarefas concluídas, atividade de *commit*), não comparáveis diretamente. Percepção vs. medição: em Stray, produtividade percebida não se correlaciona com atividade objetiva (ρ ≈ 0,17; p=0,40) [@stray2025developer]; em Becker, desenvolvedores preveem 24% de redução no tempo e, depois, ainda se acreditam acelerados, quando foram desacelerados em 19% [@becker2025measuring].

## 4. O efeito varia com a tarefa

[HIPÓTESE] Esta é a seção-eixo da revisão e o paralelo mais direto com a tese de 2010; a evidência aqui é a mais forte do lote, mas permanece analogia — nenhuma obra testa formalmente a ligação com 2010.

[FATO] O dado mais limpo é de Rondon et al.: a mesma técnica (agente Passerine, Gemini 1.5 Pro, sem alteração de configuração) varia de 78% a 25,6% de taxa de *patch* plausível apenas por origem do *bug* — sanitizador automático (SAN) 78%, dependência de ordem de teste (TOD) 68%, humano 25,6% — atribuída pelos autores a buscabilidade da descrição, dispersão espacial da mudança e diversidade de linguagem; o padrão comportamental da trajetória do agente também varia por tipo de *bug* [@rondon2025evaluating]. Takerngsaksiri et al. replicam o padrão em produção na Atlassian: recall cai de 86% para 30% e similaridade de 45% para 30% ao sair do SWE-bench para o conjunto interno JIRA, atribuído à "natureza de como a tarefa é escrita" (SWE-bench traz nomes de módulo e trechos de código; *issues* ágeis são mais curtas) [@takerngsaksiri2025humanintheloop]; desenvolvedores confirmam que o agente é útil sobretudo em "tarefas simples ou diretas" [@takerngsaksiri2025humanintheloop]. Yang et al. mostram lacuna de 75,2 pontos percentuais (12,5% vs. 87,7%) para o mesmo agente entre SWE-bench e HumanEvalFix (função isolada) [@yang2024sweagent], sem decompor a diferença estruturalmente.

[FATO] Zhou et al. formalizam a variação com maior rigor: numa matriz de 8 modelos de fronteira × 9 dimensões de tarefa (~10 mil instâncias, CodeRouter-Bench), nenhum modelo domina todas as dimensões — Opus 4.6 lidera em correção de *bugs* (0,719), GPT-5.4 em geração de teste (0,753), Qwen3-Max em ciência de dados (0,823) — e a dimensão sozinha explica ~27% da entropia da decisão ótima [@zhou2026agentasarouter]. Peng et al., com tarefa fixa, encontram heterogeneidade por perfil do desenvolvedor (menos experiência, mais horas de codificação, 25–44 anos: maior ganho) [@peng2023impact] — eixo de variação do lado de quem executa, que 2010 não previa.

[HIPÓTESE] Um terceiro eixo, ausente em 2010, é temporal/comportamental: SWE-Router mostra que a descrição textual sozinha não separa um "*typo* localizado" de um "*refactor* multi-módulo" — é preciso observar a trajetória parcial do agente, sinal que só existe durante a execução [@son2026swerouter]. Isso qualifica a analogia: em 2010 a característica do domínio é extraída antes de qualquer execução (via UML); aqui parte do sinal só surge em tempo de execução.

## 5. Escolher agente, modelo ou estratégia conforme a tarefa

[FATO] Três estágios de maturidade coexistem no lote. Protocolo propositivo: Madeyski formula o Triage, que usaria saúde/qualidade do código como sinal de roteamento de *tier* de modelo e define condições falseáveis de custo-efetividade, mas não reporta avaliação empírica concluída [@madeyski2026triage]. Prova de conceito: SWE-Router deixa um modelo barato explorar algumas *turns* antes de escalar [@son2026swerouter]; Zhou et al. mostram por ablação que só a descrição da dimensão não melhora o roteador *zero-shot* (41,41% → 41,18%), mas estatística de desempenho prévia por dimensão sim (→ 47,74%), ainda distante do oráculo por tarefa (57,00%) [@zhou2026agentasarouter]. Produção real: HULA já opera na Atlassian, roteando entre agente de planejamento e de codificação com aprovação humana obrigatória, com 82% de aprovação de plano e 59% de PR integrado em 663 *issues* [@takerngsaksiri2025humanintheloop].

[HIPÓTESE] Nenhum desses sistemas cita 2010. Em comum: a característica preditiva não é estrutural/estática como a UML de 2010, e sim uma de três famílias — qualidade de código estática [@madeyski2026triage], estatística agregada de desempenho passado [@zhou2026agentasarouter], ou sinal comportamental em execução [@son2026swerouter].

## 6. Relação com a dissertação de 2010 e com a Q4

| Rótulo/pergunta | O que a literatura permite | Marcação | Chaves |
|---|---|---|---|
| A1/A3 (varia por característica) | Confirmado por analogia repetida: mesma técnica, 25,6%–78% por tipo de tarefa; matriz modelo×dimensão sem dominância única | [HIPÓTESE] | [@rondon2025evaluating; @takerngsaksiri2025humanintheloop; @zhou2026agentasarouter; @yang2024sweagent; @jimenez2024swebench; @madeyski2026triage; @son2026swerouter] |
| A2 (técnicas sofisticadas vencem) | Corrigido: abordagem sem agente, de três fases fixas, supera agentes complexos em desempenho e custo | [HIPÓTESE] | [@xia2025demystifying] |
| A4 (mais características melhoram o ranking) | Ecoado com formalização: dimensão explica ~27% da entropia da decisão ótima; o resto exige informação adicional por tarefa | [HIPÓTESE] | [@zhou2026agentasarouter] |
| A6 (taxonomia de técnicas) | Obsoleta: taxonomia de planejamento não se aplica; cada obra propõe taxonomia própria | [HIPÓTESE] | [@xia2025demystifying; @liu2026large] |
| A7/F5 (cobertura como métrica única) | Limitação viva: "% Resolved" é binário por instância; qualidade, segurança e eficiência ficam de fora, com risco de mascarar efeito negativo | [FATO/HIPÓTESE] | [@jimenez2024swebench; @perry2023do; @stray2025developer] |
| Q4 (ajuste tarefa-estratégia) | Roteamento operacional em três estágios (analítico, prova de conceito, produção); nenhum se declara herdeiro de 2010 | [HIPÓTESE] | [@madeyski2026triage; @son2026swerouter; @zhou2026agentasarouter; @takerngsaksiri2025humanintheloop] |
| Piloto Fase 5 (efeito em equipe real) | Contradição direta entre ganho, nulo e perda, associada a desenho, maturidade do repositório e experiência do desenvolvedor, não resolvida | [FATO] | [@peng2023impact; @cui2024effects; @stray2025developer; @becker2025measuring] |

## 7. Divergências e pontos em disputa

[FATO] O ponto de maior disputa é o sinal do efeito em equipes reais: ganho de 55,8% [@peng2023impact], ganho de 26,08% [@cui2024effects], efeito nulo [@stray2025developer] e perda de 19% [@becker2025measuring]. Não é disputa sobre o número certo, é disputa sobre condições — Becker et al. ressalvam: "our results are consistent with small greenfield projects or development in unfamiliar codebases seeing substantial speedup from AI assistance" [@becker2025measuring], compatível com o resultado de Peng et al. (tarefa nova, isolada) [@peng2023impact].

[FATO] Há desacordo sobre se sofisticação de agente ajuda: Xia et al. mostram abordagem simples superando agentes complexos no SWE-bench Lite [@xia2025demystifying], enquanto Yang et al. mostram que uma interface agente-computador dedicada eleva o estado da arte [@yang2024sweagent] — talvez conciliável (sofisticação de interface ≠ sofisticação de decisão), mas o lote não resolve a distinção.

[FATO] Um terceiro ponto é onde reside a heterogeneidade: no lado da tarefa (Rondon, Takerngsaksiri, Zhou, Yang) ou do desenvolvedor (Peng, Cui, Becker) [@rondon2025evaluating; @takerngsaksiri2025humanintheloop; @zhou2026agentasarouter; @yang2024sweagent; @peng2023impact; @cui2024effects; @becker2025measuring]. Nenhuma obra testa os dois eixos no mesmo desenho.

## 8. Lacunas

[FATO] Nenhuma obra formaliza métrica estrutural de tarefa comparável à UML de 2010; as candidatas ficam em nível descritivo (tipo de *bug*, riqueza da descrição, contexto) [@rondon2025evaluating; @takerngsaksiri2025humanintheloop], só operacionalizadas estatisticamente nos trabalhos de roteamento de 2025–2026 [@madeyski2026triage; @zhou2026agentasarouter].

[FATO] Não há estudo combinando, no mesmo desenho, tarefas reais de desenvolvedores (Peng, Cui, Becker, Stray) com a decomposição estrutural de tarefa dos estudos de *benchmark* (Rondon, Zhou) — as duas evidências vêm de literaturas separadas, lacuna para investigação futura derivada da Fase 5.

[FATO] Segurança (Perry et al.) e qualidade da solução (SWE-bench) apontam risco pouco explorado: nenhum roteador (Triage, SWE-Router, Agent-as-a-Router) usa segurança ou qualidade como critério — todos otimizam taxa de resolução ou custo [@perry2023do; @jimenez2024swebench; @madeyski2026triage; @son2026swerouter; @zhou2026agentasarouter].

## 9. Insumos para as próximas fases

[HIPÓTESE] Para o piloto da Fase 5, duas referências de método com armadilhas documentadas. De Becker/Stray: preferir RCT com designação aleatória por tarefa (não por desenvolvedor), pois sem randomização quem adota a ferramenta já era mais ativo antes, inflando o efeito [@becker2025measuring; @stray2025developer]. De Peng/Cui/Becker: registrar experiência do desenvolvedor e familiaridade com o repositório como covariáveis desde o desenho — os estudos encontram heterogeneidade nesse eixo em direções opostas (menos experiência ganha mais em Cui; mais familiaridade perde mais em Becker), só resolvível medindo ambos juntos [@peng2023impact; @cui2024effects; @becker2025measuring].

[HIPÓTESE] Características de tarefa a medir, por analogia com Rondon/Takerngsaksiri: origem do problema (humano vs. automático), riqueza da descrição, tamanho/maturidade do repositório ou módulo, dispersão espacial da mudança [@rondon2025evaluating; @takerngsaksiri2025humanintheloop]. Métricas, nunca uma só: (i) sucesso objetivo por execução (testes, tempo, como em Peng et al.) e (ii) percepção subjetiva, reportadas separadamente e correlacionadas — Stray et al. mostram que podem divergir por completo (ρ ≈ 0,17, não significativo) [@peng2023impact; @stray2025developer]. Perry et al. sugerem acrescentar qualidade/segurança do artefato, não só conclusão da tarefa [@perry2023do].

[HIPÓTESE] Três armadilhas a evitar: efeito nulo mascarado por granularidade agregada — métricas de repositório/organização escondem a heterogeneidade por tarefa, visível só com tarefas individuais rotuladas [@stray2025developer]; autosseleção — quem escolhe a ferramenta difere sistematicamente de quem não escolhe [@stray2025developer]; percepção divergente da medição — nem o desenvolvedor (Becker) nem a equipe (Stray) percebem corretamente o efeito real, logo um estudo futuro não pode se apoiar só em autorrelato [@becker2025measuring; @stray2025developer]. Zhou et al. sugerem testar ainda se fornecer informação de desempenho passado por tipo de tarefa, sem trocar de agente, já muda o resultado [@zhou2026agentasarouter].

## 10. Obras usadas

- [@becker2025measuring] — RCT com 16 desenvolvedores experientes de OSS; IA aumentou tempo de conclusão em 19%.
- [@cui2024effects] — três RCTs de campo, 4.867 desenvolvedores; ganho de 26,08% em tarefas concluídas.
- [@hong2023metagpt] — framework multiagente com SOPs para engenharia de software colaborativa.
- [@hou2023large] — revisão sistemática de 395 artigos sobre LLMs em engenharia de software (2017–2024).
- [@jimenez2024swebench] — SWE-bench, benchmark seminal de 2.294 issues reais do GitHub.
- [@liang2024largescale] — survey de usabilidade com 410 desenvolvedores sobre assistentes de código.
- [@liu2026large] — revisão sistemática de 124 artigos sobre agentes de LLM em engenharia de software.
- [@madeyski2026triage] — Triage: roteamento de tier de LLM por métricas de saúde do código.
- [@pan2024training] — SWE-Gym, ambiente de treino para agentes de engenharia de software.
- [@peng2023impact] — RCT fundacional do GitHub Copilot; ganho de 55,8% em tempo de tarefa.
- [@perry2023do] — estudo de usuário: assistentes de IA levam a código menos seguro.
- [@rondon2025evaluating] — reparo de programas por agente no Google; desempenho de 78% a 25,6% por tipo de bug.
- [@son2026swerouter] — SWE-Router: roteamento condicionado à trajetória parcial do agente.
- [@stray2025developer] — estudo de caso longitudinal na NAV IT; efeito nulo em atividade de commit.
- [@takerngsaksiri2025humanintheloop] — HULA, agente implantado em produção na Atlassian.
- [@wang2024openhands] — OpenHands, plataforma aberta para agentes de desenvolvimento de software.
- [@wu2023autogen] — AutoGen, framework de conversação multiagente.
- [@xia2025demystifying] — Agentless: abordagem sem agente supera agentes complexos no SWE-bench Lite.
- [@yang2024sweagent] — SWE-agent, interface agente-computador; estado da arte em 2024.
- [@zhou2026agentasarouter] — Agent-as-a-Router, roteamento agêntico com matriz modelo×dimensão de tarefa.
