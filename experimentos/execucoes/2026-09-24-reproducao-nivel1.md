# Registro de experimento — EXP-03: reprodução do método de 2010 por script (Nível 1)

| Campo | Valor |
|---|---|
| ID | EXP-03 |
| Data | 24/09/2026 |
| Fase | 3 |
| Pergunta | Q1 (Nível 1 de `auditoria/reexecucao.md`: R-05 a R-08) |
| Autor da execução | Claude Code (Coordenador, claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `experimentos/analise/reproducao_2010.py` (só biblioteca padrão).
- **Dados de entrada:** `data/2010/` (métricas, classes, eficiências, notas, técnicas) e as tabelas publicadas em `data/2010/extraido/`. Nenhum planejador é executado.
- **Ambiente:** Mac, Python 3.12 via `uv`. Determinístico.

## Como reproduzir

```
uv run --no-project python experimentos/analise/reproducao_2010.py
```

## Resultado

- **Onde estão os resultados:** `experimentos/analise/reproducao-2010/` (um CSV por etapa, com o valor publicado e o reproduzido lado a lado, e `resumo.txt`).

| Etapa de 2010 | Tabelas | Reproduzido | Observação |
|---|---|---|---|
| 3. Discretização | 10–11, 26, 32, 38 | 220 de 221 classes | Regra aplicada ≠ regra descrita (G23). Exceção: Logistics / ações de saída = 4, publicada Baixo |
| 5. Eficiência → nota | 16–17 | 100 de 100 notas | Nota = eficiência exata ÷ 10, arredondada com o meio para cima (resolve G6) |
| 7. Característica × técnica | 19–20 | 535 de 539 células | As 4 divergências somem com o IPP fora de *Forward-chaining* (49 de 49 na coluna; G24) |
| 8. Relevância | 21–23 | 49 de 49 características | Classe, menor e maior conferem; a coluna "Variância" não se reproduz por nenhuma fórmula testada (populacional, amostral, desvios, subconjuntos de técnicas) |
| 8. Marcas de impacto | 24–25 | 179 de 187 | `[HIPÓTESE]` regra "diferença ≥ 3 entre as classes da métrica"; a regra não está escrita em 2010. 5 das 8 falhas na coluna *Backward-chaining* (um só planejador) |
| Validação: células | 27–28, 33–34, 39–40 | 561 de 561 | Cópia correta das Tabelas 19–20 |
| Validação: médias por técnica | idem | 33 de 33 | Com arredondamento ou truncamento (G18) |
| Validação: *rankings* | 30, 36, 42 | 1 de 3 na mesma ordem | Zeno-travel e Elevator só diferem dentro de empates publicados (6,90 e 6,26), que os valores exatos desempatam de outro modo (G18) |

## Interpretação

- O método de 2010 é reproduzível quase por inteiro a partir dos dados publicados. As exceções são pontuais e explicadas, exceto a coluna "Variância" das Tabelas 21–23, que não influi em nenhuma classificação.
- **G23.** A discretização efetivamente aplicada foi: menor valor dos domínios de treino = Baixo, maior = Alto, todo o resto = Médio (169 de 170 no treino; 51 de 51 na validação, em relação aos extremos do treino). A regra descrita no texto (cortes na variância e no dobro dela) reproduz só 80 de 170. `[HIPÓTESE]` Com essa regra, "Alto" e "Baixo" dependem de um único domínio extremo por métrica, e acrescentar um domínio pode reclassificar todos os outros.
- **G24.** As Tabelas 19–20 foram calculadas com o IPP fora de *Forward-chaining* (como no SQL, achado G3), mas a validação (Tabelas 29, 35, 41) usa o IPP com *Forward-chaining* (como na Tabela 4). O mesmo método usou duas taxonomias.

## Problemas e desvios

- Três métricas têm rótulos diferentes nas Tabelas 19–25 e nas Tabelas 8–11 ("Número Médio de Atores por Caso de Uso", "Agregação (pares todo-parte)", "Generalização (pares pai-filho)"); o script as trata como a mesma métrica.
- O Nível 1 não reproduz o segundo bloco de características do SQL (G10, R-09), que segue em aberto.
