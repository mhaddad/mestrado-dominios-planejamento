# Registro de experimento — EXP-17: X4, LLM com verificador (VAL), instâncias p05 (completo)

| Campo | Valor |
|---|---|
| ID | EXP-17 |
| Data | 26/09/2026 |
| Fase | 4 |
| Pergunta | Q3: devolver ao LLM o erro apontado pelo VAL melhora o X1? (`llm/x4-verificador/protocolo.md`; desenho escolhido pelo autor: instâncias maiores) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `llm/x4-verificador/x4_verificador.py` (commit `af00406`, feito antes das chamadas). *Prompt* do X1 na primeira tentativa.
- **Instâncias:** a p05 do Autoscale em Blocks World, TPP, Floortile e Pipesworld sem tanques, os 4 domínios em que uma técnica antiga é a melhor no Nível 4.
- **Referência do LAMA (lama-first, 300 s):** 160, 106 e 48 passos. No Floortile p05, o LAMA não achou plano.
- **Ciclo:** até 3 correções. Cada correção devolve ao modelo o motivo e os últimos 1.500 caracteres da saída do VAL.
- **Trava:** US$ 8,90 no uso da chave na primeira passada, para reservar o saldo do X2. Ela cortou 4 conversas.
- **Retomada:** depois que o autor subiu o limite para US$ 12, a trava passou a US$ 11,50. As 4 conversas foram retomadas de onde pararam: o histórico foi reconstruído das respostas e dos retornos gravados, sem repetir chamadas já feitas, e a retomada fica marcada no registro.
- **Custo:** US$ 3,29 (soma do custo registrado em cada chamada).
- **Validação:** a avaliação final usa a checagem que exige a linha exata "Plan valid", adotada durante esta rodada; o X1 foi reavaliado com ela e não mudou.

## Como reproduzir

```
uv run --no-project --with scikit-learn --with scipy python llm/x4-verificador/x4_verificador.py rodar --rodada p05
uv run --no-project --with scikit-learn --with scipy python llm/x4-verificador/x4_verificador.py avaliar --rodada p05
```

## Resultado

**Onde estão os resultados:** `llm/x4-verificador/resultados/p05.csv`; as conversas inteiras em `llm/registros/x4/p05/`.

| Modelo | Blocks World | TPP | Floortile | Pipesworld |
|---|---|---|---|---|
| GPT-6 Sol | válido na 1ª (86 passos) | válido na 1ª (73) | válido na 1ª (206) | válido na 1ª (42) |
| Gemini 3.1 Pro | válido na 1ª (86) | válido na 1ª (75) | válido na 2ª (204) | válido na 3ª (36) |
| Claude Sonnet 5 | válido na 1ª (90) | válido na 3ª (73) | 4 respostas sem plano | 4 respostas sem plano |
| DeepSeek V4 Pro | válido na 1ª (90) | válido na 3ª (73) | 4 respostas sem plano | válido na 2ª (44) |

- **Primeira tentativa (o X1 nas instâncias maiores):** 8 planos válidos em 16.
- **Ao final do ciclo:** 13 válidos em 16. O retorno do VAL recuperou 5 das 8 falhas, em 1 ou 2 rodadas:
  - Sonnet e DeepSeek no TPP;
  - Gemini no Floortile;
  - Gemini e DeepSeek no Pipesworld.
- **As 3 falhas restantes são todas por limite de *tokens*:** as respostas terminam em 16.000 *tokens* (`finish_reason: length`) sem chegar ao plano. Estão no Sonnet no Floortile e no Pipesworld e no DeepSeek no Floortile.
  - Numa rodada, o provedor do DeepSeek entregou 33.473 *tokens*, acima do limite pedido.
- **Comprimento:** no Blocks World, os planos válidos têm de 86 a 90 passos, contra 160 do LAMA. No TPP, de 73 a 75, contra 106. No Pipesworld, de 36 a 44, contra 48.
- **Floortile p05:** o GPT-6 Sol e o Gemini produziram planos válidos, de 206 e 204 passos, numa instância em que o LAMA não achou plano em 300 s.

## Interpretação

- **O verificador ajuda:** 5 das 8 falhas foram recuperadas com o retorno do VAL, em 1 ou 2 rodadas. Todas as falhas que sobraram são por limite de *tokens*, não por plano errado. `[FATO]` É o efeito previsto pela arquitetura LLM-Modulo (`kambhampati2024llms`), aqui com poucos casos.
- **Nas instâncias p05 dos 4 domínios "de técnica antiga",** os LLMs com raciocínio produzem planos válidos e bem mais curtos que os do LAMA. No Floortile, resolvem o que o LAMA não resolveu em 5 minutos. `[FATO]`
  - `[HIPÓTESE]` O custo e o tempo de resposta crescem com a instância (até US$ 0,71 numa conversa), e as falhas por esgotar *tokens* aumentam. A escala do Nível 4 (30 instâncias, as maiores com dezenas de vezes mais objetos) continua fora de alcance deste teste.
- **Para a Q3:** o LLM entra no mapa como planejador de instâncias pequenas e médias, forte justamente onde técnicas antigas se destacam (Floortile, TPP, Blocks World). Com um verificador formal, fica mais confiável.

## Limites

- A retomada das 4 conversas cortadas aconteceu horas depois da primeira passada, com os mesmos modelos e parâmetros.
- `max_tokens` de 16.000: as falhas restantes indicam que um limite maior mudaria o resultado, com custo maior.
- Uma instância por domínio; sem repetições.
