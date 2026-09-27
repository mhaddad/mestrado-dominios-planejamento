---
tipo: sintese-exploratoria
fase: 5
pergunta: Q4
data: 2026-09-27
status: concluida-aguarda-revisao-do-autor
---

# Fase 5 — da seleção de planejadores ao desenvolvimento de software dirigido por IA

## Síntese executiva

[FATO] Há uma conexão substantiva, embora não uma transferência demonstrada, entre a pergunta da dissertação e o desenvolvimento de software dirigido por IA. Estudos de reparo de programas e de agentes implantados mostram que o desempenho do mesmo agente varia com propriedades observáveis da tarefa, como a origem do *bug*, a riqueza da especificação e o contexto do repositório [@rondon2025evaluating; @takerngsaksiri2025humanintheloop]. Sistemas de roteamento de LLMs também mostram que escolher condicionalmente entre modelos pode reduzir custo sem sacrificar a qualidade na distribuição em que foram treinados [@ong2024routellm; @chen2023frugalgpt].

[FATO] A revisão e os experimentos deste projeto impõem uma ressalva tão importante quanto a conexão. Nas Fases 3 e 4, métricas UML e *features* SAS+ não acrescentaram poder preditivo suficiente para selecionar planejadores por domínio, e o LLM não superou a linha de base como seletor. Na rodada final da Fase 4B, as 16 *features* SAS+ quase não anteciparam, fora do domínio, qual família resolveria uma instância nas IPCs de 2011 e 2018: a AUC mediana da logística foi 0,59, praticamente igual aos 0,58 do modelo só com tamanho. Na seleção por instância, nenhum seletor superou o melhor planejador único com todos os planejadores disponíveis; o único ganho local não sobreviveu à correção conjunta. Esses resultados não falam diretamente sobre software, mas tornam implausível tratar métricas estruturais estáticas como solução suficiente.

[HIPÓTESE] A oportunidade não é reproduzir o método de 2010 sobre código. É formular um problema mais completo de escolha de configuração: caracterizar a tarefa, o repositório, a configuração do agente e, quando existir, a trajetória parcial de execução; otimizar resultado, custo, tempo e qualidade; e comparar a política condicional com uma configuração fixa forte. O resultado desta fase é uma agenda de pesquisa, não uma recomendação de produto nem uma alegação de eficácia.

## 1. Pergunta e escopo

Q4 pergunta quais conexões, oportunidades e hipóteses ligam o ajuste entre características da tarefa e estratégia de solução ao desenvolvimento de software dirigido por IA. A resposta desta síntese não é “sim, o ajuste funciona”: não houve experimento próprio em tarefas de software, nem piloto no Ateliê.

O que foi feito aqui foi uma consolidação das fontes verificadas dos eixos E7 e E8, dos relatórios das Fases 3 e 4 e dos EXP-21 e EXP-24 da Fase 4B. A integração usa os resultados finais disponíveis para as 16 *features* SAS+ e a cobertura nas IPCs de 2011 e 2018; ela não presume que propriedades teóricas ainda não avaliadas teriam o mesmo comportamento.

O [dossiê para o Capítulo 7](dossie-capitulo-7.md) aprofunda a arquitetura argumentativa, as objeções conceituais, os limites de inferência e os subsídios de redação.

## 2. O que já é evidência

### 2.1 O desempenho de agentes de código varia com a tarefa e o contexto

[FATO] Em um *benchmark* industrial de reparo de programas, o mesmo agente com Gemini 1.5 Pro obteve *patch* plausível em 78% dos casos reportados por sanitizadores, 68% dos de dependência de ordem de testes e 25,6% dos reportados por humanos. O estudo associa a diferença à buscabilidade da descrição, à dispersão espacial da mudança e à diversidade de linguagens [@rondon2025evaluating]. Isso sustenta a afirmação limitada de que a dificuldade e a estrutura da tarefa importam para o desempenho do agente.

