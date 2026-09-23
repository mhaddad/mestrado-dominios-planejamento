---
tipo: nota-de-leitura
eixo: E8
citekey: stray2025developer
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2509.20353
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A3]
fragilidades: []
perguntas: [Q4]
---

# Developer Productivity With and Without GitHub Copilot: A Longitudinal Mixed-Methods Case Study

**Stray, V.; Brandtzæg, E. G.; Wivestad, V. T.; Barbala, A.; Moe, N. B. · 2025/2026 (HICSS 2026) · arXiv**
**Link/DOI:** https://arxiv.org/abs/2509.20353 (DOI HICSS do registro: 10.24251/HICSS.2026.880)

## Extração estruturada

- **Problema:** impacto real do GitHub Copilot na atividade de desenvolvimento e na produtividade percebida, em uma organização real (não experimento de laboratório).
- **Método:** estudo de caso longitudinal de métodos mistos em NAV IT (grande órgão público ágil, Noruega). RQ1: como a adoção do Copilot influencia a atividade no GitHub? RQ2: como a produtividade percebida se relaciona com a atividade de *commits* entre usuários do Copilot? Analisaram 26.317 *commits* únicos (não-*merge*) de 703 repositórios do GitHub da NAV IT ao longo de dois anos, com foco em métricas de atividade baseadas em *commit* de 25 usuários do Copilot e 14 não usuários (39 funcionários no total). Complementado por pesquisa de percepção sobre papéis/produtividade e 13 entrevistas.
- **Dados/benchmarks:** comparação de um ano antes e um ano depois da introdução do Copilot na organização, para os mesmos 39 funcionários (25 adotantes, 14 não adotantes); testes de Mann–Whitney U e correlação de Spearman.
- **Resultado principal:** "We did not find any statistically significant changes in commit-based activity for Copilot users after they adopted the tool, although minor increases were observed" (resumo) — efeito nulo no indicador quantitativo principal. Adicionalmente, adotantes do Copilot já eram significativamente mais ativos que não adotantes **antes mesmo** da adoção (p<0,00555, teste de Mann–Whitney U), sugerindo autosseleção: "Copilot adopters were already significantly more active developers to begin with, and they remained more active afterwards, indicating a self-selection effect." A relação entre produtividade percebida e atividade de *commits* não foi estatisticamente significativa (ρ de Spearman ≈ 0,17; p=0,40).
- **Relação com a dissertação de 2010:** **A3** [analogia fraca/negativa, HIPÓTESE] — diferente de rondon2025evaluating e becker2025measuring, este estudo **não** encontra variação de efeito ligada a uma característica de tarefa/repositório mensurável; a principal fonte de heterogeneidade identificada é a autosseleção do desenvolvedor (quem já era mais ativo adotou a ferramenta), um viés metodológico, não uma característica de domínio análoga às de 2010. É um contraponto útil: mostra que "efeito varia por característica X" não é garantido — em métricas de atividade de repositório de larga escala, o sinal pode desaparecer completamente, reforçando a necessidade de métricas subjetivas complementares (a divergência entre atividade objetiva e produtividade percebida é o achado mais forte do estudo).

## Pontos relevantes para o projeto

- Segundo caso do lote (com becker2025measuring) de efeito nulo/sem-ganho em condição real de equipe, mas por um mecanismo distinto: aqui não há RCT (é observacional, com risco de autosseleção reconhecido pelos próprios autores), enquanto becker2025measuring é RCT com resultado negativo causal.
- Achado central é a **discrepância** entre métricas objetivas de *commit* (nulo) e experiência subjetiva de produtividade — relevante para Q4 porque mostra que "efeito" depende de qual métrica se escolhe medir, não só de características da tarefa.
- Amostra pequena (39 funcionários, 25 vs. 14) e desenho observacional (não randomizado) — limita força causal em comparação com peng2023impact e becker2025measuring.
- Entrevistas registram que desenvolvedores individuais dão pesos muito diferentes à ferramenta conforme o contexto do time (um entrevistado descreve que sua equipe já eliminava boilerplate por escolhas arquiteturais, tornando o Copilot "supérfluo") — evidência qualitativa (não quantificada) de variação por contexto de tarefa/equipe.

## Marcações

- `[FATO]` "We did not find any statistically significant changes in commit-based activity for Copilot users after they adopted the tool, although minor increases were observed. This suggests a discrepancy between changes in commit-based metrics and the subjective experience of productivity" (resumo).
- `[FATO]` "Copilot adopters were already significantly more active developers to begin with, and they remained more active afterwards, indicating a self-selection effect" (Seção 4.1, comparando 25 usuários vs. 14 não usuários, p<0,00555).
- `[HIPÓTESE]` A ausência de um sinal de variação por característica de tarefa/repositório neste estudo — em contraste com rondon2025evaluating, takerngsaksiri2025humanintheloop e becker2025measuring — sugere que a granularidade da métrica importa: métricas agregadas de atividade em nível de repositório/organização podem mascarar exatamente o tipo de heterogeneidade por tarefa que a Q4 busca detectar, que só aparece em desenhos com tarefas individuais rotuladas (como em becker2025measuring e rondon2025evaluating).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2509.20353 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
