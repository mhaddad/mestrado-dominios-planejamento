# Conferência: dissertação (docx) × `script.sql` do acervo

Gerado por `data/2010/scripts/conferir_dataset_2010.py`. Não editar à mão.

## 0. Mapeamento de ids

| id | domínio (SQL) → slug | planejador (SQL) → canônico |
|---|---|---|
| 1 | Blocks World → blocksworld | Blackbox → Blackbox |
| 2 | Depot → depots | IPP → IPP |
| 3 | Driver Log → driverlog | FF → FF |
| 4 | Gripper → gripper | R → R |
| 5 | Logistic World → logistics | LPG → LPG |
| 6 | Mystery → mystery | Fast Downward → Fast Downward |
| 7 | Pathways → pathways | YAHSP → YAHSP |
| 8 | Pipes World → pipesworld | SGPlan → SGPlan |
| 9 | Satellite → satellite | SATPlan → SATPlan |
| 10 | TPP → tpp | MAXPlan → MaxPlan |

## 1. Classes Alto/Médio/Baixo (`dominios_caracteristicas`)

O SQL tem **2 blocos** desta tabela: bloco 1 = 170 linhas; bloco 2 = 100 linhas.

- **Bloco 1** cobre 10 domínios × 17 características = 170 pares (esperado 170).
  - Coincide com a dissertação em 170/170 pares; divergências: 0 (`divergencias_classes.csv`).
- **Bloco 2** cobre os domínios [6, 7, 8, 9, 10] com características 1 a 20.
  - Nas características 1–17 (85 pares) difere do bloco 1 em 43 pares (`divergencias_bloco2_vs_bloco1.csv`).
  - As características **18, 19 e 20** (15 valores) não existem na tabela `caracteristicas` do SQL nem na dissertação (`caracteristicas_18_a_20.csv`).

## 2. Eficiência e nota (`planejamentos`)

- Linhas no SQL: 100 (esperado 100)
- Eficiência coincide com a dissertação após arredondar para inteiro: 100/100 (dos quais 37 têm casas decimais no SQL que a dissertação arredondou)
- Nota coincide exatamente: 100/100
- Divergências: 0 (detalhe em `divergencias_eficiencia.csv`)

## 3. Planejadores × técnicas (`planejadores_tecnicas`)

- Blocos no SQL: 2, com [52, 52] linhas.
- Blocos idênticos entre si: True
- Pares na dissertação (Tabela 4): 47
- Bloco 1 × dissertação: só no SQL = 10, só na dissertação = 5
- Bloco 2 × dissertação: só no SQL = 10, só na dissertação = 5

## 4. Anomalias de integridade do `script.sql`

- Linha 298: texto solto após um INSERT completo: `cteristicas VALUES(5,20,"Alto");`. Parece o final de um `INSERT INTO dominios_caracteristicas` truncado por edição manual `[HIPÓTESE]`. Não foi incluído em nenhum bloco.

