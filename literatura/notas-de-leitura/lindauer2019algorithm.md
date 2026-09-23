---
tipo: nota-de-leitura
eixo: E1
citekey: lindauer2019algorithm
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/1805.01214
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: [F2, F6]
perguntas: [Q1]
---

# The Algorithm Selection Competitions 2015 and 2017

**Lindauer, M.; van Rijn, J. N.; Kotthoff, L. · 2019 · Artificial Intelligence (também em arXiv:1805.01214)**
**Link/DOI:** 10.1016/j.artint.2018.10.004

## Extração estruturada

- **Problema:** relatar e comparar o estado da arte em seleção de algoritmos por instância, a partir dos resultados de duas competições internacionais (2015 e 2017) que avaliam sistemas de seleção em cenários diversos de IA.
- **Método:** organização e análise comparativa das submissões às competições, usando a *Algorithm Selection Library* (ASlib) como infraestrutura comum de cenários e a métrica PAR10 (penalização por *timeout*).
- **Dados/benchmarks:** cenários de seleção de algoritmos em domínios como SAT, CSP, ASP, Max-SAT, entre outros, reunidos na ASlib (Bischl et al., 2016).
- **Resultado principal:** o *virtual best solver* obtém, em média, *speedup* de 31,8x sobre o melhor solver único nos cenários de 2017; nenhum sistema submetido performa bem em todos os tipos de cenário, evidenciando um "problema de meta-seleção de algoritmo" ainda em aberto.
- **Relação com a dissertação de 2010:** sem relação direta com A1–A8. Toca **F2** (amostra pequena) e **F6** (dados fora de competições): o artigo mostra, para seleção de algoritmos em geral, como competições padronizadas (ASlib) sustentam comparações mais robustas do que dados isolados — o inverso do que 2010 fez, com 10 planejadores em 10+3 domínios sem *benchmark* compartilhado formal.

## Pontos relevantes para o projeto

- Fornece evidência quantitativa (31,8x de *speedup* do *virtual best solver*) de que a seleção por instância tem grande margem de ganho — pano de fundo útil para justificar por que a pergunta de 2010 (que técnica combina com qual domínio) continua relevante em 2026.
- Reforça a importância de infraestrutura de *benchmark* compartilhada (ASlib) como pré-requisito metodológico que 2010 não teve, relevante para **Q1**.
- Nenhum sistema domina todos os cenários — achado consistente com A1 (características do domínio/instância importam para escolher a técnica), embora em outro subcampo de IA.

## Trechos literais

> "We show that although performance in some cases is very good, there is still room for improvement in other cases." (Resumo)

## Marcações

- `[FATO]` O *virtual best solver* obtém *speedup* médio de 31,8x sobre o melhor solver único nos cenários de tempo de execução de 2017 (Seção 6, Conclusions).
- `[HIPÓTESE]` O "problema de meta-seleção de algoritmo" (nenhum sistema domina todos os cenários) identificado aqui é análogo, em espírito, à motivação de 2010 de ligar características de domínio a técnicas de planejamento — mas com infraestrutura de comparação mais madura.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://arxiv.org/pdf/1805.01214. Conferência humana: pendente.
