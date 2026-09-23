---
tipo: nota-de-leitura
eixo: E5
citekey: hao2023reasoning
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://aclanthology.org/2023.emnlp-main.507/
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A2, A5]
fragilidades: []
perguntas: [Q3]
---

# Reasoning with Language Model is Planning with World Model

**Hao, S.; Gu, Y.; Ma, H.; Hong, J.; Wang, Z.; Wang, D.; Hu, Z. · 2023 (EMNLP 2023) · ACL Anthology**
**Link/DOI:** https://aclanthology.org/2023.emnlp-main.507/ (10.18653/v1/2023.emnlp-main.507)

## Extração estruturada

- **Problema:** LLMs com *prompting* padrão (inclusive *Chain-of-Thought*) carecem de um modelo de mundo interno para simular estados futuros e planejar deliberadamente; o artigo propõe reaproveitar o próprio LLM como modelo de mundo, além de agente de raciocínio.
- **Método:** papel do LLM = **duplo: gerador de heurística/modelo de mundo e agente de raciocínio** (RAP — *Reasoning via Planning*). O mesmo LLM é reaproposto para (i) prever o próximo estado do mundo dado um estado e uma ação (modelo de mundo) e (ii) propor ações e avaliar recompensa. Um algoritmo de *Monte Carlo Tree Search* (MCTS) usa essas duas funções para construir incrementalmente uma árvore de raciocínio e extrair um caminho de alta recompensa, balanceando exploração e explotação. Comparado com *prompting* padrão e com CoT (inclusive com GPT-4).
- **Dados/benchmarks:** Blocksworld (planejamento clássico, tarefas de 2, 4 e 6 passos, do mesmo conjunto usado por Valmeekam et al. 2022); GSM8K (raciocínio matemático); ProntoQA (raciocínio lógico). Apenas Blocksworld é um domínio de planejamento automatizado propriamente dito; os outros dois são tarefas de raciocínio geral, não domínios PDDL.
- **Modelo e data:** **LLaMA-33B** (Touvron et al. 2023a, modelo base, não ajustado por instrução) como agente/modelo de mundo dentro do RAP; comparado com **GPT-4** (OpenAI 2023) usando apenas CoT. Artigo publicado em EMNLP 2023.
- **Resultado principal:** Tabela 1, Blocksworld — CoT com LLaMA-33B: 0,17/0,02/0,00 (2/4/6 passos); CoT com GPT-4: 0,50/0,63/0,40; **RAP(20) com LLaMA-33B**: 1,00/0,88/0,42, com taxa média de sucesso de **64%**, superando CoT-GPT4 mesmo sendo um modelo muito menor. O texto afirma explicitamente: "RAP with LLaMA-33B even surpasses CoT with GPT-4, achieving 33% relative [improvement]" — um modelo ~1.500 vezes menor que se estima para GPT-4 supera o maior via melhor algoritmo de busca, não via mais parâmetros.
- **Relação com a dissertação de 2010:** **A2** [dialoga diretamente] — a arquitetura RAP combina, na terminologia de técnicas de planejamento de 2010, elementos de busca heurística (MCTS orientada por recompensa estimada pelo próprio LLM) com um "modelo de mundo" aprendido/aproximado; a melhoria de desempenho ao adicionar uma estrutura de busca (RAP) sobre geração direta (CoT) é consistente com a afirmação de 2010 de que técnicas de busca heurística e encadeamento para frente figuram entre as mais promissoras, embora aqui a "heurística" venha do próprio LLM, não de uma função definida sobre o domínio. **A5** [parcialmente testável] — o desempenho cai visivelmente com o aumento do número de passos exigidos (de 100%/88% em 2–4 passos para 42% em 6 passos), mostrando sensibilidade a uma dimensão de complexidade da tarefa, mas o artigo testa um único domínio de planejamento (Blocksworld), então não há variação *entre* domínios de planejamento a reportar aqui — só entre tarefas de planejamento e tarefas de raciocínio geral (GSM8K, ProntoQA), que não são comparáveis a domínios PDDL.

## Pontos relevantes para o projeto

- Único artigo do lote em que o LLM assume simultaneamente o papel de heurística e de "modelo de mundo" dentro de uma busca MCTS — papel distinto de tradutor, planejador direto ou verificador, relevante para a taxonomia da Q3.
- O ganho de RAP sobre CoT dentro do mesmo Blocksworld, crescente com o número de passos exigidos (de +0,83 em 2 passos a +0,42 em 6 passos, sobre a base CoT-LLaMA), é evidência de que a *técnica de busca* (não apenas o tamanho do modelo) determina desempenho — argumento afim ao de 2010 sobre técnicas.
- Cuidado ao citar: não há domínios adicionais de planejamento automatizado neste artigo além de Blocksworld; GSM8K e ProntoQA não devem ser tratados como "domínios de planejamento" na nota consolidada, para não confundir com a pergunta sobre variação de desempenho por domínio pedida no prompt.
- Data e modelo: LLaMA-33B (2023, modelo base pré-treinado, sem *instruction tuning* alegado no texto) — importante registrar que não é um modelo "de fronteira" mesmo em 2023, o que reforça o argumento dos autores de que o ganho vem do algoritmo de busca.

## Marcações

- `[FATO]` "RAP with LLaMA-33B even surpasses CoT with GPT-4, achieving 33% relative [gain]" e Tabela 1: RAP(20) com LLaMA-33B atinge 1,00/0,88/0,42 em Blocksworld de 2/4/6 passos, contra CoT-GPT-4 em 0,50/0,63/0,40 (resumo/abstract e seção 4.1).
- `[FATO]` "CoT with LLaMA-33B can only generate successful plans for a few 2-step cases, and completely fails on harder problems" (seção 4.1, análise dos resultados de Blocksworld).
- `[HIPÓTESE]` Não é possível, a partir apenas deste artigo, avaliar se o padrão de desempenho de RAP varia por domínio de planejamento automatizado (só um domínio, Blocksworld, foi testado); qualquer afirmação sobre "desempenho por domínio" para este método precisaria vir de outra fonte que replique RAP em mais domínios PDDL.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://aclanthology.org/2023.emnlp-main.507/ (PDF baixado da ACL Anthology, extraído com pdftotext). Conferência humana: pendente.
