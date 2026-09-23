---
tipo: nota-de-leitura
eixo: E5
citekey: valmeekam2023planbench
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2206.10498
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5, A7]
fragilidades: [F5]
perguntas: [Q3]
---

# PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change

**Valmeekam, K.; Marquez, M.; Olmo, A.; Sreedharan, S.; Kambhampati, S. · 2022 (NeurIPS 2023, Track on Datasets and Benchmarks) · arXiv**
**Link/DOI:** https://arxiv.org/abs/2206.10498 (10.52202/075280-1693)

## Extração estruturada

- **Problema:** construir um *benchmark* extensível para avaliar se LLMs têm capacidade genuína de planejamento e raciocínio sobre mudança, em vez de mera recuperação de padrões, usando domínios do estilo das IPCs.
- **Método:** papel do LLM = **planejador direto** (geração autônoma de planos a partir de descrição em linguagem natural do domínio e do problema, few-shot). O framework é domínio-independente na geração/verificação de instâncias (usa Fast Downward como planejador de referência e VAL como validador) e domínio-dependente na tradução PDDL↔linguagem natural. Também inclui tarefas auxiliares (verificação de plano, raciocínio sobre execução, replanejamento, generalização de plano, otimalidade de custo).
- **Dados/benchmarks:** dois domínios da IPC — Blocksworld e Logistics —, cada um com uma versão ofuscada ("Mystery Blocksworld", nomes de predicados/ações trocados por termos enganosos ou *strings* alfanuméricas aleatórias). ~26.250 *prompts* no total.
- **Resultado principal:** avaliação inicial ("*specimen evaluation*") com **GPT-4** (versão usada entre março e junho de 2023, janela de contexto de 8k) e **Instruct-GPT3** (`text-davinci-002`), temperatura 0. Na Geração de Plano em Blocksworld, GPT-4 acerta 206/600 (34,3%) contra 41/600 (6,8%) do Instruct-GPT3. Na versão ofuscada Mystery Blocksworld (mesma estrutura lógica, só os nomes mudam), o desempenho desaba: GPT-4 cai a 26/600 (4,3%) e Instruct-GPT3 a 14/600 (0,23%).
- **Relação com a dissertação de 2010:** **A5** [confirma, com ressalva] — a obra mostra que uma característica "de superfície" do domínio (os nomes usados, não a estrutura lógica) já altera drasticamente o desempenho do "planejador" (LLM); isso é consistente com a tese de que características do domínio afetam o desempenho da técnica, mas desloca a discussão: em 2010 a complexidade estrutural (UML) é o que varia; aqui o que varia é a robustez semântica do LLM diante de rótulos, o que sugere que, para LLMs, a "característica do domínio" relevante inclui aspectos lexicais que não têm equivalente nas métricas UML de 2010. **A7** [amplia] — a obra usa um critério de eficiência mais rico que cobertura simples (conjunto de tarefas: geração, verificação, execução, replanejamento, generalização, otimalidade), o que é um contraponto à redução de 2010 a cobertura.

## Pontos relevantes para o projeto

- Evidência clara e citável de forte variação de desempenho de um LLM entre duas versões do "mesmo" domínio (estrutura idêntica, nomes diferentes) — dado direto para a seção sobre Q3 e para discutir se "características do domínio" precisam incluir fatores lexicais quando o "planejador" é um LLM.
- O framework de avaliação (gerador de instância domínio-dependente + verificador domínio-independente) é reaproveitado por praticamente todos os outros trabalhos do eixo E5 lidos neste lote (Kambhampati et al. 2024, Valmeekam et al. 2024, Stechly et al. 2024), o que datou uma linhagem metodológica.
- Data e versão do modelo registradas de forma explícita no texto (GPT-4, março–junho de 2023, contexto 8k) — importante porque os números "envelhecem"; comparar com Valmeekam et al. (2024) mostra queda/estagnação em relação a versões posteriores de GPT-4 avaliadas por outros autores.
- Repositório do *benchmark* é público e versionado (GitHub), o que permite reprodução.

## Marcações

- `[FATO]` GPT-4 (mar.–jun. 2023) acerta 34,3% das instâncias de geração de plano em Blocksworld e cai para 4,3% na versão ofuscada Mystery Blocksworld, com estrutura logicamente idêntica ("Table 2... Mystery Blocksworld (Deceptive) 26/600 (4.3%)... Table 1... Plan Generation... 206/600 (34.3%)").
- `[HIPÓTESE]` A fragilidade dos LLMs a ofuscação lexical sugere que, se um dia se quiser repetir o estudo de 2010 usando LLM como "planejador", será preciso controlar (ou pelo menos registrar) o vocabulário do domínio como uma variável independente adicional, algo sem paralelo nas métricas estruturais de UML usadas em 2010.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2206.10498 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
