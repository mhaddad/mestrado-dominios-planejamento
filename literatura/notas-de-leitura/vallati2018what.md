---
tipo: nota-de-leitura
eixo: E1
citekey: vallati2018what
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: PDF do artigo fornecido pelo autor em 27/09/2026 (36 p.)
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [F1]
fragilidades: [F1, F2]
perguntas: [Q1, Q5]
---

# What you always wanted to know about the deterministic part of the International Planning Competition (IPC) 2014 (but were too afraid to ask)

**Vallati, M.; Chrpa, L.; McCluskey, T. L. · 2018 · The Knowledge Engineering Review, v. 33, e3, p. 1–36**
**Link/DOI:** 10.1017/S0269888918000012

## Extração estruturada

- **Problema:** relatório dos organizadores sobre a parte determinística da IPC 2014: regras, trilhas, pontuação, seleção de *benchmarks*, resultados, complementaridade dos planejadores e progresso em relação à IPC 2011.
- **Método:** descrição da competição e análise dos resultados com placar da IPC, contagem de Borda, teste binomial (cobertura) e teste de Wilcoxon (qualidade e tempo), com correção de Bonferroni; portfólios-oráculo (*virtual best solver*) de 2 a 4 planejadores; reexecução de vencedores de 2011 (LAMA-11, FDSS-1, ArvandHerd, YAHSP2) e de FF e LPG nos *benchmarks* de 2014, no mesmo *hardware*.
- **Dados / benchmarks:** 67 planejadores submetidos, 23 modelos de domínio (14 de IPCs anteriores, 9 novos), 20 problemas por domínio. Trilhas e limites: *satisficing* e ótima (30 min, 4 GB), *agile* (5 min, 4 GB), *multi-core* (4 núcleos, 30 min de relógio, 4 GB), temporal *satisficing* (30 min). Temporal ótima e preferências foram canceladas. O modelo da CPU do *cluster* não é informado.
- **Resultado principal:** vencedores IBaCoP2 (*satisficing*, portfólio), SymBA*-2 (ótima, busca simbólica bidirecional), YAHSP3 (*agile*), ArvandHerd (*multi-core*) e YAHSP3-MT (temporal). 29 dos 67 sistemas são portfólios e 29 são construídos sobre o Fast Downward. A complementaridade é alta nas trilhas *satisficing* e *agile* e baixa na ótima: o melhor par de planejadores resolve 88,9% na *satisficing*, contra 70,7% do melhor individual, e 60,0% na ótima, contra 53,9% (Tabela 8). Há progresso desde 2011 nas trilhas *satisficing* e ótima, e não nas trilhas temporal e *multi-core*.
- **Relação com a dissertação de 2010:** a conclusão (p. 34) afirma que não havia, até então, propriedades de domínio independentes de planejador que fossem aceitas para classificar modelos estaticamente. É a lacuna que a dissertação de 2010 tentou ocupar com métricas UML e que a Q5 retoma com *features* de PDDL.

## O que o artigo traz de dados (Fase 4B)

- **Totais por trilha, para todos os planejadores:** Tabelas 3 (*satisficing*, 20 linhas), 4 (*agile*, 15), 5 (*multi-core*, 9), 6 (ótima, 17) e 7 (temporal, 6), com placar, resolvidos, % e Borda.
- **Não há tabela por domínio e planejador.** Por domínio, só agregados: a Figura 2 mostra a fração de planejadores *satisficing* por faixa de cobertura, e as Figuras 3 e 4 mostram a fração de problemas resolvidos e de planejadores que resolveram tudo. O texto cita casos isolados, como os 60 dos 81,6 pontos do YAHSP3 obtidos em GED, Transport e Visitall (p. 18) e as 14 instâncias do Planets no Thoughtful (p. 16).
- **Domínios e recursos do PDDL por trilha:** Tabelas 1 e 2 (as 15 linhas da Tabela 1 incluem Tidybot, que só entrou na ótima, no lugar do Thoughtful).
- **Registro de "não suporta" × "não resolveu":** o Thoughtful tem um predicado e um tipo com o mesmo nome, o que afetou todos os planejadores que usam o *parser* do Fast Downward; os portfólios ainda resolveram instâncias com componentes de fora do Fast Downward (p. 9 e 16). O RIDA exigia efeitos condicionais declarados no Cavediving (p. 23). Os geradores produziram tarefas insolúveis na trilha ótima: 6 no Barman, 15 no Maintenance e 3 no Tetris (p. 23).
- O texto diz que os dados gerados foram publicados no site da competição (p. 2), que saiu do ar (ver `docs/resultados-ipc-2011-2023.md`).

