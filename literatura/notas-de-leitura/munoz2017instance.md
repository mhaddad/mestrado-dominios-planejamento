---
tipo: nota-de-leitura
eixo: E2
citekey: munoz2017instance
prioridade: A
status: lido
profundidade: resumo
fonte-lida: https://link.springer.com/article/10.1007/s10994-017-5629-5
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: []
perguntas: [Q2]
---

# Instance Spaces for Machine Learning Classification

**Muñoz, M.A.; Villanova, L.; Baatar, D.; Smith-Miles, K. · 2017 (publicado 2018) · Machine Learning 107(1), 109–147**
**Link/DOI:** https://doi.org/10.1007/s10994-017-5629-5

## Extração estruturada

- **Problema:** a avaliação de desempenho de classificadores de aprendizado de máquina costuma depender fortemente da escolha das instâncias de teste (ex.: o repositório UCI); o artigo questiona a diversidade e a qualidade desse repositório como base objetiva de avaliação.
- **Método (pelo resumo):** examina a diversidade e qualidade dos conjuntos de teste do repositório UCI, partindo do princípio de que propriedades estatísticas ou *features* de um conjunto de dados afetam a dificuldade de uma instância para algoritmos de classificação específicos. Constrói um "espaço de instâncias" (*instance space*) visualizável em duas dimensões, no qual cada conjunto de dados de classificação é representado como um ponto; o espaço é construído para revelar regiões de instâncias fáceis e difíceis, permitindo identificar pontos fortes e fracos de classificadores individuais. Propõe também uma metodologia para gerar novas instâncias de teste que enriqueçam a diversidade do espaço.
- **Dados/benchmarks:** conjuntos de dados de classificação do repositório UCI (não detalhado nesta leitura de resumo).
- **Resultado principal (pelo resumo):** o método revela "bolsões" de instâncias fáceis e difíceis no repositório UCI e demonstra como visualizar objetivamente forças e fraquezas de classificadores via projeção 2D do espaço de instâncias.
- **Relação com a dissertação de 2010:** a obra não trata de planejamento automatizado nem de PDDL — é sobre classificação de aprendizado de máquina em geral. Não confirma, corrige nem torna obsoleta diretamente nenhuma afirmação A1–A8. Sua relevância é **metodológica**, análoga a Hutter et al. (2014) e Leyton-Brown et al. (2009): formaliza a técnica de **análise de espaço de instâncias** (*instance space analysis*), que projeta um conjunto de instâncias em um espaço 2D com base em suas *features*, revelando onde diferentes algoritmos se saem melhor ou pior — é exatamente a técnica que os grupos de Vallati e Smith-Miles (citados por Vallati et al. 2014, ASAP, e mencionados como referência metodológica por Hutter et al. 2014) depois adaptaram para caracterizar domínios de planejamento e prever desempenho de planejadores. Relevante para Q2 como possível técnica complementar de visualização a ser considerada numa revisão de 2010, para além do *ranking* discreto por característica.
- **Features por classe (para Q2):** de modelo (propriedades estatísticas dos conjuntos de dados de classificação — análogo, em espírito, às métricas estruturais usadas em planejamento, mas aplicadas a *datasets* de aprendizado supervisionado, não a domínios PDDL).

## Pontos relevantes para o projeto

- A técnica de análise de espaço de instâncias (projeção 2D de instâncias por dificuldade/característica) é uma alternativa metodológica à discretização Alto/Médio/Baixo usada em 2010 (A1, F7) — poderia ser citada em T5/T6 (domínios artificiais, análise estatística da discretização) como direção de trabalho futuro.
- É referenciada por Hutter et al. (2014) como um dos poucos trabalhos que também consideram tarefas além da previsão de desempenho — agrupamento, classificação fácil/difícil, visualização — mesmo espectro de tarefas que uma revisão de 2010 poderia ambicionar para além do *ranking* simples.
- Não foi possível obter o texto integral (Springer bloqueou o acesso automatizado); a leitura ficou restrita ao resumo, recuperado de uma cópia arquivada da página do editor.

## Marcações

- `[FATO]` O artigo propõe uma projeção 2D do espaço de instâncias de classificação, construída para revelar "bolsões" de instâncias fáceis e difíceis para algoritmos de aprendizado de máquina (Resumo).
- `[HIPÓTESE]` A técnica de espaço de instâncias, se adaptada a domínios de planejamento (usando como eixos características estruturais como as de grafo causal/DTG, em vez de métricas UML), poderia oferecer uma alternativa visual e contínua ao *ranking* discreto de 2010, respondendo em parte a T5/T6.

## Trechos literais

1. "This paper tackles the issue of objective performance evaluation of machine learning classifiers, and the impact of the choice of test instances... We show how an instance space can be visualized, with each classification dataset represented as a point in the space. The instance space is constructed to reveal pockets of hard and easy instances, and enables the strengths and weaknesses of individual classifiers to be identified." (Resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://link.springer.com/article/10.1007/s10994-017-5629-5 (texto integral bloqueado por controle de acesso do editor; resumo recuperado de cópia arquivada da página, Wayback Machine, snapshot de 09/07/2024). Conferência humana: pendente — recomenda-se nova tentativa de leitura de texto integral via acesso institucional.
