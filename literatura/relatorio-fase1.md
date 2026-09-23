# Relatório da Fase 1 — revisão de literatura assistida por IA

Execução multiagente de 22 e 23/09/2026, conforme `plan/fase1-estrategia-multiagentes.md`. Coordenação: Claude Code, claude-opus-5. Execução: subagentes claude-sonnet-5. **Tudo aqui é material de trabalho pendente de confirmação do autor.**

---

## 1. O que foi feito, onda a onda

| Onda | Agentes | Saída | Estado |
|---|---|---|---|
| 0. Protocolo | Coordenador | `literatura/protocolo/protocolo-busca.md` (v1.1) | concluída |
| 1. Busca | 8 buscadores | 8 listas brutas, `lista-consolidada.csv` | 344 registros, **317 obras únicas** |
| 1b. Lacunas | 1 buscador dirigido | `busca/lacunas-bruta.csv`, `lacunas-memo.md` | 5 lacunas investigadas, 4 obras novas |
| 2. Triagem | 4 triadores + Coordenador | `triagem.csv` | 321 triadas, **155 incluídas**, 166 excluídas |
| 3. Verificação | 4 verificadores + Coordenador | `verificacao-metadados.csv`, `candidatas.bib` | **154 verificadas** no registro primário, 1 divergente |
| 4. Leitura | 12 leitores + Coordenador | 153 notas em `notas-de-leitura/` | 91 de texto integral, 62 de resumo |
| 5. Síntese | 8 sintetizadores | 8 sínteses, 17.785 palavras | todas as 153 notas citadas |
| 6. Rascunho | 1 redator + 1 crítico + Coordenador | `redacao/capitulos/02-fundamentos.md` e o parecer | 6.000 palavras, 90 chaves, 9 achados corrigidos |
| 7. Consolidação | Coordenador | este relatório, `auditoria/insumos-fase1.md` | concluída |

Foram 45 execuções de subagentes. Duas interrupções por limite de uso da API foram superadas retomando os agentes com o contexto preservado, sem refazer trabalho.

**Números da triagem:** 155 incluídas (77 de prioridade A, 67 B, 11 C), distribuídas entre 15 e 24 obras por eixo. Das 166 exclusões, 96 foram por redundância diante do teto (critério X7, criado na revisão da triagem), 32 por aplicação específica, 24 por estar fora do tema, 12 por duplicata e 2 por falta de resumo.

**Números da verificação:** 154 obras conferidas no registro primário (Crossref, arXiv, anais oficiais). Em 68 houve alguma discrepância com o que a busca havia registrado, e **17 *preprints* tinham versão publicada revisada por pares** que passou a ser a referência. Há texto integral aberto para 117 das 155.

## 2. Achados principais

### 2.1 A tese central de 2010 se sustenta; o instrumento e a unidade de análise, não

`[FATO]` O princípio de que características extraídas de um problema antes da escolha da técnica predizem qual técnica terá melhor desempenho não é hipótese isolada da dissertação: é o fundamento de um campo inteiro, formalizado por Rice em 1976 e desenvolvido desde 2008 em portfólios de planejadores. `[FATO]` Mas a unidade preditiva migrou do **domínio** para a **instância**: sistemas modernos escolhem planejadores diferentes para instâncias distintas do mesmo domínio, e superam a seleção fixa por domínio. A afirmação A3 de 2010 — de que bastam as características do domínio, independentemente do problema — é a que menos resiste.

### 2.2 A taxonomia de técnicas não se sustenta

`[FATO]` Três atribuições de 2010 contrariam a fonte primária: o Fast Downward se descreve como planejador de progressão heurística, não como *Hierarchical*; planejadores SAT não fazem encadeamento progressivo; e a categoria *plan-space* não descreve SATPlan nem MAXPLAN. `[FATO]` A raiz é estrutural: a taxonomia mistura, em seis rótulos exclusivos, quatro dimensões que a literatura trata separadamente — algoritmo de busca, tipo de heurística, representação de estado e arquitetura do sistema. Famílias inteiras de hoje (largura/novidade, busca simbólica, heurísticas aprendidas e, sobretudo, portfólios, que vencem trilhas das IPCs desde 2011) não cabem nela.

### 2.3 A ameaça mais séria ao método de 2010 não estava prevista

