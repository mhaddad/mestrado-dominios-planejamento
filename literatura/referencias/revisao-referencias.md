# Revisão das referências (promoção para o `referencias.bib`)

Preparado pelo Coordenador em 23/09/2026. **Decisão do autor (23/09/2026):** as referências são revisadas diretamente neste arquivo, sem Zotero.

## Como usar

1. Leia cada referência formatada (estilo ABNT, variante UFPR). Confira autor, título, veículo e ano. Se algo estiver errado, **não corrija aqui**: anote ao lado da linha, e o `.bib` é corrigido na fonte (`candidatas.bib`) antes de promover.
2. `[x]` = promover para o `referencias.bib`; `[ ]` = não promover.
   - As **122 confirmadas** vêm marcadas: desmarque só o que rejeitar.
   - As **29 com ressalva** vêm desmarcadas: marque as que aceitar. A seção 1 diz o motivo de cada ressalva e quantas vezes a obra é citada nas sínteses e no capítulo — uma obra com ressalva que sustenta argumento do capítulo merece atenção.
3. Rode `python3 literatura/scripts/promover_referencias.py`. Ele lê as marcas deste arquivo e gera o `referencias.bib`.

Critérios da confirmação: revisão por pares; impacto medido pelo percentil de citação normalizado por área e ano (OpenAlex, 23/09/2026); peso do veículo; ausência de retratação (nenhuma das 155 obras está retratada); e leitura efetiva da obra. Detalhe em `literatura/protocolo/protocolo-busca.md`, seção 9.

**Fora desta revisão:** `nunez2015automatic`, `sette2008are` e `tonidandel2006reading` (não lidas por falta de acesso; não citáveis) e `simpson2001gipo` (excluída).

---

## 1. Com ressalva — decidir (29)

- [ ] `delarosa2017performance` — DE LA ROSA, T.; CENAMOR, I.; FERNÁNDEZ, F. Performance Modelling of Planners from Homogeneous Problem Sets. Proceedings of the International Conference on Automated Planning and Scheduling, v. 27, p. 425–433, 2017. AAAI Press. Disponível em: <https://doi.org/10.1609/icaps.v27i1.13848>.
  - **Ressalva:** revisada por pares, mas baixo impacto (percentil de citação 0.11; 2 citações); não sustentar sozinha um argumento central
  - Eixo E2, prioridade A · citada 14× nas sínteses e **5× no capítulo**
- [ ] `valmeekam2024llms` — VALMEEKAM, K.; STECHLY, K.; KAMBHAMPATI, S. LLMs Still Can’t Plan; Can LRMs? A Preliminary Evaluation of OpenAI’s o1 on PlanBench., 2024. Disponível em: <https://arxiv.org/abs/2409.13373>.
  - **Ressalva:** preprint pouco citado (6 citações) sem versão revisada; não usar como evidência central
  - Eixo E5, prioridade A · citada 16× nas sínteses e **4× no capítulo**
- [ ] `zhou2026agentasarouter` — ZHOU, P.; TANG, Z.; MA, Y.; et al. Agent-as-a-Router: Agentic Model Routing for Coding Tasks., 2026. Disponível em: <https://arxiv.org/abs/2606.22902>.
  - **Ressalva:** preprint recente (fronteira, sem tempo para revisão/citações); usar como evidência complementar e marcado como preprint
  - Eixo E8, prioridade A · citada 13× nas sínteses e **4× no capítulo**
- [ ] `liu2023llmp` — LIU, B.; JIANG, Y.; ZHANG, X.; et al. LLM+P: Empowering Large Language Models with Optimal Planning Proficiency., 2023. Disponível em: <https://arxiv.org/abs/2304.11477>.
  - **Ressalva:** preprint sem versão revisada localizada, mas muito citado (85 citações)
  - Eixo E5, prioridade A · citada 9× nas sínteses e **3× no capítulo**
- [ ] `madeyski2026triage` — MADEYSKI, L. Triage: Routing Software Engineering Tasks to Cost-Effective LLM Tiers via Code Quality Signals., 2026. Disponível em: <https://arxiv.org/abs/2604.07494>.
  - **Ressalva:** preprint recente (fronteira, sem tempo para revisão/citações); usar como evidência complementar e marcado como preprint
  - Eixo E8, prioridade B · citada 9× nas sínteses e **3× no capítulo**
- [ ] `son2026swerouter` — SON, S.; YOON, S.; TANG, J.; et al. SWE-Router: Routing in Multi-turn Agentic Software Engineering Tasks., 2026. Disponível em: <https://arxiv.org/abs/2607.00053>.
  - **Ressalva:** preprint recente (fronteira, sem tempo para revisão/citações); usar como evidência complementar e marcado como preprint
  - Eixo E8, prioridade A · citada 8× nas sínteses e **3× no capítulo**
- [ ] `katz2018delfi` — KATZ, M.; SOHRABI, S.; SAMULOWITZ, H.; SIEVERS, S. Delfi: Online Planner Selection for Cost-Optimal Planning. International Planning Competition (IPC) 2018 – Planner Abstracts.Anais... , 2018. Disponível em: <https://ai.dmi.unibas.ch/papers/katz-et-al-ipc2018.pdf>.
  - **Ressalva:** literatura cinza oficial (resumo de planejador de IPC, resultados ou workshop); aceitável para descrever o sistema ou o resultado oficial
  - Eixo E1, prioridade A · citada 7× nas sínteses e **3× no capítulo**
- [ ] `becker2025measuring` — BECKER, J.; RUSH, N.; BARNES, E.; REIN, D. Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity., 2025. Disponível em: <https://arxiv.org/abs/2507.09089>.
  - **Ressalva:** preprint recente (fronteira, sem tempo para revisão/citações); usar como evidência complementar e marcado como preprint
  - Eixo E8, prioridade A · citada 12× nas sínteses e **2× no capítulo**
- [ ] `peng2023impact` — PENG, S.; KALLIAMVAKOU, E.; CIHON, P.; DEMIRER, M. The Impact of AI on Developer Productivity: Evidence from GitHub Copilot., 2023. Disponível em: <https://arxiv.org/abs/2302.06590>.
  - **Ressalva:** preprint sem versão revisada localizada, mas muito citado (274 citações)
  - Eixo E8, prioridade A · citada 10× nas sínteses e **2× no capítulo**
- [ ] `rintanen2014madagascar` — RINTANEN, J. Madagascar: Scalable Planning with SAT., 2014. Descrição de sistema associada à International Planning Competition 2014. Disponível em: <https://users.aalto.fi/~rintanj1/papers/Rintanen14IPC.pdf>.
  - **Ressalva:** literatura cinza oficial (resumo de planejador de IPC, resultados ou workshop); aceitável para descrever o sistema ou o resultado oficial
  - Eixo E3, prioridade A · citada 9× nas sínteses e **2× no capítulo**
- [ ] `cenamor2019insights` — CENAMOR, I.; POZANCO, A. Insights from the 2018 IPC Benchmarks. Proceedings of the Workshop on the International Planning Competition (WIPC 2019), held at ICAPS 2019.Anais... . p.8–14, 2019. Disponível em: <https://icaps19.icaps-conference.org/workshops/WIPC/proceedings.pdf>.
  - **Ressalva:** literatura cinza oficial (resumo de planejador de IPC, resultados ou workshop); aceitável para descrever o sistema ou o resultado oficial
  - Eixo E3, prioridade C · citada 8× nas sínteses e **1× no capítulo**
- [ ] `helmert2011fast` — HELMERT, M.; RÖGER, G.; KARPAS, E. Fast Downward Stone Soup: A Baseline for Building Planner Portfolios. Proceedings of the ICAPS 2011 Workshop on Planning and Learning (PAL).Anais... , 2011. Disponível em: <https://ai.dmi.unibas.ch/papers/helmert-et-al-icaps2011ws.pdf>.
  - **Ressalva:** literatura cinza oficial (resumo de planejador de IPC, resultados ou workshop); aceitável para descrever o sistema ou o resultado oficial
  - Eixo E1, prioridade A · citada 8× nas sínteses e **1× no capítulo**
- [ ] `hu2024routerbench` — HU, Q. J.; BIEKER, J.; LI, X.; et al. RouterBench: A Benchmark for Multi-LLM Routing System., 2024. Disponível em: <https://arxiv.org/abs/2403.12031>.
  - **Ressalva:** preprint pouco citado (3 citações) sem versão revisada; não usar como evidência central
  - Eixo E7, prioridade B · citada 8× nas sínteses e **1× no capítulo**
