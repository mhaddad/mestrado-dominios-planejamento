# Dados

| Pasta | Conteúdo | Fase |
|---|---|---|
| `2010/` | Dataset da dissertação em formato processável (CSV) | 0 |
| `raw/` | Dados brutos e imutáveis de fontes externas (metadados de benchmarks, listas de planejadores) | 3 |
| `processed/` | Dados derivados: *features* extraídas, tabelas de desempenho, resultados agregados | 3 |

## Regras

- CSV com cabeçalho, UTF-8, separador vírgula.
- Cada dataset tem um `README.md` (ou seção aqui) com: origem, como foi obtido, script que o gera, data.
- Nada em `processed/` é editado à mão. Se precisa mudar, muda o script que o gera.
- Arquivos grandes (mais de 50 MB) não entram no Git; documente onde estão e como reproduzir.
