# Dataset 2010

Dados da dissertação em formato processável. Entregável da Fase 0: `dataset-2010.csv` (ou conjunto de CSVs).

## Origem provável

- `acervo-2010/planejadores_analise_resultados/comp/script.sql`: tabelas `dominios`, `planejadores`, `caracteristicas`, `tecnicas`, `dominios_caracteristicas`, `planejadores_tecnicas`, `planejamentos`.
- Planilhas em `acervo-2010/planejadores_analise_resultados/` para as contagens brutas.
- Tabelas 8–25 da dissertação, para conferência.

Detalhes e anomalias conhecidas: [../../docs/catalogo-acervo-2010.md](../../docs/catalogo-acervo-2010.md).

## Pendente

- [ ] Resolver a anomalia das linhas de `dominios_caracteristicas` (domínios 6–10 com 37 linhas em vez de 17).
- [ ] Exportar cada tabela para CSV com script versionado.
- [ ] Conferir cada tabela contra a dissertação (conferência manual obrigatória).
- [ ] Localizar as contagens brutas das 17 características.
