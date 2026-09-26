# Registro de experimento — EXP-08: Nível 2, R-11, R-12, R-13 e R-15

| Campo | Valor |
|---|---|
| ID | EXP-08 |
| Data | 26/09/2026 |
| Fase | 3 |
| Pergunta | Q1 e F3 (itens R-11, R-12, R-13 e R-15 de `auditoria/reexecucao.md`) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `experimentos/analise/nivel2.py`, com três cenários novos e a linha de base. As condições são as da referência do EXP-04: classes publicadas, aritmética corrigida e os 11 rótulos de técnica de 2010.
  - **`correcoes-G17` (R-12):** Pathways/Associações = 2 e TPP/Generalização = 4. As duas métricas são rediscretizadas inteiras pela regra que 2010 aplicou (extremos do treino, G23), porque trocar um valor de treino pode mover o mínimo ou o máximo e mudar a classe de outros domínios.
  - **`classes-com-auxiliares` (R-13):** "Número total de Classes" contada com as classes auxiliares do modelo itSIMPLE (*Utility*, *Global*; coluna `classes_xml` de `data/2010/modelos_itsimple_2010.csv`), rediscretizada da mesma forma.
  - **`linha-de-base` (R-15):** sem características. Cada planejador recebe a média das suas notas nos 10 domínios de treino, a mesma nos 3 domínios de validação (G20).
- **R-11:** correção de rótulo, sem cálculo. Registrada em `data/2010/rotulos_corrigidos.csv`. Os arquivos de dados mantêm o rótulo publicado, para rastreabilidade.
- **R-13, critério da Agregação:** quatro critérios candidatos foram contados nos XML dos 13 modelos itSIMPLE (`acervo-2010/planejadores_analise_resultados/itSIMPLE/examples/`) e comparados com a Tabela 9. A contagem foi feita por comando nesta sessão; não há script versionado.

## Como reproduzir

```
uv run --no-project python experimentos/analise/nivel2.py
```

## Resultado

**Onde estão os resultados:** `experimentos/analise/nivel2/cenarios.csv` e `rankings.csv`.

| Cenário | Classes diferentes da referência | Acerto por posição (Storage / Zeno / Elevator) | Correlação de postos |
|---|---|---|---|
| Referência | 0 | 50% / 30% / 40% | 0,81 / 0,86 / 0,61 |
| Correções G17 (R-12) | 6 | 50% / 30% / 40% | 0,81 / 0,86 / 0,61 |
| Classes com auxiliares (R-13) | 1 | 50% / 30% / 40% | 0,81 / 0,86 / 0,61 |
| Linha de base (R-15) | — | 0% / 0% / 10% | 0,75 / 0,68 / 0,65 |

- **Correções G17:** as 6 classes que mudam são todas de Associações.
  - O Pathways passa de Médio a Baixo, como o G17 previa.
  - Como 2 é o novo mínimo, Blocks World, Depots, Gripper, TPP e Elevator passam de Baixo a Médio.
  - A generalização do TPP não muda de classe.
  - A maior mudança numa nota prevista é de 0,19; nenhum *ranking* muda.
- **Classes com auxiliares:** o Depots passa a ter 10 classes, o novo máximo, e o Storage cai de Alto a Médio. A maior mudança numa nota prevista é de 0,07; nenhum *ranking* muda.
- **Critério da Agregação (R-13):** nenhum dos quatro critérios reproduz a Tabela 9.

| Critério contado no XML | Domínios em que bate com 2010 |
|---|---|
| Associações com extremo de agregação ou composição | 1 de 13 |
| Atributos cujo tipo é outra classe | 2 de 13 |
| Autoassociações (a classe se liga a ela mesma) | 6 de 13 |
| Total de associações | 0 de 13 |

## Interpretação

- **R-11:** a característica que 2010 apontou como a de maior impacto se chama, corrigida, "Número Médio de Atores por Caso de Uso" (atores ÷ casos de uso). A leitura de 2010 precisa ser invertida. `[FATO]` (G1)
  - O exemplo da AF-234 fala em um domínio com muitos atores, muitos casos de uso e valor baixo. Pela fórmula, valor baixo quer dizer poucos atores por caso de uso: cada ator se liga a **muitos** casos de uso, não a poucos, como o texto de 2010 conclui.
  - AF-281, AF-282 e AF-331 mantêm o sentido, mas o nome da característica muda.
  - Na nova versão, usar o rótulo corrigido em todo o texto.
- **R-12 e R-13 (classes):** as duas correções de contagem mudam classes, mas não mudam nenhum *ranking*. As conclusões de validação de 2010 não dependem desses erros de contagem. `[FATO]`
- **R-13 (Agregação):** o critério de contagem da Agregação não pode ser reconstruído dos modelos itSIMPLE. `[FATO]`
  - O texto de 2010 descreve a agregação no Blocks World pela semântica ("os blocos podem ser agregados sobre a mesa", "os blocos podem ser empilhados") e com base na Figura 11, um diagrama UML desenhado à parte, não no modelo itSIMPLE.
  - `[HIPÓTESE]` A Agregação foi contada por julgamento semântico de quem modelou, relação por relação.
  - Só o autor pode confirmar o critério. Sem essa confirmação, a métrica fica registrada como não reproduzível, e a AF-331, que a lista entre as seis mais impactantes, precisa dessa ressalva.
- **R-15:** ao lado de cada resultado de validação agora sai a linha de base sem características.
  - Pela correlação de postos, o método de 2010 supera a linha de base no Storage (0,81 contra 0,75) e no Zeno-travel (0,86 contra 0,68), e fica abaixo no Elevator (0,61 contra 0,65).
  - `[HIPÓTESE]` Com 10 planejadores por domínio, diferenças dessa ordem estão dentro do que o acaso explica. A linha de base segue como comparação obrigatória em todo resultado do Nível 4.

## Problemas e desvios

- O acerto por posição da linha de base (0% / 0% / 10%) difere do G20 (10% / 10% / 0%) porque os empates são desfeitos de outro modo: aqui, pela ordem publicada em 2010, igual em todos os cenários; no G20, pela ordem da tabela observada. A correlação de postos, que não depende de desempate, é a mesma. Isso reforça a recomendação do G19 de não usar o acerto por posição como medida principal.
- Os critérios de Agregação foram contados por comando nesta sessão, não por script versionado.
