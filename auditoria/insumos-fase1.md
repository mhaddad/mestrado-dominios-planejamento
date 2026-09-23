# Insumos da Fase 1 para a auditoria (Fase 2)

Produzido pelo Coordenador (Claude Code, claude-opus-5) em 22/09/2026, a partir das oito sínteses em `literatura/sinteses/`. **Pendente de confirmação do autor.**

A Fase 2 classifica cada afirmação da dissertação de 2010 como **mantém / reformula / descarta**. Este documento entrega o que a literatura tem a dizer sobre cada uma, com as chaves que sustentam o veredito. Toda chave existe em `literatura/referencias/candidatas.bib` e tem nota em `literatura/notas-de-leitura/`; nenhuma está no `referencias.bib` verificado ainda, então **nada aqui é citável no texto final** antes da aprovação do autor em `literatura/referencias/revisao-referencias.md`.

Os rótulos A1–A8 e T1–T6 estão definidos em `literatura/protocolo/instrucoes-leitura.md`, seção 1; as fragilidades F1–F7, no plano, seção 4; os achados G1–G17, em `auditoria/achados-fase0.md`.

---

## 1. Veredito por afirmação de 2010

| Afirmação | Veredito sugerido | Por quê | Chaves principais |
|---|---|---|---|
| **A1** — existe relação entre características de domínio e técnicas | **mantém, com reformulação** | O princípio é a base de um campo inteiro (seleção de algoritmos), reconfirmado com dados atuais. Mas a unidade preditiva migrou de "domínio" para "instância", e características sintéticas de alto nível discriminam entre domínios sem capturar dificuldade dentro deles | `rice1976algorithm`, `kerschke2019automated`, `delarosa2017performance`, `stahlberg2022learninga` |
| **A2** — técnicas promissoras: *Heuristic Search*, *Hierarchical*, *Knowledge-based*, *Forward-chaining*, *Plan-Space*, *Total-order* | **reformula** | Busca heurística segue central, mas a lista está incompleta: falta aprendizado de máquina como família. Em **Storage**, um dos três domínios de validação de 2010, uma heurística aprendida supera LAMA e h_FF | `ferber2022neural`, `toyer2020asnets`, `jimenez2012review` |
| **A3** — só com características do domínio, independentemente do problema, o ranking escolhe o melhor planejador | **descarta na forma atual** | Sistemas por instância escolhem planejadores diferentes dentro do mesmo domínio e superam a seleção fixa por domínio; dentro de um domínio, *features* de domínio não discriminam nada | `cenamor2016ibacop`, `katz2018delfi`, `delarosa2017performance` |
| **A4** — mais características e planejadores melhoram o ranking | **mantém, com ressalva** | Vale como tendência, mas não há subconjunto de *features* bom para todos os planejadores, e ampliar escopo não garante generalização | `fawcett2014improved`, `seipp2014fast`, `hofmann2024learning` |
| **A5** — a UML mede a complexidade do domínio, que afeta o desempenho | **reformula (espírito mantido, instrumento trocado)** | A complexidade estrutural afeta o desempenho, mas os determinantes com efeito demonstrado são grafo causal, DTG e *treewidth*, extraídos automaticamente do PDDL; e parte do efeito atribuído à "complexidade" pode ser da ordem/configuração sintática do modelo | `helmert2009concise`, `hoffmann2011analyzing`, `domshlak2013complexity`, `vallati2021importance` |
| **A6** — taxonomia de técnicas (SAT como *forward-chaining*; SATPlan/MAXPLAN/SGPlan como *plan-space*; Fast Downward como *Hierarchical*) | **descarta** | Três atribuições contrariam a fonte primária, e a taxonomia mistura quatro dimensões independentes: algoritmo de busca, tipo de heurística, representação de estado e arquitetura do sistema. Famílias inteiras de hoje (largura/novidade, busca simbólica, heurísticas aprendidas, portfólios) não cabem nela | `helmert2006fast`, `rintanen2014madagascar`, `torralba2017efficient`, `coles2012survey`, `cenamor2019insights` |
| **A7** — eficiência = cobertura | **reformula** | A literatura mede também tempo, qualidade e custo do plano; margens de vitória por cobertura podem ser de ~1% e sensíveis a hardware; o *ranking* pode inverter conforme o limite de tempo | `helmert2011fast`, `percassi2021improving`, `ferber2022neural` |
| **A8** — trabalhos relacionados (só Hoffmann 2001 e Gerevini, Saetti e Serina 2004) | **descarta como revisão** | Faltam a linhagem de seleção de algoritmos (Rice; BUS/Roberts & Howe), a IPC 2008, o LAMA e — o caso mais grave — o artigo de 2005 dos próprios autores do itSIMPLE, que já declarava o objetivo de classificar características de domínio para escolher a técnica | `rice1976algorithm`, `roberts2009learning`, `richter2010lama`, `vaquero2005itsimple` |

