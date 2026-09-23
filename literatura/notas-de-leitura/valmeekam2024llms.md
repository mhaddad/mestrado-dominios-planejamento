---
tipo: nota-de-leitura
eixo: E5
citekey: valmeekam2024llms
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2409.13373
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5, A7]
fragilidades: [F5]
perguntas: [Q3]
---

# LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench

**Valmeekam, K.; Stechly, K.; Kambhampati, S. · 2024 · arXiv**
**Link/DOI:** https://arxiv.org/abs/2409.13373 (10.48550/arxiv.2409.13373)

## Extração estruturada

- **Problema:** reavaliar o PlanBench com a chegada de um novo tipo de modelo, o "Large Reasoning Model" (LRM) da OpenAI, série o1 (Strawberry), testando se a alegada capacidade de raciocínio supera as limitações de planejamento observadas em LLMs autorregressivos convencionais.
- **Método:** papel do LLM/LRM = **planejador direto** (geração autônoma de plano em linguagem natural a partir da descrição do domínio, mesmo protocolo do PlanBench original). Compara LLMs convencionais entre si e com os LRMs o1-preview e o1-mini; também testa robustez a obfuscação (Mystery Blocksworld e uma versão "Randomized Mystery Blocksworld", com nomes de predicados/objetos sorteados por instância para reduzir risco de vazamento de dados de treino) e a comprimento de plano (subconjunto exigindo planos de 20 a 40 passos).
- **Dados/benchmarks:** 600 instâncias de Blocksworld (3 a 5 blocos) e as mesmas 600 em Mystery Blocksworld, do PlanBench; mais um subconjunto de 110 instâncias de Blocksworld exigindo planos de 20–40 passos; mais um teste de detecção de problemas insolúveis (100 instâncias insolúveis + 600 solúveis).
- **Modelos e data:** avaliação "no momento da escrita, o1-preview e o1-mini estavam disponíveis havia uma semana" (artigo de 20/09/2024) — LRMs **o1-preview** e **o1-mini**, comparados na mesma tabela com GPT-4, GPT-4-Turbo, GPT-4o, Claude-3-Opus, Gemini Pro e LLaMA-3.1 405B.
- **Resultado principal:** em Blocksworld regular, o melhor LLM convencional (LLaMA 3.1 405B) chega a 62,6%; **o1-preview** salta para **97,8%**. Em Mystery Blocksworld, nenhum LLM convencional passa de 5%, enquanto o1-preview atinge **52,8%** e, na versão Randomized Mystery Blocksworld, **37,3%**. Mas o desempenho de o1-preview degrada com o aumento do número de passos exigidos: no subconjunto de 20–40 passos, cai para **23,63%**. O texto conclui explicitamente que "performance on one version of the domain does not clearly predict performance on the other" entre Blocksworld normal e a versão ofuscada.
- **Relação com a dissertação de 2010:** **A5** [confirma e refina] — mesmo com um salto de arquitetura (LRM com cadeia de raciocínio interna, não apenas LLM autorregressivo), o desempenho continua fortemente dependente da versão do domínio (nomes ofuscados) e, adicionalmente, do comprimento do plano exigido — uma dimensão de complexidade que também não está nas métricas estruturais UML de 2010, mas que é análoga em espírito a "quanto o domínio exige de profundidade de busca". **A7** [amplia] — o critério de sucesso permanece binário por instância (cobertura), comparável ao de 2010, mas o artigo acrescenta a dimensão custo computacional/tempo por resposta como achado relevante, algo que 2010 explicitamente exclui (A7 original).

## Pontos relevantes para o projeto

- É a fonte do lote com a data e a versão mais precisas e mais recentes de modelo (o1-preview e o1-mini, testados na primeira semana de disponibilidade, setembro de 2024) — ilustra concretamente a instrução do prompt sobre "resultados que envelhecem rápido": o salto de 34,3% (GPT-4, 2023) para 97,8% (o1-preview, Blocksworld normal) em pouco mais de um ano.
- Confirma, com um modelo de arquitetura distinta, o mesmo padrão qualitativo de forte variação por domínio/versão de domínio já visto em Kambhampati et al. (2024) e Valmeekam et al. (2023) — evidência de robustez do fenômeno através de gerações de modelo.
- Introduz explicitamente o comprimento do plano (profundidade de busca) como variável que degrada desempenho mesmo dentro do "mesmo" domínio — ponto a discutir na seção sobre limites de generalização de A3/A5 para a era LLM.
- Nota metodológica relevante: os autores mudam a ofuscação para "aleatorizada por instância" (Randomized Mystery Blocksworld) especificamente para reduzir a chance de vazamento de dados de treino/memorização — mostra amadurecimento metodológico da linha de pesquisa desde o PlanBench original (2022).

## Marcações

- `[FATO]` "the best performance on regular Blocksworld is achieved by LLaMA 3.1 405B with 62.6% accuracy... no LLM achieves even 5% on our test set [Mystery Blocksworld]... performance on one version of the domain does not clearly predict performance on the other" (seção de resultados, comparando Tabela 1).
- `[FATO]` "Far surpassing any LLM, o1 correctly answers 97.8% of these instances [Blocksworld]... answering 52.8% correctly [Mystery Blocksworld]... 37.3% of instances are answered correctly [Randomized Mystery Blocksworld]" (Tabela 2 e texto associado); e "over these 110 instances [20-40 passos], o1-preview only manages 23.63%".
- `[HIPÓTESE]` O fato de o salto de arquitetura (LRM) melhorar substancialmente o desempenho médio, mas não eliminar a dependência de domínio/comprimento de plano, sugere que a relação característica-de-domínio × desempenho não é um artefato específico de uma geração de LLM, e sim algo mais estrutural — o que reforça a relevância de perguntar (Q3) que papel um LLM/LRM deveria assumir (planejador vs. auxiliar de um planejador clássico) em vez de perguntar apenas "qual modelo é melhor".

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2409.13373 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
