---
tipo: dossie-editorial
fase: 5
destino: redacao/capitulos/07-do-planejamento-ao-software.md
data: 2026-09-27
status: base-para-redacao-aguarda-integracao-4b
---

# Dossiê para o Capítulo 7 — do planejamento ao desenvolvimento de software apoiado por IA

## 1. Função do capítulo

O capítulo não deve vender uma aplicação pronta, nem encerrar a dissertação com uma analogia confortável. Sua função é mostrar que a pergunta de 2010 — em que condições características de um problema ajudam a escolher uma técnica de solução — reaparece em um trabalho de engenharia de software que já usa agentes de IA, mas reaparece transformada.

A contribuição aplicável da dissertação não é uma regra do tipo “para tal métrica de código, use tal agente”. Os resultados das Fases 3 e 4 impedem essa promessa. A contribuição é uma forma de enquadrar e avaliar a decisão: antes de padronizar um agente, uma organização precisa distinguir a tarefa, a configuração do agente e os critérios de resultado; precisa medir se há heterogeneidade real; e precisa demonstrar que uma política condicional melhora uma linha de base fixa em tarefas que não viu.

**Tese editorial proposta.**

> [HIPÓTESE] A permanência prática da pesquisa de 2010 não está em suas métricas UML como instrumento de seleção. Está na pergunta de ajuste entre problema e técnica, corrigida pela própria revisão: em desenvolvimento de software com IA, a escolha de uma configuração de agente deve ser tratada como seleção condicional, com características de tarefa, contexto de repositório, configuração do agente, sinais de execução e objetivos múltiplos.

O *perspective shift* desejado é este: sair de “qual é o melhor agente para programar?” para “em que condições, segundo quais evidências e com quais custos uma configuração é preferível a outra?”.

## 2. Escada de inferência: o que o capítulo pode afirmar

| Degrau | Afirmação | Estatuto | Base |
|---|---|---|---|
| 1 | O problema de escolher um algoritmo conforme o problema tem arcabouço formal estabelecido em seleção de algoritmos e meta-aprendizado. | [FATO] | [@smithmiles2009cross; @smithmiles2023instance] |
| 2 | Em tarefas de software, o desempenho de agentes varia com propriedades observáveis da tarefa e do contexto. | [FATO] | [@rondon2025evaluating; @takerngsaksiri2025humanintheloop; @jimenez2024swebench] |
| 3 | Em tarefas gerais de linguagem, roteadores e cascatas mostram que a escolha condicional entre modelos pode melhorar o compromisso entre custo e qualidade quando treinada e avaliada na distribuição relevante. | [FATO] | [@ong2024routellm; @chen2023frugalgpt] |
| 4 | Logo, faz sentido formular a escolha de configurações de agentes de software como um problema de seleção condicional. | [HIPÓTESE] | Síntese dos degraus 1–3 |
| 5 | Métricas estruturais estáticas de código são suficientes para resolver esse problema. | Não sustentado | Fases 3, 4 e 4B; ausência de estudo direto |
| 6 | Um roteador de agentes produzirá ganho numa equipe ou repositório específico. | Não sustentado | Não houve experimento próprio nem validação naquele contexto |

Essa escada impede dois erros opostos. O primeiro seria ignorar uma conexão que já possui evidência parcial: tarefas e contexto de fato alteram o desempenho de agentes. O segundo seria chamar de “aplicação” aquilo que é somente a transposição de um vocabulário.

## 3. Onde a analogia é forte, e onde ela se rompe

### 3.1 A estrutura que permanece

Em 2010, o esquema implícito era: descrição de domínio → métricas → técnica/planejador → cobertura. No caso de software apoiado por IA, há uma estrutura reconhecível: tarefa situada → características observáveis → configuração de agente → resultado. A literatura de seleção de algoritmos organiza essa estrutura como espaços de problemas, *features*, algoritmos e desempenho [@smithmiles2009cross].

