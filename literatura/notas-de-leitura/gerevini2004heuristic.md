---
tipo: nota-de-leitura
eixo: E2
citekey: gerevini2004heuristic
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://cdn.aaai.org/ICAPS/2004/ICAPS04-022.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026 (aprovação delegada ao Coordenador)
afirmacoes-2010: [A8]
fragilidades: []
perguntas: [Q1]
---

# An Empirical Analysis of Some Heuristic Features for Local Search in LPG

**Gerevini, A.; Saetti, A.; Serina, I. · 2004 · Proceedings of the Fourteenth International Conference on Automated Planning and Scheduling (ICAPS-04), Whistler, p. 171–180**
**Link/DOI:** sem DOI (proceedings AAAI pré-DOI); https://cdn.aaai.org/ICAPS/2004/ICAPS04-022.pdf

**Nota sobre identidade da obra:** esta é a fonte primária efetivamente citada por 2010 (referências, linha 1866 de `data/2010/extraido/texto.md`: "GEREVINI, A.; SAETTI, A.; SERINA, I. An Empirical Analysis of Some Heuristic Features for Local Search in LPG. [...] p. 171-180."). A chave já existente no projeto `gerevini2004lpgtd` é uma obra **diferente** — Gerevini, Saetti, Serina e Toninelli, "LPG-TD: a Fully Automated Planner for PDDL2.2 Domains" (descrição de sistema da IPC-4, com um quarto autor) — sem relação direta com a análise experimental de heurísticas discutida aqui. Um auditor da Onda 3 classificou as afirmações AF-192 a AF-194 comparando erroneamente com `gerevini2004lpgtd`; esta nota corrige a base de comparação.

## Extração estruturada

- **Problema:** entender e avaliar o impacto de características heurísticas do planejador LPG (baseado em busca local estocástica, algoritmo Walkplan) no seu desempenho.
- **Método:** duas contribuições declaradas pelos próprios autores (Introdução): (1) técnicas para restringir o espaço de vizinhança de busca do Walkplan e para escolher a próxima inconsistência a tratar; (2) análise experimental das principais características heurísticas do LPG — três funções heurísticas de avaliação de vizinhança (E0, EH, Eπ) e o parâmetro de ruído ("noise") que randomiza o próximo passo para escapar de mínimos locais — com teste estatístico de Friedman sobre percentual de problemas resolvidos, tempo de CPU e qualidade do plano.
- **Dados/benchmarks:** domínios STRIPS simples (não especificados por nome no trecho lido; o artigo diz "we focus our analysis on simple STRIPS domains").
- **Resultado principal:** restringir a vizinhança de busca do Walkplan por qualquer uma das técnicas propostas melhora estatisticamente o desempenho em tempo de CPU; a restrição chamada NRall foi a melhor entre as consideradas, tanto em tempo de CPU quanto em qualidade do plano; a função heurística Eπ (mais precisa e computacionalmente mais cara) só compensa quando combinada com restrição de vizinhança.
- **Relação com a dissertação de 2010:**
  - **A8 (confirma):** as três afirmações de 2010 sobre esta obra (AF-192, AF-193, AF-194) batem com o texto do artigo:
    - AF-192 ("estudo experimental para compreender e avaliar o impacto das funções heurísticas no desempenho do planejador LPG") corresponde quase literalmente ao resumo do artigo (Trecho 1).
    - AF-193 ("técnicas foram propostas para restringir a busca pela vizinhança no algoritmo Walkplan") corresponde à primeira contribuição declarada e à frase de abertura da própria seção de Conclusões do artigo (Trecho 2).
    - AF-194 ("análise das principais características heurísticas [...] impacto da busca local no planejador LPG") é, na prática, uma reformulação de AF-192 — mesma correspondência com o resumo do artigo, sem acrescentar afirmação nova conferível.
  - Não há incorreção factual identificada nas três afirmações; a citação de 2010 a este trabalho é fiel ao conteúdo da fonte primária, diferentemente do que ocorre com Hoffmann (2001) (ver nota `hoffmann2001topology`, onde a frase sobre o escopo "FF e HSP" está incorreta).

## Pontos relevantes para o projeto

- É a fonte primária real por trás de A8 para o trabalho de Gerevini, Saetti e Serina; a nota anterior do projeto associada a "Gerevini 2004" (`gerevini2004lpgtd`) é sobre outro artigo (descrição de sistema da IPC-4, quatro autores) — a Fase 2 deve usar `gerevini2004heuristic` em qualquer citação a este trabalho específico.
- Reforça, junto com a nota de `hoffmann2001topology`, a distinção entre "a citação individual a uma obra está correta" (aqui, sim) e "a seção como um todo é uma revisão de literatura suficiente" (não — ver insumo A8 da Fase 1: faltam Rice, Roberts & Howe, IPC 2008, LAMA e o artigo de 2005 do itSIMPLE).
- O artigo cita o próprio Hoffmann (2001) nas referências ("Hoffmann, J. Local search topology in planning benchmarks: an empirical analysis. In Proc. of IJCAI-01."), o que corrobora de forma independente a identificação da fonte primária de Hoffmann feita nesta Onda.

## Marcações

- `[FATO]` O resumo do artigo declara exatamente as duas contribuições que 2010 atribui à obra: técnicas de restrição de vizinhança do Walkplan e análise experimental do impacto das funções heurísticas no desempenho do LPG (Resumo; Conclusões).
- `[HIPÓTESE]` Nenhuma — as três afirmações de 2010 sobre esta obra são descritivas e batem com o texto lido; não há lacuna a preencher por interpretação.

## Trechos literais

1. "LPG is a planner that performed very well in the last International planning competition (2002). [...] In this paper we experimentally analyze the most important of them [heuristic features] with the goal of understanding and evaluating their impact on the performance of the planner." (Resumo)
2. "We have proposed some techniques for restricting the search neighborhood of Walkplan, and for selecting the next inconsistency to handle." (Conclusões, p. 179–180)
3. "we propose some techniques for effectively restricting the search neighborhood of Walkplan, and for selecting the next inconsistency to handle; [...] we experimentally analyze the main heuristic features for local search in LPG with the goal of understanding and evaluating their impact on the performance of the planner." (Introdução, contribuições declaradas)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral em https://cdn.aaai.org/ICAPS/2004/ICAPS04-022.pdf (PDF baixado diretamente e extraído com `pdftotext -layout`; páginas confirmadas no rodapé de cada página do próprio PDF, 171–180). Identidade da obra (autores, ano, venue) conferida no cabeçalho do PDF ("From: ICAPS-04 Proceedings. Copyright © 2004, AAAI"). Sem DOI localizado via Crossref para o artigo original de conferência (só a versão de periódico de 2011, obra distinta, tem DOI). Conferência humana: pendente.
