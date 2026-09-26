# Registro de experimento — EXP-17: X4, LLM com verificador (VAL), instâncias p05

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
- **Trava:** US$ 8,90 no uso da chave, para reservar o saldo do X2.
- **Custo:** US$ 2,35. Uso acumulado da chave: US$ 8,92.
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
| Claude Sonnet 5 | válido na 1ª (90) | válido na 3ª (73) | 4 respostas sem plano | sem plano; **cortado pela trava** |
| DeepSeek V4 Pro | válido na 1ª (90) | inválido, depois sem plano; **cortado pela trava** | **não rodou (trava)** | **não rodou (trava)** |

- **Primeira tentativa (o X1 nas instâncias maiores):** 8 planos válidos em 14 conversas iniciadas.
- **Ao final do ciclo:** 11 válidos em 14. O retorno do VAL recuperou 3 das 6 falhas:
  - Sonnet no TPP, depois de um erro de tipos e de uma pré-condição;
  - Gemini no Floortile, depois de uma resposta sem plano;
  - Gemini no Pipesworld, depois de uma resposta sem plano e de uma meta não alcançada.
- **Das 3 falhas restantes,** 2 foram cortadas pela trava de orçamento. A outra é o Sonnet no Floortile, com 4 respostas sem plano, provavelmente por esgotar os *tokens* raciocinando.
- **Comprimento:** no Blocks World, os planos válidos têm de 86 a 90 passos, contra 160 do LAMA. No TPP, de 73 a 75, contra 106. No Pipesworld, 36 e 42, contra 48.
- **Floortile p05:** o GPT-6 Sol e o Gemini produziram planos válidos, de 206 e 204 passos, numa instância em que o LAMA não achou plano em 300 s.

## Interpretação

- **O verificador ajuda:** metade das falhas foi recuperada com o retorno do VAL, em 1 ou 2 rodadas. `[FATO]` É o efeito previsto pela arquitetura LLM-Modulo (`kambhampati2024llms`), aqui com poucos casos.
- **Nas instâncias p05 dos 4 domínios "de técnica antiga",** os LLMs com raciocínio produzem planos válidos e bem mais curtos que os do LAMA. No Floortile, resolvem o que o LAMA não resolveu em 5 minutos. `[FATO]`
  - `[HIPÓTESE]` O custo e o tempo de resposta crescem com a instância (até US$ 0,71 numa conversa), e as falhas por esgotar *tokens* aumentam. A escala do Nível 4 (30 instâncias, as maiores com dezenas de vezes mais objetos) continua fora de alcance deste teste.
- **Para a Q3:** o LLM entra no mapa como planejador de instâncias pequenas e médias, forte justamente onde técnicas antigas se destacam (Floortile, TPP, Blocks World). Com um verificador formal, fica mais confiável.

## Limites

- **Rodada incompleta:** 2 das 16 conversas não começaram e 2 foram cortadas pela trava de orçamento.
- Uma instância por domínio; sem repetições.