[FATO] O paralelo não é apenas terminológico. Em reparo de programas, uma mesma configuração de agente obtém resultados muito diferentes conforme o tipo/origem do *bug*; Rondon et al. reportam 78% de *patches* plausíveis em casos de sanitizador e 25,6% em *bugs* humanos [@rondon2025evaluating]. Em agentes implantados, a forma e a riqueza da especificação também mudam o desempenho: no HULA, os autores associam a queda do SWE-bench para *issues* internos à natureza mais curta e colaborativa das descrições internas [@takerngsaksiri2025humanintheloop].

O que se transfere, portanto, é a pergunta investigativa: há regiões de tarefas em que configurações diferentes têm vantagens diferentes? Essa pergunta é compatível com o problema de seleção de algoritmos; não depende de a resposta ser positiva em todos os domínios.

### 3.2 A unidade de análise muda

[HIPÓTESE] Um domínio PDDL é uma descrição relativamente estável de ações, estados e objetivos. Uma tarefa de software é situada e aberta: começa com uma especificação possivelmente incompleta, exige localizar contexto em um repositório que evolui e pode produzir novas informações durante a execução. Por isso, “o domínio” da ponte não é apenas o repositório nem apenas a *issue*: é a combinação tarefa–repositório–configuração–momento. O SWE-Router é evidência de fronteira para esta última dimensão: em vez de decidir só pela descrição inicial, ele condiciona o escalonamento à trajetória parcial de uma execução barata [@son2026swerouter].

Essa distinção explica por que não basta adaptar as métricas de 2010. O contexto pode ser descoberto durante a execução. O SWE-bench já demonstra que mais contexto recuperado não equivale automaticamente a melhor resultado: no estudo original, aumentar a janela de contexto reduziu o desempenho do Claude 2, embora aumentasse o *recall* dos arquivos corretos [@jimenez2024swebench]. A característica relevante pode ser a qualidade do contexto selecionado, não seu volume bruto.

### 3.3 A “técnica” deixa de ser objeto fixo

Em planejamento clássico, um planejador é uma implementação relativamente identificável. No desenvolvimento de software com IA, “usar GPT” ou “usar Claude” não identifica uma técnica suficiente para comparação. Uma configuração pode variar em:

- modelo e versão;
- instruções de sistema e *prompt*;
- ferramentas, permissões e ambiente de execução;
- política de planejamento antes de editar ou de execução direta;
- uso de subagentes, revisão humana ou verificador externo;
- orçamento de *tokens*, tempo e custo;
- critério de parar, escalar ou devolver a tarefa.

[HIPÓTESE] A variável comparável ao planejador é a configuração inteira, não o modelo isolado. Essa é uma consequência analítica da natureza composta dos agentes; é também coerente com AS-LLM, que encontra ganho ao representar o algoritmo além de representar o problema [@wu2024large]. SALLMA oferece uma arquitetura para distinguir orquestração da execução e manter configurações em um catálogo; sua prova de conceito não demonstra que essa separação melhora seleção em desenvolvimento de software [@becattini2025sallma].

### 3.4 O resultado não cabe em uma única coluna

O paralelo mais útil com a crítica à dissertação original está na medida de resultado. A cobertura foi uma medida insuficiente para a Fase 3 porque ignorava tempo e qualidade do plano. A taxa de tarefa resolvida também é insuficiente em software: o SWE-bench reconhece que passar testes não garante que o código gerado seja abrangente, eficiente ou legível [@jimenez2024swebench]. Em estudo com usuários, participantes com assistente de IA escreveram código menos seguro e, ao mesmo tempo, tenderam a acreditar que seu código era mais seguro [@perry2023do].

[HIPÓTESE] Qualquer futura seleção de agentes precisa ser multiobjetivo. Uma configuração pode ser preferível em correção e inferior em segurança; mais barata e mais lenta; rápida, mas exigir retrabalho humano. “Melhor” só ganha significado depois de fixar o objetivo e as restrições.

## 4. O que os resultados negativos da revisão ensinam à aplicação

Esta é a ponte mais importante do capítulo. O trabalho revisado não deve aparecer como um antepassado que antecipou uma solução hoje confirmada. Deve aparecer como um caso que preserva a pergunta e corrige o modo de respondê-la.