[FATO] Na Atlassian, o HULA teve desempenho inferior ao passar do SWE-bench para *issues* internos: o agente de planejamento caiu de 86% para 30% de *recall* na identificação de arquivos e o de código de 45% para 30% de similaridade. Os autores atribuem parte da diferença à forma como a tarefa é escrita: *issues* do benchmark trazem detalhes e nomes de módulos que *issues* internos frequentemente não trazem [@takerngsaksiri2025humanintheloop].

[FATO] Há também evidência de que uma estratégia mais complexa não é automaticamente melhor. No SWE-bench Lite, o Agentless — fluxo fixo de localização, reparo e validação — superou os agentes de código de código aberto da comparação em desempenho e custo [@xia2025demystifying]. Isso impede que a taxonomia de configurações trate “mais agêntico” ou “mais sofisticado” como sinônimo de melhor.

### 2.2 A seleção condicional existe, mas depende de evidência situada

[FATO] RouteLLM aprende a rotear consultas entre um modelo forte e um mais barato, e relata redução de custo mantendo qualidade nos *benchmarks* avaliados; seu próprio resultado depende de dados de preferência ou desempenho da distribuição relevante [@ong2024routellm]. FrugalGPT encontra complementaridade de erros entre modelos e exige exemplos rotulados da mesma distribuição ou de uma semelhante para a cascata funcionar bem [@chen2023frugalgpt].

[FATO] A seleção de algoritmos pode se beneficiar de informação sobre ambos os lados da relação. AS-LLM combina *features* do problema com representação do algoritmo extraída do código; no estudo de ablação, retirar as *features* do algoritmo causa a maior perda, e o método supera comparadores em oito dos dez cenários do ASLib [@wu2024large].

[HIPÓTESE] Para agentes de software, isso sugere descrever uma configuração como um objeto composto — modelo, ferramentas, permissões, estratégia, verificador, orçamento e critério de escalonamento — e não apenas pelo nome do modelo. A hipótese não foi testada pelo AS-LLM em agentes de código.

### 2.3 Medidas agregadas escondem o que importa

[FATO] A *Instance Space Analysis* foi proposta justamente para revelar pontos fortes e fracos de algoritmos que ficam ocultos em desempenho médio sobre uma coleção de instâncias [@smithmiles2023instance]. Em desenvolvimento de software, um estudo longitudinal da adoção do Copilot não encontrou mudança estatisticamente significativa em atividade de *commit*, embora os participantes relatassem benefícios; o desenho também registrou autosseleção entre quem adotou a ferramenta [@stray2025developer].

[HIPÓTESE] A unidade informativa para a futura agenda não é o repositório inteiro nem a equipe inteira, mas a tarefa situada: tarefa, estado do repositório, configuração do agente, trajetória e resultado. Agregar cedo demais poderia esconder justamente a heterogeneidade que a Ponte quer compreender.

## 3. O que a dissertação transfere — e o que não transfere

| Elemento de planejamento | Correspondência exploratória em software com IA | Estado | Limite |
|---|---|---|---|
| Problema/domínio | Tarefa situada: *issue*, *bug*, história, refatoração, com o contexto do repositório | [HIPÓTESE] útil | Uma tarefa de software muda enquanto o agente atua; não é um domínio PDDL fixo. |
| Características do domínio | Tipo de tarefa, clareza da especificação, dispersão da mudança, maturidade e saúde do código, cobertura de testes | [FATO] como candidatas | Ainda não há conjunto validado de *features* estruturais que selecione agentes. |
| Técnica/planejador | Configuração de agente: modelo, estratégia, ferramentas, verificador, subagentes e supervisão | [HIPÓTESE] útil | A configuração pode mudar durante a execução; a taxonomia de planejadores não basta. |
| Desempenho | Correção, aceitação, qualidade, segurança, tempo e custo | [FATO] como exigência metodológica | Não devem ser reduzidos a “tarefa resolvida”. |
| Seletor | Política fixa, roteador por tarefa ou escalonamento após observação parcial | [HIPÓTESE] promissora | A política precisa superar uma configuração fixa em avaliação fora da amostra. |

