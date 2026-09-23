---
tipo: nota-de-leitura
eixo: E4
citekey: stahlberg2022learninga
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/download/19851/19610
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A5]
fragilidades: [F3, F4]
perguntas: [Q2]
---

# Learning General Optimal Policies with Graph Neural Networks: Expressive Power, Transparency, and Limits

**Ståhlberg, S.; Bonet, B.; Geffner, H. · 2022 · Proceedings of ICAPS 2022**
**Link/DOI:** 10.1609/icaps.v32i1.19851

## Extração estruturada

- **Problema:** entender o poder e os limites de redes neurais em grafo (GNNs) para aprender políticas gerais ótimas em domínios de planejamento clássico tratáveis, ligando essa capacidade à correspondência formal entre a expressividade de GNNs e a de fragmentos de lógica de contagem de variáveis finitas (C_k).
- **Método:** treino supervisionado de uma GNN simples para aproximar a função de valor ótimo V*(s) a partir de estados amostrados; a arquitetura recebe a estrutura relacional do estado (predicados do domínio) e agrega mensagens entre objetos. Os autores comparam essa capacidade com o pool de *features* de lógica de descrição (DL) usado em trabalhos anteriores para expressar políticas gerais, apoiando-se na correspondência teórica entre DL e o fragmento lógico C2 e entre C2 e o poder expressivo de GNNs.
- **Dados/benchmarks:** 11 domínios clássicos (Blocks-clear, Blocks-on, Gripper, Logistics, Miconic, Parking, Rovers, Satellite, Transport, Visitall), com 306 problemas de teste.
- **Resultado principal:** GNNs com agregação MAX resolvem 98% dos 306 problemas de teste de forma ótima; a única exceção sistemática é Rovers, cujas políticas ótimas exigem *features* C3 (mais expressivas que C2), que GNNs padrão não conseguem computar — confirmado com o domínio simplificado "Vacuum", em que a generalização só ocorre na variante cuja função de valor é expressável em C2.
- **Relação com a dissertação de 2010:** oferece a **evidência mais formal e direta do lote para A1/A5** — mostra, com prova teórica e verificação empírica, que a complexidade estrutural do domínio (medida pelo grau de lógica de contagem de variáveis necessário para expressar a função de valor ótima) determina se uma técnica (aqui, GNN) generaliza corretamente. Isso **confirma o espírito de A5** (a complexidade do domínio afeta o desempenho da técnica), mas propõe uma métrica de complexidade muito mais rigorosa (Ck) do que a discretização Alto/Médio/Baixo de atributos UML de 2010, respondendo diretamente a **Q2**: sim, existe pelo menos uma métrica estrutural (o grau da lógica necessária) com poder preditivo comprovado sobre o desempenho de uma técnica — mas é derivada de predicados de domínio (PDDL), não de diagramas UML. Isso também ataca **F3** (a métrica não depende do modelador, é uma propriedade formal do domínio) e reforça **F4** (a "técnica" GNN não se encaixa na taxonomia de 2010).

## Pontos relevantes para o projeto

- Estabelece formalmente que **DL-features (lógica de descrição) e GNNs têm o mesmo teto de expressividade** (correspondência com C2); isso unifica duas das quatro representações de domínio observadas neste lote (lógica de descrição e grafo/GNN) como equivalentes em poder, o que é um achado central para Q2.
- Mostra um caso concreto (Rovers) em que a representação padrão de domínio **falha estruturalmente** — não é questão de mais dados ou treino, mas de expressividade insuficiente da representação, ilustrando por que "mais características" (T4 de 2010) não resolve automaticamente o problema se a classe de representação for limitada.
- Ainda assim, os autores conseguem decompor Rovers em uma variante mais simples (Vacuum) e mostrar que a causa exata da falha é uma propriedade estrutural (múltiplos mapas por robô) — o tipo de diagnóstico fino que a discretização de 2010 (Alto/Médio/Baixo) não permitiria fazer.
- As *features* aprendidas pela GNN foram comparadas (por regressão linear) com as *features* artesanais de DL e mostraram alta correspondência na maioria dos domínios — evidência de que a rede está de fato "redescobrindo" a mesma estrutura conceitual da lógica de descrição.

## Trechos literais

> "it is observed that general optimal policies are obtained in domains where general optimal value functions can be defined with C2 features but not in those requiring more expressive C3 features" (Resumo)

> "The neural network does not approximate well the optimal value function in Rovers, which is the only domain where the optimal policy does not generalize 100% with max aggregation. The problem is that optimal policies for Rovers require C3 features that cannot be computed with standard GNNs." (Seção "Understanding the Limitations", p. 634)

> "the realization that general policies and value functions for many classical benchmark domains can be expressed in terms of features defined from the domain predicates using a description logic (DL) grammar" (Introdução, p. 629)

## Marcações

- `[FATO]` GNN-MAX resolveu 300 de 306 problemas de teste de forma ótima; os 6 problemas não resolvidos ótimos são todos em Rovers (Tabela 2, p. 633).
- `[FATO]` A causa da falha em Rovers foi isolada experimentalmente ao domínio simplificado Vacuum, mostrando que múltiplos mapas por robô (exigindo C3) é o fator crítico (Seção "Understanding the Limitations", p. 634).
- `[HIPÓTESE]` Se a expressividade lógica necessária (Ck) for tomada como proxy formal para "complexidade do domínio", ela pode ser um substituto mais rigoroso — e comparável entre estudos — do que as métricas de diagramas UML de 2010, o que forneceria um caminho concreto para revisar A5 com maior precisão metodológica.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/ICAPS/article/download/19851/19610. Conferência humana: pendente.
