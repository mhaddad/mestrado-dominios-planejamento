---
tipo: nota-de-leitura
eixo: E6
citekey: jiang2026toward
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2606.29700 (PDF baixado, lidos resumo e introdução)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [T1]
fragilidades: [F3]
perguntas: [Q3]
---

# Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback

**Jiang, J.; Zhang, J.; Mo, F.; Li, L.; Zeng, D. · 2026 · arXiv preprint**
**Link/DOI:** https://doi.org/10.48550/arxiv.2606.29700

## Extração estruturada

- **Problema:** falhas na formalização de especificações simbólicas (PDDL) por LLMs, usados em sistemas autônomos ou de apoio à decisão, podem gerar decisões não verificáveis, falhas de execução ou comportamento inseguro.
- **Método:** apresentam o NL-PDDL-Bench, um benchmark multi-domínio para construção de especificações PDDL a partir de linguagem natural, com executabilidade verificada por planejador e escalonamento controlado de dificuldade pelo número de objetos. Propõem também um *framework* "planejador-no-laço" (*planner-in-the-loop*) que usa diagnósticos de validador e planejador para revisar especificações não executáveis por meio de edições localizadas.
- **Dados/benchmarks:** NL-PDDL-Bench (benchmark próprio, multi-domínio).
- **Resultado principal:** não detalhado em profundidade na leitura de resumo/introdução (nota curta); os autores buscam tornar as saídas de LLM verificáveis externamente, executáveis e corrigíveis sob restrições formais.
- **Relação com a dissertação de 2010:** dialoga com **T1** (extração/geração automática de modelos, trabalho futuro de 2010) e com **F3** (dependência do modelador): o mecanismo de "planejador no laço" usa o próprio planejador e validadores formais como fonte de correção, uma forma de reduzir (não eliminar) a dependência de um modelador humano especialista. Alimenta **Q3**.

## Pontos relevantes para o projeto

- Traz uma métrica de controle de dificuldade por número de objetos, relevante para pensar em escalonamento de complexidade de domínios — tema próximo à discussão de métricas estruturais em Q2.
- Data de publicação (2026) situa este trabalho entre os mais recentes do lote, relevante para mostrar a trajetória mais atual da linha "LLM + verificação formal" na engenharia do conhecimento para planejamento.
- Nota de cautela: arXiv ID 2606.29700 (junho de 2026), publicação muito recente em relação à data desta leitura (22/09/2026); tratar como preprint ainda não passível de citações que dependam de revisão por pares consolidada.

## Trechos literais

"We present NL-PDDL-Bench, a multi-domain benchmark for natural-language-to-PDDL specification construction with planner-verified executability and controlled difficulty scaling by object count" (resumo).

## Marcações

- `[FATO]` o artigo apresenta um benchmark (NL-PDDL-Bench) e um framework de correção guiado por planejador para geração de especificações PDDL a partir de linguagem natural por LLMs (resumo).
- `[HIPÓTESE]` interpretação minha: este é mais um exemplo, ao lado de gestrin2024nl2plan e smirnov2024generating, de uma tendência que combina LLM com verificação simbólica externa para mitigar a dependência de modeladores humanos — padrão recorrente neste lote de leitura do eixo E6.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução do PDF em https://arxiv.org/pdf/2606.29700. Conferência humana: pendente.
