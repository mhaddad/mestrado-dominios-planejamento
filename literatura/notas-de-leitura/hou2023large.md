---
tipo: nota-de-leitura
eixo: E8
citekey: hou2023large
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2308.10620
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1]
fragilidades: []
perguntas: [Q4]
---

# Large Language Models for Software Engineering: A Systematic Literature Review

**Hou, X.; Zhao, Y.; Liu, Y.; Yang, Z.; Wang, K.; Li, L.; Luo, X.; Lo, D.; Grundy, J.; Wang, H. · 2023/2024 (ACM TOSEM) · arXiv**
**Link/DOI:** https://arxiv.org/abs/2308.10620 (10.48550/arxiv.2308.10620; publicado em ACM Trans. Softw. Eng. Methodol., 10.1145/3695988)

## Extração estruturada

- **Problema:** falta de uma compreensão abrangente de como LLMs vêm sendo aplicados, com que efeitos e com que limitações, em engenharia de software (LLM4SE).
- **Método:** revisão sistemática de literatura (SLR), não estudo empírico primário. Selecionaram e analisaram 395 artigos de pesquisa publicados entre janeiro de 2017 e janeiro de 2024, estruturados em torno de quatro perguntas de pesquisa: RQ1 (quais LLMs são empregados em tarefas de SE e suas características), RQ2 (métodos de coleta/preparação de dados), RQ3 (estratégias de otimização e avaliação de desempenho), RQ4 (tarefas específicas de SE em que LLMs mostraram sucesso, organizadas pelo ciclo de vida de desenvolvimento: engenharia de requisitos, projeto de software, desenvolvimento de software, e por extensão outras fases).
- **Dados/benchmarks:** corpus de 395 artigos (não um *benchmark* de código executável); artefatos publicados em repositório público (github.com/xinyi-hou/LLM4SE_SLR).
- **Resultado principal:** a RQ4 organiza o uso de LLMs por fase e tarefa do ciclo de desenvolvimento — por exemplo, em projeto de software: recuperação de GUI (BERT *fine-tuned* como *learning-to-rank*), prototipagem rápida, síntese de especificação de software (SpecSyn, ganho de 21% em F1 sobre o estado da arte anterior); em desenvolvimento de software: geração de código, completação de código, sumarização de código, entre outras. O artigo não reporta um número único de "efeito médio" (é uma síntese qualitativa/taxonômica de centenas de estudos individuais, cada um com sua própria métrica), mas mapeia sistematicamente que tipos de tarefa de SE têm sido mais ou menos explorados e bem-sucedidos com LLMs.
- **Relação com a dissertação de 2010:** **A1** [analogia fraca/estrutural, HIPÓTESE] — a estrutura da RQ4 (organizar sucesso de LLMs por tipo de tarefa/fase do ciclo de vida) é, em espírito, análoga à pergunta central de 2010 (que características de domínio predizem que técnica funciona melhor), mas aplicada em nível de taxonomia qualitativa de tarefas de SE, sem uma métrica estrutural comparável às métricas UML de 2010 nem um ranking quantitativo único. É a fonte mais adequada do lote para orientar QUAIS tipos de tarefa de SE existem e merecem comparação sistemática de desempenho por característica (útil como mapa, não como evidência quantitativa de variação de efeito).

## Pontos relevantes para o projeto

- Não é evidência primária de efeito que varia com a tarefa (é síntese de literatura), mas fornece a taxonomia de tarefas de SE (requisitos, projeto, desenvolvimento, teste, manutenção) contra a qual os demais estudos do lote (rondon2025evaluating, takerngsaksiri2025humanintheloop, son2026swerouter, zhou2026agentasarouter) podem ser posicionados.
- Escala (395 artigos, janeiro/2017 a janeiro/2024) supera em muito a amostra de qualquer estudo primário do lote — útil para contextualizar o estado do campo, mas datado already (corte em jan/2024) frente aos trabalhos de 2025/2026 do mesmo lote, que já mostram achados (efeito nulo/negativo, roteamento por dimensão) posteriores ao escopo desta revisão.
- Fonte apropriada para citar afirmações gerais sobre "onde LLMs têm sido aplicados em SE", mas não deve ser citada como fonte de números de desempenho específicos sem checar o artigo primário correspondente na própria SLR.

## Marcações

- `[FATO]` "we conducted a systematic literature review (SLR) on LLM4SE... We select and analyze 395 research papers from January 2017 to January 2024 to answer four key research questions" (resumo).
- `[FATO]` "RQ4 examines the specific SE tasks where LLMs have shown success to date, illustrating their practical contributions to the field" (resumo); a Seção 6 organiza esse mapeamento por fase (6.2 engenharia de requisitos, 6.3 projeto de software, 6.4 desenvolvimento de software).
- `[HIPÓTESE]` A ausência, nesta SLR, de qualquer tentativa de quantificar sistematicamente "por que tarefa X favorece modelo Y" (ao contrário do que fazem rondon2025evaluating e zhou2026agentasarouter) sugere que a pergunta de Q4 — ajuste tarefa-estratégia para configuração de agentes — ainda não tinha, até o corte desta revisão (jan/2024), tratamento sistemático comparável ao de 2010 para domínios de planejamento; isso só aparece nos trabalhos de 2025/2026 do lote.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2308.10620 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
