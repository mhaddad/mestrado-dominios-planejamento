---
tipo: nota-de-leitura
eixo: E1
citekey: cenamor2016ibacop
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/download/11020/26182/20526
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A3]
fragilidades: [F3]
perguntas: [Q2]
---

# The IBaCoP Planning System: Instance-Based Configured Portfolios

**Cenamor, I.; de la Rosa, T.; Fernández, F. · 2016 · Journal of Artificial Intelligence Research 56, 657–691**
**Link/DOI:** https://doi.org/10.1613/jair.5080

## Extração estruturada

- **Problema:** construir um portfólio de planejadores configurável por instância (não fixo), que decida quais planejadores incluir e por quanto tempo executar cada um, a partir de modelos preditivos.
- **Método:** três etapas: (1) filtragem de planejadores candidatos por dominância de Pareto sobre a métrica QT (qualidade × tempo) em *benchmarks* representativos; (2) modelagem preditiva — classificação (o planejador resolve a tarefa?) e regressão (em quanto tempo?) — usando 89 *features* automaticamente extraídas: PDDL básicas, de instanciação do Fast Downward, do grafo causal e dos grafos de transição de domínio (representação SAS+), heurísticas (hmax, hFF) e "*fact balance*" do plano relaxado; (3) estratégia de seleção que combina as predições numa configuração de portfólio.
- **Dados/benchmarks:** *benchmarks* de IPCs anteriores para treino; IPC 2014 para teste — a versão IBaCoP2 venceu a Faixa Satisfativa Sequencial.
- **Resultado principal:** IBaCoP2 venceu a Faixa Satisfativa Sequencial da IPC 2014; a conclusão central dos próprios autores é que a diversidade do conjunto de planejadores filtrados (não os modelos preditivos em si) é o que mais contribui para o desempenho do portfólio.
- **Relação com a dissertação de 2010:**
  - **Q2 (alimenta diretamente):** as 89 *features* usadas são inteiramente automáticas e derivadas da representação SAS+/grafo causal do Fast Downward, não de modelagem UML manual — resposta concreta a Q2 (características estruturais de PDDL/SAS+, não diagramas UML, sustentam a predição de desempenho de planejadores nesta linha de pesquisa).
  - **A3 (corrige):** 2010 afirma que características do domínio, independentemente do problema, bastam para escolher o ranking de planejadores. IBaCoP é explicitamente *per-instance*, e os autores concluem que configurações fixas por domínio "*are limited by the components and the fixed time bound for each base planner*", com teto de desempenho mais baixo que uma configuração dinâmica por instância — evidência direta contra a suficiência de "só características de domínio" (A3).
  - **F3 (mitiga, não resolve):** ao contrário das métricas UML de 2010 (que dependem do modelador), as *features* de IBaCoP são extraídas automaticamente e de forma determinística a partir do PDDL/SAS+, eliminando a variabilidade humana que F3 aponta como fragilidade — mas o próprio artigo reconhece que "*in their current form, predictive models hardly contribute to the overall performance of the portfolio*" (Conclusão): *features* automáticas não garantiram, sozinhas, ganho robusto de desempenho.

## Pontos relevantes para o projeto

- A filtragem por dominância de Pareto (métrica QT) é um método replicável para reduzir um conjunto grande de planejadores a poucos candidatos "diversos" — pode informar T4 (pesos por característica) ou uma futura etapa de seleção de planejadores na revisão.
- Os autores relatam explicitamente que estimar o tempo de execução continua muito difícil e que os modelos de regressão "não fornecem informação adicional útil" — acrescenta nuance a Q1 (as conclusões de 2010 se sustentam com mais dados e estatística?): mesmo com mais dados e aprendizado de máquina, prever desempenho continua difícil em 2016.
- A Seção 2.1.2 é, dentro deste lote, a fonte mais detalhada de um conjunto alternativo e bem documentado de métricas estruturais (grafo causal, grafos de transição de domínio) diretamente comparável às métricas UML de 2010 numa fase futura da revisão.

## Trechos literais

1. "there is still no agreement as to what a planning portfolio is (Vallati, Chrpa, & Kitchin, 2015)" (Introdução)
2. "static portfolio configurations (including IBACOP) are limited by the components and the fixed time bound for each base planner. Their performance has an upper-limit, as computed by MiPlan, that is smaller than the achievable performance of a dynamic configuration." (Conclusion and Future Work)
3. "In their current form, predictive models hardly contribute to the overall performance of the portfolio." (Conclusion and Future Work)

## Marcações

- `[FATO]` IBaCoP2 venceu a Faixa Satisfativa Sequencial da IPC 2014 (Resumo).
- `[FATO]` O conjunto de 89 *features* é inteiramente derivado do PDDL, da tradução para SAS+ do Fast Downward, do grafo causal, dos grafos de transição de domínio e de heurísticas — nenhuma delas é um diagrama UML (Seção 2.1.2; Apêndice A).
- `[HIPÓTESE]` O teto de desempenho mais baixo de configurações fixas por domínio, citado pelos autores, é evidência a favor de revisar A3 no sentido de "características de domínio são necessárias, mas não suficientes", quando comparadas a características de instância.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/download/11020/26182/20526. Conferência humana: pendente.
