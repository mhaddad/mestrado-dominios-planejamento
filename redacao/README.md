# Fase 6 — Redação e compartilhamento

**Objetivo:** produzir a nova versão do trabalho e compartilhar com o orientador.
**Critério de conclusão:** versão enviada e retorno registrado.

## Decisão de formato (autor, 21/09/2026)

A nova versão será uma **dissertação revisada**, seguindo o **padrão ABNT** de formatação, citações e referências bibliográficas, além das boas práticas e recomendações acadêmicas do Brasil.

> **A confirmar:** o autor escreveu "ABTN2". Interpretei como **abnTeX2**, o conjunto de classes e estilos LaTeX que implementa as normas da ABNT (classe `abntex2`, estilos de citação `abntex2cite`). Se a intenção foi só "padrão ABNT", sem LaTeX, a ferramenta de redação muda (ver "Ferramenta de redação"). As normas em si são as mesmas.

### Normas de referência

| Norma ABNT | Assunto |
|---|---|
| NBR 14724 | Trabalhos acadêmicos: apresentação (estrutura, formatação) |
| NBR 10520 | Citações em documentos |
| NBR 6023 | Referências |
| NBR 6024 | Numeração progressiva das seções |
| NBR 6027 | Sumário |
| NBR 6028 | Resumo |

`[A CONFIRMAR]` A **edição vigente** de cada norma e o **manual de normalização da FEI** (que pode acrescentar regras ou modelos institucionais). As normas da ABNT são documentos pagos e não estão no repositório; a conferência é do autor, na fonte. Nada aqui foi copiado das normas.

### O que a versão de 2010 já faz (observado no docx)

| Item | Observado |
|---|---|
| Página | A4 (21,0 × 29,7 cm) |
| Margens | superior 3,0 · inferior 2,0 · esquerda 3,0 · direita 2,0 cm |
| Fonte e espaçamento | Times New Roman 12, entrelinhas 1,5 |
| Citações | Autor-data, como `(SIAU e CAO, 2006)` |
| Elementos pré-textuais | Capa, folha de rosto, folha de aprovação (comissão julgadora), dedicatória, agradecimentos, epígrafe, resumo, *abstract*, lista de siglas, lista de tabelas, lista de ilustrações, sumário |
| Elementos pós-textuais | Referências |
| Não encontrados | Ficha catalográfica, apêndices, anexos, glossário `[A CONFIRMAR]` se são exigidos pela FEI |

Fonte: `acervo-2010/dissertacao/dissertacao-haddad-2010.docx` (inspeção em 21/09/2026).

## Liberdade de escopo (autor, 21/09/2026)

A revisão **não fica presa à estrutura e ao conteúdo de 2010**. Pode reorganizar capítulos, ampliar o que existe e criar conteúdo novo. A versão de 2010 é ponto de partida e objeto de auditoria (Fase 2), não molde.

O que continua valendo, porque é o método do projeto e não a estrutura de 2010:
- toda referência verificada na fonte primária; todo número vindo de execução reprodutível;
- `[FATO]` separado de `[HIPÓTESE]`;
- **toda expansão de escopo entra no registro de decisões do plano** (seção 10), com o motivo e a fase afetada. O risco R1 do plano é justamente a expansão sem controle.

## Estrutura

### Como era em 2010 (referência)

1. Introdução (motivações; objetivo e justificativa; contribuições; estrutura da dissertação)
2. Revisão bibliográfica (planejamento automático; competições; técnicas; modelagem de domínios; trabalhos relacionados)
3. Planejadores (selecionados; planejadores × técnicas)
4. Domínios (selecionados; características; domínios × características)
5. Características de domínios × técnicas de planejamento (método; relação; testes e validações)
6. Conclusões e trabalhos futuros

### Proposta inicial para a nova versão

O plano prevê oito capítulos. O mapa abaixo mostra de onde cada um poderia vir. É **ponto de partida, sujeito a mudança** (ver "Liberdade de escopo"): capítulos podem ser fundidos, divididos, acrescentados ou removidos conforme as Fases 1 a 5 mostrarem o que vale a pena.

| Nova versão | Origem em 2010 | Trabalho |
|---|---|---|
| 1. Introdução — a pergunta em 2010 e hoje | Cap. 1 | Reescrever ou substituir, com o percurso 2010 → 2026 |
| 2. Fundamentos e estado da arte | Cap. 2 | **Refazer** a partir da Fase 1 (seleção de algoritmos, portfólios, *features*, IPCs 2008–2023, aprendizado, LLMs) |
| 3. Revisitando 2010 — auditoria | Cap. 3, 4 e 5 (leitura crítica) | **Novo**: resultado da Fase 2 (mantém / reformula / descarta) |
| 4. Método | Cap. 5 (Método) | Reescrever: extração automática de métricas, replicação com mais planejadores e domínios |
| 5. Resultados experimentais | Cap. 5 (Relação, testes) | **Novo**: resultados da Fase 3 |
| 6. LLMs no mapa das técnicas | — | **Novo**: Fase 4 |
| 7. Do domínio de planejamento ao desenvolvimento de software dirigido por IA | — | **Novo**: Fase 5 |
| 8. Conclusões e próximos passos | Cap. 6 | Reescrever |

Na proposta, os capítulos de "Planejadores" e "Domínios" de 2010 (3 e 4) alimentam o Método (4) e os Resultados (5). Se a ampliação justificar (por exemplo, um capítulo próprio sobre a taxonomia atual de técnicas, ou sobre *features*), a estrutura muda.

### Elementos que a revisão precisa refazer ou acrescentar

- Capa, folha de rosto, folha de aprovação: dados novos (versão revisada; data; comissão, se houver). `[A CONFIRMAR]` como a FEI trata uma versão revisada de trabalho já defendido.
- Resumo e *abstract*, listas (siglas, tabelas, ilustrações) e sumário: regenerar.
- Referências: reconstruir a partir do `.bib` verificado (ver abaixo).
- **Declaração do uso de IA**: o plano exige registrar todo uso substantivo (seção 11). Como declarar isso no texto segue as regras da instituição e do programa `[A CONFIRMAR]`.

## Ferramenta de redação (a decidir antes da Fase 6)

| Opção | Como funciona | Observações |
|---|---|---|
| **A. abnTeX2 (LaTeX)** | Capítulos em `.tex`; referências em `.bib` (exportado do Zotero) com estilo `abntex2cite`; compila para PDF | Casa com a leitura "ABTN2 = abnTeX2". As referências verificadas em `literatura/referencias/*.bib` entram direto. Exige ambiente LaTeX. |
| **B. Word com modelo ABNT/FEI** | Capítulos em `.docx`; referências pelo Zotero + estilo ABNT | Igual ao formato de 2010. Menos reprodutível; o versionamento em Git é pior. |
| **C. Markdown → Pandoc → uma das duas** | Capítulos em `.md` (como o plano previa), convertidos | Mantém o texto legível no Git; é preciso validar a saída contra a norma. |

Regras para qualquer opção: cada número do texto vem de execução reprodutível; cada referência foi verificada na fonte; o texto final é na voz do autor.

## Pastas

| Pasta | Conteúdo |
|---|---|
| `capitulos/` | Um arquivo por capítulo (`01-introducao`, …), no formato que a ferramenta escolhida exigir |
| `orientador/` | Material dos marcos M1, M2 e M3 e registro do retorno |
