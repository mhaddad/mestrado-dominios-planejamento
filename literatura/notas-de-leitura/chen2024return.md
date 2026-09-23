---
tipo: nota-de-leitura
eixo: E4
citekey: chen2024return
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/view/31462
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q2]
---

# Return to Tradition: Learning Reliable Heuristics with Classical Machine Learning

**Chen, D.Z.; Trevizan, F.; Thiébaux, S. · 2024 · ICAPS**
**Link/DOI:** 10.1609/icaps.v34i1.31462

## Extração estruturada

- **Problema:** abordagens de aprendizado para planejamento ainda não alcançam desempenho competitivo com planejadores clássicos em vários domínios e têm desempenho geral fraco.
- **Método:** constrói representações de grafo de tarefas de planejamento *lifted* e usa o algoritmo Weisfeiler-Leman (WL) para gerar *features* a partir delas; essas *features* alimentam métodos clássicos de aprendizado de máquina, com muito menos parâmetros e treino muito mais rápido que os modelos de aprendizado profundo para planejamento do estado da arte.
- **Dados / benchmarks:** dez domínios de comparação, com métricas de cobertura e qualidade de plano, comparando com a heurística h_FF e com o planejador LAMA.
- **Resultado principal:** o método proposto, WL-GOOSE, aprende heurísticas de forma confiável a partir do zero e supera a heurística h_FF em um cenário de competição justo; também supera ou empata com LAMA em 4 de 10 domínios quanto a cobertura e em 7 de 10 domínios quanto a qualidade de plano — sendo, segundo os autores, o primeiro modelo de aprendizado para planejamento a atingir esses resultados.
- **Relação com a dissertação de 2010:** achado central para **Q2** (métricas estruturais de modelagem acrescentam poder preditivo às *features* de PDDL?): o artigo mostra que *features* derivadas de grafos estruturais da tarefa (via algoritmo WL), combinadas com aprendizado de máquina clássico (não profundo), conseguem rivalizar com LAMA — um resultado forte em favor da hipótese de que representações estruturais (análogas, em espírito, às métricas de diagramas UML de HADDAD 2010) têm poder preditivo relevante, com custo computacional muito menor que redes profundas.

## Pontos relevantes para o projeto

- Evidência direta e forte para Q2: *features* estruturais simples (grafos WL) bastam para métodos clássicos de ML rivalizarem com o estado da arte (LAMA) em parte dos domínios testados, sem o custo de aprendizado profundo.
- Metodologicamente relevante para qualquer replicação futura que compare métricas estruturais (T1, extração automática de métricas via itSIMPLE) com *features* aprendidas de grafos da tarefa.
- Explicitamente cita conexões teóricas com "*Description Logic Features* for planning", uma linha de trabalho relacionada a *features* estruturais interpretáveis.

## Trechos literais

- "Our novel approach, WL-GOOSE, reliably learns heuristics from scratch and outperforms the hFF heuristic in a fair competition setting. It also outperforms or ties with LAMA on 4 out of 10 domains on coverage and 7 out of 10 domains on plan quality." (resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://ojs.aaai.org/index.php/ICAPS/article/view/31462 (não foi possível baixar o PDF completo nesta sessão; a página de visualização do periódico retornou apenas HTML). Conferência humana: pendente.
