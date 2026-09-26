# Registro de experimento — EXP-16: X1, LLM como planejador

| Campo | Valor |
|---|---|
| ID | EXP-16 |
| Data | 26/09/2026 |
| Fase | 4 |
| Pergunta | Q3: o LLM como planejador (`llm/x1-planejador/protocolo.md`) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `llm/x1-planejador/x1_planejador.py` (commit `fbb0fc4`, feito antes das chamadas).
- ***Prompt*:** `llm/prompts/x1-planejador-v1.md`, em inglês. Domínio e problema em PDDL; o plano pedido entre BEGIN PLAN e END PLAN, em sintaxe PDDL.
- **Instâncias:** a p01 do Autoscale em 8 domínios: Blocks World, TPP, Floortile, Pipesworld sem tanques, Gripper, Logistics, Miconic e Rovers.
- **Modelos e parâmetros:** os do X3 (raciocínio *medium*, `max_tokens` de 16.000); uma chamada por par.
- **Validação:** VAL (`Validate`), compilado no Mac a partir do código que veio no artefato do Planner Museum, com `cmake` instalado pelo `uv`.
  - **Teste do validador:** um plano válido do Gemini foi aceito; a versão embaralhada foi recusada (pré-condição) e a versão sem o último passo também (meta).
- **Referência:** Fast Downward 26.6, compilado localmente, `--alias lama-first`. As 8 referências foram aceitas pelo VAL (`llm/x1-planejador/resultados/referencia-lama.csv`).
- **Custo:** US$ 1,21. Uso acumulado da chave: US$ 6,56 de US$ 10.

## Como reproduzir

```
uv run --no-project --with scikit-learn --with scipy python llm/x1-planejador/x1_planejador.py referencia
uv run --no-project --with scikit-learn --with scipy python llm/x1-planejador/x1_planejador.py rodar --rodada principal
uv run --no-project --with scikit-learn --with scipy python llm/x1-planejador/x1_planejador.py avaliar --rodada principal
```

Requer o VAL e o Fast Downward compilados em `experimentos/ferramentas/`, fora do git.

## Resultado

**Onde estão os resultados:** `llm/x1-planejador/resultados/principal.csv`; respostas brutas em `llm/registros/x1/principal/`.

| Modelo | Planos válidos (VAL) | Falhas |
|---|---|---|
| Gemini 3.1 Pro | 8 de 8 | — |
| Claude Sonnet 5 | 7 de 8 | Pipesworld: esgotou os 16.000 *tokens* raciocinando, sem plano |
| GPT-6 Sol | 7 de 8 | TPP: ação com pré-condição não satisfeita |
| DeepSeek V4 Pro | 6 de 8 | Gripper e Logistics: ações sem parênteses (fora da sintaxe pedida) |
| **Total** | **28 de 32** | |

- **Análise secundária, fora da regra do protocolo:** com os parênteses acrescentados, os dois planos do DeepSeek também são válidos (59 e 31 passos). O conteúdo estaria certo em 30 de 32.
- **Comprimento dos planos válidos:** em geral, igual ou menor que o do LAMA (lama-first, que não é ótimo).
  - Blocks World: 28 contra 36, nos quatro modelos.
  - TPP: de 19 a 23 contra 27.
  - Floortile: 11 ou 13 contra 13.
  - Pipesworld: 14 contra 18.
  - Gripper, Logistics, Miconic e Rovers: igual ou até 5 passos a menos.
  - Maiores que a referência: o DeepSeek no Miconic (58 contra 56) e o Sonnet no Rovers (31 contra 30).

## Interpretação

- **Nas instâncias menores do Autoscale, os LLMs de 2026 com raciocínio produzem planos válidos na grande maioria dos casos (28 de 32), muitas vezes mais curtos que os do LAMA.** `[FATO]`
  - Isso contrasta com as avaliações de 2023, em que os LLMs raramente produziam planos válidos (`valmeekam2023planbench`, `liu2023llmp`).
  - `[HIPÓTESE]` A diferença vem sobretudo do raciocínio longo antes da resposta. O custo aparece no tempo e nos *tokens*: o Sonnet gastou US$ 0,17 e o limite inteiro no Pipesworld sem responder.
- **Nos 4 domínios em que uma técnica antiga é a melhor no Nível 4,** os LLMs resolvem a p01 tão bem quanto nos demais. `[FATO]` Com uma instância por domínio, não dá para dizer se o LLM se comporta como alguma técnica específica.
- **Limite importante:** são as menores instâncias de cada domínio. O Nível 4 mede instâncias até 30 vezes maiores, com 30 minutos. Nada aqui indica que o LLM escale para essas instâncias. `[HIPÓTESE]` O custo e o limite de *tokens* crescem com o tamanho do plano.

## Limites

- Uma instância (a menor) por domínio, uma chamada por par. Sem repetição.
- As instâncias do Autoscale são geradas por gerador, mas domínios como Blocks World e Gripper são muito conhecidos; o modelo pode ter visto instâncias parecidas.
- A regra de formato é rígida por desenho. A análise secundária mostra o efeito dela.
