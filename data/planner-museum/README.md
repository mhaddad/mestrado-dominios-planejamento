# Planner Museum: cobertura publicada por domínio

**Origem:** Tabela 1 do material suplementar de Lequen et al. (2026), *Planner Museum: Evaluating Classical Planners Over Time*, ICAPS 2026 (`lequen2026planner` no `referencias.bib`). Arquivo `supplementary.pdf` do registro Zenodo 10.5281/zenodo.17861051 (versão 19136146, publicada em 20/03/2026), baixado em 26/09/2026.

**Método de obtenção:** texto extraído do PDF com `pypdf`. As linhas da Tabela 1 foram lidas por expressão regular (nome do domínio seguido de 29 inteiros), agrupadas pela IPC de origem que a tabela indica. **Conferência:** a soma de cada uma das 29 colunas é igual à linha "Total" publicada.

**Conteúdo:** `cobertura_por_dominio.csv`, com 42 linhas (domínios) e 29 colunas de planejadores. Cada valor é o número de instâncias resolvidas, de 30 por domínio.

**Condições do experimento original (texto do artigo):**
- *benchmarks* Autoscale com custo unitário;
- cluster Intel Xeon Gold 6130;
- 4 GiB de memória e 30 minutos por instância.

Domínios introduzidos na IPC 2023 não estão incluídos.

**Siglas dos planejadores:** na ordem da tabela, BB2 (Blackbox 2), HSP, IPP, FF, HSP2, MIPS, SysR (System R), LPG, SimP (SimPlanner), FD (Fast Downward 2004), FDD (Fast Diagonally Downward), MIPSXXL, C3, FFSA, LAMA08, FDSS11, LAMA11, Probe, Merc (Mercury), MpC (Madagascar), YAHSP (YAHSP3, IPC 2014), FDRemix, LAPKT (BFWS), Saar (Saarplan), ANS, DecS (DecStar), FDSS23, Levitron, Maidu (Scorpion Maidu).

**Observações:**
- O Pathways tem cobertura 0 para todos os 29 planejadores. A causa não é explicada na tabela e está `[A CONFIRMAR]`.
- O YAHSP da tabela é a versão de 2014, não a de 2010.
- O repositório do artefato (`github.com/mrlab-ai/planner-museum`, tag `icaps-2026`) não tem arquivo de licença. Os dados aqui são só a tabela publicada, citada com a fonte.
