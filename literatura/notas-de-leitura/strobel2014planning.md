---
tipo: nota-de-leitura
eixo: E6
citekey: strobel2014planning
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: PDF fornecido pelo autor em 23/09/2026 (versão dos autores; a nota de rodapé do título remete à versão final na Springer, DOI 10.1007/978-3-319-11206-0_27)
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [T1]
fragilidades: [F3]
perguntas: [Q2]
---

# Planning in the Wild: Modeling Tools for PDDL

**Strobel, V.; Kirsch, A. · 2014 · KI 2014: Advances in Artificial Intelligence, LNCS, p. 273-284 (Springer)**
**Link/DOI:** 10.1007/978-3-319-11206-0_27

## Extração estruturada

- **Problema:** escrever e manter domínios e problemas em PDDL é difícil, demorado e sujeito a erro, em parte por falta de ferramentas de engenharia; isso dificulta levar o planejamento para sistemas reais.
- **Método:** propõe o myPDDL, conjunto modular de ferramentas sobre o editor Sublime Text: realce de sintaxe sensível ao contexto (até PDDL 3.1), modelos de código, gerador de estrutura de projeto, gerador de diagrama de tipos, pré-processador de distâncias e interface com a linguagem Clojure. Usa como critérios de projeto os sete critérios de ferramentas de engenharia do conhecimento de Shah et al. (2013).
- **Dados / benchmarks:** comparação de funcionalidades com PDDL Studio, itSIMPLE e o modo PDDL do Emacs (Tabela 1); teste com 8 usuários sem experiência em PDDL, em desenho intra-sujeitos.
- **Resultado principal:** com o realce de sintaxe, os participantes encontraram em média 10,3 erros, contra 7,6 sem ele (cerca de 36% a mais); com o diagrama de tipos, responderam quatro de cinco perguntas cerca de duas vezes mais rápido; a nota de usabilidade (SUS) foi 89,6, com desvio padrão de 3,9. A amostra é pequena, e os próprios autores a justificam pela prática de testes de usabilidade.
- **Relação com a dissertação de 2010:**
  - **T1 [informa]:** `[FATO]` o artigo afirma que o fluxo do itSIMPLE é unidirecional (mudanças no PDDL não voltam para a UML), que os modelos UML têm de ser feitos à mão e que a tradução de PDDL para UML.P de Tonidandel, Vaquero e Silva (`tonidandel2006reading`) **não estava incluída** na versão do itSIMPLE da época. `[HIPÓTESE]` Para extrair automaticamente as métricas UML dos domínios PDDL na Fase 3, será preciso reimplementar essa tradução, e não apenas usar a ferramenta.
  - **F3 [contexto]:** o artigo retoma o critério de "operacionalidade" de Shah et al. — se o modelo gerado melhora o desempenho do planejamento — e declara que sua ferramenta não pretende afetá-lo. Mostra que a própria literatura de engenharia do conhecimento trata a qualidade do modelo como algo que pode afetar o desempenho, em linha com `vallati2021importance`.

## Pontos relevantes para o projeto

- Cita "Knowledge engineering tools in planning: State-of-the-art and future challenges" (Shah et al., KEPS 2013), a revisão de ferramentas que a busca da Fase 1 não conseguiu localizar como semente do eixo E6. A referência completa está na lista do artigo e pode orientar uma nova busca.
- Descreve as limitações da tradução de 2006 com as mesmas convenções anotadas em `tonidandel2006reading`: primeiro parâmetro vira subclasse de `Agent`, predicados até aridade 2.
- Confirma, de fora do grupo do itSIMPLE, que a UML.P é uma variante de UML específica para planejamento proposta no caminho do itSIMPLE.

## Marcações

- `[FATO]` Com realce de sintaxe, 10,3 erros encontrados em média contra 7,6 sem (seção 4.2.2); SUS de 89,6 (desvio padrão de 3,9); 8 participantes.
- `[FATO]` A tradução de PDDL para UML não estava na versão do itSIMPLE descrita pelos autores (seção 2).
- `[HIPÓTESE]` A falta de caminho de volta de PDDL para UML na ferramenta explica por que as métricas de 2010 foram contadas à mão em modelos feitos à mão.

## Trechos literais

1. "itSimple's modeling workflow is unidirectional as changes in the pddl domain do not affect the uml model and uml models have to be modeled manually, meaning that they cannot by generated from pddl." (seção 2)
2. "The currently version of itSimple does not include the translation process from pddl to uml." (seção 2)
3. "on average participants found 7.6 errors without syntax highlighting and 10.3 errors with syntax highlighting" (seção 4.2.2)

## Uso de IA nesta nota

Claude Code, Coordenador (claude-opus-5-5), 23/09/2026. Leitura do texto integral da versão dos autores, fornecida pelo autor. A versão lida declara que a publicação final está na Springer (mesmo artigo). Conferência humana: pendente.
