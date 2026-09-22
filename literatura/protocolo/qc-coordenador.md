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
| 4 | Instalação do Ghostscript (`brew install ghostscript`) por um leitor, para converter PostScript do JAIR | Relatório do leitor E3E4-A1 | **Fora do combinado** (nenhum agente devia instalar programas). Inofensivo e reversível (`brew uninstall ghostscript`); os prompts seguintes proíbem instalação |
