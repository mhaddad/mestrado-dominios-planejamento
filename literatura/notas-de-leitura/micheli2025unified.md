---
tipo: nota-de-leitura
eixo: E6
citekey: micheli2025unified
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://andrea.micheli.website/papers/up_softwarex.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: []
perguntas: []
---

# Unified Planning: Modeling, manipulating and solving AI planning problems in Python

**Andrea Micheli, Arthur Bit-Monnot, Gabriele Röger, Enrico Scala, Alessandro Valentini, Luca Framba, Alberto Rovetta, Alessandro Trapasso, Luigi Bonassi, Alfonso Emilio Gerevini, Luca Iocchi, Felix Ingrand, Uwe Köckemann, Fabio Patrizi, Alessandro Saetti, Ivan Serina, Sebastian Stock · 2025 (publicado online em 2024) · SoftwareX, v. 29, art. 102012**
**Link/DOI:** https://andrea.micheli.website/papers/up_softwarex.pdf · DOI: 10.1016/j.softx.2024.102012 (acesso aberto, CC BY 4.0)

## Extração estruturada

- **Problema:** aplicar planejamento automatizado na prática é difícil porque (i) modelar um problema real como tarefa de planejamento exige lidar com linguagens de descrição específicas (PDDL, ANML) usualmente escritas à mão, e (ii) cada motor de planejamento tem instruções próprias de instalação e uso, com fragmentos de expressividade distintos — tornando difícil para o usuário saber qual planejador serve ao seu problema.
- **Método:** artigo de publicação de software (SoftwareX). Descrevem a arquitetura da biblioteca Unified Planning (UP), desenvolvida no projeto europeu AIPlan4EU: uma API Python que permite modelar problemas de planejamento programaticamente (Classical, Numeric, Temporal, Scheduling, Multi-Agent, Hierarchical, Task and Motion Planning, Contingent), com um sistema de "flags" (ProblemKind) que descreve os recursos de modelagem usados em cada problema, permitindo que a biblioteca selecione automaticamente motores de planejamento compatíveis via um sistema de plugins.
- **Dados/benchmarks:** não é um estudo experimental comparativo; ilustram a API com um exemplo de robô movendo-se em um grafo (numeric planning) e reportam métricas de adoção do projeto (194 estrelas e 42 forks no GitHub no momento da escrita).
- **Resultado principal:** a biblioteca UP unifica o acesso a múltiplos motores de planejamento por meio de "Operation Modes" padronizados (OneshotPlanner, PlanValidator, SequentialSimulator, Compiler, AnytimePlanner, Replanner, PlanRepairer, PortfolioSelector), desacoplando a modelagem do problema da escolha de um planejador específico, e já foi usada para integrar planejamento em plataformas robóticas e em pipelines de IA europeias.
- **Relação com a dissertação de 2010:** é uma obra de infraestrutura moderna do eixo E6 (não trata diretamente de A1–A8, F1–F7 ou Q1–Q4), mas na seção de trabalhos relacionados cita explicitamente o itSIMPLE como ferramenta de aquisição de modelos: "The model acquisition tool itSIMPLE [12] allows modeling tasks in the diagram-based UML language, and provides analyses based on Petri nets." Isso confirma, por fonte terceira e independente (2024), que o itSIMPLE segue sendo reconhecido na literatura atual como a ferramenta de referência para modelagem UML de domínios de planejamento, e que suas análises históricas se apoiam em redes de Petri (não nas métricas estruturais de diagramas usadas na dissertação de 2010) — relevante como contexto para [T1] (extração automática de métricas no itSIMPLE), mas sem detalhar quais métricas ou análises o itSIMPLE oferece.

## Pontos relevantes para o projeto

- Confirma que o itSIMPLE segue ativo como referência na literatura de ferramentas de modelagem para planejamento (citado ao lado de Tarski, PDDL4J, planning.domains, planutils), útil para justificar a atualidade da linha itSIMPLE no eixo E6.
- A observação de que o itSIMPLE "provides analyses based on Petri nets" (não mencionada nas outras notas deste lote) é um dado novo sobre a ferramenta, a verificar com leitura direta da linha itSIMPLE original (Vaquero et al.), já que esta obra não detalha o mecanismo.
- O sistema de "flags"/ProblemKind da UP é um paralelo interessante, em espírito, à ideia de caracterizar domínios por conjuntos de features — mas opera sobre a linguagem de modelagem (quais construtos PDDL/ANML são usados), não sobre métricas estruturais do domínio como em 2010; útil como contraste conceitual para [Q2], sem ser evidência direta.
- Projeto de infraestrutura ativa (AIPlan4EU, Horizon 2020) mostra o estado da arte de ferramentas de modelagem em Python como alternativa moderna às linguagens de descrição tradicionais — contexto útil para discutir "escopo livre" e ampliações possíveis da revisão.

## Trechos literais

- "The Unified Planning (UP) library addresses this issue by providing a feature-rich Python API for modeling automated planning problems, which are solved seamlessly by planning engines that specify the set of features they support." (Abstract)
- "The model acquisition tool itSIMPLE [12] allows modeling tasks in the diagram-based UML language, and provides analyses based on Petri nets." (Seção 2, Related Work)

## Marcações

- `[FATO]` A biblioteca Unified Planning padroniza o acesso a motores de planejamento heterogêneos por meio de "Operation Modes" e um sistema de flags de recursos (ProblemKind), permitindo seleção automática de planejadores compatíveis com um dado modelo (Seção 3).
- `[FATO]` O artigo cita o itSIMPLE como ferramenta de modelagem baseada em UML com análises fundamentadas em redes de Petri, na seção de trabalhos relacionados (Seção 2).
- `[HIPÓTESE]` (minha interpretação) Nenhuma ligação direta com as métricas específicas de diagramas de caso de uso/classe/estado da dissertação de 2010 foi encontrada nesta obra; a menção ao itSIMPLE é breve e não substitui a leitura da literatura primária do itSIMPLE (não obtida neste lote para [@tonidandel2006reading]) para confirmar ou refutar detalhes de [A5]/[T1].

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://andrea.micheli.website/papers/up_softwarex.pdf (cópia de acesso aberto idêntica ao publicado em SoftwareX, CC BY 4.0). Conferência humana: pendente.