- [ ] `ferber2022explainable` — FERBER, P.; SEIPP, J. Explainable Planner Selection for Classical Planning. Proceedings of the AAAI Conference on Artificial Intelligence, v. 36, n. 9, p. 9741–9749, 2022. AAAI Press. Disponível em: <https://doi.org/10.1609/aaai.v36i9.21209>.
  - **Ressalva:** revisada por pares, mas baixo impacto (percentil de citação 0.39; 1 citações); não sustentar sozinha um argumento central
  - Eixo E1, prioridade B · citada 6× nas sínteses e **1× no capítulo**
- [ ] `seipp2014fast` — SEIPP, J.; SIEVERS, S.; HUTTER, F. Fast Downward Cedalion. International Planning Competition (IPC) 2014 – Planner Abstracts.Anais... , 2014. Disponível em: <https://mrlab.ai/papers/seipp-et-al-ipc2014b.pdf>.
  - **Ressalva:** literatura cinza oficial (resumo de planejador de IPC, resultados ou workshop); aceitável para descrever o sistema ou o resultado oficial
  - Eixo E1, prioridade A · citada 6× nas sínteses e **1× no capítulo**
- [ ] `gestrin2024nl2plan` — GESTRIN, E.; KUHLMANN, M.; SEIPP, J. NL2Plan: Robust LLM-Driven Planning from Minimal Text Descriptions., 2024. Disponível em: <https://arxiv.org/abs/2405.04215>.
  - **Ressalva:** preprint pouco citado (1 citações) sem versão revisada; não usar como evidência central
  - Eixo E6, prioridade B · citada 5× nas sínteses e **1× no capítulo**
- [ ] `jiang2026toward` — JIANG, J.; ZHANG, J.; MO, F.; LI, L.; ZENG, D. Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback., 2026. Disponível em: <https://arxiv.org/abs/2606.29700>.
  - **Ressalva:** preprint recente (fronteira, sem tempo para revisão/citações); usar como evidência complementar e marcado como preprint
  - Eixo E6, prioridade B · citada 5× nas sínteses e **1× no capítulo**
- [ ] `smirnov2024generating` — SMIRNOV, P.; JOUBLIN, F.; CERAVOLA, A.; GIENGER, M. Generating consistent PDDL domains with Large Language Models., 2024. Disponível em: <https://arxiv.org/abs/2404.07751>.
  - **Ressalva:** preprint pouco citado (1 citações) sem versão revisada; não usar como evidência central
  - Eixo E6, prioridade B · citada 5× nas sínteses e **1× no capítulo**
- [ ] `huang2025spar` — HUANG, S.; WU, Y.; SHI, G.; SUKHATME, G. S.; KUMAR, V. SPAR: Scalable LLM-based PDDL Domain Generation for Aerial Robotics., 2025. Disponível em: <https://arxiv.org/abs/2509.13691>.
  - **Ressalva:** preprint recente (fronteira, sem tempo para revisão/citações); usar como evidência complementar e marcado como preprint
  - Eixo E6, prioridade C · citada 7× nas sínteses e **0× no capítulo**
- [ ] `percassi2021improving` — PERCASSI, F.; GEREVINI, A. E.; SCALA, E.; SERINA, I.; VALLATI, M. Improving domain-independent heuristic state-space planning via plan cost predictions. Journal of Experimental & Theoretical Artificial Intelligence, v. 35, n. 6, p. 849–875, 2021. Taylor & Francis. Disponível em: <https://doi.org/10.1080/0952813x.2021.1970239>.
  - **Ressalva:** revisada por pares, mas baixo impacto (percentil de citação 0.08; 1 citações); não sustentar sozinha um argumento central
  - Eixo E2, prioridade A · citada 6× nas sínteses e **0× no capítulo**
- [ ] `ferber2019ipc` — FERBER, P.; MA, T.; HUO, S.; CHEN, J.; KATZ, M. IPC: A Benchmark Data Set for Learning with Graph-Structured Data., 2019. Disponível em: <https://arxiv.org/abs/1905.06393>.
  - **Ressalva:** preprint pouco citado (3 citações) sem versão revisada; não usar como evidência central
  - Eixo E2, prioridade B · citada 5× nas sínteses e **0× no capítulo**
- [ ] `huang2024understanding` — HUANG, X.; LIU, W.; CHEN, X.; et al. Understanding the planning of LLM agents: A survey., 2024. Disponível em: <https://arxiv.org/abs/2402.02716>.
  - **Ressalva:** preprint pouco citado (35 citações) sem versão revisada; não usar como evidência central
  - Eixo E5, prioridade B · citada 4× nas sínteses e **0× no capítulo**
- [ ] `ipc2008results` — INTERNATIONAL PLANNING COMPETITION. Results - IPC-2008, Deterministic Part., 2008. Página oficial de resultados, IPC-2008. Disponível em: <https://ipc08.icaps-conference.org/deterministic/Results.html>.
  - **Ressalva:** literatura cinza oficial (resumo de planejador de IPC, resultados ou workshop); aceitável para descrever o sistema ou o resultado oficial
  - Eixo E3, prioridade C · citada 3× nas sínteses e **0× no capítulo**
- [ ] `jilani2014automated` — JILANI, R.; CRAMPTON, A.; KITCHIN, D. E.; VALLATI, M. Automated Knowledge Engineering Tools in Planning: State-of-the-art and Future Challenges. Proceedings of the ICAPS 2014 Workshop on Knowledge Engineering for Planning and Scheduling (KEPS).Anais... , 2014. Disponível em: <https://eprints.hud.ac.uk/id/eprint/20380/>.
  - **Ressalva:** literatura cinza oficial (resumo de planejador de IPC, resultados ou workshop); aceitável para descrever o sistema ou o resultado oficial
  - Eixo E6, prioridade B · citada 3× nas sínteses e **0× no capítulo**
- [ ] `yang2022pg3` — YANG, R.; SILVER, T.; CURTIS, A.; LOZANO-PÉREZ, T.; KAELBLING, L. P. PG3: Policy-Guided Planning for Generalized Policy Generation. Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence (IJCAI 2022).Anais... . p.4686–4692, 2022. Disponível em: <https://doi.org/10.24963/ijcai.2022/650>.
  - **Ressalva:** revisada por pares, mas baixo impacto (percentil de citação 0.40; 1 citações); não sustentar sozinha um argumento central
  - Eixo E4, prioridade B · citada 3× nas sínteses e **0× no capítulo**
- [ ] `aghzal2025survey` — AGHZAL, M.; PLAKU, E.; STEIN, G. J.; YAO, Z. A Survey on Large Language Models for Automated Planning., 2025. Disponível em: <https://arxiv.org/abs/2502.12435>.
  - **Ressalva:** preprint recente (fronteira, sem tempo para revisão/citações); usar como evidência complementar e marcado como preprint
  - Eixo E5, prioridade C · citada 2× nas sínteses e **0× no capítulo**
- [ ] `greco2022scaling` — GRECO, M.; TORRALBA, Á.; BAIER, J. A.; PALACIOS, H. Scaling up ML-based Black-box Planning with Partial STRIPS Models., 2022. Disponível em: <https://arxiv.org/abs/2207.04479>.
  - **Ressalva:** preprint pouco citado (0 citações) sem versão revisada; não usar como evidência central
  - Eixo E4, prioridade B · citada 2× nas sínteses e **0× no capítulo**
- [ ] `pallagani2023understanding` — PALLAGANI, V.; MUPPASANI, B.; MURUGESAN, K.; et al. Understanding the Capabilities of Large Language Models for Automated Planning., 2023. Disponível em: <https://arxiv.org/abs/2305.16151>.
  - **Ressalva:** preprint pouco citado (6 citações) sem versão revisada; não usar como evidência central
  - Eixo E5, prioridade C · citada 2× nas sínteses e **0× no capítulo**
- [ ] `xie2023translating` — XIE, Y.; YU, C.; ZHU, T.; et al. Translating Natural Language to Planning Goals with Large-Language Models., 2023. Disponível em: <https://arxiv.org/abs/2302.05128>.
  - **Ressalva:** preprint pouco citado (46 citações) sem versão revisada; não usar como evidência central
  - Eixo E5, prioridade B · citada 2× nas sínteses e **0× no capítulo**

---

## 2. Confirmadas (122)


### E1 — Seleção de algoritmos e portfólios (16)

- [x] `bischl2016aslib` — BISCHL, B.; KERSCHKE, P.; KOTTHOFF, L.; et al. ASlib: A benchmark library for algorithm selection. Artificial Intelligence, v. 237, p. 41–58, 2016. Elsevier. Disponível em: <https://doi.org/10.1016/j.artint.2016.04.003>.
  - Verificação: existe versão publicada: Artificial Intelligence, vol. 237, pp. 41-58, 2016, DOI 10.1016/j.artint.2016.04.003 (registro original era o preprint arXiv, DOI 10.48550/arXiv.1506.02465, ano 2015); a versão publicada lista 11…
