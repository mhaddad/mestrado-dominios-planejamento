---
tipo: nota-de-leitura
eixo: E4
citekey: zhuo2011crossdomain
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/view/13449
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: [F2]
perguntas: [Q2, Q4]
---

# Cross-Domain Action-Model Acquisition for Planning via Web Search

**Zhuo, H.H.; Yang, Q.; Pan, R.; Li, L. · 2011 · ICAPS**
**Link/DOI:** 10.1609/icaps.v21i1.13449

## Extração estruturada

- **Problema:** técnicas de aprendizado para adquirir modelos de ação em planejamento geralmente assumem quantidade significativa de dados de treino no domínio de interesse (domínio-alvo); frequentemente é difícil obter dados suficientes para garantir modelos de ação de alta qualidade.
- **Método:** desenvolve uma abordagem para aprender modelos de ação com dados de treino limitados no domínio-alvo, transferindo conhecimento de domínios auxiliares/fonte relacionados (já com modelos de ação criados); usa busca na Web para identificar conhecimento transferível entre os domínios fonte e alvo, codificando o conhecimento transferido e os dados disponíveis do domínio-alvo como restrições em um problema de satisfatibilidade máxima ponderada (*weighted MAX-SAT*), resolvido por um solver MAX-SAT.
- **Dados / benchmarks:** domínios da International Planning Competition (IPC) e alguns domínios sintéticos.
- **Resultado principal:** o arcabouço de aprendizado por transferência é empiricamente efetivo em vários domínios, incluindo domínios da IPC e sintéticos, para aprender modelos de ação de alta qualidade com dados limitados no domínio-alvo.
- **Relação com a dissertação de 2010:** não corrige nem confirma diretamente nenhuma afirmação específica (A/T/F) de HADDAD (2010), mas é diretamente relevante para **Q2** e **Q4** — trata explicitamente de como conhecimento aprendido em um domínio pode ser transferido para outro, questão central para saber se características/técnicas aprendidas em domínios conhecidos generalizam para novos domínios (paralelo à pergunta de HADDAD 2010 sobre se características de domínio predizem desempenho de técnica). Relacionado a F2 (amostra pequena de HADDAD 2010): a motivação central do artigo — poucos dados de treino no domínio-alvo — é análoga à limitação de amostra pequena identificada em 2010.

## Pontos relevantes para o projeto

- Trata diretamente da generalização entre domínios via transferência de conhecimento (aprendizado de modelos de ação), tema central para Q2/Q4 mesmo não usando as mesmas métricas de HADDAD (2010).
- Usa domínios da IPC como *benchmark*, ligando-se ao mesmo universo de dados usado por HADDAD (2010) e por outros trabalhos deste lote (E3).
- É um exemplo antigo (2011) de "aprendizado por transferência" em planejamento, que antecede a onda de GNNs/aprendizado profundo dos demais trabalhos do eixo E4 do lote — útil para traçar a linha do tempo da pesquisa em aprendizado para planejamento.

## Trechos literais

- "We develop a novel approach to learning action models with limited training data in the target domain by transferring knowledge from related auxiliary or source domains." (resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://ojs.aaai.org/index.php/ICAPS/article/view/13449 (não foi possível baixar o PDF completo nesta sessão; a página de visualização do periódico retornou apenas HTML). Conferência humana: pendente.
