---
tipo: nota-de-leitura
eixo: E4
citekey: chen2024learning
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/AAAI/article/view/29986/31730
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q2]
---

# Learning Domain-Independent Heuristics for Grounded and Lifted Planning

**Chen, D.Z.; Thiébaux, S.; Trevizan, F. · 2024 · AAAI**
**Link/DOI:** 10.1609/aaai.v38i18.29986

## Extração estruturada

- **Problema:** heurísticas independentes de domínio aprendidas por redes neurais em grafo (GNNs) para guiar a busca de planejamento; abordagens anteriores (STRIPS-HGN) têm limitações — representação de hipergrafo que ignora listas de exclusão (*delete lists*), função de agregação não invariante a permutação e a necessidade de construir todo o hipergrafo instanciado (impraticável para problemas grandes).
- **Método:** apresenta três representações de grafo para tarefas de planejamento adequadas ao aprendizado de heurísticas via GNNs; propõe o primeiro método para aprender heurísticas independentes de domínio usando apenas a representação *lifted* de uma tarefa de planejamento (não instanciada); análise teórica da expressividade dos modelos em relação a STRIPS-HGN; implementa o planejador GOOSE, otimizado para uso de GPU.
- **Dados / benchmarks:** conjunto de domínios de planejamento não especificado no trecho lido em detalhe; comparação com a heurística h_FF e com STRIPS-HGN, incluindo domínios como VisitAll, VisitSome, Spanner e Blocksworld.
- **Resultado principal:** as heurísticas aprendidas de forma independente de domínio generalizam para problemas muito maiores do que os do conjunto de treino, superando amplamente as heurísticas STRIPS-HGN; GOOSE (com a representação grounded SLG) supera ou empata com STRIPS-HGN (dependente de domínio) em quase todos os domínios testados, exceto VisitAll, e supera h_FF em VisitAll e VisitSome quanto a número de nós expandidos.
- **Relação com a dissertação de 2010:** relevante para **Q2** (métricas estruturais de modelagem acrescentam poder preditivo às *features* de PDDL?): este trabalho usa representações de grafo derivadas diretamente da estrutura PDDL/*lifted* da tarefa (não métricas de UML) como base para aprendizado de heurística — um paralelo conceitual às métricas estruturais de HADDAD (2010), mas obtidas de outra fonte (grafo da tarefa, não diagrama UML de domínio). Estende a taxonomia A6/F4 com a família de heurísticas independentes de domínio aprendidas por GNN, especialmente na variante *lifted* (não instanciada), inexistente em 2010.

## Pontos relevantes para o projeto

- Demonstra que representações estruturais derivadas da tarefa de planejamento (grafos de predicados/ações) têm poder preditivo para heurísticas de busca — paralelo direto, embora não idêntico, à intuição de Q2 sobre métricas estruturais.
- É o primeiro método, segundo os próprios autores, a aprender heurísticas independentes de domínio usando apenas a representação *lifted*, evidenciando uma fronteira de pesquisa relevante em 2024.
- Reforça, junto com wichlacz2022landmark (mesmo lote), a importância crescente do cenário *lifted* (não instanciado) na pesquisa recente de planejamento — dimensão ausente de HADDAD (2010).

## Marcações

- `[FATO]` As heurísticas aprendidas generalizam para problemas muito maiores que os do treino, superando STRIPS-HGN (seção 6, Conclusion).
- `[HIPÓTESE]` O uso de representações estruturais da tarefa (grafos PDDL) para prever desempenho de heurísticas é conceitualmente análogo ao uso de métricas estruturais de UML em 2010 para prever desempenho de técnicas — mas os dois trabalhos operam em granularidades distintas (heurística individual vs. técnica/planejador completo) e não foram comparados diretamente aqui.

## Trechos literais

- "We have constructed various novel graph representations of planning problems for the task of learning domain-independent heuristics. In particular we provide the first domain-independent graph representation of lifted planning." (seção 6, Conclusion)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/AAAI/article/view/29986/31730 (resumo, introdução e conclusão). Conferência humana: pendente.