- [x] `cenamor2016ibacop` — CENAMOR, I.; DE LA ROSA, T.; FERNÁNDEZ, F. The IBaCoP Planning System: Instance-Based Configured Portfolios. Journal of Artificial Intelligence Research, v. 56, p. 657–691, 2016. AI Access Foundation. Disponível em: <https://doi.org/10.1613/jair.5080>.
- [x] `eggensperger2019pitfalls` — EGGENSPERGER, K.; LINDAUER, M.; HUTTER, F. Pitfalls and Best Practices in Algorithm Configuration. Journal of Artificial Intelligence Research, v. 64, p. 861–893, 2019. AI Access Foundation. Disponível em: <https://doi.org/10.1613/jair.1.11420>.
- [x] `gerevini2014planning` — GEREVINI, A.; SAETTI, A.; VALLATI, M. Planning through Automatic Portfolio Configuration: The PbP Approach. Journal of Artificial Intelligence Research, v. 50, p. 639–696, 2014. AI Access Foundation. Disponível em: <https://doi.org/10.1613/jair.4359>.
- [x] `hutter2009paramils` — HUTTER, F.; HOOS, H. H.; LEYTON-BROWN, K.; STUETZLE, T. ParamILS: An Automatic Algorithm Configuration Framework. Journal of Artificial Intelligence Research, v. 36, p. 267–306, 2009. AI Access Foundation. Disponível em: <https://doi.org/10.1613/jair.2861>.
- [x] `kerschke2019automated` — KERSCHKE, P.; HOOS, H. H.; NEUMANN, F.; TRAUTMANN, H. Automated Algorithm Selection: Survey and Perspectives. Evolutionary Computation, v. 27, n. 1, p. 3–45, 2019. MIT Press. Disponível em: <https://doi.org/10.1162/evco_a_00242>.
  - Verificação: ano registrado 2018, registro primário (Crossref, issued) 2019-03; chave corrigida de kerschke2018automated para kerschke2019automated
- [x] `kotthoff2014algorithm` — KOTTHOFF, L. Algorithm Selection for Combinatorial Search Problems: A Survey. AI Magazine, v. 35, n. 3, p. 48–60, 2014. Wiley. Disponível em: <https://doi.org/10.1609/aimag.v35i3.2460>.
- [x] `lindauer2015autofolio` — LINDAUER, M.; HOOS, H. H.; HUTTER, F.; SCHAUB, T. AutoFolio: An Automatically Configured Algorithm Selector. Journal of Artificial Intelligence Research, v. 53, p. 745–778, 2015. AI Access Foundation. Disponível em: <https://doi.org/10.1613/jair.4726>.
- [x] `lindauer2019algorithm` — LINDAUER, M.; VAN RIJN, J. N.; KOTTHOFF, L. The algorithm selection competitions 2015 and 2017. Artificial Intelligence, v. 272, p. 86–100, 2019. Elsevier. Disponível em: <https://doi.org/10.1016/j.artint.2018.10.004>.
- [x] `ma2020online` — MA, T.; FERBER, P.; HUO, S.; CHEN, J.; KATZ, M. Online Planner Selection with Graph Neural Networks and Adaptive Scheduling. Proceedings of the AAAI Conference on Artificial Intelligence, v. 34, n. 04, p. 5077–5084, 2020. AAAI Press. Disponível em: <https://doi.org/10.1609/aaai.v34i04.5949>.
- [x] `rice1976algorithm` — RICE, J. R. The Algorithm Selection Problem. Advances in Computers. v. 15, p.65–118, 1976. Elsevier. Disponível em: <https://doi.org/10.1016/S0065-2458(08)60520-3>.
- [x] `sievers2019deep` — SIEVERS, S.; KATZ, M.; SOHRABI, S.; SAMULOWITZ, H.; FERBER, P. Deep Learning for Cost-Optimal Planning: Task-Dependent Planner Selection. Proceedings of the AAAI Conference on Artificial Intelligence, v. 33, n. 01, p. 7715–7723, 2019. AAAI Press. Disponível em: <https://doi.org/10.1609/aaai.v33i01.33017715>.
- [x] `vallati2015portfolio` — VALLATI, M.; CHRPA, L.; KITCHIN, D. Portfolio-based planning: State of the art, common practice and open challenges. AI Communications, v. 28, n. 4, p. 717–733, 2015. IOS Press. Disponível em: <https://doi.org/10.3233/AIC-150671>.
- [x] `vallati2018what` — VALLATI, M.; CHRPA, L.; MCCLUSKEY, T. L. What you always wanted to know about the deterministic part of the International Planning Competition (IPC) 2014 (but were too afraid to ask). The Knowledge Engineering Review, v. 33, 2018. Cambridge University Press. Disponível em: <https://doi.org/10.1017/S0269888918000012>.
- [x] `vatter2026beyond` — VATTER, J.; MAYER, R.; JACOBSEN, H.-A.; SAMULOWITZ, H.; KATZ, M. Beyond Message Passing: Modern GNN Architectures for Online Planner Selection. Proceedings of the International Conference on Automated Planning and Scheduling, v. 36, n. 1, p. 351–360, 2026. AAAI Press. Disponível em: <https://doi.org/10.1609/icaps.v36i1.42845>.
- [x] `xu2008satzilla` — XU, L.; HUTTER, F.; HOOS, H. H.; LEYTON-BROWN, K. SATzilla: Portfolio-based Algorithm Selection for SAT. Journal of Artificial Intelligence Research, v. 32, p. 565–606, 2008. AI Access Foundation. Disponível em: <https://doi.org/10.1613/jair.2490>.

### E2 — Features e predição de desempenho (12)

- [x] `domshlak2013complexity` — DOMSHLAK, C.; NAZARENKO, A. The Complexity of Optimal Monotonic Planning: The Bad, The Good, and The Causal Graph. Journal of Artificial Intelligence Research, v. 48, p. 783–812, 2013. AI Access Foundation. Disponível em: <https://doi.org/10.1613/jair.4145>.
- [x] `fawcett2014improved` — FAWCETT, C.; VALLATI, M.; HUTTER, F.; et al. Improved Features for Runtime Prediction of Domain-Independent Planners. Proceedings of the International Conference on Automated Planning and Scheduling, v. 24, p. 355–359, 2014. AAAI Press. Disponível em: <https://doi.org/10.1609/icaps.v24i1.13680>.
- [x] `helmert2009concise` — HELMERT, M. Concise finite-domain representations for PDDL planning tasks. Artificial Intelligence, v. 173, n. 5-6, p. 503–535, 2009. Elsevier. Disponível em: <https://doi.org/10.1016/j.artint.2008.10.013>.
- [x] `hoffmann2011analyzing` — HOFFMANN, J. Analyzing Search Topology Without Running Any Search: On the Connection Between Causal Graphs and h+h^+. Journal of Artificial Intelligence Research, v. 41, p. 155–229, 2011. AI Access Foundation. Disponível em: <https://doi.org/10.1613/jair.3276>.
- [x] `hutter2014algorithm` — HUTTER, F.; XU, L.; HOOS, H. H.; LEYTON-BROWN, K. Algorithm runtime prediction: Methods & evaluation. Artificial Intelligence, v. 206, p. 79–111, 2014. Elsevier. Disponível em: <https://doi.org/10.1016/j.artint.2013.10.003>.
  - Verificação: ano registrado 2013, registro primário (Crossref, issued) 2014-01 (vol. 206); chave corrigida de hutter2013algorithm para hutter2014algorithm
- [x] `leytonbrown2009empirical` — LEYTON-BROWN, K.; NUDELMAN, E.; SHOHAM, Y. Empirical hardness models: Methodology and a case study on combinatorial auctions. Journal of the ACM, v. 56, n. 4, p. 1–52, 2009. ACM. Disponível em: <https://doi.org/10.1145/1538902.1538906>.
  - Verificação: título registrado ('Empirical hardness models') é truncado; título completo no registro primário: 'Empirical hardness models: Methodology and a case study on combinatorial auctions'
- [x] `munoz2017instance` — MUÑOZ, M. A.; VILLANOVA, L.; BAATAR, D.; SMITH-MILES, K. Instance spaces for machine learning classification. Machine Learning, v. 107, n. 1, p. 109–147, 2017. Springer. Disponível em: <https://doi.org/10.1007/s10994-017-5629-5>.
  - Verificação: publicado online (issued) em 28/12/2017, ano usado como referência (compatível com o registrado); edição impressa saiu em janeiro de 2018
