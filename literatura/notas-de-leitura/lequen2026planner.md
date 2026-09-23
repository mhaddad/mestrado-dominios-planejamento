---
tipo: nota-de-leitura
eixo: E3
citekey: lequen2026planner
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/download/42852/50412/46953
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A3, A4]
fragilidades: [F1, F2, F6]
perguntas: [Q1]
---

# Planner Museum: Evaluating Classical Planners Over Time

**Lequen, A.; Joergensen, O.; Phung, W.; Gestrin, E.; Van Meerbeeck, D.; Fritzsche, M.; Drexler, D.; Seipp, J. · 2026 · Proceedings of ICAPS 2026**
**Link/DOI:** https://doi.org/10.1609/icaps.v36i1.42852

## Extração estruturada

- **Problema:** a IPC documenta 28 anos de progresso em planejamento automatizado, mas não havia uma avaliação sistemática, em hardware moderno e num benchmark unificado abrangendo toda a história da competição, de como planejadores de diferentes épocas se comparam entre si.
- **Método:** os autores coletam código-fonte de 29 planejadores distintos de todas as edições da IPC (1998–2023), corrigem-nos quando necessário e os empacotam em contêineres Apptainer para rodar em hardware atual. Avaliam a cobertura (número de instâncias resolvidas dentro de limites de tempo/memória) de cada planejador em um conjunto de *benchmarks* que abrange toda a história da IPC, com dificuldade de instância escalada para não favorecer planejadores otimizados para um tipo específico de problema.
- **Dados/benchmarks:** 29 planejadores, incluindo exatamente vários dos planejadores estudados em 2010 (Blackbox=BB2, HSP, IPP, FF, LPG=LPG?, R=SysR, Fast Downward=FD/FDD, YAHSP, entre outros das gerações seguintes: LAMA08, LAMA11, FDSS11/23, Merc/Mercury, MpC/Madagascar, Levitron, Maidu/Scorpion Maidu); limite de 4 GiB de memória e 30 minutos por instância, em um cluster com processadores Intel Xeon Gold 6130.
- **Resultado principal:** apesar de "modestos começos" em que Fast Forward dominou, diferentes planejadores venceram competições sucessivas, com desempenho aumentando de forma constante desde 2008; ao mesmo tempo, alguns planejadores mais antigos (ex.: System R de 2000, SimPlanner de 2002) ainda exibem desempenho de ponta em domínios específicos, mesmo décadas depois — nenhum planejador único domina todos os domínios em nenhuma época.
- **Relação com a dissertação de 2010:**
  - **A1/A3 (nuança — nem confirma nem torna obsoleta, qualifica):** o achado central — planejadores antigos ainda vencem em domínios específicos, enquanto os mais recentes dominam a cobertura agregada — é compatível com a tese de 2010 de que características de domínio indicam qual técnica funciona melhor (A1): se não fosse assim, o planejador mais recente venceria sempre, em todo domínio. Ao mesmo tempo, qualifica A3 (ranking definido só pelas características do domínio, independentemente do problema): a obra usa **cobertura agregada por domínio ao longo de várias instâncias**, não por características estruturais extraídas de UML como em 2010; a correlação entre "característica de domínio" e "planejador vencedor" mostrada aqui é empírica e não testada com um método preditivo como o de 2010 — portanto, esta obra não valida nem invalida o método de extração UML de A1/A3, apenas mostra que o fenômeno geral (dependência do desempenho ao domínio) persiste.
  - **A4 (confirma parcialmente):** mais planejadores (29, cobrindo 28 anos) e mais domínios (todas as IPCs) tornam o quadro mais completo e menos sujeito a viés de amostra pequena, sustentando a ideia de que ampliar a base melhora a capacidade de generalizar conclusões — mas o artigo é sobre cobertura simples, não sobre um "ranking preditivo por característica de domínio" como em 2010, então a confirmação de A4 é indireta.
  - **F1/F6 (evidencia as fragilidades):** confirma diretamente que a comparação entre planejadores de diferentes épocas é rara na literatura (motivação do próprio artigo, inspirado no "SAT Museum") — reforça que a comparação de 2010 (10 planejadores de uma janela de tempo estreita) carece de uma perspectiva histórica mais ampla, que esta obra agora fornece.
  - **F2 (evidencia a fragilidade):** ao mostrar que rankings de planejadores mudam substancialmente conforme o conjunto de domínios/instâncias considerado (ex.: Fast Forward "performs better on domains from IPC 2008 than some more recent planners"), reforça que um ranking construído sobre uma amostra pequena de domínios (10+3, como em 2010) tem risco real de não generalizar — evidência empírica direta para a fragilidade F2.

## Pontos relevantes para o projeto

- Contém, na Tabela 1, cobertura de planejadores que aparecem no próprio corpus de 2010 sob nomes ou siglas semelhantes (Blackbox/BB2, IPP, FF, Fast Downward/FD-FDD, YAHSP), o que permite, em trabalho futuro da revisão, comparar diretamente desempenho histórico desses planejadores nos mesmos domínios usados em 2010 — mas isso exigiria conferir se as versões/formulações de domínio coincidem antes de qualquer number entrar no texto.
- Demonstra formalmente (índice de Jaccard sobre conjuntos de instâncias resolvidas) que planejadores de abordagens semelhantes (ex.: ANS e LAPKT, ambos baseados em busca por largura) tendem a resolver as mesmas instâncias — abordagem metodológica interessante para caracterizar "família de técnica" empiricamente, algo que 2010 não fez.
- É um artigo do ICAPS 2026 (o mais recente do lote), com DOI e fonte da própria IPC — mostra que a pergunta "a taxonomia/os rankings de planejadores por domínio se sustentam ao longo do tempo?" (Q1 da revisão) é uma pergunta de pesquisa ativa reconhecida pela comunidade em 2026, não apenas uma preocupação interna deste projeto.
- Observação de escopo: o artigo é publicado com data futura (ICAPS 2026, proceedings de conferência ainda não realizada na data de leitura, 22/09/2026); o registro Crossref/DOI e o PDF já estavam publicamente disponíveis no repositório da OJS/AAAI no momento da leitura.

## Marcações

- `[FATO]` "The main takeaway is that the highest coverage is achieved by the most recent planners. Another interesting observation [...] is that some earlier planners perform well on domains that were first used in later IPCs" (Seção "Results").
- `[FATO]` "From that year onward [2008, quando LAMA venceu], each competition saw a new planner outperform the previous ones, thereby gradually pushing the coverage frontier forward" (Seção "Results").
- `[HIPÓTESE]` A persistência de planejadores antigos como vencedores em domínios específicos décadas depois sugere que a relação entre característica de domínio e técnica vencedora (A1 de 2010) é um fenômeno real e duradouro, mas que a extração de características por UML/itSIMPLE usada em 2010 não é a única forma possível de capturá-lo — a "característica de domínio" que explica o desempenho aqui é inferida apenas post-hoc pelos autores (ex.: Scanalyzer, Satellite), não medida sistematicamente como em 2010.

## Trechos literais

1. "Using modern hardware and coverage as our primary metric, we show that, despite modest beginnings in which Fast Forward [...] dominated, different planners won successive competitions, with performance increasing steadily since 2008." (Resumo)
2. "Our results show that, perhaps reassuringly, the most recent planners perform the best. Yet, some older planners exhibit state-of-the-art performance on certain domains." (Seção "Conclusions")
3. "A case in point is Fast Forward, which competed in IPC 2000 yet performs better on domains from IPC 2008 than some more recent planners." (Seção "Results")

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/ICAPS/article/download/42852/50412/46953. Conferência humana: pendente.
