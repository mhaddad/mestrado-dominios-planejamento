---
tipo: sintese-exploratoria
fase: 5
pergunta: Q4
data: 2026-09-27
status: preliminar-aguarda-integracao-4b
---

# Fase 5 — da seleção de planejadores ao desenvolvimento de software dirigido por IA

## Síntese executiva

[FATO] Há uma conexão substantiva, embora não uma transferência demonstrada, entre a pergunta da dissertação e o desenvolvimento de software dirigido por IA. Estudos de reparo de programas e de agentes implantados mostram que o desempenho do mesmo agente varia com propriedades observáveis da tarefa, como a origem do *bug*, a riqueza da especificação e o contexto do repositório [@rondon2025evaluating; @takerngsaksiri2025humanintheloop]. Sistemas de roteamento de LLMs também mostram que escolher condicionalmente entre modelos pode reduzir custo sem sacrificar a qualidade na distribuição em que foram treinados [@ong2024routellm; @chen2023frugalgpt].

[FATO] A revisão e os experimentos deste projeto impõem uma ressalva tão importante quanto a conexão. Nas Fases 3 e 4, métricas UML e *features* SAS+ não acrescentaram poder preditivo suficiente para selecionar planejadores por domínio, e o LLM não superou a linha de base como seletor. A segunda rodada da Fase 4B aponta provisoriamente na mesma direção para 16 *features* SAS+ e famílias de técnicas. Esses resultados não falam diretamente sobre software, mas tornam implausível tratar métricas estruturais estáticas como solução suficiente.

[HIPÓTESE] A oportunidade não é reproduzir o método de 2010 sobre código. É formular um problema mais completo de escolha de configuração: caracterizar a tarefa, o repositório, a configuração do agente e, quando existir, a trajetória parcial de execução; otimizar resultado, custo, tempo e qualidade; e comparar a política condicional com uma configuração fixa forte. O resultado desta fase é uma agenda de pesquisa, não uma recomendação de produto nem uma alegação de eficácia.

## 1. Pergunta e escopo

Q4 pergunta quais conexões, oportunidades e hipóteses ligam o ajuste entre características da tarefa e estratégia de solução ao desenvolvimento de software dirigido por IA. A resposta desta síntese não é “sim, o ajuste funciona”: não houve experimento próprio em tarefas de software, nem piloto no Ateliê.

O que foi feito aqui foi uma consolidação das fontes verificadas dos eixos E7 e E8, dos relatórios das Fases 3 e 4 e do EXP-21 da Fase 4B. A síntese da 4B ainda está incompleta; por isso este documento é preliminar e deverá ser integrado antes do encerramento da fase.

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

## 7. Integração pendente da Fase 4B

O EXP-21 fornece, até aqui, um contrapeso útil: em IPCs de 2011 e 2018, 16 *features* SAS+ quase não antecipam, fora do domínio, a família de técnica que resolve uma instância; os poucos sinais que permanecem após a correção estatística se concentram em famílias pequenas ou planejadores específicos. O resultado ainda é provisório porque a rodada de 2018 e as propriedades teóricas previstas pela 4B não estão fechadas.

[HIPÓTESE] Se a conclusão se mantiver após R-29 e as propriedades teóricas, ela reforçará quatro exigências desta Ponte: não supor que *features* estáticas bastam; comparar contra uma linha de base fixa; separar efeitos de configuração específica de efeitos de família; e privilegiar a unidade tarefa/instância. A integração final deve registrar também qualquer resultado da 4B que limite ou contrarie essa leitura.

## 8. Conclusão provisória

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
