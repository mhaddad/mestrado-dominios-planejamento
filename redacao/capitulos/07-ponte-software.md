---
titulo: "Do domínio de planejamento ao desenvolvimento de software dirigido por IA"
status: revisado-por-ia
data: 2026-09-28
fonte: ponte-software/relatorio/sintese-exploratoria.md; ponte-software/relatorio/dossie-capitulo-7.md; experimentos/relatorio-fase4b.md
---

# Do domínio de planejamento ao desenvolvimento de software dirigido por IA

Este capítulo responde à Q4 por meio de uma investigação exploratória. Seu objetivo não é declarar que as métricas de domínio de 2010 selecionam agentes de software, nem propor um roteador pronto para equipes. A contribuição é formular com precisão onde a pergunta original permanece útil e quais condições uma aplicação real teria de satisfazer.

A pergunta de 2010 pode ser enunciada como um problema de ajuste: em que condições características de um problema ajudam a escolher uma técnica de solução? Essa estrutura pertence à seleção de algoritmos, que relaciona espaços de problemas, *features*, algoritmos e desempenho [@smithmiles2009cross]. Em desenvolvimento de software apoiado por IA, o problema reaparece, mas com uma unidade mais situada, configurações mais compostas e resultados que não cabem em uma medida única.

## A conexão e seus limites

Há evidência de que o desempenho de agentes de software varia com a tarefa e o contexto. Em reparo de programas, o mesmo agente obteve *patches* plausíveis em 78% dos casos originados por sanitizadores e em 25,6% dos *bugs* relatados por humanos; o estudo associa a diferença à buscabilidade da descrição, à dispersão da mudança e à diversidade de linguagens [@rondon2025evaluating]. Em um agente implantado na Atlassian, a passagem de tarefas do SWE-bench para *issues* internos reduziu o *recall* do agente de planejamento de 86% para 30% e a similaridade do agente de código de 45% para 30%; os autores relacionam parte da diferença à riqueza das descrições disponíveis [@takerngsaksiri2025humanintheloop].

Esses resultados sustentam uma afirmação limitada: tarefa e contexto importam para o desempenho de agentes. Eles não demonstram que exista uma métrica estrutural única capaz de escolher a melhor configuração. Também não autorizam inferir causalidade de uma característica isolada, pois versão do modelo, *prompt*, recuperação de contexto, conjunto de testes e distribuição de *issues* podem explicar parte da variação observada.

O resultado da presente revisão reforça essa cautela. Nos capítulos 5 e 6, nem métricas UML, nem *features* SAS+, nem LLMs usados como seletores superaram de modo robusto uma escolha fixa forte. Nas IPCs de 2011 e 2018, a AUC mediana das *features* SAS+ para prever, fora do domínio, a resolução por família foi 0,59, praticamente igual aos 0,58 de um modelo que recebe apenas o tamanho da tarefa. A seleção por instância tampouco superou o melhor planejador único quando todos os planejadores foram incluídos. <!-- fonte: EXP-21; EXP-24 --> A ponte, portanto, preserva a pergunta e descarta a promessa de transferir a solução de 2010.

## Da tarefa PDDL à tarefa situada

Um domínio PDDL descreve ações, estados e objetivos em uma forma relativamente estável. Uma tarefa de software começa, em geral, com uma especificação incompleta, exige localizar contexto em um repositório que evolui e pode gerar informação relevante durante a execução. A unidade de análise adequada não é apenas o repositório, nem apenas a *issue*, mas a combinação entre tarefa, estado do repositório, configuração e momento da execução.

Essa dimensão temporal tem evidência contemporânea. O SWE-Router executa alguns turnos exploratórios com um modelo mais barato e usa a trajetória parcial para decidir se continua ou escala a execução [@son2026swerouter]. O resultado é uma evidência de fronteira, baseada em *benchmarks*, e não uma demonstração organizacional. Ainda assim, ele mostra por que uma decisão tomada somente sobre a descrição inicial pode ser incompleta. Mais contexto tampouco é automaticamente melhor: no SWE-bench, aumentar a janela de contexto elevou o *recall* de arquivos corretos, mas reduziu o desempenho do Claude 2 [@jimenez2024swebench].

