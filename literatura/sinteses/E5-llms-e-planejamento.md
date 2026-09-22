---
tipo: sintese-de-eixo
eixo: E5
obras: 20
data: 2026-09-22
---

# E5 — LLMs e planejamento

## 1. Pergunta e resposta curta

Que papéis os LLMs assumem em planejamento automatizado, e o que a evidência empírica mostra sobre cada um?

[FATO] As 20 obras do eixo documentam cinco papéis: planejador direto, tradutor/formalizador para PDDL, gerador de heurística/"modelo de mundo", verificador/autocrítico e gerador de programa/planejador generalizado — nenhum caso de seletor de planejador (lacuna confirmada, seção 7). [FATO] Como planejador direto, o LLM falha de forma consistente e piora com o horizonte da tarefa: de 1% (GPT-3, 2023) a no máximo 62,6% (LLaMA-3.1 405B, 2024) em Blocksworld; só com o LRM o1-preview (setembro de 2024) o número salta a 97,8% [@valmeekam2023planning; @valmeekam2024llms]. [FATO] Como tradutor para PDDL acoplado a um planejador clássico externo, o desempenho sobe muito (85–100% em vários domínios) mas cai a zero em domínios com relações espaciais complexas [@liu2023llmp]. [HIPÓTESE] O padrão que atravessa quase todas as obras: o ganho de confiabilidade vem de acoplar o LLM a um componente verificável externamente, não de raciocinar ou se autocorrigir sozinho — o que responde à Q3 apontando para "LLM auxiliar de planejador clássico", não "LLM como planejador".

## 2. Os papéis do LLM

### Planejador direto

[FATO] Isolado, o LLM planejador autônomo tem desempenho baixo e instável. Em 2023, GPT-3 (`davinci`) acerta 1% de Blocksworld, Instruct-GPT3 6,8%, BLOOM 1,6%, contra baseline humano de 78% de planos válidos [@valmeekam2023planning]. Com GPT-4 (março–junho de 2023), o PlanBench mede 34,3% [@valmeekam2023planbench]. Em 2024, comparando seis modelos (GPT-4, GPT-4-Turbo, GPT-4o, Claude-3-Opus, Gemini Pro, LLaMA-3 70B), nenhum ultrapassa 48,2% e a troca de geração "não tem muito impacto" [@kambhampati2024llms]. Só com o LRM o1-preview (setembro de 2024) o número salta para 97,8% [@valmeekam2024llms]. Com múltiplas restrições simultâneas o desempenho colapsa: 0,6% em planejamento de viagens [@xie2024travelplanner]. Um survey recente resume: "promessa em horizonte curto, degradação forte em horizonte longo, custo de plano arbitrariamente alto mesmo em sucesso" [@aghzal2025survey].

### Tradutor / formalizador para PDDL

[FATO] Quando o LLM só traduz linguagem natural para PDDL, deixando a busca a um planejador clássico externo, o desempenho sobe substancialmente. LLM+P, com GPT-4 (setembro de 2023) gerando o problema PDDL e acionando Fast Downward, chega a 85–100% em Barman, Storage e Grippers, mas 0% em Floortile e 20% em Termes, por falha de especificação de relações espaciais na tradução, não do planejador [@liu2023llmp]. Xie et al. (2023) confirmam qualitativamente que GPT-3.5 é "muito mais adequado à tradução que ao planejamento", falhando em raciocínio numérico e espacial [@xie2023translating]. Guan et al. (2023) vão adiante: GPT-4 constrói o próprio modelo de domínio PDDL (mais de 40 ações), corrigido com validadores e humano, resolvendo 48 tarefas com a garantia de corretude do planejador externo [@guan2023leveraging]. Um levantamento de ~80 trabalhos (2025) confirma que a literatura converge para o LLM "formalizador" [@tantakoun2025llms]; Pallagani et al. mapeiam o mesmo espaço, incluindo ajuste fino versus *prompting* [@pallagani2023understanding; @pallagani2024prospects].

### Heurística / modelo de mundo