- [x] `odense2022neural` — ODENSE, S.; GUPTA, K.; MACREADY, W. G. Neural-Guided Runtime Prediction of Planners for Improved Motion and Task Planning with Graph Neural Networks. 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS).Anais... . p.12471–12478, 2022. IEEE. Disponível em: <https://doi.org/10.1109/iros47612.2022.9981823>.
- [x] `roberts2009learning` — ROBERTS, M.; HOWE, A. Learning from planner performance. Artificial Intelligence, v. 173, n. 5-6, p. 536–561, 2009. Elsevier. Disponível em: <https://doi.org/10.1016/j.artint.2008.11.009>.
  - Verificação: ano registrado 2008, registro primário (Crossref, issued) 2009-04 (vol. 173, n. 5-6); chave corrigida de roberts2008learning para roberts2009learning; PDF em cs.colostate.edu encontrado na busca por texto integral é um a…
- [x] `shen2020learning` — SHEN, W.; TREVIZAN, F.; THIÉBAUX, S. Learning Domain-Independent Planning Heuristics with Hypergraph Networks. Proceedings of the International Conference on Automated Planning and Scheduling, v. 30, p. 574–584, 2020. AAAI Press. Disponível em: <https://doi.org/10.1609/icaps.v30i1.6754>.
- [x] `vallati2014asap` — VALLATI, M.; CHRPA, L.; KITCHIN, D. ASAP: An Automatic Algorithm Selection Approach for Planning. International Journal on Artificial Intelligence Tools, v. 23, n. 06, p. 1460032, 2014. World Scientific. Disponível em: <https://doi.org/10.1142/s021821301460032x>.
- [x] `vallati2015identifying` — VALLATI, M.; SERINA, I.; SAETTI, A.; GEREVINI, A. Identifying and Exploiting Features for Effective Plan Retrieval in Case-Based Planning. Proceedings of the International Conference on Automated Planning and Scheduling.Anais... . v. 25, p.239–243, 2015. Association for the Advancement of Artificial Intelligence (AAAI). Disponível em: <http://dx.doi.org/10.1609/icaps.v25i1.13715>.
  - Verificação: título registrado incluía a anotação '(versão de periódico)', que não faz parte do título real, apenas 'Identifying and Exploiting Features for Effective Plan Retrieval in Case-Based Planning' | Coordenador 23/09/2026: c…

### E3 — Planejadores, heurísticas e IPCs (15)

- [x] `bocchese2018performance` — BOCCHESE, A. F.; FAWCETT, C.; VALLATI, M.; GEREVINI, A. E.; HOOS, H. H. Performance robustness of AI planners in the 2014 International Planning Competition. AI Communications, v. 31, n. 6, p. 445–463, 2018. Disponível em: <https://doi.org/10.3233/aic-170537>.
- [x] `coles2012survey` — COLES, A.; COLES, A.; OLAYA, Á. G.; et al. A Survey of the Seventh International Planning Competition. AI Magazine, v. 33, n. 1, p. 83–88, 2012. Disponível em: <https://doi.org/10.1609/aimag.v33i1.2392>.
- [x] `helmert2006fast` — HELMERT, M. The Fast Downward Planning System. Journal of Artificial Intelligence Research, v. 26, p. 191–246, 2006. Disponível em: <https://doi.org/10.1613/jair.1705>.
- [x] `helmert2009landmarks` — HELMERT, M.; DOMSHLAK, C. Landmarks, Critical Paths and Abstractions: What’s the Difference Anyway? Proceedings of the International Conference on Automated Planning and Scheduling, v. 19, p. 162–169, 2009. Disponível em: <https://doi.org/10.1609/icaps.v19i1.13370>.
- [x] `helmert2014merge` — HELMERT, M.; HASLUM, P.; HOFFMANN, J.; NISSIM, R. Merge-and-Shrink Abstraction: A Method for Generating Lower Bounds in Factored State Spaces. Journal of the ACM, v. 61, n. 3, p. 1–63, 2014. Disponível em: <https://doi.org/10.1145/2559951>.
  - Verificação: título registrado omite o subtítulo; título completo no registro primário (Crossref/JACM): "Merge-and-Shrink Abstraction: A Method for Generating Lower Bounds in Factored State Spaces"
- [x] `lequen2026planner` — LEQUEN, A.; JOERGENSEN, O.; PHUNG, W.; et al. Planner Museum: Evaluating Classical Planners Over Time. Proceedings of the International Conference on Automated Planning and Scheduling, v. 36, n. 1, p. 393–398, 2026. Disponível em: <https://doi.org/10.1609/icaps.v36i1.42852>.
- [x] `lipovetzky2012width` — LIPOVETZKY, N.; GEFFNER, H. Width and Serialization of Classical Planning Problems. ECAI 2012 – Proceedings of the 20th European Conference on Artificial Intelligence.Anais... , 2012. IOS Press. Disponível em: <https://doi.org/10.3233/978-1-61499-098-7-540>.
  - Verificação: metadados de autoria no Crossref vêm sem separação nome/sobrenome ("Lipovetzky Nir", "Geffner Hector"); correspondem a Nir Lipovetzky e Hector Geffner, consistentes com o registro
- [x] `lipovetzky2017bestfirst` — LIPOVETZKY, N.; GEFFNER, H. Best-First Width Search: Exploration and Exploitation in Classical Planning. Proceedings of the AAAI Conference on Artificial Intelligence, v. 31, n. 1, 2017. Disponível em: <https://doi.org/10.1609/aaai.v31i1.11027>.
- [x] `richter2010lama` — RICHTER, S.; WESTPHAL, M. The LAMA Planner: Guiding Cost-Based Anytime Planning with Landmarks. Journal of Artificial Intelligence Research, v. 39, p. 127–177, 2010. Disponível em: <https://doi.org/10.1613/jair.2972>.
- [x] `rintanen2012planning` — RINTANEN, J. Planning as satisfiability: Heuristics. Artificial Intelligence, v. 193, p. 45–86, 2012. Disponível em: <https://doi.org/10.1016/j.artint.2012.08.001>.
- [x] `seipp2020saturated` — SEIPP, J.; KELLER, T.; HELMERT, M. Saturated Cost Partitioning for Optimal Classical Planning. Journal of Artificial Intelligence Research, v. 67, 2020. Disponível em: <https://doi.org/10.1613/jair.1.11673>.
- [x] `sievers2016analysis` — SIEVERS, S.; WEHRLE, M.; HELMERT, M. An Analysis of Merge Strategies for Merge-and-Shrink Heuristics. Proceedings of the International Conference on Automated Planning and Scheduling, v. 26, p. 294–298, 2016. Disponível em: <https://doi.org/10.1609/icaps.v26i1.13763>.
- [x] `taitler2024international` — TAITLER, A.; ALFORD, R.; ESPASA, J.; et al. The 2023 International Planning Competition. AI Magazine, v. 45, n. 2, p. 280–296, 2024. Disponível em: <https://doi.org/10.1002/aaai.12169>.
- [x] `torralba2017efficient` — TORRALBA, Á.; ALCÁZAR, V.; KISSMANN, P.; EDELKAMP, S. Efficient symbolic search for cost-optimal planning. Artificial Intelligence, v. 242, p. 52–79, 2017. Disponível em: <https://doi.org/10.1016/j.artint.2016.10.001>.
- [x] `wichlacz2022landmark` — WICHLACZ, J.; HÖLLER, D.; HOFFMANN, J. Landmark Heuristics for Lifted Classical Planning. Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence (IJCAI 2022).Anais... . p.4665–4671, 2022. Disponível em: <https://doi.org/10.24963/ijcai.2022/647>.

### E4 — Aprendizado para planejamento (15)

