---
tipo: sintese-de-eixo
eixo: E6
obras: 23
data: 2026-09-22
---

# E6 — Engenharia do conhecimento para planejamento

## 1. Pergunta e resposta curta

Como evoluíram as ferramentas e métodos de modelagem de domínios (itSIMPLE, ICKEPS, Unified Planning) e o uso de LLMs para gerar modelos PDDL? Há trabalho sobre métricas de qualidade de modelos de domínio?

[FATO] A linha itSIMPLE nasce em 2005 já com o objetivo de extrair características do domínio para escolher técnica ou heurística [@vaquero2005itsimple] — o mesmo objetivo de HADDAD (2010) cinco anos depois, mas por métricas de diagramas UML, não pela análise em redes de Petri originalmente projetada. A ferramenta evolui em dissertação [@vaquero2007itsimpleb] e artigo de periódico [@vaquero2013itsimple], e segue referenciada como ferramenta corrente ainda em 2024–2025 [@micheli2025unified]. Um corpo robusto de evidência (McCluskey e Vallati e coautores) mostra que a *configuração* sintática de um modelo — sem alterar seu significado — afeta de forma substancial o desempenho, a ponto de mudar o *ranking* entre planejadores [@vallati2015effective; @vallati2021importance; @vallati2019robustness]: decisivo para F3. A qualidade de modelo ganhou, em 2017, formalização em cinco dimensões qualitativas [@mccluskey2017engineering], nenhuma equivalente às métricas quantitativas de 2010. LLMs geram e corrigem PDDL desde ~2024, quase sempre com planejador ou validador simbólico no laço [@gestrin2024nl2plan; @smirnov2024generating; @jiang2026toward; @huang2025spar], e a literatura de 2025 reafirma que expertise humana e validação simbólica continuam indispensáveis [@vallati2025knowledge].

## 2. Ferramentas e métodos

[FATO] A linha itSIMPLE tem três marcos lidos neste eixo. O artigo de 2005 traz a versão preliminar: UML com estrutura fixa de classes `Planner`, `Environment`, `Agent`, tradução para XML e depois PDDL, e análise por redes de Petri ainda não implementada [@vaquero2005itsimple]. A dissertação de Vaquero (2007), na mesma Escola Politécnica da USP de 2010, implementa o ambiente integrado UML → XML → Redes de Petri → PDDL, com a qualidade melhorando por "sucessivos refinamentos" do projetista [@vaquero2007itsimpleb]. O artigo de 2013 é a versão madura, com diagramas de *timing*/objeto, OCL, redes de Petri automáticas, PDDL até 3.1, e três estudos de caso reais (petróleo, *software*, montagem automotiva) fora do universo de IPC [@vaquero2013itsimple]; cita, sem demonstrar, um ganho de "até três ordens de magnitude" atribuído a outra publicação dos mesmos autores — número relatado, não verificado aqui.

[FATO] Em paralelo, a linha de Huddersfield (McCluskey e colaboradores) ataca o mesmo problema por modelagem orientada a objetos, não UML. McCluskey & Porteous (1997) é fundacional: em quatro famílias de domínios, modelos "compilados" (macro-operadores e ordens de metas automáticas) resolvem muito mais problemas, com muito menos CPU, que modelos não compilados do mesmo domínio [@mccluskey1997engineering]. GIPO (Simpson, Kitchin & McCluskey, 2007) é concorrente direto do itSIMPLE [@simpson2007planning]. Um tradutor PDDL→OCLh (Simpson, McCluskey, Liu & Kitchin, 2000) aplicado ao Tyre World mostra que a tradução já introduz ambiguidades (atribuição de predicado a um *sort*, *substates* incompletos) decorrentes do algoritmo tradutor, não do domínio [@simpson2000knowledge].

[FATO] Jilani et al. (2014) revisam nove ferramentas de indução automática de modelo a partir de traços de plano [@jilani2014automated]; o KEEN (Orlandini et al., 2014) integra *model checking* (UPPAAL-TIGA) à engenharia do conhecimento para planejamento baseado em *timelines* [@orlandini2014planning]. A ICKEPS, competição desde 2005 dedicada à engenharia do conhecimento, teve sua quinta edição (2016) resumida por Chrpa, McCluskey, Vallati e Vaquero — este último, autor fundacional do itSIMPLE [@chrpa2017fifth].

[FATO] A infraestrutura mais recente é a biblioteca Unified Planning (UP, projeto AIPlan4EU): API Python com *flags* (`ProblemKind`) que selecionam automaticamente motores compatíveis [@micheli2025unified]. Cita o itSIMPLE, em trabalhos relacionados, com "*análises baseadas em redes de Petri*" — confirmação independente e recente de sua relevância; o sistema de *flags* opera sobre construtos de linguagem, não sobre métricas estruturais do domínio como em 2010.

