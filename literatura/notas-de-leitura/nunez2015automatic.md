---
tipo: nota-de-leitura
eixo: E1
citekey: nunez2015automatic
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: PDF fornecido pelo autor em 23/09/2026 (Artificial Intelligence, v. 226, p. 75-101, 2015)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A3, A6, A7]
fragilidades: [F2, F4, F5]
perguntas: [Q1]
---

# Automatic construction of optimal static sequential portfolios for AI planning and beyond

**Núñez, S.; Borrajo, D.; Linares López, C. · 2015 · Artificial Intelligence, v. 226, p. 75-101**
**Link/DOI:** 10.1016/j.artint.2015.05.005

## Extração estruturada

- **Problema:** a construção de portfólios de planejadores é quase toda empírica; falta entender seus limites, saber quanto se pode ganhar combinando os planejadores disponíveis e quais instâncias de treino realmente importam.
- **Método:** GOP, formulação em programação inteira mista (MIP) que calcula o **portfólio sequencial estático ótimo** (OSS) para um conjunto de treino e de planejadores candidatos: quanto tempo dar a cada planejador para maximizar a qualidade (ou a cobertura) e, em seguida, minimizar o tempo total. Para planejamento ótimo, o problema é uma variação da mochila; para o satisficing, a utilidade depende do tempo. Também analisa a "utilidade" das instâncias de treino, agrupando-as pelo número de planejadores que as resolvem.
- **Dados / benchmarks:** trilhas ótima, satisficing e de aprendizado da IPC 2011 (14 domínios, 20 tarefas cada; 30 minutos e 6 GB por tarefa), com treino na IPC 2008; trilha aberta da SAT Competition 2013.
- **Resultado principal:**
  - Na trilha ótima da IPC 2011, o portfólio OSS resolve 200 das 280 tarefas (77 não foram resolvidas por nenhum planejador). O vencedor, FDSS-1, resolveu 185, isto é, 92,5% do limite; os segundos colocados, 169 (84,5%).
  - O mesmo portfólio ótimo pode ser obtido com só 27 tarefas de treino, em vez de todas: nem toda instância carrega a mesma informação.
  - Nos domínios novos da IPC 2011, o portfólio GOP-1 resolve 65 tarefas, o mesmo que o FDSS-1 e o FDSS-2, treinando com menos tarefas.
  - Na trilha satisficing, o LAMA-2011 atinge 94,3% da cobertura e 85,6% da qualidade do limite OSS.
  - O MIPlan, planejador baseado no GOP que monta um portfólio **por domínio**, venceu a trilha de aprendizado da IPC 2014. O MIPSat ficou com a medalha de prata na trilha aberta da SAT Competition 2013.
- **Relação com a dissertação de 2010:**
  - **A1 [confirma]:** a premissa do artigo é a mesma de 2010 — nenhum planejador domina todos os domínios.
  - **A3 [matiza o veredito da Fase 1]:** a Tabela 1 classifica as abordagens pela granularidade do portfólio: por domínio (PbP), por vários domínios (FDSS, GOP) e por instância (IBaCoP, SATzilla). O GOP, que usa **o mesmo portfólio para todas as instâncias**, empata com o FDSS em domínios novos, e o MIPlan, configurado **por domínio**, venceu a trilha de aprendizado da IPC 2014. `[HIPÓTESE]` A seleção por domínio continua competitiva quando há treino no próprio domínio; o veredito "descarta" do A3 em `auditoria/insumos-fase1.md` deve ser suavizado para "reformula": o que não se sustenta é "independentemente do problema", não a ideia de configurar por domínio.
  - **A6 / F4 [reforça a correção]:** `[FATO]` cinco dos sete premiados das trilhas ótima, satisficing e de aprendizado da IPC 2011 eram portfólios ou planejadores compostos por vários resolvedores. A arquitetura de sistema é uma dimensão própria, que a taxonomia de 2010 não tinha.
  - **A7 / F5 [mostra alternativa]:** a medida usada é a qualidade da IPC 2011 (custo do melhor plano sobre o custo do plano obtido, entre 0 e 1), com o tempo como segundo critério, e não só a cobertura.
  - **F2 [nuança]:** `[HIPÓTESE]` o resultado de que 27 tarefas bem escolhidas bastam para configurar o portfólio ótimo sugere que o problema de 2010 talvez não seja só o tamanho da amostra, mas quais instâncias ela contém. Vale para configurar portfólios, não automaticamente para validar uma relação entre características e desempenho.

## Pontos relevantes para o projeto

- **Para a Fase 3:** o portfólio OSS dá um terceiro ponto de referência, entre o melhor planejador isolado (*single best*) e o oráculo por instância (*virtual best*), para avaliar um *ranking* como o de 2010. Com as eficiências reproduzidas, dá para dizer que fração do limite atingível o *ranking* por domínio captura.
- Os autores registram que, em planejamento, se um planejador não resolve uma tarefa rápido, é improvável que a resolva, o que justifica portfólios sequenciais com fatias de tempo.
- O artigo é a versão de periódico; o trabalho de 2012 dos mesmos autores ("Performance analysis of planning portfolios", SoCS) é a versão preliminar só para planejamento ótimo, e estava entre os excluídos da triagem (E1-019) como redundante.

## Marcações

- `[FATO]` OSS da trilha ótima da IPC 2011: 200 tarefas; FDSS-1: 185 (92,5%); segundos colocados: 169 (84,5%) (seção 6.1.1).
- `[FATO]` 27 tarefas de treino reproduzem o portfólio ótimo obtido com todas (Tabela 2).
- `[FATO]` O MIPlan venceu a trilha de aprendizado da IPC 2014 com o melhor desempenho em qualidade e em cobertura (seção 6.3, Figura 8).
- `[HIPÓTESE]` A seleção por domínio não fica obsoleta; ela perde para a por instância quando não há treino no próprio domínio.

## Trechos literais

1. "the inherent difficulty of solving these problems using domain-independent solvers implies that no single solver dominates all others in every domain; i.e., different solvers perform best on different problems." (seção 1, p. 75)
2. "the results of the International Planning Competition 2011 (IPC 2011) show that five out of seven awarded planners in the sequential optimal, sequential satisficing and learning tracks were portfolios or planners that consisted of a collection of solvers." (seção 1, p. 76)
3. "MIPlan, the planning system which is able to automatically generate a portfolio configuration for a specific planning domain using gop, won the learning track of the International Planning Competition 2014." (resumo, p. 75)

## Uso de IA nesta nota

Claude Code, Coordenador (claude-opus-5-5), 23/09/2026. Leitura do texto integral do PDF fornecido pelo autor (o ScienceDirect bloqueia o download automatizado, embora o artigo esteja em acesso aberto). Conferência humana: pendente.
