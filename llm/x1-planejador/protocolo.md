# X1 — LLM como planejador: protocolo

Rascunho de 26/09/2026 (Claude Code), seguindo a ordem aprovada pelo autor (compilar o VAL; X1; X4 sobre o X1; X2).

- **Pergunta:** como o LLM se sai como planejador, comparado com os planejadores clássicos, nos mesmos domínios do Nível 4?
- **Instâncias:** a p01 do Autoscale em 8 domínios:
  - os 4 em que uma técnica antiga é a melhor por domínio (EXP-13): Blocks World, TPP, Floortile e Pipesworld sem tanques;
  - Gripper, Logistics, Miconic e Rovers.
  - Uma instância por domínio, por causa do orçamento (saldo de cerca de US$ 4,70 do teto de US$ 10).
- **Referência clássica:** o Fast Downward 26.6 com `--alias lama-first` resolve as 8 instâncias com planos de 13 a 59 passos. Os comprimentos ficam registrados junto com os resultados e são reproduzíveis.
- **Modelos e parâmetros:** os mesmos do X3 (`llm/x3-seletor/protocolo.md`): Sonnet 5, GPT-6 Sol, Gemini 3.1 Pro *preview* e DeepSeek V4 Pro 0813, com raciocínio *medium* e no máximo 16.000 *tokens* de saída. Uma chamada por par modelo × instância.
- ***Prompt*:** `llm/prompts/x1-planejador-v1.md`, em inglês, com domínio e problema em PDDL e o plano pedido entre as linhas BEGIN PLAN e END PLAN.
- **Validação:** VAL (o `Validate` compilado do código que veio no artefato do Planner Museum, `tools/VAL`). Um plano conta como válido só se o VAL o aceitar. Plano ausente ou mal formatado conta como inválido.
- **Medidas:**
  - planos válidos por modelo e por domínio;
  - nos válidos, a razão entre o comprimento do plano e o da referência do LAMA;
  - nos inválidos, o tipo de falha que o VAL aponta (pré-condição não satisfeita, meta não alcançada, ação desconhecida).
- **Orçamento:** a mesma trava de US$ 9,50 no uso da chave. O custo real de cada chamada fica no registro.
- **Registro:** respostas brutas em `llm/registros/x1/`, que também alimentam o X4.

## EXP-23: condição com nomes ofuscados (27/09/2026)

Decisão do autor na avaliação das Fases 1 a 4: testar se o desempenho do X1 depende de nomes familiares, a ressalva que a literatura mais repete (Mystery Blocksworld, `valmeekam2023planbench`, `valmeekam2024llms`).

- **Única diferença para o EXP-16:** os nomes. Domínio e instância p01 dos mesmos 8 domínios, com todos os nomes do modelador (domínio, problema, tipos, constantes, predicados, ações, variáveis e objetos) trocados por rótulos aleatórios de 5 letras (`llm/x1-planejador/ofuscar.py`, semente 2026; mapa em `resultados/ofuscacao-mapa.csv`). Mesmo *prompt* (`x1-planejador-v1.md`), mesmos modelos e parâmetros, uma chamada por par.
- **Equivalência conferida antes das chamadas:** o plano do `lama-first` traduzido pelo mapa é válido no VAL do outro lado, nos dois sentidos, nos 8 domínios (`ofuscar.py conferir`). O critério fixado primeiro, "mesmo tamanho de plano do `lama-first` nos dois lados", foi abandonado: a troca de nomes muda a ordem alfabética e o desempate do LAMA, e os tamanhos mudam em 6 dos 8 domínios (Pipesworld: 18 → 98) sem mudar o problema.
- **Medidas:** planos válidos pelo VAL nos arquivos ofuscados; tipo de falha; tamanho do plano contra o `lama-first` original (`referencia-lama.csv`), como no EXP-16. Comparação par a par com o EXP-16, descritiva (32 pares).
- **Custo:** o EXP-16 custou US$ 1,21. Trava desta rodada: US$ 11,90 (`--teto`), abaixo do limite da chave (US$ 12); uso antes da rodada: US$ 10,51. Se a trava parar a rodada, os pares que faltarem ficam registrados como não rodados.
- **Complemento (27/09/2026):** o autor subiu o limite da chave para US$ 13 para completar os 7 pares sem chamada. Rodada em sequência (`--sequencial`, uma chamada de cada vez) com trava de US$ 12,80; uso antes: US$ 12,09. Os 25 pares já registrados não são refeitos (o script pula o que existe).
