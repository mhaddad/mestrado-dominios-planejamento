# Relatório de auditoria da dissertação de 2010 (Fase 2)

Versão 1.0 · 23/09/2026 · Coordenador (Claude Code, claude-opus-5-5). Rascunho de trabalho para revisão do autor. Os números saem de `auditoria/scripts/resumir_auditoria.py` sobre `auditoria/afirmacoes.csv`, salvo indicação de outro script.

---

## 1. O que foi feito

1. **Extração.** 349 afirmações substantivas tiradas do texto de 2010 (`data/2010/extraido/texto.md`), cada uma com trecho literal conferido por script contra a linha de origem. Frases de navegação, agradecimentos e células de tabela ficaram de fora. O conteúdo das tabelas entra pelas frases que o interpretam e, no caso das Tabelas 2–4, 29–31, 35–37 e 41–43, pela conferência direta (seções 3 e 4).
2. **Conferência numérica.** 106 afirmações com números. As médias publicadas e a taxa de acerto do *ranking* foram recalculadas por script (`conferir_medias.py`, `conferir_rankings.py`).
3. **Fontes primárias.** Lidas as fontes dos 10 planejadores de 2010 e das duas obras citadas em "Trabalhos relacionados" (Hoffmann, 2001; Gerevini, Saetti e Serina, 2004). 11 notas novas, 11 entradas no `candidatas.bib`.
4. **Classificação.** Cada afirmação recebeu mantém / reformula / descarta, com confiança, justificativa e ação, segundo `auditoria/extracao/instrucoes-classificacao.md`, e coerência com os vereditos da Fase 1 (`auditoria/insumos-fase1.md`).
5. **Taxonomia.** Nova taxonomia de técnicas em quatro dimensões (`auditoria/taxonomia-tecnicas.md`).
6. **Plano de reexecução** para a Fase 3 (`auditoria/reexecucao.md`, 31 itens em cinco níveis).

A divisão do trabalho entre agentes e as correções feitas pelo Coordenador estão em `plan/fase2-estrategia-multiagentes.md`, seção 6.

## 2. Resultado geral

| Classe | Afirmações |
|---|---|
| mantém | 248 |
| reformula | 99 |
| descarta | 2 |
| **Total** | **349** |

Confiança: alta 181, média 107, baixa 61.

**Por capítulo**

| Capítulo | Afirmações | mantém | reformula | descarta |
|---|---|---|---|---|
| Resumo | 6 | 4 | 2 | 0 |
| 1 Introdução | 43 | 23 | 20 | 0 |
| 2 Revisão bibliográfica | 145 | 109 | 36 | 0 |
| 3 Planejadores | 20 | 18 | 1 | 1 |
| 4 Domínios | 31 | 25 | 6 | 0 |
| 5 Características × técnicas | 41 | 35 | 6 | 0 |
| 6 Testes e validações | 42 | 30 | 11 | 1 |
| 7 Conclusões e trabalhos futuros | 21 | 4 | 17 | 0 |

**Leitura.** A maior parte das afirmações é descrição fiel do que foi feito (métodos, domínios, história do campo) e se mantém. O que precisa mudar se concentra onde a dissertação **tira conclusões**: das 69 afirmações de resultado, 43 são "reformula"; nas Conclusões e trabalhos futuros, 17 de 21. Descrição de método ruim não foi classificada como erro de descrição: a fraqueza foi para a conclusão que se apoia nele (regra de desempate das instruções).

## 3. Vereditos por estrutura (além das frases)

A extração é por frase. Duas estruturas da dissertação precisam de veredito próprio, alinhado com a Fase 1:

| Estrutura | Veredito | Por quê |
|---|---|---|
| **Tabelas 2–4** (planejador × técnica) | **descarta; substituir** pela taxonomia em quatro dimensões | Mistura dimensões (direção de busca, espaço de busca, ordem do plano, heurística, fonte de conhecimento) e atribui a vários planejadores rótulos que a fonte primária não sustenta (`auditoria/taxonomia/fontes-planejadores.csv`, coluna `observacao`). Ex.: Fast Downward como *Hierarchical* (a hierarquia está só na heurística); YAHSP como *Knowledge-based*; SAT como *Forward-chaining* por convenção. |
| **Tabelas 18–25** (característica × técnica) | **reformula; recalcular** (Fase 3, R-06 e R-10) | Foram montadas com os rótulos das Tabelas 2–4. `[HIPÓTESE]` Parte das relações muda com a taxonomia corrigida; só o recálculo dirá quanto. |
| **Seção "Trabalhos relacionados"** | **descarta como revisão; reescrever e ampliar** (A8) | As duas obras citadas estão descritas corretamente, com um erro de escopo (AF-191), mas a seção ignora a seleção de algoritmos (Rice, 1976, e a linhagem posterior) e o próprio objetivo declarado pelo itSIMPLE em 2005 (`vaquero2005itsimple`). |
| **Validação do *ranking*** (Tabelas 30–31, 36–37, 42–43) | **reformula** | Ver achados G19 e G20 na seção 4. |

## 4. Achados novos da Fase 2

Detalhes e evidência em `auditoria/achados-fase0.md`.

