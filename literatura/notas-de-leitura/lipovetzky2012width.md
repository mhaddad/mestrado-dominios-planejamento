---
tipo: nota-de-leitura
eixo: E3
citekey: lipovetzky2012width
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://gwern.net/doc/reinforcement-learning/model/2012-lipovetzky.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A2, A6]
fragilidades: [F4]
perguntas: [Q2]
---

# Width and Serialization of Classical Planning Problems

**Lipovetzky, N.; Geffner, H. · 2012 · ECAI**
**Link/DOI:** 10.3233/978-1-61499-098-7-540

## Extração estruturada

- **Problema:** definir uma noção de *width* (largura) que limite a complexidade de problemas e domínios de planejamento clássica, e explorar seu valor prático para construir planejadores eficientes.
- **Método:** define o parâmetro de largura sobre grafos cujos vértices são tuplas de até *m* átomos; propõe o algoritmo de busca cega em largura iterativa e podada IW (*Iterated Width*), que roda em tempo exponencial na largura do problema; estende a ideia para serializar metas conjuntivas em subproblemas (algoritmo SIW).
- **Dados / benchmarks:** domínios de referência (*benchmark domains*) do planejamento clássico, com metas restritas a átomos únicos e metas conjuntivas.
- **Resultado principal:** muitos domínios de referência têm largura pequena e limitada quando as metas são restritas a átomos únicos, tornando-os solúveis em tempo polinomial baixo; o planejador cego SIW (que usa IW para serializar e resolver subproblemas) é competitivo com um planejador de busca *best-first* guiado por heurísticas de estado da arte, e a noção de novidade derivada da largura pode ser integrada a técnicas de planejamento existentes para um planejador com desempenho de estado da arte.
- **Relação com a dissertação de 2010:** este artigo **introduz** a família de técnicas baseada em largura (*width-based search*, origem do BFWS), **ausente da taxonomia de seis famílias** de HADDAD (2010) em A2/A6 (*Heuristic Search*, *Hierarchical*, *Knowledge-based*, *Forward-chaining*, *Plan-Space*, *Total-order*). Isso **torna obsoleta** parcialmente a lista de A2 para o período pós-2012, pois uma família de técnicas relevante e influente (dá origem a planejadores premiados nas IPCs seguintes) não é contemplada — reforça F4 (taxonomia discutível). Não trata diretamente de métricas estruturais de domínio no sentido de HADDAD (2010) (Q2), mas define uma métrica de complexidade de domínio alternativa (a largura) que poderia, em princípio, ser comparada às métricas de diagrama UML de 2010.

## Pontos relevantes para o projeto

- Introduz uma família de técnica de busca (largura/novidade) inteiramente ausente na taxonomia A2/A6 de 2010, essencial para atualizar F4.
- A noção de largura é, ela própria, uma métrica de complexidade de domínio — pode ser comparada (não medida aqui) à abordagem de HADDAD (2010) de usar métricas de diagramas UML para caracterizar complexidade de domínio (A5).
- O algoritmo SIW é citado por trabalhos futuros de aprendizado de heurísticas (ex.: chen2024learning, chen2024return, deste mesmo lote), mostrando sua influência contínua na literatura de planejamento.

## Trechos literais

- "We introduce a width parameter that bounds the complexity of classical planning problems and domains, along with a simple but effective blind-search procedure that runs in time that is exponential in the problem width." (resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://gwern.net/doc/reinforcement-learning/model/2012-lipovetzky.pdf (resumo, introdução e seção de discussão/conclusão). Conferência humana: pendente.
