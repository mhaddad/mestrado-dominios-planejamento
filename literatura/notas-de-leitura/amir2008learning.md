---
tipo: nota-de-leitura
eixo: E4
citekey: amir2008learning
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/download/10576/25307
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: [F6]
perguntas: [Q1]
---

# Learning Partially Observable Deterministic Action Models

**Amir, E.; Chang, A. · 2008 · Journal of Artificial Intelligence Research 33**
**Link/DOI:** 10.1613/jair.2575

## Extração estruturada

- **Problema:** identificar exatamente (sem erro) os efeitos e pré-condições de ações determinísticas em domínios parcialmente observáveis, quando o modelo de ação é desconhecido e deve ser aprendido a partir de observações parciais ao longo do tempo — problema anterior e independente da escolha de técnica de busca para planejar.
- **Método:** algoritmo SLAF (*Simultaneous Learning and Filtering*), que atualiza uma fórmula lógica proposicional (*Transition Belief Formula*) representando todas as relações de transição e estados de mundo consistentes com a sequência de ações e observações vista até o momento; inclui um algoritmo dedutivo geral (exponencial no pior caso) e algoritmos polinomiais por passo para classes restritas de ações determinísticas (ex.: STRIPS).
- **Dados/benchmarks:** quatro domínios da 3ª Competição Internacional de Planejamento (IPC-3) — **Drivelog, Zenotravel, Blocksworld e Depots** — com sequências geradas aleatoriamente de 5.000 passos, variando o número de fluentes proposicionais (19 a 250) e observando 10 fluentes aleatórios por passo.
- **Resultado principal:** o tempo de computação de SLAF cresce linearmente com o número de passos e escala razoavelmente com o tamanho do domínio (cerca de 1 ms por passo para domínios de 200 fluentes); os autores demonstram que é possível calcular soluções exatas para domínios de centenas de *fluents*, e que o número de traços necessário até a convergência é polinomial no número de características do domínio.
- **Relação com a dissertação de 2010:** o artigo usa **Zeno-travel, um dos três domínios de validação da dissertação de 2010** (junto com Storage e Elevator), mas em um problema diferente — aprendizado do próprio modelo de ação sob observabilidade parcial, não seleção de técnica de busca sobre um modelo já dado. Por isso, **não confirma nem corrige diretamente nenhuma das afirmações A1–A8**, que pressupõem um modelo PDDL correto e completo como ponto de partida. A relevância está em expor um pressuposto implícito de 2010: a dissertação assume que o modelo do domínio (do qual a UML e as métricas são extraídas) já está correto e disponível; este trabalho mostra que, em cenários realistas de observabilidade parcial, essa suposição pode falhar e precisar ser resolvida antes de qualquer seleção de técnica — uma lacuna que toca indiretamente **F6** (dados fora das competições, aqui geradas artificialmente sobre domínios de IPC) e alimenta **Q1** ao lembrar que qualquer réplica das conclusões de 2010 com mais dados também herdaria o pressuposto de completude do modelo.

## Pontos relevantes para o projeto

- Representa o domínio por **fórmulas lógicas proposicionais** (STRIPS/ADL generalizado), no mesmo espírito formal-lógico de Srivastava et al. (2011), mas focado em aprender o próprio modelo, não uma política ou heurística sobre um modelo dado — mais uma variação da representação lógica de domínio no eixo E4.
- Uso do domínio Zenotravel cria uma ponte concreta e citável com os domínios de validação de 2010, útil para contextualizar, na revisão, até que ponto a suposição "modelo correto e completo" pesa sobre os resultados originais.
- Resultados de escalabilidade (tempo linear no número de passos, polinomial no número de fluentes) mostram que aprendizado de modelo de ação é tratável mesmo em domínios de médio porte — relevante para T3 (detalhar subtécnicas), caso a revisão de 2026 queira tratar "aprendizado do modelo" como uma etapa anterior à escolha de técnica de busca.
- Não há qualquer comparação entre planejadores nem entre técnicas de busca — o artigo é ortogonal ao núcleo empírico de 2010 (ranking de planejadores por domínio).

## Trechos literais

> "Our algorithms take sequences of partial observations over time as input, and output deterministic action models that could have lead to those observations." (Resumo)

> "We implemented our algorithms and ran experiments with AS-STRIPS-SLAF over the following domains taken from the 3rd International Planning Competition (IPC): Drivelog, Zenotravel, Blocksworld, and Depots." (Seção 7, "Experimental Evaluation", p. 371)

> "We can add bias and compute an exact solution for large domains (hundreds of features), in many cases." (Seção 9, "Conclusions", p. 380)

## Marcações

- `[FATO]` Os experimentos usam sequências de ação-observação geradas artificialmente (não traços de planejadores reais) sobre quatro domínios da IPC-3, incluindo Zenotravel (Seção 7, p. 371).
- `[FATO]` O tempo por passo de SLAF permanece aproximadamente constante ao longo da execução e cresce linearmente com o tamanho do domínio, chegando a ~1ms por passo para 200 fluentes (Seção 7, "How much time and space...").
- `[HIPÓTESE]` A dissertação de 2010 pressupõe implicitamente que o modelo de domínio já é conhecido e correto antes de aplicar qualquer técnica de busca; este artigo sugere que essa suposição é uma simplificação relevante a declarar explicitamente em qualquer trabalho futuro que amplie 2010 para cenários de observabilidade parcial.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/download/10576/25307. Conferência humana: pendente.
