# Registro de experimento — EXP-18: X2, LLM como tradutor (linguagem natural → PDDL)

| Campo | Valor |
|---|---|
| ID | EXP-18 |
| Data | 26–27/09/2026 |
| Fase | 4 |
| Pergunta | Q3: o LLM gera o PDDL de um domínio correto a partir da descrição em linguagem natural? (`llm/x2-tradutor/protocolo.md`) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Descrições:** as publicadas pelo LLM+P (`liu2023llmp`; `github.com/Cranial-XIX/llm-pddl`, commit `f5f897c`, fora do git por não ter licença).
- **Domínios:** 6: Barman, Blocks World, Floortile, Grippers, Storage e Termes.
  - O Tyreworld saiu antes de qualquer chamada: o domínio de referência publicado usa o objeto `wrench` sem declará-lo.
- **O que o modelo recebe:** a descrição em linguagem natural e o problema p01 em PDDL, para usar os mesmos nomes de tipos, predicados e constantes.
- ***Prompt*:** `llm/prompts/x2-tradutor-v1.md`. Modelos e parâmetros do X3; uma chamada por par (24).
- **Erro do provedor:** o Gemini no Barman teve três respostas interrompidas pelo provedor (`finish_reason: error`, sem cobrança), guardadas em `llm/registros/x2/erros-do-provedor/`. Por pedido do autor, houve novas tentativas, e a quarta deu certo.
- **Avaliação:** problemas p01–p05 de cada domínio.
  - **Sintaxe:** o tradutor do Fast Downward aceita o domínio gerado.
  - **Solidez:** o plano do Fast Downward (lama-first, 120 s) com o domínio gerado é válido no domínio de referência (VAL).
  - **Completude:** o plano feito com a referência é válido no domínio gerado (VAL).
- **Custo:** US$ 0,65.

## Artefatos da medida (encontrados durante a avaliação)

A solidez e a completude pelo VAL só valem quando o plano de um domínio pode ser lido no outro: mesmos nomes de ação, mesmo número de parâmetros e mesmos tipos, na mesma ordem. A descrição em linguagem natural não fixa esses detalhes. Por exemplo, ela diz "Move up", e a referência chama a ação de `up`. A comparação de assinaturas foi feita em duas etapas:

1. Nome e número de parâmetros: 5 dos 24 pares diferem.
2. Tipos na ordem, depois que um caso do Grippers revelou parâmetros trocados, como `pick(robô, garra, objeto, sala)` contra `pick(robô, objeto, sala, garra)`: **só 10 dos 24 pares têm assinatura igual** (`llm/x2-tradutor/resultados/principal-assinaturas.csv`).

Nos outros 14, só a sintaxe e a solubilidade são julgáveis.

A checagem de tipos do VAL é mais estrita que a do Fast Downward. O Sonnet no Blocks World declara `(:types block)` sem usá-lo, e o VAL recusa, embora as ações sejam idênticas às da referência.

O classificador de motivos teve dois erros, corrigidos antes deste registro:
- tratava o registro "Type-checking …" do modo `-v`, que o VAL imprime sempre, como erro;
- o modo `-v` travou num plano do Barman.

A versão final (`llm/x2-tradutor/motivos.py`) decide a validade com o VAL sem `-v` e usa o `-v`, com limite de 60 s, só para achar o motivo.

## Como reproduzir

```
uv run --no-project --with scikit-learn --with scipy python llm/x2-tradutor/x2_tradutor.py rodar --rodada principal
uv run --no-project --with scikit-learn --with scipy python llm/x2-tradutor/x2_tradutor.py avaliar --rodada principal
uv run --no-project --with scikit-learn --with scipy python llm/x2-tradutor/motivos.py
```

## Resultado

**Onde estão os resultados:** `llm/x2-tradutor/resultados/`:
- `principal.csv`, por problema;
- `principal-assinaturas.csv`;
- `principal-motivos.csv`, com os motivos dos 3 pares do Gemini.

**Sintaxe:** 23 dos 24 domínios são aceitos pelo tradutor do Fast Downward em todos os problemas. A exceção é o DeepSeek no Storage, recusado em 2 de 5 problemas.

**Os 10 pares com assinatura igual:**

| Modelo | Correto (solidez e completude em todos os problemas mensuráveis) | Erro real (pré-condição) | Artefato do VAL |
|---|---|---|---|
| GPT-6 Sol | Blocks World, Grippers, Storage | — | — |
| Gemini 3.1 Pro | Blocks World, Grippers | Floortile, Storage, Termes | — |
| Claude Sonnet 5 | Storage | — | Blocks World (tipo declarado e não usado) |
| DeepSeek V4 Pro | — (nenhum par com assinatura igual) | — | — |

- **Pares com assinatura diferente (14):** nomes diferentes em 3 (Floortile: Sonnet, GPT, DeepSeek); número de parâmetros diferente em 2 (Barman: Sonnet, DeepSeek); ordem ou tipos dos parâmetros diferentes em 9.

## Interpretação

- **Gerar PDDL sintaticamente válido é fácil para os quatro modelos (23 de 24).** `[FATO]`
- **Gerar um domínio equivalente à referência é bem mais difícil.** Dos 10 pares comparáveis, 6 são corretos. O GPT-6 Sol acerta os 3 que dá para comparar. `[FATO]`
- **Parte grande da diferença não é erro, é liberdade de modelagem:** nomes de ações, ordem de parâmetros, tipos a mais. A mesma descrição admite modelos diferentes. `[HIPÓTESE]` É o eco, no PDDL, do achado F3 da auditoria sobre os modelos UML de 2010 (EXP-07): quem modela decide detalhes que a descrição do domínio não fixa.
- **Para a Q3:** o LLM como tradutor produz PDDL utilizável, mas precisa de verificação contra uma referência ou contra problemas conhecidos. A linha LLM+P (`liu2023llmp`) fornecia o domínio pronto, justamente para evitar essa etapa.

## Limites

- Uma chamada por par; 6 domínios; o problema p01 dado como exemplo.
- A equivalência é testada por planos em 5 problemas, não provada.
- Nos 14 pares com assinatura diferente, a correção semântica não foi medida. Uma verificação que mapeasse ações e parâmetros entre os dois modelos resolveria isso e fica como trabalho futuro.
