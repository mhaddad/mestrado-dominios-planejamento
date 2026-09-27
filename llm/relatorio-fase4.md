# Relatório da Fase 4 — camada LLM e resposta a Q3

> **Rascunho de IA; resposta a Q3 e propostas da seção 8 aceitas pelo autor em 27/09/2026.** Redação calibrada no mesmo dia, depois da avaliação das Fases 1 a 4 (referência do LAMA, correção de Holm, alcance das amostras), sem mudar a posição dos LLMs no mapa. Claude Code (claude-opus-5-5), 27/09/2026. Cada número vem de um registro de experimento (EXP-14 a EXP-18, em `experimentos/execucoes/`) e do script nele indicado. O texto da dissertação é do autor; este relatório é material de trabalho.

## 1. A pergunta

**Q3.** Onde os LLMs entram no mapa: como técnica de planejamento, como tradutores de domínio ou como seletores?

Quatro experimentos, um para cada papel, com os mesmos quatro modelos de 2026 (Claude Sonnet 5, GPT-6 Sol, Gemini 3.1 Pro e DeepSeek V4 Pro, via OpenRouter), raciocínio no nível *medium* e limite de 16.000 *tokens* por resposta. Custo da fase: US$ 10,51 nos EXP-14 a EXP-18; com o EXP-23 (27/09/2026, US$ 1,59), o uso da chave chegou a US$ 12,08, US$ 0,08 acima do teto de US$ 12 (chamadas em paralelo passaram da trava; ver o registro do EXP-23).

| Papel | Experimento | Registro |
|---|---|---|
| Seletor | X3: dado o domínio, escolher o planejador | EXP-14 (catálogo anônimo), EXP-15 (com nomes) |
| Planejador | X1: gerar o plano | EXP-16; EXP-23 (nomes ofuscados) |
| Planejador com verificador | X4: gerar o plano e corrigir com o retorno do VAL | EXP-17 |
| Tradutor | X2: gerar o domínio PDDL a partir de linguagem natural | EXP-18 |

## 2. Como seletor: não supera a escolha fixa do melhor planejador

`[FATO]` (EXP-14) Nos 41 domínios do Nível 4, com os planejadores descritos só pelas técnicas da taxonomia em 4 dimensões:
- o GPT-6 Sol empata com o melhor planejador único (perda 146 contra 143, p = 0,18);
- os outros três são significativamente piores (perdas de 188,5 a 259), também com a correção de Holm para os 4 modelos; com a pontuação exata, usada para comparar com o EXP-15, só o Gemini é (`experimentos/analise/correcao-multipla/holm.csv`);
- 148 das 163 respostas válidas escolhem um portfólio;
- nos quatro domínios em que uma técnica antiga é a melhor (System R no Blocks World e no TPP, SAT no Floortile, ANS no Pipesworld sem tanques), nenhum modelo escolhe o vencedor nem a técnica dele.

`[FATO]` (EXP-15) Com o nome e a edição da IPC de cada planejador, a escolha piora em 3 dos 4 modelos e se concentra em planejadores famosos: o Sonnet escolhe o LAMA 2011 em 40 dos 41 domínios; o Gemini, o FDSS23 em 40.

`[HIPÓTESE]` O LLM age como uma regra fixa: "escolher a descrição mais completa" sem nomes, "escolher o mais famoso" com nomes. Não há sinal de que lembre dos resultados por domínio. É o mesmo papel do melhor planejador único, e às vezes com uma escolha pior.

## 3. Como planejador: bom em instâncias pequenas e médias, melhor com verificador

`[FATO]` (EXP-16) Na menor instância (p01) de 8 domínios, 28 de 32 planos são válidos pelo VAL. As 4 falhas: 2 de formato (o conteúdo estaria certo), 1 pré-condição não satisfeita, 1 esgotamento de *tokens*. Os planos são em geral iguais ou mais curtos que os do LAMA na configuração `lama-first`, que para no primeiro plano encontrado e não procura planos curtos: no Blocks World, 28 passos contra 36 nos quatro modelos.

