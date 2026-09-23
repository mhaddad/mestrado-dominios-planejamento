---
tipo: nota-de-leitura
eixo: E2
citekey: domshlak2013complexity
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://www.jair.org/index.php/jair/article/download/10852/25897/20241
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5]
fragilidades: [F3, F4]
perguntas: [Q2]
---

# The Complexity of Optimal Monotonic Planning: The Bad, The Good, and The Causal Graph

**Domshlak, C.; Nazarenko, A. · 2013 · Journal of Artificial Intelligence Research 48**
**Link/DOI:** 10.1613/jair.4145

## Extração estruturada

- **Problema:** caracterizar, de forma refinada, a complexidade de pior caso do planejamento monotônico (relaxação "*delete-free*") ótimo — central às heurísticas de estado da arte —, identificando o que fica mais difícil e o que fica mais fácil ao restringir a topologia do grafo causal, em representações de tarefa com domínio finito (*finite-domain representation*, FDR).
- **Método:** análise teórica de complexidade computacional, estabelecendo resultados negativos (casos difíceis mesmo com estruturas de grafo causal simples) e positivos (tratabilidade em função do *treewidth* do grafo causal e do tamanho dos domínios das variáveis de estado).
- **Dados/benchmarks:** não há experimentação empírica; é um artigo de complexidade computacional (provas teóricas), sem *benchmarks* de execução.
- **Resultado principal:** planejamento ótimo para relaxações monotônicas é difícil mesmo com estruturas de grafo causal simples quando os domínios das variáveis são grandes; restrito a domínios de tamanho constante, o problema se torna solúvel em tempo exponencial apenas no *treewidth* do grafo causal — uma tratabilidade mais ampla do que a do planejamento ótimo geral não-relaxado.
- **Relação com a dissertação de 2010:** relação indireta com **A5** (diagramas UML medem complexidade do domínio, que afeta desempenho de técnicas): este artigo mostra, formalmente, que a estrutura do **grafo causal** (não a UML) é a variável estrutural que efetivamente determina a complexidade computacional de uma classe de planejamento. Isso sugere, para **Q2**, que a complexidade estrutural relevante à escolha de técnica pode estar mais bem capturada por estruturas nativas do PDDL (grafo causal, *treewidth*) do que por métricas de diagramas UML de caso de uso/classes/estados como as de 2010. Toca **F3** (métricas UML dependem do modelador) e **F4** (taxonomia de técnicas discutível): a métrica aqui (*treewidth* do grafo causal) é objetiva e derivada automaticamente do PDDL, sem depender de interpretação humana do domínio.

## Pontos relevantes para o projeto

- Fornece uma métrica estrutural alternativa às de UML — *treewidth* do grafo causal — com fundamentação teórica rigorosa e extraível automaticamente do PDDL, candidata natural para uma réplica de 2010 que queira responder **Q2** com rigor formal, não só empírico.
- É um artigo puramente teórico (sem execução de planejadores), o que limita sua relação direta com o núcleo empírico de 2010 (ranking por cobertura), mas fortalece o argumento de que características estruturais objetivas do domínio (grafo causal) afetam a dificuldade computacional, logo plausivelmente o desempenho prático das técnicas.
- Não trata de seleção de planejador nem de comparação entre técnicas — é ortogonal ao núcleo empírico de 2010, mas relevante ao debate teórico sobre o que conta como "característica de domínio".

## Trechos literais

> "Optimal planning for monotonic relaxations is hard even if restricted to very simple causal graph structures, but the complexity there stems from the size of the state variable domains." (Seção 6, Summary and Future Work)

## Marcações

- `[FATO]` Restrito a variáveis de estado de domínio constante, o planejamento monotônico ótimo é solúvel em tempo exponencial apenas no *treewidth* do grafo causal (Seção 6, item 2).
- `[HIPÓTESE]` O *treewidth* do grafo causal é uma característica estrutural do domínio, objetiva e automaticamente extraível do PDDL, que poderia substituir ou complementar as métricas UML de 2010 (A5) em uma réplica que queira responder Q2 com base teórica, não apenas correlação empírica.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão (Seção 6) em https://www.jair.org/index.php/jair/article/download/10852/25897/20241. Conferência humana: pendente.
