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