`[FATO]` (EXP-17) Na p05 dos 4 domínios de técnica antiga:
- 8 de 16 planos válidos na primeira tentativa;
- 13 de 16 depois de devolver ao modelo o erro apontado pelo VAL, em 1 ou 2 rodadas;
- as 3 falhas restantes são todas por limite de *tokens*, nenhuma por plano errado;
- planos bem mais curtos que os do LAMA (Blocks World: 86 a 90 contra 160; TPP: 73 a 75 contra 106);
- no Floortile p05, o GPT-6 Sol e o Gemini acham planos válidos (206 e 204 passos) onde o LAMA não achou em 300 s. O LAMA não é a referência forte nesse domínio: no Nível 4, o Floortile é vencido por planejadores SAT, que não foram rodados nessa instância.

`[FATO]` (EXP-23) Com todos os nomes trocados por rótulos sem significado, nos 25 pares que rodaram (7 ficaram sem chamada pela trava de custo), 16 planos são válidos, contra 23 dos mesmos pares com os nomes originais. Das 7 perdas, 5 são respostas que gastaram os 16.000 *tokens* raciocinando, sem chegar ao plano (Sonnet e DeepSeek), e 2 são planos errados. GPT-6 Sol e Gemini quase não mudam (13 de 16 contra 15 de 16), e o Blocks World ofuscado continua resolvido por todos os modelos que responderam.

Isso contrasta com as avaliações de 2023, em que os LLMs raramente produziam planos válidos [@valmeekam2023planbench], e é coerente com o efeito previsto pela arquitetura com verificador externo [@kambhampati2024llms], numa amostra de uma instância por domínio.

`[HIPÓTESE]` O custo e as falhas por *tokens* crescem com o tamanho da instância. As instâncias testadas são as menores do conjunto; as do Nível 4 chegam a dezenas de vezes mais objetos, e nada aqui indica que o LLM escale até elas.

## 4. Como tradutor: sintaxe fácil, equivalência difícil

`[FATO]` (EXP-18) A partir das descrições em linguagem natural do LLM+P [@liu2023llmp], em 6 domínios:
- 23 de 24 domínios gerados têm sintaxe válida;
- só 10 dos 24 têm a mesma assinatura de ações da referência (nomes, número, tipos e ordem dos parâmetros), e só nesses dá para testar a equivalência;
- desses 10, 6 são corretos (o GPT-6 Sol acerta os 3 que dá para comparar), 3 têm erro real de pré-condição e 1 é artefato do VAL. Os 10 não são uma amostra ao acaso: são os que coincidiram com a referência na assinatura, e a taxa de acerto nos outros 14 é desconhecida.

`[HIPÓTESE]` Boa parte da diferença não é erro, é liberdade de modelagem: a descrição não fixa nomes, ordem de parâmetros nem tipos. É o mesmo fenômeno das métricas UML de 2010 (EXP-07; F3): quem modela decide detalhes que a descrição do domínio não determina.

## 5. Posição dos LLMs no mapa das técnicas

Aceita pelo autor em 27/09/2026 como extensão da revisão (`auditoria/taxonomia-tecnicas.md`, seção 6.1), nas quatro dimensões da taxonomia (`auditoria/taxonomia-tecnicas.md`):