[FATO] Em RAP, o mesmo LLM (LLaMA-33B, 2023) é modelo de mundo (prevê o próximo estado) e agente que propõe ações e estima recompensa, dentro de MCTS; em Blocksworld, RAP(20) atinge 64% de sucesso médio e supera CoT-GPT-4 (33% de ganho relativo) — evidência de que a estrutura de busca pesa mais que o tamanho do modelo [@hao2023reasoning]. SayCanPay integra geração de ações por LLM com busca heurística clássica guiada por estimativas de viabilidade e custo [@hazra2024saycanpay]. Valmeekam et al. (2023) já testavam o LLM como sugestão inicial para o planejador local LPG, com "melhoria modesta" [@valmeekam2023planning]. ReAct, base de vários desses trabalhos, intercala raciocínio e ação sem ser, em si, um planejador [@yao2023react]; DeepSeek-R1 ilustra, fora de planejamento, a linhagem de raciocínio via aprendizado por reforço que alimenta modelos como o1 [@guo2025deepseekr1].

### Verificador / autocrítico

[FATO] O LLM autoverificador é frágil e pode piorar o resultado: no Jogo do 24 a autocrítica LLM+LLM derruba a acurácia de 5% para 3%, em Coloração de Grafos de 16% para 2%; em Blocksworld melhora (40% para 55%), mas em Mystery Blocksworld piora (4% para 0%) [@stechly2025self]. Com verificador externo sólido (VAL, SymPy), o desempenho sobe em todos os domínios — até 87% em Blocksworld [@stechly2025self]. Kambhampati et al. (2024) confirmam em escala maior: com *back-prompting* de verificador sólido, GPT-4 sobe de ~34% para 82% em Blocksworld e 70% em Logistics, com teto em domínios ofuscados (~10%) [@kambhampati2024llms]. Kambhampati (2024) sintetiza: "não há base" para supor que LLMs corrigem os próprios erros sem apoio externo [@kambhampati2024can].

### Gerador de programa / planejador generalizado

[FATO] Silver et al. (2024) testam um papel adicional: o LLM (GPT-4) gera um *programa* Python que resolve qualquer instância de um domínio, com depuração automatizada contra tarefas de treino. O desempenho vai de 1,00 (Forest) a 0,01 (Miconic) no mesmo protocolo — um dos contrastes de domínio mais extremos do lote — e cai de forma acentuada sem depuração automática ou nomes informativos no PDDL [@silver2024generalized]. Huang et al. (2024) documentam uma taxonomia paralela de cinco categorias (decomposição de tarefas, seleção de plano, módulo externo, reflexão, memória) para métodos de agentes LLM em geral [@huang2024understanding].

## 3. Variação por domínio

[FATO] A variação de desempenho entre domínios — e entre versões do mesmo domínio — é o achado mais replicado do eixo. LLM+P varia de 0% (Floortile) a 100% (Barman) com o mesmo método e modelo [@liu2023llmp]; Silver et al. (2024) relatam de 0,01 (Miconic) a 1,00 (Forest) [@silver2024generalized]; Hao et al. (2023) mostram queda de 100%/88% (2–4 passos) para 42% (6 passos) dentro de um único domínio [@hao2023reasoning].

[FATO] O caso mais estudado é o par Blocksworld / Mystery Blocksworld — versão logicamente idêntica, com nomes de predicados e ações trocados por rótulos enganosos ou aleatórios. Valmeekam et al. (2023) já registram queda de ~1–7% para menos de 1,1% [@valmeekam2023planning]; PlanBench confirma com GPT-4: 34,3% para 4,3% [@valmeekam2023planbench]; Kambhampati et al. (2024) replicam com seis modelos, todos caindo para 0,8–4,3%, teto de ~10% mesmo com verificador externo [@kambhampati2024llms]; Stechly et al. (2024) replicam de novo [@stechly2025self]. Mesmo o1-preview, com 97,8% em Blocksworld comum, cai para 52,8% na versão ofuscada e 37,3% na aleatorizada — "o desempenho em uma versão do domínio não prediz claramente o desempenho na outra" [@valmeekam2024llms].

[HIPÓTESE] Esse padrão conversa diretamente com A3 e A5 de 2010. A5 (UML mede complexidade do domínio, e essa complexidade afeta o desempenho da técnica) é confirmada no espírito — a característica do domínio segue afetando o desempenho —, mas com mecanismo que a métrica de 2010 não capta: não é a complexidade estrutural que mais pesa aqui, e sim a familiaridade lexical/semântica do domínio face ao treinamento do modelo, mais o comprimento do plano [@kambhampati2024llms; @valmeekam2024llms]. A3 (o ranking só com características do domínio escolhe o melhor planejador independentemente do problema) fica mais frágil com LLM: Blocksworld comum e Mystery Blocksworld têm exatamente as mesmas características estruturais UML, e mesmo assim o desempenho varia em ordens de grandeza — variação que nenhuma métrica estrutural de 2010 prevê, por não ser estrutural.