- **G18 — médias publicadas com pequenos erros.** Das 64 linhas "MÉDIA" recalculadas, 9 foram truncadas em vez de arredondadas e 5 divergem além disso. O texto dá 6,17 para o Blackbox no Storage; a conta dá 6,07. A Tabela 30 não copia a Tabela 29 em 4 valores. `[FATO]` **Nenhuma divergência muda a ordem de nenhum *ranking*.**
- **G19 — a taxa de acerto é coincidência exata de posição.** Os 50% do Storage e do Elevator se reproduzem assim (5 de 10), e o autor confirmou a regra. No Zeno-travel, que o texto não informa, dá 40%. Em Zeno-travel e Elevator, 6 e 5 planejadores empatam na nota máxima, então a posição dentro do empate é arbitrária e a medida depende do desempate.
- **G20 — o *ranking* previsto quase não muda entre domínios.** Correlação de postos entre os três *rankings* previstos: 0,94 a 0,99. Uma linha de base **sem características de domínio** (nota média de cada planejador nos 10 domínios de treino) acerta os mesmos cinco primeiros em Storage e Zeno-travel e 4 de 5 no Elevator. `[HIPÓTESE]` Boa parte da previsão reflete a qualidade geral dos planejadores; com 10 planejadores e 3 domínios, a vantagem do método sobre a linha de base (correlação 0,81 × 0,75; 0,86 × 0,68; 0,65 × 0,65) não permite concluir que as características do domínio melhoram a escolha.
- **Trabalhos relacionados.** Hoffmann (2001) analisa a heurística teórica h+ e testa empiricamente só a do FF; o HSP aparece como trabalho futuro. 2010 diz que a análise foi feita "para as heurísticas utilizadas nos planejadores FF e HSP" (AF-191, reformula). Gerevini, Saetti e Serina (2004) estão descritos corretamente.
- **Competição de 1998.** A organização da IPC 1998 evitou declarar um vencedor geral; só a trilha ADL teve vencedor (IPP). 2010 chama IPP e Blackbox de "vencedores" (AF-018, AF-089, reformula).
- **Elevator.** O domínio usado é a variante simples do Miconic, mas o texto descreve restrições da variante completa (AF-315, reformula).

## 5. As duas afirmações descartadas

| ID | Afirmação | Por quê |
|---|---|---|
| AF-214 | Planejadores SAT são tratados como *forward-chaining* "porque partem do estado inicial" | Convenção própria, contrariada pelas fontes de Blackbox, SATPlan e MAXPLAN: quem busca é o resolvedor SAT sobre uma codificação de horizonte fixo. É a base textual do erro das Tabelas 2–4. |
| AF-328 | O R é o único planejador que usa *backward-chaining* | A fonte descreve o R como STRIPS recursivo, dirigido por metas, com o estado avançado ao aplicar cada ação; não há *backward-chaining* como técnica separada. |

Nenhuma das duas é uma conclusão central da dissertação; ambas sustentam a taxonomia que a Fase 1 já tinha marcado como "descarta" (A6), com a concordância do autor.

## 6. Conclusões centrais de 2010 (A1–A8)

| Rótulo | Veredito (Fase 1, confirmado na Fase 2) | O que a Fase 2 acrescentou |
|---|---|---|
| A1 — existe relação entre características e técnicas | mantém, com reformulação | G20 mostra que os dados de 2010 não separam o efeito das características do efeito da qualidade geral dos planejadores. |
| A2 — técnicas promissoras | reformula | A lista usa rótulos que a nova taxonomia desfaz (*Knowledge-based*, *Plan-Space*, *Total-order*). |
| A3 — escolher planejador só pelo domínio | reformula | G19 e G20 enfraquecem a evidência de validação: 50% é coincidência de posição e a linha de base sem características faz quase o mesmo. |
| A4 — mais dados melhoram o *ranking* | mantém, com ressalva | — |
| A5 — UML mede a complexidade que afeta o desempenho | reformula | AF-005 reclassificada pelo Coordenador para coerência com A5. |
| A6 — taxonomia de técnicas | descarta (Tabelas 2–4) | Fontes primárias dos 10 planejadores; nova taxonomia. |
| A7 — eficiência = cobertura | reformula | — |
| A8 — trabalhos relacionados | descarta (como revisão suficiente) | As duas obras citadas ficam e estão descritas quase corretamente (só o escopo de Hoffmann, 2001, está errado); o problema é o que falta, e a seção é reescrita. |

## 7. O que ainda depende de verificação

- **61 afirmações com confiança baixa**, a maioria com ação "CONFERIR" (49 ações pedem conferência na fonte): percentuais das competições de 1998 a 2006 ("40% melhor", "150% melhor"), detalhes históricos e descrições de domínios apoiadas só em plausibilidade. Não mudam as conclusões centrais; precisam de fonte antes de ir para o texto revisado.
- **11 fontes novas não são citáveis** até o autor aprová-las no `referencias.bib` (9 planejadores — o Fast Downward já estava — e os 2 trabalhos relacionados; ver `literatura/referencias/revisao-referencias.md`).
- **G10** (segundo bloco de características do SQL) segue em aberto.
- **Conferência humana.** As classificações são de agentes, revisadas por amostragem e por regra pelo Coordenador (21 linhas em `auditoria/extracao/classificacao-Z-coordenador.csv`: 19 revisões do Coordenador e 2 confirmações do autor). Não houve dupla classificação independente para medir concordância. As 101 afirmações "reformula" e "descarta" são as que o autor deve ler primeiro.

## 8. Limites desta auditoria

- A extração é por frase. Uma afirmação repetida em dois lugares aparece duas vezes (marcado na coluna `acao` quando o auditor notou).
- A classificação depende das fontes que o projeto já tem. Onde não havia fonte, a regra foi baixar a confiança, não inventar apoio.
- Os números de G18 a G20 vêm das tabelas publicadas, não de nova execução. A reexecução é da Fase 3.
