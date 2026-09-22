---
tipo: nota-de-leitura
eixo: E5
citekey: huang2024understanding
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2402.02716 (PDF baixado, lidos resumo, introdução e seção 9 - conclusões)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: [F4]
perguntas: [Q3]
---

# Understanding the planning of LLM agents: A survey

**Huang, X.; Liu, W.; Chen, X.; Wang, X.; Wang, H.; Lian, D.; Wang, Y.; Tang, R.; Chen, E. · 2024 · arXiv preprint (IJCAI)**
**Link/DOI:** https://doi.org/10.48550/arxiv.2402.02716

## Extração estruturada

- **Problema:** organizar sistematicamente os trabalhos recentes que usam LLMs como módulos de planejamento de agentes autônomos.
- **Método:** revisão com taxonomia própria, dividindo os trabalhos em cinco direções: Decomposição de Tarefas, Seleção de Plano, Módulo Externo, Reflexão e Memória; inclui experimentos comparativos próprios em quatro benchmarks.
- **Dados/benchmarks:** ALFWorld, ScienceWorld, HotPotQA e FEVER (para os experimentos comparativos dos autores).
- **Resultado principal:** o desempenho de métodos de planejamento com LLM tende a aumentar com o custo computacional/de API, mas persistem desafios centrais como alucinações e falta de garantia de viabilidade dos planos gerados.
- **Relação com a dissertação de 2010:** dialoga com **F4** (taxonomia de técnicas discutível em 2010): este survey propõe uma taxonomia própria e diferente (decomposição, seleção, módulo externo, reflexão, memória) para a era dos LLMs, ilustrando que toda taxonomia de "técnicas de planejamento" — inclusive a de 2010 (A6) — é uma escolha do pesquisador, sujeita a revisão. Não confirma nem corrige diretamente A1–A8, mas alimenta **Q3**.

## Pontos relevantes para o projeto

- Boa referência de taxonomia alternativa de "técnicas" para contrastar com a taxonomia de 2010 (A6: SAT como *forward-chaining*, SGPlan/SATPlan/MAXPLAN como *plan-space*, Fast Downward como *hierarchical*), ao discutir F4.
- Reconhece explicitamente limitações do campo (alucinação, viabilidade), o que ajuda a calibrar expectativas na seção de LLMs da revisão.
- Os experimentos próprios comparam métodos em benchmarks de agentes interativos, não em domínios clássicos de planejamento — atenção ao aplicar conclusões aos domínios do tipo IPC usados em 2010.

## Trechos literais

"We provide a taxonomy of existing works on LLM-Agent planning, which can be categorized into Task Decomposition, Plan Selection, External Module, Reflection and Memory" (resumo).

## Marcações

- `[FATO]` o survey propõe uma taxonomia própria de cinco categorias para métodos de planejamento com LLM e conduz experimentos comparativos em quatro benchmarks (resumo; seção 9).
- `[HIPÓTESE]` interpretação minha: a proliferação de taxonomias distintas (a de 2010 para planejadores clássicos, a deste survey para LLMs) reforça a fragilidade F4 já identificada no plano — nenhuma taxonomia de "técnica" parece consensual no campo.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e seção 9 (Conclusions and Future Directions) do PDF em https://arxiv.org/pdf/2402.02716. Conferência humana: pendente.