## 4. Volatilidade dos resultados

[FATO] Os números deste eixo têm data de validade curta. Salto mais nítido: GPT-4 (2023) resolve 34,3% de Blocksworld comum [@valmeekam2023planbench]; o1-preview (setembro de 2024, "disponível havia uma semana" no estudo) resolve 97,8% [@valmeekam2024llms] — ganho de quase 3x em pouco mais de um ano, atribuído a mudança de arquitetura (LRM com cadeia de raciocínio interna), não a mais dados ou parâmetros.

[HIPÓTESE] Envelhece rápido: qualquer taxa de sucesso absoluta por modelo e domínio (a tabela de seis modelos de Kambhampati et al. 2024 já está defasada frente a o1-preview, testado meses depois pelo mesmo grupo [@kambhampati2024llms; @valmeekam2024llms]); e qualquer alegação de que "o problema está resolvido" ou "nunca será" com base numa geração específica.

[HIPÓTESE] Tende a permanecer, por se replicar através de gerações distintas (GPT-3, GPT-4, Claude-3-Opus, Gemini Pro, LLaMA-3, o1-preview) e arquiteturas distintas (autorregressiva vs. LRM): (i) a variação forte por domínio e por versão do domínio [@valmeekam2023planning; @valmeekam2023planbench; @kambhampati2024llms; @stechly2025self; @valmeekam2024llms]; (ii) a fragilidade da autoverificação sem apoio externo [@stechly2025self; @kambhampati2024can]; (iii) o ganho ao acoplar o LLM a um componente verificável em vez de usá-lo isolado [@guan2023leveraging; @liu2023llmp; @kambhampati2024llms; @tantakoun2025llms]. Por isso qualquer número neste eixo precisa vir com modelo e data.

## 5. Relação com a dissertação de 2010

| Rótulo | Relação | O que a literatura mostra | Chaves |
|---|---|---|---|
| A1 | Amplia | UML segue relevante: o valor do LLM está em produzir/refinar a representação formal (PDDL), não em substituí-la; surgem características novas (relações espaciais implícitas) sem equivalente em 2010 | [@tantakoun2025llms; @liu2023llmp; @silver2024generalized] |
| A2 | Confirma, com deslocamento | Busca heurística permanece central mesmo com LLM: RAP combina MCTS com heurística/modelo de mundo do próprio LLM; SayCanPay reencaixa o LLM em busca heurística clássica | [@hao2023reasoning; @hazra2024saycanpay] |
| A3 | Corrige/torna mais específica | Ranking "só com características do domínio" não se sustenta para LLM: Blocksworld e Mystery Blocksworld têm a mesma estrutura lógica e desempenho radicalmente diferente, por fatores lexicais/semânticos | [@kambhampati2024llms; @valmeekam2024llms; @valmeekam2023planbench] |
| A5 | Confirma no espírito, corrige o mecanismo | A complexidade do domínio segue afetando o desempenho, mas o eixo dominante para LLM é familiaridade lexical e comprimento do plano, não contagem UML | [@liu2023llmp; @silver2024generalized; @stechly2025self; @valmeekam2024llms] |
| A6 | Torna obsoleta a taxonomia fechada | Taxonomias de "técnica" se multiplicam (papel no pipeline, não tipo de busca): formalizador/editor/benchmark [@tantakoun2025llms], decomposição/seleção/módulo externo/reflexão/memória [@huang2024understanding] — nenhuma mapeia para forward-chaining/plan-space de 2010 | [@tantakoun2025llms; @huang2024understanding] |
| A7 | Amplia | Vários trabalhos vão além de cobertura binária: validade e otimalidade condicional do baseline humano [@valmeekam2023planning], tarefas auxiliares de verificação/replanejamento [@valmeekam2023planbench], custo computacional por resposta [@valmeekam2024llms] | [@valmeekam2023planning; @valmeekam2023planbench; @valmeekam2024llms] |

## 6. Divergências e pontos em disputa

