# Controle de qualidade do Coordenador (Fase 1)

Conferências feitas pelo Coordenador (Claude Code, claude-opus-5) sobre o trabalho dos subagentes, em 22/09/2026. Cada linha diz o que foi conferido, contra qual fonte e o resultado. Serve para o autor saber o que já passou por uma segunda leitura e o que não passou.

| Onda | O que foi conferido | Fonte | Resultado |
|---|---|---|---|
| 1 | Amostra aleatória de 32 dos 317 itens da lista bruta (semente 20260922) | Crossref por DOI; página do arXiv | 31 conferem; 1 não conferido (URL do OpenAlex bloqueada pela cota). Nenhum item inventado |
| 2 | Todos os 14 "talvez"; as 76 decisões de prioridade A; amostra de 45 outras decisões | Resumos e justificativas | "Talvez" resolvidos; E7-021 rebaixado de A para B; E1-033 excluído por teto; exclusões por redundância recodificadas de X2/X6 para X7 (90 linhas) |
| 3 | Todas as 115 entradas do `candidatas.bib` com DOI | Crossref (título, ano, primeiro autor) | 104 conferem de primeira; 6 falsos alarmes (subtítulo em campo separado, autoria malformada no Crossref, tese sem ano); 4 DOIs com `\_` escapado corrigidos; DeepSeek-R1: autor coletivo removido e chave trocada para `guo2025deepseekr1` |
| 3 | As 19 entradas só com arXiv | API do arXiv (título, primeiro autor) | Todas conferem |
| 3 | MetaGPT: autor "Jonathan Chen" (anais) × "Jiaqi Chen" (arXiv) | proceedings.iclr.cc | Anais do ICLR 2024 trazem "Chen, Jonathan"; o BibTeX segue a versão publicada. **Para o autor:** divergência entre as duas fontes |
| 3 | GIPO (E6-019) | Relatório do verificador | Só fontes secundárias; rebaixado para `divergente` e fora do `.bib` |
| 3 | 4 obras da busca de lacunas | Crossref e arXiv (feito pelo próprio Coordenador) | Verificadas; 2 autores faltantes na busca (Hutter; Kumar); L1-003 tem versão publicada (CAIN 2026) |
| 4 | `silver2024generalized`: Forest 1,00 e Miconic 0,01 | PDF do arXiv 2305.11014, Tabela 1 | Conferem. Deslize na nota: fala em "revisão de 2025" (é 2026) |
| 4 | `helmert2006fast`: "Fast Downward is a heuristic progression planner" | Texto do artigo no JAIR | Confere literalmente |
| 4 | `ferber2022neural`: Storage, hBoot ~90% × LAMA 39% × hFF 48% | PDF da AAAI 2022 | O texto do artigo diz "almost 90% ... only 39% for LAMA and 48% for hFF"; **a tabela do próprio artigo dá 38 para o LAMA**. Inconsistência interna do artigo, não da nota |
| 4 | `becker2025measuring`: IA aumenta o tempo de conclusão em 19% | PDF do arXiv (texto extraído) | Confere ("allowing AI actually increases completion time by 19%") |
| 4 | **PDFs fornecidos pelo autor (22/09/2026)** para as duas obras sem acesso nenhum: Lawrence & Lorsch (1967) e o artigo do itSIMPLE de 2005 | Os próprios PDFs | Notas escritas pelo Coordenador a partir do texto integral. Lawrence & Lorsch: páginas 1–47 confirmadas (o Crossref trazia só "1"); corrigido no `.bib`. O PDF do itSIMPLE **não é** `tonidandel2006reading`, e sim `vaquero2005itsimple` (E6-003), que a triagem havia excluído como versão superada — **exclusão revertida**, agora prioridade A: o artigo declara em 2005 o objetivo de classificar características de domínio para escolher a técnica, antecedente direto da pergunta de 2010, e documenta as classes auxiliares da ferramenta (achado G2). `tonidandel2006reading` continua sem acesso |
| 4 | `vallati2019robustness`: a nota foi feita sobre uma versão de *workshop* (KEPS 2020), mas o `.bib` registra a versão do K-CAP 2019 (ACM, paga) | Relatório do leitor E5E6-BC | **Divergência entre o texto lido e a obra citada.** Antes de usar qualquer afirmação dessa nota no texto, conferir na versão do K-CAP |
| 4 | `vallati2016identifying`: nota feita sobre a versão do ICAPS 2015; o `.bib` registra a de periódico (Fundamenta Informaticae, 2016) | Relatório do leitor E1E2-BC | Mesma situação de `vallati2019robustness`: conferir antes de citar |
| 4 | `nunez2015automatic` (E1-022): sem acesso ao texto nem ao resumo (ScienceDirect 403; resumo suprimido no Crossref, no Semantic Scholar e no Unpaywall) | Relatório do leitor E1E2-BC | **Sem nota de leitura.** Obra verificada nos metadados, mas não lida; precisa de acervo institucional |
| 4 | Instalação do Ghostscript (`brew install ghostscript`) por um leitor, para converter PostScript do JAIR | Relatório do leitor E3E4-A1 | **Fora do combinado** (nenhum agente devia instalar programas). Inofensivo e reversível (`brew uninstall ghostscript`); os prompts seguintes proíbem instalação |

