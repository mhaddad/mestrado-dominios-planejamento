---
tipo: nota-de-leitura
eixo: E1
citekey: lindauer2015autofolio
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://jair.org/index.php/jair/article/download/10955/26096/20440
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: [F4]
perguntas: [Q1]
---

# AutoFolio: An Automatically Configured Algorithm Selector

**Lindauer, M.; Hoos, H. H.; Hutter, F.; Schaub, T. · 2015 · Journal of Artificial Intelligence Research 53**
**Link/DOI:** 10.1613/jair.4726

## Extração estruturada

- **Problema:** como escolher, para um novo problema de seleção de algoritmos (AS), tanto a abordagem de seleção mais adequada quanto os valores de seus hiperparâmetros — hoje decididos manualmente e de forma não trivial.
- **Método:** AutoFolio, que aplica configuração automática de algoritmos (via ParamILS/SMAC) ao *framework* altamente parametrizado claspfolio 2, que implementa várias estratégias de seleção de algoritmos (SATzilla, ISAC, 3S, aspeed etc.) em um único sistema configurável.
- **Dados/benchmarks:** 13 cenários da *Algorithm Selection Library* (ASlib), cobrindo SAT, Max-SAT, CSP, ASP, QBF e *container pre-marshalling*.
- **Resultado principal:** AutoFolio superou o melhor solver único em 8 dos 13 cenários, com fatores de *speedup* entre 1,3 e 15,4, e estabeleceu novo estado da arte em 7 dos 13 cenários, igualando o estado da arte anterior nos demais.
- **Relação com a dissertação de 2010:** sem relação direta com A1–A8 (o artigo trata de seleção/configuração automática de algoritmos de propósito geral — SAT, ASP etc. —, não da relação entre características de domínios de planejamento e técnicas). Toca **F4**: mostra que mesmo dentro de uma única "técnica" de seleção de algoritmos, o espaço de configurações interfere fortemente no desempenho, reforçando que comparar "técnicas" de planejamento sem configuração controlada (como em 2010) mistura efeito de técnica com efeito de ajuste.

## Pontos relevantes para o projeto

- Demonstra, com a ASlib como *benchmark* padronizado, uma metodologia de comparação entre estratégias de seleção de algoritmo que poderia inspirar um protocolo de comparação mais rigoroso para planejadores (E1), algo que 2010 não tinha.
- Relevante para T2 (agregação automática de novos resultados): claspfolio 2/AutoFolio ilustra um sistema que incorpora resultados de múltiplas estratégias de forma automatizada — analogia de infraestrutura útil para pensar T2 em planejamento.

## Trechos literais

> "We demonstrate AutoFolio can significantly improve the performance of claspfolio 2 on 8 out of the 13 scenarios from the Algorithm Selection Library, leads to new state-of-the-art algorithm selectors for 7 of these scenarios." (Resumo)

## Marcações

- `[FATO]` AutoFolio supera o melhor solver único em 8 de 13 cenários ASlib, com ganhos de 1,3 a 15,4x (Resumo).
- `[HIPÓTESE]` A lição de que a configuração de hiperparâmetros afeta fortemente o desempenho de uma estratégia de seleção é transferível ao debate de 2010 sobre taxonomia de técnicas: parte da variação atribuída a "técnica" pode ser variação de ajuste/configuração não controlada.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://jair.org/index.php/jair/article/download/10955/26096/20440. Conferência humana: pendente.
