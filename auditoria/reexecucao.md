> **Rascunho de IA para revisão do autor.** Produzido por Claude Code (subagente redator, claude-sonnet-5) em 23/09/2026, a partir de `auditoria/afirmacoes.csv` (colunas `acao` marcadas `FASE3:` e afirmações `reformula`/`descarta` cuja correção depende de experimento), `auditoria/achados-fase0.md` (G1–G20), `auditoria/condicoes-de-execucao-2010.md`, `auditoria/insumos-fase1.md`, `auditoria/taxonomia-tecnicas.md` e `plan/plano-revisao-dissertacao.md` (seções "Fase 3" e 10). Fecha o critério de conclusão da Fase 2 ("plano de reexecução definido"). Nenhum número aqui é novo: todos vêm dos arquivos citados. Pendente de confirmação do autor.

# Plano de reexecução (Fase 3)

## 1. Objetivo e princípio

Definir o que precisa ser recalculado ou reexecutado na Fase 3 para responder Q1 e Q2 (plano, seção 5) e para corrigir ou testar cada afirmação de 2010 marcada `reformula`/`descarta` cuja justificativa depende de um experimento, não só de checar uma fonte primária.

**Princípio:** primeiro reproduzir 2010 exatamente (Nível 1), depois corrigir sobre os mesmos dados (Nível 2), depois reexecutar os planejadores sob condições padronizadas (Nível 3), depois ampliar (Nível 4). Cada nível é separado dos demais para que se saiba, célula a célula, o efeito de cada mudança — se um número mudar do Nível 1 para o Nível 2, a causa é a correção aplicada, não uma reexecução misturada a uma correção.

Este documento não substitui `auditoria/taxonomia-tecnicas.md` (que já traz a reclassificação dos 10 planejadores nas quatro dimensões) nem repete os achados de `auditoria/achados-fase0.md`: aqui eles viram itens de trabalho, agrupados por nível e ligados às afirmações que corrigem.

## 2. Nível 0 — o que a Fase 2 já reproduziu

Sem executar nenhum planejador, só recalculando sobre as tabelas publicadas em `data/2010/`. Já concluído; listado aqui como base de comparação para os níveis seguintes.

- Recontagem de todas as linhas "MÉDIA" das tabelas extraídas (`auditoria/scripts/conferir_medias.py` → `auditoria/extracao/conferencia-medias.csv`, `conferencia-transcricao-ranking.csv`). Achado: G18 — 9 de 64 médias truncadas em vez de arredondadas, 5 divergem além disso; nenhuma divergência muda a ordem dos rankings.
- Reprodução da "taxa de acerto" do ranking previsto × observado nos três domínios de validação, como coincidência exata de posição (`auditoria/scripts/conferir_rankings.py` → `auditoria/extracao/conferencia-rankings.csv`). Achado: G19 — os 50% de Storage e Elevator se reproduzem; Zeno-travel dá 40% (não informado no texto); a medida depende do desempate onde há nota máxima empatada.
- Cálculo de uma linha de base sem características de domínio (nota média de cada planejador nos 10 domínios de treino), pelo mesmo script. Achado: G20 — a correlação de postos da linha de base com o observado é próxima da do método de 2010 (0,75×0,81 em Storage; 0,68×0,86 em Zeno; 0,65×0,65 em Elevator); o ranking previsto quase não varia entre os três domínios de validação (correlação de postos 0,94–0,99 entre eles).
- Conferência numérica de todas as 349 afirmações extraídas contra `data/2010/extraido/texto.md` e os datasets (`auditoria/scripts/consolidar_extracao.py` → `auditoria/afirmacoes.csv`, coluna `conferencia_numerica`).

## 3. Nível 1 — Reprodução fiel de 2010

Recalcular exatamente o método descrito em 2010 sobre os mesmos dados (`data/2010/`), por script, sem nenhuma correção. Serve de referência para medir o efeito de cada correção do Nível 2.