## 3. A configuração do modelo afeta o desempenho

[FATO] Esta é a evidência mais decisiva do eixo para F3. Vallati, Hutter, Chrpa & McCluskey (2015) formalizam "configuração do modelo" como a ordem de predicados, operadores e pré-condições/efeitos em PDDL, com conteúdo semântico idêntico. Com SMAC sobre 6 planejadores e 7 domínios (~3.800 problemas), mostram impacto estatisticamente significativo (Wilcoxon) e, em vários domínios, **mudança de qual planejador é o melhor**; uma configuração adversarial degrada o IPC score em 21,1 pontos frente ao original [@vallati2015effective]. Vallati, Chrpa, McCluskey & Hutter (2021) estendem o resultado (50 configurações aleatórias, 12 planejadores, 13 domínios da IPC 2014): o IPC score do planejador Probe varia entre 63 e 37 só por reordenação, e Probe cai do 2º ao 11º lugar dependendo da configuração — "*competitions ranks are not stable*". Configuração automática gera acelerações de até 25×; reposicionar um único macro-operador gera até 3 ordens de magnitude de melhoria no PAR10. Planejadores Fast-Downward-based, que reordenam operadores no pré-processamento, são menos sensíveis [@vallati2021importance].

[FATO] Vallati & Chrpa (2019), na perspectiva de um atacante hipotético, mostram que modificações sutis e válidas de um modelo — não detectáveis por validação padrão — degradam o desempenho de planejadores com estratégias distintas [@vallati2019robustness], achado que McCluskey, Vaquero & Vallati (2017) citam como terceira fonte independente do mesmo efeito de ordem [@mccluskey2017engineering]. Georgievski, Tekin & Aiello (preprint, 2026) reformulam a pergunta para energia: aridade de ação redundante aumenta consumo por fatores de 2 a 12 (podendo causar falhas), e *dead ends* vão de efeitos desprezíveis a catastróficos conforme a estrutura do domínio, não do planejador; energia e tempo nem sempre se correlacionam [@georgievski2026energy].

[HIPÓTESE] O tamanho de efeito — mudança de *ranking* completo, 25× de aceleração, 3 ordens de magnitude por macro — é grande o suficiente para que a variação de cobertura atribuída em 2010 a "características do domínio" esteja, em parte, confundida com decisões não controladas de tradução/serialização UML→PDDL. 2010 não relata ter controlado a ordem dos elementos gerados pelo itSIMPLE: lacuna metodológica identificável, não refutação de A1/A5.

## 4. Qualidade e métricas de modelos de domínio

[FATO] McCluskey, Vaquero & Vallati (2017) formalizam cinco propriedades de qualidade — *consistência*, *acurácia*, *completude*, *adequação*, *operacionalidade* — nenhuma quantitativa e contável como em 2010; são propriedades a verificar, não a medir. Citam o itSIMPLE, notando que "*a qualidade depende tanto da codificação inicial quanto da correção da tradução*" [@mccluskey2017engineering].

[FATO] Alnazer & Georgievski (2023) propõem taxonomia concorrente: sete categorias de "aspectos realistas" (*Objectives, Tasks, Quantities, Determinism, Agents, Constraints, Qualities*), por revisão de 20 estudos, sem se apoiar em UML. Reafirmam que "*a qualidade dos modelos depende principalmente das habilidades dos engenheiros de conhecimento*" — terceira fonte independente de F3 — e apontam como trabalho futuro ainda inexistente "*sintetizar métricas que avaliem quantitativamente o realismo dos domínios*" [@alnazer2023understanding].

[FATO] Huang et al. (2025, SPAR) é o candidato mais próximo de uma métrica quantitativa estrutural comparável: complexidade composta de PDDL com nove componentes (ações, tipos, predicados, funções, pré-condições/efeitos médios, *interdependency score*, acoplamento de ação etc.), calibrada em 30 domínios (Blocksworld = 5,23, 17º) [@huang2025spar]. Aplica-se a PDDL, não a UML; a leitura não verificou poder preditivo testado sobre desempenho, só caracterização de domínios gerados por LLM.

[HIPÓTESE] Nenhuma das 23 obras aplica métricas de diagramas UML no estilo Genero & Piattini (as de 2010) a modelos de planejamento — aprofundado na seção 8 (busca L1).

## 5. LLMs gerando e corrigindo PDDL

