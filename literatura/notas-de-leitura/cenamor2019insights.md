---
tipo: nota-de-leitura
eixo: E3
citekey: cenamor2019insights
prioridade: C
status: lido
profundidade: texto-integral
fonte-lida: https://icaps19.icaps-conference.org/workshops/WIPC/proceedings.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6, A7]
fragilidades: [F4, F5]
perguntas: [Q1, Q3]
---

# Insights from the 2018 IPC Benchmarks

**Cenamor, I.; et al. · 2019 · Anais do workshop WIPC, ICAPS-19 (proceedings do workshop, com várias contribuições)**
**Link/DOI:** https://icaps19.icaps-conference.org/workshops/WIPC/proceedings.pdf

## Extração estruturada

- **Problema:** este arquivo é o *proceedings* completo do workshop WIPC (Workshop on the International Planning Competition) de 2019, reunindo várias contribuições curtas que discutem e analisam os resultados/benchmarks da IPC-2018 (trilha clássica/determinística e trilha de planejamento probabilístico), não um único artigo com autoria unificada.
- **Método:** conjunto de posições e análises dos organizadores e participantes sobre metodologia de pontuação da IPC-2018, critérios de vitória e desempenho comparativo dos planejadores.
- **Dados / benchmarks:** IPC-2018, trilha clássica/determinística (comparação de planejadores) e trilha probabilística (comparação incluindo P ROST-DD, SOGBOFA, Random Bandit).
- **Resultado principal:** o vencedor da trilha clássica/ótima da IPC-2018 foi um **planejador de portfólio**, que chamou o vencedor da IPC anterior (baseado em busca simbólica) em cerca de metade de suas execuções bem-sucedidas, vencendo por uma margem pequena (~1% a mais de problemas resolvidos). O texto argumenta que a contribuição de planejadores de portfólio está mais no algoritmo de aprendizado de máquina que seleciona o planejador do que em técnicas de planejamento propriamente ditas, e discute se portfólios deveriam ser excluídos da competição. Na trilha probabilística, o vencedor foi **P ROST-DD** (Geißer e Speck 2018), com os *runners-up* SOGBOFA e Random Bandit separados por poucos pontos.
- **Relação com a dissertação de 2010:** achado forte para **A6/F4** — o vencedor da IPC-2018 é um portfólio orientado por classificador de aprendizado de máquina, categoria de técnica inexistente na taxonomia de seis famílias de 2010 (A2/A6). Isso **torna obsoleta** parte da taxonomia de 2010 para competições recentes, pois "vencer" hoje frequentemente significa "selecionar bem entre planejadores" e não pertencer a uma única família de busca. Também alimenta diretamente **Q3** (onde entram LLMs — como planejador, tradutor ou **seletor**): o papel do classificador de ML em Delfi é estruturalmente análogo ao de um seletor de configuração, o mesmo papel cogitado para LLMs em Q3/Q4. Reforça F5, pois o texto observa que a margem de vitória por cobertura (~1% de 200 problemas) é pequena, questionando o uso de cobertura como métrica decisiva (A7).

## Pontos relevantes para o projeto

- Primeiro achado do lote que documenta explicitamente um vencedor de IPC baseado em seleção por classificador de ML — ligação direta e concreta com Q3/Q4 (papel de LLMs como seletores de planejador/configuração).
- Discussão editorial sobre se portfólios "deveriam" contar como vencedores da competição é relevante para decidir como classificar tecnicamente planejadores de portfólio na taxonomia revisada (F4).
- Cita LAMA (Richter e Westphal 2010) como um caso ambíguo de portfólio, o que complica ainda mais a classificação de A6 (2010 trata LAMA implicitamente como uma técnica única).
- Contém também uma seção sobre a trilha probabilística (fora do escopo determinístico de 2010, mas mostra a diversidade de abordagens atuais: MCTS, gradiente de política, redes bayesianas).

## Trechos literais

- "The winner of IPC 2018 with an ≈ 1% lead in problems being solved, however, is a so-called portfolio planner, consisting of a selection of many different planners, one of which is chosen in a classifier that was trained on a manually selected set of benchmark instances." (seção de discussão sobre o vencedor de 2018)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral (proceedings do workshop) em https://icaps19.icaps-conference.org/workshops/WIPC/proceedings.pdf (introdução e seções de discussão sobre o vencedor de 2018 e a trilha probabilística; não foram lidas todas as contribuições individuais do volume). Conferência humana: pendente.
