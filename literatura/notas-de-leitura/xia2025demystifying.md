---
tipo: nota-de-leitura
eixo: E8
citekey: xia2025demystifying
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2407.01489
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A2, A6]
fragilidades: [F4]
perguntas: [Q3, Q4]
---

# Demystifying LLM-Based Software Engineering Agents (Agentless)

**Xia, C. S.; Deng, Y.; Dunn, S.; Zhang, L. · 2025 (versão publicada; preprint arXiv 2024) · Proc. ACM Softw. Eng. (FSE)**
**Link/DOI:** https://doi.org/10.1145/3715754 (texto lido via preprint aberto arXiv:2407.01489)

## Extração estruturada

- **Problema:** questionar se é realmente necessário empregar agentes autônomos de software complexos (com decisão de ações, ferramentas e observação de ambiente) para resolver tarefas de desenvolvimento de software de ponta a ponta, dada a complexidade desses agentes e as limitações dos LLMs atuais.
- **Método:** constroem o AGENTLESS, uma abordagem "sem agente" que resolve problemas de desenvolvimento de software em três fases simples e sequenciais — localização, reparo e validação de patch — sem deixar o LLM decidir ações futuras ou operar com ferramentas complexas; comparam com abordagens baseadas em agentes no benchmark SWE-bench Lite. Também classificam manualmente os problemas do SWE-bench Lite, identificando problemas com *patches* de referência exatos ou descrições de issue insuficientes/enganosas, e constroem o SWE-bench Lite-S excluindo esses casos problemáticos.
- **Dados/benchmarks:** SWE-bench Lite (e a versão curada SWE-bench Lite-S, construída pelos próprios autores).
- **Resultado principal:** a abordagem simplista AGENTLESS alcança o maior desempenho (32,00%, 96 correções corretas) e o menor custo ($0,70) em comparação com todos os agentes de software de código aberto existentes na época; foi adotada pela OpenAI como abordagem de referência para demonstrar o desempenho de codificação no mundo real de GPT-4o e o1.
- **Relação com a dissertação de 2010:** **A2** [corrige, HIPÓTESE] — 2010 supôs que técnicas mais sofisticadas (busca heurística, hierárquica etc.) seriam as mais promissoras; este artigo mostra, no domínio de agentes de IA para SE, o oposto: uma abordagem simples e não-agentiva supera abordagens agentivas complexas na tarefa testada, o que desafia a suposição implícita de que "mais sofisticado é melhor" presente em A2. **A6** [torna obsoleta parcialmente, HIPÓTESE] — a taxonomia de técnicas de 2010 (forward-chaining, plan-space etc.) não se aplica a agentes de LLM; este artigo propõe uma taxonomia distinta (agente vs. não-agente / localização-reparo-validação) para esse novo domínio, sinalizando que qualquer generalização de 2010 para a Q4 precisa de taxonomia própria. **F4** [ajuda a tratar, HIPÓTESE] — reforça que a discussão sobre taxonomia de técnicas é uma fragilidade viva também no domínio de agentes de IA, não uma exclusividade de 2010.

## Pontos relevantes para o projeto

- É o achado metodológico mais forte do lote de E8 sobre ajuste tarefa-técnica: mostra que, para a tarefa "resolver issues do SWE-bench Lite", uma técnica simples supera técnicas complexas — achado que teoricamente poderia informar a Q4, mas o artigo não caracteriza a tarefa por métricas estruturais (não é ajuste "por características do domínio" no sentido de 2010).
- É a versão publicada e canônica do Agentless, com classificação manual dos problemas do benchmark que expõe fragilidades do próprio benchmark (patches de referência problemáticos) — ponto de rigor metodológico relevante para qualquer trabalho futuro que use SWE-bench como benchmark análogo às IPCs de 2010.
- Não estabelece relação de causalidade entre características de tarefa e desempenho da técnica; o resultado é agregado (desempenho médio no benchmark), não desagregado por tipo de issue — limite direto para uso na Q4 sem trabalho adicional.

## Trechos literais

"the simplistic AGENTLESS is able to achieve both the highest performance (32.00%, 96 correct fixes) and low cost ($0.70) compared with all existing open-source software agents" (resumo).

## Marcações

- `[FATO]` AGENTLESS, uma abordagem de três fases sem decisão autônoma do LLM, superou agentes de software mais complexos em desempenho e custo no SWE-bench Lite, sendo adotada pela OpenAI como referência (resumo).
- `[HIPÓTESE]` Esse resultado desafia a suposição de 2010 (A2) de que técnicas mais sofisticadas tendem a ser mais promissoras, e mostra que a taxonomia de técnicas de 2010 (A6) não se transpõe diretamente para agentes de LLM em engenharia de software — mas o artigo não faz essa comparação com 2010, é interpretação minha.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão no preprint aberto https://arxiv.org/abs/2407.01489 (PDF baixado, extraído com pdftotext); a versão publicada (DOI 10.1145/3715754) está bloqueada por paywall da ACM. Conferência humana: pendente.
