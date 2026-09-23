---
tipo: nota-de-leitura
eixo: E3
citekey: wichlacz2022landmark
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://www.ijcai.org/proceedings/2022/0647.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A2, A6]
fragilidades: [F4]
perguntas: []
---

# Landmark Heuristics for Lifted Classical Planning

**Wichlacz, J.; Höller, D.; Hoffmann, J. · 2022 · IJCAI**
**Link/DOI:** 10.24963/ijcai.2022/647

## Extração estruturada

- **Problema:** sistemas de planejamento de estado da arte precisam de uma representação instanciada (*grounded*/proposicional) da tarefa, mas o modelo de entrada é fornecido "*lifted*" (predicados e esquemas de ação com variáveis); o tamanho do modelo instanciado é exponencial na aridade dos predicados/esquemas, limitando aplicabilidade. Faltavam heurísticas de busca heurística eficazes no cenário *lifted*.
- **Método:** define dois métodos de extração de marcos (*landmarks*) diretamente no modelo *lifted* e projeta uma nova família de funções heurísticas baseadas nesses marcos, integrada a um mecanismo de busca (incluindo estilo LAMA).
- **Dados / benchmarks:** conjunto de *benchmarks* usado por Lauer et al. (2021) para avaliar planejadores *lifted*, com domínios que exploram diferentes razões de dificuldade de instanciação (alta aridade de esquema de ação, alta aridade de predicado, grande universo de objetos).
- **Resultado principal:** as heurísticas de marco *lifted* propostas, quando usadas isoladamente, têm desempenho inferior às melhores heurísticas *lifted* existentes, mas quando combinadas com a heurística aditiva *lifted* (h_Ladd) em um sistema semelhante ao LAMA instanciado, superam todas as demais configurações avaliadas.
- **Relação com a dissertação de 2010:** estende a família de heurísticas baseadas em marcos (*landmarks*), relevante para **A2** (técnicas promissoras, embora landmarks não seja listada nominalmente) e **A6** (taxonomia), mostrando uma linha de evolução técnica (marcos aplicados ao cenário *lifted*, não apenas instanciado) que **detalha e atualiza** a taxonomia de 2010 (F4), a qual não distingue entre planejamento instanciado e *lifted* nem entre subtécnicas de marcos.

## Pontos relevantes para o projeto

- Evidencia que planejamento *lifted* (sem instanciação total do domínio) é uma direção de pesquisa ativa em 2022, dimensão ausente do escopo original de HADDAD (2010), que trabalha com PDDL processado por planejadores que assumem instanciação.
- A combinação de marcos com heurística aditiva "*similar to the grounded LAMA planning system*" reforça que LAMA/derivados continuam sendo referência de desempenho mesmo em 2022, o que é relevante para reavaliar a persistência das "técnicas promissoras" de A2 ao longo do tempo (indiretamente ligado a Q1).

## Trechos literais

- "Lifted heuristic search planning has been neglected but is currently taking up speed. Landmarks are a natural candidate for the design of heuristics in this setting, and our results clearly show their promise." (seção 6, Conclusion)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://www.ijcai.org/proceedings/2022/0647.pdf (resumo, introdução e conclusão). Conferência humana: pendente.
