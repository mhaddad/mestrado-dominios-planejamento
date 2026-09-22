---
tipo: nota-de-leitura
eixo: E6
citekey: vaquero2005itsimple
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: PDF fornecido pelo autor em 22/09/2026 (The_itSIMPLE_tool_for_Modeling_Planning_Domains.pdf)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A5, A8]
fragilidades: [F3]
perguntas: [Q2]
---

# The itSIMPLE tool for Modeling Planning Domains

**Vaquero, T. S.; Tonidandel, F.; Silva, J. R. · 2005 · documento com copyright da AAAI; o texto diz que a ferramenta foi proposta à ICKEPS. Veículo exato `[A CONFIRMAR]`**
**Link/DOI:** sem DOI localizado (Crossref não tem registro). Cópia em PDF fornecida pelo autor.

## Extração estruturada

- **Problema:** dar aos engenheiros de conhecimento um ambiente integrado para modelar domínios de planejamento em linguagem familiar (UML), validar o comportamento estático e dinâmico do modelo e exportá-lo para PDDL, reduzindo a distância entre aplicações reais e domínios de planejamento.
- **Método:** ferramenta (itSIMPLE) que encadeia três representações — UML para a modelagem, XML como formato interno e ponte, redes de Petri para a análise dinâmica — e gera PDDL a partir do XML. A modelagem UML tem estrutura fixa com as classes `Planner`, `Environment` e `Agent`; diagramas de classes definem tipos, predicados e operadores; diagramas de estados definem pré e pós-condições; diagramas de objetos (*snapshots*) definem os estados inicial e objetivo.
- **Dados / benchmarks:** não há avaliação empírica. São exemplos de modelagem: Elevator (Figura 2), Logistics (Figuras 3 a 5) e Blocks World (Figuras 6 a 10, incluindo o esquema em rede de Petri do problema de três blocos).
- **Resultado principal:** versão preliminar da ferramenta, com a tradução UML → XML → PDDL funcionando e a análise por redes de Petri ainda por implementar. As regras de tradução são explícitas: cada atributo booleano e cada associação do diagrama de classes viram predicados; classes e generalizações viram tipos; operadores viram ações; o estado de origem de uma ação dá pré-condições e lista de exclusão, o estado de destino dá pós-condições e lista de inclusão.
- **Relação com a dissertação de 2010:**
  - **A1 e A5 [antecedente direto, confirma a origem da pergunta]:** a intenção de usar características extraídas do modelo para escolher a técnica de planejamento **já é um objetivo declarado do projeto itSIMPLE em 2005**, cinco anos antes da dissertação, em duas passagens (seção "Why Petri Nets?" e conclusão). A dissertação de 2010 é, nesse sentido, a execução de um alvo que os autores da ferramenta tinham anunciado — mas por métricas de diagramas UML, não pela análise em redes de Petri que o artigo projetava.
  - **A8 [corrige a revisão de 2010]:** a seção de trabalhos relacionados de 2010 cita apenas Hoffmann (2001) e Gerevini, Saetti e Serina (2004). Este artigo, da própria ferramenta usada na dissertação, enuncia a mesma ideia e não aparece na revisão.
  - **F3 [explica a contagem de classes]:** a estrutura obrigatória do itSIMPLE inclui as classes `Planner`, `Environment` e `Agent`, que existem em todo modelo e não descrevem o domínio. Isso dá base documental à hipótese, levantada na Fase 0 (achado G2), de que a contagem de classes de 2010 excluiu classes auxiliares: parte delas é imposta pela ferramenta, não escolhida pelo modelador.
  - **Q2 [define o que as métricas medem]:** o artigo mostra o mapeamento elemento a elemento entre UML e PDDL. Isso delimita quais métricas UML têm contrapartida em PDDL (atributos e associações → predicados; classes e generalizações → tipos; operadores → ações) e quais não têm (agregação, composição, multiplicidade, diagramas de estados além de pré e pós-condições).

## Pontos relevantes para o projeto

- O Elevator, um dos três domínios de validação de 2010, aparece aqui como exemplo de modelagem em UML (Figura 2), com as classes `Building`, `Floor`, `Elevator` e `Passenger`.
- A tradução de associações em predicados usa o atributo `navigation` para decidir a ordem dos parâmetros: a direção da associação, que é escolha do modelador, muda o PDDL gerado.
- O artigo reconhece que "pure UML does not fit all structures in PDDL language" e que regras para fluentes foram inseridas *ad hoc* no tradutor — limitação da ponte UML→PDDL que vale registrar ao discutir a Q2.
- A análise por redes de Petri, apresentada como caminho para extrair padrões do domínio, aparece só como esquema desenhado à mão no exemplo do Blocks World; o editor de redes de Petri não estava implementado.

## Marcações

- `[FATO]` (o que o artigo mostra): o objetivo de classificar características de domínio para escolher técnica ou heurística é declarado em 2005 pelos autores do itSIMPLE.
- `[FATO]`: a estrutura UML do itSIMPLE impõe as classes `Planner`, `Environment` e `Agent`.
- `[HIPÓTESE]` (minha interpretação): a escolha da dissertação de 2010 por métricas de diagramas, em vez da análise em redes de Petri projetada aqui, pode ter sido pragmática (as métricas são contáveis à mão; o editor de redes de Petri não existia). Confirmar com o autor.

## Trechos literais

1. "We also hope that with the Petri Nets model we can extract enough information and patterns to decide which heuristic, or which planning technique, can be used in each domain." (seção "Why Petri Nets?", p. 3)
2. "And a more distant target which is the classification of domain features, extracted from the domain analyses, in order to decide which kind of planning technique or heuristic suits better the proposed domain." (seção "Conclusion and Future Works", p. 8)
3. "The itSIMPLE permits to model planning environments in UML by defining a general structure composed by Agents, a domain Environment and a Planner." (seção "Why UML?", p. 2)

## Uso de IA nesta nota

Claude Code, Coordenador (claude-opus-5), 22/09/2026. Leitura do texto integral do PDF fornecido pelo autor. Conferência humana: pendente. A reclassificação deste item (estava excluído como X1 na triagem) é decisão do Coordenador, registrada em `literatura/protocolo/triagem.csv` e no log de QC.