| Item | O que fazer | Entrada | Em aberto |
|---|---|---|---|
| Discretização por variância | Reproduzir por script o cálculo de variância entre os valores de cada característica e a classificação em Alto/Médio/Baixo pelos limiares publicados (até 3 pontos = não relevante; 4–5 = pouco relevante; acima de 6 = muito relevante) | `data/2010/metricas_dominios.csv`; limiares das Tabelas 21–23 | F7 — método com poucos pontos (13 domínios); G10 — segundo bloco de 20 características no `script.sql`, sem definição publicada |
| Tabelas 18–25 | Recalcular por script as tabelas de características de domínio, discretização e cruzamento característica × técnica, hoje conferidas só nas médias (Nível 0) | `data/2010/metricas_dominios.csv`, `data/2010/planejadores_tecnicas.csv` | G1 (rótulo invertido da métrica "atores por caso de uso"), G11–G13 (contagens de associações/generalizações/agregação) |
| Rankings e taxa de acerto (definição original) | Recalcular as Tabelas 30, 36, 42 (ranking previsto × observado) e a taxa de acerto pela definição reproduzida no Nível 0 (coincidência exata de posição), formalizando-a em script versionado | `data/2010/eficiencia_planejadores.csv`, `data/2010/validacao_ranking.csv` | G19 — a definição não está no texto; ver seção 8 |
| Conversão eficiência → nota 0–10 | Reproduzir a regra que converte percentual de problemas resolvidos em nota 0–10, testando as duas hipóteses (a partir do valor arredondado ou do valor preciso do SQL) | `data/2010/conferencia/eficiencia_precisa_sql.csv` | G6 — ainda não se sabe qual das duas foi usada |
| Segundo bloco de características (G10) | Registrar as 20 características do segundo bloco do `script.sql` como não publicadas e não reproduzidas neste nível, até resposta do autor | `data/2010/conferencia/divergencias_bloco2_vs_bloco1.csv`, `caracteristicas_18_a_20.csv` | G10 — ver seção 8 |

## 4. Nível 2 — Correções sobre os mesmos dados

Ainda sem executar planejadores: aplica ao mesmo dataset de 2010 as correções já decididas ou já levantadas na Fase 2, e recalcula o que muda.

| Item | Correção | Fecha |
|---|---|---|
| Taxonomia em 4 dimensões | Recalcular o cruzamento característica × técnica (Tabelas 18–25) e os rankings usando a reclassificação de `auditoria/taxonomia-tecnicas.md` §3 (algoritmo/espaço de busca, heurística, representação, arquitetura) no lugar dos 11 rótulos de 2010 | AF-213, AF-214, AF-285, AF-286, AF-326, AF-328; A6, F4 |
| Rótulo G1 | Corrigir "Número de Casos de Uso por Atores" para "Número Médio de Atores por Caso de Uso" (a métrica é atores ÷ casos de uso) e repropagar a correção pelas tabelas e pela interpretação dos exemplos | AF-234, AF-281, AF-282, AF-331; G1 |
| Correções G17 | Aplicar Pathways/Associações 4→2 e TPP/Generalização 2→4 (contagens confirmadas nas figuras) e recalcular a discretização e as Tabelas 19–25; por monotonia, Pathways deve passar de Médio a Baixo em Associações | G17 (`data/2010/correcoes_2010.csv`) |
| Critério de "Agregação" e classes auxiliares | Documentar como regra explícita o critério de contagem de "Agregação" (G13, hoje não conferível pelo XML) e testar a robustez da contagem de classes com e sem classes auxiliares (*Utility*, *Global*) (G2) | AF-225, AF-283; F3 |
| Medida de "taxa de acerto" com empates | Definir e recalcular com medidas que tratem empates — correlação de postos (Spearman), acerto do melhor colocado, perda em relação ao *virtual best* — substituindo ou complementando a coincidência exata de posição | AF-299, AF-322, AF-334; G19 |
| Comparação com a linha de base | Estender a comparação do Nível 0 (G20) para relatar, ao lado de cada afirmação sobre o poder preditivo do método, o ganho sobre a linha de base sem características de domínio | AF-006, AF-300, AF-312, AF-329, AF-330; G20 |
| Robustez da discretização com mais pontos | Recalcular a discretização por variância incluindo mais domínios com PDDL já disponível no acervo (sem executar planejadores), para testar se os limiares (3, 4–5, acima de 6 pontos) se sustentam com mais de 13 valores | AF-250 (parte "testar a robustez"); F7, G10 |

## 5. Nível 3 — Reexecução dos planejadores

Envolve rodar planejadores. Objetivo central: eliminar a mistura de duas populações de dados (38 pares de competição pela Tabela 12/13 — na verdade 34, ver G21 —, condições de cada IPC; 62 pares de execução própria, hardware único e timeout de 20 min — G9) e produzir dados que faltam (tempo, qualidade, validação de planos).