- [x] `amir2008learning` — AMIR, E.; CHANG, A. Learning Partially Observable Deterministic Action Models. Journal of Artificial Intelligence Research, v. 33, p. 349–402, 2008. Disponível em: <https://doi.org/10.1613/jair.2575>.
- [x] `asai2018classical` — ASAI, M.; FUKUNAGA, A. Classical Planning in Deep Latent Space: Bridging the Subsymbolic-Symbolic Boundary. Proceedings of the AAAI Conference on Artificial Intelligence, v. 32, n. 1, 2018. Disponível em: <https://doi.org/10.1609/aaai.v32i1.12077>.
- [x] `bonet2019learninga` — BONET, B.; FRANCÈS, G.; GEFFNER, H. Learning Features and Abstract Actions for Computing Generalized Plans. Proceedings of the AAAI Conference on Artificial Intelligence, v. 33, n. 01, p. 2703–2710, 2019. Disponível em: <https://doi.org/10.1609/aaai.v33i01.33012703>.
- [x] `chen2024learning` — CHEN, D. Z.; THIÉBAUX, S.; TREVIZAN, F. Learning Domain-Independent Heuristics for Grounded and Lifted Planning. Proceedings of the AAAI Conference on Artificial Intelligence, v. 38, n. 18, p. 20078–20086, 2024. Disponível em: <https://doi.org/10.1609/aaai.v38i18.29986>.
- [x] `chen2024return` — CHEN, D. Z.; TREVIZAN, F.; THIÉBAUX, S. Return to Tradition: Learning Reliable Heuristics with Classical Machine Learning. Proceedings of the International Conference on Automated Planning and Scheduling, v. 34, p. 68–76, 2024. Disponível em: <https://doi.org/10.1609/icaps.v34i1.31462>.
- [x] `ferber2022neural` — FERBER, P.; GEISSER, F.; TREVIZAN, F.; HELMERT, M.; HOFFMANN, J. Neural Network Heuristic Functions for Classical Planning: Bootstrapping and Comparison to Other Methods. Proceedings of the International Conference on Automated Planning and Scheduling, v. 32, p. 583–587, 2022. Disponível em: <https://doi.org/10.1609/icaps.v32i1.19845>.
- [x] `hofmann2024learning` — HOFMANN, T.; GEFFNER, H. Learning Generalized Policies for Fully Observable Non-Deterministic Planning Domains. Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence (IJCAI 2024).Anais... . p.6733–6742, 2024. Disponível em: <https://doi.org/10.24963/ijcai.2024/744>.
- [x] `jimenez2012review` — JIMÉNEZ, S.; DE LA ROSA, T.; FERNÁNDEZ, S.; FERNÁNDEZ, F.; BORRAJO, D. A review of machine learning for automated planning. The Knowledge Engineering Review, v. 27, n. 4, p. 433–467, 2012. Disponível em: <https://doi.org/10.1017/s026988891200001x>.
- [x] `jimenez2019review` — JIMÉNEZ, S.; SEGOVIA-AGUAS, J.; JONSSON, A. A review of generalized planning. The Knowledge Engineering Review, v. 34, 2019. Disponível em: <https://doi.org/10.1017/s0269888918000231>.
- [x] `srivastava2011new` — SRIVASTAVA, S.; IMMERMAN, N.; ZILBERSTEIN, S. A new representation and associated algorithms for generalized planning. Artificial Intelligence, v. 175, n. 2, p. 615–647, 2011. Disponível em: <https://doi.org/10.1016/j.artint.2010.10.006>.
  - Verificação: ano registrado 2010; a publicação (Artificial Intelligence, v.175, n.2, p.615-647) é de fevereiro de 2011 (published-print no Crossref). O DOI carrega a data de disponibilização online (outubro de 2010), provável origem …
- [x] `stahlberg2022learninga` — STÅHLBERG, S.; BONET, B.; GEFFNER, H. Learning General Optimal Policies with Graph Neural Networks: Expressive Power, Transparency, and Limits. Proceedings of the International Conference on Automated Planning and Scheduling, v. 32, p. 629–637, 2022. Disponível em: <https://doi.org/10.1609/icaps.v32i1.19851>.
- [x] `stahlberg2023learning` — STÅHLBERG, S.; BONET, B.; GEFFNER, H. Learning General Policies with Policy Gradient Methods. Proceedings of the 20th International Conference on Principles of Knowledge Representation and Reasoning (KR 2023).Anais... . p.647–657, 2023. Disponível em: <https://doi.org/10.24963/kr.2023/63>.
- [x] `toyer2020asnets` — TOYER, S.; THIÉBAUX, S.; TREVIZAN, F.; XIE, L. ASNets: Deep Learning for Generalised Planning. Journal of Artificial Intelligence Research, v. 68, p. 1–68, 2020. Disponível em: <https://doi.org/10.1613/jair.1.11633>.
- [x] `wang2024learning` — WANG, R. X.; THIÉBAUX, S. Learning Generalised Policies for Numeric Planning. Proceedings of the International Conference on Automated Planning and Scheduling, v. 34, p. 633–642, 2024. Disponível em: <https://doi.org/10.1609/icaps.v34i1.31526>.
- [x] `zhuo2011crossdomain` — ZHUO, H. H.; YANG, Q.; PAN, R.; LI, L. Cross-Domain Action-Model Acquisition for Planning via Web Search. Proceedings of the International Conference on Automated Planning and Scheduling, v. 21, p. 298–305, 2011. Disponível em: <https://doi.org/10.1609/icaps.v21i1.13449>.

### E5 — LLMs e planejamento (14)

- [x] `guan2023leveraging` — GUAN, L.; VALMEEKAM, K.; SREEDHARAN, S.; KAMBHAMPATI, S. Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning. Advances in Neural Information Processing Systems 36 (NeurIPS 2023).Anais... . p.79081–79094, 2023. Disponível em: <https://doi.org/10.52202/075280-3459>.
  - Verificação: Existe versao publicada: NeurIPS 2023 (Advances in Neural Information Processing Systems 36), DOI 10.52202/075280-3459, p.79081-79094. BibTeX gerado a partir do DOI da versao publicada.
- [x] `guo2025deepseekr1` — GUO, D.; YANG, D.; ZHANG, H.; et al. DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning. Nature, v. 645, n. 8081, p. 633–638, 2025. Disponível em: <https://doi.org/10.1038/s41586-025-09422-z>.
  - Verificação: Coordenador: removido o autor coletivo DeepSeek-AI (vem do arXiv; a versão da Nature começa por Guo, D.); chave ajustada ao primeiro autor
- [x] `hao2023reasoning` — HAO, S.; GU, Y.; MA, H.; et al. Reasoning with Language Model is Planning with World Model. Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing.Anais... . p.8154–8173, 2023. Association for Computational Linguistics. Disponível em: <https://doi.org/10.18653/v1/2023.emnlp-main.507>.
- [x] `hazra2024saycanpay` — HAZRA, R.; ZUIDBERG DOS MARTIRES, P.; DE RAEDT, L. SayCanPay: Heuristic Planning with Large Language Models Using Learnable Domain Knowledge. Proceedings of the AAAI Conference on Artificial Intelligence, v. 38, n. 18, p. 20123–20133, 2024. Disponível em: <https://doi.org/10.1609/aaai.v38i18.29991>.
- [x] `kambhampati2024can` — KAMBHAMPATI, S. Can large language models reason and plan? Annals of the New York Academy of Sciences, v. 1534, n. 1, p. 15–18, 2024. Disponível em: <https://doi.org/10.1111/nyas.15125>.
- [x] `kambhampati2024llms` — KAMBHAMPATI, S.; VALMEEKAM, K.; GUAN, L.; et al. Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks. Proceedings of the 41st International Conference on Machine Learning.Anais... , Proceedings of Machine Learning Research. v. 235, p.22895–22907, 2024. PMLR. Disponível em: <https://proceedings.mlr.press/v235/kambhampati24a.html>.
  - Verificação: Existe versao publicada: ICML 2024 (PMLR vol. 235), titulo oficial "Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks" (prefixo "Position:" ausente no registro), p.22895-22907. journal_ref do arXi…
- [x] `pallagani2024prospects` — PALLAGANI, V.; MUPPASANI, B. C.; ROY, K.; et al. On the Prospects of Incorporating Large Language Models (LLMs) in Automated Planning and Scheduling (APS). Proceedings of the International Conference on Automated Planning and Scheduling, v. 34, p. 432–444, 2024. Disponível em: <https://doi.org/10.1609/icaps.v34i1.31503>.
- [x] `silver2024generalized` — SILVER, T.; DAN, S.; SRINIVAS, K.; et al. Generalized Planning in PDDL Domains with Pretrained Large Language Models. Proceedings of the AAAI Conference on Artificial Intelligence, v. 38, n. 18, p. 20256–20264, 2024. Disponível em: <https://doi.org/10.1609/aaai.v38i18.30006>.
- [x] `stechly2025self` — STECHLY, K.; VALMEEKAM, K.; KAMBHAMPATI, S. On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks. The Thirteenth International Conference on Learning Representations (ICLR 2025).Anais... , 2025. Disponível em: <https://openreview.net/forum?id=4O0v4s3IzY>.
  - Verificação: Existe versao publicada: ICLR 2025 (poster), openreview.net/forum?id=4O0v4s3IzY, sem DOI. Chave atualizada de stechly2024self para stechly2025self.
- [x] `tantakoun2025llms` — TANTAKOUN, M.; MUISE, C.; ZHU, X. LLMs as Planning Formalizers: A Survey for Leveraging Large Language Models to Construct Automated Planning Models. Findings of the Association for Computational Linguistics: ACL 2025.Anais... . p.25167–25188, 2025. Association for Computational Linguistics. Disponível em: <https://doi.org/10.18653/v1/2025.findings-acl.1291>.
  - Verificação: Existe versao publicada: Findings of the ACL 2025, DOI 10.18653/v1/2025.findings-acl.1291, p.25167-25188. Ordem de autores na versao publicada: Tantakoun, Muise, Zhu (registro trazia Tantakoun, Zhu, Muise). BibTeX gerado…
