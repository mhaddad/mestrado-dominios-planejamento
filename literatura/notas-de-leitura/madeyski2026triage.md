---
tipo: nota-de-leitura
eixo: E8
citekey: madeyski2026triage
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2604.07494
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A3]
fragilidades: []
perguntas: [Q3, Q4]
---

# Triage: Routing Software Engineering Tasks to Cost-Effective LLM Tiers via Code Quality Signals

**Madeyski, L. · 2026 · arXiv**
**Link/DOI:** https://arxiv.org/abs/2604.07494

## Extração estruturada

- **Problema:** agentes de codificação com IA roteiam toda tarefa para um único LLM de fronteira, pagando custo de inferência premium mesmo quando muitas tarefas são rotineiras e poderiam ser resolvidas por um modelo mais barato.
- **Método:** propõe o Triage, um framework que usa métricas de saúde de código (indicadores de manutenibilidade de software) como sinal de roteamento, atribuindo cada tarefa ao nível ("tier") de modelo mais barato cujo resultado passa no mesmo portão de verificação que o modelo caro passaria. Define três níveis de capacidade (leve, padrão, pesado — espelhando, por exemplo, Haiku, Sonnet, Opus) e compara três políticas de roteamento (limiares heurísticos, um classificador de aprendizado de máquina treinado, e um oráculo de "hindsight perfeito") no SWE-bench Lite (300 tarefas, três níveis de modelo).
- **Dados/benchmarks:** SWE-bench Lite (300 tarefas), avaliado sobre três tiers de modelo.
- **Resultado principal:** derivam analiticamente duas condições falseáveis sob as quais a assimetria dependente de tier (modelos médios se beneficiam de código limpo; modelos de fronteira não) torna o roteamento custo-efetivo: a taxa de acerto do tier leve em código saudável precisa exceder a razão de custo entre tiers, e a saúde do código precisa discriminar o tier de modelo necessário com pelo menos um efeito pequeno (p̂ ≥ 0,56).
- **Relação com a dissertação de 2010:** **A1, A3** [confirma por analogia direta, HIPÓTESE] — é, entre todo o lote, o artigo estruturalmente mais próximo de 2010: usa uma característica mensurável da "instância" (saúde/qualidade do código, análoga às métricas UML de 2010) para prever, antes de executar a tarefa, qual "técnica" (nível de modelo de LLM) terá melhor desempenho — a mesma lógica de A3 (ranking a partir de características do domínio, independente do problema específico), agora aplicada a tarefas de engenharia de software e modelos de linguagem.

## Pontos relevantes para o projeto

- É a peça mais forte do lote para a Q4: opera exatamente a lógica de "característica do domínio/tarefa → escolha de técnica/modelo" que está no núcleo de 2010, com formalização estatística explícita (condições falseáveis, efeito mínimo), algo que 2010 não tinha.
- Reutiliza explicitamente achados prévios (Borg et al., 2026, citado no artigo) de que código limpo melhora desempenho de modelos médios mas não de modelos de fronteira — evidência empírica de que o "ajuste" característica-modelo não é uniforme entre técnicas, ecoando a necessidade de 2010 de testar múltiplos planejadores, não um só.
- Trabalho muito recente (abril de 2026) e ainda não publicado em veículo revisado por pares (arXiv), o que pede cautela antes de tratá-lo como resultado consolidado.
- Não avaliei o desenho experimental completo (apenas resumo e introdução), portanto os resultados numéricos (p̂ ≥ 0,56 etc.) são citados como definidos pelo autor, não verificados em detalhe metodológico.

## Trechos literais

"the tier-dependent asymmetry (medium LLMs benefit from clean code while frontier models do not) yields cost-effective routing: the light-tier pass rate on healthy code must exceed the inter-tier cost ratio, and code health must discriminate the required model tier with at least a small effect size (p̂ ≥ 0.56)" (resumo).

## Marcações

- `[FATO]` O artigo define condições analíticas falseáveis sob as quais métricas de saúde de código predizem o tier de LLM necessário para uma tarefa, testando três políticas de roteamento no SWE-bench Lite (resumo e introdução).
- `[HIPÓTESE]` Esta é, entre os itens lidos neste lote, a analogia estrutural mais direta ao programa de pesquisa de 2010 (característica de domínio prediz técnica ótima), agora aplicada a agentes de IA e tarefas de engenharia de software — ligação central para a Q4, mas não afirmada pelo autor, que não cita 2010 nem planejamento automatizado.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução em https://arxiv.org/abs/2604.07494 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
