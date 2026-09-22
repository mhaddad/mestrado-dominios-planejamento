---
tipo: nota-de-leitura
eixo: E6
citekey: vaquero2013itsimple
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://tidel.mie.utoronto.ca/pubs/KERtvaquero.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: [F3]
perguntas: [Q1]
---

# itSIMPLE: Towards an Integrated Design System for Real Planning Applications

**Vaquero, T. S.; Silva, J. R.; Tonidandel, F.; Beck, J. C. · 2013 (The Knowledge Engineering Review) · Cambridge Core**
**Link/DOI:** https://www.cambridge.org/core/journals/knowledge-engineering-review/article/abs/itsimple-towards-an-integrated-design-system-for-real-planning-applications/0121A24A18344F1E86B279BCB76DAA45 (10.1017/s0269888912000434)

## Extração estruturada

- **Problema:** como apoiar sistematicamente as fases iniciais de projeto de aplicações reais de planejamento automatizado — elicitação e engenharia de requisitos, análise e transformação em um modelo pronto para os planejadores — que exigem conhecimento e engenharia mais elaborados do que problemas acadêmicos típicos.
- **Método:** apresenta o itSIMPLE, ambiente que integra três representações mínimas: **UML** (diagramas de classe, máquina de estados, *timing* e objeto, mais OCL para pré/pós-condições) para elicitação e modelagem de requisitos; **Redes de Petri** (Redes de Petri Elementares) geradas automaticamente a partir do modelo UML para análise dinâmica (checagem de vivacidade); e **PDDL** (até a versão 3.1), também gerada automaticamente do modelo UML, para comunicação com planejadores externos e simulação/validação de planos. Não é um estudo experimental controlado; é um artigo de ferramenta/sistema com relato de três estudos de caso reais.
- **Dados/benchmarks:** três aplicações reais relatadas como estudos de caso, não domínios de IPC: (1) planejamento e escalonamento de distribuição de petróleo bruto no Porto de São Sebastião (SP) — modelo com 9 tipos de objeto, 20 predicados, 26 funções, 11 esquemas de ação, instâncias diárias com até 13 navios-tanque, 4 píeres, 18 tanques, 14 tipos de óleo; (2) planejamento de atividades de desenvolvimento de software (*Lean Software Development*) — modelo com 15 tipos de objeto, 26 predicados, 8 operadores, instâncias com até 50 pessoas e 80 versões de *software*, planos com até 567 ações; (3) sequenciamento de carros em linha de montagem inspirado na RENAULT — modelo com 7 tipos, 11 predicados, 12 funções, 5 ações complexas.
- **Resultado principal:** não há métrica de cobertura como em 2010; o resultado é qualitativo/de engenharia. O texto relata (citando um trabalho anterior dos mesmos autores, Vaquero et al. 2010, não lido nesta nota) que "a disciplined modeling phase and a careful plan analysis process in itSIMPLE can significantly improve plan quality and increase planning speed of up to three order[s] of magnitude" em comparação a especificação direta em PDDL. A conclusão central do próprio artigo é que especificação direta em PDDL não é viável para aplicações reais complexas, por não suportar engenharia de conhecimento nem elicitação de requisitos, e que o processo disciplinado UML→Rede de Petri→PDDL supre essa lacuna.
- **Relação com a dissertação de 2010:** **A1** [contexto direto] — este artigo descreve exatamente a ferramenta (itSIMPLE) e a cadeia de representações (UML → PDDL) que HADDAD (2010) usa para extrair as métricas estruturais de domínio; é a fonte primária metodológica do instrumento de medição usado em 2010, não um teste da tese A1 em si. **F3** [ilumina a fragilidade] — o artigo é explícito sobre o fato de que a modelagem em UML é um processo de engenharia de requisitos guiado por especialistas humanos ("focus on identifying the domain objects and ensure that all the system logic is..."), o que reforça, com a voz dos próprios criadores da ferramenta, a fragilidade F3 de 2010 (métricas UML dependem do modelador) — a obra não discute isso como limitação, mas descreve o processo de forma que torna essa dependência evidente.

## Pontos relevantes para o projeto

- É a versão de periódico (mais completa e citável) da linha de trabalhos sobre itSIMPLE, a ferramenta central usada na metodologia de 2010; útil para a seção de método da revisão ao descrever com precisão o que o itSIMPLE faz e não faz.
- Os três estudos de caso são aplicações reais de grande porte (não domínios de IPC), o que contrasta com os 10+3 domínios de IPC usados em 2010 — pode ser citado para discutir a diferença entre "complexidade de domínio acadêmico" e "complexidade de domínio real" na revisão.
- O número "até três ordens de magnitude" de ganho de velocidade de planejamento vem de uma citação interna a outro artigo dos mesmos autores (Vaquero et al. 2010), não é um resultado gerado neste artigo — registrado aqui como achado relatado, não verificado na fonte primária; se a revisão quiser usar esse número, precisa localizar e ler Vaquero et al. (2010) separadamente.
- Descreve o objetivo de trabalho futuro de estender os tipos de diagrama UML suportados (diagramas de atividade, decomposição hierárquica de ações) — pista de evolução da ferramenta que pode ser relevante para T1 (extração automática das métricas no itSIMPLE), embora este artigo não trate de automação de extração de métricas propriamente dita.

## Marcações

- `[FATO]` "itSIMPLE, therefore, translates the entire model described in UML to a solver-ready PDDL representation" (seção 1, Introdução).
- `[FATO]` "the work (Vaquero et al. 2010) has shown that a disciplined modeling phase and a careful plan analysis process in itSIMPLE can significantly improve plan quality and increase planning speed of up to three order of magnitude" (seção 4, "An Overview of Practical Results") — resultado atribuído a outra publicação, não demonstrado neste artigo.
- `[HIPÓTESE]` Como o itSIMPLE é a própria ferramenta usada para extrair as métricas de 2010, uma leitura de Vaquero et al. (2006, 2009b, 2010) — citados aqui como as fontes primárias dos estudos de caso e do resultado de "três ordens de magnitude" — poderia ajudar a verificar diretamente a fragilidade F3 (dependência do modelador) com mais profundidade do que este artigo de visão geral permite.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://tidel.mie.utoronto.ca/pubs/KERtvaquero.pdf (o lote não trazia `texto_integral_url`; localizei esta cópia aberta via busca web, hospedada pelo grupo de pesquisa TIDEL da Universidade de Toronto, com título e autoria idênticos ao registro do lote — PDF extraído com pdftotext). Conferência humana: pendente.
