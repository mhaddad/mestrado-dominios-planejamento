---
titulo: "Apêndices"
status: revisado-por-ia
data: 2026-09-28
fonte: auditoria/taxonomia/; experimentos/execucoes/; README.md
---

# Apêndices {.unnumbered}

## Apêndice A — Codificação dos planejadores {.unnumbered}

A codificação completa dos planejadores na taxonomia em quatro dimensões está em arquivos versionados no repositório: `auditoria/taxonomia/planejadores_4d.csv` contém os dez planejadores de 2010; `auditoria/taxonomia/planejadores_museu_4d.csv`, os planejadores do Planner Museum; e `data/ipc-2011-2023/planejadores_4d.csv`, as codificações por trilha das IPCs de 2011 e 2018. As fontes primárias e as decisões de codificação estão em `auditoria/taxonomia/fontes-planejadores.csv` e `auditoria/taxonomia-tecnicas.md`.

Cada registro distingue algoritmo e espaço de busca, heurística, representação e arquitetura. Nos casos de portfólio, os campos registram a composição descrita na fonte e a regra aplicada é documentada em `docs/fase4b-desenho.md`.

## Apêndice B — Registros de experimento {.unnumbered}

Cada experimento possui um registro com objetivo, dados, comandos, resultados e limitações. A tabela a seguir identifica os registros usados nesta dissertação.

| Código | Tema | Registro |
|---|---|---|
| EXP-01 | Execução dos planejadores de 2010 em ambiente local | `2026-09-24-teste-orbstack.md` |
| EXP-02 | Calibração do limite de tempo | `2026-09-24-calibracao-2010.md` |
| EXP-03 | Reprodução do método de 2010 | `2026-09-24-reproducao-nivel1.md` |
| EXP-04 | Discretização pela regra escrita | `2026-09-24-nivel2-discretizacao.md` |
| EXP-05 | Reexecução homogênea no GCP | `2026-09-27-nivel3-gcp.md` |
| EXP-06 | Taxonomia em quatro dimensões | `2026-09-26-nivel2-taxonomia-4d.md` |
| EXP-07 | Extrator das métricas de 2010 a partir do PDDL | `2026-09-26-extrator-metricas-2010.md` |
| EXP-08 | Correções de métricas e classes | `2026-09-26-nivel2-correcoes.md` |
| EXP-09 | Perda em relação ao *virtual best* | `2026-09-26-nivel2-perda-vbs.md` |
| EXP-10 | Robustez da discretização | `2026-09-26-robustez-discretizacao.md` |
| EXP-11 | *Features* da representação SAS+ | `2026-09-26-features-sas.md` |
| EXP-12 | Nível 4 com resultados publicados | `2026-09-26-nivel4-publicados.md` |
| EXP-13 | Nível 4 por técnica | `2026-09-26-nivel4-tecnicas.md` |
| EXP-14 | LLM como seletor, catálogo anônimo | `2026-09-26-x3-llm-seletor.md` |
| EXP-15 | LLM como seletor, catálogo com nomes | `2026-09-26-x3-nomes.md` |
| EXP-16 | LLM como planejador | `2026-09-26-x1-llm-planejador.md` |
| EXP-17 | LLM com verificador formal | `2026-09-26-x4-llm-verificador.md` |
| EXP-18 | LLM como tradutor para PDDL | `2026-09-27-x2-llm-tradutor.md` |
| EXP-19 | Método de 2010 com notas do Nível 3 | `2026-09-27-nivel3-metodo.md` |
| EXP-20 | Qualidade dos planos | `2026-09-27-nivel3-qualidade.md` |
| EXP-21 | Características × famílias de técnica nas IPCs | `2026-09-27-q5-ipc.md` |
| EXP-22 | Tempo e memória no Nível 3 | `2026-09-27-nivel3-tempo-memoria.md` |
| EXP-23 | Planejamento com nomes ofuscados | `2026-09-27-x1-ofuscado.md` |
| EXP-24 | Seleção por instância nas IPCs | `2026-09-27-r29-instancias.md` |
| EXP-25 | Topologia de busca na Q5 e no R-29 | `2026-09-28-topologia-q5.md` |

: Registros de experimento utilizados na dissertação

::: fonte
Fonte: Autor.
:::

## Apêndice C — Reprodutibilidade {.unnumbered}

O repositório contém os dados derivados, *scripts*, registros de execução e instruções de ambiente. O acervo de 2010 é preservado como somente leitura; os dados processados ficam em `data/`, a auditoria em `auditoria/`, os experimentos em `experimentos/` e as fontes bibliográficas em `literatura/`.

O ambiente Python é criado com Python 3.12 e `uv`:

```sh
uv venv .venv --python 3.12
uv pip install -r requirements.txt
```

Os registros do Apêndice B indicam o comando específico de cada análise. Para conferir que uma citação do texto possui referência aprovada, usa-se:

```sh
python3 literatura/scripts/checar_citacoes.py redacao/capitulos/arquivo.md
```

O documento final é montado a partir dos capítulos em Markdown, do arquivo bibliográfico e do estilo definido para o guia da FEI:

```sh
uv run --no-project --with python-docx python redacao/montagem/montar.py
```

Saídas brutas de planejadores, *benchmarks* e credenciais não são versionados. Os registros indicam a origem, o ambiente e os limites necessários para reproduzir cada resultado derivado.
