# Registro de experimento — EXP-01: os planejadores de 2010 no OrbStack

| Campo | Valor |
|---|---|
| ID | EXP-01 |
| Data | 24/09/2026 |
| Fase | 3 |
| Pergunta | Q1 (viabilidade da reexecução, Nível 3 de `auditoria/reexecucao.md`) |
| Autor da execução | Claude Code (Coordenador, claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `experimentos/containers/orbstack/provisionar.sh` e `experimentos/planejadores/teste_2010.sh` (commit deste registro).
- **Dados de entrada:** planejadores e PDDL do acervo (`acervo-2010/planejadores_analise_resultados/comp/`), copiados para `~/fase3/planners-2010` dentro da máquina; o acervo não é alterado.
- **Ambiente:** Mac com Apple M4 (24 GB). Máquina OrbStack `fase3-amd64`: Ubuntu 22.04.5 LTS amd64, *kernel* 7.0.14-orbstack, 9 CPUs virtuais, 11 GB de memória. Os binários de 2010 são ELF 32-bit Intel 80386; rodam por **QEMU i386** (registrado em `binfmt_misc`), não pelo Rosetta, que atende só x86_64.
- **Dependências instaladas:** bibliotecas i386 do Ubuntu (libc6, libstdc++6, libgcc-s1, libncurses5, libtinfo6, zlib1g), `python2` 2.7.18 (tradutor do Fast Downward), Tcl 8.6.12 (scripts do R) e `libreadline5` i386 do Ubuntu 20.04 (SWI-Prolog 3.2.9 do acervo, usado pelo R).
- **Limites:** 120 s no teste de fumaça; 600 a 1.200 s nas medições de tempo. Sem limite de memória.
- **Semente(s) aleatória(s):** não definidas (o LPG-TD usa semente própria; não afeta este teste).

## Como reproduzir

```
orb create --arch amd64 ubuntu:jammy fase3-amd64
orb -m fase3-amd64 -u root bash experimentos/containers/orbstack/provisionar.sh
orb -m fase3-amd64 bash experimentos/planejadores/teste_2010.sh driverlog pfile1 120
```

As medições de tempo do R e do Fast Downward usaram as mesmas chamadas do script, nos problemas `pfile3`, `pfile8`, `pfile16` e `pfile20` do DriverLog.

## Resultado

- **Onde estão os resultados:** logs em `~/fase3/teste-2010/` dentro da máquina (brutos, não versionados); números abaixo.

**1. Os 10 planejadores rodam e acham plano** no DriverLog `pfile1`, com as linhas de comando dos scripts finais de 2010 (`comp/planners/scripts/`). `[FATO]`

| Planejador | Terminou | Evidência de plano no log | Tempo (s) |
|---|---|---|---|
| Blackbox | sim | `Begin plan` | 0,27 |
| IPP | sim | `found plan` | 0,16 |
| FF 2.3 | sim | `found legal plan` | 0,14 |
| LPG-TD 1.0 | sim | `solution found` | 0,77 |
| YAHSP | sim | `Valid plan : 8 actions` | 0,20 |
| SGPlan 6 | sim | `Solution found` | 0,30 |
| SATPlan 2006 | sim | `SAT! Solved in 6 layers` | 1,83 |
| MAXPLAN | sim | `solution found` | 0,38 |
| Fast Downward | sim | `Solution found` | 2,19 |
| R | sim | plano completo | 4,44 |

**2. Fidelidade e custo da emulação**, comparando com os logs de 2010 (`comp/planners/resultados/`). `[FATO]`

| Planejador | Problema | 2010: tempo / comprimento do plano | 2026 (emulado): tempo / comprimento | Razão de tempo |
|---|---|---|---|---|
| R | dlog-2-2-2 (`pfile1`) | 0,45 s / 100 | 3,59 s / 100 | 8,0 |
| R | dlog-2-2-4 (`pfile3`) | 4,58 s / 775 | 20,05 s / 775 | 4,4 |
| R | dlog-3-3-7 (`pfile8`) | 3,1 s / 586 | 15,91 s / 586 | 5,1 |
| Fast Downward | `pfile16` | 44,36 s / 239 | 71,25 s / 191 | 1,6 |
| Fast Downward | `pfile20` | 8,52 s / 184 | 53,9 s / 172 | 6,3 |

## Interpretação

- O R reproduz **os mesmos planos** de 2010 e fica de **4,4 a 8 vezes mais lento** que a máquina de 2010 (Core 2 Duo 2,5 GHz). A razão maior no problema menor inclui o custo fixo de iniciar o Prolog emulado.
- O Fast Downward acha **planos diferentes** dos de 2010. `[HIPÓTESE]` O tradutor em Python 2 depende da ordem de iteração de dicionários, que mudou entre o Python de 2010 (Ubuntu 9.04, provavelmente 2.6) e o 2.7.18 usado aqui. Com trajetórias de busca diferentes, as razões de tempo (1,6 e 6,3) não medem só a emulação.
- `[HIPÓTESE]` Com um limite de 20 minutos, problemas que em 2010 levaram mais de 3 a 5 minutos podem estourar o tempo sob emulação. A cobertura reexecutada com o limite original tenderia a ser **menor** que a de 2010 por causa do ambiente, não do planejador.

## Problemas e desvios

- **Recriação da máquina:** a primeira máquina (Ubuntu 24.04) foi apagada e recriada em 22.04, porque o 24.04 não tem `python2`.
- **Scripts de 2010 com duas versões:** os `.sh~` da pasta principal diferem dos scripts finais em `scripts/` (LPG-TD com `-speed -noout`; SGPlan e MAXPLAN com `-o`/`-f`; FF com `-p`). O teste usa os finais, que batem com os logs. O IPP tem três binários diferentes no acervo; usa-se o de `scripts/ipp/`, o único que não falha.
- **Ajustes no R** (só na cópia): caminho do SWI-Prolog e do `tclsh` trocados nos scripts Tcl (`/local/bin/tclsh` e `/usr/local/bin/pl` não existem na máquina).
- **Decisão pendente:** como tratar o limite de tempo na reexecução (Nível 3). Opções registradas no plano, ação 19.
