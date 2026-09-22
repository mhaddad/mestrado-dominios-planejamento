---
tipo: nota-de-leitura
eixo: E2
citekey: vallati2016identifying
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://cdn.aaai.org/ojs/13715/13715-40-17233-1-2-20201228.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: []
perguntas: [Q2]
---

# Identifying and Exploiting Features for Effective Plan Retrieval in Case-Based Planning

**Vallati, M.; Serina, I.; Saetti, A.; Gerevini, A. · 2016 (versão de periódico; leitura feita na versão de conferência ICAPS 2015) · Fundamenta Informaticae**
**Link/DOI:** 10.3233/fi-2016-1447

## Extração estruturada

- **Problema:** identificar, dentro de uma grande biblioteca de problemas de planejamento já resolvidos, os problemas mais similares a um novo problema a resolver (recuperação de planos em *Case-Based Planning*, CBP) — as *features* de planejamento existentes nem sempre distinguem bem problemas dentro do mesmo domínio.
- **Método:** introdução de uma nova classe de *features* de problema de planejamento (baseadas, entre outras coisas, em grafos de extração de proposições — PEG), aplicadas para acelerar e melhorar a recuperação de planos no sistema de CBP OAKPlan.
- **Dados/benchmarks:** domínios de *benchmark* de planejamento (ex.: Logistics), comparando o desempenho do OAKPlan original com a versão que usa a nova recuperação baseada em *features* e com planejadores generativos, medindo IPC speed score (usada na trilha Ágil da IPC 2014), tempo de CPU e qualidade/estabilidade do plano.
- **Resultado principal:** a abordagem baseada nas novas *features* melhora o desempenho do OAKPlan em todos os domínios considerados, tanto em IPC speed score quanto em tempo de CPU para o casamento de planos, sendo mais rápida e produzindo planos de boa qualidade em comparação com o OAKPlan original e planejadores generativos.
- **Relação com a dissertação de 2010:** **confirma A1** por analogia — mostra que *features* bem escolhidas de um problema de planejamento (não UML, mas derivadas do próprio PDDL/grafo de extração de proposições) discriminam efetivamente entre problemas e aceleram/melhoram a técnica de solução (aqui, recuperação de casos), reforçando que características estruturais da instância/domínio têm poder preditivo sobre o desempenho da técnica.

## Pontos relevantes para o projeto

- É outra evidência, desta vez em *Case-Based Planning*, de que *features* de problema bem desenhadas (aqui, baseadas em grafos de extração de proposições) superam *features* genéricas anteriores (Fawcett et al. 2014) em poder discriminativo — relevante para **Q2** (métricas estruturais versus *features* de PDDL).
- Sugere aplicações de uma função de similaridade eficaz além do CBP: identificação de clusters de problemas para ajuste de configuração de planejadores em portfólios — conecta-se ao eixo E1 (seleção/configuração de algoritmos) deste mesmo lote.
- Observação de rastreabilidade: a leitura foi feita na versão de conferência (ICAPS 2015, disponível em acesso aberto via cdn.aaai.org), não na versão de periódico canônica (Fundamenta Informaticae, 2016) indicada como preferencial pela triagem; o conteúdo é presumivelmente equivalente, mas isso deve ser registrado.

## Trechos literais

> "In this work we have proposed an efficient method that exploits problem features for effectively retrieving similar planning problems. Our experimental analysis demonstrated that (i) the filtering process is performed quickly, usually in a few seconds, and (ii) the proposed method can significantly speed-up the state-of-the-art case-based planner OAKPlan." (Seção Conclusions)

## Marcações

- `[FATO]` A abordagem baseada em *features* melhora o desempenho do OAKPlan em todos os domínios testados, tanto em IPC speed score quanto em tempo de CPU (Seção de resultados, referência à Tabela 1).
- `[HIPÓTESE]` A leitura foi feita na versão de conferência (ICAPS 2015), não na versão de periódico (Fundamenta Informaticae 2016) apontada pela triagem como canônica; presume-se conteúdo substancialmente equivalente, mas isso precisa de conferência humana antes de qualquer citação formal.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão da versão de conferência (ICAPS 2015) em https://cdn.aaai.org/ojs/13715/13715-40-17233-1-2-20201228.pdf, por não ter sido possível acessar a versão de periódico canônica (paywall em journals.sagepub.com). Conferência humana: pendente.
