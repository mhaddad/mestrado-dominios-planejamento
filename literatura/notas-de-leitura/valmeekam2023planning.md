---
tipo: nota-de-leitura
eixo: E5
citekey: valmeekam2023planning
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2302.06706
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A5, A7]
fragilidades: [F5]
perguntas: [Q3]
---

# On the Planning Abilities of Large Language Models (A Critical Investigation with a Proposed Benchmark)

**Valmeekam, K.; Sreedharan, S.; Marquez, M.; Olmo, A.; Kambhampati, S. · 2023 · arXiv**
**Link/DOI:** https://arxiv.org/abs/2302.06706 (10.48550/arxiv.2302.06706)

## Extração estruturada

- **Problema:** investigação crítica e sistemática — anterior ao PlanBench completo — sobre se LLMs têm capacidade de planejamento autônomo, e, se não, se ao menos conseguem desempenhar papéis auxiliares úteis (fonte de heurística, assistente humano).
- **Método:** avalia o LLM em **três papéis**: (1) **planejador autônomo** (gera plano completo sozinho); (2) **gerador de heurística/sugestão** para um planejador clássico de busca local, o LPG, que recebe o plano do LLM como sugestão inicial em vez de partir do zero; (3) **assistente em ciclo humano-no-laço** (o plano do LLM é oferecido como sugestão a uma pessoa resolvendo o problema manualmente). Também compara com um baseline humano (50 participantes) e com uma versão da domínio ofuscada ("Mystery Blocksworld", criada por Drew McDermott) para testar se o desempenho reflete recuperação de padrões memorizados em vez de raciocínio.
- **Dados/benchmarks:** domínio Blocksworld (versão comum e versão Mystery/ofuscada, com disfarce determinístico e com disfarce aleatorizado por instância); conjuntos de até 600 instâncias por condição, com subconjuntos menores (ex.: 100) para tarefas mais caras computacionalmente.
- **Modelos e data:** **GPT-3** (`davinci`), **Instruct-GPT3** (`text-davinci-002`) e **BLOOM**, todos via API, artigo de 2023 (pré-GPT-4 para os experimentos principais; GPT-3 também testado com *fine-tuning* em instâncias de Blocksworld, à parte).
- **Resultado principal:** modo autônomo — geração de plano em Blocksworld: GPT-3 1%, Instruct-GPT3 6,8%, BLOOM 1,6% ("baseline humano preliminar = 78%"); em Mystery Blocksworld (ofuscação determinística), os três modelos ficam entre 0% e 1,1%; com ofuscação aleatorizada por instância, entre 0,1% e 0,8%. Modo heurístico: usando o plano do LLM como sugestão para o planejador LPG, houve "melhoria modesta" na qualidade/tempo do plano final, mas o *setup* segue dependente do planejador clássico para garantir correção. Modo humano-no-laço: dos participantes que receberam sugestão do LLM, 74–82% produziram um plano correto final, uma melhora sobre o grupo controle, mas sem diferença estatisticamente conclusiva relatada como forte.
- **Relação com a dissertação de 2010:** **A5** [confirma] — mesmo neste estudo mais antigo (pré-GPT-4), a queda de desempenho de GPT-3/Instruct-GPT3/BLOOM ao trocar o domínio comum por sua versão ofuscada logicamente equivalente (de ~1–7% para <1,1%) já demonstrava que características de superfície do domínio (aqui, os rótulos lexicais) determinam desempenho, um antecessor direto do mesmo achado em Valmeekam et al. (2024) e Kambhampati et al. (2024). **A7** [amplia] — o artigo já reporta, além da cobertura binária, o baseline humano de validade (78%) e de otimalidade condicional (89,7% dos planos válidos eram ótimos), uma granularidade maior que a métrica única de cobertura de 2010.

## Pontos relevantes para o projeto

- É a origem histórica (2023, pré-PlanBench definitivo) da taxonomia de três papéis (planejador autônomo, heurística, assistente humano) que reaparece, ampliada, em Kambhampati et al. (2024, LLM-Modulo); útil para reconstruir a cronologia da linha de pesquisa para a Q3.
- Fornece um baseline humano quantificado (78% de planos válidos, 89,7% de otimalidade condicional) — referência útil caso a revisão queira comparar desempenho humano vs. LLM vs. planejador clássico no mesmo domínio.
- Mostra que *fine-tuning* de GPT-3 (davinci) em instâncias de Blocksworld eleva a geração de plano de 1% para 16,4%, mas ainda "ao redor de 20%" no total — evidência de que ajuste específico de domínio ajuda, mas não resolve, relevante para discutir se "adaptação ao domínio" é uma variável equivalente às características estruturais de 2010.
- Só um domínio de planejamento automatizado testado (Blocksworld e sua variante ofuscada); não há dados aqui sobre variação entre domínios de planejamento distintos (Blocksworld vs. Logistics, por exemplo).

## Marcações

- `[FATO]` Tabela 1 (Geração de Plano, Blocksworld): GPT-3 "1%", Instruct-GPT3 "6.8%", BLOOM "1.6%"; baseline humano preliminar declarado como "78%" (seção 6.1, cabeçalho da tabela).
- `[FATO]` "Out of the 50 participants, 39 of them (78%) came up with a valid plan... 35 (89.7%) participants came up with an optimal plan" (seção 6.1.2, baseline humano).
- `[HIPÓTESE]` O uso do LLM como fonte de "heurística" para um planejador de busca local (LPG) é conceitualmente próximo ao que 2010 chamaria de auxiliar a uma técnica de *heuristic search*; se a revisão adotar essa leitura, este artigo já demonstra empiricamente (ainda que com ganho modesto) que um LLM pode contribuir como fonte de orientação heurística sem ser o planejador principal, o que é uma resposta parcial e antecipatória à Q3.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2302.06706 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
