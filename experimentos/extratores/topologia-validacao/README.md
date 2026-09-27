# Validação do extrator de topologia (27/09/2026)

Extrator: `experimentos/extratores/topologia_sas.py`. Script: `experimentos/extratores/validar_topologia.py`. Referência: Hoffmann (2011), Tabela 3 (`hoffmann2011analyzing`, p. 184), colunas SP (R = 10) e DE.

Critérios fixados antes de rodar e resultado:

| Critério | Resultado |
|---|---|
| 1. Resultado básico em todas as tarefas do Logistics e em nenhuma dos outros domínios | OK (10 de 10 no Logistics; 0 nos demais) |
| 2. Spearman da taxa de sucesso da sondagem (SP) por domínio com a Tabela 3 ≥ 0,7 | OK: 0,966 |
| 3. Spearman da taxa de becos sem saída (DE) por domínio com a Tabela 3 ≥ 0,7 | OK: 0,987 |

- 30 domínios com dados, 315 tarefas, 10 estados amostrados por tarefa. Din-Phil e Opt-Tele ficaram de fora (axiomas).
- **Maior discrepância: Openstacks.** Com a pasta `openstacks-sat08-strips` (mapeamento fixado antes de rodar), SP 86% e DE 14%, contra 21,3% e 79,1% na tabela. Conferência feita depois, fora dos critérios: com `openstacks-strips` (versão STRIPS de 2006), 5 tarefas dão SP 34% e DE 66%. A diferença vem da versão do domínio.
- Grid tem só 5 problemas na pasta. No Mystery, `prob07.pddl` não tem plano relaxado no estado inicial (tarefa sem solução).
- Arquivos: `tarefas.csv` (uma linha por tarefa) e `dominios.csv` (agregado por domínio, com os valores da Tabela 3 ao lado).
