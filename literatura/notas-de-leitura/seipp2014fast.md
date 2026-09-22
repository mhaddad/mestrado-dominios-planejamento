---
tipo: nota-de-leitura
eixo: E1
citekey: seipp2014fast
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://mrlab.ai/papers/seipp-et-al-ipc2014b.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A4, A6]
fragilidades: [F4]
perguntas: [Q1]
---

# Fast Downward Cedalion

**Seipp, J.; Sievers, S.; Hutter, F. · 2014 · IPC 2014: planner abstracts, 17–27**
**Link/DOI:** (sem DOI; https://mrlab.ai/papers/seipp-et-al-ipc2014b.pdf)

## Extração estruturada

- **Problema:** configurar automaticamente portfólios sequenciais de configurações do planejador Fast Downward para as faixas satisfativa, ótima e ágil da IPC 2014.
- **Método:** Cedalion itera: a cada passo, escolhe o par (configuração, fatia de tempo) que mais melhora a pontuação atual do portfólio por tempo gasto na busca, usando o configurador automático SMAC (otimização bayesiana/baseada em modelo) para explorar o espaço de configurações do Fast Downward; a cada iteração, remove do conjunto de treino as instâncias já resolvidas de forma ótima pelo portfólio corrente. É conceitualmente próximo de Hydra (que usa SATzilla para selecionar por instância) e do algoritmo guloso de Streeter, Golovin & Smith (2007), mas roda todas as configurações escolhidas em sequência, sem depender de *features* da instância.
- **Dados/benchmarks:** quase todos os domínios das IPCs 1998–2011, mais domínios adicionais com efeitos condicionais (Briefcaseworld, diagnóstico de redes elétricas, distância de edição de genoma, síntese de controladores de estado finito, compilações de planejamento conformante); para cada iteração de treino, 10 execuções paralelas de SMAC de 5–10 horas em até 10 máquinas.
- **Resultado principal:** o artigo é um resumo curto de planejador de competição — apresenta as configurações encontradas para as três faixas da IPC 2014 (listadas em apêndice), mas não traz, no corpo do texto, uma tabela de cobertura ou comparação de desempenho consolidada (ao contrário de helmert2011fast).
- **Relação com a dissertação de 2010:**
  - **A4 (relaciona-se, sem confirmar diretamente):** Cedalion busca automaticamente no espaço combinado de configurações do Fast Downward, mas os próprios autores reconhecem que não incluíram outros planejadores além dele por restrição de escopo, embora admitam que isso "*would have almost certainly improved performance*". Dá suporte indireto à ideia de que mais planejadores/técnicas melhoram o portfólio (A4), mas também expõe um custo prático (tempo de configuração) que 2010 não discute.
  - **A6/F4 (evidencia a fragilidade da taxonomia):** o apêndice lista mais de dez configurações distintas do Fast Downward — combinações de LM-cut, merge-and-shrink, CEGAR, PDBs (bancos de dados de padrões), hmax, busca gulosa e A* ponderada — todas dentro de um único "planejador" que 2010 rotula com um único par de técnicas (*Hierarchical*). Mostra, com evidência primária (as próprias linhas de configuração), que uma taxonomia de uma técnica por planejador é grosseira demais para capturar a diversidade real mesmo dentro de um só sistema.

## Pontos relevantes para o projeto

- Compara-se explicitamente a Hydra (Xu, Hoos & Leyton-Brown 2010) e ao algoritmo guloso de Streeter, Golovin & Smith (2007) — outra linhagem de portfólios que 2010 não cita, reforçando F1 por transitividade com as demais notas deste lote.
- É um "*planner abstract*" curtíssimo; mesmo classificado como prioridade A, a profundidade útil da leitura equivale, em extensão, à de um resumo estendido — vale registrar essa limitação de gênero textual para a síntese da onda.
- O apêndice com as configurações completas do Fast Downward é evidência primária direta de que "*Hierarchical*" (A6) não descreve nenhuma dessas configurações: todas usam A* ou busca gulosa com heurísticas diversas, sem qualquer decomposição hierárquica de plano.

## Trechos literais

1. "We could have included planners other than Fast Downward in our Cedalion portfolios... This would have almost certainly improved performance, due to the fact that portfolios can exploit the complementary strengths of diverse approaches. Nevertheless, we chose to limit ourselves to Fast Downward in order to quantify the performance gain possible within this framework." (Portfolio Configuration)
2. "Cedalion is our algorithm for automatically configuring sequential planning portfolios." (Portfolio Configuration)
3. "Cedalion iteratively selects the pair of planner configuration and time slice that improves the current portfolio the most per time spent." (Portfolio Configuration)

## Marcações

- `[FATO]` Os autores reconhecem que restringir o portfólio a um único planejador (Fast Downward) provavelmente custou desempenho frente a um portfólio multiplanejador (seção "Portfolio Configuration").
- `[FATO]` As mais de dez configurações de Fast Downward usadas nos portfólios de 2014 (Apêndice) combinam heurísticas de busca A*/gulosa distintas, nenhuma delas hierárquica no sentido clássico de decomposição de planos.
- `[HIPÓTESE]` Sendo um resumo técnico de competição, este texto contribui menos para responder Q1 diretamente do que para evidenciar, por acúmulo com as demais notas do lote, a fragilidade F4 (taxonomia de técnicas discutível).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://mrlab.ai/papers/seipp-et-al-ipc2014b.pdf. Conferência humana: pendente.