Assim, a correspondência com os elementos de planejamento deve ser tratada como hipótese de trabalho, e não como identidade entre os domínios.

| Planejamento automático | Correspondência exploratória em software com IA | Limite da correspondência |
|---|---|---|
| Problema ou domínio | Tarefa situada, como *bug*, história ou refatoração, no contexto do repositório | A tarefa pode mudar enquanto o agente atua |
| Características do domínio | Tipo de tarefa, clareza da especificação, dispersão da mudança, testes, histórico e métricas de código | Não há conjunto validado de *features* estruturais para selecionar agentes |
| Técnica e planejador | Configuração de agente: modelo, ferramentas, permissões, estratégia, verificador, orçamento e supervisão | A configuração é composta e pode mudar durante a execução |
| Cobertura | Correção, qualidade, segurança, tempo, custo e retrabalho | Os resultados são multidimensionais |
| Ranking | Política fixa, roteador ou escalonamento | A política precisa superar uma referência fixa fora da amostra |

: Correspondências exploratórias entre planejamento e desenvolvimento de software com IA

::: fonte
Fonte: Autor.
:::

## Configuração, não apenas modelo

Chamar uma decisão de “usar GPT” ou “usar Claude” não define uma alternativa experimental suficiente. A configuração comparável a um planejador inclui, entre outros elementos, a versão do modelo, instruções de sistema, ferramentas e permissões, estratégia de planejamento, uso de subagentes, verificador, orçamento de tempo e *tokens*, ponto de escalonamento e revisão humana. A variável de comparação é a configuração inteira, e não o nome isolado do modelo.

Essa formulação tem dois apoios, de escopos distintos. AS-LLM combina características do problema a uma representação do próprio algoritmo e encontra, em sua ablação, perda importante quando a representação do algoritmo é retirada [@wu2024large]. SALLMA propõe uma arquitetura em que a camada operacional coordena fluxos e roteamento, enquanto a camada de conhecimento cataloga configurações de agentes [@becattini2025sallma]. SALLMA é uma prova de conceito funcional e qualitativa; ele serve como referência arquitetural, não como evidência de que essa separação melhora a seleção de agentes de código.

O resultado também não deve ser reduzido a “tarefa resolvida”. O capítulo 5 mostrou que cobertura, qualidade de plano, tempo e memória podem alterar a interpretação de desempenho. Em software, passar testes não garante que o artefato seja abrangente, eficiente ou legível [@jimenez2024swebench]; estudos com usuários indicam que assistentes podem produzir código menos seguro mesmo quando aumentam a confiança do participante [@perry2023do]. Uma escolha responsável de configuração precisa, portanto, declarar quais objetivos e restrições usa.

## Da escolha única à política em estágios

A literatura recente sugere que “escolher um agente” encobre ao menos três decisões. A primeira ocorre **antes da execução**: encaminhar uma tarefa com base na descrição, no repositório e no histórico de casos comparáveis. Um roteador de atualizações de dependência exemplifica esse estágio ao evitar chamadas desnecessárias de agentes em parte da amostra [@fan2026dependencyrouter]. A segunda ocorre **durante a execução**: manter, escalar, trocar ou interromper uma configuração quando surgem sinais de trajetória. SWE-Router e RISA tratam justamente essa decisão intermediária [@son2026swerouter; @chen2026risa]. A terceira ocorre **antes da integração**: aceitar o artefato, solicitar correção ou encaminhar a revisão humana, conforme testes, análise estática, segurança e risco da mudança.

Essa decomposição evita supor que uma descrição inicial contém toda a informação relevante. Também explica por que o histórico pode ser mais útil que uma descrição abstrata das capacidades do agente: em um experimento de roteamento, estatísticas de desempenho anterior melhoraram a resolução, enquanto descrições textuais das dimensões dos agentes praticamente não o fizeram [@zhou2026agentasarouter]. Arquiteturas como SALLMA separam a camada operacional, que coordena fluxos, da camada de conhecimento, que cataloga configurações [@becattini2025sallma]; a separação é conceitualmente compatível com a política em estágios, embora a prova de conceito não demonstre ganho causal de seleção.