## Onda 6 — crítica do rascunho do capítulo

O parecer adversarial (`redacao/capitulos/02-fundamentos-critica.md`) levantou 9 achados: 1 crítico, 4 sérios, 4 menores. O Coordenador conferiu cada um contra as sínteses e as notas e **aceitou todos**, aplicando as correções no rascunho em 23/09/2026:

| ID | O que era | Correção aplicada |
|---|---|---|
| CRI-001 (crítico) | O capítulo dizia que "nenhuma obra revisada" aplicou seleção de algoritmos a planejamento, contradizendo a própria seção anterior | Escopo restrito ao meta-aprendizado e à *Instance Space Analysis* de Smith-Miles e Vanschoren, com remissão explícita ao corpo de portfólios já tratado |
| CRI-002 (sério) | Atribuição trocada: qualidade estática de código citada como estatística de desempenho passado | Citações redistribuídas entre `zhou2026agentasarouter`, `son2026swerouter` e `madeyski2026triage` |
| CRI-003 (sério) | Delfi descrito como CNN sobre grafo | Corrigido para grafo → imagem em escala de cinza → CNN, conferido na nota primária |
| CRI-007 (sério) | Comparação de magnitude com 2010 sem termo de comparação | Trocada por comparação qualitativa, dizendo que o capítulo não reporta a magnitude de 2010 |
| CRI-004, CRI-005, CRI-006, CRI-008, CRI-009 (menores) | Condição omitida em Domshlak & Nazarenko; "menos da metade" impreciso; hedge "quase certamente" removido; erro aritmético (treze × quinze anos entre a IPC 2008 e a IPC 2023); aspas em tradução livre | Todas corrigidas. O erro aritmético vinha da síntese E3, também corrigida. As traduções passaram a trazer o original em inglês entre aspas |

O parecer também registra que a fidelidade do rascunho às fontes é alta e que nenhum problema exigiu nova busca bibliográfica.

## Pendências tratadas em 23/09/2026

| Pendência | Resolução |
|---|---|
| `vallati2019robustness`: nota feita na versão KEPS 2020, citação ao K-CAP 2019 | **Resolvida.** A cópia do KEPS 2020 declara, na nota de rodapé do título, que o artigo foi publicado nos anais da K-CAP 2019. É republicação do mesmo texto; a citação ao K-CAP fica mantida |
| `vallati2016identifying`: nota feita na versão ICAPS 2015, citação ao periódico de 2016 | **Resolvida.** Citação trocada para a versão lida (ICAPS 2015, DOI 10.1609/icaps.v25i1.13715, BibTeX do doi.org). Chave nova: `vallati2015identifying`, atualizada em notas, sínteses, capítulo, triagem e verificação |
| `nunez2015automatic` sem acesso | O OpenAlex e o Unpaywall indicam **acesso aberto no ScienceDirect** (acervo aberto do *Artificial Intelligence*); o bloqueio era contra robôs. Download precisa ser feito pelo autor num navegador |
