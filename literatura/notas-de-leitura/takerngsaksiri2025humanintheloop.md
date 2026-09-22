---
tipo: nota-de-leitura
eixo: E8
citekey: takerngsaksiri2025humanintheloop
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2411.12924
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A3]
fragilidades: []
perguntas: [Q4]
---

# Human-In-the-Loop Software Development Agents

**Takerngsaksiri, W.; Pasuksmit, J.; Thongtanunam, P.; Tantithamthavorn, C. K.; Zhang, R.; Jiang, F.; Li, J.; Cook, E.; Chen, K.; Wu, M. · 2025 (ICSE-SEIP 2025) · arXiv**
**Link/DOI:** https://arxiv.org/abs/2411.12924 (registro DOI do lote: 10.1109/icse-seip66354.2025.00036; PDF de acesso aberto localizado via busca, pois `texto_integral_url` do lote estava vazio)

## Extração estruturada

- **Problema:** frameworks de agentes de LLM para desenvolvimento de software são avaliados quase sempre em *benchmarks* históricos de código aberto, raramente incorporam retroalimentação humana em cada estágio, e quase nunca são implantados em produção real. O artigo introduz e avalia o HULA, implantado internamente na Atlassian.
- **Método:** framework de três agentes (Planner, Coding, Human) integrado ao JIRA. Avaliação em três estágios: (1) avaliação *offline* sem retroalimentação humana, comparando SWE-bench com um conjunto interno de 369 *issues* JIRA; (2) avaliação *online* com retroalimentação humana em 663 *issues* reais; (3) pesquisa de percepção com engenheiros da Atlassian (n=109 respostas na pesquisa de satisfação, n=83 na de benefícios percebidos).
- **Dados/benchmarks:** SWE-bench (aberto) vs. conjunto interno de 369 *issues* JIRA da Atlassian (RQ1); 663 *issues* JIRA reais em produção (RQ2); pesquisas com desenvolvedores (RQ3).
- **Resultado principal:** desempenho do mesmo agente cai fortemente do *benchmark* aberto para o conjunto interno — no SWE-bench, o AI Planner Agent atinge recall médio de 86% na identificação de arquivos a alterar e o AI Coding Agent atinge similaridade média de 45% com o código de referência; no conjunto interno da Atlassian, o Planner cai para 30% de recall médio e o Coding Agent cai para 30% de similaridade média. Na avaliação *online* com retroalimentação humana: planos gerados com sucesso para 527 de 663 *issues*, aprovados pelos profissionais em 433 de 527 (taxa de aprovação de planos de 82%); *pull requests* levantados para 95 de 376 *issues* com código gerado (taxa de PR de 25%), das quais 56 foram integradas (taxa de PR integrada de 59%).
- **Relação com a dissertação de 2010:** **A1** e **A3** [confirma por analogia direta, HIPÓTESE] — o próprio artigo atribui a queda de desempenho a uma característica observável da tarefa: a forma como a descrição do problema é escrita. *Issues* do SWE-bench têm descrições detalhadas com nomes de módulo e trechos de código; *issues* JIRA de uma organização ágil como a Atlassian são tipicamente mais curtas e colaborativas. Isso é uma instância direta da tese de 2010 de que a característica da tarefa/domínio (aqui, riqueza informacional da especificação) prediz o desempenho da técnica, independentemente da técnica em si.

## Pontos relevantes para o projeto

- Segundo caso do lote (após rondon2025evaluating) em que a mesma técnica, sem alterar o modelo, muda de desempenho por características observáveis da tarefa — aqui quantificado tanto em recall/similaridade (RQ1) quanto em taxas de aprovação/PR (RQ2).
- Explica o mecanismo hipotético da queda (riqueza da descrição do *issue*), algo que 2010 não fazia de forma causal — só correlacional via métricas estruturais UML.
- Os desenvolvedores relatam, na pesquisa de percepção, que HULA é útil sobretudo em "tarefas simples ou diretas" (*"Resolve simple or straightforward task"*, Fig. 7), reforçando por via qualitativa a mesma conclusão quantitativa de RQ1: a dificuldade/complexidade da tarefa modula a utilidade do agente.
- Estudo de implantação real em produção (não *benchmark* isolado nem ensaio de laboratório), o que dá peso empírico maior à conclusão para Q4.

## Marcações

- `[FATO]` "For SWE-bench, AI Planner Agent can correctly identify files that need to be changed, achieving an average recall of 86% per issue, while AI Coding Agent can correctly generate code that is similar to the human-written code... with an average similarity score of 45%... when applying Agents to the Atlassian internal dataset, AI Planner Agent achieves an average recall of 30% per issue, while AI Coding Agent achieves an average similarity score of 30%" (resposta à RQ1).
- `[FATO]` "plans are successfully generated for 527 out of the 663 real-world JIRA issues. Of these, practitioners approved the generated plans for 433 out of 527 plan-generated issues, achieving a plan approval rate of 82%... pull requests (PRs) were created for 95 out of 376 code-generated issues, achieving a raised PR rate of 25%. Of these, 56 PRs were successfully merged, leading to a merged PR rate of 59%" (resposta à RQ2).
- `[FATO]` "In RQ1, we found that HULA achieves a lower accuracy on the internal dataset when compared to the SWE-bench dataset. One of the possible reasons is related to the nature of how a task is written. For the SWE-bench dataset, issues typically have a detailed description... However, for Agile-driven organizations like Atlassian, practitioners tend to collaborate..." (Lição Aprendida 1).
- `[HIPÓTESE]` A atribuição explícita da queda de desempenho à "natureza de como a tarefa é escrita" é evidência de que a característica textual/estrutural da especificação da tarefa é uma variável candidata a "domínio" na analogia com 2010 — mas o artigo não a mede de forma estrutural (não há equivalente às métricas UML), apenas qualitativa.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2411.12924 (PDF baixado do arXiv, extraído com pdftotext; a URL do lote fornecia apenas o registro Crossref pelo DOI, sem PDF; localizei a versão de acesso aberto por busca web). Conferência humana: pendente.
