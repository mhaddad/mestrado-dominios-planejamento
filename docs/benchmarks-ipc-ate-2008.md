# Benchmarks das IPCs até 2008 × material da dissertação de 2010

Verificação feita em 21/09/2026 a pedido do autor: os domínios e problemas usados na dissertação existem no repositório público [potassco/pddl-instances](https://github.com/potassco/pddl-instances)? De qual IPC e de qual variante vieram?

> **Convenção:** `[FATO]` = verificado por comparação de conteúdo. `[HIPÓTESE]` = inferência. `[A CONFIRMAR]` = falta evidência.

## Resposta curta

- **Sim, os 13 domínios existem** no repositório com edições de 1998 a 2008. Foram procurados os anos de 2008 e anteriores, que é o período da primeira versão da dissertação.
- **Os 11 domínios com PDDL no acervo foram localizados por conteúdo.** Dez têm todos os problemas **idênticos** aos do repositório (após normalizar comentários e espaços); o Gripper tem 19 de 20 **equivalentes** (só muda a ordem dos objetos) e 1 problema que não existe na IPC.
- **Zeno-travel e Elevator**, sem PDDL no acervo, existem no repositório (IPC 2002 e IPC 2000). O autor confirmou em 21/09/2026 que as variantes usadas são as identificadas aqui: **`zenotravel-strips-automatic`** e **`elevator-strips-simple-typed`**. O nível `strips` foi confirmado; `automatic` e `typed` são desempate por consistência (ver a seção própria). O autor também definiu **N = 20** para os dois.
- O **mapa final** dos 13 domínios está em `data/2010/benchmarks_ipc_mapa_final.csv`.

## Como foi feito

`data/2010/scripts/mapear_benchmarks_ipc.py` compara cada arquivo de `acervo-2010/.../comp/<domínio>/` com todas as instâncias de todas as variantes de 1998 a 2008, em duas camadas:

1. **Idêntico:** texto igual após remover comentários, passar para minúsculas e colapsar espaços.
2. **Equivalente:** texto diferente, mas com os mesmos objetos e os mesmos átomos em `:init` e `:goal`, ignorando ordem e nome do problema. Só é tentado se não houver correspondência idêntica.

Resultados em `data/2010/benchmarks_ipc.csv` (por domínio e variante) e `data/2010/benchmarks_ipc_instancias.csv` (um registro por arquivo do acervo).

Repositório analisado: commit `cf19edf7c53d1540ddbb396c642595e0926ee552` (28/11/2017). **O repositório não declara licença** (`licenseInfo` vazio no GitHub); os arquivos originais são das IPCs, cada uma com seus autores, listados nos READMEs de cada domínio.

## Mapa: domínio → IPC → variante

| Domínio | IPC | Variante no repositório | Usado em 2010 | Conjunto da IPC | Problemas | Domínio PDDL |
|---|---|---|---|---|---|---|
| Blocks World | 2000 | `blocks-strips-typed` | instâncias 1–35 | 102 | 35/35 idênticos | idêntico |
| Depots | 2002 | `depots-strips-automatic` | 1–22 | 22 | 22/22 idênticos | idêntico |
| Driver Log | 2002 | `driverlog-strips-automatic` | 1–20 | 20 | 20/20 idênticos | idêntico |
| Gripper | 1998 | `gripper-round-1-strips` | 2–20 (deslocado, ver abaixo) | 20 | 19/20 equivalentes; 1 sem par | idêntico |
| Logistics | 2000 | `logistics-strips-typed` | 1–28 | 84 | 28/28 idênticos | equivalente (só muda a ordem de `:types`) |
| Mystery | 1998 | `mystery-round-1-strips` | 1–30 | 30 | 30/30 idênticos | idêntico |
| Pathways | 2006 | `pathways-propositional` (e `-strips` na pasta `Strips/`) | 1–30 | 30 | 30/30 idênticos | idêntico |
| Pipes World | 2004 **e** 2006 | `pipesworld-tankage-nontemporal-strips` = `pipesworld-propositional` (e `-strips` em `Strips/`) | 1–50 | 50 | 50/50 idênticos | idêntico |
| Satellite | 2004 (domínio); problemas também em 2002 | `satellite-strips` | 1–20 | 36 | 20/20 idênticos | idêntico ao de **2004**; o de 2002 difere |
| TPP | 2006 | `tpp-propositional` (e `-strips` em `Strips/`) | 1–30 | 30 | 30/30 idênticos | idêntico |
| Storage | 2006 | `storage-propositional` | 1–30 | 30 | 30/30 idênticos | idêntico |
| Zeno-travel | 2002 | `zenotravel-strips-automatic` (confirmada pelo autor) | 1–20 (conjunto inteiro; N confirmado pelo autor) | 20 | sem PDDL no acervo | — |
| Elevator | 2000 (Miconic-10) | `elevator-strips-simple-typed` (confirmada pelo autor) | 1–20 (N confirmado pelo autor; originais `s1-0` a `s4-4`) | 150 | sem PDDL no acervo | — |

Todos os totais coincidem com a coluna "Número Problemas" da planilha `contabilizacao_problemas.ods` (35, 22, 20, 20, 28, 30, 30, 50, 20, 30, 30). `[FATO]`

## Achados

1. **Subconjuntos, sempre as primeiras instâncias.** Em todos os domínios o acervo usa as instâncias 1 a N do conjunto da IPC: 35 de 102 no Blocks World, 28 de 84 no Logistics, 20 de 36 no Satellite. Os demais conjuntos foram usados por inteiro. `[FATO]` Como a numeração das IPCs costuma crescer com o tamanho, `[HIPÓTESE]` de que os cortados são os problemas menores; não há registro no acervo do critério de corte (talvez o limite prático de tempo, 20 min por problema).

2. **Gripper foi gerado localmente, com o gerador oficial.** Os problemas `pfile1…pfile20` têm 2, 4, 6, …, 40 bolas, produzidos pelo `GENERATOR/gripper.c` (© Freiburg 2001) com `gerar_todos.sh` (`./gripper -n 2` … `-n 40`). A IPC 1998 tem 4, 6, …, 42 bolas. Assim, os arquivos do acervo `pfile2…pfile20` correspondem às instâncias 1 a 19 da IPC (mesmo número de bolas), e o `pfile1` (2 bolas) não existe na IPC, enquanto a instância 20 da IPC (42 bolas) não foi usada. `[FATO]` Consequência para F6: o conjunto de Gripper de 2010 **não é** o das competições, embora o domínio seja.

3. **Pipes World: 2004 e 2006 são o mesmo material.** As variantes de 2004 e de 2006 têm domínio e 50 instâncias idênticos. Não é possível dizer, só pelos arquivos, de qual das duas edições o autor os obteve. `[FATO]` para a identidade; a edição de origem fica `[A CONFIRMAR]`.

4. **Satellite é o de 2004.** O `domain.pddl` do acervo é idêntico ao da IPC 2004; o da IPC 2002 difere. Os 20 problemas existem nas duas edições. `[FATO]` A pasta `sattelite/antigo/` (domínio e problemas anteriores) não foi comparada.

5. **As pastas `Strips/` são a versão compilada da IPC 2006.** Em Pathways, Pipes World e TPP, a subpasta `Strips/` do acervo é idêntica às variantes `*-propositional-strips` (30, 50 e 30 problemas). `[FATO]` para a identidade. `[HIPÓTESE]` de que são a tradução distribuída pela IPC 2006 para planejadores sem suporte a recursos além de STRIPS, e de que foram usadas com os planejadores que precisavam disso; os scripts de execução em `comp/planners/scripts/` mostrariam quais.

6. **Logistics:** o `domain.pddl` difere do da IPC 2000 só pela ordem dos tipos em `(:types …)`; a hierarquia de tipos e o resto do arquivo são iguais. `[FATO]`

7. **Duas populações de dados (G9) ficam mais claras.** Os percentuais de competição (Tabelas 12 e 13) são sobre o conjunto **completo** da IPC daquele ano (por exemplo, 102 problemas de Blocks World em 2000), e os de execução própria são sobre o **subconjunto** que o autor usou (35). Misturar os dois na Tabela 14 compara denominadores diferentes. `[HIPÓTESE]`, porque falta saber sobre qual conjunto as tabelas das competições foram calculadas; o texto da dissertação diz apenas "porcentagem de problemas resolvidos".

## Zeno-travel e Elevator (PDDL ausentes no acervo)

Sem PDDL no acervo, a identificação vem do texto da dissertação, dos modelos do itSIMPLE e do que se sabe dos outros domínios. **O autor confirmou em 21/09/2026 que as variantes usadas são as identificadas aqui.**

**Zeno-travel** (IPC 2002): `zenotravel-strips-automatic`, 20 instâncias.
- O nível `strips` foi confirmado pelo autor. O modelo `ZenoTravelDomainv1.xml` tem `fuelLevel`, `capacity`, `currentLoad`, `fuelCapacity` e as ações `board`, `debark`, `fly`, `zoom`, `refuel`, compatível com as versões STRIPS e numérica.
- `automatic` (e não `hand-coded`) é **inferência por consistência**: o README de cada variante diz "For Automatic Planners" ou "For Hand-Coded Planners" (planejadores com conhecimento de domínio); Depots, Driver Log e Satellite, também da IPC 2002, foram todos obtidos da variante `automatic` no acervo; e os dez planejadores da dissertação são independentes de domínio. As duas variantes têm o **mesmo domínio**; só mudam as instâncias. `[HIPÓTESE]`

**Elevator** (IPC 2000, Miconic-10): `elevator-strips-simple-typed`, 150 instâncias.
- O nível `strips-simple` foi confirmado pelo autor. A IPC 2008 também tem um domínio "elevator", mas o README dele diz que foi "projetado do zero" (inspirado no Miconic da IPC 2), com elevadores rápidos e lentos e capacidade, o que não corresponde à descrição da dissertação (Miconic-10 da Schindler). `[FATO]` para a diferença entre os dois domínios. O modelo `ElevatorDomainv1.xml` tem `Passenger` com `origin`, `destin`, `boarded`, `served`, que corresponde ao Miconic **simples**, não ao *full*.
- `typed` (e não `untyped`) é **inferência por consistência**: Blocks World e Logistics, também da IPC 2000, foram usados na versão `typed` (`:requirements :strips :typing`), e o modelo do itSIMPLE é tipado. `[HIPÓTESE]`

**Instâncias usadas (confirmado pelo autor em 21/09/2026): N = 20 nos dois.** No Zeno-travel são as 20 do conjunto inteiro. No Elevator (150 instâncias na IPC 2000), N = 20 foi interpretado como as **20 primeiras** (instâncias 1 a 20 do repositório, originais `s1-0` a `s4-4`), de acordo com o padrão do acervo em todos os outros domínios (achado 1). `[HIPÓTESE]` para a leitura "20 primeiras", já que o autor informou só o N.

## Alcance do repositório

Cobre as IPCs de 1998 a 2014, **só a trilha determinística**, e nem tudo: em 2002 sem as variantes sem tipos, em 2004 só a trilha determinística. Para a Fase 3 (benchmarks 1998–2023), o repositório cobre até 2014; as edições de 2018 em diante precisam de outra fonte `[A CONFIRMAR]`.

## Como reproduzir

```bash
git clone https://github.com/potassco/pddl-instances.git /caminho/pddl-instances
git -C /caminho/pddl-instances checkout cf19edf7c53d1540ddbb396c642595e0926ee552
.venv/bin/python data/2010/scripts/mapear_benchmarks_ipc.py /caminho/pddl-instances
```

O repositório de instâncias **não é versionado aqui** (62 MB e sem licença declarada); é baixado no commit indicado.

## Implicações

- **Fase 0:** a pendência "localizar os PDDL de Zeno-travel e Elevator" está resolvida: existem, e as variantes foram confirmadas pelo autor. O subconjunto também está definido (N = 20).
- **Fase 3:** o repositório é candidato a fonte dos benchmarks (decisão a registrar no plano). Para replicar 2010 com o mesmo material, os subconjuntos estão em `benchmarks_ipc_instancias.csv`. Para uma replicação ampla, vale usar os conjuntos completos, mantendo a comparação separada por origem dos dados.
