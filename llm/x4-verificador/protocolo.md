# X4 — LLM com verificador: protocolo

Rascunho de 26/09/2026 (Claude Code). **Desenho escolhido pelo autor:** instâncias maiores, porque no X1 (EXP-16) os modelos acertaram 28 de 32 planos nas instâncias p01 e restariam só 4 casos para o ciclo de correção.

- **Pergunta:** devolver ao LLM o erro apontado por um validador formal (VAL) melhora o X1? É a arquitetura "LLM + verificador" da linha LLM-Modulo (`kambhampati2024llms`).
- **Instâncias:** a p05 do Autoscale, nos **4 domínios em que uma técnica antiga é a melhor** no Nível 4 (EXP-13): Blocks World, TPP, Floortile e Pipesworld sem tanques.
  - O recorte em 4 domínios, em vez dos 8 do X1, é por orçamento: os planos de referência da p05 têm de 48 a 160 passos, e oito domínios consumiriam o saldo na primeira tentativa.
  - No Floortile p05, o LAMA não encontrou plano em 300 s. A instância fica mesmo assim: o VAL valida o plano que o LLM der.
- **Ciclo:** primeira tentativa com o *prompt* do X1. Se o plano for inválido, ausente ou mal formatado, a mesma conversa recebe o motivo e os últimos 1.500 caracteres da saída do VAL, com o pedido de um plano corrigido e completo. São até **3 correções** (4 respostas no máximo).
- **Modelos e parâmetros:** os do X3 e do X1.
- **Medidas:**
  - planos válidos na primeira tentativa, que é o X1 nas instâncias maiores;
  - planos válidos ao final do ciclo;
  - em que rodada o plano ficou válido;
  - custo por conversa.
- **Orçamento:** trava própria de **US$ 8,90** no uso da chave, para reservar o saldo do X2. O código de cada chamada fica registrado, e a conversa inteira é gravada.
- **Registro:** `llm/registros/x4/p05/`.
