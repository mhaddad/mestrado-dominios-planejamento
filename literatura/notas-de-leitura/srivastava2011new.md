---
tipo: nota-de-leitura
eixo: E4
citekey: srivastava2011new
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://people.cs.umass.edu/~immerman/pub/AIJ10.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5]
fragilidades: [F3]
perguntas: [Q2]
---

# A new representation and associated algorithms for generalized planning

**Srivastava, S.; Immerman, N.; Zilberstein, S. · 2011 (recebido em 2010) · Artificial Intelligence 175(2)**
**Link/DOI:** 10.1016/j.artint.2010.10.006

## Extração estruturada

- **Problema:** construir planos generalizados — algoritmos tipo "planos com laços" (*loops*) — que resolvam classes inteiras de instâncias de planejamento clássico de tamanho não limitado, e determinar formalmente as condições sob as quais esses laços terminam e alcançam o objetivo.
- **Método:** framework formal de planejamento generalizado ("planos generalizados baseados em grafo"), construído sobre abstração de três valores (lógica ternária, sistema TVLA de verificação estática de programas), que representa conjuntos de estados com quantidades não limitadas e desconhecidas de objetos por meio de predicados unários e binários (domínios "extended-LL"). O algoritmo Aranda-Learn identifica segmentos de um plano clássico de exemplo que, colocados em laço, fazem progresso mensurável, e calcula as pré-condições sob as quais o plano generalizado é aplicável e correto.
- **Dados/benchmarks:** oito problemas (Delivery, Trucks, Blocks, Green Block, Hall-A, Prize-A em duas configurações, Corner-A), implementados em Python usando TVLA como motor de aplicação de ações; medidas de tempo (rastreamento, busca de laço, cálculo de pré-condições) e de cobertura de domínio (ex.: "≥ 3 itens", "≥ 4 pares de blocos").
- **Resultado principal:** o método computa, para cada problema, planos generalizados com garantias formais de correção e de cobertura mínima de instâncias, em tempos que variam de ~7 a ~89 segundos por problema (predominantemente na fase de rastreamento).
- **Relação com a dissertação de 2010:** obra fundacional citada por quase todos os demais trabalhos deste lote (Ståhlberg et al. 2022, Hofmann e Geffner 2024, Jiménez et al. 2019); oferece uma **representação alternativa de domínio** — predicados lógicos unários/binários sob abstração de três valores — anterior tanto à lógica de descrição quanto às GNNs usadas mais tarde. Quanto a **A5** (diagramas UML medem a complexidade do domínio, e essa complexidade afeta o desempenho da técnica), o artigo **não confirma nem corrige diretamente**, pois não usa UML nem mede "complexidade" no sentido de 2010; mas **oferece uma via concreta e alternativa de caracterização estrutural do domínio** — a classe de predicados exigida (unário vs. binário/"extended-LL") — que determina se a técnica funciona, resposta relevante para **Q2**. Também ataca **F3** de forma indireta: aqui a "métrica" (classe de predicados) é uma propriedade formal do domínio, não uma medida dependente de um modelador humano fazendo um diagrama UML.

## Pontos relevantes para o projeto

- É o trabalho seminal da linha "planejamento generalizado com representação lógica formal", citado como ponto de partida por Ståhlberg et al. (2022) e Hofmann e Geffner (2024) — ajuda a situar cronologicamente a evolução da representação de domínio nesse subcampo (de lógica de três valores, em 2010–2011, até lógica de descrição/C2 e GNNs, em 2018–2022).
- A limitação central admitida pelos próprios autores — abstração restrita a predicados unários pode não capturar todas as propriedades necessárias — antecipa, em linguagem diferente, o mesmo tipo de problema de expressividade insuficiente que Ståhlberg et al. (2022) formalizam depois com a hierarquia C2/C3.
- Trabalha com problemas manualmente formalizados e pequenos (8 problemas), sem crítica de escala equivalente a IPCs completas — situação análoga à amostra pequena de 2010 (**F2**, por analogia, embora não rotulada nas afirmações A).
- Não há qualquer conexão com métricas de diagramas de casos de uso, classes ou estados UML; a "estrutura do domínio" aqui é inteiramente definida por vocabulário lógico (predicados e ações).

## Marcações

- `[FATO]` O framework representa conjuntos de estados com número não limitado de objetos usando abstração de três valores sobre predicados unários e binários (Seção 3, "State abstraction using 3-valued logic").
- `[FATO]` Os autores reconhecem que a abstração baseada em predicados unários pode não capturar todas as propriedades necessárias para medir o progresso de um laço, exigindo, em casos mais complexos, predicados de instrumentação adicionais (Seção 9, "Limitations and future work").
- `[HIPÓTESE]` A escolha entre predicados unários e binários (domínios "extended-LL") funciona, neste trabalho, como um análogo lógico primitivo da discretização de características UML de 2010 — ambos tentam capturar, com vocabulário limitado, a estrutura relevante do domínio para prever a viabilidade de uma técnica.

## Trechos literais

> "we develop a novel approach for computing generalizations of classical plans by identifying sequences of actions that will make measurable progress when placed in a loop." (Resumo)

> "The presented approach is based on abstraction in terms of unary predicates. In some situations, a domain's unary predicates may not capture all the properties necessary for determining the progress made by loops." (Seção 9, "Limitations and future work", p. 29–30)

> "Constructing plans that can handle multiple problem instances is a longstanding open problem in AI." (Resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://people.cs.umass.edu/~immerman/pub/AIJ10.pdf. Conferência humana: pendente.
