---
tipo: nota-de-leitura
eixo: E6
citekey: smirnov2024generating
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2404.07751 (PDF baixado, lidos resumo e introdução)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: [F3]
perguntas: [Q3]
---

# Generating consistent PDDL domains with Large Language Models

**Smirnov, A.V.; Joublin, F.; Ceravola, A.; Gienger, M. · 2024 · arXiv preprint**
**Link/DOI:** https://doi.org/10.48550/arxiv.2404.07751

## Extração estruturada

- **Problema:** LLMs conseguem transformar descrições de domínio em linguagem natural em marcações PDDL plausíveis, mas garantir consistência entre as ações dentro de um domínio ainda é desafiador.
- **Método:** propõem checagem de consistência automatizada durante o processo de geração, integrando mecanismos de checagem e análise de alcançabilidade (*reachability*) em um laço de geração baseado em LLM: predicados e tipos de parâmetros mal usados são filtrados antes do planejamento, e predicados ausentes, contraditórios ou nunca alcançados são detectados e realimentados ao LLM para correção.
- **Dados/benchmarks:** domínios de planejamento clássicos e customizados: logística, *gripper*, *tyreworld*, doméstico, *pizza*.
- **Resultado principal:** a quantidade de erros nos domínios PDDL gerados é reduzida, resultando em descrições de domínio significativamente melhoradas para a etapa final de checagem humana (não elimina totalmente a necessidade de revisão humana, mas reduz o esforço).
- **Relação com a dissertação de 2010:** dialoga com **F3** (métricas UML/modelos dependem do modelador): aqui o "modelador" volta a ser parcialmente humano (LLM gera, humano checa no fim), mas o mecanismo de checagem automatizada de consistência é uma forma de mitigar erros de modelagem sem depender só da habilidade do modelador humano. Alimenta **Q3**.

## Pontos relevantes para o projeto

- Exemplo concreto de mecanismo de correção automatizada de modelos de domínio gerados por LLM, relevante para discutir como a "dependência do modelador" (F3) pode mudar de natureza (de humano para humano+LLM+validador) na era atual.
- Usa domínios clássicos (logística, gripper) que também aparecem na literatura de planejamento citada por 2010, facilitando comparação.

## Trechos literais

"In this paper we present a novel concept to significantly improve the quality of LLM-generated PDDL models by performing automated consistency checking during the generation process" (resumo).

## Marcações

- `[FATO]` o artigo demonstra, em cinco domínios de planejamento (incluindo logística e doméstico), redução de erros em modelos PDDL gerados por LLM através de checagem de consistência e alcançabilidade (resumo).
- `[HIPÓTESE]` interpretação minha: mecanismos como este, se amadurecidos, poderiam eventualmente reduzir a dependência de modeladores humanos especialistas apontada em F3 — mas a checagem humana final ainda é mencionada como necessária, então a dependência não é eliminada, apenas reduzida.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução do PDF em https://arxiv.org/pdf/2404.07751. Conferência humana: pendente.