Considere, por exemplo, uma atualização de biblioteca. Antes da execução, sinais simples — existência de testes, alcance declarado da mudança, criticidade do módulo e histórico de atualizações semelhantes — podem encaminhá-la a uma configuração econômica ou à revisão humana. Após instalar a versão, falhas de compilação, dispersão dos arquivos alterados e comportamento dos testes atualizam a decisão: continuar, escalar para uma configuração com mais contexto ou interromper. Antes do *merge*, verificadores independentes avaliam o resultado. O exemplo não prescreve um roteador; ele torna observáveis os pontos em que uma política futura precisaria ser comparada com o fluxo fixo já usado pela equipe.

## Uma formulação para investigação futura

Seja `t` uma tarefa situada; `φ(t)`, a representação de suas características antes da execução; `A`, o conjunto de configurações disponíveis; `ψ(A)`, a descrição dessas configurações e de seu histórico; `τ`, os sinais produzidos por uma exploração parcial; `w`, os objetivos e restrições da equipe; e `y`, um vetor de resultados que inclui correção, qualidade, segurança, tempo, custo e necessidade de retrabalho humano. A hipótese de trabalho é escolher uma política

`π(φ(t), ψ(A), τ, w) ∈ A ∪ {revisão humana, interromper}`

que seja preferível a uma configuração fixa forte sob objetivos e restrições explícitos. Sua saída é uma configuração de `A` ou uma decisão de não prosseguir automaticamente. A política pode ser novamente avaliada quando `τ` muda; portanto, roteamento inicial e escalonamento durante a execução pertencem ao mesmo problema decisório, mas usam informações diferentes.

Essa formulação não é apresentada como método novo. Ela sintetiza seleção de algoritmos, roteamento de modelos, avaliação de agentes e ajuste entre tarefa e tecnologia. A literatura de roteamento já mostra que cascatas podem reduzir custo preservando qualidade quando são treinadas e avaliadas na distribuição relevante [@ong2024routellm; @chen2023frugalgpt]. O que esta dissertação acrescenta é uma genealogia crítica: uma política não deve ser presumida melhor apenas porque usa mais informação ou é mais complexa.

## Salvaguardas antes de qualquer roteamento

Os resultados negativos das Fases 3, 4 e 4B sugerem cinco perguntas operacionais anteriores ao desenvolvimento de um roteador.

1. **Há heterogeneidade reproduzível?** Configurações diferentes vencem em regiões distintas de tarefas, ou uma configuração fixa já domina?
2. **O sinal acrescenta algo?** Métricas estáticas de código superam sinais simples, como tipo de tarefa, tamanho, qualidade da descrição e histórico de desempenho?
3. **Qual é o custo total da decisão?** Uma configuração barata pode falhar; uma cara pode desperdiçar recursos; a coleta e a classificação também têm custo.
4. **O ganho generaliza?** A política funciona em repositórios, períodos ou equipes não observados no treino?
5. **A verificação é independente da geração?** Testes, análise estática e revisão humana detectam falhas sem depender apenas da autocrítica do mesmo agente?

Essas perguntas mudam a adoção de agentes de uma decisão baseada em reputação de modelo para uma hipótese mensurável. A Fase 4B acrescenta uma precaução específica: o pequeno ganho de topologia veio de sondar a tarefa com hFF, não de leitura estática do PDDL. <!-- fonte: EXP-25 --> Por analogia, uma tentativa curta e barata — como executar testes ou observar os primeiros passos do agente — pode ser mais informativa do que métricas estáticas do repositório. Essa é uma hipótese a testar, não um resultado sobre software.

## Níveis de aplicabilidade

O primeiro nível de aplicação é observabilidade. Uma equipe pode registrar tipo de mudança, clareza do pedido, extensão estimada, módulos envolvidos, disponibilidade de testes, maturidade do trecho, configuração utilizada e resultados. O objetivo inicial não é automatizar a escolha, mas tornar a distribuição de tarefas e resultados visível. Essa etapa é compatível com a evidência de que *issues* de *benchmark* e de produção diferem em contexto e desempenho [@takerngsaksiri2025humanintheloop].