`[FATO]` Reordenar ou reconfigurar sintaticamente um modelo de domínio, **sem alterar o que ele significa**, muda o desempenho dos planejadores e inverte *rankings*: um mesmo planejador variou do 2º ao 11º lugar só por reordenação, e a configuração automática produziu acelerações de até 25 vezes. `[HIPÓTESE]` Como a dissertação não relata ter controlado a ordem dos elementos que o itSIMPLE gera ao exportar PDDL, parte da variação atribuída em 2010 a "características do domínio" pode estar confundida com decisões de serialização. Isso é lacuna metodológica identificável, não refutação.

### 2.4 O antecedente esquecido

`[FATO]` O artigo de 2005 dos próprios criadores do itSIMPLE já declarava o objetivo de "classificar características de domínio para decidir que técnica de planejamento ou heurística serve melhor ao domínio". A dissertação de 2010 executou um alvo anunciado pela equipe da ferramenta que usou, e não citou esse artigo. É o caso mais concreto da fragilidade F1. O mesmo artigo documenta que a ferramenta **impõe** as classes `Planner`, `Environment` e `Agent`, o que dá base documental ao achado G2 da Fase 0 sobre a exclusão de classes auxiliares na contagem.

### 2.5 Os LLMs entram como tradutores, não como planejadores

`[FATO]` Como planejador autônomo, o desempenho é baixo; acoplado a um planejador clássico como tradutor para PDDL, sobe muito. O ganho de confiabilidade vem sempre de um verificador externo, não da autocrítica do modelo. `[FATO]` E a variação por domínio é o achado mais replicado do eixo: trocar os nomes de um domínio por rótulos sem significado, mantendo a lógica idêntica, derruba o desempenho em ordens de grandeza — inclusive nos modelos de raciocínio de 2024. `[HIPÓTESE]` Isso confirma o espírito da tese de 2010 e ao mesmo tempo mostra que, para LLMs, o que pesa é familiaridade lexical, dimensão que nenhuma métrica UML captura.

### 2.6 A ponte para desenvolvimento de software é hipótese, e a literatura delimita bem o quanto

`[FATO]` Cinco arcabouços fora do planejamento compartilham a mesma estrutura lógica, mas nenhum autoriza, sozinho, a transferência: o No Free Lunch vale sobre médias em todas as funções de custo; o *task-technology fit* trata de ajuste no uso, não de escolha prévia. `[FATO]` Em desenvolvimento de software há evidência forte de variação por característica da tarefa (o mesmo agente vai de 78% a 25,6% conforme a origem do erro) e resultados contraditórios em ensaios com desenvolvedores reais, de ganho de 55,8% a perda de 19% no tempo, explicáveis por desenho, maturidade do repositório e experiência. `[FATO]` **Não há elo intermediário publicado** entre os arcabouços gerais e a proposta da Q4.

## 3. Lacunas investigadas deliberadamente

Afirmar que algo não existe exige busca dirigida. Foram feitas cinco, documentadas em `literatura/protocolo/lacunas-memo.md`:

| Lacuna | Veredito |
|---|---|
| Métricas de diagramas UML como *features* de domínio de planejamento | **Confirmada** nas bases consultadas. Há trabalhos sobre configuração estrutural de PDDL, nenhum com métricas UML no estilo de 2010 |
| LLM como seletor de planejador ou de portfólio | **Confirmada** nas bases consultadas |
| *Instance Space Analysis* aplicada a planejamento | **Confirmada** nas bases consultadas; a metodologia existe e é aplicada a escalonamento e otimização, nunca a planejamento |
| *Features* de sondagem (*probing*) | **Não confirmada**: Fawcett et al. (2014) já as usa |
| ICKEPS depois de 2017 | **Parcial**: nenhuma edição posterior localizada |

Todas são "ausência de evidência nas bases consultadas", não prova de inexistência. As três confirmadas são, juntas, a maior oportunidade de originalidade da revisão.

## 4. Controle de qualidade

Está detalhado em `literatura/protocolo/qc-coordenador.md`. Em resumo: amostra de 32 itens da busca reconferida (31 conferem, nenhum inventado); todas as 115 entradas com DOI e as 19 do arXiv reconferidas pelo Coordenador, com correção de 4 DOIs inválidos e de uma autoria; quatro números centrais de notas reconferidos no PDF original; e o parecer adversarial do capítulo, com 9 achados, todos conferidos e corrigidos.

