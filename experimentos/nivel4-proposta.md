# Nível 4 (R-24): proposta de desenho

Rascunho de trabalho de 26/09/2026 (Claude Code). **Decisão do autor (26/09/2026): opção A, só dados publicados; *benchmarks* Autoscale; limites de 30 min e 4 GiB (os dos dados publicados).** O desenho aprovado da Fase 3 está no plano (seção 7) e em `auditoria/reexecucao.md` §6.

## 1. O que já existe

| Recurso | O que traz | Situação |
|---|---|---|
| `potassco/pddl-instances` (commit `cf19edf`) | Instâncias originais das IPCs de 1998 a 2014 | Clonado em `experimentos/benchmarks/ipc/` |
| Planner Museum (`lequen2026planner`; GitHub `mrlab-ai/planner-museum`, tag `icaps-2026`, commit `723a31c0`) | 26 receitas Apptainer, correspondentes aos 29 planejadores das IPCs de 1998 a 2023; *benchmarks* Autoscale com custo unitário (42 domínios × 30 instâncias); o conjunto de *benchmarks* do Fast Downward; VAL; scripts do Downward Lab | Clonado em `experimentos/ferramentas/planner-museum` (fora do git; o repositório não tem arquivo de licença) |
| Cobertura publicada do Planner Museum | 29 planejadores × 42 domínios, mesmo hardware, 30 min e 4 GiB | `data/planner-museum/cobertura_por_dominio.csv`, conferida pela linha Total |
| Extratores (EXP-07, EXP-11) | 11 métricas de 2010 e 16 *features* SAS+ a partir do PDDL | Prontos |
| Os 10 planejadores de 2010 | Binários do acervo, rodando no GCP (Nível 3) | EXP-05 em andamento |

**Planejadores de 2010 no Planner Museum:** Blackbox (BB2), IPP, FF, R (SysR), LPG e Fast Downward (versão de 2004). Não estão: SGPlan, SATPlan e MaxPlan. Esses três temos no acervo. O YAHSP do museu é o de 2014, não o de 2010.

## 2. Opções

**A. Dados publicados primeiro, sem executar nada.**
- **Como:** cruzar a cobertura publicada (29 × 42) com as *features* SAS+ e as métricas extraídas do PDDL das instâncias Autoscale, e analisar por domínio: método de 2010, *single best*, *virtual best*, modelos simples.
- **Ganho:** custo zero, e mostra logo se há sinal.
- **Limites:**
  - só cobertura e só por domínio (sem tempo, qualidade nem resultado por instância);
  - 42 domínios;
  - Pathways zerado, a investigar.
- **Atenção:** antecipa parte da ideia da Fase 4B (dados publicados), agora com dados de um experimento controlado, não das IPCs.

**B. Execução própria.**
- **Como:** os contêineres do Planner Museum mais SGPlan, SATPlan e MaxPlan do acervo, sobre o Autoscale, no GCP, com as mesmas condições do museu (30 min e 4 GiB).
- **Ganho:**
  - dados por instância (cobertura, tempo e, com o VAL, qualidade do plano);
  - a tabela publicada serve para validar o nosso ambiente.
- **Tamanho:** 32 planejadores × 42 domínios × 30 instâncias = 40.320 execuções. O teto é de cerca de 20.000 horas-núcleo, com todas as execuções chegando aos 30 minutos; o real será menor. O custo no GCP precisa ser estimado antes, contra o crédito disponível.

**C. Híbrido: A agora e B depois, num subconjunto** escolhido a partir do que A mostrar (por exemplo, os planejadores que cobrem os valores da taxonomia 4D e os domínios que discriminam).

## 3. Recomendação

**C.** A opção A custa pouco, responde rápido se as características explicam alguma coisa em 42 domínios e orienta o recorte de B. A opção B, com as condições do museu, dá os dados por instância que a análise por instância (A1, A3) e o R-27 precisam.

## 4. Decisões do autor

1. **Conjunto de *benchmarks*:** Autoscale (recomendado: instâncias ajustadas para discriminar os planejadores atuais e mesmas instâncias da tabela publicada) ou as instâncias originais das IPCs. A decisão de 23/09 sobre o G14 ("Nível 4 usa os conjuntos completos") foi tomada antes de o Autoscale estar no radar.
2. **Opção A, B ou C.** A opção A toca a ideia da Fase 4B; confirmar se pode ser antecipada aqui.
3. **Condições da execução própria:** as do museu, 30 min e 4 GiB (recomendado, para validar contra a tabela), ou outras.
4. **Planejadores:** os 29 do museu mais os 3 de 2010 que faltam, ou um recorte. O R-31 (heurística aprendida) exigiria um planejador fora do museu.

## 5. Pendências de verificação

- Autoscale (Torralba, Seipp e Sievers, 2021) e a cobertura zero no Pathways: fonte primária a ler antes de citar ou concluir.
- Classificar os planejadores do museu na taxonomia 4D a partir das fontes primárias (como foi feito para os 10 de 2010).
