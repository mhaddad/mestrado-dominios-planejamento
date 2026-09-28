---
tipo: nota-de-leitura
eixo: E8
citekey: chen2026risa
prioridade: B
status: verificado
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2608.22191
metadados: verificada-na-fonte-primaria
referencia-verificada: true
afirmacoes-2010: [A1]
fragilidades: []
perguntas: [Q3, Q4]
---

# Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents

**Chen, K.; Nian, J.; Cao, Y.; Jiang, Y. · 2026 · arXiv (v1, 23/08/2026)**
**Link/DOI:** https://arxiv.org/abs/2608.22191 (sem DOI Crossref no momento da leitura)

## Extração estruturada

- **Problema:** agentes de engenharia de software resolvem tarefas de repositório com trajetórias longas e estocásticas; repetir tentativas acha correções que uma execução só perde. Mas escolher entre tentativas é difícil: *patches* não têm forma canônica, e ações irmãs geradas do mesmo prefixo são correlacionadas.
- **Método:** Risa (*Routing-Informed Steering and Arbitration*). Usa os traços do roteador interno de modelos *mixture-of-experts* esparsos (quais especialistas cada *token* ativou, com que peso) como uma "impressão digital" do que o modelo está computando. Em dois níveis: dentro de uma tentativa, favorece ações diferentes do histórico recente na exploração e ações convergentes na escrita do *patch* (16 candidatas por passo); entre 4 tentativas independentes, escolhe o *patch* final com maior concordância nos *tokens* de decisão (os menos prováveis). Não usa juiz externo nem executa os *patches* para escolher.
- **Dados:** SWE-bench Verified (500 tarefas), com gpt-oss-20b e gpt-oss-120b em três níveis de raciocínio (baixo, médio, alto), e reprodução com Qwen3.6-35B-A3B.
- **Resultado principal:** com os mesmos conjuntos de 4 tentativas, a escolha pelo Risa sobe a média de 44,9% (escolha ao acaso) para 48,2% nas seis condições do gpt-oss, contra 48,0% da escolha por consenso textual e 48,3% da variante híbrida; o oráculo (alguma das 4 tentativas resolve) chega a 60,9% (Tabela 2). No Qwen3.6, 45,2% contra 41,7% ao acaso e 45,0% do consenso textual (McNemar exato p = 1,000 contra o consenso). Custo: cerca de 360 mil *tokens* gerados por tarefa na configuração média; de 22 a 222 GPU-h por condição (Apêndice I.1).
- **Relação com a dissertação de 2010:** **A1** [por analogia fraca, `[HIPÓTESE]`]. A distância entre o oráculo das 4 tentativas (60,9%) e a melhor escolha (48,3%) é a mesma estrutura da lacuna entre o *virtual best* e o *single best* das Fases 3 e 4B: há complementaridade entre execuções, e o problema é identificá-la antes de saber o resultado. Não há características de domínio nem escolha entre técnicas.

## Pontos relevantes para o projeto

- Não é roteamento entre configurações de agente: é coordenação de tentativas repetidas de um mesmo agente. Entra na Ponte como exemplo de **exploração e compromisso** guiados por sinais da própria trajetória, o terceiro nível (orquestração) da tese provisória da Fase 5.
- O sinal usado é interno ao modelo (roteamento de MoE), disponível só em modelos abertos com essa arquitetura. Os próprios autores limitam o método a agentes MoE "caixa-branca".
- O ganho sobre o consenso textual é pequeno (0,2 a 0,3 ponto na média); o resultado mais forte é contra a escolha ao acaso. Isso reforça, em outro terreno, o padrão das Fases 3, 4 e 4B: a escolha fixa ou simples já captura boa parte do que um seletor sofisticado alcança.
- Para a Q3: mostra LLMs usados com várias tentativas e arbitragem, uma arquitetura de "gerar e escolher" parente da de "gerar e verificar" do X4, mas sem verificador formal.

## Trechos literais

"Risa's routing arbitration raises the macro-average resolved rate from 44.9% under uniform sampling to 48.2% on the gpt-oss family, matching text consensus without answer-string matching" (resumo)

"The 60.9% Oracle confirms substantial complementary coverage across the four-attempt pools." (seção 5.1)

"Risa's current instantiation assumes accessible sparse-MoE routing and repeated trajectories, making it naturally suited to white-box MoE agents." (Limitações)

## Marcações

- `[FATO]` Com os mesmos conjuntos de tentativas, a arbitragem por roteamento supera a escolha ao acaso em todas as condições e empata com o consenso textual (Tabela 2; Qwen, McNemar p = 1,000).
- `[FATO]` O oráculo das 4 tentativas (60,9%) fica 12,6 pontos acima da melhor escolha implantável (48,3%) (Tabela 2).
- `[FATO]` O método depende de acesso aos traços de roteamento de modelos MoE (Limitações).
- `[HIPÓTESE]` A lacuna oráculo × escolha é o análogo, em agentes de código, da lacuna *virtual best* × *single best* estudada desde 2010.

## Uso de IA nesta nota

Claude Code (claude-opus-5-5), 28/09/2026. Leitura do PDF do arXiv (v1), extraído com `pdftotext`: corpo do artigo inteiro (seções 1 a 7) e apêndice de custo (I.1); os demais apêndices não foram lidos; números conferidos na Tabela 2 e no texto da seção 5; metadados conferidos na API do arXiv. Promoção aprovada pelo autor em 28/09/2026.
