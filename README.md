# Domínios × Técnicas de Planejamento — Revisão da dissertação de 2010

Revisão e evolução da dissertação de mestrado *Relação entre características de domínios e técnicas de planejamento* (Matheus Haddad, Centro Universitário da FEI, 2010; orientador: Prof. Dr. Flavio Tonidandel).

A pergunta original: nenhum planejador é o melhor em todos os domínios, e características do domínio podem indicar a técnica mais promissora. Desde 2010 a área desenvolveu essa linha sob o nome de *seleção de algoritmos* e *portfólios de planejadores*. Este projeto refaz o trabalho com o estado da arte e os recursos de hoje, verifica o que das conclusões originais se sustenta e testa se o princípio de ajuste entre problema e técnica ajuda a escolher configurações de agentes de IA no desenvolvimento de software.

**Versão final da dissertação:** [redacao/final/dissertacao-haddad-2026.docx](redacao/final/dissertacao-haddad-2026.docx), revisada pelo autor em 29/09/2026.

**Documento de trabalho:** [plan/plano-revisao-dissertacao.md](plan/plano-revisao-dissertacao.md) — fases, perguntas de pesquisa, riscos, registros de decisão e de uso de IA.

**Retomando o trabalho (pessoa ou agente):** comece por [MEMORY.md](MEMORY.md), que registra o estado da execução, as pendências e o log de sessões.

## Estrutura

| Pasta | Fase | O que contém |
|---|---|---|
| [MEMORY.md](MEMORY.md) | — | Memória de execução: estado atual, pendências, log de sessões |
| [plan/](plan/) | — | Plano de trabalho vivo (painel, decisões, registro de IA, changelog) |
| [acervo-2010/](acervo-2010/) | 0 | Material original, **somente leitura**: dissertação, planejadores, domínios, resultados, modelos itSIMPLE |
| [docs/](docs/) | 0 | Catálogo do acervo e notas de apoio |
| [data/](data/) | 0, 3, 4B | Datasets: `2010/` (transcrito da dissertação), `ipc-2011-2023/`, `planner-museum/` |
| [literatura/](literatura/) | 1 | Protocolo de busca, notas de leitura, sínteses por eixo, referências verificadas |
| [auditoria/](auditoria/) | 2 | Classificação das afirmações de 2010: mantém / reformula / descarta |
| [experimentos/](experimentos/) | 3 | Contêineres, benchmarks, planejadores, extratores de *features*, execuções, análise |
| [llm/](llm/) | 4 | Experimentos X1–X4 (LLM como planejador, tradutor, seletor, com verificador) |
| [ponte-software/](ponte-software/) | 5 | Síntese exploratória e dossiê do capítulo 7 (sem piloto) |
| [redacao/](redacao/) | 6 | **Versão final** (`final/`), capítulos em Markdown da versão gerada, montagem, pareceres e material para o orientador |
| [templates/](templates/) | — | Modelos de nota de leitura, registro de experimento e de uso de IA |

## Fases

| # | Fase | Status |
|---|---|---|
| 0 | Enquadramento e artefatos | 🟢 concluída |
| 1 | Revisão de literatura assistida por IA | 🟢 concluída |
| 2 | Auditoria da versão original | 🟢 concluída |
| 3 | Infraestrutura e replicação experimental | 🟢 concluída |
| 4 | Camada LLM | 🟢 concluída |
| 4B | Panorama das IPCs posteriores a 2010 | 🟢 concluída |
| 5 | Ponte para desenvolvimento de software apoiado por IA | 🟢 concluída (exploratória) |
| 6 | Redação e compartilhamento | 🟡 versão final revisada pelo autor; falta o envio ao orientador (M3) |

**Produto final:** dissertação revisada, no padrão da FEI/ABNT: [redacao/final/](redacao/final/) (ver [redacao/README.md](redacao/README.md)).

O painel completo, com datas e entregáveis, fica no plano de trabalho. Este quadro só resume.

## Regras do projeto

1. Nenhuma referência entra sem verificação na fonte primária.
2. Nenhum número entra no texto sem vir de execução reprodutível (script versionado + dados + configuração).
3. Todo uso substantivo de IA é registrado (ferramenta, modelo, versão, finalidade).
4. A IA propõe, o autor decide. O texto final é na voz do autor.
5. Resultado e hipótese ficam separados, marcados com `[FATO]` e `[HIPÓTESE]`.
6. Modelos de linguagem usados em experimentos têm versão congelada e data registrada.

## O que não está neste repositório

- **Referências** (sem Zotero, decisão de 23/09/2026): obras verificadas por agente ficam em `candidatas.bib`; o autor aprova em `revisao-referencias.md` e o script gera o `referencias.bib`, a única fonte citável. Ver [literatura/referencias/](literatura/referencias/). As notas de leitura ficam no repositório, em [literatura/notas-de-leitura/](literatura/notas-de-leitura/).
- **Benchmarks das IPCs** e **planejadores de terceiros** (`experimentos/benchmarks/ipc/`, `experimentos/ferramentas/`): clones de repositórios públicos, ignorados pelo Git; os registros de experimento indicam repositório e commit.
- **Saídas brutas** (`experimentos/execucoes/brutos/`, `data/ipc-2011-2023/brutos/`) **estão versionadas** desde 29/09/2026, preservadas byte a byte (`.gitattributes`): as máquinas da Fase 3 foram apagadas e não há outra cópia.
- **Versão montada pela IA** (`redacao/saida/`): gerada por `redacao/montagem/montar.py`, fora do Git.
- **Lixo do acervo de 2010**: metadados `.svn`, objetos compilados (`.o`, `.pyc`) e `.DS_Store`. Todo o resto foi preservado.
