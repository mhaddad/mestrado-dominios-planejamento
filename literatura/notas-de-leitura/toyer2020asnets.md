---
tipo: nota-de-leitura
eixo: E4
citekey: toyer2020asnets
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/download/11633/26580
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A5, A6]
fragilidades: [F4]
perguntas: [Q2]
---

# ASNets: Deep Learning for Generalised Planning

**Toyer, S.; Thiébaux, S.; Trevizan, F.; Xie, L. · 2020 · Journal of Artificial Intelligence Research 68**
**Link/DOI:** 10.1613/jair.1.11633

## Extração estruturada

- **Problema:** aprender políticas generalizadas — aplicáveis a qualquer instância de um domínio PPDDL/PDDL, não apenas à instância em que foram treinadas — usando redes neurais, superando o uso limitado de aprendizado em autosseletores/autoconfiguradores de portfólio.
- **Método:** Action Schema Networks (ASNets), uma arquitetura que constrói um grafo bipartido de módulos de ação e módulos de proposição, conectados segundo a "relação" entre ações e proposições definida pelos esquemas de ação (*action schemas*) do PDDL/PPDDL. Os pesos são compartilhados entre todas as instâncias do mesmo domínio (análogo a uma convolução sobre a estrutura relacional do problema, em vez de sobre uma grade de pixels). O treino imita um planejador "professor" (LRTDP ou A* com heurística h-add ou LM-cut) em instâncias pequenas.
- **Dados/benchmarks:** sete domínios probabilísticos e determinísticos (incluindo Blocksworld, Triangle Tireworld, CosaNostra Pizza), com avaliação estendida em 18.300 instâncias de Blocksworld (18–50 blocos) após treino em 50 instâncias pequenas (8–10 blocos).
- **Resultado principal:** ASNets treinadas em instâncias pequenas resolvem instâncias muito maiores mais rápido que planejadores de busca heurística aplicados diretamente às instâncias grandes, porque aprendem um "truque" específico do domínio generalizável. Em Blocksworld, a política aprendida resolveu corretamente as 18.300 instâncias de teste.
- **Relação com a dissertação de 2010:** a obra **corrige/amplia A6** ao introduzir uma família de técnica — política aprendida por rede neural sobre a estrutura relacional do domínio — que não existe na taxonomia de 2010 (heuristic search, hierarchical, knowledge-based, forward-chaining, plan-space, total-order); a taxonomia de 2010 fica incompleta perante o estado da arte pós-2010, reforçando **F4**. Quanto a **A1** e **A5** (existe relação entre características do domínio e a técnica que funciona melhor, e essa relação vem de complexidade estrutural), o artigo **confirma o espírito geral**, mas por caminho distinto: aqui a "estrutura" não é extraída de diagramas UML, e sim diretamente da estrutura relacional do PDDL (esquemas de ação e predicados) — uma resposta concreta e testável a **Q2**, mostrando que existe pelo menos uma representação estrutural do domínio (grafo ação–proposição) que sustenta generalização de políticas entre instâncias do mesmo domínio.

## Pontos relevantes para o projeto

- Representa a tarefa/domínio por um **grafo relacional derivado do PDDL** (ações e proposições ligadas pela relação de "posição" nos esquemas de ação), não por UML nem por lógica de descrição — uma terceira via de representação estrutural relevante para Q2.
- O compartilhamento de pesos entre todas as instâncias de um domínio é o mecanismo técnico que permite a generalização — algo que a discretização Alto/Médio/Baixo de métricas UML de 2010 não modela.
- Limitações reconhecidas pelos próprios autores (campo receptivo fixo, incapacidade de lidar com pré-condições quantificadas e fórmulas de meta arbitrárias, custo computacional em problemas com muitas ações/proposições) mostram que a expressividade da representação do domínio ainda é um fator limitante — eco direto de F3/F4.
- Não há qualquer menção a métricas de diagramas UML (casos de uso, classes, estados) como as de 2010; a "característica do domínio" relevante aqui é puramente sintático-relacional (PDDL).

## Marcações

- `[FATO]` ASNets compartilham pesos entre todas as instâncias de um domínio por meio da relação ação–proposição definida pelos esquemas de ação PDDL (Seção 3, p. 6–8).
- `[FATO]` A política aprendida em Blocksworld generalizou de 50 instâncias de treino (8–10 blocos) para 18.300 instâncias de teste (18–50 blocos), todas resolvidas corretamente (Seção 8, p. 44–45).
- `[HIPÓTESE]` A convergência entre este trabalho (representação ação–proposição), a lógica de descrição de Ståhlberg et al. (2022) e a UML de 2010 sugere que "característica estrutural do domínio" é um conceito amplo com múltiplas operacionalizações possíveis, e que a escolha da representação (não apenas sua presença) é o que determina o poder preditivo sobre a técnica — hipótese central para Q2.

## Trechos literais

> "ASNets are able to learn a generalised reactive policy that can quickly solve much larger instances from the domain." (Resumo)

> "This connectivity scheme enables modules to share weights in such a way that the size and shape of learnt weights is the same for all ASNets from a given domain." (Seção 3, p. 7)

> "Our policy correctly solved 18,300 test instances with 18–50 blocks after training on just 50 smaller instances with 8–10 blocks." (Seção 8, p. 44–45)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/download/11633/26580. Conferência humana: pendente.
