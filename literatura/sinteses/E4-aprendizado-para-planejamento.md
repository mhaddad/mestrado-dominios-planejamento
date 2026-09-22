---
tipo: sintese-de-eixo
eixo: E4
obras: 17
data: 2026-09-22
---

# E4 — Aprendizado para planejamento

## 1. Pergunta e resposta curta

O eixo pergunta o que o aprendizado de máquina trouxe ao planejamento — heurísticas e políticas aprendidas, planejamento generalizado, aprendizado de modelos de ação — e quão bem isso generaliza entre domínios. Resposta curta: trouxe uma família de técnicas inteira, ausente da lista de 2010, que em ao menos um caso documentado supera a busca heurística tradicional em um dos próprios domínios de validação da dissertação [@ferber2022neural]. Mas a generalização entre domínios segue sendo o problema central e não resolvido do campo: nenhuma técnica de aprendizado domina em todos os domínios testados, o desempenho varia conforme a estrutura de cada domínio, e a própria representação usada para aprender — não só o algoritmo — determina se a generalização ocorre [@stahlberg2022learninga; @hofmann2024learning]. Duas revisões do mesmo grupo, sete anos apesar, chegam à mesma conclusão: encontrar uma representação de conhecimento eficaz através de uma coleção de domínios continua em aberto [@jimenez2012review; @jimenez2019review] — em essência, a pergunta Q2, já formulada na literatura em 2012.

## 2. O que a literatura estabelece

### Heurísticas aprendidas