- [x] `valmeekam2023planbench` — VALMEEKAM, K.; MARQUEZ, M.; OLMO, A.; SREEDHARAN, S.; KAMBHAMPATI, S. PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change. Advances in Neural Information Processing Systems 36 (NeurIPS 2023).Anais... . p.38975–38987, 2023. Disponível em: <https://doi.org/10.52202/075280-1693>.
  - Verificação: Registrado como preprint arXiv (2022, PlanBench). Localizada versao publicada revisada por pares: NeurIPS 2023 (Advances in Neural Information Processing Systems 36), DOI 10.52202/075280-1693, p.38975-38987. Caso conheci…
- [x] `valmeekam2023planning` — VALMEEKAM, K.; MARQUEZ, M.; SREEDHARAN, S.; KAMBHAMPATI, S. On the Planning Abilities of Large Language Models - A Critical Investigation. Advances in Neural Information Processing Systems 36 (NeurIPS 2023).Anais... . p.75993–76005, 2023. Disponível em: <https://doi.org/10.52202/075280-3320>.
  - Verificação: Existe versao publicada revisada por pares: NeurIPS 2023 (Advances in Neural Information Processing Systems 36), DOI 10.52202/075280-3320, p.75993-76005. Titulo oficial: "On the Planning Abilities of Large Language Model…
- [x] `xie2024travelplanner` — XIE, J.; ZHANG, K.; CHEN, J.; et al. TravelPlanner: A Benchmark for Real-World Planning with Language Agents. Proceedings of the 41st International Conference on Machine Learning.Anais... , Proceedings of Machine Learning Research. v. 235, p.54590–54613, 2024. PMLR. Disponível em: <https://proceedings.mlr.press/v235/xie24j.html>.
  - Verificação: Existe versao publicada: ICML 2024 (PMLR vol. 235), p.54590-54613. journal_ref do arXiv confirma "ICML 2024 (Spotlight)". BibTeX gerado a partir da pagina oficial PMLR.
- [x] `yao2023react` — YAO, S.; ZHAO, J.; YU, D.; et al. ReAct: Synergizing Reasoning and Acting in Language Models. The Eleventh International Conference on Learning Representations (ICLR 2023).Anais... , 2023. Disponível em: <https://openreview.net/forum?id=WE_vluYUL-X>.
  - Verificação: Registrado apenas como preprint arXiv (2022); aceito e publicado na ICLR 2023 (openreview.net/forum?id=WE_vluYUL-X), sem DOI atribuido pela conferencia. Comentario do proprio arXiv confirma: "v3 is the ICLR camera ready …

### E6 — Engenharia do conhecimento (16)

- [x] `alnazer2023understanding` — ALNAZER, E.; GEORGIEVSKI, I. Understanding Real-World AI Planning Domains: A Conceptual Framework. Service-Oriented Computing, Communications em Computer e Information Science. p.3–23, 2023. Springer. Disponível em: <https://doi.org/10.1007/978-3-031-45728-9_1>.
- [x] `chrpa2017fifth` — CHRPA, L.; MCCLUSKEY, T. L.; VALLATI, M.; VAQUERO, T. The Fifth International Competition on Knowledge Engineering for Planning and Scheduling: Summary and Trends. AI Magazine, v. 38, n. 1, p. 104–106, 2017. Disponível em: <https://doi.org/10.1609/aimag.v38i1.2719>.
- [x] `georgievski2026energy` — GEORGIEVSKI, I.; TEKIN, S.; AIELLO, M. The Energy Impact of Domain Model Design in Classical Planning. Proceedings of the IEEE/ACM 5th International Conference on AI Engineering - Software Engineering for AI.Anais... , CAIN ’26. p.234–239, 2026. ACM. Disponível em: <http://dx.doi.org/10.1145/3793653.3793791>.
  - Verificação: existe versão publicada: CAIN 2026 (IEEE/ACM), pp. 234-239, DOI 10.1145/3793653.3793791; BibTeX da versão publicada
- [x] `mccluskey1997engineering` — MCCLUSKEY, T. L.; PORTEOUS, J. M. Engineering and compiling planning domain models to promote validity and efficiency. Artificial Intelligence, v. 95, n. 1, p. 1–65, 1997. Disponível em: <https://doi.org/10.1016/S0004-3702(97)00034-9>.
- [x] `mccluskey2017engineering` — MCCLUSKEY, T. L.; VAQUERO, T. S.; VALLATI, M. Engineering Knowledge for Automated Planning: Towards a Notion of Quality. Proceedings of the Knowledge Capture Conference (K-CAP 2017).Anais... . p.1–8, 2017. ACM. Disponível em: <https://doi.org/10.1145/3148011.3148012>.
  - Verificação: Titulo oficial completo: "Engineering Knowledge for Automated Planning: Towards a Notion of Quality" (registro trazia apenas a primeira parte, sem o subtitulo).
- [x] `micheli2025unified` — MICHELI, A.; BIT-MONNOT, A.; RÖGER, G.; et al. Unified Planning: Modeling, manipulating and solving AI planning problems in Python. SoftwareX, v. 29, p. 102012, 2025. Disponível em: <https://doi.org/10.1016/j.softx.2024.102012>.
  - Verificação: Registro trazia ano 2024; o registro primario (Crossref) mostra publicacao formal (issued) em fevereiro de 2025, volume 29 (DOI mantem o padrao 'softx.2024.102012', referente ao ano de aceite/deposito em dez/2024). Chave…
- [x] `orlandini2014planning` — ORLANDINI, A.; BERNARDI, G.; CESTA, A.; FINZI, A. Planning meets verification and validation in a knowledge engineering environment. Intelligenza Artificiale, v. 8, n. 1, p. 87–100, 2014. Disponível em: <https://doi.org/10.3233/IA-140063>.
- [x] `simpson2000knowledge` — SIMPSON, R. M.; MCCLUSKEY, T. L.; LIU, D.; KITCHIN, D. E. Knowledge Representation in Planning: A PDDL to OCLh Translation. Foundations of Intelligent Systems, Lecture Notes em Computer Science. p.610–618, 2000. Springer. Disponível em: <https://doi.org/10.1007/3-540-39963-1_64>.
- [x] `simpson2007planning` — SIMPSON, R. M.; KITCHIN, D. E.; MCCLUSKEY, T. L. Planning domain definition using GIPO. The Knowledge Engineering Review, v. 22, n. 2, p. 117–134, 2007. Disponível em: <https://doi.org/10.1017/S0269888907001063>.
- [x] `vallati2015effective` — VALLATI, M.; HUTTER, F.; CHRPA, L.; MCCLUSKEY, T. L. On the Effective Configuration of Planning Domain Models. Proceedings of the Twenty-Fourth International Joint Conference on Artificial Intelligence (IJCAI 2015).Anais... . p.1704–1711, 2015. Disponível em: <https://www.ijcai.org/Proceedings/15/Papers/243.pdf>.
- [x] `vallati2019robustness` — VALLATI, M.; CHRPA, L. On the Robustness of Domain-Independent Planning Engines: The Impact of Poorly-Engineered Knowledge. Proceedings of the 10th International Conference on Knowledge Capture.Anais... , K-CAP ’19. p.197–204, 2019. ACM. Disponível em: <http://dx.doi.org/10.1145/3360901.3364416>.
- [x] `vallati2021importance` — VALLATI, M.; CHRPA, L.; MCCLUSKEY, T. L.; HUTTER, F. On the Importance of Domain Model Configuration for Automated Planning Engines. Journal of Automated Reasoning, v. 65, n. 6, p. 727–773, 2021. Springer Science and Business Media LLC. Disponível em: <http://dx.doi.org/10.1007/s10817-021-09592-1>.
  - Verificação: autor faltante na busca: Hutter, F. (4 autores no registro)
