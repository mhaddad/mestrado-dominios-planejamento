---
titulo: "Introdução: a pergunta de 2010 e as perguntas de hoje"
status: revisado-por-ia
data: 2026-09-29
fonte: plano (seções 1, 5 e 7), relatórios das Fases 3 a 5, relatório de auditoria
---

# Introdução

Um planejador automático recebe a descrição de um domínio, um estado inicial e um objetivo, e devolve uma sequência de ações que leva de um ao outro [@weld1994introduction]. Desde que as Competições Internacionais de Planejamento passaram a comparar planejadores sobre os mesmos problemas, em 1998, um padrão se repete: planejadores que se destacam em alguns domínios falham em outros, e nenhum domina todos [@mcdermott2000planning; @nunez2015automatic]. Se o desempenho depende do domínio, faz sentido perguntar se é possível saber de antemão, olhando para o domínio, qual planejador escolher.

Essa foi a pergunta da dissertação de 2010 [@haddad2010relacao]. A resposta proposta foi medir o domínio por métricas contadas em modelos UML feitos no itSIMPLE, relacionar essas métricas às técnicas usadas pelos planejadores e, com essa relação, gerar um *ranking* de planejadores para um domínio novo. O trabalho concluiu que a relação existe, que algumas características e técnicas se destacam e que o *ranking* ajuda a escolher o planejador.

Dezesseis anos depois, a pergunta continua atual, mas o terreno mudou. A escolha automática de algoritmos a partir de características do problema tornou-se um campo próprio, com *portfólios* de planejadores, sistemas que escolhem por instância e infraestrutura de avaliação compartilhada [@kerschke2019automated; @helmert2011fast; @cenamor2016ibacop; @bischl2016aslib]. As características que predizem desempenho passaram a ser extraídas automaticamente do PDDL e da representação de estados, e não contadas à mão [@fawcett2014improved; @helmert2009concise]. O aprendizado de máquina passou a produzir heurísticas [@ferber2022neural; @toyer2020asnets]. E modelos de linguagem de grande escala entraram no planejamento, com resultados que variam muito conforme o domínio: em *benchmarks* clássicos, os melhores modelos acertam uma fração dos planos e caem para perto de zero quando só os nomes dos objetos mudam [@valmeekam2023planbench; @kambhampati2024llms].

Esta revisão parte da dissertação de 2010 e a reexamina com esses instrumentos. Ela não se limita a corrigir o trabalho original: a liberdade de ampliar o escopo foi uma decisão explícita, e parte do que se propõe aqui não existia em 2010.

## A auditoria da versão original

O primeiro passo foi auditar o que a dissertação afirmava. Das 349 afirmações substantivas extraídas do texto, 265 se mantêm, 80 precisam ser reformuladas e 4 são descartadas (capítulo 3). O que se sustenta é sobretudo o que o trabalho descreve e a formulação do problema, que relaciona características, alternativas e desempenho no campo de seleção de algoritmos [@rice1976algorithm]. Isso não presume que as características escolhidas em 2010 consigam prever o vencedor. O que precisa mudar está nas conclusões: a taxonomia de técnicas usada para relacionar planejadores e características não resiste às fontes primárias dos próprios planejadores; e a validação do *ranking* não se distingue de uma linha de base que ignora as características do domínio. A auditoria também mostrou que a pergunta de 2010 tinha uma origem não registrada no texto: o artigo que apresentou o itSIMPLE já a declarava como objetivo [@vaquero2005itsimple].

## Perguntas de pesquisa

A revisão se organiza em cinco perguntas.