O principal ponto de não transferência vem das Fases 3 e 4. A tentativa de escolher técnica de planejamento a partir de métricas estruturais não superou a linha de base; portanto, a semelhança de origem das métricas UML e de código não licencia reutilizá-las como preditores. Elas continuam candidatas a variável explicativa, e não base para uma promessa de seleção.

## 4. Uma formulação mais rigorosa da oportunidade

[HIPÓTESE] Seja uma tarefa situada `t`, uma representação de suas características `φ(t)`, uma configuração de agente `a`, uma descrição da própria configuração `ψ(a)` e, quando houver, sinais observados após uma exploração limitada `τ`. O problema futuro seria escolher uma política `π(φ(t), ψ(a), τ)` que maximize uma função multiobjetivo de correção, qualidade, segurança, tempo e custo.

Essa formulação difere de 2010 em cinco pontos:

1. A unidade é a tarefa, não a média de um domínio.
2. A configuração é caracterizada, não tratada só como rótulo de técnica.
3. O sinal pode ser estático e também surgir durante a execução.
4. O objetivo é multiobjetivo; cobertura ou aceite binário é apenas uma medida.
5. A linha de base obrigatória é uma configuração fixa forte, não apenas um ranking por médias.

[FATO] Essa formulação é compatível com a estrutura de seleção de algoritmos e com a crítica da ISA a médias agregadas [@smithmiles2023instance; @wu2024large]. [HIPÓTESE] Ela ainda precisa de validação no domínio específico de agentes de software.

## 5. Hipóteses e condições de refutação

| ID | Hipótese | O que a sustentaria | O que a enfraqueceria |
|---|---|---|---|
| H1 | Nenhuma configuração é a melhor para todos os tipos de tarefa. | Matriz tarefa × configuração com vitórias distribuídas entre configurações, fora do erro de medição. | Uma configuração fixa domina de modo estável todas as regiões observadas. |
| H2 | Características da tarefa e do repositório ajudam a escolher configuração melhor que uma linha de base fixa. | Política avaliada fora da amostra supera a configuração fixa em objetivo pré-definido. | Ganho não se sustenta fora da amostra ou é explicado apenas por tamanho/complexidade trivial. |
| H3 | Métricas estruturais de código acrescentam informação às características textuais e históricas. | Ablação mostra ganho reproduzível ao adicioná-las. | Não há ganho sobre texto, tamanho, tipo de tarefa e desempenho passado. |
| H4 | Sinais da trajetória parcial do agente acrescentam informação às características estáticas. | Escalonamento ou troca tardia supera roteamento decidido só no início. | A trajetória não melhora previsão, ou custa mais que o benefício. |
| H5 | Uma política de seleção deve otimizar mais que taxa de conclusão. | O resultado permanece favorável quando qualidade, segurança, tempo e custo são reportados separadamente. | O ganho em conclusão é anulado por piora relevante em uma dimensão crítica. |

Todas são `[HIPÓTESE]`. H1 e H2 são informadas pelos estudos de heterogeneidade e roteamento; H3, em vez de ser consequência de 2010, é deliberadamente uma hipótese cética à luz dos resultados negativos das Fases 3 e 4.

## 6. Oportunidades que decorrem do trabalho

### 6.1 Agenda de pesquisa

[HIPÓTESE] A oportunidade acadêmica é deslocar a pergunta de “quais métricas de código escolhem o melhor agente?” para “que combinação de informação estática, contextual e dinâmica permite escolher ou escalar configurações sem piorar qualidade?”. Isso evita repetir a redução de 2010 e aproxima o problema de seleção de algoritmos de sua formulação contemporânea.

