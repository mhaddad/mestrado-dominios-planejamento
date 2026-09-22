---
tipo: nota-de-leitura
eixo: E8
citekey: son2026swerouter
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2607.00053
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A3]
fragilidades: []
perguntas: [Q4]
---

# SWE-Router: Routing in Multi-turn Agentic Software Engineering Tasks

**Son, S.; Yoon, S.; Tang, J.; Wang, S.; Wolf, L.; Bogunovic, I. · 2026 (5th Deep Learning for Code Workshop, ICML 2026) · arXiv**
**Link/DOI:** https://arxiv.org/abs/2607.00053 (sem DOI Crossref no momento da leitura)

## Extração estruturada

- **Problema:** roteamento de modelo em tarefas agênticas de engenharia de software de múltiplos turnos: encaminhar toda tarefa a um modelo de fronteira (caro) é desperdício quando muitas *issues* admitem correções baratas, mas roteadores existentes decidem só a partir da descrição textual da tarefa, sem observar o comportamento do agente.
- **Método:** proposta de arquitetura (não ensaio com humanos). SWE-Router deixa um modelo barato (m1) rodar por algumas *turns* exploratórias; uma cabeça de valor (`Qwen2.5-Coder-7B-Instruct` com cabeça de classificação de 2 classes, ajustada via LoRA) lê a trajetória parcial e decide se continua com m1 ou escala para um modelo forte (m2). Inclui um teorema de Bayes-otimalidade (Teorema 4.1) mostrando que condicionar na trajetória parcial nunca piora o roteamento e é estritamente melhor quando a exploração é informativa. Comparam com três roteadores só de texto (regressão logística, k-NN, XGBoost sobre *embeddings* `text-embedding-3-large`) e com uma variante não-temporal do próprio método (K=0).
- **Dados/benchmarks:** SWE-Smith e o conjunto de teste do SWE-Bench Verified; pares de modelo fraco/forte cobrindo a fronteira custo-capacidade contemporânea (ex.: gpt-5-mini/gemini-3-pro; deepseek-v3.2/gemini-3-pro, conforme Figura 2).
- **Resultado principal:** "SWE-Router greatly improves the cost efficiency of SWE tasks, while maintaining the majority of the performances of the stronger model" (resumo) e "on SWEBench-Verified, SWE-Router achieves substantial cost reductions at matched resolution relative to strong prompt-only baselines" (Contribuições). O artigo não fornece, no corpo lido, uma tabela numérica única e citável com o ganho percentual exato de custo — os resultados centrais estão nas curvas de custo-vs-taxa-resolvida da Figura 2, comparadas à referência de atribuição aleatória.
- **Relação com a dissertação de 2010:** **A1** e **A3** [analogia direta, HIPÓTESE] — o argumento central do artigo é exatamente a lógica de 2010 aplicada ao roteamento de modelo: a resposta correta (usar modelo barato ou caro) não é fixa por tarefa nominal, mas pode ser inferida a partir de sinais observáveis (aqui, a trajetória parcial do agente, análoga a características estruturais do domínio em 2010) sem precisar rodar o modelo caro do início. O artigo nomeia explicitamente essa dependência: "a similar issue description can specify a localized typo or a multi-module refactor, and the distinction is often not identifiable from q alone" — ou seja, a descrição da tarefa por si só (equivalente a um rótulo de domínio) não basta; é preciso uma característica adicional observável (aqui, comportamental/temporal) para prever qual "técnica" (modelo) funciona melhor.

## Pontos relevantes para o projeto

- É o exemplo mais direto do lote de "roteamento condicionado a características da tarefa" pedido na Q4 — mas nota-se que a "característica" usada não é estática (como em 2010), e sim dinâmica: observada durante a execução do agente, não antes dela.
- Publicado como artigo de *workshop* (ICML 2026, Deep Learning for Code), o que sugere um estágio de maturidade e revisão por pares menor que os artigos de conferência principal do lote (ICSE-SEIP); os números de ganho de custo citados no resumo são qualitativos ("greatly", "substantial"), sem valor percentual único reportado no texto corrido lido.
- Teorema de Bayes-otimalidade (Seção 4, "conditioning on the partial trajectory never harms routing and is strictly better whenever exploration is informative") dá uma justificativa formal para por que informação adicional sobre a tarefa (trajetória parcial) deveria sempre ajudar ou não piorar o roteamento — argumento estrutural análogo (mas formalizado) ao pressuposto informal de 2010 de que mais características do domínio melhoram o ranking (T4 de 2010).
- Datas: publicado no arXiv em 30/06/2026 (identificador `2607.00053`), no momento da leitura desta nota (22/09/2026) trata-se de trabalho muito recente, ainda não publicado em veículo principal.

## Marcações

- `[FATO]` "Existing LLM routers operate on the task description alone, which inherits an information-theoretic Bayes-error floor in agentic settings: a similar issue can hide either a localized typo or a multi-module refactor, and the prompt does not separate the two" (resumo).
- `[FATO]` "on SWEBench-Verified, SWE-Router achieves substantial cost reductions at matched resolution relative to strong prompt-only baselines" (Seção 1, Contribuições, item iii).
- `[HIPÓTESE]` A escolha de condicionar o roteamento em sinal comportamental (trajetória parcial) em vez de característica estática da tarefa sugere uma extensão possível à lógica de 2010 para agentes de IA: a "característica do domínio" relevante pode não ser observável antes da execução, exigindo uma etapa exploratória — algo sem equivalente na metodologia de 2010, que extrai métricas do modelo UML do domínio antes de qualquer execução do planejador.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2607.00053 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
