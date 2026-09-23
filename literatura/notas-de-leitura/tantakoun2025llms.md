---
tipo: nota-de-leitura
eixo: E5
citekey: tantakoun2025llms
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2503.18971
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A6]
fragilidades: [F4]
perguntas: [Q2, Q3]
---

# LLMs as Planning Formalizers: A Survey for Leveraging Large Language Models to Construct Automated Planning Models

**Tantakoun, M.; Zhu, X.; Muise, C. · 2025 · arXiv**
**Link/DOI:** https://arxiv.org/abs/2503.18971 (10.48550/arxiv.2503.18971)

## Extração estruturada

- **Problema:** mapear sistematicamente a literatura que usa LLMs não como planejadores diretos, mas como **formalizadores** — ferramentas para gerar e refinar especificações de modelos de planejamento (tipicamente PDDL) a partir de linguagem natural, apoiando planejadores clássicos "de prateleira".
- **Método:** revisão de literatura (survey), não um experimento original. Propõe uma taxonomia em três eixos: **Geração de Modelo** (subdividida em Geração de Tarefa — tradução do estado inicial/meta e atribuição de objetos —, Geração de Domínio — construção de predicados e esquemas de ação — e Geração Híbrida — ambas), **Edição de Modelo** (correção/refinamento de código PDDL malformado) e **Benchmarks de Modelo** (avaliação do desempenho de LLMs em tarefas de planejamento e da qualidade das formalizações geradas). Os autores revisam cerca de 80 artigos e também apresentam L2P, uma biblioteca Python própria que reimplementa métodos centrais cobertos pela revisão.
- **Dados/benchmarks:** não há um benchmark único — a obra cataloga múltiplos benchmarks usados na literatura revisada (menciona explicitamente, por exemplo, o Planetarium, benchmark para avaliar tradução de linguagem natural para PDDL). Não reporta um experimento numérico próprio.
- **Resultado principal:** não há um número de desempenho único a reportar (é uma síntese, não um estudo empírico). O achado central é qualitativo: a literatura converge para tratar o LLM como **tradutor/formalizador** (gera ou edita especificações PDDL) em vez de planejador autônomo, exatamente para tirar proveito das garantias de corretude, otimalidade e busca de planejadores clássicos "off-the-shelf" — o papel oposto ao de "LLM-as-Planner", que os autores tratam como abordagem de menor confiabilidade. A obra também identifica como desafios recorrentes na literatura revisada: degradação de desempenho sob *feedback* iterativo autogerado pelo próprio LLM (citando Stechly et al. 2023 e Valmeekam et al. 2023b) e a dependência de orientação textual mínima além do prompt inicial.
- **Relação com a dissertação de 2010:** **A6** [dialoga, sem equivalência direta] — a obra propõe uma taxonomia de *papéis* de LLM em planejamento (formalizador, com subcategorias de geração e edição de modelo) que é organizada por função no processo de planejamento, não por técnica de busca como a taxonomia de técnicas de 2010 (heurística, hierárquica, baseada em conhecimento etc.); não há correspondência direta entre as duas taxonomias, mas ambas compartilham a preocupação de categorizar abordagens para comparação sistemática — relevante para a discussão de F4 (taxonomia de técnicas discutível em 2010) ao mostrar que a comunidade de LLM+planejamento também precisou construir sua própria taxonomia do zero. **A1** [dialoga] — o papel de "formalizador" reafirma implicitamente a importância de representações estruturadas de domínio (como PDDL, e por extensão os modelos UML de 2010/itSIMPLE) mesmo na era dos LLMs, já que o valor do LLM aqui está em produzir essas representações, não em substituí-las.

## Pontos relevantes para o projeto

- É a fonte mais adequada do lote para embasar a resposta à Q3 na dimensão "onde entram os LLMs" de forma ampla e atualizada (2025, ~80 artigos cobertos), complementando os estudos empíricos pontuais das outras obras do lote.
- A taxonomia de três eixos (Geração de Modelo, Edição de Modelo, Benchmarks de Modelo) pode servir de estrutura para organizar a seção da revisão sobre papéis de LLM em planejamento, junto com a taxonomia por papel (planejador, tradutor, heurística, verificador) usada nas outras notas deste lote.
- Não fornece dados quantitativos por domínio de planejamento (por não ser um estudo empírico), então não alimenta diretamente a comparação por domínio pedida para A3/A5 — isso deve ficar explícito ao usar esta obra, para não confundir com as obras empíricas do mesmo eixo.
- Cita explicitamente, como referências de apoio à ideia de que autocrítica de LLM degrada desempenho, os mesmos trabalhos de Stechly et al. e Valmeekam et al. já lidos neste lote — permite checar consistência de citação cruzada dentro do próprio corpus da revisão.

## Marcações

- `[FATO]` "This paper aims to provide a timely survey of the current research... positioning LLMs as tools for formalizing and refining planning specifications to support reliable off-the-shelf AP planners" (resumo/abstract).
- `[FATO]` "Our survey's taxonomy is divided into three key areas: Model Generation... Model Editing... Finally, Model Benchmarks... encompass assessments of both the performance of LLMs in planning tasks and the quality of LLM-generated planning formalizations" (seção 1, Introdução).
- `[HIPÓTESE]` Como survey, esta obra não permite, por si só, sustentar afirmações numéricas sobre desempenho por domínio; qualquer número citado a partir dela deveria ser rastreado até o estudo empírico original que ela referencia, não citado como se fosse resultado próprio.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2503.18971 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
