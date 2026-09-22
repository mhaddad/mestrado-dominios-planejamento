---
tipo: nota-de-leitura
eixo: E7
citekey: smithmiles2014towards
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: http://www.rhydlewis.eu/papers/COR_RhydFINAL.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A3]
fragilidades: [F2]
perguntas: [Q1, Q2]
---

# Towards objective measures of algorithm performance across instance space

**Smith-Miles, K.; Baatar, D.; Wreford, B.; Lewis, R. · 2014 · Computers & Operations Research**
**Link/DOI:** https://doi.org/10.1016/j.cor.2013.11.015

## Extração estruturada

- **Problema:** a avaliação de desempenho de algoritmos de otimização costuma reportar desempenho médio sobre um conjunto escolhido de instâncias, o que pode enviesar as conclusões; falta uma metodologia objetiva para comparar forças e fraquezas de diferentes algoritmos ao longo de um espaço de instâncias mais amplo.
- **Método:** propõe uma metodologia (o que depois seria formalizado como *Instance Space Analysis*, ISA) para mapear o espaço de instâncias de um problema de otimização e revisita, com essa metodologia, resultados de um artigo anterior de Computers and Operations Research que comparava heurísticas de coloração de grafos.
- **Dados/benchmarks:** instâncias de coloração de grafos (revisita resultados de comparação de heurísticas já publicados).
- **Resultado principal:** demonstra (i) como existem regiões ("bolsões") do espaço de instâncias em que o desempenho de um algoritmo varia significativamente da média; (ii) como propriedades das instâncias podem prever o desempenho de algoritmos em instâncias não vistas, com alta acurácia; e (iii) como as forças e fraquezas relativas de cada algoritmo podem ser visualizadas e medidas objetivamente.
- **Relação com a dissertação de 2010:** **A1, A3** [confirma por analogia direta, HIPÓTESE] — é o artigo fundacional da metodologia de *Instance Space Analysis*, que é exatamente o programa de pesquisa que 2010 tentou executar de forma incipiente com métricas UML: caracterizar instâncias (domínios/problemas) por propriedades mensuráveis e usar essas propriedades para prever qual algoritmo (técnica) terá melhor desempenho, inclusive antes de rodar o problema (A3). **F2** [ajuda a tratar, HIPÓTESE] — a ênfase em cobrir todo o espaço de instâncias, e não apenas uma amostra pequena e enviesada, é diretamente relevante à fragilidade de amostra pequena de 2010.

## Pontos relevantes para o projeto

- É a base metodológica mais próxima, entre os itens deste lote, do programa de pesquisa de 2010: caracterizar problemas por métricas objetivas e prever desempenho de algoritmos a partir delas — mas aplicado a otimização combinatória (coloração de grafos), não a planejamento automatizado.
- Introduz a lógica de visualização do espaço de instâncias (mapear onde cada algoritmo é forte/fraco), algo que 2010 não fez de forma sistemática (usou apenas discretização Alto/Médio/Baixo).
- Precursor direto da linha de Algorithm Selection / ISA que aparece em outros itens do acervo (ver bischl2016aslib, kerschke2019automated, munoz2017instance).
- Trata de otimização combinatória geral, não de planejamento nem de agentes de IA — relação com Q4 é apenas indireta via metodologia, não referenciada diretamente na nota.

## Trechos literais

"we propose a methodology to enable the strengths and weaknesses of different optimization algorithms to be compared across a broader instance space" (resumo).

## Marcações

- `[FATO]` O artigo propõe uma metodologia para mapear o espaço de instâncias e prever desempenho de algoritmos a partir de propriedades das instâncias, revisitando dados de coloração de grafos (resumo e introdução).
- `[HIPÓTESE]` Essa metodologia é o análogo metodologicamente mais maduro do que 2010 tentou fazer com métricas UML e discretização; a comparação reforça A1 e A3, e a ênfase em cobertura ampla do espaço de instâncias evidencia a fragilidade F2 (amostra pequena) de 2010.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução em cópia de acesso aberto (http://www.rhydlewis.eu/papers/COR_RhydFINAL.pdf, preprint do autor), localizada via Semantic Scholar após o link da editora (ScienceDirect) recusar acesso. Conferência humana: pendente.
