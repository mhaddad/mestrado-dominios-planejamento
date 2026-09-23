---
tipo: nota-de-leitura
eixo: E3
citekey: coles2012survey
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2392/2275
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A2, A6]
fragilidades: [F1, F4]
perguntas: [Q1]
---

# A Survey of the Seventh International Planning Competition

**Coles, A.; Coles, A.; García-Olaya, Á.; Jiménez, S.; Linares López, C.; et al. · 2012 · AI Magazine**
**Link/DOI:** 10.1609/aimag.v33i1.2392

## Extração estruturada

- **Problema:** apresentar uma visão geral da IPC-2011 (7ª competição), suas trilhas, mudanças em relação a edições anteriores e os resultados/vencedores de cada trilha.
- **Método:** relato descritivo dos organizadores sobre a estrutura da competição (trilha determinística/clássica, multicore, ótima, satisfatória, temporal satisfatória, aprendizado, incerteza) e comparação de desempenho entre planejadores participantes, incluindo comparação com o vencedor da edição anterior (IPC-2008).
- **Dados / benchmarks:** 55 planejadores na trilha determinística (recorde até então, quase 8x mais que a 1ª competição); domínios padrão de IPC e nove domínios na trilha de aprendizado.
- **Resultado principal:** LAMA-2011 (Richter, Westphal, Helmert, Röger) venceu a trilha determinística/clássica, seguindo uma linhagem de planejadores por *forward-chaining search* (HSP 1998, FF 2000, Fast Downward 2004) com uso de *landmarks*. Na trilha ótima, o vencedor foi **Fast Downward Stone Soup 1** (Helmert, Röger, Seipp, Westphal), um planejador **baseado em portfólio**, superando o vencedor de 2008, Gamer (busca simbólica com BDDs). Na trilha multicore, venceu ArvandHerd, mas não superou o LAMA-2011 da trilha clássica. Na trilha de aprendizado, PBP2 venceu e superou o LAMA-2011 em quatro dos nove domínios.
- **Relação com a dissertação de 2010:** este é um achado direto para **A6** (taxonomia de técnicas de HADDAD 2010, que classifica Fast Downward como *hierarchical*): o artigo mostra que a versão vencedora da trilha ótima em 2011, **Fast Downward Stone Soup, é "portfolio based"** e não puramente hierárquica — sugerindo que a classificação A6 de 2010 é imprecisa ou desatualizada para essa família de planejadores, reforçando a fragilidade **F4** (taxonomia de técnicas discutível). Também alimenta **A2** (técnicas promissoras): a permanência do *forward-chaining* com *landmarks* como base do vencedor da trilha clássica (LAMA) é consistente com A2, mas a diversidade de trilhas (multicore, portfólio, aprendizado) sugere que a lista de seis técnicas "promissoras" de 2010 já não cobre toda a paisagem em 2011. Relevante para F1 (lacunas de revisão: HADDAD 2010 não cita a literatura de IPCs pós-2004 além de referências pontuais).

## Pontos relevantes para o projeto

- Corrige diretamente a classificação de Fast Downward em A6: a versão vencedora da trilha ótima em 2011 é explicitamente descrita como "portfolio based", não hierárquica.
- Mostra que planejadores "vencedores" mudam de família técnica entre trilhas e edições (busca simbólica → portfólio, por exemplo), o que é evidência empírica útil para Q1 (as conclusões de 2010 se sustentam com mais planejadores/domínios?).
- Documenta a introdução da trilha multicore em 2011, mostrando expansão de dimensões de avaliação além de cobertura (mas note: mede coverage/quality, alinhado a A7).
- Relaciona LAMA-2011 a uma linhagem histórica clara de vencedores por *forward-chaining* (HSP, FF, Fast Downward), útil para validar/atualizar a família "promissora" de A2.

## Trechos literais

- "Fast Downward Stone Soup 1 [...] won this year's competition outperforming the new version of the 2008 winner, Gamer [...] Fast Downward Stone Soup is portfolio based, in contrast to the symbolic search using binary decision diagrams (BDDs) of Gamer." (seção "Optimal Track")

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2392/2275 (resumo, introdução, descrição de todas as trilhas e vencedores, seção de referências/bios finais). Conferência humana: pendente.
