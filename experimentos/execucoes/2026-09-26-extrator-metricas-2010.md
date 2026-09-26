# Registro de experimento — EXP-07: extrator das métricas de 2010 a partir do PDDL (R-25)

| Campo | Valor |
|---|---|
| ID | EXP-07 |
| Data | 26/09/2026 |
| Fase | 3 |
| Pergunta | Q2, conjunto de *features* (a) (item R-25 de `auditoria/reexecucao.md`; F3; G2, G11–G13) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `experimentos/extratores/metricas_2010_pddl.py`. Tem um *parser* de PDDL próprio, sem dependências. As regras estão no cabeçalho do script.
- **Entrada:** o arquivo de domínio das 13 variantes de `data/2010/benchmarks_ipc_mapa_final.csv`, do repositório `potassco/pddl-instances` no commit `cf19edf`. O Pathways tem um arquivo de domínio por instância; foi usado o da primeira (`domain-1.pddl`). O número de ações varia entre esses arquivos: 6 no primeiro, 45 no trigésimo.
- **Regras:** foram fixadas antes da comparação, a partir das definições das Tabelas 5–7 de 2010 e do desenho da Fase 3:
  - hierarquia de tipos → classes, generalização, hierarquias e DIT;
  - ações → casos de uso, métodos e ações;
  - predicados de aridade 0 ou 1 → atributos;
  - predicados de aridade 2 ou mais → associações.

  Nenhuma regra foi ajustada depois de ver os valores de 2010. Em domínios sem `:types`, as classes são os predicados unários estáticos usados como guarda de parâmetro.
- **Atores:** a regra é uma convenção fraca. Conta os tipos distintos do primeiro parâmetro das ações, supondo que o primeiro parâmetro seja o agente. O PDDL não declara agentes.
- **Não extraídas (6 de 17):** Agregação, HAgg Máximo, estados, ações de entrada, ações de saída e transições. Não têm correspondente no PDDL: são decisões de quem modela em UML.P. As do diagrama de estados podem ganhar um substituto no grafo de transição de domínio (DTG) do R-26. `[HIPÓTESE]`
- **Comparação:** contra os valores publicados, com as correções aprovadas (Pathways/Associações = 2; TPP/Generalização = 4). Classes pela regra de discretização que 2010 aplicou (extremos do treino, G23).

## Como reproduzir

Ver `experimentos/extratores/README.md` (clonar os benchmarks e rodar o script).

## Resultado

**Onde estão os resultados:** `experimentos/extratores/metricas-2010-pddl/` (`metricas.csv`, `comparacao.csv`, `resumo.csv`).

| Métrica | Valores iguais (13 domínios) | Correlação de postos | Classe igual (13) |
|---|---|---|---|
| Número total de Classes | 7 | 0,92 | 11 |
| Número total de Generalização | 10 | 0,92 | 11 |
| Número total de Hierarquias | 10 | 0,89 | 10 |
| DIT Máximo | 10 | 0,81 | 10 |
| Número de Casos de Uso | 11 | 0,77 | 11 |
| Número total de Métodos | 11 | 0,69 | 11 |
| Número total de ações | 11 | 0,69 | 11 |
| Número de Casos de Uso por Atores | 5 | 0,61 | 9 |
| Número total de Associações | 3 | 0,51 | 5 |
| Número de Atores | 5 | 0,40 | 5 |
| Número total de Atributos | 1 | 0,31 | 8 |

## Interpretação

- **As métricas que vêm da estrutura do PDDL se reproduzem bem.** São as da hierarquia de tipos e as da contagem de ações. `[FATO]`
  - As divergências nas ações se concentram em dois domínios:
    - **Elevator:** o modelo itSIMPLE de 2010 tem 6 casos de uso, 9 métodos e 10 ações; o PDDL da IPC 2000 (`strips-simple-typed`) tem 4 ações. O modelo de 2010 não é uma tradução desse PDDL.
    - **Pathways:** 6 ações no `domain-1.pddl` contra 5 em 2010.
  - Nos tipos, as divergências vêm de modelos que acrescentam ou retiram classes:
    - **Blocks World:** 3 classes em 2010 (bloco, mesa e garra) contra 1 tipo no PDDL.
    - **Mystery e Zeno-travel:** o PDDL não tem tipos, mas o modelo de 2010 tem hierarquia.
    - **Logistics:** 6 generalizações no PDDL contra 4 no modelo.
- **As métricas que dependem de escolhas de modelagem não se reproduzem.** Atributos (1 de 13), associações (3 de 13) e atores (5 de 13), com correlação de postos entre 0,31 e 0,51. `[FATO]` Em 2010, a divisão entre atributo e associação e a escolha dos atores foram feitas por quem modelou, e o PDDL não determina essas escolhas.
- **Consequência para F3 e Q2:** 6 das 17 métricas de 2010 não existem sem o modelo UML.P, e 3 das 11 extraíveis mudam muito conforme a regra de correspondência. `[HIPÓTESE]` Isso reforça a leitura de F3: parte das características de 2010 mede o modelo, não o domínio. O teste UML × *features* de PDDL (R-27) já pode usar as 11 métricas extraídas, marcando as 3 frágeis.
- **O que não está coberto:** o R-13 (documentar o critério de contagem da Agregação e testar classes com e sem classes auxiliares) depende dos modelos itSIMPLE, não do PDDL, e continua pendente.

## Problemas e desvios

- **Pathways:** usar o domínio da primeira instância é uma escolha. O número de ações muda por instância.
- **Atores:** a regra do primeiro parâmetro é convenção, não definição. Outra regra razoável daria outros números.
