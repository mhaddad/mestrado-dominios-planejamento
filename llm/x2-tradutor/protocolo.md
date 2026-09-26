# X2 — LLM como tradutor (linguagem natural → PDDL): protocolo

Rascunho de 26/09/2026 (Claude Code), seguindo a ordem aprovada pelo autor (X2 depois do X1 e do X4).

- **Pergunta:** o LLM gera o PDDL de um domínio correto a partir da descrição em linguagem natural? Com que taxa de erro?
- **Descrições:** as publicadas pelo LLM+P (`liu2023llmp`; repositório `github.com/Cranial-XIX/llm-pddl`, citado no artigo, commit `f5f897c`), com `domain.nl` e o PDDL de referência de cada domínio.
  - Usar descrições publicadas evita o viés de escrevê-las nós mesmos.
  - O repositório não tem arquivo de licença: fica fora do git, em `experimentos/ferramentas/llm-pddl`.
- **Domínios:** os 7 do LLM+P com conjunto de problemas (Barman, Blocks World, Floortile, Grippers, Storage, Termes e Tyreworld). O Manipulation fica de fora: tem só 2 problemas e é uma demonstração com robô.
- **O que o modelo recebe:** a descrição do domínio em linguagem natural e **o problema p01 em PDDL**, para que use os mesmos nomes de tipos, predicados e objetos. É preciso fornecer o problema porque a descrição em linguagem natural não fixa esses nomes. Sem eles, nenhum domínio gerado seria comparável com os problemas de referência.
- **Pedido:** o domínio em PDDL.
- **Modelos e parâmetros:** os mesmos do X3 e do X1. Uma chamada por par modelo × domínio (28 chamadas).
- **Critérios de correção,** em três níveis, sobre os problemas p01 a p05 de cada domínio:
  1. **Sintaxe:** o tradutor do Fast Downward aceita o domínio gerado com os problemas.
  2. **Solidez:** o plano que o Fast Downward (lama-first) encontra com o domínio gerado é válido no domínio de **referência** (VAL). Plano válido no modelo gerado e inválido na referência revela um modelo permissivo demais.
  3. **Completude:** o plano encontrado com o domínio de referência é válido no domínio **gerado** (VAL). A falha revela um modelo restritivo demais.
- **Medidas:** fração de domínios e de problemas que passam em cada nível, por modelo, e tipos de erro.
- **Orçamento:** saídas curtas; estimativa abaixo de US$ 0,50. Mesma trava de US$ 9,50.
