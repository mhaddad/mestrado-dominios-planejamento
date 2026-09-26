# X3 — LLM como seletor: protocolo

Rascunho de 26/09/2026 (Claude Code), para aprovação do autor antes de qualquer chamada paga.

## Pergunta

Dado o domínio de planejamento em PDDL, um LLM escolhe bem a técnica (ou o planejador) para ele? Como se compara com o *single best* e com os seletores por características da Fase 3 (EXP-12, EXP-13)? A síntese E1 aponta o LLM como seletor como lacuna na literatura.

## Dados

- **Os mesmos 41 domínios do EXP-12**, com a mesma medida: cobertura publicada do Planner Museum e perda em relação ao *virtual best*.
- **O que o modelo recebe:** o arquivo de domínio PDDL do Autoscale e uma instância pequena (p01).
  - Arquivos com mais de 40 KB são truncados: afeta o domínio do Airport (404 KB), o do Organic Synthesis (258 KB) e a instância do NoMystery (179 KB). O truncamento fica marcado no *prompt* e no registro.

## Condições

- **Principal: planejadores anônimos.** O modelo recebe os 29 planejadores rotulados de P01 a P29, cada um descrito só pelas técnicas da taxonomia 4D (`auditoria/taxonomia/planejadores_museu_4d.csv`), sem nome, ano ou resultado.
  - Motivo: o artigo do Planner Museum e a tabela de cobertura são públicos desde março de 2026. Um modelo treinado depois disso pode lembrar os resultados em vez de raciocinar sobre o domínio.
  - A condição anônima testa o que interessa à Q3: se o modelo liga a estrutura do domínio à técnica adequada.
- **Secundária, se houver orçamento: planejadores com nome.** Testa a utilidade prática e dá uma medida indireta da contaminação (a diferença entre as duas condições).

## Resposta pedida

O identificador de um planejador (P01–P29) e uma justificativa curta. A resposta vem em JSON, validado por script. Resposta inválida conta como falha e entra na avaliação com perda de escolha ao acaso.

## Modelos (proposta)

Um modelo de ponta por fornecedor principal, mais um de pesos abertos. Todos são chamados pelo OpenRouter, com o identificador fixo registrado e a mesma configuração: raciocínio no nível *medium* e no máximo 8.000 *tokens* de saída. Preços do catálogo do OpenRouter em 26/09/2026, em US$ por milhão de *tokens* (entrada / saída):

| Modelo (id no OpenRouter) | Fornecedor | Entrada / saída | Motivo |
|---|---|---|---|
| `anthropic/claude-sonnet-5` | Anthropic | 2,00 / 10,00 | Nível de ponta com custo menor. O Opus 5.5 custa o dobro |
| `openai/gpt-6-sol` | OpenAI | 2,00 / 10,00 | Modelo principal atual da OpenAI |
| `google/gemini-3.1-pro-preview` | Google | 2,00 / 12,00 | Linha Pro mais recente disponível. É uma *preview*: o identificador pode mudar, por isso vai registrado |
| `deepseek/deepseek-v4-pro-0813` | DeepSeek | 0,26 / 0,79 | Pesos abertos, com data no identificador (reprodutível) |

Os três primeiros ficam na mesma faixa de preço, o que torna a comparação justa. Não entram por custo: Claude Opus 5.5 e Fable 5.1; e por redundância: variantes *flash* e *mini*.

## Orçamento (teto de US$ 10; decisão do autor)

A estimativa usa cerca de 4 mil *tokens* de entrada e 3 mil de saída por chamada, com raciocínio incluído. O custo real é lido do campo de uso que o OpenRouter devolve.

| Etapa | Chamadas | Estimativa |
|---|---|---|
| Teste com 3 domínios × 4 modelos | 12 | cerca de US$ 0,50 |
| Condição anônima, 41 domínios × 4 modelos, 1 repetição | 164 | cerca de US$ 5 |
| Folga (repetições ou a condição com nomes num subconjunto) | — | até o teto |

O script para quando o custo acumulado chega a US$ 9,50. **Recomendação ao autor:** configurar a chave no OpenRouter com limite de crédito de US$ 10, para que o teto valha também do lado do serviço.

## Avaliação

- **Medidas:** as mesmas do EXP-12: perda total, domínios com perda zero, fração da lacuna SBS→VBS fechada e Wilcoxon pareado contra o SBS.
- **Leitura das justificativas:** a técnica que o modelo alega usar bate com a codificação do planejador escolhido?

## Registro

- **Prompts:** versionados em `llm/prompts/`.
- **Respostas:** brutas em `llm/registros/`, com o modelo, o provedor que atendeu, a data, os *tokens* e o custo de cada chamada.
- **Registro do experimento:** `experimentos/execucoes/`.
- **Chave:** lida de `OPENROUTER_API_KEY` no `.env`, que está no `.gitignore` e nunca vai para o repositório.