[FATO] O NL2Plan (Gestrin, Kuhlmann & Seipp, 2024) é o primeiro sistema totalmente automático de linguagem natural mínima para PDDL completo, com raciocínio guiado por planejador; em sete domínios (cinco inéditos), supera a *baseline* LLM+validador em todos exceto Blocksworld (memorização), com 260% mais tarefas perfeitas quando usado isoladamente; descrito como "*ferramenta assistiva*", não substituição do modelador [@gestrin2024nl2plan].

[FATO] Smirnov et al. (2024) integram checagem de consistência e alcançabilidade ao laço de geração por LLM, filtrando predicados/tipos mal usados; em cinco domínios, reduz erros, mas ainda menciona checagem humana final [@smirnov2024generating]. Jiang et al. (2026) propõem o NL-PDDL-Bench e um *framework* "planejador-no-laço" que corrige especificações não executáveis por edições localizadas [@jiang2026toward]. Huang et al. (2025, SPAR) usa LLMs para gerar domínios PDDL para UAVs, avaliados pela métrica de nove componentes já descrita [@huang2025spar]. Vallati, Barták, Chrpa, McCluskey & Petrick (2025) sintetizam a posição mais recente: "*LLMs podem auxiliar na aquisição de conhecimento, mas expertise humana e validadores simbólicos externos continuam indispensáveis*" [@vallati2025knowledge].

[HIPÓTESE] O padrão recorrente em 2024–2026 é sempre o mesmo: LLM gera, mecanismo simbólico corrige. Isso desloca, mas não elimina, a dependência de F3 — de modelador humano para LLM+validador+revisão humana final.

## 6. Relação com a dissertação de 2010

| Rótulo | Relação | O que a literatura mostra | Chaves |
|---|---|---|---|
| A1 | amplia | O objetivo de ligar características de domínio à escolha de técnica já era declarado no itSIMPLE em 2005; a métrica de complexidade PDDL de 2025 é exemplo concreto de característica estrutural comparável | [@vaquero2005itsimple; @huang2025spar] |
| A5 | corrige (qualifica) | A "complexidade" via métricas estruturais pode estar confundida com a ordem/serialização sintática do modelo — artefato de engenharia, não do domínio —, com efeito grande (25×, 3 ordens de magnitude, mudança de *ranking*) | [@vallati2015effective; @vallati2021importance; @vallati2019robustness; @mccluskey1997engineering; @georgievski2026energy] |
| A8 | corrige | 2010 cita só Hoffmann (2001) e Gerevini, Saetti & Serina (2004); o artigo fundacional do itSIMPLE (2005), com o mesmo objetivo, não aparece | [@vaquero2005itsimple] |
| F1 | confirma | A ICKEPS (desde 2005) e a linha GIPO/Huddersfield, contemporâneas ou anteriores a 2010, não aparecem na revisão original | [@chrpa2017fifth; @simpson2007planning; @mccluskey1997engineering] |
| F3 | confirma (central) | Fontes independentes mostram dependência do engenheiro e da configuração sintática; as classes fixas do itSIMPLE também contaminam contagens estruturais | [@mccluskey1997engineering; @mccluskey2017engineering; @vallati2015effective; @vallati2021importance; @vallati2019robustness; @alnazer2023understanding; @vaquero2005itsimple; @simpson2000knowledge] |
| T1 | amplia | A extração/geração automática de modelos, trabalho futuro de 2010, foi perseguida por indução de traços de plano (já em 2014) e por LLM (2024–2026) — nenhuma estende o itSIMPLE | [@jilani2014automated; @gestrin2024nl2plan; @smirnov2024generating; @jiang2026toward] |

## 7. Divergências e pontos em disputa

[FATO] Não há divergência quanto ao achado central de que a configuração sintática afeta o desempenho — Vallati et al. (2015, 2021), Vallati & Chrpa (2019), McCluskey et al. (2017) e Georgievski et al. (2026) convergem, variando só o alvo (tempo, energia, *ranking*) e o enquadramento (engenharia a corrigir, vulnerabilidade, sustentabilidade).

[FATO] Há divergência metodológica não resolvida, mas não contraditória, entre a linha UML/itSIMPLE e a linha orientada a objetos/OCLh/GIPO (McCluskey, Simpson, Kitchin): ambas partem do mesmo diagnóstico — PDDL não é boa linguagem de modelagem —, mas nenhuma obra lida compara as duas quanto a desempenho ou qualidade do modelo resultante. Já sobre LLMs gerando PDDL não há discordância explícita: as quatro obras de 2024–2026 assumem que devem ser usados, com correção simbólica, sugerindo consenso e não disputa.