[FATO] Há divergência de ênfase, não de dado bruto, entre a leitura "cética" (Kambhampati e colaboradores: LLMs não planejam nem se autoverificam sozinhos; só ajudam num LLM-Modulo com verificador externo sólido [@kambhampati2024llms; @kambhampati2024can; @stechly2025self]) e a leitura que enfatiza ganhos de arquitetura (o1-preview salta a 97,8% em Blocksworld comum [@valmeekam2024llms]; RAP com modelo menor supera CoT-GPT-4 [@hao2023reasoning]). Ambas vêm em parte do mesmo grupo (Kambhampati/Valmeekam/Stechly), o que reforça a consistência interna mas limita a diversidade de fontes.

[HIPÓTESE] Ponto não resolvido: se o teto em domínios ofuscados (~10% mesmo com verificador sólido [@kambhampati2024llms]) é limitação fundamental de LLMs autorregressivos ou efeito temporário de treinamento — a diferença entre o1-preview (52,8%) e GPT-4 (0,8–4,3%) em Mystery Blocksworld [@valmeekam2024llms; @kambhampati2024llms] sugere que raciocínio interno reduz, mas não fecha, a distância; nenhuma obra testa gerações posteriores.

## 7. Lacunas

[FATO] A busca dirigida do memorando de lacunas (`literatura/protocolo/busca/lacunas-memo.md`, lacuna L2) não encontrou, em oito *strings* e quatro bases (WebSearch, arXiv em texto completo, Crossref, Semantic Scholar bloqueado por limite de requisições), nenhum trabalho em que um LLM escolha o planejador, a heurística ou a configuração de portfólio — o papel de **seletor**, que a Q3 pede explicitamente. Consistente com as 20 notas: nenhuma descreve esse papel.

[HIPÓTESE] O memorando distingue "não encontramos" de "não existe": achou GRIMIP (2025–2026, LLM configurando solvers de programação inteira mista por instância) e `E7-037` (LLM enriquecendo representação de algoritmos num seletor de otimização combinatória) — nenhum sobre planejadores automatizados, mas a proximidade sugere extensão plausível, talvez em preprint não indexado. O veredito para L2 é "confirmada nas bases consultadas", não "prova de inexistência".

[HIPÓTESE] Lacuna adicional identificada nesta síntese, não coberta pelo memorando: nenhuma obra do eixo testa a relação entre métricas estruturais UML (as de 2010, via itSIMPLE) e o desempenho de qualquer papel de LLM — Silver et al. (2024) chegam perto, ao discutir características relacionais implícitas por trás do fracasso em Miconic, mas não modelam os domínios em UML [@silver2024generalized]. É a pergunta Q2 aplicada à era LLM, e nenhuma obra lida a responde diretamente.

## 8. Insumos para as próximas fases

[HIPÓTESE] Para o desenho da Fase 4 (camada LLM), três decisões emergem das obras lidas: (i) não desenhar em torno de "LLM como planejador direto" — desempenho baixo e volátil mesmo com LRMs, que mantêm dependência de domínio [@valmeekam2023planning; @kambhampati2024llms; @valmeekam2024llms]; (ii) desenhar em torno de "LLM como tradutor/formalizador acoplado a planejador clássico externo", o papel de maior ganho, seguindo LLM+P e Guan et al. [@liu2023llmp; @guan2023leveraging]; (iii) se houver verificação por LLM, acoplar sempre um verificador externo sólido, não autocrítica pura [@stechly2025self].

[HIPÓTESE] Precisa ser **congelado** antes de qualquer experimento novo: versão exata do(s) modelo(s) (não apenas "GPT-4"), data de acesso à API, configuração de *prompting*, e a versão exata dos domínios de teste (ofuscação determinística ou aleatorizada por instância, seguindo a prática de Valmeekam et al. 2024 [@valmeekam2024llms]). Sem isso, comparar um experimento próprio aos números aqui citados fica sem base.

[HIPÓTESE] Para comparar com os domínios de 2010, Storage e Grippers já aparecem em LLM+P com resultados altos (85% e 95–100%) [@liu2023llmp] — ponto de partida se a Fase 4 reaproveitar domínios comuns às duas literaturas.

## 9. Obras usadas

- @aghzal2025survey
- @guo2025deepseekr1
- @guan2023leveraging
- @hazra2024saycanpay
- @hao2023reasoning
- @huang2024understanding
- @kambhampati2024llms
- @kambhampati2024can
- @liu2023llmp
- @pallagani2024prospects
- @pallagani2023understanding
- @silver2024generalized
- @tantakoun2025llms
- @stechly2025self
- @valmeekam2023planbench
- @valmeekam2024llms
- @valmeekam2023planning
- @xie2023translating
- @xie2024travelplanner
- @yao2023react