## 2. As fragilidades F1–F7 depois da revisão

| # | Situação após a Fase 1 | Chaves |
|---|---|---|
| F1 (lacunas de revisão) | **Confirmada e ampliada.** Além de Rice, Roberts & Howe, IPC 2008 e LAMA, faltou o artigo fundacional do itSIMPLE (2005) e a linha ICKEPS/GIPO | `vaquero2005itsimple`, `roberts2009learning`, `richter2010lama` |
| F2 (amostra pequena) | **Confirmada**, com alternativa institucional pronta: conjuntos padronizados de cenários e competições de seleção | `bischl2016aslib`, `lindauer2019algorithm`, `lequen2026planner` |
| F3 (métricas medem o modelo, dependem do modelador) | **Confirmada, e é o achado mais forte da Fase 1.** Reordenar ou reconfigurar o mesmo modelo, sem mudar o que ele significa, altera desempenho e *ranking* | `vallati2021importance`, `vallati2015effective`, `mccluskey1997engineering`, `georgievski2026energy` |
| F4 (taxonomia discutível) | **Confirmada**, ver A6 | `helmert2006fast`, `rintanen2014madagascar`, `vallati2015portfolio` |
| F5 (eficiência reduzida a cobertura) | **Confirmada**, ver A7 | `percassi2021improving`, `helmert2011fast` |
| F6 (dados fora das competições) | **Confirmada**; resultados fora do ambiente oficial podem não ser comparáveis aos publicados | `lindauer2019algorithm`, `cenamor2019insights` |
| F7 (discretização por variância) | Sem tratamento direto na literatura lida. Continua como questão de método para a Fase 3 | — |

## 3. Achados da Fase 0 que a literatura ajuda a resolver

| Achado | O que a Fase 1 acrescenta |
|---|---|
| **G2** (a contagem de classes parece excluir classes auxiliares) | O artigo de 2005 do itSIMPLE documenta que a ferramenta **impõe** as classes `Planner`, `Environment` e `Agent` em todo modelo. Parte das "classes auxiliares" não é escolha do modelador, e sim estrutura fixa da ferramenta — o que dá base documental à exclusão e deve virar regra explícita do extrator da Fase 3 (`vaquero2005itsimple`) |
| **G3** (o SQL guarda taxonomia anterior, com `Linear`/`Non-Linear`) | Reforça A6/F4: a taxonomia era instável já em 2010, e a literatura mostra que ela mistura dimensões. A mudança entre o SQL e o texto pode ser sintoma disso, não descuido (`vallati2015portfolio`) |
| **G4** (Elevator: 6 casos de uso, 9 métodos, 10 ações) | Sem resposta na literatura; continua conferência interna |
| **G6, G7, G16** (arredondamento, agregação alternativa, denominadores diferentes) | A literatura reforça que métrica e limite de tempo mudam o *ranking*, então a escolha de agregação de 2010 precisa ser documentada e testada, não só reproduzida (`ferber2022neural`, `helmert2011fast`) |
| **G11, G12, G13, G17** (contagens de associações, generalizações e agregação; recálculo das classes) | A Fase 1 não resolve as contagens, mas muda o peso da questão: se o instrumento UML não é o preditor adequado (A5), recontar sem trocar o instrumento resolve pouco. Recomendo recontar **e** extrair *features* automáticas do PDDL para comparação (`helmert2009concise`, `hoffmann2011analyzing`) |
| **G14, G15** (subconjuntos de instâncias; Gripper gerado localmente) | Reforçados por F6: conjuntos e condições precisam ser idênticos para comparar (`lindauer2019algorithm`) |