Redes neurais para heurísticas mostram desempenho **complementar**, não dominante: cada arquitetura é forte em um subconjunto de domínios [@ferber2022neural]. O achado de maior impacto para este projeto: em **Storage**, um dos três domínios de validação de HADDAD (2010) (com Zeno-travel e Elevator), a heurística por *bootstrapping* (h_Boot) resolve ~90% das tarefas difíceis contra 39% do LAMA e 48% do h_FF [@ferber2022neural]; os autores não explicam por quê. Trabalhos recentes usam grafos derivados da estrutura PDDL/*lifted*, sem modelagem manual, para treinar heurísticas independentes de domínio via GNN: GOOSE generaliza a problemas maiores que os de treino, superando h_HGN [@chen2024learning]. WL-GOOSE, com ML clássico sobre *features* de grafo Weisfeiler-Leman, supera ou empata com LAMA em 4 de 10 domínios (cobertura) e 7 de 10 (qualidade de plano), a custo menor [@chen2024return].

### Políticas generalizadas e planejamento generalizado

Linha mais numerosa do eixo. O trabalho fundacional representa domínios por abstração lógica de três valores sobre predicados unários e binários, para planos com laços válidos para classes de instâncias [@srivastava2011new]. Evoluiu para *features* de lógica de descrição (DL) combinadas com MaxSAT e um planejador FOND, aprendendo *features* e ações abstratas [@bonet2019learninga], depois estendida a domínios FOND, com sucesso em 7 de 12 domínios e falha por explosão combinatória nos outros 5 [@hofmann2024learning]. ASNets aprendem políticas reativas sobre o grafo bipartido ação–proposição do PDDL, com pesos compartilhados por domínio; em Blocksworld, política treinada em 50 instâncias pequenas resolveu 18.300 instâncias maiores [@toyer2020asnets], família estendida a planejamento numérico [@wang2024learning]. Outras abordagens usam gradiente/ator-crítico, aproximando-se de métodos combinatórios sem o gargalo dos *pools* de *features* [@stahlberg2023learning], ou busca guiada por política candidata (PG3) [@yang2022pg3].

### Aprendizado de modelos de ação

Uma linha distinta trata o próprio modelo de domínio como algo a aprender, não a assumir correto. SLAF aprende modelos de ação determinísticos sob observabilidade parcial, com garantias de exatidão, testado sobre Zeno-travel [@amir2008learning]. Outra abordagem transfere conhecimento entre domínios via busca na Web e MAX-SAT ponderado, com poucos dados no domínio-alvo [@zhuo2011crossdomain]. Uma terceira combina um modelo STRIPS deliberadamente incompleto com heurísticas/políticas de ML sobre simulador *black-box* [@greco2022scaling], citando o itSIMPLE — mesma ferramenta de 2010 — como referência de modelagem em engenharia de conhecimento.

### Da representação subsimbólica à simbólica

LatPlan aprende toda a representação simbólica do domínio — estados e ações — de imagens não rotuladas, eliminando a modelagem humana, e resolve a maioria das instâncias de três domínios de brinquedo mesmo sob ruído [@asai2018classical]. É prova de conceito, não testada em escala de IPC, mas é a resposta mais radical à proposta de 2010 de automatizar a extração de métricas do domínio (T1).

## 3. Como o domínio é representado para aprender

Ponto de contato direto com **Q2** — se métricas estruturais de modelagem acrescentam poder preditivo às *features* de PDDL. O lote revela pelo menos cinco famílias de representação, nenhuma delas UML:

1. **Lógica proposicional/predicados sob abstração de três valores** [@srivastava2011new].
2. ***Features* de lógica de descrição (DL)**, de predicados primitivos, para políticas e funções de valor gerais [@bonet2019learninga; @hofmann2024learning].
3. **Grafos/hipergrafos derivados da estrutura PDDL**, em políticas (ASNets, pesos compartilhados por domínio) [@toyer2020asnets; @wang2024learning] e em heurísticas via GNN, inclusive *lifted* [@chen2024learning] e via Weisfeiler-Leman com ML clássico [@chen2024return].
4. **Espaço latente aprendido** de dados subsimbólicos (imagens), sem estrutura simbólica dada [@asai2018classical].
5. **Estado bruto em representação de domínio finito (FDR)**, sem *features* manuais [@ferber2022neural].

O achado mais forte para Q2 é formal: existe correspondência teórica entre *features* de lógica de descrição e o fragmento lógico C2, e entre C2 e o poder expressivo de GNNs padrão — mesmo teto de expressividade [@stahlberg2022learninga]. Esse trabalho mostra, com prova teórica e verificação empírica, que a generalização depende do grau de lógica de contagem de variáveis (C_k) exigido pela função de valor ótima do domínio: GNNs generalizam perfeitamente em 10 de 11 domínios testados, mas falham sistematicamente em Rovers, cuja política ótima exige *features* C3, que GNNs padrão não computam. É o resultado mais próximo de responder Q2 diretamente: existe ao menos uma métrica estrutural — o grau de expressividade lógica necessária — com poder preditivo comprovado, mas derivada de predicados PDDL, não de UML [@stahlberg2022learninga]. Duas revisões, no entanto, mostram que a comunidade não convergiu para uma representação dominante em mais de uma década: em 2012 e de novo em 2019, a representação de conhecimento eficaz "através de uma coleção de domínios" segue em aberto [@jimenez2012review; @jimenez2019review].

## 4. Percurso 2008–2026

**2008–2011:** aprendizado de modelo de ação sob observabilidade parcial [@amir2008learning]; fundação lógica do planejamento generalizado [@srivastava2011new]; transferência de modelo de ação entre domínios [@zhuo2011crossdomain]. **2012:** primeira revisão sistemática, já com a representação de conhecimento entre domínios em aberto [@jimenez2012review]. **2018–2019:** LatPlan aprende a representação simbólica de imagens não rotuladas [@asai2018classical]; segunda revisão mostra a mesma lacuna sete anos depois [@jimenez2019review]; ASNets introduzem políticas generalizadas testadas em escala (18.300 instâncias) [@toyer2020asnets]; *features*/ações abstratas via MaxSAT [@bonet2019learninga]. **2022:** ano de maior densidade — relação formal entre expressividade lógica e generalização de GNNs [@stahlberg2022learninga]; heurística de rede neural supera o LAMA em Storage [@ferber2022neural]; modelagem STRIPS parcial com ML *black-box*, citando o itSIMPLE [@greco2022scaling]; PG3 [@yang2022pg3]. **2023–2024:** políticas por gradiente/ator-crítico [@stahlberg2023learning]; extensão a FOND [@hofmann2024learning] e a numérico [@wang2024learning]; GNN *lifted* [@chen2024learning] e ML clássico competitivo com LAMA [@chen2024return]. Padrão: expansão de escopo e diversificação de representação, sem família superior.

## 5. Relação com a dissertação de 2010

| Rótulo | Status | O que a literatura mostra | Chaves |
|---|---|---|---|
| A2 | corrige/amplia | ML ausente da lista de 2010; heurística aprendida supera LAMA e h_FF em Storage, domínio de validação da dissertação | [@ferber2022neural] |
| A1/A3 | confirma, por outra via | GNNs generalizam ou falham conforme o grau de lógica de contagem exigido pela função de valor — característica estrutural formal, mas não a métrica UML | [@stahlberg2022learninga; @toyer2020asnets] |
| A4 | matiza | Ampliar escopo (clássico → FOND) e o *pool* de *features* não garante melhor generalização; falha em 5 de 12 domínios | [@hofmann2024learning] |
| A5 | confirma espírito, corrige instrumento | Complexidade estrutural afeta desempenho, mas a métrica com poder preditivo comprovado é lógica (C_k), não UML | [@stahlberg2022learninga; @srivastava2011new; @jimenez2012review; @jimenez2019review] |
| A6 | torna obsoleta/amplia | Políticas generalizadas, heurísticas por GNN, aprendizado de modelo de ação, espaço latente não cabem na taxonomia de 2010 | [@toyer2020asnets; @bonet2019learninga; @chen2024learning; @yang2022pg3; @wang2024learning; @asai2018classical] |
| F2 | confirma, por analogia | Trabalhos do eixo também operam com poucos domínios ou dados limitados | [@srivastava2011new; @asai2018classical; @hofmann2024learning; @zhuo2011crossdomain] |
| F3 | amplia | *Features* lógicas/estruturais não dependem de modelador humano fazendo UML, mas a representação segue sendo decisão de projeto | [@srivastava2011new; @stahlberg2022learninga] |
| F4 | confirma e agrava | Taxonomias concorrentes coexistem (família algorítmica, alvo de aprendizado, forma de representação), nenhuma consolidada | [@jimenez2012review; @jimenez2019review] |
| F5 | amplia | Ranking pode se inverter conforme o limite de tempo, não só a cobertura final | [@ferber2022neural] |
| T1 | amplia radicalmente | LatPlan elimina a modelagem humana, aprendendo a representação simbólica de imagens não rotuladas | [@asai2018classical] |

