---
tipo: nota-de-leitura
eixo: E3
citekey: vidal2004lookahead
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://cdn.aaai.org/ICAPS/2004/ICAPS04-020.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A2, A6]
fragilidades: [F4]
perguntas: [Q1]
---

# A Lookahead Strategy for Heuristic Search Planning

**Vidal, V. · 2004 · Proceedings of the 14th International Conference on Automated Planning and Scheduling (ICAPS-04), 150–160**
**Link/DOI:** https://cdn.aaai.org/ICAPS/2004/ICAPS04-020.pdf (sem DOI registrado; base do planejador YAHSP citado em 2010)

## Extração estruturada

- **Problema:** melhorar o desempenho da busca heurística forward em planejamento STRIPS não-ótimo, aproveitando melhor a informação já calculada pela heurística de plano relaxado do FF.
- **Método:** o artigo introduz uma estratégia de *lookahead* que reaproveita trechos do plano relaxado (extraído do grafo de planos do problema relaxado, técnica do FF) para gerar estados "adiantados" no espaço de busca, incorporados a um algoritmo *best-first search* completo e modificado para lidar com ações úteis (*helpful actions*) sem perder completude. Essa estratégia é a base do planejador YAHSP (Yet Another Heuristic Search Planner).
- **Dados/benchmarks:** domínios de referência das competições internacionais de planejamento (não há uma lista fechada no trecho lido; o artigo cita a 2ª e a 3ª IPC como contexto de desempenho do FF).
- **Resultado principal:** a estratégia de lookahead melhora o desempenho da busca heurística e o tamanho dos problemas resolvidos em numerosos domínios; YAHSP, baseado nela, teve bom desempenho na 4ª Competição Internacional de Planejamento (IPC-4), citada em 2010.
- **Relação com a dissertação de 2010:**
  - **A6 (corrige):** 2010 classifica YAHSP como State-Space, Total-order, Forward-chaining, Graph-based, Knowledge-based e Heurist Search (Tabela 4). A fonte confirma State-Space (forward-chaining best-first search), Graph-based (grafo de planos do problema relaxado, herdado do FF) e Heuristic Search — mas não descreve nenhum uso de conhecimento de domínio fornecido a priori: a técnica central é reaproveitar informação já calculada pela própria heurística (o plano relaxado), não conhecimento externo sobre o domínio. O rótulo "Knowledge-based" não tem respaldo no artigo.
  - **A2 (confirma parcialmente):** reforça *Heuristic Search* e *Forward-chaining* como técnicas centrais, mas evidencia mais um caso em que 2010 combina rótulos (aqui, "Knowledge-based") sem sustentação na fonte primária.

## Pontos relevantes para o projeto

- YAHSP é uma extensão direta do mecanismo de heurística do FF (mesmo grafo de planos relaxado), reforçando o padrão observado em Fast Downward e FF: "Graph-based" quase sempre descreve a heurística, não o algoritmo de busca.
- A confusão de "Knowledge-based" com "reaproveitamento de informação heurística já computada" é um bom exemplo, para a Fase 2, de por que a dimensão "tipo de heurística" precisa ser separada da dimensão "algoritmo de busca" e de eventuais rótulos genéricos como "baseado em conhecimento".

## Marcações

- `[FATO]` YAHSP é descrito como construído sobre a técnica de heurística de plano relaxado do FF, usada para lookahead em uma busca best-first forward (Resumo).
- `[HIPÓTESE]` O rótulo "Knowledge-based" de 2010 para YAHSP provavelmente decorre de uma leitura imprecisa da descrição de 2010 no corpo do texto ("considerando planos de alta qualidade computados por funções heurísticas em vários domínios"), interpretando "conhecimento sobre planos de alta qualidade" como uma técnica de planejamento baseada em conhecimento de domínio, quando a fonte descreve apenas reaproveitamento do plano relaxado já calculado pela heurística.

## Trechos literais

1. "We focus in this paper on a technique introduced in the FF planning system (Hoffmann & Nebel 2001) for calculating the heuristic, based on the extraction of a solution from a planning graph computed for the relaxed problem." (Introdução, p. 150)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral em https://cdn.aaai.org/ICAPS/2004/ICAPS04-020.pdf (PDF baixado diretamente e extraído com `pdftotext -layout`). Conferência humana: pendente.