## 4. Trabalhos futuros de 2010: o que a comunidade já fez

| Rótulo | Situação |
|---|---|
| T1 (extração automática de métricas no itSIMPLE) | Realizado fora do itSIMPLE, por outra via: *features* automáticas de PDDL e representações aprendidas a partir de dados brutos (`fawcett2014improved`, `asai2018classical`) |
| T3 (detalhar as técnicas) | Realizado e superado: a comunidade separou heurística, busca e arquitetura (`helmert2009landmarks`, `seipp2020saturated`) |
| T4 (pesos por característica) | Realizado por modelos estatísticos e de aprendizado (`hutter2014algorithm`) |
| T6 (análise estatística da discretização) | Parcialmente: a prática hoje é evitar discretizar, usando regressão sobre *features* contínuas (`fawcett2014improved`) |
| T2, T5 | Sem tratamento direto nas obras lidas |

## 5. O que a Fase 2 deve decidir e o que não precisa mais discutir

**Não precisa mais discutir** (a literatura já resolveu, com fonte primária): que Fast Downward não é *Hierarchical*; que planejadores SAT não são *forward-chaining* nem *plan-space*; que a seleção por instância supera a seleção por domínio; que cobertura sozinha é métrica insuficiente.

**Precisava decidir** (escolhas do autor, não da literatura) — **decidido em 23/09/2026**, ver plano, seção 10:
1. Se a nova versão mantém a taxonomia de técnicas como objeto (corrigida em quatro eixos) ou abandona a ideia de classificar planejadores por técnica exclusiva. → **Refazer em quatro dimensões.**
2. Se a pergunta central passa a ser sobre **instâncias** e não só sobre domínios — o que muda o desenho da Fase 3. → **Os dois níveis, reportados separadamente.**
3. Se as métricas UML continuam como objeto de teste (para responder Q2 com um resultado publicável, inclusive negativo) ou se são substituídas por *features* automáticas. → **Testadas contra *features* de PDDL, com controle da serialização.**
4. Como tratar a coincidência de propósito com o artigo de 2005 do itSIMPLE: a dissertação de 2010 executou um objetivo declarado pela equipe da ferramenta, e isso precisa aparecer na nova revisão de trabalhos relacionados. → **Assumido como origem da pergunta; conversar com o Tonidandel.**

## 6. Força da evidência por veredito (acrescentado em 23/09/2026)

Depois da confirmação da triagem (critérios em `literatura/protocolo/protocolo-busca.md`, seção 9), algumas obras da tabela da seção 1 ficaram **com ressalva**. Todos os vereditos têm ao menos uma obra confirmada, mas dois dependem mais das obras com ressalva e precisam de reforço antes de virar texto:

| Veredito | Obras com ressalva | Obras confirmadas que sustentam | O que fazer |
|---|---|---|---|
| **A3** (descarta) | `katz2018delfi` (literatura cinza de IPC), `delarosa2017performance` (baixo impacto: 2 citações) | `cenamor2016ibacop` | Reforçar com obras confirmadas do eixo E1 que mostram a seleção por instância: `sievers2019deep`, `ma2020online`, `kerschke2019automated` |
| **A7** (reformula) | `helmert2011fast` (literatura cinza de IPC), `percassi2021improving` (baixo impacto: 1 citação) | `ferber2022neural` | Reforçar com obras confirmadas que medem tempo e qualidade além da cobertura: `vallati2015portfolio`, `fawcett2014improved` |
| A1, A4, A6 | uma ou duas obras de literatura cinza de IPC | as demais | A literatura cinza de IPC é a referência padrão para descrever os planejadores das competições; aceitável para esse uso |

O argumento de que *features* de domínio não discriminam dificuldade **dentro** de um domínio, usado no capítulo e no veredito do A3, vem só de `delarosa2017performance`. É um artigo do ICAPS, revisado por pares, mas pouco citado. Esse ponto específico merece busca de confirmação independente antes da redação final.
