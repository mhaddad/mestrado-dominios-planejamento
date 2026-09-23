---
tipo: nota-de-leitura
eixo: E3
citekey: kautz1999unifying
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://www.ijcai.org/Proceedings/99-1/Papers/047.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# Unifying SAT-based and Graph-based Planning

**Kautz, H.; Selman, B. · 1999 · Proceedings of the 16th International Joint Conference on Artificial Intelligence (IJCAI-99), 318–325**
**Link/DOI:** https://www.ijcai.org/Proceedings/99-1/Papers/047.pdf (sem DOI registrado; verificado também via OpenAlex, sem DOI)

## Extração estruturada

- **Problema:** unificar a abordagem de planejamento como satisfatibilidade (SATPLAN) com a abordagem de grafos de planos (GraphPlan), para resolver problemas STRIPS com desempenho competitivo.
- **Método:** o planejador Blackbox constrói primeiro um grafo de planos (GraphPlan) para limitar o espaço de busca e depois traduz esse grafo em uma instância de satisfatibilidade proposicional (SAT), resolvida por um SAT-solver plugável (Walksat, satz, rel_sat).
- **Dados/benchmarks:** problemas de planejamento clássicos usados para comparar Blackbox, SATPLAN e Graphplan (domínio de logística e outros citados no artigo).
- **Resultado principal:** para alguns problemas computacionalmente difíceis, a abordagem unificada supera tanto SATPLAN quanto Graphplan isoladamente; algoritmos polinomiais de simplificação SAT aplicados à instância traduzida complementam a propagação de mutex do grafo de planos.
- **Relação com a dissertação de 2010:**
  - **A6 (corrige):** 2010 classifica Blackbox como State-Space, Total-order, Forward-chaining, Graph-based e SAT-based (Tabela 4). A fonte confirma diretamente Graph-based e SAT-based, mas não descreve Blackbox como busca sequencial no espaço de estados (State-Space) nem como busca dirigida a partir do estado inicial (Forward-chaining): o mecanismo é construção de um grafo de planos seguida de tradução e resolução SAT, sem percorrer estados um a um. O rótulo "Forward-chaining" para planejadores SAT-based é uma convenção estipulada pela própria dissertação (corpo do texto, antes da Tabela 2: "planejadores baseados em resolução de problemas de satisfabilidade são relacionados com a técnica Forward-chaining"), não uma descrição extraída da fonte primária.

## Pontos relevantes para o projeto

- A fonte primária descreve Blackbox como um sistema de duas fases (grafo de planos → tradução SAT → solução), sem uma noção de "estado atual" percorrido sequencialmente — relevante para a dimensão "algoritmo de busca" da nova taxonomia da Fase 2.
- Confirma que a escolha do SAT-solver é modular (Walksat, satz, rel_sat), o que pode ser relevante para a dimensão "arquitetura" (não é portfólio, mas tem um componente plugável).

## Marcações

- `[FATO]` Blackbox unifica planejamento-como-satisfatibilidade com a abordagem de grafo de planos do GraphPlan (Resumo).
- `[HIPÓTESE]` O rótulo "Forward-chaining" atribuído por 2010 a planejadores SAT-based é uma convenção declarada pelos próprios autores da dissertação, não uma leitura da fonte primária de cada planejador — o que ajuda a explicar por que esse rótulo aparece em todos os planejadores SAT-based (Blackbox, SATPlan, MaxPlan) independentemente do que a fonte de cada um descreve.

## Trechos literais

1. "The Blackbox planning system unifies the planning as satisfiability framework (Kautz and Selman 1992, 1996) with the plan graph approach to STRIPS planning (Blum and Furst 1995)." (Resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral em https://www.ijcai.org/Proceedings/99-1/Papers/047.pdf (PDF baixado diretamente e extraído com `pdftotext -layout`). Conferência humana: pendente.
