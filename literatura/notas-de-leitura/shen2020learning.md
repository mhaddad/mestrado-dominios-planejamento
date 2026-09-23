---
tipo: nota-de-leitura
eixo: E2
citekey: shen2020learning
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/download/6754/6608/9983
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A2]
fragilidades: []
perguntas: [Q2]
---

# Learning Domain-Independent Planning Heuristics with Hypergraph Networks

**Shen, W. B.; Trevizan, F.; Thiébaux, S. · 2020 · Proceedings of the International Conference on Automated Planning and Scheduling (ICAPS 2020)**
**Link/DOI:** 10.1609/icaps.v30i1.6754

## Extração estruturada

- **Problema:** aprender heurísticas de planejamento independentes de domínio inteiramente do zero — que generalizem não apenas entre estados, objetivos e conjuntos de objetos, mas também entre domínios nunca vistos no treino —, algo que abordagens anteriores de aprendizado para planejamento não alcançavam plenamente.
- **Método:** Hypergraph Networks (HGN), um novo *framework* que generaliza Graph Networks para hipergrafos; instanciado como STRIPS-HGNs, que mapeiam a representação em hipergrafo da relaxação *delete-free* de um problema STRIPS (vértices = proposições, hiperarestas = ações) para uma estimativa de custo, aproximando o caminho de custo mínimo nesse hipergrafo via uma arquitetura recorrente de codifica-processa-decodifica.
- **Dados/benchmarks:** problemas de planejamento STRIPS de múltiplos domínios, comparando os STRIPS-HGNs treinados de forma específica por domínio, multi-domínio e independente de domínio contra heurísticas clássicas de relaxação *delete-free* (hmax, hadd, LM-cut), usando número de expansões de nó em A* como métrica.
- **Resultado principal:** os STRIPS-HGNs aprendem heurísticas competitivas com LM-cut e outras heurísticas clássicas de relaxação, e conseguem generalizar para domínios não vistos durante o treinamento — sendo, segundo os autores, o primeiro trabalho a aprender heurísticas independentes de domínio inteiramente do zero.
- **Relação com a dissertação de 2010:** relação indireta com **A2** (técnicas mais promissoras incluem *heuristic search*): o artigo é um desenvolvimento moderno exatamente dentro da técnica que 2010 já apontava como promissora, mostrando que heurísticas de busca podem hoje ser aprendidas (não só projetadas manualmente) e generalizar entre domínios — uma evolução da "técnica heurística" que 2010 tratou como categoria fixa e não detalhada (ver **T3**, detalhar subtécnicas).

## Pontos relevantes para o projeto

- É evidência de que a fronteira de pesquisa em heurísticas de busca (uma das técnicas "promissoras" de A2) hoje passa por aprendizado de representação (hipergrafos, GNN), não apenas por heurísticas manualmente projetadas — relevante para **T3** (detalhar subtécnicas de busca heurística) se a revisão quiser atualizar a taxonomia de 2010.
- A generalização entre domínios nunca vistos é um resultado forte que relativiza a premissa de 2010 de que cada domínio precisa de uma técnica "combinada" a ele: aqui, uma única heurística aprendida funciona razoavelmente bem em múltiplos domínios, inclusive não vistos.
- Não trata de seleção/ranking de planejadores nem de características estruturais tipo UML — é ortogonal ao núcleo empírico de 2010, mas relevante à discussão de como as próprias técnicas internas evoluíram.

## Trechos literais

> "We show that the heuristics we learn are able to generalise across different problems and domains, including to domains that were not seen during training." (Resumo)

## Marcações

- `[FATO]` Os STRIPS-HGNs aprendem heurísticas competitivas com LM-cut, medidas pelo número de expansões de nó em A*, generalizando para domínios não vistos no treino (Resumo; Seção 7).
- `[HIPÓTESE]` Uma heurística única que generaliza razoavelmente bem entre domínios (inclusive não vistos) é um contraponto interessante à tese de 2010 de que a escolha de técnica deveria ser feita por domínio (A1/A3): sugere que, ao menos para heurísticas de busca aprendidas, parte do trabalho de "ajuste por domínio" pode estar sendo absorvida pelo próprio processo de aprendizado, reduzindo a necessidade de seleção explícita por características do domínio.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://ojs.aaai.org/index.php/ICAPS/article/download/6754/6608/9983. Conferência humana: pendente.
