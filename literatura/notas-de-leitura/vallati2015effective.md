---
tipo: nota-de-leitura
eixo: E6
citekey: vallati2015effective
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://www.ijcai.org/Proceedings/15/Papers/243.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A5]
fragilidades: [F3]
perguntas: [Q2]
---

# On the Effective Configuration of Planning Domain Models

**Mauro Vallati, Frank Hutter, Lukáš Chrpa, Thomas L. McCluskey · 2015 · Proceedings of the Twenty-Fourth International Joint Conference on Artificial Intelligence (IJCAI 2015), p. 1704–1711**
**Link:** https://www.ijcai.org/Proceedings/15/Papers/243.pdf

## Extração estruturada

- **Problema:** o desempenho dos planejadores independentes de domínio depende não só do conteúdo do domínio, mas também de como os elementos do modelo PDDL estão ordenados (predicados, operadores, pré-condições e efeitos), algo até então subestimado na engenharia de conhecimento para planejamento.
- **Método:** formalizam a "configuração do modelo de domínio" como o conjunto das ordens em que predicados, operadores, e as pré-condições/pós-condições de cada operador são listados no PDDL. Usam o algoritmo de configuração automática SMAC (busca em espaço de parâmetros contínuos [0,1] por elemento configurável) para encontrar, para cada planejador, a configuração que minimiza o *Penalized Average Runtime* (PAR10). Comparam o modelo original (o usado nas IPCs) com o modelo configurado por planejador.
- **Dados/benchmarks:** 6 planejadores (Jasper, LPG, Madagascar/Mp, Mercury, Probe, Yahsp3) sobre 7 domínios (Blocksworld, Depots, Matching-Bw, Parking, Rovers, Tetris, ZenoTravel), com ~550 instâncias aleatórias por domínio (~500 treino, ~50 teste), cerca de 3.800 problemas de planejamento no total. Métricas: cobertura, IPC score e PAR10.
- **Resultado principal:** a configuração do modelo de domínio tem impacto substancial e estatisticamente significativo no desempenho dos planejadores (teste de Wilcoxon), incluindo casos em que a configuração muda qual é o melhor planejador em um domínio (ex.: em Blocksworld, Yahsp passa a superar LPG após configuração; em Depots e Tetris, outro planejador assume a liderança). Uma configuração "ruim" (deliberadamente adversarial) degrada o desempenho de forma significativa (IPC score: −21,1 vs. original, −64,4 vs. melhor; cobertura: −2,0% vs. original, −6,6% vs. melhor).
- **Relação com a dissertação de 2010:** o artigo mostra que variações de desempenho atribuíveis à "complexidade do domínio" podem, na verdade, ser produzidas por decisões de codificação (ordem dos elementos) que nada têm a ver com o conteúdo semântico do domínio. Isso qualifica/corrige [A5] (que trata a complexidade medida pela UML como determinante do desempenho): o artigo evidencia um fator de confusão — a *configuração sintática* do modelo — que também move o desempenho, de forma robusta e mensurável, independentemente das características "reais" do domínio. É evidência central para [F3] (as métricas do modelo, e não do problema, e dependentes de quem o constrói, também aqui dependem de escolhas do engenheiro do conhecimento) e alimenta [Q2] (mostra que propriedades estruturais do modelo têm poder preditivo sobre o desempenho, mas não são propriedades do domínio em si — são artefatos de codificação que precisam ser controlados antes de atribuir causalidade a "características do domínio").

## Pontos relevantes para o projeto

- Fornece o primeiro grande estudo controlado (após Howe & Dahlman 2002, citado no próprio artigo) que isola o efeito da *ordem* dos elementos do modelo PDDL sobre o desempenho, com metodologia reprodutível (SMAC, PAR10, IPC score).
- Mostra que rankings de competições (IPC) podem mudar apenas por reordenação do modelo — implicação direta para a validade de comparações entre planejadores como as feitas em 2010.
- Identifica mecanismo causal plausível: a ordem influencia o desempate em buscas A* e a ordem de checagem de pré-condições, afetando a exploração do espaço de busca.
- Nota que planejadores baseados no framework Fast Downward tendem a ser menos sensíveis à configuração (por reordenarem operadores alfabeticamente no pré-processamento) — relevante para qualquer generalização sobre "que técnica é mais sensível a que característica".
- Referência ao trabalho pioneiro de Howe e Dahlman (2002) como precursor direto desta linha, útil para registro em [F1] (lacunas de revisão de 2010).

## Trechos literais

- "In this paper, we investigate how the performance of planners is affected by domain model configuration. [...] this process (which can, in principle, be combined with other forms of reformulation and configuration) can have a remarkable impact on performance across planners." (Abstract)
- "Results presented in Table 1 confirm the significant impact of domain model configurations on most of the state of the art planning engines, leading to some remarkable score fluctuations." (Seção 3.2, p. 1707)
- "This indicates that the original domain models, i.e. the models which are currently used when benchmarking planning systems, are not in a 'planner-friendly' shape." (Seção 3.2, p. 1709)

## Marcações

- `[FATO]` A configuração (ordem) do modelo PDDL, mantendo o conteúdo semântico idêntico, produz mudanças estatisticamente significativas de desempenho em 6 planejadores e 7 domínios, ao ponto de alterar o ranking relativo entre eles (Seção 3.2, Tabelas 1–4).
- `[FATO]` Uma configuração adversarial (pior caso) degrada desempenho de forma mensurável e generalizada entre planejadores (Seção 3.2).
- `[HIPÓTESE]` (minha interpretação) Isso sugere que, em 2010, parte da variação de cobertura atribuída às características de domínio medidas em UML pode estar confundida com decisões de tradução/serialização do modelo (do UML para PDDL, e do PDDL para a entrada do planejador) que não foram controladas — um risco não discutido na dissertação original.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://www.ijcai.org/Proceedings/15/Papers/243.pdf. Conferência humana: pendente.
