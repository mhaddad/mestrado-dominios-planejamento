---
tipo: nota-de-leitura
eixo: E2
citekey: hutter2014algorithm
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://www.cs.ubc.ca/~hoos/Publ/HutEtAl14-preprint.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: []
perguntas: [Q2]
---

# Algorithm Runtime Prediction: Methods & Evaluation

**Hutter, F.; Xu, L.; Hoos, H.H.; Leyton-Brown, K. · 2014 (preprint 2013) · Artificial Intelligence 206, 79–111**
**Link/DOI:** https://doi.org/10.1016/j.artint.2013.10.003

## Extração estruturada

- **Problema:** prever quanto tempo um algoritmo levará para resolver uma instância não vista de um problema combinatório difícil (SAT, MIP, TSP), tanto para algoritmos sem parâmetros quanto para algoritmos parametrizados — e fazer isso de forma mais precisa e mais geral que os métodos anteriores.
- **Método:** propõe técnicas de modelagem mais sofisticadas (*random forests* e processos gaussianos aproximados) para construir *empirical performance models* (EPMs); trata parâmetros de algoritmo (categóricos e contínuos) como entradas adicionais do modelo; introduz conjuntos abrangentes de *features* de instância para SAT (138), MIP (121) e TSP (64), incluindo *features* novas de sondagem (*probing*) e de tempo; avalia tudo isso na maior comparação experimental da área até então — 11 algoritmos, 35 distribuições de instâncias — cobrindo previsão para instâncias novas, configurações de parâmetro novas, e ambas simultaneamente.
- **Dados/benchmarks:** conjuntos de SAT (INDU, HAND, RAND, IBM, SWV etc.), MIP (BIGMIX, CORLAT etc.) e TSP, descritos em detalhe no Apêndice A — não inclui domínios de planejamento clássico.
- **Resultado principal:** os modelos baseados em *random forests* (e, secundariamente, processos gaussianos aproximados) superam consistentemente os métodos anteriores da literatura em todos os cenários testados, com coeficientes de correlação entre tempo previsto e real acima de 0,9 mesmo com poucas centenas de observações de treino.
- **Relação com a dissertação de 2010:** a obra não trata de planejamento automatizado nem discute domínios PDDL — não confirma, corrige nem torna obsoleta diretamente nenhuma afirmação A1–A8 de 2010. Sua relevância é **metodológica**: é a referência canônica, citada por Fawcett et al. (2014) e De la Rosa et al. (2017), do pipeline "*features* de instância → modelo estatístico (*random forest*) → predição de desempenho" e da técnica de seleção progressiva de *features* (*forward selection*) para medir importância relativa — exatamente o ferramental usado pelas obras de planejamento do eixo E2 para responder Q2. O próprio texto situa a origem da ideia na literatura de planejamento: "In the AI planning literature, Fink [26] used linear regression to predict how the performance of three planning algorithms depends on problem size... In the same community, Howe and co-authors [45, 97] used linear regression to predict how both a planner's runtime and its probability of success depend on various features of the planning problem" (Seção 2.1, Trabalhos Relacionados, p. 3) — ou seja, a própria linhagem metodológica de Roberts & Howe é reconhecida aqui como um dos pontos de partida históricos do campo de EPMs.
- **Features por classe (para Q2):** de modelo/representação (as 138+121+64 *features* de SAT/MIP/TSP, específicas de cada problema, não de planejamento); de sondagem (*probing features*, introduzidas nesta obra para os três problemas). Não há *features* de grafo causal/DTG nem sintáticas de PDDL, por não ser um artigo de planejamento.

## Pontos relevantes para o projeto

- É a referência metodológica-mãe da família de técnicas ("EPM", *random forest*, *forward selection* para importância de *features*) usada por todas as obras de predição de desempenho em planejamento lidas neste lote (Fawcett et al., De la Rosa et al.).
- Mostra que *random forests* são consistentemente a melhor família de modelo entre as testadas — justifica por que os artigos de planejamento do eixo E2 adotaram a mesma técnica.
- A técnica de seleção progressiva (*forward selection*) para medir importância de *features*, usada por Fawcett et al. (2014) para planejamento, é definida e validada aqui primeiro, em SAT/MIP/TSP.
- Não deve ser citada como evidência sobre domínios de planejamento — é preciso, na síntese, deixar claro que seu papel é de base metodológica, não de resultado aplicado ao domínio-alvo de 2010.

## Marcações

- `[FATO]` A obra não aborda planejamento clássico; seus experimentos cobrem exclusivamente SAT, MIP e TSP (Apêndice A; ausência de qualquer menção a PDDL ou planejadores fora da seção de trabalhos relacionados).
- `[FATO]` *Random forests* superaram as demais famílias de modelo (regressão linear, processos gaussianos exatos, redes neurais) em todos os cenários de avaliação (Seção 10, Conclusões).
- `[HIPÓTESE]` A adoção de *random forests* como modelo padrão nos artigos de EPM para planejamento (Fawcett et al. 2014, De la Rosa et al. 2017) decorre diretamente dos resultados desta obra, ainda que nenhum deles trate de planejamento automatizado.

## Trechos literais

1. "Over the past decade, a wide variety of techniques have been studied for building such models... we demonstrate that our new models yield substantially better runtime predictions than previous approaches." (Resumo)
2. "In the AI planning literature, Fink [26] used linear regression to predict how the performance of three planning algorithms depends on problem size and used these predictions for deciding which algorithm to run for how long." (Seção 2.1, Trabalhos Relacionados)
3. "Overall, we showed that our methods are fast, general, and achieve good, robust performance." (Seção 10, Conclusões)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://www.cs.ubc.ca/~hoos/Publ/HutEtAl14-preprint.pdf (baixado com `curl`, extraído com `pdftotext -layout`). Conferência humana: pendente.