| Item | O que reexecutar | Condições | Fecha |
|---|---|---|---|
| 62 pares de execução própria | Repetir os pares planejador × domínio de treino que em 2010 vieram de execução própria, registrando tempo por problema e o motivo de cada não-resolução | Mesmo hardware, mesmo limite de tempo e memória para todos (desenho da Fase 3); timeout de 2010 foi 20 min (`condicoes-de-execucao-2010.md`) | AF-264, AF-324; F5, F6 |
| 38 pares de competição | Reexecutar (ou obter os artefatos oficiais) sob as mesmas condições padronizadas dos 62 pares acima, em vez de herdar as condições de cada edição da IPC | Idem | G9, G16 |
| Conjunto de instâncias | Fixar um único critério — replicar o subconjunto usado em 2010 (35/102 Blocks World, 28/84 Logistics, 20/36 Satellite) ou usar o conjunto completo da IPC — e aplicá-lo às 100 células com o mesmo denominador | Decisão do autor (seção 8) | G14, G15, G16 |
| Validação de planos | Validar todo plano gerado com um validador formal (ex.: VAL) e registrar separadamente timeout, falta de memória, erro do planejador e plano inválido como causas de "não resolvido" | Requer decisão sobre limite de memória (item seguinte) | `condicoes-de-execucao-2010.md`, "O que falta" |
| Limite de memória | Definir e aplicar um limite de memória por processo (não documentado em 2010) e registrar explicitamente | 4 GB de RAM na máquina original; sem `ulimit` registrado | `condicoes-de-execucao-2010.md`, "O que falta" |
| Qualidade do plano | Medir custo/comprimento do plano, não só cobertura, no Zeno-travel (onde 2010 afirma dificuldade de "plano de boa qualidade" sem nunca medir qualidade) e nos demais domínios de validação | Planos gerados nos itens acima | AF-303; F5, A7 |
| Mais planejadores comparáveis ao R | Incluir mais planejadores forward-chaining/recursivos (STRIPS clássico) comparáveis ao System R, para testar se a distorção do ranking do Elevator (Tabela 42) é efeito de amostra pequena (F2) ou um padrão que se sustenta com mais planejadores da mesma família | AF-327; F2 |

## 6. Nível 4 — Ampliação (Q1, Q2)

O desenho já aprovado da Fase 3 (plano, seção "Fase 3"), ligado a cada afirmação que testa.

| Item | Desenho | Responde | Fecha |
|---|---|---|---|
| Escopo e condições | *Benchmarks* das IPCs 1998–2023 (clássico, determinístico); mesmo hardware, mesmo limite de tempo e memória para todos os planejadores; medidas de cobertura, tempo, qualidade do plano e escore IPC | Base de Q1 | Substitui as condições heterogêneas de 2010 (F2, F6) |
| Extrator automático das métricas de 2010 | Implementar a extração automática das métricas UML-like a partir do PDDL (hierarquia de tipos → classes e DIT; ações → casos de uso; predicados → associações e atributos) e validar contra as contagens manuais de 2010 | Q2 (*features* (a)) | F3; G2, G11, G12, G13 |
| Extrator de *features* modernas | Implementar ou reutilizar um extrator de *features* automáticas de PDDL/SAS+ (grafo causal, DTG, *treewidth*) | Q2 (*features* (b)) | A5 — determinantes de complexidade com efeito demonstrado na literatura [@helmert2009concise; @hoffmann2011analyzing; @domshlak2013complexity] |
| Métricas UML × *features* de PDDL | Testar as métricas UML.P contra as *features* automáticas de PDDL nos mesmos domínios, controlando a ordem de serialização do modelo (decisão do autor de 23/09/2026); resultado negativo também é resultado | Q2 diretamente | AF-310, AF-337; A5 |
| Combinação de *features* e modelos | Combinar (a)+(b) em (c); treinar *random forest* e *gradient boosting*, com a média por rankings de 2010 como linha de base; validar por *leave-one-domain-out*; comparar com *single best* e *virtual best* | Q1 | Continuação de G20 em escala ampliada |
| Dois níveis de análise | Reportar separadamente a análise por domínio (continuidade com 2010) e por instância (estado da arte em seleção de algoritmos), sem misturar as duas unidades preditivas | Q1, A1, A3 | AF-329, AF-335; decisão do autor de 23/09/2026 — a seleção por instância supera a seleção fixa por domínio quando não há treino no domínio, mas a seleção por domínio continua competitiva com treino no próprio domínio [@cenamor2016ibacop; @nunez2015automatic] |
| Discretização vs. regressão | Comparar a discretização Alto/Médio/Baixo por variância (Nível 1–2) com regressão sobre *features* contínuas, prática hoje mais comum na literatura de seleção de algoritmos [@fawcett2014improved] | Q1, T6 | AF-346; F7 |
| Aprendizado de máquina como família | Incluir aprendizado de máquina (heurísticas aprendidas, seleção por classificador) na reclassificação de técnicas promissoras e, se viável no ambiente montado, incluir ao menos um planejador dessa família na reexecução — em Storage (um dos três domínios de validação de 2010), uma heurística aprendida supera LAMA e h_FF [@ferber2022neural; @toyer2020asnets] | Q1, A2 | AF-332, AF-333 |

