# Plano de escrita da dissertação revisada (Fase 6)

Decisões do autor em 28/09/2026 (plano, seção 10): a IA redige a dissertação inteira; o autor revisa e ajusta depois de **02/10/2026**, prazo da escrita; formatação pelo guia da FEI (`redacao/README.md`); a Fase 4B entra no capítulo 5; declaração de uso de IA no modelo do autor.

## Regras de redação

- **Fonte de cada afirmação:** relatórios das fases e registros de experimento (`experimentos/execucoes/EXP-nn`). Nenhum número sem origem: cada número leva, ao lado, um comentário `<!-- fonte: arquivo -->` para a verificação final.
- **Citações:** só chaves do `literatura/referencias/referencias.bib`, conferidas por `literatura/scripts/checar_citacoes.py`. Uso de cada obra conferido na nota de leitura.
- **Fato × hipótese:** as marcas `[FATO]`/`[HIPÓTESE]` saem do texto; a distinção passa para a redação (afirmação, conjectura, limitação).
- **Registro acadêmico:** português do Brasil, terceira pessoa ou voz impessoal, sem primeira pessoa; termos técnicos em itálico no original (*features*, *single best*). Nada do estilo de artigos e posts do autor.
- **Formatação:** títulos com `#` a `#####` (a numeração vem da montagem); tabela com legenda `: Título` e, embaixo, `::: fonte` com "Fonte: Autor." ou a origem; quadro dentro de `::: quadro`; figura com `![Título](arquivo)`, sempre seguida de `::: fonte`.
- **Montagem:** `uv run --no-project --with python-docx python redacao/montagem/montar.py` → `redacao/saida/dissertacao-haddad-2026.docx`. Sumário, listas e números de página se atualizam ao abrir no Word.

## Cronograma

| Dia | Entrega |
|---|---|
| 28/09 (seg) | Padrão FEI montado (modelo, CSL, filtro, script); plano de escrita; **capítulo 4 (Método)** — feito |
| 29/09 (ter) | **Capítulo 5 (Resultados)**: Fase 3 e Fase 4B |
| 30/09 (qua) | **Capítulo 6 (LLMs)** e **capítulo 7 (Ponte)** |
| 01/10 (qui) | **Capítulos 1, 2 e 3** atualizados; **capítulo 8**; apêndices |
| 02/10 (sex) | Resumo e *abstract*; lista de siglas; verificação de todas as citações e números; revisão de consistência entre capítulos; montagem final; entrega ao autor |

Depois de 02/10: revisão e ajustes do autor; confirmar título, natureza, ficha catalográfica e folha de aprovação; declaração de IA válida só então; M3.

## Roteiro por capítulo

### 1 Introdução (reescrever `01-introducao.md`)
Motivação (a pergunta de 2010 e o que mudou); objetivo da revisão; perguntas Q1 a Q5 (Q4 exploratória); contribuições, agora com os resultados; método em resumo (auditoria, replicação em quatro níveis, IPCs, LLMs, ponte); estrutura do trabalho. Fontes: plano (seções 1 e 5), relatórios das Fases 1 a 5.

### 2 Fundamentos e estado da arte (atualizar `02-fundamentos.md`)
Manter a revisão (Fase 1); ajustar a síntese final ao que as Fases 3 a 5 mostraram (nesses dados, nenhum seletor supera o *single best*, nem por domínio nem por instância); remissões aos capítulos 5 a 7.

### 3 Revisitando 2010: auditoria (atualizar `03-revisitando-2010.md`)
Manter a auditoria (Fase 2); remissão aos achados G22 a G26 no capítulo 4; conferir números contra `auditoria/afirmacoes.csv`.

