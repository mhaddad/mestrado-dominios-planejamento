---
tipo: nota-de-leitura
eixo: E3
citekey: sievers2016analysis
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/view/13763
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: []
---

# An Analysis of Merge Strategies for Merge-and-Shrink Heuristics

**Sievers, S.; Wehrle, M.; Helmert, M. · 2016 · ICAPS (Proceedings of the International Conference on Automated Planning and Scheduling)**
**Link/DOI:** 10.1609/icaps.v26i1.13763

## Extração estruturada

- **Problema:** o arcabouço *merge-and-shrink* fornece uma base geral para computar heurísticas de abstração para sistemas de transição fatorados; estratégias de *merge* não lineares foram recentemente mostradas úteis mas pouco estudadas em profundidade.
- **Método:** análise experimental da qualidade de estratégias de *merge* de estado da arte, comparando-as com estratégias aleatórias e considerando o efeito do desempate (*tie-breaking*).
- **Dados / benchmarks:** não especificado no resumo (dados de execução não lidos além do resumo, apenas indicados nesta fonte).
- **Resultado principal:** há espaço considerável para melhoria nas estratégias de *merge* de estado da arte; os autores descrevem uma nova estratégia de *merge* que supera experimentalmente o estado da arte atual.
- **Relação com a dissertação de 2010:** aprofunda a família de heurísticas de abstração *merge-and-shrink*, que não é uma das seis famílias listadas em A2/A6 de HADDAD (2010) — **corrige/detalha** a taxonomia (F4), mostrando que há subtécnicas (estratégias de *merge*) com impacto relevante de desempenho dentro dessa família, não capturadas por uma classificação de alto nível como a de 2010.

## Pontos relevantes para o projeto

- Reforça, junto com seipp2020saturated (também deste lote), que a família de heurísticas de abstração (*merge-and-shrink*, *cost partitioning*) é ativa e tecnicamente diversa, mas ausente da taxonomia A6 de 2010.
- Útil como contexto de fundo caso o Coordenador queira detalhar F4 com subfamílias dentro de "heurísticas admissíveis para planejamento ótimo".

## Trechos literais

- "We experimentally analyze the quality of state-of-the-art merge strategies by comparing them to random strategies and with respect to tie-breaking, showing that there is considerable room for improvement." (resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://ojs.aaai.org/index.php/ICAPS/article/view/13763 (não foi possível baixar o PDF completo nesta sessão; a página de visualização do periódico retornou apenas HTML). Conferência humana: pendente.
