---
tipo: nota-de-leitura
eixo: E6
citekey: alnazer2023understanding
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/pdf/2307.04701
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5]
fragilidades: [F3]
perguntas: [Q2]
---

# Understanding Real-World AI Planning Domains: A Conceptual Framework

**Ebaa Alnazer, Ilche Georgievski · 2023 · Service-Oriented Computing (SummerSOC 2023), Communications in Computer and Information Science, Springer, p. 3–23**
**Link/DOI:** https://arxiv.org/abs/2307.04701 (arXiv:2307.04701) · DOI: 10.1007/978-3-031-45728-9_1

## Extração estruturada

- **Problema:** não existe, na comunidade de planejamento automatizado, um mecanismo compartilhado para identificar e categorizar os aspectos "realistas" que caracterizam domínios de aplicação do mundo real — o que dificulta orientar engenheiros de conhecimento e de software nas fases de projeto de sistemas de planejamento (seleção do tipo de planejamento, modelagem do domínio, arquitetura do sistema).
- **Método:** pesquisa exploratória top-down sobre a literatura existente. Identificam 20 estudos relevantes (sobre requisitos/características de domínios de aplicação, medidas de qualidade de conhecimento de planejamento, e processos sistemáticos de engenharia de conhecimento), extraem "aspectos realistas" desses estudos, e os organizam por pesquisa descritiva em uma hierarquia de categorias. Ilustram o resultado com o domínio de edifícios sustentáveis (Sustainable Buildings).
- **Dados/benchmarks:** nenhum experimento computacional; é um framework conceitual/taxonômico construído por revisão sistemática de 20 estudos (listados em tabela no apêndice, com aspecto/subcategoria/categoria por estudo).
- **Resultado principal:** propõem sete categorias de alto nível de aspectos realistas de domínios de planejamento — *Objectives* (objetivos), *Tasks* (tarefas), *Quantities* (quantidades), *Determinism* (determinismo), *Agents* (agentes), *Constraints* (restrições) e *Qualities* (qualidades) —, cada uma decomposta em subcategorias (ex.: Objectives se divide em tipo de meta — soft/hard, qualitativa/quantitativa, otimização/satisfação — e granularidade).
- **Relação com a dissertação de 2010:** oferece uma taxonomia alternativa e mais ampla do que "o que caracteriza um domínio de planejamento", que não se apoia em métricas de diagramas UML (classes, atributos, associações etc., como em 2010) mas em aspectos funcionais/semânticos (metas, tarefas, determinismo, agentes, restrições, qualidades). Isso é relevante para [A5] e [Q2]: sugere que a complexidade "real" de um domínio é multidimensional e não necessariamente capturada por contagens estruturais de diagramas UML — uma taxonomia concorrente que poderia ser usada para perguntar se as métricas de 2010 cobrem, ou não, os aspectos aqui identificados como relevantes. Toca [F3] indiretamente: os próprios autores observam que a qualidade dos modelos de domínio "depends mainly on the skills of the knowledge engineers", citando a mesma linha McCluskey et al. usada nas outras notas deste lote.

## Pontos relevantes para o projeto

- A framework de sete categorias (Objectives, Tasks, Quantities, Determinism, Agents, Constraints, Qualities) pode servir como checklist para avaliar, na revisão da dissertação de 2010, quais aspectos dos 10+3 domínios usados (Storage, Zeno-travel, Elevator etc.) as métricas UML de fato capturam e quais ficam de fora.
- Os autores citam explicitamente que a engenharia de conhecimento de planejamento é, em geral, "done in an ad-hoc manner, and the quality of the resulting planning domain models depends mainly on the skills of the knowledge engineers and, if available, the tools they use" — reafirmação independente (terceira fonte, depois de McCluskey 1997/2017) do argumento central de [F3].
- Trabalho futuro proposto pelos próprios autores é "synthesise metrics that can quantitatively evaluate the realism of planning domains" — atualmente inexistente, o que sinaliza que a pergunta [Q2] (métricas estruturais acrescentam poder preditivo?) segue em aberto mesmo em 2023, treze anos depois de 2010.
- Metodologia de revisão sistemática (20 estudos, tabela de aspecto/categoria/subcategoria por estudo, no Apêndice) é um modelo replicável para a própria revisão de literatura desta dissertação.

## Trechos literais

- "To the best of our knowledge, there is currently no support for software engineers and knowledge engineers in the process of identifying relevant and realistic aspects of real-world planning domains necessary for the development of essential planning elements." (Seção 2.4, Problem Statement)
- "Usually, the process of designing this knowledge is done in an ad-hoc manner, and the quality of the resulting planning domain models depends mainly on the skills of the knowledge engineers and, if available, the tools they use." (Seção 2.4)
- "We categorise these realistic aspects into seven main categories based on their relevance to each other, namely: Objectives, Tasks, Quantities, Determinism, Agents, Constraints, and Qualities." (Seção 4, The Framework)

## Marcações

- `[FATO]` O artigo propõe uma taxonomia de sete categorias de alto nível para aspectos realistas de domínios de planejamento, construída por revisão de 20 estudos, sem usar métricas de diagramas UML (Seção 4).
- `[FATO]` Os autores afirmam explicitamente, citando a literatura de engenharia de conhecimento em planejamento, que a qualidade dos modelos de domínio depende principalmente das habilidades do engenheiro de conhecimento (Seção 2.4).
- `[HIPÓTESE]` (minha interpretação) As categorias "Determinism" e "Qualities" desta taxonomia não têm contrapartida clara nas métricas de diagramas de caso de uso/classes/estados usadas em 2010, o que sugere que essas métricas cobrem apenas uma fração (talvez a parte estrutural de "Tasks") do espaço de aspectos que a literatura atual considera relevante para caracterizar um domínio — uma lacuna a explorar em [Q2], mas que exigiria mapeamento cuidadoso, não feito nesta obra nem nesta nota.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/pdf/2307.04701. Conferência humana: pendente.
