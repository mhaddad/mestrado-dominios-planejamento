---
tipo: nota-de-leitura
eixo: E6
citekey: simpson2000knowledge
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: http://eprints.hud.ac.uk/id/eprint/2239/1/trans.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: [F3]
perguntas: []
---

# Knowledge Representation in Planning: A PDDL to OCLh Translation

**R. M. Simpson, T. L. McCluskey, D. Liu, D. E. Kitchin · 2000 · Foundations of Intelligent Systems (ISMIS 2000), Springer, p. 610–618**
**Link/DOI:** http://eprints.hud.ac.uk/id/eprint/2239/1/trans.pdf · DOI: 10.1007/3-540-39963-1_64

## Extração estruturada

- **Problema:** PDDL é uma linguagem de troca de domínios entre grupos de pesquisa, não uma linguagem de modelagem; faltava uma ferramenta que traduzisse modelos PDDL para OCLh, uma linguagem orientada a objeto (sorts, substates, transições de objeto) desenvolvida especificamente para modelagem e validação de domínios de planejamento.
- **Método:** descrevem e implementam um algoritmo de tradução de dois passos de PDDL (operadores STRIPS com literais tipados) para OCLh. O primeiro passo identifica, para cada predicado, um único "sort" (classe de objeto) que "possui" aquele predicado (resolvendo o "frame problem" de atribuição de predicados relacionais a mais de um sort), induz classes de substates a partir dos efeitos dos operadores PDDL, e gera transições de objeto e cláusulas de "prevail" (pré-condições persistentes). Aplicam o tradutor a domínios de exemplo (Tyre World, Gripper World) e comparam o resultado com modelos OCLh construídos manualmente.
- **Dados/benchmarks:** domínios de exemplo PDDL (Tyre World — 13 ações — e Gripper World); sem avaliação de desempenho de planejadores, apenas comparação estrutural entre tradução automática e modelagem manual em OCLh.
- **Resultado principal:** a tradução automática de primeiro passo produz resultados próximos aos modelos traduzidos manualmente, mas revela inconsistências e "insegurenças" (insecurities) na codificação PDDL original — por exemplo, no domínio Tyre World, a ação jack_down é traduzida de forma operacionalmente correta mas semanticamente incompleta (a transição do macaco/jack não caracteriza corretamente seu estado anterior), e o predicado on_ground(H) é tratado como substate completo do hub quando, na verdade, depende também de fastened(H)/unfastened(H). Das treze ações do Tyre World, oito continham negações desnecessárias (mas corretas) e duas tinham transições de objeto incompletas.
- **Relação com a dissertação de 2010:** o artigo é uma linha paralela (McCluskey/Huddersfield, OCLh) à linha itSIMPLE (Vaquero/Tonidandel/Silva, UML) na tradução entre PDDL e modelagem orientada a objeto — ambas nascem da mesma premissa de que PDDL, por si, não é uma boa linguagem de modelagem. É relevante para [F3]: mostra concretamente que o processo de tradução PDDL→modelo-orientado-a-objeto pode introduzir ambiguidades (escolha de qual sort "possui" um predicado; substates incompletos) que dependem de decisões do tradutor/modelador, e não apenas do domínio — reforçando que qualquer métrica extraída do modelo orientado a objeto (UML ou OCLh) herda essa dependência do processo de construção, não apenas do problema original.

## Pontos relevantes para o projeto

- Documenta, com exemplo concreto (ação jack_down do Tyre World), como a tradução de PDDL para uma representação orientada a objeto pode ser "operacionalmente correta mas conceitualmente inadequada" — achado diretamente relevante para qualquer alegação de que métricas extraídas de diagramas UML capturam de forma neutra a complexidade "real" do domínio.
- A "frame problem" que resolvem (a quem atribuir um predicado relacional, como in(tool,container), entre os sorts referenciados) é a mesma decisão de modelagem que qualquer tradutor PDDL→UML (como o do itSIMPLE) precisa tomar — e os autores mostram que a escolha muda a completude do modelo resultante.
- É um antecedente direto e contemporâneo de [@tonidandel2006reading] (2006, itSIMPLE) e de [@mccluskey1997engineering] (1997), formando com eles uma linha coerente de pesquisa em Huddersfield sobre modelagem orientada a objeto para planejamento, útil para a seção de trabalhos relacionados.
- Ferramenta de tradução funciona como instrumento de *validação* do PDDL original (revela inconsistências), não como gerador de métricas de complexidade — distinção importante ao posicionar esta obra frente às métricas UML de 2010, que usam a UML para medir, não para validar.

## Trechos literais

- "We describe a prototype implementation of a translation algorithm between two languages used in planning representation: PDDL, a language used for communication of example domains between research groups, and OCLh, a language developed specifically for planning domain modelling." (Abstract)
- "The tool performs well when its output is measured against hand-crafted OCLh models, but more importantly, we show how it has helped uncover insecurities in PDDL encodings." (Abstract)

## Marcações

- `[FATO]` A tradução automática de PDDL para OCLh revelou, no domínio Tyre World, uma transição de objeto semanticamente inadequada para a ação jack_down (o estado do "jack" antes da ação não é corretamente restringido) e um substate incompleto para o hub (Seção 5.2, "Translation Results").
- `[FATO]` Das 13 ações do Tyre World, 8 apresentaram negações desnecessárias (porém corretas) e 2 apresentaram transições de objeto incompletas na tradução de primeira passada (Seção 5.2).
- `[HIPÓTESE]` (minha interpretação) Como a atribuição de "posse" de um predicado a um sort é uma escolha do algoritmo/modelador (não determinada univocamente pelo domínio), o mesmo tipo de grau de liberdade provavelmente existe na tradução PDDL↔UML do itSIMPLE usada em 2010 — o que apoiaria [F3] caso confirmado na leitura direta da linha itSIMPLE (a verificar em [@tonidandel2006reading], cuja leitura de texto integral não foi possível neste lote).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em http://eprints.hud.ac.uk/id/eprint/2239/1/trans.pdf (extração de texto corrompida por fonte customizada do PDF original; leitura feita página a página via renderização de imagem). Conferência humana: pendente.
