---
tipo: nota-de-leitura
eixo: E3
citekey: rintanen2012planning
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://users.aalto.fi/~rintanj1/papers/Rintanen12AIJ.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q2]
---

# Planning as satisfiability: Heuristics

**Rintanen, J. · 2012 · Artificial Intelligence (AIJ)**
**Link/DOI:** 10.1016/j.artint.2012.08.001

## Extração estruturada

- **Problema:** melhorar a busca de planos por satisfatibilidade (SAT) usando uma heurística de seleção de variáveis específica para planejamento, em vez das heurísticas genéricas de solvers SAT (como VSIDS).
- **Método:** estratégia de seleção de variáveis para solvers CDCL, baseada em propriedades genéricas de planos; implementada no planejador Madagascar (SAT-based) e comparada com VSIDS e com outros métodos de busca (busca de estados com heurísticas).
- **Dados / benchmarks:** benchmarks das competições de planejamento (IPC) e problemas combinatoriamente difíceis (grafos, transição de fase de satisfatibilidade, sequenciamento de ações).
- **Resultado principal:** a heurística proposta supera VSIDS nos benchmarks das IPCs e aproxima o desempenho de solvers baseados em busca heurística de estados; em problemas pequenos mas combinatoriamente difíceis, VSIDS continua superior.
- **Relação com a dissertação de 2010:** o artigo **detalha** a família de planejamento por satisfatibilidade (SAT), que HADDAD (2010) trata em A6 como parte da classificação de técnicas (planejadores SAT como *forward-chaining*). O detalhamento da heurística de seleção de variáveis mostra que a família SAT-based tem subtécnicas próprias (heurísticas de variável específicas de planejamento vs. genéricas de SAT), o que **ajuda a corrigir/detalhar** a taxonomia simplificada de A6 e a fragilidade F4 (taxonomia discutível). Não trata diretamente de características estruturais de domínio (Q2), mas fornece uma peça da família de técnicas relevante para eixo E3.

## Pontos relevantes para o projeto

- Detalha subtécnicas dentro da família "SAT-based planning", útil para refinar A6/F4 (a dissertação de 2010 trata SAT genericamente como *forward-chaining*).
- Mostra que a escolha de heurística de variável é sensível ao tipo de problema (pequeno e combinatoriamente difícil vs. benchmarks de IPC), o que se conecta à pergunta geral de ajuste característica-técnica (Q1).
- Referência de peso na família SAT (planejador Madagascar), citado por outros trabalhos do lote (ex.: cenamor2019insights menciona Madagascar-pC).

## Marcações

- `[FATO]` A heurística de seleção de variáveis "based on generic principles about properties of plans" supera VSIDS nos benchmarks de planejamento (resumo; seção 8, Conclusions and Future Work).
- `[HIPÓTESE]` A existência de subtécnicas distintas dentro da família SAT sugere que a taxonomia de seis famílias de A2/A6 é grossa demais para capturar diferenças relevantes de desempenho — reforça F4.

## Trechos literais

- "The contribution of this paper is a simple yet powerful variable selection strategy for clause-learning SAT solvers that solve AI planning problems, as well as an empirical demonstration that the strategy outperforms VSIDS for benchmarks from the planning competitions." (seção 8, Conclusions and Future Work)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://users.aalto.fi/~rintanj1/papers/Rintanen12AIJ.pdf (resumo, introdução, sumário de seções e conclusão). Conferência humana: pendente.