## Pontos relevantes para o projeto

- **Seleção de instâncias condicionada aos participantes (p. 9–10):** as 20 instâncias de cada domínio foram escolhidas rodando os próprios competidores, com três critérios: no máximo 80% dos competidores resolvem tudo, no máximo 80% não resolvem nada, e a diferença entre o primeiro e o segundo é menor que 50%. Os autores reconhecem o viés. `[HIPÓTESE]` Na Fase 4B, a dificuldade por domínio nos dados da IPC 2014 é calibrada pela própria competição, o que atenua diferenças entre domínios e confunde efeitos de característica do domínio com o protocolo de seleção. Vale verificar se a IPC 2018 usou protocolo parecido.
- **Não há definição de portfólio (p. 33):** os organizadores não separaram portfólios de planejadores "básicos" por falta de uma definição clara, e dão o FF, com dois algoritmos de busca, como exemplo de caso ambíguo. É insumo direto para a regra dos portfólios da 4B.
- **Ordem do modelo PDDL (p. 34):** os autores citam `vallati2015effective` para dizer que a ordem dentro do arquivo de domínio afeta o desempenho. Isso reforça o achado da Fase 1 sobre serialização.
- **Limite de generalização (p. 14 e 31):** os resultados dependem do *hardware*, do *software*, dos *benchmarks* e da configuração dos modelos. Os autores lembram que planejadores aleatorizados podem ter distribuições de tempo diferentes a cada execução.
- **Progresso relativo (seção 6):** o LAMA-11 ficaria em 12º de 21 na *satisficing* de 2014; o FDSS-1, em 6º de 18 na ótima; na *agile*, o LPG ficaria em 13º e o FF em 17º de 17. Sem os domínios com efeitos condicionais, o LPG subiria para 9º.

## Inconsistências internas encontradas

- A Tabela 8 atribui ao IBaCoP2 placar individual de 153,3 na *satisficing*; a Tabela 3 dá 166,2. O valor de 153,3 é o do ArvandHerd na *multi-core* (Tabela 5). `[HIPÓTESE]` erro de transcrição na Tabela 8.
- O texto da p. 15 diz que o primeiro grupo de cobertura resolve "entre 192 e 168" instâncias (70,7–60,0%); a Tabela 3 dá 198 para o IBaCoP2, e 198/280 = 70,7%.
- As submissões citadas na seção 2.1.1 (21 na *satisficing*, 16 na *agile*) diferem das linhas das Tabelas 3 e 4 (20 e 15). O artigo não explica a diferença.

## Trechos literais

> "From a general point of view, the proposed protocol introduces a potentially strong bias towards the participating planners." (p. 10)

> "However, there is no clear definition of portfolios in planning (Vallati et al., 2015b) and therefore there are some ‘grey areas’ (e.g. whether FF that implements two different search algorithms is a portfolio)." (p. 33)

> "Leaving aside the inherent computational complexity of a problem, no generally accepted planner-independent properties or characteristics have been proposed that we are aware of in order to statically classify domain models." (p. 34)

> "Recently, it has been shown that even the ordering of features within a domain file can affect the performance of plan generation in current planners (Vallati et al., 2015c), and so comparisons of planners with one particular benchmark set can be called into question." (p. 34)

## Marcações

- `[FATO]` A IPC 2014 teve 67 planejadores submetidos, dos quais 29 eram portfólios e 29 usavam o Fast Downward (p. 31–32).
- `[FATO]` As instâncias foram selecionadas pelo desempenho dos próprios competidores (p. 9–10).
- `[FATO]` O artigo publica totais por trilha para todos os planejadores, mas não resultados por domínio e planejador.
- `[HIPÓTESE]` A afirmação da p. 34 é a melhor formulação publicada da lacuna que a Q5 enfrenta; a literatura posterior a 2018 sobre *features* de PDDL (Fase 1, eixo E2) precisa ser confrontada com ela antes de usá-la no texto.

## Uso de IA nesta nota

22/09/2026: primeira versão por Claude Code (subagente claude-sonnet-5), só com o resumo. 27/09/2026: reescrita por Claude Code (claude-opus-5-5) a partir do texto integral fornecido pelo autor. Trechos literais copiados do PDF; números conferidos contra as tabelas do próprio artigo, incluindo as inconsistências registradas. Conferência humana: pendente.
