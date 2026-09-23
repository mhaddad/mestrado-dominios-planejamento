---
tipo: nota-de-leitura
eixo: E3
citekey: lin2001planner
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/download/1575/1474
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026 (aprovação delegada ao Coordenador)
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# A Planner Called R

**Lin, F. · 2001 · AI Magazine 22(3), 73–76**
**Link/DOI:** https://doi.org/10.1609/aimag.v22i3.1575

## Extração estruturada

- **Problema:** apresentar o planejador R (System R), variante do STRIPS original, que competiu nas faixas automática e "hand-tailored" da Quinta Competição Internacional de Planejamento.
- **Método:** dado um objetivo conjuntivo, R seleciona um subobjetivo simples e, se existe uma ação executável que o torna verdadeiro, executa-a e passa ao próximo subobjetivo; senão, computa um novo objetivo conjuntivo a partir das ações que têm aquele subobjetivo como efeito e tenta atingi-lo recursivamente, mantendo uma lista global das ações já decididas (sem retroceder sobre o estado inicial, ao contrário do STRIPS clássico).
- **Dados/benchmarks:** resultados da Quinta Competição Internacional de Planejamento (AIPS/IPC), citados de forma qualitativa no artigo.
- **Resultado principal:** o artigo descreve o algoritmo e suas diferenças em relação ao STRIPS clássico de Fikes e Nilsson (1971); não traz uma tabela de resultados numéricos no corpo lido.
- **Relação com a dissertação de 2010:**
  - **A6 (parcialmente corrige):** 2010 classifica R como State-Space, Partial-order, Forward-chaining e Backward-chaining (Tabela 4). A fonte primária chama R explicitamente de "forward-chaining, recursive STRIPS" (citando Nilsson 1998), o que confirma o rótulo Forward-chaining, mas não descreve uma técnica de *backward-chaining* separada: o processo de subobjetivação recursiva é uma forma de regressão de metas dentro de uma busca que a própria fonte rotula como forward-chaining, não uma técnica distinta e coexistente. O rótulo duplo (Forward-chaining **e** Backward-chaining) de 2010 mistura o nome que a fonte dá ao algoritmo com uma leitura própria do mecanismo interno de subobjetivação.

## Pontos relevantes para o projeto

- É o único, entre os 10 planejadores de 2010, cuja fonte primária usa o termo "forward-chaining" para se autodescrever de forma explícita e sem ressalvas — referência útil para calibrar o que "forward-chaining" deveria significar nas outras notas desta leva.
- R não usa grafo de planos, SAT nem heurística numérica — é o planejador mais próximo do STRIPS clássico entre os 10, o que o torna um caso de controle útil para a nova dimensão "representação de estado" da Fase 2.

## Marcações

- `[FATO]` A fonte primária descreve R como "a variant of the original STRIPS ... (called forward-chaining, recursive STRIPS in Nilsson [1998])" (corpo do artigo, p. 73).
- `[HIPÓTESE]` O rótulo "Backward-chaining" atribuído por 2010 a R provavelmente vem de uma leitura do mecanismo de subobjetivação recursiva (que lembra regressão de metas) sem levar em conta que a própria fonte já rotula o algoritmo inteiro como forward-chaining.

## Trechos literais

1. "SYSTEM R is a variant of the original STRIPS by Fikes and Nilsson (1971) (called forward-chaining, recursive STRIPS in Nilsson [1998])." (p. 73)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral em https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/download/1575/1474 (PDF baixado diretamente do OJS da AAAI e extraído com `pdftotext -layout`). Metadados (DOI, volume, páginas) verificados via OpenAlex e metadados Dublin Core da página do artigo. Conferência humana: pendente.
