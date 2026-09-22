# Fase 1 — Estratégia de execução multiagente e multimodelo

Versão 1.0 · 22/09/2026 · proposta do Coordenador (Claude Code, claude-opus-5), **aprovada pelo autor em 22/09/2026** com estas escolhas:

- **Autonomia ponta a ponta:** o Coordenador aprova protocolo e triagem em nome do autor; tudo fica marcado "pendente de confirmação do autor".
- **Citações no rascunho:** chaves `[@chave]` do `candidatas.bib`; o rascunho fica "não citável" até todas as chaves estarem no `referencias.bib`.
- **Escala:** a proposta da seção 4.
- **Pandoc:** instalar e fazer o teste de conversão ABNT (ação 7 do plano) nesta execução.

Complementa a seção "Fase 1" do [plano](plano-revisao-dissertacao.md). O plano diz *o quê*; este documento diz *como* os agentes executam.

---

## 1. Papéis e modelos

| Papel | Modelo | Quem é | Faz | Não faz |
|---|---|---|---|---|
| **Coordenador** | Opus 5 | A sessão principal do Claude Code | Protocolo, divisão do trabalho, consolidação, controle de qualidade, decisões de triagem em nome do autor (marcadas como pendentes de confirmação), revisão das sínteses e do rascunho, relatório final, atualização de `MEMORY.md` e do plano, commits | Pesquisa em massa, leitura de artigos em lote, redação longa |
| **Buscador** (1 por eixo) | Sonnet 5 | Subagente `general-purpose` | Busca por eixo, lista bruta com a URL onde cada item foi encontrado | Triagem, escrever `.bib` |
| **Triador** | Sonnet 5 | Subagente `general-purpose` | Pré-classifica por título e resumo segundo os critérios do protocolo | Decisão final |
| **Verificador de metadados** | Sonnet 5 | Subagente `general-purpose`, **nunca o mesmo que buscou** | Confere cada item incluído no registro primário (Crossref, DBLP, arXiv, página da editora ou do evento) e gera o BibTeX a partir desse registro | Digitar referência de memória |
| **Leitor-extrator** | Sonnet 5 | Subagente `general-purpose`, lotes de 6 a 8 obras | Uma nota de leitura por obra, no modelo do projeto, com trechos literais que sustentam cada afirmação-chave | Opinião sem marcação `[HIPÓTESE]` |
| **Sintetizador** (1 por eixo) | Sonnet 5 | Subagente `general-purpose` | Síntese do eixo **só a partir das notas**, sem busca nova | Citar obra sem nota |
| **Redator** | Sonnet 5 | Subagente `general-purpose` | Rascunho do capítulo 2 a partir das sínteses e do roteiro aprovado pelo Coordenador | Texto final (é do autor) |
| **Crítico** | Sonnet 5 | Subagente `redacao-editorial:critico` com modelo Sonnet | Leitura adversarial das sínteses e do rascunho | Reescrever |

Por que assim: o trabalho de volume (buscar, ler, extrair, redigir) é paralelizável e vai para o Sonnet; o que exige julgamento e visão de conjunto (critérios, cortes, coerência entre eixos, detecção de exagero) fica com o Opus. O verificador é separado do buscador para que um erro de uma etapa não seja confirmado por quem o cometeu.

---

## 2. Fluxo em ondas

Cada onda termina com um **ponto de controle do Coordenador** e um commit. Ondas com vários agentes rodam em paralelo; cada agente escreve só nos seus arquivos, para não haver conflito.