### 4.1 Da hipótese promissora ao limite empírico

[FATO] A Fase 3 não encontrou ganho preditivo, por domínio, das métricas UML nem das *features* SAS+ sobre uma linha de base de melhor planejador único. A Fase 4 mostrou que LLMs também não superaram essa linha de base como seletores de planejadores. A rodada final da Fase 4B converge: nas IPCs de 2011 e 2018, as 16 *features* SAS+ quase não antecipam, fora do domínio, a família que resolve uma instância (AUC mediana 0,59, contra 0,58 só com tamanho); com todos os planejadores, nenhum seletor por instância supera o melhor planejador único. O ganho local sem portfólios na *agile* de 2018 não resiste à correção sobre todas as comparações.

[HIPÓTESE] A lição para software não é que “*features* não servem”. É que *features* estáticas, agregação por domínio e uma descrição pobre da técnica são uma aposta frágil. Uma aplicação responsável começaria testando se existe sinal preditivo incremental além de bases simples — tipo da tarefa, tamanho, contexto disponível e histórico de desempenho — antes de investir em métricas sofisticadas de código.

### 4.2 A aplicação mais concreta é uma salvaguarda metodológica

A aplicabilidade ao mundo real pode ser expressa em quatro perguntas operacionais, anteriores a qualquer roteador:

1. **A heterogeneidade existe?** Configurações diferentes vencem em conjuntos de tarefas diferentes, ou uma configuração fixa já domina?
2. **Qual sinal é informativo?** Características estáticas de código acrescentam algo a tipo de tarefa, qualidade da especificação e evidência de desempenho anterior?
3. **Qual é o custo do erro de seleção?** Escolher uma configuração barata demais pode falhar; escolher uma cara demais pode desperdiçar orçamento e atenção humana.
4. **O ganho generaliza?** A política funciona em repositórios, equipes ou períodos não observados no treino?

[HIPÓTESE] Essas perguntas são aplicáveis imediatamente como critério de avaliação de qualquer proposta de automação com agentes, mesmo sem criar um novo produto. Elas convertem a “adoção de IA” de decisão baseada em reputação de modelo para hipótese mensurável.

## 5. Três níveis de aplicabilidade no trabalho de engenharia de software

### Nível A — caracterizar antes de automatizar

[HIPÓTESE] Uma equipe pode registrar, sem selecionar automaticamente nada, uma ficha mínima da tarefa: tipo de mudança, clareza do pedido, extensão estimada da alteração, número de módulos envolvidos, disponibilidade de testes, maturidade do trecho e configuração usada pelo agente. O objetivo inicial não é prever; é tornar visível a distribuição de tarefas e resultados que hoje costuma ficar escondida em relatos anedóticos.

Esse nível é o mais defensável porque transforma a contribuição da dissertação em observabilidade. A própria literatura de software mostra que a distribuição importa: *issues* de benchmark e de produção não têm a mesma qualidade de contexto [@takerngsaksiri2025humanintheloop], e desempenho varia entre repositórios e contextos [@jimenez2024swebench].

### Nível B — configurar e escalar por evidência

[HIPÓTESE] Se dados locais mostrarem heterogeneidade reproduzível, uma política simples pode ser comparada a uma configuração fixa: por exemplo, uma tarefa bem especificada e localizada pode começar com um fluxo curto de localização–reparo–validação; uma tarefa ambígua ou distribuída pode exigir planejamento, inspeção adicional, verificador ou revisão humana antes de editar. O Agentless torna plausível que um fluxo mais simples seja competitivo em certo recorte, mas não demonstra a regra de roteamento proposta [@xia2025demystifying].

O mecanismo pode ser seleção inicial, cascata ou escalonamento. RouteLLM e FrugalGPT mostram que cascatas e roteadores dependem de dados de desempenho da distribuição em que operarão [@ong2024routellm; @chen2023frugalgpt]. Portanto, políticas universais importadas de *benchmarks* não são o alvo; políticas falsificáveis e locais são.

### Nível C — integrar a dimensão sociotécnica

