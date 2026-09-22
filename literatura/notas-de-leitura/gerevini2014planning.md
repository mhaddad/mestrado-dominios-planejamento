---
tipo: nota-de-leitura
eixo: E1
citekey: gerevini2014planning
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/download/10894/25981/20325
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A6]
fragilidades: [F1]
perguntas: [Q1, Q2]
---

# Planning through Automatic Portfolio Configuration: The PbP Approach

**Gerevini, A. E.; Saetti, A.; Vallati, M. · 2014 · Journal of Artificial Intelligence Research 50, 639–696**
**Link/DOI:** https://doi.org/10.1613/jair.4359

## Extração estruturada

- **Problema:** como configurar automaticamente, para cada domínio de planejamento, um portfólio de planejadores existentes (com ou sem macro-ações) que maximize velocidade ou qualidade do plano.
- **Método:** PbP analisa estatisticamente (teste de Wilcoxon sign-rank) o desempenho de planejadores candidatos e de conjuntos de macro-ações candidatos sobre um conjunto de instâncias de treino do domínio-alvo; produz um "cluster" ordenado de planejadores (cada um com seu conjunto de macros, possivelmente vazio) executado por *round-robin scheduling* com fatias de CPU pré-calculadas. Tem duas variantes: PbP.s (velocidade) e PbP.q (qualidade do plano).
- **Dados/benchmarks:** domínios e problemas das faixas de aprendizado da IPC6 e IPC7.
- **Resultado principal:** PbP.s e PbP.q venceram a faixa de aprendizado da IPC6 e da IPC7; PbP configurado supera claramente PbP-nok (a versão não configurada, já competitiva com LAMA) e supera outros portfólios domain-specific/domain-independent existentes na maior parte dos casos.
- **Relação com a dissertação de 2010:**
  - **F1 (evidencia a lacuna):** a Seção 2 (Related Work) dedica-se extensamente a Roberts & Howe (sistema BUS e trabalhos subsequentes, 1999–2009) como a principal linha anterior de portfólios de planejadores por domínio, e cita Rice (1976) como base conceitual do problema de seleção de algoritmo aplicado a SAT/MaxSAT/QBF. 2010 não cita nenhuma dessas referências, apesar de tratar essencialmente do mesmo problema (relacionar características de domínio a técnicas de melhor desempenho) — confirma, com evidência bibliográfica direta, a lacuna já registrada no plano (seção 4, F1, que nomeia explicitamente Roberts & Howe).
  - **A1 (torna obsoleta a abordagem específica, não a pergunta):** PbP mostra que, já em 2009–2014, é possível derivar automaticamente, por domínio, um portfólio configurado a partir de estatística de desempenho dos próprios planejadores nas instâncias de treino, sem depender de métricas estruturais de modelagem UML nem de discretização Alto/Médio/Baixo. A pergunta de 2010 (que características do domínio preveem a melhor técnica) permanece válida, mas a resposta operacional de PbP prescinde inteiramente das métricas de 2010.
  - **A6 (contexto, sem confirmar ou corrigir diretamente):** menciona que SGPlan5 tem uma "estratégia de *backup*" — um mecanismo alternativo de busca acionado quando o método padrão falha — e não um mecanismo de seleção automática entre técnicas. Combinado com a leitura de vallati2015portfolio (que classifica SGPlan e SATPlan como "*frameworks*", não portfólios), reforça que a taxonomia de técnicas de 2010 (A6) mistura critérios distintos (paradigma de busca vs. arquitetura de sistema).

## Pontos relevantes para o projeto

- A seção de trabalhos relacionados (Seção 2) é um mapa útil de toda a linhagem de portfólios em planejamento entre 1999 e 2014 — BUS, SATzilla/MaxSAT/QBF, PbP, e antecipa FDSS/IBaCoP/ASAP citados por outras obras deste lote — pode ajudar a consolidar F1 nas próximas ondas de leitura.
- PbP é *domain-specific* por construção (aprende um portfólio por domínio), mais próximo em espírito ao "ranking de planejadores por domínio" de 2010 do que os sistemas *per-instance* lidos neste lote (IBaCoP, Delfi) — mas com validação estatística explícita (teste de Wilcoxon) em vez de correlação com métricas de modelagem.
- Os autores corroboram empiricamente a observação atribuída a Howe et al. (1999) e Roberts & Howe de que *round-robin scheduling* com fatias de tempo é robusto para um portfólio de planejadores — achado relevante para T2/T4 (agregação automática de resultados; pesos por característica).

## Trechos literais

1. "no one outperforms all the others in every available benchmark domain (see, e.g., Roberts & Howe, 2009)" (Seção 1, Introdução)
2. "Many papers on algorithm portfolio design concern the definition of models to select the best algorithm(s) for an instance of a certain problem according to the values of some predetermined features of the instance (Rice, 1976)." (Seção 2.1, Algorithm Portfolio Design in Automated Reasoning)
3. "the round-robin scheduling of the planner execution times is a robust strategy for a planner portfolio (Howe, Dahlman, Hansen, vonMayrhauser, & Scheetz, 1999; Roberts & Howe, 2006)." (Seção 1, Introdução)

## Marcações

- `[FATO]` PbP.s e PbP.q venceram as faixas de aprendizado da IPC6 e da IPC7 (Resumo; Seção 1).
- `[FATO]` A configuração de PbP usa teste estatístico (Wilcoxon sign-rank) sobre o desempenho dos planejadores em instâncias de treino do próprio domínio, não métricas de modelagem estrutural do tipo UML (Seção 1, "based on a statistical analysis... using the Wilcoxon sign-rank test").
- `[HIPÓTESE]` A ausência de citação a Roberts & Howe e a Rice (1976) em 2010 provavelmente decorre de a dissertação ter emergido de uma linha de modelagem (itSIMPLE/UML), isolada da linha de portfólios de algoritmo onde o "problema de seleção de algoritmo por características" já estava formalizado havia décadas.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/download/10894/25981/20325. Conferência humana: pendente.