| Onda | Quem | Paralelismo | Entrada | Saída | Controle do Coordenador |
|---|---|---|---|---|---|
| 0. Protocolo | Coordenador | — | Plano, seção 13, achados da Fase 0 | `literatura/protocolo/protocolo-busca.md` | Gate A (autor) ou autoaprovação, conforme o modo escolhido |
| 1. Busca | 8 buscadores | 8 em paralelo | Protocolo | `literatura/protocolo/busca/E{n}-bruta.csv` | Deduplicação entre eixos, cobertura das sementes da seção 13, reabertura de 10% das URLs |
| 2. Triagem | 4 triadores (2 eixos cada) | 4 em paralelo | Lista consolidada | `literatura/protocolo/triagem.csv` | Revisa **todos** os "talvez" e 15% dos demais; fecha a lista de inclusão |
| 3. Verificação | 4 verificadores | 4 em paralelo | Itens incluídos | `literatura/protocolo/verificacao-metadados.csv`, `literatura/referencias/candidatas.bib` | Reconfere 10%; resolve cada divergência |
| 4. Leitura | ~12–16 leitores | até 8 por vez | Itens verificados, prioridade A primeiro | `literatura/notas-de-leitura/<chave>.md` | Por lote, reconfere 1 nota contra a fonte (trecho citado existe e diz o que a nota afirma) |
| 5. Síntese | 8 sintetizadores + crítico | 8 em paralelo | Notas | `literatura/sinteses/E{n}-<tema>.md` | Coerência entre eixos, contradições, exageros, `[FATO]`/`[HIPÓTESE]` |
| 6. Rascunho | Redator + crítico | sequencial | Sínteses + roteiro | `redacao/capitulos/02-fundamentos.md` (rascunho de IA) | Roteiro antes, revisão depois; checagem automática de chaves |
| 7. Relatório | Coordenador | — | Tudo | `literatura/relatorio-fase1.md`, `MEMORY.md`, plano | — |

Estimativa: 45 a 55 execuções de subagentes. O custo é relevante; os tetos da seção 4 existem para contê-lo.

---

## 3. Salvaguardas (regras do projeto aplicadas aos agentes)

1. **Nenhuma referência de memória.** Toda linha da lista bruta tem a URL onde foi encontrada. Sementes da seção 13 que não forem localizadas ficam "não localizada", nunca são completadas por inferência.
2. **BibTeX só a partir do registro primário** (Crossref por DOI, DBLP, arXiv). Vai para `candidatas.bib`, **nunca para `referencias.bib`**, que continua sendo só a exportação do Zotero feita pelo autor.
3. **Três níveis de status**, visíveis em cada nota e na planilha: `localizada` → `verificada-por-agente` (metadados conferidos no registro primário) → `verificada` (entrou no Zotero e no `referencias.bib`). O campo `referencia-verificada` da nota só vira `true` no último nível.
4. **Profundidade de leitura declarada** em cada nota: `texto integral` ou `só resumo`. Afirmação tirada de resumo não sustenta argumento central no rascunho.
5. **Trecho literal com localização** (seção ou página) para cada afirmação-chave de uma nota, para permitir conferência rápida.
6. **Sínteses e rascunho só usam obras com nota.** Script de checagem compara as chaves citadas com `candidatas.bib` e `referencias.bib`.
7. **`acervo-2010/`, `plan/` e `MEMORY.md`**: subagentes não escrevem. Só o Coordenador atualiza plano, memória e commits (sem *push*).
8. **Registro de uso de IA**: uma linha por onda na seção 11 do plano, com modelo e o que foi conferido.
9. **Expansão de escopo** que aparecer na literatura (tema novo, eixo novo) vai para o relatório como proposta, não entra sozinha.

---

## 4. Tetos por eixo (proposta)

| Item | Teto |
|---|---|
| Lista bruta | até 60 por eixo |
| Incluídos após triagem | 12 a 20 por eixo (~120 no total) |
| Leitura de texto integral (prioridade A) | 8 a 10 por eixo |
| Demais incluídos | nota curta a partir do resumo |

Critérios de inclusão e exclusão, bases e *strings* ficam no protocolo (Onda 0).

---

## 5. Ligação com a Fase 2

Cada nota tem o campo "Relação com a dissertação de 2010". O Coordenador cruza essas relações com as fragilidades F1–F7 do plano e os achados G1–G17 de `auditoria/achados-fase0.md` e entrega, no relatório, uma tabela de **insumos para a auditoria**: que afirmação de 2010 a literatura confirma, corrige ou torna obsoleta (por exemplo, a taxonomia de técnicas da F4).

---

## 6. O que continua com o autor

- Confirmar a triagem (a planilha tem a coluna `confirmado_autor`).
- Importar as candidatas no Zotero (por DOI ou pelo `candidatas.bib`) e exportar o `referencias.bib`. `[A CONFIRMAR]` se o Better BibTeX preserva a chave importada; se não, o script de checagem converte as chaves do rascunho por DOI.
- Reescrever o capítulo na própria voz.
- Aprovar expansões de escopo.

---

## 7. Relatório final do Coordenador

`literatura/relatorio-fase1.md`, exibido também no terminal: o que foi feito por onda (números de itens em cada etapa), principais achados por eixo, contradições e lacunas da literatura, estado de cada referência, pendências do autor, insumos para a Fase 2 e propostas de expansão de escopo.