| Papel | D1 Algoritmo e busca | D2 Heurística | D3 Representação | D4 Arquitetura |
|---|---|---|---|---|
| LLM como planejador (X1) | Valor novo: geração do plano pelo modelo de linguagem, sem busca explícita | Não aplicável (não há heurística explícita) | Valor novo: domínio e problema lidos como texto (PDDL) | Planejador único |
| LLM com verificador (X4) | Idem | Idem | Idem | Valor novo: gerar e testar com verificador formal externo (VAL) |
| LLM como seletor (X3) | Não aplicável | Não aplicável | Não aplicável | Seletor de portfólio sem treino, pela descrição do domínio; o mesmo papel dos seletores treinados, como Delfi [@katz2018delfi] e IBaCoP [@cenamor2016ibacop]; sem ganho sobre o melhor planejador único nem sobre o seletor por características do EXP-12 (os seletores treinados da literatura não foram comparados) |
| LLM como tradutor (X2) | Fora do mapa das técnicas de planejamento: é uma etapa de modelagem, anterior ao planejador | | | |

Os valores novos na D1 e na D3 são do mesmo tipo dos já previstos para a busca simbólica e para a busca por largura (seção 6 da taxonomia): categorias que os 10 planejadores de 2010 não cobrem.

## 6. Resposta a Q3

(Aceita pelo autor em 27/09/2026.) Os LLMs entram no mapa **como técnica de planejamento**, não como seletores:

1. **Como planejador, com verificador formal:** é o papel em que se saem melhor nesta amostra. Nas instâncias pequenas e médias testadas, uma por domínio e uma chamada por modelo, produzem planos válidos na maioria dos casos, mais curtos que os do `lama-first`, e o verificador recupera a maior parte das falhas. A instância do Floortile que o LAMA não resolveu em 5 minutos não foi comparada com o vencedor do domínio. Com nomes ofuscados (EXP-23), o desempenho cai de 23 para 16 planos válidos em 25: a familiaridade dos nomes pesa, sobretudo como custo de raciocínio, mas bem menos que a queda do Mystery Blocksworld na literatura de 2023 [@valmeekam2023planbench]. Fica sem teste a escala.
2. **Como tradutor:** úteis para produzir PDDL sintaticamente válido, mas o resultado precisa de verificação contra uma referência ou contra problemas conhecidos. Ficam fora do mapa das técnicas, como etapa de modelagem, o mesmo lugar que as ferramentas de modelagem UML ocupavam em 2010.
3. **Como seletor:** não acrescentam nada à escolha fixa do melhor planejador. Escolhem por regra geral ou por reputação, sem ler o ajuste entre técnica e domínio, o que é coerente com a resposta a Q1 (`experimentos/relatorio-fase3.md`): nem as características de domínio nem os LLMs antecipam os poucos domínios em que uma técnica antiga vence.

## 7. Limites

- **Uma chamada por par** modelo × domínio (ou instância), sem repetição: a variação entre repetições não foi medida.
- **Amostras pequenas no X1 e no X4:** uma instância por domínio (p01 em 8 domínios; p05 em 4). O X2 tem 6 domínios.
- **Instâncias conhecidas:** domínios como Blocks World e Gripper são muito divulgados; o modelo pode ter visto instâncias parecidas. A condição com nomes ofuscados (EXP-23) cobre só o X1 (não o X4) e 25 dos 32 pares.
- **Referência do planejador clássico:** `lama-first` com 300 s, que não otimiza o tamanho do plano e não é o melhor planejador em todos os domínios testados.
- **Limite de 16.000 *tokens*:** as falhas restantes do X4 indicam que um limite maior mudaria o resultado, com custo maior.
- **Seletor avaliado só por domínio e só por cobertura**, como no Nível 4 da Fase 3.
- **Modelos de setembro de 2026:** os resultados valem para essas versões; as datas de corte do treinamento não foram verificadas na fonte.

## 8. O que isto muda na dissertação

Aceito pelo autor em 27/09/2026:

1. Um capítulo ou seção nova sobre LLMs, com os três papéis separados e a conclusão de que o lugar deles no mapa é o de técnica de planejamento com verificador.
2. A taxonomia em 4 dimensões ganha os valores novos da seção 5, marcados como extensão da revisão.
3. A ligação entre X2 e F3 (a descrição não determina o modelo) entra na discussão das métricas de modelagem.
