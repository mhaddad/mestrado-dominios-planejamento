---
tipo: nota-de-leitura
eixo: E1
citekey: helmert2011fast
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ai.dmi.unibas.ch/papers/helmert-et-al-icaps2011ws.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6, A7]
fragilidades: [F5]
perguntas: [Q1]
---

# Fast Downward Stone Soup: A Baseline for Building Planner Portfolios

**Helmert, M.; Röger, G.; Karpas, E. · 2011 · IPC 2011 planner abstracts, 38–45**
**Link/DOI:** (sem DOI; https://ai.dmi.unibas.ch/papers/helmert-et-al-icaps2011ws.pdf)

## Extração estruturada

- **Problema:** como construir automaticamente, a partir de componentes já existentes do planejador Fast Downward (heurísticas e algoritmos de busca), um portfólio sequencial ("Stone Soup") competitivo para a IPC 2011, sem depender de features do problema de entrada.
- **Método:** *hill-climbing* simples no espaço de portfólios: a cada iteração, escolhe-se o incremento de tempo (aplicado a um único "ingrediente") que mais aumenta a pontuação do portfólio no conjunto de treino (IPC 1998–2008), até esgotar o limite de 1800s da IPC; a pontuação é 0/1 por instância na faixa ótima (resolveu ou não) e uma razão de qualidade da solução na faixa satisfativa.
- **Dados/benchmarks:** 1116 instâncias (faixa ótima) e conjunto equivalente (faixa satisfativa) das IPCs 1998–2008.
- **Resultado principal:** na faixa ótima, o portfólio (4 de 11 ingredientes: LM-cut, BJOLP e duas variantes de merge-and-shrink) resolve 654 das 673 instâncias solucionáveis por algum ingrediente, contra 605 do melhor ingrediente isolado (BJOLP); na faixa satisfativa, o portfólio atinge pontuação 1057,57 de um teto teórico ("holy grail") de 1078.
- **Relação com a dissertação de 2010:**
  - **A6 (corrige, por acúmulo de evidência independente):** todos os "ingredientes" de Fast Downward listados (LM-cut, merge-and-shrink, hmax, busca gulosa e A* ponderada com múltiplas heurísticas) são descritos exclusivamente como heurísticas combinadas por busca A* ou gulosa — nenhuma menção a decomposição hierárquica como técnica de busca de planos; merge-and-shrink usa abstrações, mas como mecanismo interno de cálculo de heurística, não como planejamento hierárquico no sentido HTN. Isso reforça, de forma independente da nota já registrada sobre helmert2006fast, que rotular Fast Downward como "*Hierarchical*" (A6) mistura o mecanismo interno de heurística com o algoritmo de busca.
  - **F5 (evidencia a fragilidade, mas com alternativa concreta):** a métrica de pontuação usada para a faixa satisfativa incorpora explicitamente a qualidade da solução (razão entre a melhor qualidade entre todos os ingredientes e a qualidade obtida pelo portfólio), não apenas se a instância foi resolvida — uma alternativa replicável e documentada à simplificação "eficiência = cobertura" de 2010 (A7/F5), relevante para T6.
  - **A7 (relacionado, nuança):** o texto reproduz a observação (creditada por outras fontes do lote a Roberts & Howe) de que "a cobertura de um algoritmo de planejamento raramente diminui muito ao reduzir seu tempo de execução — ou, dito de outro modo, se um planejador não resolve uma tarefa rapidamente, é provável que não a resolva de forma alguma". Isso dá algum suporte empírico à escolha de cobertura como proxy razoável quando o gargalo é tempo, mas o próprio artigo trata cobertura e qualidade como dimensões distintas — algo que 2010 (que usa majoritariamente planejadores satisfativos como FF, LPG, SGPlan, YAHSP) não faz.

## Pontos relevantes para o projeto

- A métrica "*holy grail*" (pontuação teórica máxima se cada ingrediente rodasse os 1800s completos) é um teto útil para avaliar quão perto um portfólio está do ótimo — poderia inspirar uma métrica de teto para reavaliar o "ranking de planejadores por domínio" de 2010.
- É um resumo de planejador de competição ("planner description"), não um artigo de pesquisa com revisão de literatura própria; qualquer generalização deve ser lida como relato de um sistema específico.
- A ordem dos ingredientes no portfólio importa explicitamente (por exemplo, priorizar planejadores que consomem memória rapidamente, ou que têm maior cobertura primeiro) — dimensão de escalonamento que o "ranking por domínio" de 2010 não trata, por não alocar tempo de CPU.

## Trechos literais

1. "There is no single common search algorithm and heuristic that dominates all others for classical planning." (Before We Can Eat)
2. "The coverage of a planning algorithm is often not diminished significantly when giving it less runtime, or put differently: if a planner does not solve a planning task quickly, it is likely not to solve it at all." (Before We Can Eat)
3. "With 654 solved instances, the portfolio significantly outperforms BJOLP, the best individual configuration, which solves 605 instances." (Optimizing IPC 2011 Soups)

## Marcações

- `[FATO]` O portfólio ótimo usa apenas 4 dos 11 ingredientes disponíveis (LM-cut, BJOLP, dois merge-and-shrink), todos descritos como heurísticas para busca A*, sem qualquer componente hierárquico no sentido HTN (Tabela 1; seção "Optimizing IPC 2011 Soups").
- `[FATO]` Na faixa satisfativa, a pontuação usada é a razão entre a melhor qualidade encontrada por qualquer ingrediente e a qualidade obtida pelo portfólio — métrica sensível à qualidade da solução, não só à cobertura (seção "Judging the Taste of a Soup").
- `[HIPÓTESE]` Como o conjunto de planejadores de 2010 é majoritariamente satisfativo, a simplificação "eficiência = cobertura" (A7/F5) provavelmente descarta informação que os próprios autores de portfólios de 2011 já consideravam relevante para esse tipo de planejador.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ai.dmi.unibas.ch/papers/helmert-et-al-icaps2011ws.pdf. Conferência humana: pendente.
