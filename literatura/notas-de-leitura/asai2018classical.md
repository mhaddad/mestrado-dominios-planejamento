---
tipo: nota-de-leitura
eixo: E4
citekey: asai2018classical
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/AAAI/article/download/12077/11936
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: [F2]
perguntas: [Q2]
---

# Classical Planning in Deep Latent Space: Bridging the Subsymbolic-Symbolic Boundary

**Asai, M.; Fukunaga, A. · 2018 · Proceedings of AAAI 2018**
**Link/DOI:** 10.1609/aaai.v32i1.12077

## Extração estruturada

- **Problema:** planejadores clássicos exigem um modelo simbólico (PDDL) fornecido por um humano, gerando o chamado "gargalo de aquisição de conhecimento" (*knowledge acquisition bottleneck*). O artigo pergunta se é possível construir automaticamente essa representação simbólica a partir de dados subsimbólicos não rotulados (imagens).
- **Método:** LatPlan, arquitetura com três componentes: (1) *State Autoencoder* (SAE), um autoencoder variacional que aprende uma representação proposicional discreta (espaço latente) a partir de pares de imagens de transições válidas do ambiente; (2) *Action Model Acquisition* (AMA), que agrupa transições em símbolos de ação e aprende implicitamente pré-condições/efeitos, usando aprendizado PU (*Positive-Unlabeled*) para lidar com a ausência de exemplos negativos explícitos; (3) um planejador simbólico convencional (A*) que resolve o problema no espaço latente aprendido, cuja solução é depois decodificada de volta em imagens.
- **Dados/benchmarks:** versões baseadas em imagem de três domínios "de brinquedo": 8-puzzle (com dígitos MNIST e outras texturas), Torres de Hanói e LightsOut; 100 instâncias por domínio e tipo de ruído, com passeios aleatórios de 7 (benchmark A) ou 14 passos (benchmark B) a partir do estado-objetivo.
- **Resultado principal:** LatPlan resolve a maioria das instâncias mesmo sob ruído de entrada (Gaussiano ou sal-e-pimenta); as falhas remanescentes vêm sobretudo de *timeout*, causado pela lentidão da função sucessora baseada em redes neurais, não de erros de planejamento em si (Tabela 1).
- **Relação com a dissertação de 2010:** não toca diretamente nenhuma afirmação A1–A8 de 2010 (não usa domínios de planejamento clássico com PDDL nomeado, não compara técnicas de busca entre si — usa A* como único planejador simbólico após a conversão), mas é a resposta mais radical do lote a **T1** (extração automática de métricas do domínio, proposta em 2010 para o itSIMPLE): em vez de extrair métricas estruturais de um modelo UML feito por humano, LatPlan elimina inteiramente a necessidade de modelagem humana, aprendendo toda a representação simbólica (estados e ações) diretamente de imagens não rotuladas. É uma prova de conceito — não uma comparação de técnicas de planejamento — e por isso não permite avaliar A1/A3/A5; sua relevância para 2010 é mais metodológica do que substantiva. **F2** (amostra pequena) se aplica plenamente: apenas três domínios pequenos e sintéticos, sem qualquer IPC real.

## Pontos relevantes para o projeto

- Representa o domínio por um **espaço latente aprendido** (vetor discreto via Gumbel-Softmax), convertido automaticamente em um modelo PDDL — a quarta forma de representação de domínio observada neste lote (ao lado de grafo ação-proposição, lógica de descrição/GNN e lógica de três valores), diretamente relevante para o enquadramento de Q2 pedido para este eixo E4.
- É citado pela própria literatura da área (ex.: Ståhlberg et al. 2022 mencionam Asai 2019 como trabalho relacionado de aprendizado de predicados de domínio) como ponto de referência da linha "aprender a representação simbólica em si", distinta da linha "aprender a política/heurística dado o modelo simbólico" que domina os demais trabalhos do lote.
- Assume explicitamente que o domínio é totalmente observável e determinístico — as mesmas premissas simplificadoras da dissertação de 2010 — mas não faz nenhuma afirmação sobre relação entre características estruturais do domínio e desempenho de técnicas de busca, pois usa sempre o mesmo planejador (A*) após a conversão.
- Não há qualquer teste de escalabilidade a domínios de tamanho realista ou a IPCs; os autores reconhecem isso como trabalho futuro.

## Trechos literais

> "LatPlan finds a plan to the goal state in a symbolic latent space and returns a visualized plan execution." (Resumo)

> "This results in the knowledge-acquisition bottleneck, where the modeling step is sometimes the bottleneck in the problem-solving cycle." (Introdução, p. 6094)

> "The only key assumptions about the input domain we make are that (1) it is fully observable and deterministic and (2) NNs can learn from the available data." (Seção 8, "Discussion and Conclusion", p. 6100)

## Marcações

- `[FATO]` LatPlan resolve as instâncias testadas usando exclusivamente um planejador simbólico A* após converter o problema para o espaço latente; nenhuma outra técnica de busca é comparada (Seção 6, "Evaluation").
- `[FATO]` Os autores identificam a lentidão da função sucessora neural (muitas chamadas à rede *feedforward*) como a principal causa de falha por *timeout* (Seção 6, p. 6099).
- `[HIPÓTESE]` Se a extração automática de representação (T1 de 2010) evoluir na direção de LatPlan, a pergunta de 2010 sobre "quais características do domínio predizem a técnica" pode se transformar em "que espaço latente aprendido é mais preditivo" — um reenquadramento de Q2 que ainda carece de teste em domínios de escala realista.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/AAAI/article/download/12077/11936. Conferência humana: pendente.