[FATO] O *Task-Technology Fit* sustenta, com escopo próprio, que uma tecnologia precisa ser utilizada e se ajustar à tarefa para afetar desempenho individual; ele não é uma teoria de seleção automática prévia entre tecnologias [@goodhue1995task]. A teoria da contingência, por sua vez, encontrou em seis organizações químicas associação entre desempenho e adequação dos subsistemas às exigências dos subambientes, mas também que diferenciação e integração são antagônicas [@lawrence1967differentiation].

[HIPÓTESE] Para agentes de software, isso impede reduzir a aplicação a um classificador técnico. A configuração pode depender de supervisão, regras de revisão, confiança, responsabilidade sobre o *merge* e capacidade de a equipe absorver o resultado. Um agente bem roteado, mas inserido sem integração com os controles humanos, pode criar outro tipo de desajuste. Essa é uma hipótese organizacional, não resultado dos experimentos de planejamento.

## 6. Formulação conceitual proposta para o capítulo

Para uma tarefa situada `t`, seja:

- `φ(t)`: características da tarefa e do contexto do repositório antes da execução;
- `a`: uma configuração de agente disponível;
- `ψ(a)`: representação da configuração (modelo, ferramentas, estratégia, verificador, custo e limites);
- `τ`: sinais da trajetória parcial, se a política permitir exploração antes de decidir;
- `y`: vetor de resultados, incluindo correção, qualidade, segurança, tempo, custo e necessidade de retrabalho humano.

[HIPÓTESE] O problema de aplicação é escolher uma política `π(φ(t), ψ(a), τ) → a` que seja preferível a uma configuração fixa, sob um objetivo e restrições explicitados. A política pode concluir que não deve delegar a tarefa a um agente, ou que deve encaminhá-la a revisão humana: “nenhum agente” é uma configuração válida do espaço de decisão.

Essa formulação oferece cinco correções a 2010:

| Limite revelado na revisão | Correção proposta na Ponte |
|---|---|
| Domínio como unidade agregada | Tarefa situada como unidade; generalização por repositório/família de tarefa deixada fora |
| Métricas UML manuais e estáticas | *Features* candidatas testadas por ablação contra sinais simples e históricos |
| Técnica como rótulo taxonômico | Configuração de agente caracterizada em suas partes relevantes |
| Cobertura como eficiência | Vetor multiobjetivo, com segurança e retrabalho separados de correção |
| Ranking fixo por médias | Política comparada contra configuração fixa forte, oráculo e custos do próprio roteamento |

Não se deve chamar essa formulação de novo campo ou método novo. **Classificação de novidade: SÍNTESE_NOVA, não CONCEITO_NOVO.** Seleção de algoritmos, roteamento de LLMs, ajuste tarefa-tecnologia e avaliação de agentes já existem; a contribuição desta dissertação seria conectá-los criticamente a partir do caso de planejamento e de seus limites empíricos.

## 7. Auditoria conceitual: objeções que o capítulo deve antecipar

| Tese sob pressão | Explicação concorrente forte | Estado | Implicação editorial |
|---|---|---|---|
| “A tarefa explica o desempenho do agente.” | A diferença observada pode ser efeito de versão do modelo, *prompt*, recuperação de contexto, conjunto de testes ou distribuição de *issues*, não da tarefa em si. | MÚLTIPLAS_PLAUSÍVEIS | Falar em associação e heterogeneidade; não atribuir causalidade à *feature* sem desenho apropriado. |
| “Métricas de código permitirão roteamento.” | Sinais simples, como tipo da tarefa, tamanho e qualidade da descrição, podem explicar todo o ganho; métricas estruturais podem não acrescentar nada. | PRIMÁRIA_QUALIFICADA | H3 deve exigir ablação e ganho incremental fora da amostra. |
| “Um roteador é melhor que uma configuração fixa.” | A sobrecarga de coleta, classificação e erro de roteamento pode superar o ganho, sobretudo se há um agente forte que já resolve quase tudo. | PRIMÁRIA_QUALIFICADA | Comparar sempre com *single best*, custo total e oráculo; não assumir valor de complexidade. |
| “Passar testes indica aplicação bem-sucedida.” | Código pode passar testes e ainda ser inseguro, pouco legível ou caro de manter. | PRIMÁRIA_ENFRAQUECIDA | Manter qualidade, segurança e retrabalho como resultados separados [@jimenez2024swebench; @perry2023do]. |
| “O ajuste é puramente técnico.” | Adoção, confiança, revisão e divisão de responsabilidade alteram o resultado e não são capturados por *features* de código. | PRIMÁRIA_QUALIFICADA | Incluir o contexto sociotécnico como limite e variável futura, não como ruído. |

