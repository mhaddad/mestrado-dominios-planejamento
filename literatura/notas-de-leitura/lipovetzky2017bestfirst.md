---
tipo: nota-de-leitura
eixo: E3
citekey: lipovetzky2017bestfirst
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/AAAI/article/view/11027/10886
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A2, A6]
fragilidades: [F4]
perguntas: [Q1]
---

# Best-First Width Search: Exploration and Exploitation in Classical Planning

**Lipovetzky, N.; Geffner, H. · 2017 · Proceedings of AAAI-17**
**Link/DOI:** https://doi.org/10.1609/aaai.v31i1.11027

## Extração estruturada

- **Problema:** a busca gulosa best-first (GBFS), usada como algoritmo de busca padrão em planejadores como FF, Fast Downward e LAMA, frequentemente encontra platôs heurísticos onde a busca "se perde" por falta de estados com valor heurístico melhor; como combinar exploração estrutural com busca dirigida a objetivo para superar esse problema.
- **Método:** os autores usam métodos de busca *width-based* (busca por largura/novidade) — derivados do algoritmo IW(k), uma busca em largura que poda estados cujos átomos (tuplas de até k fatos) já não são "novos" em relação a todos os estados gerados antes — e os combinam com busca heurística dirigida a objetivo em um esquema geral chamado *best-first width search* (BFWS), que ordena a fronteira de busca por medidas de novidade (w) e heurísticas (h) em conjunto.
- **Dados/benchmarks:** conjunto padrão de domínios de competições de planejamento (não detalhado em números nesta leitura da introdução/corpo principal, mas comparado a GBFS, GBFS-LS e a planejadores estado da arte).
- **Resultado principal:** a exploração baseada em largura (*width-based exploration*) em GBFS é mais eficaz que GBFS com busca local GBFS (GBFS-LS); a combinação BFWS supera ambas isoladamente e resulta em algoritmos de planejamento clássico competitivos com o estado da arte (Resumo).
- **Relação com a dissertação de 2010:**
  - **A6 (corrige/detalha):** a obra apresenta *width-based search* (busca por largura/novidade) como uma família de técnicas de exploração estrutural, distinta tanto da busca heurística pura quanto de qualquer categoria de 2010 (*Heuristic Search*, *Hierarchical*, *Knowledge-based*, *Forward-chaining*, *Plan-Space*, *Total-order*). O conceito central — "novidade" de um estado, medida por quantas tuplas de átomos de tamanho i ele é o primeiro a tornar verdadeiras — não corresponde a nenhuma das seis categorias de A2/A6. Isso mostra que a taxonomia de 2010, fixada em 2010, já ficou incompleta em 2017 com o surgimento de uma família de técnicas nova e influente.
  - **A2 (confirma parcialmente, mas desatualiza):** confirma que GBFS (busca heurística gulosa) continua sendo "the complete search method of choice in planners such as FF, FD, and LAMA" — ou seja, valida a centralidade de *Heuristic Search* como categoria em 2017 —, mas mostra que o estado da arte de 2017 em diante passa a combinar heurística com exploração por largura, uma dimensão ausente na lista de A2.
  - **F4 (evidencia a fragilidade):** o surgimento e sucesso da busca por largura após 2012 (Lipovetzky & Geffner 2012) demonstra que a taxonomia de seis técnicas de 2010 não é apenas discutível quanto à classificação dos planejadores já existentes, mas também desatualizada frente a técnicas surgidas depois de 2010.

## Pontos relevantes para o projeto

- Introduz e formaliza o conceito de "novidade" (*novelty*) de um estado, base dos algoritmos IW(k) e da família *width-based*, citada explicitamente no protocolo de leitura como semente central do eixo E3.
- Mostra que a busca por largura tem origem fora do planejamento clássico "tradicional": foi usada com sucesso em jogos Atari e na competição *General Video-Game AI* antes de ser reincorporada ao planejamento clássico — um exemplo concreto de técnica que "migrou" de outra subárea de IA.
- Detalha como LAMA combina múltiplas filas de busca (duas ordenadas por hFF/hadd, duas por hL, com filas adicionais para ações úteis) — detalhe técnico útil para comparação com a nota sobre richter2010lama.
- O artigo é publicado em 2017, sete anos depois da dissertação de 2010 — bom marcador temporal para argumentar, na revisão, que a taxonomia de técnicas precisa acompanhar o estado da arte de forma contínua (ligação com T2, trabalho futuro de 2010 sobre agregação automática de novos resultados).

## Marcações

- `[FATO]` GBFS é "the complete search method of choice in planners such as FF, FD, and LAMA", mas sofre de platôs heurísticos que a busca por largura ajuda a superar (Introdução).
- `[FATO]` A novidade de um estado s é definida como i se e somente se existe uma tupla t de i átomos tal que s é o primeiro estado na busca a tornar todos os átomos de t verdadeiros, e nenhuma tupla menor tem essa propriedade (Seção "Width-Based Search").
- `[HIPÓTESE]` A ausência da família *width-based* na taxonomia de 2010 não é uma falha da dissertação original (a técnica de Lipovetzky & Geffner é de 2012, dois anos posterior), mas evidencia que qualquer taxonomia fixa em um só momento no tempo tende a ficar desatualizada — ponto relevante para T2/Q1 da revisão atual.

## Trechos literais

1. "In classical planning, exploration is not needed for optimality, as greedy best-first search (GBFS) and, indeed, any best-first algorithm (BFS), delivers optimal solutions when used in anytime mode [...]. GBFS is the complete search method of choice in planners such as FF, FD, and LAMA." (Seção "Background")
2. "The algorithm IW(k) is a normal breadth-first except that newly generated states s are pruned when their 'novelty' is greater than k, where the novelty of s is i iff there is a tuple t of i atoms such that s is the first state in the search that makes all the atoms in t true." (Seção "Width-Based Search")
3. "Width-based exploration in GBFS is more effective than GBFS with local GBFS search (GBFS-LS), and then proceed to formulate a simple and general computational framework [...] best-first width search, that is better than both." (Resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/AAAI/article/view/11027/10886. Conferência humana: pendente.
