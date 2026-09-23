# Fase 2 — Estratégia de execução multiagente

Versão 1.0 · 23/09/2026 · Coordenador (Claude Code, claude-opus-5-5). Mesma abordagem da Fase 1, por decisão do autor, com modelos mais econômicos nas tarefas simples.

Complementa a seção "Fase 2" do [plano](plano-revisao-dissertacao.md).

---

## 1. Papéis e modelos

| Papel | Modelo | Faz |
|---|---|---|
| **Coordenador** | Opus 5.5 (sessão principal) | Desenho, divisão do trabalho, verificação e validação de tudo, decisões conforme o propósito do trabalho, perguntas ao autor quando a decisão ou a verificação for dele, consolidação, documentação e commits |
| **Extrator** | **Haiku 4.5** | Tarefa mecânica e bem delimitada: listar, com trecho literal e número de linha, as afirmações substantivas de um trecho da dissertação |
| **Conferente numérico** | **Haiku 4.5** | Comparar números citados no texto com as tabelas extraídas (`data/2010/extraido/tabela_NN.csv`) |
| **Auditor** | Sonnet 5 | Classificar afirmações em mantém / reformula / descarta, com justificativa baseada na literatura (Fase 1), nos dados de 2010 e nos achados da Fase 0 |
| **Pesquisador de fontes** | Sonnet 5 | Localizar e verificar as fontes primárias dos 10 planejadores de 2010, para a nova taxonomia |
| **Redator** | Sonnet 5 | Rascunho da taxonomia e do material do Marco M1 |

Regra de escolha: Haiku quando a tarefa tem critério objetivo e saída conferível linha a linha; Sonnet quando exige julgamento ou leitura de fontes; o Coordenador decide e confere.

## 2. Ondas

| Onda | Quem | Saída | Controle do Coordenador |
|---|---|---|---|
| 1. Extração | 4 extratores Haiku, um por bloco do texto | `auditoria/extracao/bloco-N.csv` | Cobertura por seção, deduplicação, conferência de trechos literais contra o texto |
| 1b. Fontes dos planejadores (em paralelo) | 1 pesquisador Sonnet | notas em `literatura/notas-de-leitura/`, entradas no `candidatas.bib` | Mesma verificação da Fase 1; promoção ao `referencias.bib` só com aprovação do autor |
| 2. Conferência numérica | Haiku | coluna de conferência nas afirmações numéricas | Amostra reconferida |
| 3. Classificação | Auditores Sonnet, por tema | `auditoria/afirmacoes.csv` preenchido | Revisão de todos os "descarta" e das afirmações centrais; coerência com `auditoria/insumos-fase1.md` |
| 4. Taxonomia | Redator Sonnet | `auditoria/taxonomia-tecnicas.md` | Validação contra as fontes; decisão final do Coordenador, com ponto de verificação do autor |
| 5. Reexecução, F6 e M1 | Coordenador + redator | `reexecucao.md`, `condicoes-de-execucao-2010.md` completado, `m1-orientador.md` | Revisão final |

## 3. Numeração

As afirmações extraídas recebem IDs `AF-NNN`. A coluna `rotulo_fase1` liga cada uma aos rótulos usados na Fase 1 (A1–A8, T1–T6; ver `literatura/protocolo/instrucoes-leitura.md`). A tabela semente do plano (A1–A4) usa outra numeração e passa a apontar para o CSV.

## 4. Quando o Coordenador pergunta ao autor

- Fatos que só o autor sabe sobre 2010 (por que um critério foi escolhido, o que significam dados sem documentação — ex.: achados G7, G10, G14).
- Classificações "descarta" de afirmações centrais da dissertação.
- A nova taxonomia, antes de fechá-la.
- Promoção de novas referências ao `referencias.bib`.

As perguntas são agrupadas, para não interromper o trabalho a cada item.

## 5. Salvaguardas

As mesmas da Fase 1: nenhuma referência de memória; nenhum número sem fonte; `[FATO]` e `[HIPÓTESE]`; `acervo-2010/` somente leitura; subagentes não escrevem em `plan/`, `MEMORY.md` nem no `referencias.bib`; só o Coordenador faz commit.

## 6. Registro de execução

- **Onda 1 (23/09/2026).** Os extratores Haiku não copiaram os trechos literalmente: cortaram citações entre parênteses no meio das frases e, ao corrigir, reduziram alguns trechos a fragmentos. O bloco 1 parou antes das seções Técnicas, Modelagem e Trabalhos relacionados. **Correção:** conferência automática de substring exata (`auditoria/scripts/consolidar_extracao.py`), devolução aos extratores, bloco 3 (capítulo central) refeito com Sonnet, linhas 355–492 extraídas por Sonnet (`bloco-1b.csv`), fragmentos estendidos até a frase inteira por script do Coordenador, e 5 afirmações de lacunas de cobertura registradas pelo Coordenador (`bloco-5.csv`). **Regra adotada:** tarefa de cópia literal por Haiku só é aceita depois da conferência automática e de uma checagem de fragmentos curtos. Resultado: 349 afirmações.