- [x] `vallati2025knowledge` — VALLATI, M.; BARTÁK, R.; CHRPA, L.; MCCLUSKEY, T. L.; PETRICK, R. P. A. Knowledge Engineering for Planning and Scheduling in the LLM Era. Proceedings of the International Conference on Automated Planning and Scheduling, v. 35, n. 1, p. 391–395, 2025. Disponível em: <https://doi.org/10.1609/icaps.v35i1.36142>.
- [x] `vaquero2005itsimple` — VAQUERO, T. S.; TONIDANDEL, F.; SILVA, J. R. The itSIMPLE tool for Modeling Planning Domains. ICAPS 2005 Competition on Knowledge Engineering for Planning and Scheduling (ICKEPS).Anais... , 2005. Monterey, California, USA. Disponível em: <https://ipc05.icaps-conference.org/papers/paper5.pdf>.
  - Verificação: Sem registro no Crossref. Veículo confirmado em 23/09/2026 no site oficial da competição: ICAPS 2005 Competition on Knowledge Engineering for Planning and Scheduling, 7 jun. 2005, Monterey (páginas de programa e competid…
- [x] `vaquero2007itsimpleb` — VAQUERO, T. S. itSIMPLE: ambiente integrado de modelagem e análise de domínios de planejamento automático, 2007. Disserta{\c{c}}{\~a}o de Mestrado, Universidade de São Paulo. Disponível em: <https://doi.org/10.11606/D.3.2007.tde-19072007-174135>.
  - Verificação: O registro Crossref nao preenche o campo 'issued' (retorna null), mas o proprio identificador do DOI codifica a data de defesa (tde-19072007 = 19/07/2007), confirmando o ano de 2007 ja registrado. Escola: Universidade de…
- [x] `vaquero2013itsimple` — VAQUERO, T. S.; SILVA, J. R.; TONIDANDEL, F.; BECK, J. C. itSIMPLE: towards an integrated design system for real planning applications. The Knowledge Engineering Review, v. 28, n. 2, p. 215–230, 2013. Disponível em: <https://doi.org/10.1017/S0269888912000434>.

### E7 — Pontes conceituais (19)

- [x] `chen2023frugalgpt` — CHEN, L.; ZAHARIA, M.; ZOU, J. FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance. Transactions on Machine Learning Research, 2024. Disponível em: <https://openreview.net/forum?id=cSimKw5p6R>.
  - Verificação: Existe versão publicada: Transactions on Machine Learning Research (TMLR), 12/2024 (confirmado lendo o cabeçalho da primeira página do PDF publicado pelos autores, que traz "Published in Transactions on Machine Learning …
- [x] `davern2007towards` — DAVERN, M. J. Towards a Unified Theory of Fit: Task, Technology and Individual. Information Systems Foundations: Theory, Representation and Reality, 2007. ANU Press. Disponível em: <https://doi.org/10.22459/isftrr.11.2007.03>.
- [x] `donaldson2006contingency` — DONALDSON, L. The Contingency Theory of Organizational Design: Challenges and Opportunities. Organization Design, Information e Organization Design Series. p.19–40, 2006. Springer US. Disponível em: <https://doi.org/10.1007/0-387-34173-0_2>.
  - Verificação: O BibTeX do Crossref não traz o campo year; o ano (2006) foi confirmado pelo campo created (2006-09-09) e pelo ISBN da edição (9780387341729) no registro Crossref, e acrescentado ao BibTeX com base nesse mesmo registro p…
- [x] `furneaux2011task` — FURNEAUX, B. Task-Technology Fit Theory: A Survey and Synopsis of the Literature. Information Systems Theory, Integrated Series em Information Systems. p.87–106, 2011. Springer New York. Disponível em: <https://doi.org/10.1007/978-1-4419-6108-2_5>.
  - Verificação: O veículo registrado ("Integrated Series in Information Systems") é o nome da série; o título do livro é "Information Systems Theory: Explaining and Predicting Our Digital Society, Vol. 1". A edição impressa é de 2012, m…
- [x] `gomez2016empirical` — GÓMEZ, D.; ROJAS, A. An Empirical Overview of the No Free Lunch Theorem and Its Effect on Real-World Machine Learning Classification. Neural Computation, v. 28, n. 1, p. 216–228, 2016. MIT Press. Disponível em: <https://doi.org/10.1162/neco_a_00793>.
- [x] `goodhue1995task` — GOODHUE, D. L.; THOMPSON, R. L. Task-Technology Fit and Individual Performance. MIS Quarterly, v. 19, n. 2, p. 213–236, 1995. MIS Quarterly. Disponível em: <https://doi.org/10.2307/249689>.
- [x] `howard2019refining` — HOWARD, M. C.; ROSE, J. C. Refining and extending task–technology fit theory: Creation of two task–technology fit scales and empirical clarification of the construct. Information & Management, v. 56, n. 6, p. 103134, 2019. Elsevier BV. Disponível em: <https://doi.org/10.1016/j.im.2018.12.002>.
- [x] `lawrence1967differentiation` — LAWRENCE, P. R.; LORSCH, J. W. Differentiation and Integration in Complex Organizations. Administrative Science Quarterly, v. 12, n. 1, p. 1–47, 1967. JSTOR. Disponível em: <https://doi.org/10.2307/2391211>.
  - Verificação: Crossref registra apenas a página inicial (pages=1); fontes secundárias (SCIRP, ResearchGate, citações padrão da área) indicam o intervalo 1-47 para o artigo (ASQ v.12 n.1), mas isso não foi confirmado em fonte primária …
- [x] `moslem2026dynamic` — MOSLEM, Y.; KELLEHER, J. D. Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey. Transactions on Machine Learning Research, 2026. Disponível em: <https://arxiv.org/abs/2603.04445>.
  - Verificação: O campo journal-ref do próprio registro arXiv informa aceite em Transactions on Machine Learning Research (TMLR), 2026, sem DOI próprio (TMLR não emite DOI); comentário do arXiv confirma "Accepted by TMLR (2026)".
- [x] `ong2024routellm` — ONG, I.; ALMAHAIRI, A.; WU, V.; et al. RouteLLM: Learning to Route LLMs from Preference Data. The Thirteenth International Conference on Learning Representations (ICLR 2025).Anais... , 2025. Disponível em: <https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html>.
  - Verificação: Existe versão publicada revisada por pares: ICLR 2025, com título ligeiramente alterado para "RouteLLM: Learning to Route LLMs FROM Preference Data" (a versão arXiv usa "WITH"). BibTeX gerado a partir da versão publicada…
- [x] `passmore2025if` — PASSMORE, J.; DALY, J.; TEE, D. If the hat fits: A review of Task Technology Fit Theory (TTF) through users experience of engaging with an AI coaching agent. Organisationsberatung, Supervision, Coaching, v. 33, n. 1, p. 39–54, 2025. Springer Science and Business Media LLC. Disponível em: <https://doi.org/10.1007/s11613-025-00981-8>.
  - Verificação: Publicação eletrônica (issued) em 18/12/2025, condizente com o ano registrado (2025); o fascículo impresso (v.33 n.1, p.39-54) só sai em março de 2026.
- [x] `smithmiles2009cross` — SMITH-MILES, K. A. Cross-disciplinary perspectives on meta-learning for algorithm selection. ACM Computing Surveys, v. 41, n. 1, p. 1–25, 2009. Association for Computing Machinery (ACM). Disponível em: <https://doi.org/10.1145/1456650.1456656>.
- [x] `smithmiles2014towards` — SMITH-MILES, K.; BAATAR, D.; WREFORD, B.; LEWIS, R. Towards objective measures of algorithm performance across instance space. Computers & Operations Research, v. 45, p. 12–24, 2014. Elsevier BV. Disponível em: <https://doi.org/10.1016/j.cor.2013.11.015>.
- [x] `smithmiles2023instance` — SMITH-MILES, K.; MUÑOZ, M. A. Instance Space Analysis for Algorithm Testing: Methodology and Software Tools. ACM Computing Surveys, v. 55, n. 12, p. 1–31, 2023. Association for Computing Machinery (ACM). Disponível em: <https://doi.org/10.1145/3572895>.
- [x] `soodan2024ai` — SOODAN, V.; RANA, A.; JAIN, A.; SHARMA, D. AI Chatbot Adoption in Academia: Task Fit, Usefulness and Collegial Ties. Journal of Information Technology Education: Innovations in Practice, v. 23, 2024. Informing Science Institute. Disponível em: <https://doi.org/10.28945/5260>.
- [x] `sterkenburg2021nofreelunch` — STERKENBURG, T. F.; GRÜNWALD, P. D. The no-free-lunch theorems of supervised learning. Synthese, v. 199, n. 3-4, p. 9979–10015, 2021. Springer Science and Business Media LLC. Disponível em: <https://doi.org/10.1007/s11229-021-03233-1>.
- [x] `vanschoren2019metalearning` — VANSCHOREN, J. Meta-Learning. Automated Machine Learning, The Springer Series on Challenges em Machine Learning. p.35–61, 2019. Springer International Publishing. Disponível em: <https://doi.org/10.1007/978-3-030-05318-5_2>.
  - Verificação: O veículo registrado ("The Springer Series on Challenges in Machine Learning") é o nome da série; o título do livro é "Automated Machine Learning: Methods, Systems, Challenges". O conteúdo do capítulo corresponde ao prep…
- [x] `wolpert1997no` — WOLPERT, D. H.; MACREADY, W. G. No free lunch theorems for optimization. IEEE Transactions on Evolutionary Computation, v. 1, n. 1, p. 67–82, 1997. Institute of Electrical and Electronics Engineers (IEEE). Disponível em: <https://doi.org/10.1109/4235.585893>.
- [x] `wu2024large` — WU, X.; ZHONG, Y.; WU, J.; JIANG, B.; TAN, K. C. Large Language Model-Enhanced Algorithm Selection: Towards Comprehensive Algorithm Representation. Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence (IJCAI 2024).Anais... . p.5235–5244, 2024. International Joint Conferences on Artificial Intelligence Organization. Disponível em: <https://doi.org/10.24963/ijcai.2024/579>.

### E8 — IA no desenvolvimento de software (15)

- [x] `cui2024effects` — CUI, K. Z.; DEMIRER, M.; JAFFE, S.; et al. The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers. Management Science, 2026. Institute for Operations Research and the Management Sciences (INFORMS). Disponível em: <https://doi.org/10.1287/mnsc.2025.00535>.
  - Verificação: O registro consultado (SSRN) é posted-content, não revisado por pares. Existe versão publicada: Management Science, 2026, DOI 10.1287/mnsc.2025.00535 (INFORMS). O nome do primeiro autor aparece como "Cui, Kevin Zheyuan" …
- [x] `hong2023metagpt` — HONG, S.; ZHUGE, M.; CHEN, J.; et al. MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. The Twelfth International Conference on Learning Representations (ICLR 2024).Anais... , 2024. Disponível em: <https://proceedings.iclr.cc/paper_files/paper/2024/hash/6507b115562bb0a305f1958ccc87355a-Abstract-Conference.html>.
  - Verificação: Existe versão publicada: ICLR 2024 (oral, top 1,2%). O terceiro autor aparece como "Jiaqi Chen" no arXiv e como "Jonathan Chen" na página oficial do ICLR - mesma pessoa, mudança de nome preferido entre o preprint e a ver…
- [x] `hou2023large` — HOU, X.; ZHAO, Y.; LIU, Y.; et al. Large Language Models for Software Engineering: A Systematic Literature Review. ACM Transactions on Software Engineering and Methodology, v. 33, n. 8, p. 1–79, 2024. Association for Computing Machinery (ACM). Disponível em: <https://doi.org/10.1145/3695988>.
  - Verificação: Existe versão publicada: ACM Transactions on Software Engineering and Methodology, 2024, DOI 10.1145/3695988, v.33 n.8, p.1-79. BibTeX gerado a partir da versão publicada.
- [x] `jimenez2024swebench` — JIMENEZ, C. E.; YANG, J.; WETTIG, A.; et al. SWE-bench: Can Language Models Resolve Real-World GitHub Issues? The Twelfth International Conference on Learning Representations (ICLR 2024).Anais... , 2024. Disponível em: <https://openreview.net/forum?id=VTF8yNQM66>.
  - Verificação: Publicado no ICLR 2024 (oral), OpenReview id VTF8yNQM66, conforme o próprio comentário do registro arXiv. A listagem HTML do ICLR mostra o título com capitalização diferente ("Real-world Github"); manteve-se a capitaliza…
- [x] `liang2024largescale` — LIANG, J. T.; YANG, C.; MYERS, B. A. A Large-Scale Survey on the Usability of AI Programming Assistants: Successes and Challenges. Proceedings of the IEEE/ACM 46th International Conference on Software Engineering.Anais... , ICSE ’24. p.1–13, 2024. ACM. Disponível em: <https://doi.org/10.1145/3597503.3608128>.
- [x] `liu2026large` — LIU, J.; WANG, K.; CHEN, Y.; et al. Large Language Model-Based Agents for Software Engineering: A Survey. ACM Transactions on Software Engineering and Methodology, 2026. Association for Computing Machinery (ACM). Disponível em: <https://doi.org/10.1145/3796507>.
  - Verificação: Registro já correspondia à versão publicada (ACM Transactions on Software Engineering and Methodology, 2026); existe preprint correspondente em arXiv:2409.02977.
- [x] `pan2024training` — PAN, J.; WANG, X.; NEUBIG, G.; et al. Training Software Engineering Agents and Verifiers with SWE-Gym. In: A. Singh; M. Fazel; D. Hsu; et al. (Org.); Proceedings of the 42nd International Conference on Machine Learning (ICML 2025).Anais... , Proceedings of Machine Learning Research. v. 267, p.47717–47737, 2025. PMLR. Disponível em: <https://proceedings.mlr.press/v267/pan25g.html>.
  - Verificação: Existe versão publicada: ICML 2025, PMLR vol. 267, p. 47717-47737. BibTeX gerado a partir da versão publicada (PMLR).
- [x] `perry2023do` — PERRY, N.; SRIVASTAVA, M.; KUMAR, D.; BONEH, D. Do Users Write More Insecure Code with AI Assistants? Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security.Anais... , CCS ’23. p.2785–2799, 2023. ACM. Disponível em: <https://doi.org/10.1145/3576915.3623157>.
- [x] `rondon2025evaluating` — RONDON, P.; WEI, R.; CAMBRONERO, J.; et al. Evaluating Agent-Based Program Repair at Google. 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP).Anais... . p.365–376, 2025. IEEE. Disponível em: <https://doi.org/10.1109/icse-seip66354.2025.00038>.
- [x] `stray2025developer` — STRAY, V.; BRANDTZÆG, E. G.; WIVESTAD, V. T.; BARBALA, A.; MOE, N. B. Developer Productivity With and Without GitHub Copilot: A Longitudinal Mixed-Methods Case Study. Proceedings of the 59th Hawaii International Conference on System Sciences (HICSS-59).Anais... . p.7413–7422, 2026. Hawaii International Conference on System Sciences. Disponível em: <https://doi.org/10.24251/HICSS.2026.880>.
  - Verificação: Existe versão publicada: Proceedings of the 59th Hawaii International Conference on System Sciences (HICSS-59), 2026, DOI 10.24251/HICSS.2026.880, p. 7413-7422 (identificado pelo campo journal-ref do próprio registro arX…
- [x] `takerngsaksiri2025humanintheloop` — TAKERNGSAKSIRI, W.; PASUKSMIT, J.; THONGTANUNAM, P.; et al. Human-In-The-Loop Software Development Agents. 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP).Anais... . p.342–352, 2025. IEEE. Disponível em: <https://doi.org/10.1109/icse-seip66354.2025.00036>.
- [x] `wang2024openhands` — WANG, X.; LI, B.; SONG, Y.; et al. OpenHands: An Open Platform for AI Software Developers as Generalist Agents. The Thirteenth International Conference on Learning Representations (ICLR 2025).Anais... , 2025. Disponível em: <https://proceedings.iclr.cc/paper_files/paper/2025/hash/a4b6ad6b48850c0c331d1259fc66a69c-Abstract-Conference.html>.
  - Verificação: Existe versão publicada: ICLR 2025. BibTeX gerado a partir da versão publicada.
- [x] `wu2023autogen` — WU, Q.; BANSAL, G.; ZHANG, J.; et al. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations. First Conference on Language Modeling (COLM 2024).Anais... , 2024. Disponível em: <https://openreview.net/forum?id=BAakY1hNKS>.
  - Verificação: Existe versão publicada: COLM 2024 (Conference on Language Modeling), sem DOI (COLM não emite DOI). O título da versão publicada usa "Conversations" (plural); o preprint arXiv usa "Conversation" (singular). BibTeX gerado…
- [x] `xia2025demystifying` — XIA, C. S.; DENG, Y.; DUNN, S.; ZHANG, L. Demystifying LLM-Based Software Engineering Agents. Proceedings of the ACM on Software Engineering, v. 2, n. FSE, p. 801–824, 2025. Association for Computing Machinery (ACM). Disponível em: <https://doi.org/10.1145/3715754>.
- [x] `yang2024sweagent` — YANG, J.; JIMENEZ, C.; WETTIG, A.; et al. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. In: A. Globerson; L. Mackey; D. Belgrave; et al. (Org.); Advances in Neural Information Processing Systems 37 (NeurIPS 2024).Anais... . v. 37, p.50528–50652, 2024. Curran Associates, Inc. Disponível em: <https://proceedings.neurips.cc/paper_files/paper/2024/file/5a7c947568c1b1328ccc5230172e1e7c-Paper-Conference.pdf>.
  - Verificação: Existe versão publicada: NeurIPS 2024 (Advances in Neural Information Processing Systems 37), DOI 10.52202/079017-1601, p. 50528-50652. BibTeX gerado a partir da versão publicada (NeurIPS), conforme exemplo citado no pro…
