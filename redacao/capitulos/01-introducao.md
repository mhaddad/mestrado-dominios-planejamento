---
titulo: "Introdução: a pergunta de 2010 e as perguntas de hoje"
status: rascunho-de-ia
data: 2026-09-23
fonte: plano (seções 1, 5 e 7), capítulos 2 e 3, relatório de auditoria
---

# Introdução

> Rascunho gerado por IA. As seções que dependem dos resultados das Fases 3 a 5 (contribuições confirmadas, síntese dos resultados) estão marcadas como pendentes. As citações usam só chaves do `literatura/referencias/referencias.bib`. É material de trabalho: o texto final é do autor.

Um planejador automático recebe a descrição de um domínio, um estado inicial e um objetivo, e devolve uma sequência de ações que leva de um ao outro [@weld1994introduction]. Desde que as Competições Internacionais de Planejamento passaram a comparar planejadores sobre os mesmos problemas, em 1998, um padrão se repete: planejadores que se destacam em alguns domínios falham em outros, e nenhum domina todos [@mcdermott2000planning; @nunez2015automatic]. Se o desempenho depende do domínio, faz sentido perguntar se é possível saber de antemão, olhando para o domínio, qual planejador escolher.

Essa foi a pergunta da dissertação de 2010 [@haddad2010relacao]. A resposta proposta foi medir o domínio por métricas contadas em modelos UML feitos no itSIMPLE, relacionar essas métricas às técnicas usadas pelos planejadores e, com essa relação, gerar um *ranking* de planejadores para um domínio novo. O trabalho concluiu que a relação existe, que algumas características e técnicas se destacam e que o *ranking* ajuda a escolher o planejador.

Dezesseis anos depois, a pergunta continua atual, mas o terreno mudou. A escolha automática de algoritmos a partir de características do problema tornou-se um campo próprio, com *portfólios* de planejadores, sistemas que escolhem por instância e infraestrutura de avaliação compartilhada [@kerschke2019automated; @helmert2011fast; @cenamor2016ibacop; @bischl2016aslib]. As características que predizem desempenho passaram a ser extraídas automaticamente do PDDL e da representação de estados, e não contadas à mão [@fawcett2014improved; @helmert2009concise]. O aprendizado de máquina passou a produzir heurísticas [@ferber2022neural; @toyer2020asnets]. E modelos de linguagem de grande escala entraram no planejamento, com resultados que variam muito conforme o domínio: em *benchmarks* clássicos, os melhores modelos acertam uma fração dos planos e caem para perto de zero quando só os nomes dos objetos mudam [@valmeekam2023planbench; @kambhampati2024llms].

Esta revisão parte da dissertação de 2010 e a reexamina com esses instrumentos. Ela não se limita a corrigir o trabalho original: a liberdade de ampliar o escopo foi uma decisão explícita, e parte do que se propõe aqui não existia em 2010.

## A auditoria da versão original

O primeiro passo foi auditar o que a dissertação afirmava. Das 349 afirmações substantivas extraídas do texto, 265 se mantêm, 80 precisam ser reformuladas e 4 são descartadas (capítulo 3). O que se sustenta é sobretudo o que o trabalho descreve e a sua premissa, que é o fundamento da seleção de algoritmos [@rice1976algorithm]. O que precisa mudar está nas conclusões: a taxonomia de técnicas usada para relacionar planejadores e características não resiste às fontes primárias dos próprios planejadores; e a validação do *ranking* não se distingue de uma linha de base que ignora as características do domínio. A auditoria também mostrou que a pergunta de 2010 tinha uma origem não registrada no texto: o artigo que apresentou o itSIMPLE já a declarava como objetivo [@vaquero2005itsimple].

## Perguntas de pesquisa

A revisão se organiza em quatro perguntas.

- **Q1 — Replicação.** As conclusões de 2010 se sustentam com mais planejadores, mais domínios e método estatístico adequado?
- **Q2 — Continuidade.** Métricas estruturais de modelagem, no estilo orientado a objetos, acrescentam poder preditivo às *features* modernas extraídas de PDDL? Nenhum trabalho revisado fez essa comparação, e ela precisa controlar um efeito conhecido: reordenar um modelo de domínio, sem mudar seu significado, altera o desempenho dos planejadores [@vallati2021importance].
- **Q3 — Atualização.** Onde os modelos de linguagem entram nesse mapa: como técnica de planejamento, como tradutores de domínio para PDDL ou como seletores de planejador [@guan2023leveraging; @liu2023llmp; @pallagani2024prospects]?
- **Q4 — Transferência.** O princípio de ajustar a estratégia de solução às características da tarefa ajuda a escolher configurações de agentes de IA no desenvolvimento de software? A questão tem apoio indireto: em correção automática de defeitos, uma abordagem simples de três fases superou agentes mais complexos em desempenho e custo [@xia2025demystifying]. `[HIPÓTESE]` A ponte com a teoria da contingência nas organizações [@lawrence1967differentiation] é analogia para organizar hipóteses, não evidência.

As duas primeiras perguntas são o núcleo da revisão e ficam no território do trabalho original. As duas últimas são expansões de escopo, com peso menor e registro explícito como tal.

## Objetivos

O objetivo geral é reexaminar a relação entre características de domínios e técnicas de planejamento proposta em 2010, com os dados, os métodos e as técnicas disponíveis em 2026. Os objetivos específicos são:

1. auditar as afirmações da dissertação de 2010 e documentar o que se mantém, o que se reformula e o que se descarta (capítulo 3);
2. propor uma taxonomia de técnicas de planejamento fundamentada nas fontes primárias, em quatro dimensões: busca, heurística, representação e arquitetura (capítulo 3);
3. reproduzir o método de 2010 por script e medir o efeito de cada correção (capítulos 4 e 5);
4. comparar métricas de modelagem UML com *features* extraídas de PDDL como preditoras de desempenho (capítulo 5);
5. posicionar os modelos de linguagem no mapa das técnicas (capítulo 6);
6. testar, como hipótese, se o princípio de ajuste informa a escolha de configurações de agentes em desenvolvimento de software (capítulo 7).

## Contribuições

> PENDENTE: esta seção depende dos resultados das Fases 3 a 5. Por ora, as contribuições já entregues são a auditoria documentada da dissertação de 2010, com dados e scripts reprodutíveis, e a taxonomia de técnicas em quatro dimensões.

## Estrutura do texto

O capítulo 2 revisa os fundamentos e o estado da arte de 2008 a 2026: seleção de algoritmos, caracterização de tarefas de planejamento, planejadores e competições, aprendizado, modelos de linguagem, engenharia do conhecimento e o ajuste entre tarefa e técnica fora do planejamento. O capítulo 3 apresenta a auditoria da dissertação de 2010 e a nova taxonomia. O capítulo 4 descreve o método da replicação e da ampliação experimental. O capítulo 5 apresenta os resultados e responde às perguntas Q1 e Q2. O capítulo 6 trata dos modelos de linguagem (Q3), e o capítulo 7, da ponte com o desenvolvimento de software (Q4). O capítulo 8 conclui.

## Uso de inteligência artificial

> PENDENTE: declaração do uso de IA conforme as regras da instituição (plano, Fase 6). O registro detalhado está no plano do projeto, seção 11.
