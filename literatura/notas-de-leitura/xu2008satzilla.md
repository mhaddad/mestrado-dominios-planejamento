---
tipo: nota-de-leitura
eixo: E1
citekey: xu2008satzilla
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/download/10556/25269/19618
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1]
fragilidades: [F1]
perguntas: [Q2]
---

# SATzilla: Portfolio-based Algorithm Selection for SAT

**Xu, L.; Hutter, F.; Hoos, H. H.; Leyton-Brown, K. · 2008 · Journal of Artificial Intelligence Research 32, 565–606**
**Link/DOI:** https://doi.org/10.1613/jair.2490

## Extração estruturada

- **Problema:** construir portfólios de algoritmos SAT que escolham, por instância, qual(is) solucionador(es) executar, usando modelos empíricos de dureza (*empirical hardness models*) baseados em *features* da instância.
- **Método:** SATzilla07 usa 48 *features* (de 84 originalmente propostas por Nudelman et al. 2004) — tamanho do problema, grafos variável-cláusula, balanceamento, proximidade a fórmulas de Horn, sondagem DPLL e de busca local — para prever, por regressão, o tempo de execução de cada solucionador; seleciona pré-solucionadores rápidos, um solucionador de *backup* e o solucionador principal previsto como melhor. É um portfólio sequencial "3-of-n" (dois pré-solucionadores seguidos de um solucionador principal).
- **Dados/benchmarks:** instâncias da Competição SAT (categorias RANDOM, INDUSTRIAL, HANDMADE), incluindo as instâncias da Competição SAT de 2007.
- **Resultado principal:** SATzilla07 ganhou três medalhas de ouro, uma de prata e uma de bronze na Competição SAT de 2007; nos experimentos dos próprios autores, SATzilla sempre supera seus componentes individuais.
- **Relação com a dissertação de 2010:**
  - **A1/Q2 (confirma o princípio, aplicado a outro domínio):** SATzilla é o exemplo mais citado, em todo o campo de seleção de algoritmo, de que características de instância (não de domínio inteiro) predizem desempenho de solucionador — o mesmo princípio geral de A1 (características → técnica de melhor desempenho), mas aplicado a instâncias de SAT com *features* numéricas de grafo e de busca local, não a diagramas UML de domínios de planejamento. É a referência fundacional que toda a literatura de portfólios de planejamento lida neste lote (PbP, IBaCoP, Cedalion, Delfi) cita como ponto de partida metodológico.
  - **F1 (evidencia a lacuna por proximidade metodológica):** embora SATzilla trate de SAT, não de planejamento, sua influência direta sobre os métodos de PbP, Cedalion (via Hydra) e IBaCoP mostra que 2010 estava isolado não só da literatura de planejamento sobre portfólios (Roberts & Howe), mas também da tradição mais ampla de seleção de algoritmo por características (Rice 1976; SATzilla), da qual aquela literatura deriva diretamente.

## Pontos relevantes para o projeto

- A definição de "(a,b)-of-n portfolio" (SATzilla é um "3-of-n") é uma taxonomia mais precisa de estrutura de portfólio do que a distinção usada em 2010; útil para descrever com precisão o "ranking de planejadores por domínio" de 2010 (que seria um n-of-n com ordenação, sem alocação de tempo).
- O artigo distingue explicitamente a abordagem "*winner-take-all*" (escolher o melhor solucionador médio) do "*algorithm selection problem*" de Rice — 2010 pratica algo intermediário (um ranking por domínio, não uma escolha única, mas também não *per-instance*).
- Os "*hierarchical hardness models*" de SATzilla (não confundir com "*Hierarchical*" de A6) usam classificação prévia do tipo de instância antes de prever tempo — outra "hierarquia" no sentido de *pipeline* de modelos, terminologia potencialmente confusa que reforça a fragilidade F4 sobre uso impreciso de "hierárquico" na literatura.

## Trechos literais

1. "practitioners with hard SAT problems to solve face a potentially difficult \"algorithm selection problem\" (Rice, 1976): which algorithm(s) should be run in order to minimize some performance objective" (Seção 1.1, The Algorithm Selection Problem)
2. "we define an (a, b)-of-n portfolio as a set of n algorithms and a procedure for selecting among them with the property that if no algorithm terminates early, at least a and no more than b algorithms will be executed." (Seção 1.2, Algorithm Portfolios)
3. "SATzilla07 solvers won three gold, one silver and one bronze medal" (Resumo)

## Marcações

- `[FATO]` SATzilla07 usa 48 *features* de instância para prever tempo de execução via regressão e venceu cinco medalhas na Competição SAT 2007 (Resumo; Seção 3.3).
- `[FATO]` SATzilla é formalmente um portfólio sequencial "3-of-n" (dois pré-solucionadores mais um solucionador principal) (Seção 1.2).
- `[HIPÓTESE]` O uso do termo "*hierarchical hardness models*" por SATzilla, num sentido totalmente distinto de "*Hierarchical*" como técnica de planejamento (A6), sugere que parte da confusão terminológica de 2010 pode vir de transposição imprecisa de termos entre subcampos da IA.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/download/10556/25269/19618. Conferência humana: pendente.
