---
tipo: nota-de-leitura
eixo: E3
citekey: ipc2008results
prioridade: C
status: lido
profundidade: resumo
fonte-lida: https://ipc08.icaps-conference.org/deterministic/Results.html
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: [F1]
perguntas: []
---

# Results - IPC-2008, Deterministic Part

**IPC-2008, Deterministic Part (sem autoria individual) · 2008 · página oficial da competição**
**Link/DOI:** https://ipc08.icaps-conference.org/deterministic/Results.html

## Extração estruturada

- **Problema:** página não é um artigo, mas o registro oficial de resultados da parte determinística da 6ª International Planning Competition (IPC-2008), realizada em conjunto com o ICAPS-08.
- **Método:** disponibiliza links para apresentações, pôsteres e arquivos com os dados brutos e detalhados de pontuação de cada planejador competidor.
- **Dados / benchmarks:** resultados da competição de 2008, organizada em três partes (determinística, incerteza, planejamento com aprendizado) e, dentro da parte determinística, em múltiplas trilhas de otimização e satisfação (*optimization tracks*, *satisficing tracks*).
- **Resultado principal:** não há, no texto acessível desta página nem da página-irmã HomePage.html, uma lista explícita de planejadores vencedores por trilha — apenas links para PDFs de apresentação/pôsteres e arquivos de dados brutos (não baixados nesta sessão). A página HomePage.html confirma a estrutura de patrocínio por trilha: IBM Research patrocinou a trilha de otimização sequencial, ATRiCS a trilha temporal satisfatória, Adventium Labs a trilha satisfatória sequencial e SICK a trilha de otimização por *net-benefit*.
- **Relação com a dissertação de 2010:** a IPC-2008 é uma das fontes de dados originais de HADDAD (2010) (10 planejadores testados incluem vários competidores desta edição, como Blackbox, FF, SGPlan, SATPlan). Esta página **não permite**, por si só, confirmar ou corrigir a taxonomia de técnicas (A6) porque não lista vencedores nem famílias de técnica — apenas a estrutura de trilhas. Relevante para F1 (lacunas de revisão), pois documenta que a IPC-2008 é citada mas a fonte primária de resultados/vencedores não foi consultada em detalhe em 2010.

## Pontos relevantes para o projeto

- Confirma que a IPC-2008 teve estrutura de trilhas segmentada (otimização sequencial, satisfatória sequencial, temporal satisfatória, *net-benefit* de otimização), o que é mais granular do que a comparação única de HADDAD (2010).
- Os dados brutos e detalhados (score details) estão disponíveis para download, mas não foram baixados aqui (fora do escopo desta nota curta); poderiam ser usados em trabalho futuro (T2, agregação automática de novos resultados).
- Não permitiu, nesta leitura, identificar vencedores e famílias de técnica — recomenda-se, se o Coordenador quiser essa informação para IPC-2008, buscar o artigo de análise pós-competição (não presente neste lote) em vez desta página de resultados brutos.

## Trechos literais

- "IPC-2008 and its organization is split into three parts: the deterministic part, that considers fully deterministic and observable planning (previously also called \"classical\" planning), the uncertainty part [...] and the new planning with learning part" (página HomePage.html)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo (páginas HTML Results.html, HomePage.html e Planners.html do site oficial da IPC-2008; não continha texto de análise de vencedores). Conferência humana: pendente.
