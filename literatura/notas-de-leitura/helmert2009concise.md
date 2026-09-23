---
tipo: nota-de-leitura
eixo: E2
citekey: helmert2009concise
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ai.dmi.unibas.ch/papers/helmert-aij2009.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5]
fragilidades: [F3]
perguntas: [Q2]
---

# Concise Finite-Domain Representations for PDDL Planning Tasks

**Helmert, M. · 2009 · Artificial Intelligence 173(5-6), 503–535**
**Link/DOI:** https://doi.org/10.1016/j.artint.2008.10.013

## Extração estruturada

- **Problema:** tarefas de planejamento PDDL são normalmente compiladas em representações proposicionais (STRIPS), que tratam cada proposição como independente e não capturam a estrutura de que, por exemplo, "a peça p1 está em A" e "a peça p1 está em B" são valores mutuamente exclusivos de uma mesma variável. O artigo propõe traduzir PDDL para uma representação de variáveis de domínio finito (FDR, também chamada SAS+), mais concisa e estruturada.
- **Método:** algoritmo de tradução em quatro estágios: (1) normalização da tarefa PDDL para um fragmento restrito; (2) síntese de invariantes que identificam grupos de proposições mutuamente exclusivas, representáveis por uma única variável de domínio finito; (3) análise de alcançabilidade relaxada via programação lógica (Datalog) para gerar a instanciação (*grounding*); (4) combinação dos resultados anteriores para gerar a representação final. A partir da FDR, define formalmente o **grafo de transição de domínio** (*domain transition graph*, DTG — um grafo por variável, com arcos entre valores que uma ação pode alterar) e o **grafo causal** (um grafo entre variáveis, com arco quando uma variável depende de outra via pré-condição/efeito).
- **Dados/benchmarks:** todas as tarefas proposicionais das IPCs 1–5, usadas para medir desempenho e qualidade da tradução.
- **Resultado principal:** o algoritmo traduz a grande maioria das instâncias em menos de 10 segundos (93,4%); a representação FDR gerada é, na maioria dos domínios testados, muito próxima ou idêntica a uma representação projetada manualmente; heurísticas baseadas em decomposição do grafo causal degradam-se substancialmente sem essa tradução concisa.
- **Relação com a dissertação de 2010:**
  - **A5 (corrige/refina):** 2010 afirma que diagramas UML medem a complexidade do domínio, e essa complexidade afeta o desempenho das técnicas. Esta obra define, com precisão formal, a noção de estrutura de domínio que a literatura de planejamento de fato usa para esse propósito — grafo causal e DTG, derivados automaticamente da tradução FDR do próprio PDDL — e mostra que essa estrutura tem efeito direto e demonstrável no desempenho de heurísticas: "without the concise FDR translation, the causal graph heuristic is not competitive with other approaches" (Seção 8.2, p. 54). É uma noção de "estrutura do domínio" tecnicamente mais precisa, automática e amplamente adotada do que as métricas de diagrama UML de 2010 (nº de classes, atributos, associações etc.), que dependem de modelagem manual.
  - **F3 (contrasta e corrige):** a métrica UML de 2010 "depende do modelador" (F3). O grafo causal e o DTG, por serem derivados algoritmicamente da tradução PDDL→FDR (síntese de invariantes + análise de alcançabilidade), são **reprodutíveis e determinísticos** — dado o mesmo PDDL, sempre produzem a mesma estrutura, eliminando a subjetividade de modelagem que caracteriza a UML.
- **Features por classe (para Q2):** estruturais de grafo causal/DTG — esta é a obra de referência formal que define essas duas estruturas, usadas depois como *features* por Cenamor et al. (2012/2013), Fawcett et al. (2014) e De la Rosa et al. (2017), todas lidas neste mesmo lote.

## Pontos relevantes para o projeto

- Fonte primária e formal da definição de grafo causal e DTG — indispensável para qualquer nota ou capítulo que discuta *features* estruturais em Q2, já que todas as obras de predição de desempenho do eixo E2 (Fawcett et al., De la Rosa et al.) constroem suas *features* de grafo a partir exatamente destas estruturas.
- Mostra, com evidência empírica direta (Seção 8.2), que a representação estrutural do domínio (FDR/grafo causal) tem efeito causal comprovado sobre o desempenho de heurísticas — o tipo de evidência que falta, segundo F3/F5, à métrica UML de 2010.
- A Figura 4 vs. Figura 5 do artigo (grafo causal do exemplo em STRIPS vs. em FDR) ilustra visualmente por que a escolha de representação, não só o domínio "em si", determina a complexidade estrutural aparente — ponto relevante para qualquer discussão sobre robustez de métricas de domínio.

## Marcações

- `[FATO]` O algoritmo de tradução PDDL→FDR processa 93,4% das instâncias de IPC 1–5 em menos de 10 segundos, e a representação gerada é próxima ou idêntica a uma representação manual na maioria dos domínios (Seção 8.1–8.2).
- `[FATO]` Heurísticas de planejamento baseadas em decomposição do grafo causal (como a do Fast Downward) degradam-se em ordens de grandeza de desempenho se a tradução FDR concisa não for usada (Seção 8.2, p. 54).
- `[HIPÓTESE]` Se a dissertação de 2010 tivesse usado grafo causal/DTG (derivados automaticamente do PDDL) em vez de diagramas UML (modelados manualmente no itSIMPLE) como fonte de características estruturais, a fragilidade F3 (dependência do modelador) provavelmente teria sido evitada, ao custo de perder a interpretabilidade "conceitual" que a UML oferece a um leitor não especialista em representações internas de planejadores.

## Trechos literais

1. "We introduce an efficient method for translating planning tasks specified in the standard PDDL formalism into a concise grounded representation that uses finite-domain state variables instead of the straight-forward propositional encoding." (Resumo)
2. "Planning approaches based on problem decomposition, such as the causal graph heuristic [27] used in the Fast Downward planner [28], benefit from the simpler causal structure of the finite-domain representation." (Seção 1.2, p. 6–7)
3. "The same performance degradation can be observed in heuristic planning based on causal graph decompositions [28] – without the concise FDR translation, the causal graph heuristic is not competitive with other approaches." (Seção 8.2, p. 54)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ai.dmi.unibas.ch/papers/helmert-aij2009.pdf (baixado com `curl`, extraído com `pdftotext -layout`). Conferência humana: pendente.
