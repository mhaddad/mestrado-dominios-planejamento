# Fase 5 — Ponte para desenvolvimento de software dirigido por IA

**Objetivo:** responder Q4 com um piloto no Ateliê de Software e decidir se há base para um produto.
**Critério de conclusão:** piloto analisado e decisão registrada na seção 10 do [plano](../plan/plano-revisao-dissertacao.md).

> **Toda a analogia desta fase é `[HIPÓTESE]`.** Conclusões saem só dos dados do piloto.

| Pasta | Conteúdo |
|---|---|
| `protocolo/` | Características da tarefa a registrar, configurações de agente a comparar, medidas de resultado |
| `dados/` | Dados do piloto (50–100 tarefas reais). **Sem dados sensíveis do Ateliê ou de clientes.** |
| `relatorio/` | Análise de H1–H3 e decisão final |

## Hipóteses do piloto

- **H1:** nenhuma configuração de agente é a melhor para todos os tipos de tarefa.
- **H2:** características observáveis da tarefa e do repositório ajudam a prever qual configuração funciona melhor.
- **H3:** métricas estruturais do código, das mesmas famílias usadas em 2010, contribuem para essa previsão.

## Decisão possível

Adotar internamente · seguir experimentando · avaliar produto · arquivar. Produto só é considerado se **todos** os critérios do plano forem atendidos.

## Cuidados

- Adesão da equipe é voluntária; coletar automaticamente sempre que possível (risco R7).
- O repositório é privado, mas trate os dados como se pudessem ser vistos por terceiros: anonimize antes de commitar.
