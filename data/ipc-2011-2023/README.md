# Resultados das IPCs 2011–2023 (Fase 4B)

Dataset da Fase 4B, em construção. Por enquanto contém só o levantamento das fontes; o levantamento completo, com o que cada edição publicou e o que ainda está acessível, está em [`docs/resultados-ipc-2011-2023.md`](../../docs/resultados-ipc-2011-2023.md).

## Arquivos

| Arquivo | Conteúdo | Gerado por |
|---|---|---|
| `resumo_fontes.csv` | Uma linha por edição e trilha: granularidade, execuções, planejadores, linhas de base, domínios, tarefas por domínio, limites e execuções resolvidas | `scripts/levantar_fontes.py` |
| `brutos/` | Arquivos baixados das fontes (fora do Git) | `scripts/levantar_fontes.py` |

## Origem

- **IPC 2018:** `https://ipc2018-classical.bitbucket.io/results/{optimal,satisficing,agile}-results.tar.bz2` (JSON do *downward lab*), baixados em 27/09/2026. Sem licença declarada.
- **IPC 2023:** `index.md` do repositório `ipc2023-classical/ipc2023-classical.github.io` (tabelas por domínio). Limites de tempo e memória transcritos do mesmo arquivo (seção *Tracks*).
- **IBM/IPC-graph-data** (`ferber2019ipc`, ainda não citável): `problems/problem-names-{train,valid,test}.txt`, licença Apache-2.0.

## Como reproduzir

```sh
.venv/bin/python data/ipc-2011-2023/scripts/levantar_fontes.py
```

O script baixa os arquivos para `brutos/` só se ainda não estiverem lá.

## Observações

- `execucoes_resolvidas` de 2018 conta as execuções com `coverage` = 1, incluindo linhas de base e formulações alternativas (`-split`, `-combined`). Não é o placar oficial.
- `planejadores` exclui as linhas de base (nomes com `baseline`).
