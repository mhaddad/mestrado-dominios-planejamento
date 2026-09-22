---
tipo: nota-de-leitura
eixo: E5
citekey: xie2023translating
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2302.05128 (PDF baixado, lidos resumo, introdução e discussão final)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: []
perguntas: [Q3]
---

# Translating Natural Language to Planning Goals with Large-Language Models

**Xie, Y.; Chen, Y.; Zhu, T.; Bai, J.; Gong, Z.; Soh, H. · 2023 · arXiv preprint**
**Link/DOI:** https://doi.org/10.48550/arxiv.2302.05128

## Extração estruturada

- **Problema:** se LLMs conseguem traduzir metas descritas em linguagem natural para uma linguagem de planejamento estruturada (PDDL), em vez de planejar diretamente.
- **Método:** estudo empírico com GPT-3.5 traduzindo instruções em inglês para metas PDDL em dois domínios (Blocksworld e ALFRED), com análise de subtarefas para identificar tipos de falha.
- **Dados/benchmarks:** domínios Blocksworld e ALFRED (ambiente doméstico realista).
- **Resultado principal:** LLMs são mais adequados para tradução do que para planejamento direto: conseguem completar metas subespecificadas usando conhecimento de senso comum, mas falham em tarefas que exigem raciocínio numérico ou espacial (ex.: contar objetos, relações hierárquicas), e são sensíveis ao prompt usado.
- **Relação com a dissertação de 2010:** sem relação direta com A1–A8 (não usa métricas UML nem planejadores das IPCs de 2010). Alimenta **Q3**: aqui o papel do LLM é de tradutor de linguagem natural para meta formal, um papel diferente do de planejador ou de modelador de domínio completo (comparar com guan2023leveraging).

## Pontos relevantes para o projeto

- Distingue empiricamente "LLM como tradutor" de "LLM como planejador", reforçando que o desempenho depende muito da tarefa específica atribuída ao LLM — relevante para a seção de LLMs (Q3) evitar generalizações.
- As falhas em raciocínio numérico/espacial ecoam, de forma qualitativa, a preocupação de 2010 com características estruturais do domínio (embora aqui a "característica" seja da tarefa em linguagem natural, não da UML).

## Trechos literais

"Our empirical results on GPT 3.5 variants show that LLMs are much better suited towards translation rather than planning" (resumo).

## Marcações

- `[FATO]` o artigo mostra, em Blocksworld e ALFRED, que GPT-3.5 traduz metas em linguagem natural para PDDL com sucesso em casos ambíguos comuns, mas falha em contagem e relações espaciais (introdução/resumo).
- `[HIPÓTESE]` interpretação minha: esse resultado sugere que a "característica do domínio" relevante para o desempenho de LLMs como tradutores pode não coincidir com as métricas estruturais UML de 2010 (número de classes, associações etc.), mas antes com o tipo de raciocínio exigido pela tarefa — ponto a explorar em Q2/Q3.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução do PDF em https://arxiv.org/pdf/2302.05128. Conferência humana: pendente.
