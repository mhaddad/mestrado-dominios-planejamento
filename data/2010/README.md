# Dataset 2010

Dados da dissertação de 2010 em formato processável. **Fonte de verdade: as tabelas publicadas na dissertação** (`acervo-2010/dissertacao/dissertacao-haddad-2010.docx`). O `script.sql` e as planilhas do acervo servem de conferência.

Status: gerado e conferido por máquina em 21/09/2026. **Conferência manual amostral pelo autor: pendente.**

## Arquivos

| Arquivo | Linhas | Conteúdo | Tabelas da dissertação |
|---|---|---|---|
| `dominios.csv` | 13 | 10 domínios de treino + 3 de validação; pasta correspondente no acervo | — |
| `planejadores.csv` | 10 | Planejadores; pasta correspondente em `comp/planners/` | — |
| `metricas.csv` | 17 | As 17 métricas e o diagrama UML de origem | 5, 6, 7 |
| `metricas_dominios.csv` | 221 | Valor bruto e classe (Baixo/Médio/Alto) de cada métrica em cada domínio (13 × 17) | 8–11, 26, 32, 38 |
| `eficiencia_planejadores.csv` | 100 | Por planejador × domínio de treino: eficiência (competição e completa, em %), nota 0–10, origem do dado | 12–17 |
| `planejadores_tecnicas.csv` | 47 | Técnicas de cada planejador (formato longo) | 2, 3, 4 |
| `validacao_ranking.csv` | 30 | Nos 3 domínios de validação: posição e média propostas pelo método × posição e nota reais | 30, 31, 36, 37, 42, 43 |
| `problemas_resolvidos.csv` | 110 | Nº de problemas resolvidos por planejador × domínio (inclui Storage), da planilha | — (base das Tabelas 14–15) |
| `extraido/` | — | Texto integral (`texto.md`) e as 44 tabelas do docx, uma por CSV, sem tratamento | 1–44 |
| `conferencia/` | — | Relatório de conferência contra o SQL e contra os modelos itSIMPLE | — |
| `scripts/` | — | Scripts que geram tudo acima | — |

Convenções: UTF-8, fim de linha LF, vírgula, ponto decimal, célula vazia = dado ausente. Eficiência em pontos percentuais (`25` = 25%). Domínios em *slug* (`blocksworld`, `logistics`, `pipesworld`…). Planejadores com grafia única (`Fast Downward`, `SATPlan`, `MaxPlan`).

`origem_do_dado` = `competicao` quando a Tabela 12/13 tem valor (etapa 4 do método); `execucao_propria` quando o valor veio de execução do autor (etapa 5). São 38 pares de competição e 62 de execução própria.

## Como regenerar

```bash
uv venv .venv --python 3.12 && uv pip install -r requirements.txt
.venv/bin/python data/2010/scripts/extrair_dissertacao.py        # docx -> extraido/
.venv/bin/python data/2010/scripts/construir_dataset_2010.py     # extraido/ -> CSVs
.venv/bin/python data/2010/scripts/extrair_contabilizacao.py     # planilha .ods -> problemas_resolvidos.csv
.venv/bin/python data/2010/scripts/conferir_dataset_2010.py      # docx x script.sql
.venv/bin/python data/2010/scripts/comparar_modelos_itsimple.py  # docx x XML do itSIMPLE
```

## Resultado da conferência

Detalhe em [conferencia/conferencia_sql.md](conferencia/conferencia_sql.md).

| Verificação | Resultado |
|---|---|
| Classes Alto/Médio/Baixo: dissertação × SQL (bloco 1) | 170/170 iguais |
| Eficiência: dissertação × SQL | 100/100 iguais (o SQL guarda decimais que a dissertação arredondou; ver `conferencia/eficiencia_precisa_sql.csv`) |
| Notas: dissertação × SQL | 100/100 iguais |
| Planejador × técnica: Tabela 4 × matriz das Tabelas 2–3 | 47/47 iguais |
| Planejador × técnica: dissertação × SQL | **Diferem** (o SQL é uma versão anterior da taxonomia; ver abaixo) |
| Consistência interna: casos de uso = métodos = ações | 12 de 13 domínios (exceção: Elevator, é da própria dissertação) |
| Eficiência: planilha `contabilizacao_problemas.ods` × dissertação | Concorda em todos os 63 pares em que a planilha tem valor (tolerância de 1 p.p.); 2 lacunas reais (Depots × LPG, Driverlog × LPG) |

## Limitações conhecidas

- **Só uma fonte** para os valores brutos das métricas (Tabelas 8–9, 26, 32, 38): o SQL só tem as classes discretizadas. A conferência parcial contra os XML do itSIMPLE cobre 4 das 17 métricas (ver `conferencia/modelos_itsimple.csv`).
- **`script.sql` é uma concatenação com sobras:** bloco 2 de `dominios_caracteristicas` (100 linhas, domínios 6–10, com características 18–20 inexistentes), `planejadores_tecnicas` duplicado e um fragmento truncado na linha 298. Nada disso entra no dataset.
- **Taxonomia de técnicas do SQL ≠ Tabela 4:** o SQL tem `Linear` e `Non-Linear` (10 pares) que a dissertação não usa, e omite 5 pares que a Tabela 4 tem (Forward-chaining em IPP, MaxPlan, SATPlan e SGPlan; Heuristic Search em LPG). A Tabela 4 é a que sustenta as Tabelas 18–25.
- **Grafia preservada nos rótulos de técnica:** `Heurist Search` (sic), como na dissertação.
- Domínios de validação (Storage, Zeno-travel, Elevator) só têm métricas e ranking; não há eficiência por planejador completa como nos de treino. Não há PDDL de Zeno-travel nem de Elevator no acervo.