## 8. Lacunas

[FATO] A busca L1 (métricas estruturais, `literatura/protocolo/busca/lacunas-memo.md`) teve veredito **parcial**: achou quatro trabalhos novos ligando características estruturais (ordenação, acoplamento, complexidade composta de PDDL, energia) ao desempenho, mas **nenhum** aplica métricas de diagramas UML no estilo Genero & Piattini a modelos de planejamento. É "não encontramos", não "não existe": a comunidade parece ter preferido métricas ad hoc de PDDL à ponte UML que 2010 tentou construir.

[FATO] A busca L4 (ICKEPS pós-2017) teve veredito **parcial**: não foi localizada sexta edição da competição após 2016 [@chrpa2017fifth]; o *workshop* KEPS continuou ocorrendo (2019, 2024, 2025) sem competição associada, e há uma retrospectiva/apelo à retomada (Vallati & Chrpa, 2020) fora das notas deste eixo. Não há sexta edição a citar, mas há literatura sobre o estado do formato — não afirmar "nada existe".

[HIPÓTESE] Dois textos centrais permaneceram inacessíveis (lacuna de acesso, não de existência): Tonidandel, Vaquero & Silva (2006), sobre a tradução PDDL→UML do itSIMPLE, e Sette et al. (2008), estudo de caso de Vaquero e coautores na indústria de petróleo — ambos fechados, sem cópia aberta localizada. Recomenda-se nova tentativa institucional.

[FATO] Nenhuma obra lida aplica *instance space analysis* a planejamento (busca L5, confirmada) nem LLM como seletor de planejador/portfólio (busca L2, confirmada) — fora do escopo direto de E6, registrado por completude.

## 9. Insumos para as próximas fases

Para a **Fase 2** (auditoria de 2010): a tabela da seção 6 é o checklist. Registrar que A8 omitiu o artigo fundacional do itSIMPLE [@vaquero2005itsimple], com o mesmo objetivo cinco anos antes — caso claro de F1 — e que a ordem dos elementos do itSIMPLE não foi controlada, à luz de [@vallati2015effective; @vallati2021importance] (limitação a reconhecer, não a corrigir retroativamente).

Para a **Fase 3** (extração automática de métricas), quatro decisões ancoradas neste eixo: (1) controlar a configuração/ordem do modelo antes de extrair métricas estruturais — convenção canônica ou variância sob múltiplas configurações [@vallati2015effective; @vallati2021importance]; (2) decidir se a extração mede UML, PDDL exportado ou ambos, documentando o mapeamento, já que nem toda construção UML tem contrapartida em PDDL (agregação, composição, multiplicidade, maior parte dos diagramas de estado) [@vaquero2005itsimple]; (3) excluir ou marcar as classes obrigatórias do itSIMPLE (`Planner`, `Environment`, `Agent`), que não deveriam contar como complexidade do domínio [@vaquero2005itsimple]; (4) complementar as métricas UML com uma métrica de complexidade de PDDL comparável, como a de nove componentes de [@huang2025spar] (Blocksworld = 5,23), testando se PDDL tem poder preditivo maior, menor ou comparável ao das UML — resposta direta a Q2.

Para a **Fase 4** (LLMs): o padrão "LLM gera, mecanismo simbólico corrige" [@gestrin2024nl2plan; @smirnov2024generating; @jiang2026toward; @huang2025spar; @vallati2025knowledge] sugere que qualquer LLM gerador de modelo de domínio deve incluir validação simbólica desde o desenho, nunca tratar a saída do LLM como modelo final.

## 10. Obras usadas

- [@alnazer2023understanding]
- [@chrpa2017fifth]
- [@georgievski2026energy]
- [@gestrin2024nl2plan]
- [@huang2025spar]
- [@jiang2026toward]
- [@jilani2014automated]
- [@mccluskey1997engineering]
- [@mccluskey2017engineering]
- [@micheli2025unified]
- [@orlandini2014planning]
- `sette2008are` — **não lida** (sem acesso ao texto nem ao resumo); não citada no corpo desta síntese e não citável até leitura
- [@simpson2000knowledge]
- [@simpson2007planning]
- [@smirnov2024generating]
- `tonidandel2006reading` — **não lida** (sem acesso ao texto nem ao resumo); não citada no corpo desta síntese e não citável até leitura
- [@vallati2015effective]
- [@vallati2019robustness]
- [@vallati2021importance]
- [@vallati2025knowledge]
- [@vaquero2005itsimple]
- [@vaquero2007itsimpleb]
- [@vaquero2013itsimple]
