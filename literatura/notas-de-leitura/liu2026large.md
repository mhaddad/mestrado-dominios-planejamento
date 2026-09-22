---
tipo: nota-de-leitura
eixo: E8
citekey: liu2026large
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2409.02977
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A6]
fragilidades: [F1, F4]
perguntas: [Q3, Q4]
---

# Large Language Model-Based Agents for Software Engineering: A Survey

**Liu, J.; Wang, K.; Chen, Y.; Peng, X.; Chen, Z.; Zhang, L.; Lou, Y. · 2026 (revisão sistemática; preprint 2024) · ACM Comput. Surv. / arXiv**
**Link/DOI:** https://doi.org/10.1145/3796507 (texto lido via arXiv:2409.02977)

## Extração estruturada

- **Problema:** organizar sistematicamente o campo emergente de agentes baseados em LLM aplicados a Engenharia de Software (SE), cobrindo tanto a perspectiva de SE (que tarefas são resolvidas) quanto a perspectiva de agente (como os agentes são projetados).
- **Método:** revisão sistemática de literatura: coletam 124 artigos e os categorizam em duas dimensões — perspectiva de SE (tarefas individuais como geração de código, teste, depuração, e o processo de ponta a ponta de desenvolvimento) e perspectiva de agente (LLM de base, planejamento, memória, percepção, ação, sistemas multiagente).
- **Dados/benchmarks:** corpus de 124 artigos revisados sistematicamente; repositório companheiro no GitHub (Agent4SE-Paper-List).
- **Resultado principal:** apresenta uma visão abrangente de como tarefas de SE são resolvidas por agentes de LLM, analisa os componentes de projeto desses agentes (incluindo sistemas multiagente, papéis, mecanismos de colaboração, fluxo de informação e colaboração humano-agente) e discute oportunidades de pesquisa e direções futuras no campo.
- **Relação com a dissertação de 2010:** **A1** [confirma por analogia direta, HIPÓTESE] — a survey organiza o campo de SE em tarefas específicas (analogia a "domínios" de 2010) e os agentes em componentes de projeto (analogia a "técnicas"), reproduzindo a mesma estrutura de pergunta de 2010 em escala muito maior (124 artigos vs. 10 domínios). **A6** [torna obsoleta, HIPÓTESE] — a taxonomia de técnicas de planejamento de 2010 (forward-chaining, plan-space etc.) não aparece nesta survey; agentes de LLM são taxonomizados por componentes (memória, percepção, planejamento, ação) e padrões de colaboração multiagente, uma taxonomia totalmente distinta, adequada ao novo domínio. **F1** [ajuda a tratar, HIPÓTESE] — preenche uma lacuna de revisão análoga à F1 de 2010 (revisão de literatura rasa), mas para o campo de agentes de LLM em SE. **F4** [ajuda a tratar, HIPÓTESE] — evidencia que toda nova taxonomia de "técnicas" precisa ser construída para o domínio específico, reforçando a fragilidade de 2010 sobre taxonomia discutível.

## Pontos relevantes para o projeto

- É a survey mais abrangente do lote sobre agentes de LLM em SE (124 artigos), servindo de mapa de referência para inserir os demais itens de E8 do acervo (OpenHands, Agentless, SWE-Gym, MetaGPT, AutoGen) dentro de um panorama mais amplo.
- Discute explicitamente processos de desenvolvimento (Waterfall, Scrum) adaptados por agentes de ponta a ponta, observando que o "Daily Scrum" (sincronização entre membros do time) costuma ser omitido pelos agentes atuais, pois compartilham informação via mecanismos de memória — achado concreto sobre como agentes de IA se afastam de práticas humanas de processo.
- Não realiza análise estatística de ajuste tarefa-técnica (é uma survey qualitativa/categórica, não um estudo empírico com métricas de desempenho desagregadas por característica de tarefa) — limite relevante para uso direto na Q4.

## Trechos literais

"We collect 124 papers and categorize them from two perspectives, i.e., the SE and agent perspectives. In addition, we discuss open challenges and future directions in this critical domain" (resumo).

## Marcações

- `[FATO]` A survey revisa sistematicamente 124 artigos sobre agentes de LLM em Engenharia de Software, categorizando-os pela perspectiva de tarefa de SE e pela perspectiva de projeto do agente (resumo e introdução).
- `[HIPÓTESE]` A estrutura da survey (tarefas de SE × componentes de agente) reproduz, em escala maior e com taxonomia própria, a mesma lógica de pergunta de 2010 (domínio × técnica), mas os autores não fazem essa comparação com planejamento automatizado.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e trecho da discussão sobre processos de desenvolvimento em https://arxiv.org/abs/2409.02977 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