- **Q1 — Replicação.** As conclusões de 2010 se sustentam com mais planejadores, mais domínios e método estatístico adequado?
- **Q2 — Continuidade.** Métricas estruturais de modelagem, no estilo orientado a objetos, acrescentam poder preditivo às *features* modernas extraídas de PDDL? Nenhum trabalho revisado fez essa comparação. A ordem sintática do PDDL é uma fonte conhecida de variação no desempenho [@vallati2021importance], mas seu controle não foi executado nesta revisão e permanece como limitação do desenho.
- **Q3 — Atualização.** Onde os modelos de linguagem entram nesse mapa: como técnica de planejamento, como tradutores de domínio para PDDL ou como seletores de planejador [@guan2023leveraging; @liu2023llmp; @pallagani2024prospects]?
- **Q4 — Exploração.** Que conexões, oportunidades e hipóteses de pesquisa ligam o ajuste entre características da tarefa e estratégia de solução ao desenvolvimento de software apoiado por IA? A questão tem apoio indireto: em correção automática de defeitos, uma abordagem simples de três fases superou agentes mais complexos em desempenho e custo [@xia2025demystifying]. A ponte com a teoria da contingência nas organizações [@lawrence1967differentiation] é empregada como analogia para organizar hipóteses, não como evidência de eficácia em software.
- **Q5 — Ampliação.** Nos resultados publicados das IPCs posteriores a 2010, quais características estruturais extraídas automaticamente do PDDL explicam o desempenho relativo das famílias de técnicas de planejamento? A pergunta amplia a amostra e desloca a análise para resultados por instância das IPCs de 2011 e 2018.

As duas primeiras perguntas são o núcleo da revisão e ficam no território do trabalho original. Q3 atualiza o mapa das técnicas; Q4 é uma expansão exploratória; Q5 amplia a avaliação empírica com dados posteriores a 2010.

## Objetivos

O objetivo geral é reexaminar a relação entre características de domínios e técnicas de planejamento proposta em 2010, com os dados, os métodos e as técnicas disponíveis em 2026. Os objetivos específicos são:

1. auditar as afirmações da dissertação de 2010 e documentar o que se mantém, o que se reformula e o que se descarta (capítulo 3);
2. propor uma taxonomia de técnicas de planejamento fundamentada nas fontes primárias, em quatro dimensões: busca, heurística, representação e arquitetura (capítulo 3);
3. reproduzir o método de 2010 por script e medir o efeito de cada correção (capítulos 4 e 5);
4. comparar métricas de modelagem UML com *features* extraídas de PDDL como preditoras de desempenho (capítulo 5);
5. posicionar os modelos de linguagem no mapa das técnicas (capítulo 6);
6. investigar conexões entre a seleção de planejadores e a escolha de configurações de agentes de software, formulando hipóteses e critérios para estudos futuros (capítulo 7);
7. examinar, nas IPCs de 2011 e 2018, se *features* SAS+ e propriedades de topologia explicam o desempenho relativo de famílias de técnicas por instância (capítulo 5).

## Contribuições

Esta revisão entrega uma auditoria rastreável das afirmações e dos dados de 2010; uma taxonomia de técnicas em quatro dimensões, construída a partir de fontes primárias; uma replicação em camadas que separa reprodução, correção, reexecução e ampliação; e uma avaliação com 41 domínios do Planner Museum e resultados por instância das IPCs de 2011 e 2018. <!-- fonte: auditoria/relatorio-auditoria.md; EXP-03 a EXP-25 --> A contribuição aplicada é uma ponte exploratória que formula a escolha de configuração de agentes de software como seleção condicional mensurável, sem alegar que uma política local já foi validada. O capítulo 8 retoma o alcance e os limites de cada contribuição.

## Estrutura do texto

O capítulo 2 revisa os fundamentos e o estado da arte de 2008 a 2026: seleção de algoritmos, caracterização de tarefas de planejamento, planejadores e competições, aprendizado, modelos de linguagem, engenharia do conhecimento e o ajuste entre tarefa e técnica fora do planejamento. O capítulo 3 apresenta a auditoria da dissertação de 2010 e a nova taxonomia. O capítulo 4 descreve o método da replicação e da ampliação experimental. O capítulo 5 apresenta os resultados e responde às perguntas Q1, Q2 e Q5. O capítulo 6 trata dos modelos de linguagem (Q3), e o capítulo 7, da ponte exploratória com o desenvolvimento de software (Q4). O capítulo 8 conclui.

## Uso de inteligência artificial

O uso de inteligência artificial na revisão, na extração de dados, na pesquisa, na experimentação e na redação desta versão é declarado nos elementos pré-textuais. A declaração só se torna definitiva após a revisão e a aprovação do autor.