Há ainda um risco de circularidade: se uma política aprende que determinada configuração vence em certo histórico de tarefas, ela pode reproduzir preferências prévias e reduzir a exploração de alternativas. [HIPÓTESE] Um estudo futuro deveria reservar tarefas para comparação e registrar quando a política não escolhe uma configuração potencialmente melhor; sem isso, melhora aparente pode ser só consequência de ter parado de medir alternativas.

## 8. Hipóteses de pesquisa para a conclusão do capítulo

| ID | Hipótese | Predição observável | Refutação prática |
|---|---|---|---|
| H1 | Configurações diferentes têm desempenho relativo diferente entre tipos de tarefa. | Matriz tarefa × configuração apresenta vitórias distribuídas, acima do erro e da variação entre execuções. | Uma configuração fixa domina de forma estável em todas as regiões observadas. |
| H2 | Características da tarefa e do repositório permitem escolher melhor que a configuração fixa forte. | Política supera a linha de base em dados por repositório ou período mantidos fora. | Ganho desaparece fora da amostra ou não excede o custo de roteamento. |
| H3 | Métricas estruturais acrescentam valor sobre sinais simples. | Ablação preserva ganho quando entram métricas de código depois de tipo, tamanho, contexto e histórico. | Métricas não melhoram previsão ou pioram robustez. |
| H4 | Sinais coletados durante uma exploração limitada ajudam mais que decisão exclusivamente estática. | Escalonamento após trajetória parcial melhora objetivo total. | Exploração consome custo/tempo sem ganho ou introduz erro de seleção. |
| H5 | A política ótima depende da função objetivo e das restrições da equipe. | A mesma política muda quando segurança, custo ou prazo recebem pesos diferentes. | Uma política domina todos os objetivos relevantes sem compromisso mensurável. |

Essas hipóteses têm valor mesmo que todas sejam refutadas. Uma refutação de H2 ou H3 evitaria investimento em um roteador baseado em métricas que não carregam sinal. Uma refutação de H1 indicaria que uma configuração simples e bem governada é preferível a uma arquitetura de seleção.

## 9. Arquitetura proposta para o capítulo da dissertação

### 7.1 Por que esta ponte é necessária

Retomar a pergunta de 2010 e situá-la como caso de seleção de algoritmos. Enunciar a cautela: a dissertação não demonstrou o método de seleção que propunha; a ponte começa com esse resultado, não apesar dele.

### 7.2 O que o desenvolvimento de software com IA já mostra

Apresentar evidência de heterogeneidade por *bug*, descrição e repositório [@rondon2025evaluating; @takerngsaksiri2025humanintheloop; @jimenez2024swebench]. Mostrar que estratégias simples podem vencer arquiteturas agênticas mais complexas em recortes específicos [@xia2025demystifying].

### 7.3 Da escolha de planejador à escolha de configuração

Explicar a mudança de unidade, de técnica e de resultado. Introduzir `φ(t)`, `ψ(a)`, `τ` e `y` como mapa conceitual, sempre marcados como formulação proposta. Usar seleção de algoritmos e AS-LLM para justificar por que tarefa e configuração devem ser representadas [@smithmiles2009cross; @wu2024large].

### 7.4 O que os resultados negativos ensinam

Apresentar as conclusões das Fases 3, 4 e 4B: há heterogeneidade por domínio e trilha, mas as *features* disponíveis não a antecipam robustamente fora da amostra, e o seletor por instância não supera o melhor planejador único no recorte completo. Defender que o valor da dissertação revisada é oferecer condições de teste e salvaguardas, não repetir a promessa de um seletor por métrica estrutural.

