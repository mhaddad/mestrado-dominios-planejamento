---
tipo: nota-de-leitura
eixo: E5
citekey: kambhampati2024llms
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2402.01817
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A5, A7]
fragilidades: [F5]
perguntas: [Q3]
---

# Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks

**Kambhampati, S.; Valmeekam, K.; Guan, L.; Verma, M.; Stechly, K.; Bhambri, S.; Saldyt, L. P.; Murthy, A. B. · 2024 (ICML 2024) · arXiv**
**Link/DOI:** https://proceedings.mlr.press/v235/kambhampati24a.html (10.48550/arxiv.2402.01817)

## Extração estruturada

- **Problema:** artigo de posição — argumenta que LLMs autorregressivos não conseguem planejar nem se autoverificar sozinhos, mas têm papéis construtivos como fontes aproximadas de conhecimento e geradores de planos-candidatos, desde que acoplados a verificadores externos sólidos ("LLM-Modulo").
- **Método:** papel do LLM = **gerador de planos-candidatos / fonte de conhecimento aproximado**, nunca planejador nem verificador autônomo. Revisão e síntese de resultados empíricos próprios (PlanBench e variantes) mais dois estudos de caso de arquitetura "LLM-Modulo" com *back-prompting* a partir de um verificador externo (VAL).
- **Dados/benchmarks:** Blocksworld e Mystery Blocksworld (versão ofuscada/enganosa) do PlanBench; estudo de caso adicional em planejamento de viagens (benchmark de Xie et al. 2024).
- **Modelos e data:** comparação explícita entre gerações de modelo — **GPT-4** (206/600, "specimen" original de 2023), **GPT-4-Turbo**, **GPT-4o**, **Claude-3-Opus**, **Gemini Pro**, **LLaMA-3 70B** — todos avaliados no mesmo *setup* de geração de plano em linguagem natural (Tabela 1, artigo publicado em junho de 2024).
- **Resultado principal:** Tabela 1 (*one-shot*, Blocksworld): GPT-4 34,3%, GPT-4-Turbo 23%, GPT-4o 28,3%, Claude-3-Opus 48,2%, LLaMA-3 70B 12,6%, Gemini Pro 11,3% — nenhum modelo, incluindo os mais recentes, ultrapassa ~50%. Na versão ofuscada Mystery Blocksworld (*deceptive*, *one-shot*), todos caem para 0,8–4,3%. O texto afirma: "on average, only about 12% of the plans that the best LLM (GPT-4) generates are actually executable without errors and goal-reaching" e "the choice of LLM doesn't have much bearing on this". Com *back-prompting* de um verificador externo sólido (VAL), o desempenho em Blocksworld sobe a 82% em até 15 rodadas e em Logistics a 70%, mas em Mystery Blocksworld o LLM-Modulo só alcança ~10%, porque o LLM tem dificuldade de gerar sequer candidatos plausíveis nesse domínio.
- **Relação com a dissertação de 2010:** **A5** [confirma fortemente, com mecanismo distinto] — a variação de desempenho por domínio/versão do domínio persiste mesmo trocando de modelo e de geração de LLM, e mesmo acoplando um verificador externo (LLM-Modulo): a arquitetura ajuda em domínios "normais" (Blocksworld, Logistics) mas não resolve o domínio ofuscado, porque ali o problema é a geração de candidatos, não a verificação. Isso indica que "característica do domínio" relevante para desempenho de LLM inclui o quanto o domínio se distancia do que está memorizado no treinamento, uma dimensão ausente nas métricas estruturais de 2010. **A7** [amplia] — o critério de sucesso é "plano executável sem erros e que atinge a meta", equivalente a cobertura binária por instância, então nesse ponto o critério é comparável ao de 2010.

## Pontos relevantes para o projeto

- É a fonte mais rica do lote para "que modelos, em que data": tabela única comparando 6 LLMs/versões (GPT-4, GPT-4-Turbo, GPT-4o, Claude-3-Opus, Gemini Pro, LLaMA-3 70B) no mesmo protocolo — útil para cravar "estado da arte em junho de 2024".
- Formula explicitamente a taxonomia de papéis que a Q3 pede: "front-end/back-end format translator" (papel considerado insuficiente) vs. "gerador de ideias/planos-candidatos dentro de um LLM-Modulo Framework com verificadores externos sólidos" (papel defendido pelos autores).
- Mostra que *scaling* e troca de geração de modelo (GPT-4 → GPT-4o/Turbo, ou para Claude/Gemini/LLaMA) não resolveu o problema de fundo — dado importante para qualquer discussão sobre "os resultados envelhecem rápido": aqui, especificamente, não envelheceram na direção de melhora.
- Estudo de caso quantifica quanto um verificador externo pode compensar a fragilidade do LLM, mas mostra um teto rígido em domínios ofuscados (~10%), o que é evidência direta de interação entre característica do domínio e eficácia da técnica (aqui, arquitetura LLM+verificador).

## Marcações

- `[FATO]` Tabela 1: em Blocksworld *one-shot*, GPT-4 acerta 34,3%, Claude-3-Opus 48,2% e Gemini Pro apenas 11,3%; na versão ofuscada Mystery Blocksworld *one-shot*, todos os modelos caem para 0,8–4,3% ("GPT-4o... (28.33%)... Claude-3-Opus... (48.17%)"; "Mystery BW (Deceptive)... (0.83%)... (4.3%)").
- `[FATO]` Com *back-prompting* de verificador externo (VAL), "LLM performance in Blocks World improves to 82% within 15 back prompting rounds, while in Logistics, it improves to 70%... LLM-Modulo doesn't help as much in an obfuscated version of blocks world called Mystery BW, reaching about 10% accuracy."
- `[HIPÓTESE]` O teto de ~10% em Mystery Blocksworld mesmo com verificador externo sugere que, para arquiteturas LLM-Modulo, a "característica do domínio" que mais importa não é a complexidade estrutural (no sentido UML de 2010), e sim a distância lexical/semântica entre o domínio e o que está representado no treinamento do modelo — um eixo de análise que uma extensão de 2010 para a era dos LLMs precisaria acrescentar, não substituir.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2402.01817 (PDF baixado do arXiv, extraído com pdftotext; o link de registro fornecido, proceedings.mlr.press, aponta para a mesma versão ICML). Conferência humana: pendente.
