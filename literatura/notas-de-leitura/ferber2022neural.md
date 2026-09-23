---
tipo: nota-de-leitura
eixo: E4
citekey: ferber2022neural
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/download/19845/19604
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A2, A3, A7]
fragilidades: [F5]
perguntas: [Q1, Q2]
---

# Neural Network Heuristic Functions for Classical Planning: Bootstrapping and Comparison to Other Methods

**Ferber, P.; Geißer, F.; Trevizan, F.; Helmert, M.; Hoffmann, J. · 2022 · Proceedings of ICAPS 2022**
**Link/DOI:** 10.1609/icaps.v32i1.19845

## Extração estruturada

- **Problema:** como treinar funções heurísticas baseadas em redes neurais (NN) para planejamento clássico, usando apenas estados como entrada, de forma que a geração de dados de treino seja escalável — problema que trabalhos anteriores resolviam apenas parcialmente por aprendizado por instância (limitado a instâncias pequenas) ou por domínio (exige que o conhecimento generalize entre instâncias).
- **Método:** três métodos de geração de dados de treino por *bootstrapping* e iteração de valor aproximada (incluindo uma variante nova, h_BExp, que estima esforço de busca em vez de distância ao objetivo); redes neurais residuais (duas camadas densas + bloco residual) recebem o estado bruto em representação FDR (*finite-domain representation*) como entrada. Comparação cruzada com aprendizado por imitação por instância (h_IL, de Ferber, Helmert e Hoffmann 2020) e aprendizado por domínio via hipergrafos (h_HGN, de Shen, Trevizan e Thiébaux 2020), além de LAMA e h_FF como linhas de base.
- **Dados/benchmarks:** dez domínios clássicos (Blocks, Depots, Grid, NPuzzle, Pipesworld-notankage, Rovers, Scanalyzer, **Storage**, Transport, Visitall), com tarefas de dificuldade moderada e difícil, medindo cobertura (%) com limite de 10 horas de busca.
- **Resultado principal:** nenhuma heurística de rede neural domina as demais — cada uma é forte em um subconjunto de domínios (complementaridade). LAMA é dominante na maioria dos domínios, exceto em **Storage**, onde h_Boot resolve quase 90% das tarefas contra apenas 39% do LAMA e 48% do h_FF — um dos dois únicos casos conhecidos, segundo os autores, de heurística de rede neural superando o LAMA.
- **Relação com a dissertação de 2010:** achado de **impacto direto**, porque **Storage é um dos três domínios de validação usados na dissertação de 2010** (junto com Zeno-travel e Elevator). Este artigo mostra que, especificamente em Storage, uma técnica de aprendizado de máquina supera de forma expressiva tanto a busca heurística tradicional (LAMA, h_FF) quanto outras abordagens de aprendizado por domínio — o que **corrige/amplia A2**: a lista de técnicas "mais promissoras" de 2010 (Heuristic Search, Hierarchical, Knowledge-based, Forward-chaining, Plan-Space, Total-order) não incluía aprendizado de máquina como família de técnica, e este resultado mostra que, ao menos em Storage, essa omissão é relevante. Também **confirma o espírito de A3** (só com as características do domínio, o ranking escolhe o planejador com melhor desempenho): aqui, uma propriedade estrutural não especificada de Storage explica por que a busca heurística tradicional falha e o aprendizado funciona — mas os autores não a caracterizam formalmente, deixando a pergunta de *quais* características de Storage explicam esse padrão como aberta (relevante para **Q1/Q2**). Quanto a **A7** (eficiência = cobertura), o artigo usa cobertura como métrica primária, mas complementa com análise de "cobertura ao longo do tempo", o que **amplia F5**: mostra que o ranking entre técnicas pode até se inverter dependendo do limite de tempo considerado.

## Pontos relevantes para o projeto

- É o achado mais concreto do lote para a seção "relação com 2010": aponta um dos domínios de validação exatos da dissertação (Storage) como caso onde a lista de técnicas promissoras de A2 estava incompleta.
- Representa o domínio de forma minimalista — estado bruto em FDR (fatos proposicionais), sem *features* manuais, sem UML, sem lógica de descrição — e ainda assim obtém desempenho superior em um domínio específico; isso é evidência de que uma representação simples pode bastar quando combinada com dados de treino suficientes, mas não generaliza univocamente (o próprio artigo mostra alta variância entre domínios).
- Conclusão explícita dos autores de que a "informação" das heurísticas de NN varia muito mais entre domínios do que a das heurísticas baseadas em modelo — quantifica, em linguagem atual, o mesmo fenômeno de instabilidade entre domínios que motiva o ranking por domínio de 2010.
- Nenhuma tentativa de explicar *por que* Storage favorece aprendizado — lacuna que caberia exatamente ao tipo de análise estrutural que 2010 propôs (ainda que com UML) e que a revisão de 2026 poderia perseguir com *features* de PDDL.

## Trechos literais

> "hBoot solves almost 90% of the tasks compared to only 39% for LAMA and 48% for hFF." (Seção "Coverage Comparison for Hard Tasks", p. 585–586)

> "Storage is the only domain where LAMA struggles." (Seção "Experiment Results", p. 585)

> "The results show that NN heuristic functions are extremely complementary, and that per-instance learning often beats per-domain learning." (Conclusão, p. 586)

## Marcações

- `[FATO]` Em Storage, h_Boot atingiu cobertura de ~90% contra 39% do LAMA e 48% do h_FF, nas tarefas moderadas com validação (Tabela 1, p. 585).
- `[FATO]` Nenhuma das heurísticas de rede neural avaliadas domina as demais em todos os domínios; cada uma é forte em um subconjunto (Seção "Experiment Results", p. 585).
- `[HIPÓTESE]` A razão estrutural pela qual Storage favorece heurísticas aprendidas e desfavorece a busca heurística tradicional não é discutida pelos autores; investigá-la (por exemplo, via métricas estruturais do domínio, ao estilo de 2010 ou de Ståhlberg et al. 2022) seria uma forma concreta de testar Q2 com um caso empírico já identificado na literatura.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/ICAPS/article/download/19845/19604. Conferência humana: pendente.