## 7. Tabela-resumo

| ID | Nível | O que testa | Entrada necessária | Saída esperada | Depende de | Prioridade |
|---|---|---|---|---|---|---|
| R-01 | 0 | G18 | `data/2010/extraido/` | `conferencia-medias.csv` (concluído) | — | — |
| R-02 | 0 | G19 | `data/2010/validacao_ranking.csv` | `conferencia-rankings.csv` (concluído) | — | — |
| R-03 | 0 | G20 | `data/2010/eficiencia_planejadores.csv` | linha de base × 2010 (concluído) | — | — |
| R-04 | 0 | Conferência numérica de AF-001–AF-349 | `data/2010/extraido/texto.md` | `afirmacoes.csv` (concluído) | — | — |
| R-05 | 1 | F7, G10 | `data/2010/metricas_dominios.csv` | script de discretização por variância | R-04 | alta · 🟢 feito (EXP-03): regra por extremos, 220 de 221; ver G23 |
| R-06 | 1 | G1, G11–G13 | `data/2010/metricas_dominios.csv`, `planejadores_tecnicas.csv` | Tabelas 18–25 recalculadas por script | R-05 | alta · 🟢 feito (EXP-03): Tabelas 19–25 e validação reproduzidas; ver G24 |
| R-07 | 1 | G19 | `data/2010/eficiencia_planejadores.csv` | rankings e taxa de acerto (definição original) por script | R-02 | média · 🟢 feito (EXP-03 e Nível 0): rankings reproduzidos (diferenças só dentro de empates) |
| R-08 | 1 | G6 | `data/2010/conferencia/eficiencia_precisa_sql.csv` | regra de conversão eficiência → nota testada | — | média · 🟢 feito (EXP-03): 100 de 100; G6 resolvido |
| R-09 | 1 | G10 | `data/2010/conferencia/caracteristicas_18_a_20.csv` | registro do que ficou em aberto | decisão do autor (seção 8) | baixa |
| R-10 | 2 | A6, F4; AF-213, AF-214, AF-285, AF-286, AF-326, AF-328 | `auditoria/taxonomia-tecnicas.md` §3 | Tabelas 18–25 e rankings com taxonomia de 4 dimensões | R-06 | alta · 🟢 feito (EXP-06): sem ganho claro sobre a linha de base; codificação C1–C5 aprovada pelo autor em 26/09/2026 |
| R-11 | 2 | G1; AF-234, AF-281, AF-282, AF-331 | `data/2010/metricas_dominios.csv` | rótulo e interpretação corrigidos | R-06 | média · 🟢 feito (EXP-08): `data/2010/rotulos_corrigidos.csv`; leitura do exemplo da AF-234 invertida |
| R-12 | 2 | G17 | `data/2010/correcoes_2010.csv` | discretização e Tabelas 19–25 com as correções aplicadas | R-05 | média · 🟢 feito (EXP-08): 6 classes mudam, nenhum ranking muda |
| R-13 | 2 | F3; G2, G13; AF-225, AF-283 | `data/2010/conferencia/modelos_itsimple.csv` | critério de Agregação documentado; teste de robustez de classes | R-06 | média · 🟡 EXP-08: robustez de classes feita (nenhum ranking muda); critério da Agregação não reconstruível dos XML, depende de confirmação do autor |
| R-14 | 2 | G19; AF-299, AF-322, AF-334 | `data/2010/validacao_ranking.csv` | medidas de acerto com tratamento de empate | R-07; decisão do autor (seção 8) | alta |
| R-15 | 2 | G20; AF-006, AF-300, AF-312, AF-329, AF-330 | `auditoria/extracao/conferencia-rankings.csv` | comparação sistemática com a linha de base | R-03 | média · 🟢 feito (EXP-08): linha de base em todo resultado do `nivel2.py` |
| R-16 | 2 | F7, G10; AF-250 | PDDL de domínios adicionais no acervo | discretização testada com mais pontos | R-05 | baixa |
| R-17 | 3 | F5, F6; AF-264, AF-324 | planejadores e domínios de 2010 | tempo e cobertura por par, condição padronizada | R-06 | alta |
| R-18 | 3 | G9, G16 | resultados oficiais das IPCs ou reexecução | 100 células sob condição única | R-17 | alta |
| R-19 | 3 | G14, G15, G16 | `data/2010/benchmarks_ipc_instancias.csv` | conjunto de instâncias fixado | decisão do autor (seção 8) | alta |
| R-20 | 3 | `condicoes-de-execucao-2010.md` | planos gerados nos itens acima | planos validados (VAL); causas de falha discriminadas | R-17 | média |
| R-21 | 3 | `condicoes-de-execucao-2010.md` | ambiente de execução (Fase 3) | limite de memória definido e registrado | — | média |
| R-22 | 3 | F5, A7; AF-303 | planos gerados no Zeno-travel e demais domínios | medida de qualidade do plano | R-17, R-20 | média |
| R-23 | 3 | F2; AF-327 | planejadores forward-chaining/recursivos adicionais | ranking do Elevator com mais planejadores da família do R | R-17 | baixa |
| R-24 | 4 | Q1 | *benchmarks* IPC 1998–2023 | ambiente e condições padronizadas montados | R-18, R-19, R-21 | alta |
| R-25 | 4 | F3; Q2 (*features* a); G2, G11–G13 | PDDL de todos os domínios | extrator automático validado contra 2010 | R-13 | alta · 🟢 feito (EXP-07): 11 de 17 métricas extraíveis; 8 se reproduzem, 3 dependem da modelagem; o R-13 segue pendente |
| R-26 | 4 | Q2 (*features* b) | PDDL/SAS+ | *features* modernas extraídas (grafo causal, DTG, *treewidth*) | — | média |
| R-27 | 4 | Q2; A5; AF-310, AF-337 | R-25, R-26 | comparação UML × *features* de PDDL, com controle de serialização | R-25, R-26 | alta |
| R-28 | 4 | Q1 | R-24, R-25, R-26 | modelos treinados; comparação com *single best*/*virtual best* | R-24, R-25, R-26 | alta |
| R-29 | 4 | Q1, A1, A3; AF-329, AF-335 | R-28 | relatório por domínio e por instância, separados | R-28 | média |
| R-30 | 4 | Q1, T6; AF-346 | R-25, R-26 | discretização comparada com regressão | R-25, R-26 | baixa |
| R-31 | 4 | Q1, A2; AF-332, AF-333 | ambiente da Fase 3 | ao menos um planejador com heurística aprendida incluído, se viável | R-24 | baixa |

## 8. Perguntas ao autor

Respostas de 23/09/2026 e o que ainda está em aberto.

| Item | Pergunta | Situação |
|---|---|---|
| **G7** | Por que a média das médias, e não as variantes do `testes.ods`? | **Respondido:** as variantes foram testadas; ficou a média das médias por simplicidade. A Fase 3 compara as variantes explicitamente (Nível 2), sem reabrir a escolha de 2010 no Nível 1. |
| **G19** | Como foi calculada a taxa de acerto? | **Respondido:** coincidência exata de posição (confirma a reprodução do Nível 0). **Em aberto para a Fase 3:** qual medida vira referência. Recomendação do Coordenador: reportar todas (posição exata, para comparar com 2010; correlação de postos; acerto do melhor; perda em relação ao *virtual best*), com a perda como principal. |
| **G14** | Qual o critério de corte das instâncias? | **Respondido:** igualar o subconjunto dos resultados publicados da IPC. **Em aberto para a Fase 3:** recomendação do Coordenador — Níveis 1 a 3 usam o subconjunto de 2010 (fidelidade); Nível 4 usa os conjuntos completos. |
| **G10** | O que eram as 20 características do segundo bloco do `script.sql`? | **Em aberto.** Sem resposta, o Nível 1 registra o bloco como não reproduzido. |
| **G15/G16** | Manter o Gripper gerado localmente ou usar o conjunto oficial da IPC 1998? Sobre qual conjunto recalcular as 100 células? | **Em aberto para a Fase 3.** A resposta sobre G14 enfraquece G16. Recomendação do Coordenador: mesma regra de G14 (Gripper de 2010 nos Níveis 1 a 3; oficial no Nível 4). |
| **G21** | De onde vieram os 4 valores de "competição" de R e Fast Downward no Depots e no DriverLog? | **Resolvido pelo acervo (23/09/2026):** vieram dos logs de execução própria de 2010 (`auditoria/scripts/conferir_origem_competicao.py`). Na Fase 3, esses 4 pares entram no grupo de execução própria (66 pares, não 62). |