Um estudo posterior teria de construir uma matriz de tarefas reais ou *benchmarks* por configuração, congelar versões e *prompts*, pré-definir métricas e comparar, no mínimo, uma configuração fixa, um roteador baseado em regras simples e uma política aprendida. A generalização deveria ser por repositório ou por família de tarefas mantida fora do treino, não por reamostragem aleatória de tarefas quase idênticas.

### 6.2 Instrumentação e transparência

[HIPÓTESE] Antes de qualquer roteador sofisticado, há uma oportunidade mais simples: tornar a configuração do agente observável e reprodutível. Registrar modelo, ferramentas, permissões, orçamento, estratégia, verificador, versões e resultado por tarefa permite descobrir se há heterogeneidade antes de tentar predizê-la. Essa é a analogia metodológica mais segura com a replicação das Fases 3 e 4.

### 6.3 Limites para uma oportunidade de produto

[FATO] A evidência consultada mostra que roteamento e cascatas podem funcionar em distribuições e métricas bem definidas [@ong2024routellm; @chen2023frugalgpt]. [HIPÓTESE] Isso não constitui base para produto de desenvolvimento de software: faltam validação no contexto alvo, tratamento de qualidade e segurança, comparação com uma configuração fixa forte e evidência de estabilidade quando modelos, repositórios e processos mudam. Esta fase, portanto, não recomenda produto.

## 7. Integração da Fase 4B

[FATO] O EXP-21 final confirma, no seu recorte, que há heterogeneidade por domínio e trilha, mas que as 16 *features* SAS+ não a antecipam robustamente fora do domínio. Nos 40 modelos por família do recorte completo, a AUC mediana da regressão logística foi 0,59, contra 0,58 usando apenas tamanho; a árvore rasa teve mediana 0,49. Depois de Holm, os poucos modelos sobreviventes se concentram sobretudo em famílias de um a três planejadores. A exceção com vários planejadores — *landmarks* na ótima de 2018, sem portfólios — ocorre em um só recorte e não se reproduz com portfólios nem na árvore rasa.

[FATO] O EXP-24 testa a consequência mais próxima para a Ponte: escolher um planejador por instância, deixando um domínio de fora. Com todos os planejadores, nenhum seletor supera o melhor planejador único em nenhuma das dez unidades edição × trilha × recorte. Sem portfólios, o seletor 4D melhora a *agile* de 2018 numa correção local, mas o resultado deixa de ser significativo quando as 60 comparações são corrigidas juntas. É um indício de condição de contorno — há mais espaço para seleção quando a linha de base fixa é fraca —, não uma demonstração de política útil.

[INFERÊNCIA] A 4B reforça quatro exigências da Ponte: não supor que *features* estáticas bastam; comparar contra uma linha de base fixa forte; separar efeito de família, planejador e portfólio; e validar por tarefa/instância fora de repositórios ou domínios observados. Ela não autoriza concluir que nenhum sinal poderá funcionar em software: o recorte mede 16 *features* SAS+ e cobertura, não características de código, trajetória de agentes, segurança ou qualidade de manutenção.

## 8. Conclusão

[FATO] O desenvolvimento de software dirigido por IA já fornece evidência de heterogeneidade por tarefa e de mecanismos de roteamento entre modelos. [FATO] O trabalho desta dissertação mostra que essa heterogeneidade não é automaticamente capturada por métricas estruturais nem convertida em um seletor útil. 

[HIPÓTESE] A conexão mais defensável é, portanto, metodológica: tratar a escolha de configuração de agente como problema de seleção condicional, mas medir primeiro se há sinal preditivo real, de quais tipos e contra qual linha de base. A contribuição potencial da dissertação não é prometer um roteador para equipes de software; é oferecer uma genealogia crítica e um conjunto de salvaguardas para não repetir, nesse novo domínio, a inferência que os próprios experimentos revisados não sustentaram.

## Referências usadas

- @chen2023frugalgpt
- @ong2024routellm
- @rondon2025evaluating
- @smithmiles2023instance
- @stray2025developer
- @takerngsaksiri2025humanintheloop
- @wu2024large
- @xia2025demystifying
