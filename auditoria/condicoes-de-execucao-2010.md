# Condições de execução dos experimentos de 2010 (F6)

Resposta à fragilidade F6: como foram obtidos os dados da 5ª etapa do método (eficiência de planejadores em domínios que não constam nos resultados das competições).

Legenda: `[FATO]` = declarado na dissertação ou observado nos arquivos. `[A CONFIRMAR]` = falta evidência.

## O que a dissertação declara `[FATO]`

Fonte: seção "Resultados da eficiência dos planejadores" (antes da Tabela 14).

- Planejadores "obtidos nos websites ou através de contatos com os seus autores na **versão original utilizada nas competições internacionais**".
- Executados em **8 computadores** com a mesma configuração: **Intel Core 2 Duo 2,5 GHz, 4 GB de RAM**, **Linux Ubuntu 9.04**.
- **Timeout de 20 minutos** por problema.
- Cerca de **2.000 processos** de planejamento.
- Para cada par planejador × domínio, "um arquivo contendo os planos gerados e o tempo para gerar cada um".
- Motivo das execuções: domínios e planejadores foram criados em anos diferentes e participaram de edições diferentes das competições, então faltavam pares nas Tabelas 12 e 13.
- Medida de eficiência: **percentual de problemas resolvidos** (cobertura). Tempo e qualidade do plano não entram (F5).

## O que os arquivos confirmam `[FATO]`

- Scripts em `acervo-2010/.../comp/planners/scripts/<planejador>/` e `comp/planners/*.sh~` usam `timeout 1200` (= 20 min), com caminhos absolutos `/home/matheus/mestrado/comp/…`.
- Dos 100 pares planejador × domínio de treino, **38 vêm de resultados de competição e 62 de execução própria** segundo a Tabela 12/13 (na verdade 34 e 66, ver G21) (`data/2010/eficiencia_planejadores.csv`, coluna `origem_do_dado`).
- Nos 62 pares de execução própria há 1.712 problemas; somados aos 300 de Storage (10 planejadores × 30 problemas), dão 2.012. Isso é **compatível com "cerca de 2.000"**, mas é uma coincidência de ordem de grandeza, não uma prova de que foram esses.
- As contagens de problemas resolvidos por par estão em `contabilizacao_problemas.ods` (`data/2010/problemas_resolvidos.csv`). Ela tem valor em 63 dos 100 pares de treino (59 de execução própria e 4 de competição: Depots e Driverlog com Fast Downward e R) e concorda com a Tabela 14 em todos eles (tolerância de 1 ponto percentual). Está em branco em 37 pares; 34 são pares de competição, 1 é Pathways × R (a Tabela 14 tem 0%, compatível) e **2 são lacunas reais: Depots × LPG e Driverlog × LPG**, em que a Tabela 14 tem 100% e 90%.
- **Binários chamados pelos scripts finais** (`comp/planners/scripts/<planejador>/*.sh`, lidos em 21/09/2026): `./ff` (FF v2.3), `./lpg-td-1.0`, `./maxplan`, `./r.execute`, `./yahsp`, `./satplan` (SatPlan 2006), `./sgplan6` (**SGPlan 6**, não o 5.22). Os `*.sh~` são rascunhos anteriores: os `satplan_*.sh~` chamam `./sgplan6` por cópia dos scripts do SGPlan, e os `.sh` finais corrigem para `./satplan`, então **não há contaminação** entre os dois planejadores.
- **Identidade por hash (SHA-1):** os binários `blackbox`, `ffv-2.3`, `maxplan` (e `londex`), `sgplan6` e `sgplan522` de `comp/planners/` são idênticos aos de `itSIMPLE/myPlanners/`. Isso fixa a versão exata de 4 dos 10 planejadores (Blackbox, FF, MaxPlan e SGPlan; o SGPlan tem duas versões idênticas). Os outros 6 (IPP, R, LPG, Fast Downward, YAHSP, SATPlan) só existem em `comp/planners/`.
- Fast Downward: pasta `fastdownward` com fonte, sem versão explícita e sem scripts em `scripts/fastdownward/` (só `fastd_blocksworld.sh~` em `comp/planners/fastdownward/`).

## O que falta `[A CONFIRMAR]`

- **Limite de memória por processo.** A máquina tinha 4 GB; não há registro de limite imposto (`ulimit`) nem de falhas por memória.
- **Como um "problema não resolvido" foi contado:** timeout, falta de memória, erro do planejador ou plano inválido? Não há registro de validação dos planos (por exemplo, com VAL).
- **Versão exata de cada planejador** usada, e de qual competição (IPC 2002, 2004, 2006, 2008?).
- ~~**Se os problemas usados foram os mesmos das competições** ou um subconjunto.~~ **Respondido pelo autor em 23/09/2026:** onde só as primeiras N instâncias foram usadas (Blocks World 35 de 102, Logistics 28 de 84, Satellite 20 de 36; achado G14), o corte buscou igualar o subconjunto usado nos resultados publicados da IPC. `[A CONFIRMAR]` na Fase 3: conferir, nas páginas de resultados de cada IPC, que o subconjunto publicado é de fato esse.
- **Distribuição das execuções pelas 8 máquinas** e se houve execução concorrente em cada uma.
- **Domínios sem PDDL no acervo:** Zeno-travel e Elevator.
- **Ambiguidade de "célula vazia" vs. "zero"** em `contabilizacao_problemas.ods`: a planilha não distingue "não executado" de "zero resolvidos".

## Implicação para a Fase 3

Os dados de 2010 vêm de duas populações diferentes: **34** pares de competição (hardware e limites de cada IPC) e **66** de execução própria (hardware único, timeout de 20 min). A dissertação e o `origem_do_dado` contam 38 e 62, mas 4 valores da Tabela 12 (R e Fast Downward no Depots e no DriverLog) vieram de execução própria (achado G21, 23/09/2026). Na replicação, o mesmo hardware e limite devem valer para todos os planejadores (desenho da Fase 3). Até lá, qualquer comparação com 2010 deve levar `origem_do_dado` em conta.
