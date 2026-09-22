---
tipo: nota-de-leitura
eixo: E5
citekey: stechly2025self
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2402.08115
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A5, A7]
fragilidades: [F5]
perguntas: [Q3]
---

# On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks

**Stechly, K.; Valmeekam, K.; Kambhampati, S. · 2024 (ICLR 2025) · arXiv**
**Link/DOI:** https://arxiv.org/abs/2402.08115 (10.48550/arxiv.2402.08115)

## Extração estruturada

- **Problema:** testar sistematicamente se um LLM consegue se autoverificar/autocriticar de forma eficaz em tarefas de raciocínio e planejamento, contrapondo essa hipótese (verificação seria mais fácil que geração) a um verificador externo garantidamente correto.
- **Método:** papel do LLM = **verificador (e autocrítico)**, comparado a um **verificador externo sólido** (SymPy para Jogo do 24; verificador de arestas para Coloração de Grafos; VAL para planejamento STRIPS). O sistema geral é composto de um gerador de resposta, um verificador binário e um gerador de crítica; testam-se combinações de: *prompting* padrão (S.P., linha de base), autocrítica completa LLM+LLM, crítica LLM+verificador externo sólido (com três granularidades de retorno: apenas binário, primeiro erro, todos os erros) e amostragem (*sampling*, k=15/25) com e sem autoconsistência (S.C.).
- **Dados/benchmarks:** três domínios — Jogo do 24 (aritmético), Coloração de Grafos (NP-completo, não é planejamento automatizado) e **planejamento STRIPS**, com Blocksworld e sua versão ofuscada Mystery Blocksworld (100 instâncias por domínio).
- **Modelo e data:** **GPT-4** (não há, no texto lido, menção explícita à versão/*snapshot* exata nem à data de acesso à API).
- **Resultado principal:** Tabela 1 (acurácia, 100 instâncias por domínio) — em Blocksworld, *prompting* padrão 40%, autocrítica completa LLM+LLM 55% (melhora, ao contrário dos outros domínios), crítica com verificador externo sólido e retorno de todos os erros 87%; em Mystery Blocksworld, *prompting* padrão 4%, autocrítica LLM+LLM 0% (piora), com verificador externo sólido sobe no máximo a 14%. Em Jogo do 24 e Coloração de Grafos, a autocrítica LLM+LLM **piora** o desempenho em relação à linha de base (Jogo do 24: 5%→3%; Coloração de Grafos: 16%→2%), enquanto o verificador externo sólido sempre melhora. Conclusão central: ganhos atribuídos a "autocrítica" vêm, na maior parte, da solidez do verificador externo, não do conteúdo da crítica gerada pelo próprio LLM.
- **Relação com a dissertação de 2010:** **A5** [confirma] — mais uma vez, a mesma arquitetura (GPT-4 com autocrítica ou com verificador externo) produz resultados de acurácia muito diferentes conforme o domínio e sua versão (Blocksworld 40–87% vs. Mystery Blocksworld 0–14%), reforçando que a característica do domínio (aqui, novamente, familiaridade lexical/semântica) interage com o desempenho da técnica de verificação. **A7** [amplia] — o artigo trata "acurácia" como taxa de acerto por instância, compatível com a noção de cobertura de 2010, mas aplicada tanto à geração quanto à verificação de soluções, uma dimensão que 2010 não examina (2010 avalia só planejadores, não verificadores).

## Pontos relevantes para o projeto

- Dá suporte empírico direto ao papel "verificador" da taxonomia pedida (planejador direto, tradutor, gerador de heurística, verificador, seletor) — aqui fica claro que o LLM como autoverificador é frágil e pode até piorar o resultado, ao contrário do LLM auxiliado por verificador externo sólido.
- Novamente Blocksworld vs. Mystery Blocksworld reaparece como o par de domínios que melhor evidencia sensibilidade a características de superfície — é o terceiro artigo do lote a usar esse mesmo par, o que fortalece (por replicação independente, mesmo grupo de pesquisa) a robustez do achado, mas também limita a diversidade de domínios do conjunto de evidências do eixo E5 lido até aqui.
- Nenhuma menção explícita, no texto lido, a que versão/data exata de GPT-4 foi usada — registrar essa lacuna explicitamente, conforme pedido no prompt ("em que data/versão"), em vez de supor.
- Resultado de que autocrítica pura pode piorar desempenho (Jogo do 24, Coloração de Grafos) é um contraponto importante a qualquer afirmação genérica de que "adicionar mais etapas de raciocínio sempre ajuda" — relevante para qualquer discussão sobre limites de técnicas iterativas.

## Marcações

- `[FATO]` Tabela 1: Blocksworld — S.P. 40%, LLM+LLM 55%, LLM+Sound (A.E.F.) 87%; Mystery Blocksworld — S.P. 4%, LLM+LLM 0%, LLM+Sound (F.E.F.) 8%/(A.E.F.) 6%; Jogo do 24 — S.P. 5%, LLM+LLM 3%; Coloração de Grafos — S.P. 16%, LLM+LLM 2%.
- `[FATO]` "As shown in Table 1, when we augment this condition with the full self-critique setup, performance decreases. In fact, Figure 2 shows that as the number of backprompts increases, this kind of self-correction consistently degrades output quality" (seção 5, "Examining Self-Verification").
- `[HIPÓTESE]` A melhora da autocrítica em Blocksworld (40%→55%), na contramão da piora observada nos outros dois domínios, pode ser um artefato do domínio ser relativamente familiar ao modelo (favorecendo mesmo uma crítica pouco confiável), enquanto em domínios mais raros/artificiais (Jogo do 24, Coloração de Grafos) a crítica do próprio LLM carece de base — se confirmado por mais evidências, seria mais um indício de que "familiaridade do domínio no treinamento" é uma característica de domínio relevante para técnicas baseadas em LLM, sem equivalente direto nas métricas UML de 2010.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2402.08115 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
