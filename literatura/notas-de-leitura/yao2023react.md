---
tipo: nota-de-leitura
eixo: E5
citekey: yao2023react
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2210.03629 (PDF baixado, lidos resumo e introdução)
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: []
perguntas: [Q3]
---

# ReAct: Synergizing Reasoning and Acting in Language Models

**Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.; Cao, Y. · 2022/2023 · ICLR 2023**
**Link/DOI:** arXiv:2210.03629

## Extração estruturada

- **Problema:** raciocínio (ex.: *chain-of-thought*) e ação (ex.: geração de planos de ação) em LLMs eram estudados como tópicos separados; o artigo busca explorar a sinergia entre os dois.
- **Método:** propõem o ReAct, técnica que gera de forma intercalada traços de raciocínio e ações específicas de tarefa: o raciocínio ajuda a induzir, rastrear e atualizar planos de ação e lidar com exceções; as ações permitem interface com fontes externas de informação (bases de conhecimento, ambientes).
- **Dados/benchmarks:** conjunto diverso de tarefas de linguagem e tomada de decisão (não detalhado nas 35 primeiras linhas lidas).
- **Resultado principal:** ReAct supera baselines do estado da arte em tarefas de linguagem e decisão, segundo o resumo.
- **Relação com a dissertação de 2010:** sem relação direta com A1–A8 (técnica de agentes de linguagem, não planejador clássico independente de domínio). Alimenta **Q3**: ReAct é citado amplamente como base de agentes de planejamento com LLM, incluindo vários outros trabalhos deste lote (ex.: huang2024understanding cita ReAct na sua taxonomia de "External Module"/raciocínio).

## Pontos relevantes para o projeto

- É um dos artigos fundacionais mais citados da linha de "agentes de LLM", útil como referência de base para contextualizar a seção de LLMs (Q3), mesmo sem ligação direta com domínios de planejamento clássico.
- Relevante compreender que ReAct não é, em si, um planejador — é uma técnica de prompting que intercala raciocínio e ação, o que pode ser confundido com "planejamento" em discussões menos precisas.

## Trechos literais

"We explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two" (resumo).

## Marcações

- `[FATO]` o artigo apresenta e avalia empiricamente o método ReAct, mostrando ganhos sobre baselines em tarefas de decisão e linguagem (resumo).
- `[HIPÓTESE]` interpretação minha: por ser citado como base por quase todos os outros trabalhos de LLM-planejamento deste lote, ReAct provavelmente merece menção introdutória na seção de LLMs da revisão, mesmo não tratando diretamente da relação domínio-técnica de 2010.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução do PDF em https://arxiv.org/pdf/2210.03629. Conferência humana: pendente.
