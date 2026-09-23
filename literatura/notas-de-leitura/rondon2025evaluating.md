---
tipo: nota-de-leitura
eixo: E8
citekey: rondon2025evaluating
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2501.07531
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A3]
fragilidades: []
perguntas: [Q4]
---

# Evaluating Agent-based Program Repair at Google

**Rondon, P.; Wei, R.; Cambronero, J.; Cito, J.; Sun, A.; Sanyam, S.; Tufano, M.; Chandra, S. · 2025 (ICSE-SEIP 2025) · arXiv**
**Link/DOI:** https://arxiv.org/abs/2501.07531 (registro DOI do lote: 10.1109/icse-seip66354.2025.00038; PDF de acesso aberto localizado via busca, pois `texto_integral_url` do lote estava vazio)

## Extração estruturada

- **Problema:** viabilidade de reparo automático de programas por agente de LLM em contexto industrial (Google), fora da distribuição de projetos abertos em que *benchmarks* como SWE-Bench foram construídos.
- **Método:** *benchmark* próprio (não ensaio com humanos). Constroem o GITS-Eval, 178 *bugs* reais do sistema interno de rastreamento de *issues* do Google (GITS), com filtragem em três fases documentadas (tamanho de patch < 150 linhas, exclusão de multimídia, testes não instáveis, exclusão de "constantes mágicas" não inferíveis do contexto). Implementam o Passerine, agente "similar in spirit to SWE-Agent" adaptado ao ambiente interno do Google, rodando sobre Gemini 1.5 Pro (`gemini-1.5-pro-001`, *temperature*=0,2, *top-p*=0,95), com 20 amostras de trajetória independentes por *bug*, até 25 passos cada.
- **Dados/benchmarks:** GITS-Eval = 78 *bugs* reportados por humanos + 100 *bugs* reportados por máquina, subdivididos em 50 SAN (sanitizadores automáticos) e 50 TOD (analisador de dependência de ordem de teste). *Patches* datados de amostragem entre 26/06 e um ano de corte anterior (Tabela III, "Bug Creation Cutoff... no earlier than one year before the patch date range start").
- **Resultado principal:** taxa de patch plausível (passa nos testes) muito diferente por tipo de *bug* — SAN 78%, TOD 68%, humano 25,6%; taxa de patch válido (semanticamente equivalente ao *ground truth*, após revisão manual) — SAN 62%, TOD 24%, humano 17,9% (Tabela IV). O artigo também identifica "*smells*" comportamentais na trajetória do agente que variam sistematicamente por tipo de *bug*: buscas consecutivas repetidas (`CONSECUTIVE_SEARCH`) são mais comuns em *bugs* humanos, e edições consecutivas no mesmo arquivo (`CONSECUTIVE_EDIT`) são mais comuns em SAN/TOD.
- **Relação com a dissertação de 2010:** **A1** e **A3** [confirma por analogia direta, HIPÓTESE] — a mesma técnica (Passerine/Gemini 1.5 Pro), sem qualquer alteração de modelo ou estratégia, produz desempenho de 78% a 25,6% dependendo exclusivamente do tipo/origem do *bug* (característica da tarefa, análoga a característica do domínio em 2010). O artigo chega a atribuir a causa a características estruturais da tarefa — localização (buscabilidade, dispersão espacial da mudança) e diversidade de linguagem — de forma muito próxima ao raciocínio de 2010 sobre por que métricas estruturais do domínio predizem desempenho do planejador.

## Pontos relevantes para o projeto

- É o dado mais limpo do lote para Q4: mesma técnica, mesmo modelo, variação de 52 pontos percentuais (78% → 25,6%) apenas por tipo de tarefa — evidência quantitativa direta de que características da tarefa predizem desempenho do agente, tal como 2010 propõe para domínios de planejamento.
- Table V liga tipo de *bug* a padrões comportamentais mensuráveis da trajetória do agente (buscas vs. edições repetidas), abrindo caminho para uma métrica "estrutural" da tarefa de reparo, análoga às métricas UML de 2010.
- Explicita as dimensões da tarefa que dificultam localização: buscabilidade textual da descrição, dispersão espacial das mudanças, diversidade de linguagem (Java, C++, TypeScript, Kotlin, Python vs. só Python em SWE-Bench) — candidatas a "características de domínio" para reparo de código.
- Compara diretamente a distribuição de *bugs* do GITS com a do SWE-Bench, mostrando que um *benchmark* popular pode não generalizar para um ambiente industrial — ponto relevante para qualquer generalização de resultados de *benchmark* em Q4.

## Marcações

- `[FATO]` "% bugs with plausible patch ... SAN 78% ... TOD 68% ... Human 25.6%" e "% bugs with valid patch ... SAN 62% ... TOD 24% ... Human 17.9%" (Tabela IV).
- `[FATO]` "Table V shows that human bugs are more likely to perform repeated consecutive searches (CONSECUTIVE_SEARCH)... Both SAN and TOD trajectories... the agent is more likely to perform repeated edits on the same file (CONSECUTIVE_EDIT)" (seção V, discussão da Tabela V).
- `[FATO]` "with 20 trajectory samples and Gemini 1.5 Pro, Passerine can produce a patch that passes bug tests (i.e., plausible) for 73% of machine-reported and 25.6% of human-reported bugs" (resumo).
- `[HIPÓTESE]` A magnitude da variação (mais que o triplo, de 25,6% a 78%, usando a mesma técnica) sugere que, tal como em 2010, o "ranking" de qual estratégia funciona melhor não é fixo — depende de características observáveis da tarefa/domínio (aqui, origem e estrutura do *bug*) — o que reforça diretamente a plausibilidade da Q4.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2501.07531 (PDF baixado do arXiv, extraído com pdftotext; a URL do lote fornecia apenas o registro Crossref pelo DOI, sem PDF; localizei a versão de acesso aberto por busca web). Conferência humana: pendente.