## 6. Divergências e pontos em disputa

A **generalização entre domínios** é o ponto de maior disputa implícita do lote: não há consenso sobre se ela é um problema de dados, de arquitetura ou de expressividade da representação. A posição mais forte, com prova formal, é que a expressividade é o fator limitante: GNNs padrão não computam certas classes de função de valor (C3), e nenhum volume de dados resolveria isso sem mudar a representação [@stahlberg2022learninga]. Ferber et al. não caracterizam a causa estrutural do sucesso em Storage, deixando em aberto se é peculiaridade do domínio ou padrão generalizável [@ferber2022neural]. Hofmann e Geffner mostram falha por explosão combinatória, não por limite teórico — distinção que nenhum outro trabalho discute com o mesmo rigor [@hofmann2024learning].

Quanto a **comparações com o LAMA**, o quadro é misto. Em Storage, heurística aprendida bate o LAMA por larga margem (90% contra 39% de cobertura) [@ferber2022neural]. WL-GOOSE, com ML clássico sobre *features* de grafo, supera ou empata com LAMA em 4 de 10 domínios em cobertura e 7 de 10 em qualidade de plano [@chen2024return] — resultados que os autores dizem raros na literatura. Ao mesmo tempo, o padrão dominante em Ferber et al. é que nenhuma heurística de rede neural domina as demais e que o LAMA segue dominante, com Storage como exceção [@ferber2022neural]. Nenhum trabalho reconcilia as duas leituras — uma retrata aprendizado como nicho complementar, outra como competitivo em fração relevante de domínios.

## 7. Lacunas

Nenhuma obra caracteriza formalmente **por que** Storage favorece aprendizado enquanto a maioria dos domínios favorece o LAMA — a pergunta que caberia ao tipo de análise estrutural que 2010 propôs, agora aplicada a *features* de PDDL. Não há comparação direta e controlada entre métricas UML e *features* aprendidas de grafos de tarefa ou DL — a resposta a Q2 permanece inferida por analogia. A maioria dos trabalhos de planejamento generalizado opera com poucos domínios (8 a 12), sem cobertura equivalente às IPCs completas de 2010. Falta também conexão com os planejadores originais de 2010 (Blackbox, IPP, FF, R, LPG, Fast Downward, YAHSP, SGPlan, SATPlan, MAXPLAN) — as comparações se dão majoritariamente contra LAMA e h_FF, ausentes do conjunto de 2010.

## 8. Insumos para as próximas fases

Para A1/A3/A5, Ståhlberg, Bonet e Geffner oferecem métrica estrutural formal (grau C_k) candidata a substituir ou complementar as métricas UML de 2010 [@stahlberg2022learninga]. Para A2, o caso de Storage é ponto de partida concreto: domínio de validação original de 2010, com técnica de aprendizado que ali supera LAMA e h_FF [@ferber2022neural] — vale investigar, na fase de análise, se as métricas UML já apontavam Storage como estruturalmente distinto. Para a taxonomia (A6/F4), o eixo sugere ao menos cinco famílias novas: aprendizado de modelo de ação, heurísticas aprendidas, políticas generalizadas, aprendizado de representação simbólica a partir de dados subsimbólicos, e busca híbrida com modelo parcial. Para T1, LatPlan é a referência mais radical de automação de representação [@asai2018classical]. Zhuo et al. oferecem ponte para Q4 [@zhuo2011crossdomain].

## 9. Obras usadas

- amir2008learning
- asai2018classical
- bonet2019learninga
- chen2024learning
- chen2024return
- ferber2022neural
- greco2022scaling
- hofmann2024learning
- jimenez2012review
- jimenez2019review
- srivastava2011new
- stahlberg2022learninga
- stahlberg2023learning
- toyer2020asnets
- wang2024learning
- yang2022pg3
- zhuo2011crossdomain