### 4 Método (novo, `04-metodo.md`)
1. Visão geral: perguntas × níveis × dados (quadro).
2. O experimento de 2010 como objeto: dados (tabelas publicadas, 13 domínios, 10 planejadores, 17 métricas), fonte de verdade, correções aprovadas (G11, G12), duas populações de dados (G21). Fontes: `data/2010/README.md`, `auditoria/condicoes-de-execucao-2010.md`.
3. Taxonomia de técnicas em quatro dimensões: dimensões, codificação dos 10 e dos 29 planejadores, regra dos portfólios, extensão aos LLMs. Fontes: `auditoria/taxonomia-tecnicas.md`, `auditoria/taxonomia/*.csv`.
4. Níveis 1 e 2: reprodução por script e correções (discretização, taxonomia, rótulos, classes auxiliares, perda × *virtual best*, linha de base). Fontes: EXP-03, EXP-04, EXP-06, EXP-08 a EXP-10.
5. Nível 3: reexecução dos planejadores de 2010 (ambiente, calibração do limite, conjunto de instâncias, medidas: cobertura, qualidade, tempo, memória). Fontes: EXP-01, EXP-02, EXP-05, EXP-19, EXP-20, EXP-22.
6. Nível 4: ampliação com dados publicados (Planner Museum, Autoscale, 41 domínios, 29 planejadores). Fontes: EXP-12, EXP-13, `experimentos/nivel4-proposta.md`.
7. Características extraídas do PDDL: métricas de 2010 a partir do PDDL, *features* SAS+, topologia de busca. Fontes: EXP-07, EXP-11, `experimentos/extratores/README.md`, EXP-25.
8. IPCs 2011 e 2018 (Fase 4B): fontes, recorte, dataset, validação contra os placares oficiais. Fontes: `docs/resultados-ipc-2011-2023.md`, `docs/fase4b-desenho.md`, `data/ipc-2011-2023/README.md`, EXP-21, EXP-24.
9. Seletores e validação: método de 2010, kNN, *random forest*, *single best*, *virtual best*, *leave-one-domain-out*, Wilcoxon com correção de Holm.
10. Limitações do experimento original (G22 a G26) e desta revisão (controle de serialização dispensado; validação de 2010 não reexecutada; só cobertura no Nível 4).

### 5 Resultados experimentais (novo, `05-resultados.md`)
1. O método de 2010 reproduzido (Nível 1). 2. Correções e linha de base (Nível 2). 3. Reexecução (Nível 3): cobertura, notas homogêneas, qualidade, tempo e memória. 4. Ampliação (Nível 4): seletores × *single best*; mapa por técnica; planejadores antigos que ainda vencem. 5. Métricas de modelagem × *features* modernas (Q2), com a ligação ao X2. 6. IPCs 2011 e 2018 (Q5): mapa característica × técnica; *features* SAS+ e topologia; seleção por instância (R-29). 7. Respostas a Q1, Q2 e Q5. Fontes: `experimentos/relatorio-fase3.md`, `experimentos/relatorio-fase4b.md` e registros.

### 6 LLMs no mapa das técnicas (novo, `06-llms.md`)
1. Desenho dos experimentos (modelos, parâmetros, custo). 2. Como seletor (X3, com e sem nomes). 3. Como planejador (X1) e com nomes ofuscados (EXP-23). 4. Com verificador (X4). 5. Como tradutor (X2). 6. Posição na taxonomia; resposta a Q3; limites. Fonte: `llm/relatorio-fase4.md` e EXP-14 a EXP-18, EXP-23.

### 7 Do domínio de planejamento ao desenvolvimento de software apoiado por IA (novo, `07-ponte-software.md`)
A partir de `ponte-software/relatorio/dossie-capitulo-7.md` e da síntese exploratória: analogia e seus limites; o que se transfere da 4B e o que não; triagem, escalonamento e orquestração; hipóteses H1 a H3 e desenhos empíricos; tudo como hipótese.

### 8 Conclusões e próximos passos (novo, `08-conclusoes.md`)
O que se sustenta de 2010 e o que não; respostas a Q1 a Q5; contribuições; limitações; trabalhos futuros.

### Apêndices (`10-apendices.md`)
A – Codificação dos planejadores na taxonomia em quatro dimensões. B – Registro dos experimentos (EXP-01 a EXP-25) com o script e os dados de cada um. C – Reprodutibilidade: repositório, ambientes e comandos.