O segundo nível, condicionado a heterogeneidade local reproduzível, é comparar uma política simples com uma configuração fixa. Tarefas bem especificadas e localizadas poderiam seguir um fluxo curto de localização, reparo e validação; tarefas ambíguas ou distribuídas poderiam demandar planejamento adicional, verificação ou revisão humana. Uma abordagem fixa e simples pode ser competitiva em parte do espaço, como sugere Agentless no SWE-bench Lite [@xia2025demystifying], mas não se segue daí uma regra de roteamento universal.

O terceiro nível incorpora a dimensão sociotécnica. O *Task-Technology Fit* relaciona ajuste entre tarefa, tecnologia e uso a desempenho individual [@goodhue1995task], mas não é uma teoria de seleção automática prévia. Para agentes, supervisão, confiança, revisão, responsabilidade pelo *merge* e capacidade da equipe de absorver o resultado podem alterar o efeito. Uma política tecnicamente bem ajustada pode falhar se for introduzida sem integração aos controles humanos.

## Hipóteses testáveis

| ID | Unidade e sinal | Comparação e resultado esperado | Condição de refutação |
|---|---|---|---|
| H1 | Tarefa × configuração, com repetições | Configurações vencem em regiões distintas acima da variação entre execuções | Uma configuração fixa domina de modo estável as regiões observadas |
| H2 | Tarefa situada; sinais disponíveis antes da execução | Política supera a configuração fixa forte em repositórios ou períodos mantidos fora | O ganho desaparece fora da amostra ou não paga o custo do roteamento |
| H3 | Tarefa e repositório; sinais simples mais métricas estruturais | Ablação mostra ganho incremental das métricas de código | As métricas não melhoram a previsão ou reduzem a robustez |
| H4 | Trajetória parcial limitada por orçamento | Política com escalonamento melhora o objetivo total frente à decisão apenas estática | A exploração consome custo ou tempo sem benefício líquido |
| H5 | Mesmas tarefas sob funções objetivo previamente fixadas | A decisão muda de forma explicável quando segurança, custo ou prazo recebem pesos distintos | Uma política domina todos os objetivos relevantes sem compromisso mensurável |
| H6 | Artefato produzido e verificadores independentes | Verificação externa reduz defeitos escapados sem custo desproporcional | A etapa não detecta falhas adicionais ou inviabiliza o fluxo |

: Hipóteses derivadas da ponte exploratória

::: fonte
Fonte: Autor.
:::

H1 e H2 precisam de validação por repositório, família de tarefa ou período mantido fora, e não apenas por reamostragem aleatória de tarefas semelhantes. H3 é deliberadamente cética à luz dos resultados desta dissertação: métricas estruturais são candidatas a variável explicativa, não base para promessa de seleção. H4 deriva da diferença entre sinais estáticos e sondagem de execução; H5 protege contra reduzir resultados sociotécnicos a uma taxa única de resolução; H6 incorpora a evidência, observada também no capítulo 6, de que geração e verificação não devem ser confundidas.

## Conclusão

O desenvolvimento de software dirigido por IA oferece evidência de heterogeneidade por tarefa e de mecanismos de roteamento. A presente revisão mostra, por sua vez, que heterogeneidade não é automaticamente capturada por métricas estruturais nem convertida em um seletor útil. A conexão mais defensável é metodológica: tratar a escolha de configuração de agente como seleção condicional, mas medir antes se há sinal preditivo incremental, contra qual linha de base ele será comparado e quais resultados não podem ser sacrificados.

Não se recomenda produto, piloto ou política específica para uma organização. A aplicabilidade desta pesquisa consiste em fornecer uma pergunta melhor e salvaguardas para respondê-la: caracterizar tarefa e configuração, medir resultados múltiplos, validar fora do contexto observado e manter uma configuração fixa forte como referência. Esse enquadramento transforma uma possível aplicação no mundo real em agenda verificável, e não em extrapolação da analogia.
