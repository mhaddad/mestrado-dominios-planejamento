---
tipo: nota-de-leitura
eixo: E5
citekey: xie2024travelplanner
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://proceedings.mlr.press/v235/xie24j.html (resumo completo via página PMLR; PDF baixado de cópia espelhada no GitHub para conferência da introdução)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: [F5]
perguntas: [Q3]
---

# TravelPlanner: A Benchmark for Real-World Planning with Language Agents

**Xie, J.; Zhang, K.; Chen, J.; Zhu, T.; Lou, R.; Tian, Y.; Xiao, Y.; Su, Y. · 2024 · ICML 2024, v. 235, p. 54590-54613**
**Link/DOI:** https://doi.org/10.48550/arxiv.2402.01622

## Extração estruturada

- **Problema:** se agentes de linguagem (LLMs) conseguem planejar em cenários complexos do mundo real, fora do alcance de agentes de IA anteriores.
- **Método:** propõem um benchmark de planejamento de viagens com ambiente *sandbox* rico, ferramentas de acesso a quase quatro milhões de registros de dados e 1.225 intenções de planejamento com planos de referência, avaliando agentes de linguagem atuais.
- **Dados/benchmarks:** TravelPlanner (próprio benchmark), com GPT-4 e outros agentes de linguagem como sujeitos avaliados.
- **Resultado principal:** os agentes de linguagem atuais ainda não são capazes de lidar com tarefas de planejamento complexas — mesmo o GPT-4 atinge apenas 0,6% de taxa de sucesso; os agentes têm dificuldade em manter-se na tarefa, usar as ferramentas certas para coletar informação ou respeitar múltiplas restrições simultâneas.
- **Relação com a dissertação de 2010:** dialoga com **F5** (2010 reduz eficiência à cobertura): aqui a métrica de sucesso também é essencialmente binária (plano válido/atende restrições ou não), e o resultado extremamente baixo (0,6%) mostra como métricas de sucesso puro podem esconder nuances de desempenho parcial — reforça a crítica de que "eficiência = cobertura" é uma simplificação. Alimenta **Q3**.

## Pontos relevantes para o projeto

- Benchmark realista fora do domínio robótico, útil para contrastar com os domínios de planejamento clássico (logística, blocksworld etc.) usados em 2010.
- O resultado de 0,6% de sucesso do GPT-4 é um dado forte para calibrar expectativas sobre "LLM como planejador direto" na seção de LLMs (Q3), distinto dos papéis de tradutor/gerador de modelo vistos em outras notas deste lote.
- Os autores reconhecem que a mera possibilidade de testar um problema dessa complexidade já é um progresso não trivial, o que é uma leitura mais otimista que os números brutos sugerem.

## Trechos literais

"Comprehensive evaluations show that the current language agents are not yet capable of handling such complex planning tasks—even GPT-4 only achieves a success rate of 0.6%" (resumo).

## Marcações

- `[FATO]` o artigo mede, com um benchmark próprio de 1.225 intenções de planejamento, uma taxa de sucesso de 0,6% para GPT-4 em tarefas de planejamento de viagem (resumo).
- `[HIPÓTESE]` interpretação minha: esse número extremamente baixo sugere que, para tarefas de alta complexidade combinatória e múltiplas restrições, LLMs como planejadores diretos ainda estão muito aquém dos planejadores clássicos da IPC usados em 2010 — a confirmar comparando com dados de cobertura dos planejadores de 2010.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura do resumo completo na página PMLR (https://proceedings.mlr.press/v235/xie24j.html) e da introdução no PDF (cópia mlresearch/v235 no GitHub). Conferência humana: pendente.
