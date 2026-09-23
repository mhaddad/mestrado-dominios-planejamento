---
tipo: nota-de-leitura
eixo: E3
citekey: chen2006temporal
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/download/10460/25075
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026 (aprovação delegada ao Coordenador)
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# Temporal Planning using Subgoal Partitioning and Resolution in SGPlan

**Chen, Y.; Wah, B. W.; Hsu, C.-W. · 2006 · Journal of Artificial Intelligence Research 26, 323–369**
**Link/DOI:** https://doi.org/10.1613/jair.1918

## Extração estruturada

- **Problema:** resolver problemas de planejamento temporal em PDDL2.2 de forma escalável, particionando as restrições de exclusão mútua (mutex) do problema por subobjetivo em vez de tratá-lo como um único problema monolítico.
- **Método:** o planejador SGPlan4 particiona as restrições mutex de um problema temporal em grupos por subobjetivo (*subgoal partitioning*), resolve cada subproblema com uma versão modificada do planejador Metric-FF (um planejador de busca heurística forward, herdeiro do FF) e resolve iterativamente, entre os subproblemas, as restrições globais violadas (*partition-and-resolve*). O artigo também descreve técnicas de análise de *landmarks*, busca de caminhos e redução do espaço de busca.
- **Dados/benchmarks:** benchmarks da 3ª (IPC3) e 4ª (IPC4) Competições Internacionais de Planejamento.
- **Resultado principal:** SGPlan4 resolve com eficácia os benchmarks da IPC3 e IPC4, com sensibilidade documentada a cada técnica no balanço qualidade-tempo.
- **Relação com a dissertação de 2010:**
  - **A6 (corrige):** 2010 classifica SGPlan como Plan-Space, Partial-order e Forward-chaining (Tabela 4) — a única entre as cinco técnicas atribuídas a Blackbox/IPP/FF que não inclui Graph-based nem Heurist Search, apesar de o planejador interno (Metric-FF) ser um planejador de busca heurística forward. A fonte descreve a técnica central de SGPlan como particionamento de restrições em subproblemas resolvidos por um planejador de busca heurística forward — mais próxima de uma arquitetura de decomposição/particionamento do que da noção clássica de planejamento "Plan-Space" (busca no espaço de planos parciais sem comprometimento de ordem, ao estilo SNLP/UCPOP). O corpo do texto de 2010 (antes das tabelas) já descreve corretamente a ideia de dividir o problema em subproblemas, mas a etiqueta formal na Tabela 4 usa termos da literatura clássica de planejamento que não correspondem a essa descrição.

## Pontos relevantes para o projeto

- SGPlan é o único dos 10 planejadores cuja técnica central é decompor o problema em subproblemas resolvidos por um planejador interno — relevante tanto para a dimensão "algoritmo de busca" quanto para a dimensão "arquitetura do sistema" da Fase 2: não é um planejador único no sentido estrito (usa um solver interno completo, Metric-FF, por subproblema) nem um portfólio (não escolhe entre múltiplos planejadores distintos; usa sempre o mesmo Metric-FF modificado). É um caso a discutir explicitamente na definição da dimensão "arquitetura".
- A versão usada em 2010 é o SGPlan 6 (ver `auditoria/condicoes-de-execucao-2010.md`); este artigo descreve a linhagem SGPlan4, mas a técnica de particionamento e o uso do Metric-FF como planejador base são a mesma arquitetura herdada pelas versões posteriores (5 e 6), segundo a genealogia declarada no próprio artigo.

## Marcações

- `[FATO]` SGPlan4 particiona restrições mutex por subobjetivo e resolve cada subproblema com uma versão modificada do Metric-FF, um planejador de busca heurística forward (Resumo; Seção 5.3).
- `[HIPÓTESE]` A ausência de "Graph-based" e "Heurist Search" na classificação de 2010 para SGPlan, apesar de seu planejador interno ser heurístico, sugere que 2010 classificou SGPlan pela descrição de mais alto nível (divisão em subproblemas) sem examinar o mecanismo de busca do Metric-FF embutido.

## Trechos literais

1. "We present a partition-and-resolve strategy that looks for locally optimal subplans in constraint-partitioned temporal planning subproblems and that resolves those inconsistent global constraints across the subproblems." (Resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/download/10460/25075 (PDF baixado diretamente do JAIR e extraído com `pdftotext -layout`). Metadados (DOI, páginas) verificados via Crossref. Conferência humana: pendente.
