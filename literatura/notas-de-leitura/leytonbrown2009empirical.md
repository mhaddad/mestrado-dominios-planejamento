---
tipo: nota-de-leitura
eixo: E2
citekey: leytonbrown2009empirical
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://www.cs.ubc.ca/~kevinlb/papers/EmpiricalHardness.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: []
perguntas: [Q2]
---

# Empirical Hardness Models: Methodology and a Case Study on Combinatorial Auctions

**Leyton-Brown, K.; Nudelman, E.; Shoham, Y. · 2009 · Journal of the ACM 56(4), 1–52**
**Link/DOI:** https://doi.org/10.1145/1538902.1538906

## Extração estruturada

- **Problema:** é possível prever quanto tempo um algoritmo levará para resolver uma instância não vista de um problema NP-completo? Se sim, para que serve essa previsão? O artigo propõe e valida uma metodologia geral, usando o problema de determinação de vencedores em leilões combinatórios (*winner determination problem*, WDP) como estudo de caso.
- **Método:** metodologia em cinco passos — (1) escolher o algoritmo; (2) escolher a distribuição de instâncias; (3) escolher *features*; (4) coletar dados; (5) construir modelos (regressão linear e quadrática, com seleção de subconjunto de *features*). Define 37 *features* candidatas do WDP, reduzidas a 30, organizadas em 5 grupos: grafo bipartido oferta-bem (*bid-good graph*), grafo de ofertas (*bid graph*, um grafo de restrições tipo CSP, com estatísticas de grau, coeficiente de agrupamento, excentricidade), *features* baseadas na relaxação por programação linear (vetor de folga inteira), *features* baseadas em preço, e tamanho do problema. Usa os modelos para (a) interpretar quais características tornam uma instância difícil, (b) construir um portfólio de algoritmos que supera o melhor algoritmo isolado, e (c) gerar distribuições de teste mais difíceis.
- **Dados/benchmarks:** instâncias de WDP geradas por CATS e por geradores legados; algoritmo CPLEX como solver principal, além de CASS e GL para construção de portfólio.
- **Resultado principal:** as *features* estruturais (independentes de distribuição) contêm informação suficiente para prever o tempo de execução do CPLEX com alta precisão; um portfólio composto por CPLEX+CASS+GL supera o CPLEX isolado por um fator de 3, apesar de CASS e GL serem individualmente mais lentos.
- **Relação com a dissertação de 2010:** a obra não trata de planejamento automatizado — é sobre leilões combinatórios (WDP), não PDDL. Não confirma, corrige nem torna obsoleta diretamente nenhuma afirmação A1–A8. Sua relevância é a mesma de Hutter et al. (2014): é a origem metodológica do paradigma "*features* estruturais de instância → modelo estatístico → previsão de dificuldade/tempo", que a linhagem Roberts & Howe → Cenamor et al. → Fawcett et al. → De la Rosa et al. adapta para planejamento. A ideia de usar grafos derivados da instância (grafo bipartido oferta-bem, grafo de restrições) para extrair *features* estruturais é o análogo, no domínio de leilões, do que o grafo causal e o DTG são para planejamento — mesma lógica metodológica, domínio de aplicação diferente.
- **Features por classe (para Q2):** estruturais de grafo (grafo bipartido oferta-bem e grafo de ofertas/restrições — 22 das 30 *features*, análogas em espírito ao grafo causal/DTG de planejamento); de modelo/representação (*features* da relaxação por programação linear); sintéticas de tamanho do problema. Não há *features* de sondagem de busca nesta obra (nota de rodapé 12 discute e descarta a ideia por custo computacional).

## Pontos relevantes para o projeto

- É citada explicitamente por Hutter et al. (2014) e por toda a linhagem de EPMs em planejamento como o trabalho fundador da metodologia de cinco passos — útil para o capítulo metodológico de uma revisão de 2010 que queira situar historicamente a família de técnicas.
- A distinção entre *features* do grafo bipartido (oferta-bem) e do grafo de restrições (ofertas) é conceitualmente equivalente à distinção, em planejamento, entre *features* de representação de domínio finito (FDR) e *features* de grafo causal/DTG — mesmo princípio de "dois grafos naturais associados a cada instância", aplicado a domínios diferentes.
- Discute explicitamente por que não usou *features* de sondagem de busca no WDP (dificuldade de estimar profundidade/fator de ramificação nesse problema) — contraste útil com planejamento, onde a sondagem (Fawcett et al. 2014) se mostrou viável e informativa.
- Demonstra construção de portfólio de algoritmos e geração de instâncias mais difíceis a partir do modelo de dificuldade — aplicações que aparecem depois, adaptadas, em Vallati et al. (2014, ASAP) para planejamento.

## Marcações

- `[FATO]` A obra não aborda planejamento clássico; seu estudo de caso é o problema de determinação de vencedores em leilões combinatórios (Seção 1.3).
- `[FATO]` Um portfólio de 3 algoritmos (CPLEX, CASS, GL), construído a partir do modelo de dificuldade, superou o CPLEX isolado por um fator de 3 (Seção 8, Conclusões).
- `[HIPÓTESE]` A escolha de 2010 de usar diagramas UML como fonte de características de domínio, em vez de grafos derivados diretamente da especificação formal do problema (como aqui e como em planejamento via grafo causal/DTG), representa uma bifurcação metodológica em relação à tradição de EPMs que esta obra funda — uma UML manualmente modelada introduz uma camada de interpretação humana ausente nos grafos extraídos automaticamente da instância.

## Trechos literais

1. "We propose the use of supervised machine learning to build models that predict an algorithm's runtime given a problem instance." (Resumo)
2. "There are two natural graphs associated with each instance... First is the bid-good graph (BGG)... The bid graph (BG) has an edge between each pair of bids that cannot appear together in the same allocation." (Seção 3.3, p. 18–19)
3. "We performed experiments on WDP algorithms, and showed that a portfolio composed of CPLEX, CASS and GL can outperform CPLEX alone by a factor of 3." (Seção 8, Conclusões, p. 48)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://www.cs.ubc.ca/~kevinlb/papers/EmpiricalHardness.pdf (baixado com `curl`, extraído com `pdftotext -layout`). Conferência humana: pendente.
