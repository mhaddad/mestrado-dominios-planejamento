---
tipo: nota-de-leitura
eixo: E8
citekey: yang2024sweagent
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2405.15793
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: []
perguntas: [Q4]
---

# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**Yang, J.; Jimenez, C. E.; Wettig, A.; Lieret, K.; Yao, S.; Narasimhan, K.; Press, O. · 2024 (NeurIPS 2024) · arXiv**
**Link/DOI:** https://arxiv.org/abs/2405.15793 (10.48550/arxiv.2405.15793)

## Extração estruturada

- **Problema:** desenho experimental sobre *agent-computer interfaces* (ACI): como o formato das ferramentas que um agente de LLM usa para navegar repositórios, editar arquivos e rodar testes afeta seu desempenho em tarefas reais de engenharia de software.
- **Método:** desenho de sistema mais avaliação comparativa (não é ensaio com humanos). Introduz o SWE-agent, com uma ACI própria (comandos de busca, visualização e edição de arquivo com *linting* automático), e compara com dois baselines: (i) geração não interativa por *retrieval-augmented generation* (RAG com BM25) e (ii) um agente "Shell-only" que interage apenas via *shell* Linux, sem ACI dedicada. Avaliação com modelos de fronteira do período: GPT-4 Turbo (`gpt-4-1106-preview`) e Claude 3 Opus (`claude-3-opus-20240229`); testaram também Llama 3 e DeepSeek Coder, descartados por desempenho fraco em ambiente de agente.
- **Dados/benchmarks:** SWE-bench (completo e SWE-bench Lite) e HumanEvalFix. Métrica principal: `% Resolved` (*pass@1* — proporção de instâncias em que todos os testes passam após o *patch* gerado).
- **Resultado principal:** estado da arte em ambos os *benchmarks* no momento da publicação, com *pass@1* de 12,5% em SWE-bench e 87,7% em HumanEvalFix — "achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively" (resumo). Em seis execuções repetidas na SWE-bench Lite (Tabela 10, GPT-4), a taxa de resolução variou entre 17,33% e 18,67% (média 17,94% ± 0,49), com *pass@k* subindo a 32,67% para k=6 — variância entre execuções baixa, mas resolução por instância mudando consideravelmente.
- **Relação com a dissertação de 2010:** **A1** [analogia, HIPÓTESE] — a diferença brutal de desempenho entre SWE-bench (reparo de *issues* em repositórios reais e extensos, 12,5%) e HumanEvalFix (correção de funções isoladas e curtas, 87,7%) usando exatamente o mesmo agente e os mesmos modelos é evidência de que a *tarefa* (escopo do problema, tamanho do contexto necessário, grau de integração com um repositório) determina o desempenho tanto ou mais que o modelo escolhido — paralelo direto com a tese central de 2010 de que características do domínio (não só a técnica) predizem desempenho. Diferente de 2010, o artigo não decompõe SWE-bench em características estruturais do problema; a variação fica em nível de *benchmark* inteiro, não de instância.

## Pontos relevantes para o projeto

- Fonte primária para a arquitetura de agente de codificação que a maioria dos trabalhos do lote usa ou compara (Passerine em rondon2025evaluating é descrito como "similar in spirit to SWE-Agent").
- O contraste de *pass@1* entre dois *benchmarks* de granularidade diferente (função isolada vs. repositório) é o dado mais direto do artigo para Q4, mesmo sem quebra por características internas de cada tarefa.
- Não há ensaio com desenvolvedores humanos nem medição de heterogeneidade por características do repositório dentro do SWE-bench; é fonte sobre capacidade do agente, não sobre uso humano-IA.

## Marcações

- `[FATO]` "We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively" (resumo).
- `[FATO]` "Resolve % ... 17.33 18.00 18.00 18.67 17.33 18.33 17.94±0.49" e "Pass@k ... 17.94 23.89 27.35 29.67 31.33 32.67" (Tabela 10, seis execuções em SWE-bench Lite com GPT-4).
- `[HIPÓTESE]` A lacuna de 75 pontos percentuais entre os dois *benchmarks* sugere que o "tipo de tarefa" (função isolada vs. reparo em repositório real) é uma variável tão ou mais forte que o modelo/ferramenta na predição de sucesso do agente — analogia direta com A1 e A3 de 2010, mas sem a decomposição estrutural que 2010 fazia por domínio.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2405.15793 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