### 7.5 Aplicações possíveis e condições de validação

Descrever os três níveis de aplicabilidade: observabilidade, configuração/escalonamento e integração sociotécnica. Explicitar H1–H5, critérios de refutação e medidas multiobjetivo. Situar roteamento e cascatas como precedentes, não como demonstração para engenharia de software [@ong2024routellm; @chen2023frugalgpt].

### 7.6 Limites e próximo passo

Fechar dizendo que a aplicação é uma agenda empírica. Não houve piloto, não há recomendação de produto e não se deve generalizar *benchmarks* para uma organização sem evidência local. Uma futura investigação deve comparar política fixa, roteamento simples e política aprendida fora da amostra.

## 10. Alegações permitidas e alegações proibidas

| Pode entrar no capítulo | Não deve entrar no capítulo |
|---|---|
| “Estudos de agentes de código mostram variação de desempenho por tarefa e contexto.” | “Já sabemos quais características de código escolhem o melhor agente.” |
| “A seleção condicional de modelos é uma linha operacional em LLMs.” | “Um roteador de agentes melhorará a produtividade de qualquer equipe.” |
| “Os resultados desta dissertação tornam inadequada uma transposição direta das métricas UML.” | “Os resultados negativos em planejamento provam que roteamento em software não funcionará.” |
| “A contribuição proposta é uma agenda de avaliação para escolha de configurações.” | “A dissertação oferece um produto ou método validado para seleção de agentes.” |
| “Correção, qualidade, segurança, custo e tempo podem divergir.” | “Passar testes ou concluir uma tarefa basta para caracterizar valor.” |

## 11. Insumos para a redação

**Frase de abertura possível:** a pergunta de 2010 parece pertencer a um período em que escolher entre planejadores era o problema. Hoje, quando um agente de IA pode planejar, editar, testar, pedir contexto e escalar para outro modelo, a escolha deixou de ser entre programas estáveis e passou a ser entre configurações sociotécnicas.

**Frase-pivô:** o ponto não é transportar a resposta de 2010 para o software; é transportar a pergunta, levando junto as razões pelas quais a resposta original não bastou.

**Fecho possível:** a aplicabilidade da dissertação não está em transformar métricas de código numa roleta de modelos. Está em insistir que a adoção de agentes deve ser tratada como hipótese: uma relação entre tarefa, configuração e resultado que precisa ser medida antes de ser automatizada.

Essas frases são material de trabalho, não texto final. A integração disponível da 4B já foi incorporada; a redação do capítulo ainda deve passar pela revisão de estilo e de referências da Fase 6.

## 12. Ampliação dirigida de evidência em engenharia de software com IA

Uma busca complementar identificou fontes que tornam a formulação mais concreta sem mudar seu estatuto. A principal evolução é separar a decisão em **triagem pré-agente**, **escalonamento após exploração parcial** e **orquestração**. [HIPÓTESE] Essa decomposição é mais adequada do que um seletor estático porque acomoda tanto características iniciais da tarefa quanto sinais produzidos durante a execução — testes, trajetória, custo, incerteza e necessidade de revisão.

O memorando [curadoria-fontes-se-ia.md](curadoria-fontes-se-ia.md) registra a matriz de evidências e os limites de cada nova fonte. O autor aprovou SALLMA como apoio arquitetural e SWE-Router como evidência complementar de fronteira. A inclusão recomendada é uma subseção sobre **política de escalonamento**, não uma alegação de seletor pronto: SALLMA não testa roteamento de tarefas de programação e SWE-Router ainda é preprint baseado em *benchmarks*.

## Referências usadas

- @chen2023frugalgpt
- @goodhue1995task
- @jimenez2024swebench
- @lawrence1967differentiation
- @ong2024routellm
- @perry2023do
- @rondon2025evaluating
- @smithmiles2009cross
- @smithmiles2023instance
- @takerngsaksiri2025humanintheloop
- @wu2024large
- @xia2025demystifying
