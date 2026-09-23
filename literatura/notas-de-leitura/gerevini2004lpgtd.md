---
tipo: nota-de-leitura
eixo: E3
citekey: gerevini2004lpgtd
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://icaps04.icaps-conference.org/demos/icaps04-lpgdemo.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026 (aprovação delegada ao Coordenador)
afirmacoes-2010: [A2, A6]
fragilidades: [F4]
perguntas: [Q1]
---

# LPG-TD: a Fully Automated Planner for PDDL2.2 Domains

**Gerevini, A.; Saetti, A.; Serina, I.; Toninelli, P. · 2004 · Proceedings do International Planning Competition, ICAPS-04 (descrição de sistema)**
**Link/DOI:** https://icaps04.icaps-conference.org/demos/icaps04-lpgdemo.pdf (sem DOI registrado)

## Extração estruturada

- **Problema:** estender o planejador LPG (Gerevini & Serina, 2002) para cobrir a maior parte dos recursos de PDDL2.2 (literais temporizados iniciais, predicados derivados por axiomas de domínio, ações duráveis, expressões numéricas), usado na 4ª Competição Internacional de Planejamento (IPC-4) — a versão citada por 2010 como "LPG-TD".
- **Método:** como a versão anterior do LPG, o LPG-TD é baseado em busca local estocástica (herdeira do Walksat) no espaço de "grafos de ação" (*action graphs*), um subgrafo do grafo de planos que representa planos parciais; a nova versão estende essa representação para tratar literais temporizados iniciais e predicados derivados, e melhora as fases de pré-processamento, busca (com lista tabu) e pós-processamento.
- **Dados/benchmarks:** domínios da IPC-4 com literais temporizados iniciais (ex.: Satellite) e predicados derivados; sem tabela de cobertura no artigo lido (é uma descrição de sistema, não um artigo experimental completo).
- **Resultado principal:** LPG-TD e SGPLAN foram, segundo o próprio artigo, os únicos planejadores da IPC-4 a suportar todos os recursos principais de PDDL2.1/2.2.
- **Relação com a dissertação de 2010:**
  - **A6 (corrige):** 2010 classifica LPG como Plan-Space, Partial-order, Forward-chaining, Graph-based e Heurist Search (Tabela 4). A fonte confirma Plan-Space (busca sobre planos parciais representados como grafos de ação), Graph-based e Heuristic Search (heurísticas de vizinhança), mas não descreve nenhum mecanismo de "forward-chaining": a busca é local, sobre um grafo de ação já construído, com reparos guiados por heurística — não uma expansão sequencial a partir do estado inicial. O termo "forward-chaining" não aparece em nenhum ponto do artigo.
  - **A2 (confirma):** reforça *Plan-Space* e *Heuristic Search* como técnicas centrais do LPG, mas mostra que essas categorias não se combinam bem com "Forward-chaining" como 2010 assume para todos os planejadores da tabela.

## Pontos relevantes para o projeto

- É o exemplo mais claro, entre os 10 planejadores, de busca local sobre planos parciais (não busca no espaço de estados) — referência central para a dimensão "algoritmo de busca" da nova taxonomia (busca local vs. progressão vs. SAT vs. grafo de planos).
- A versão usada em 2010 (LPG-td 1.0, ver `auditoria/condicoes-de-execucao-2010.md`) corresponde diretamente a este artigo de descrição de sistema da IPC-4.

## Marcações

- `[FATO]` LPG-TD é descrito pelos próprios autores como busca local estocástica no espaço de grafos de ação, sem menção a "forward-chaining" (Introdução).
- `[HIPÓTESE]` O rótulo "Forward-chaining" atribuído a LPG por 2010 provavelmente reflete uma regra geral aplicada a todos os planejadores da Tabela 2/3 (todos marcados com "x" em Forward-chaining), não uma leitura específica da fonte do LPG.

## Trechos literais

1. "Like the previous version of LPG, the new version is based on a stochastic local search in the space of particular 'action graphs' derived from the planning problem specification." (Introdução)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral em https://icaps04.icaps-conference.org/demos/icaps04-lpgdemo.pdf (PDF baixado diretamente e extraído com `pdftotext -layout`). Conferência humana: pendente.