**Falhas encontradas no próprio processo**, que ficam registradas:
- Os triadores usaram os códigos X2 e X6 para exclusões por redundância, o que distorcia o registro; criei o critério X7 e recodifiquei 96 linhas.
- Um leitor instalou o Ghostscript sem autorização para converter um PostScript do JAIR.
- Duas notas foram feitas sobre versões diferentes das obras que o `.bib` registra (`vallati2019robustness`, `vallati2015identifying`); precisam de conferência antes de citar.
- O GIPO foi "verificado" só por fontes secundárias; rebaixei para `divergente` e o tirei do `.bib`.

## 5. Fechamento (atualizado em 23/09/2026)

A fase foi concluída em 23/09/2026, depois de tratadas as pendências do autor:

| Pendência | Como foi resolvida |
|---|---|
| Confirmar a triagem | Delegada pelo autor ao Coordenador, com critérios acadêmicos padrão (protocolo, seção 9) |
| Gerar o `referencias.bib` | Sem Zotero, por decisão do autor. **133 obras**: 122 confirmadas aprovadas pelo autor, 5 ressalvas com ≥ 50 citações, 2 obras confirmadas a partir de PDFs do autor e 4 exceções do autor (`tonidandel2006reading`, Stone Soup, Delfi, Cedalion) |
| Obras sem acesso | Núñez et al. (2015) e Tonidandel et al. (2006) lidas a partir de PDFs do autor; Strobel e Kirsch (2014) acrescentada. Só `sette2008are` segue não lida (não citada em lugar nenhum). GIPO excluído |
| Notas com versão divergente | Resolvidas: uma é republicação declarada; a outra passou a citar a versão lida |
| Quatro decisões de fundo | Tomadas pelo autor (plano, seção 10) |
| Capítulo citável | 11 chaves trocadas ou retiradas; o capítulo cita 83 obras, todas no `referencias.bib` |

**Continua aberto, fora do escopo da Fase 1:** a ação 7 (acabamento ABNT: variante do CSL, caixa alta da NBR 10520, elementos pré-textuais). A divergência de autoria do MetaGPT foi fechada em 23/09/2026: vale a forma dos anais do ICLR 2024, a versão citada.

## 6. Insumos para a Fase 2

Estão em `auditoria/insumos-fase1.md`: veredito sugerido para cada afirmação A1–A8, situação das sete fragilidades e o que a literatura acrescenta aos achados G1–G17 da Fase 0. O resumo dos vereditos: **mantém** A1 (reformulada) e A4 (com ressalva); **reformula** A2, A3, A5 e A7; **descarta** A6 e A8 na forma atual. (Atualizado em 23/09/2026: o A3 passou de "descarta" para "reformula" depois da leitura de `nunez2015automatic`, que mostra que a configuração por domínio continua competitiva quando há treino no domínio.)

A Fase 2 não precisa mais discutir o que a literatura já resolveu com fonte primária. Precisa decidir quatro coisas que são do autor: se mantém a taxonomia de técnicas como objeto; se a pergunta passa a ser sobre instâncias; se as métricas UML continuam como objeto de teste ou são substituídas; e como tratar o antecedente de 2005.

## 7. Para as outras fases

- **Fase 3:** o experimento que responde à Q2 com originalidade é comparar, nos mesmos domínios, as métricas UML contra *features* automáticas de grafo causal e DTG, **separando discriminação entre domínios de dificuldade dentro do domínio** e controlando a ordem de serialização do modelo. Medir tempo e qualidade, não só cobertura.
- **Fase 4:** o papel a testar é o de tradutor acoplado a planejador clássico. Congelar modelo, versão e data; os números do eixo envelhecem em meses.
- **Fase 5:** o piloto deve ser aleatorizado por tarefa, medir características da tarefa explicitamente e tratar a divergência entre percepção e medição como achado esperado, não como ruído.

## 8. O que este relatório não cobre

Nenhuma referência aqui está aprovada pelo autor ainda; nada é citável no texto final. As sínteses e o capítulo são rascunhos de IA, não texto do autor. A leitura de 62 das 153 obras ficou no resumo, por acesso pago. E a busca cobriu as bases listadas no protocolo, com o OpenAlex indisponível na maior parte da execução por esgotamento de cota — o que aumenta a chance de haver obra relevante fora do alcance desta revisão.
