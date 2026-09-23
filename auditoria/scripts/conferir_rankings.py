"""Reproduz a "taxa de acerto" do ranking de planejadores de 2010.

O texto (linhas 1454 e 1768 de data/2010/extraido/texto.md) diz que o
ranking teve 50% de acerto em Storage e em Elevator, sem definir a medida.
Este script compara o ranking previsto (tabelas 30, 36, 42) com o observado
(tabelas 31, 37, 43) por quatro medidas:

- posicao_exata: fração de posições com o mesmo planejador nos dois rankings
  (hipótese de como 2010 calculou; depende da ordem dos empates publicada);
- posicao_com_empates: a posição conta como acerto se o planejador previsto
  tem a mesma nota observada que o planejador que ocupa a posição;
- top5_conjunto: fração dos 5 primeiros previstos que estão entre os 5
  primeiros observados;
- spearman: correlação de postos com postos médios nos empates.
- acerta_melhor: o 1.º previsto tem a maior nota observada.

Cada medida é calculada também para uma linha de base sem características de
domínio: o ranking pela nota média de cada planejador nos 10 domínios de
treino (data/2010/eficiencia_planejadores.csv). Se a linha de base empata
com o método, a validação não mostra ganho das características.

Saída: auditoria/extracao/conferencia-rankings.csv
Uso: python auditoria/scripts/conferir_rankings.py
"""
import csv
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TAB = RAIZ / "data/2010/extraido"
SAIDA = RAIZ / "auditoria/extracao/conferencia-rankings.csv"
PARES = {"Storage": (30, 31, "50%"), "Zeno-travel": (36, 37, "não informada"), "Elevator": (42, 43, "50%")}


def nome(p: str) -> str:
    """Grafia única dos planejadores (as tabelas usam SatPlan; o dataset, SATPlan)."""
    p = p.strip()
    return {"SATPlan": "SatPlan"}.get(p, p)


def ler(n: int):
    with (TAB / f"tabela_{n:02d}.csv").open(encoding="utf-8") as f:
        linhas = list(csv.reader(f))[1:]
    return [(nome(l[1]), float(l[2].replace(",", "."))) for l in linhas]


def postos(valores):
    ordem = sorted(range(len(valores)), key=lambda i: -valores[i])
    r = [0.0] * len(valores)
    i = 0
    while i < len(ordem):
        j = i
        while j + 1 < len(ordem) and valores[ordem[j + 1]] == valores[ordem[i]]:
            j += 1
        for k in range(i, j + 1):
            r[ordem[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(a, b):
    ra, rb = postos(a), postos(b)
    ma, mb = sum(ra) / len(ra), sum(rb) / len(rb)
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    va = sum((x - ma) ** 2 for x in ra) ** 0.5
    vb = sum((y - mb) ** 2 for y in rb) ** 0.5
    return cov / (va * vb)


def linha_de_base():
    with (RAIZ / "data/2010/eficiencia_planejadores.csv").open(encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    notas = {}
    for l in linhas:
        notas.setdefault(nome(l["planejador"]), []).append(float(l["nota"]))
    medias = {p: sum(v) / len(v) for p, v in notas.items()}
    return sorted(medias.items(), key=lambda x: -x[1])


def main() -> None:
    saida = []
    base = linha_de_base()
    print("Linha de base (nota média nos 10 domínios de treino):", [(p, round(m, 2)) for p, m in base])
    for dominio, (tp, to, declarado) in PARES.items():
      for metodo, prev in (("ranking-2010", ler(tp)), ("linha-de-base", base)):
        obs = ler(to)
        nota = dict(obs)
        nomes_prev = [p for p, _ in prev]
        nomes_obs = [p for p, _ in obs]
        exata = sum(a == b for a, b in zip(nomes_prev, nomes_obs)) / len(prev)
        empates = sum(nota[p] == obs[i][1] for i, p in enumerate(nomes_prev)) / len(prev)
        top5 = len(set(nomes_prev[:5]) & set(nomes_obs[:5])) / 5
        rho = spearman([m for _, m in prev], [nota[p] for p in nomes_prev])
        melhor = nota[nomes_prev[0]] == max(nota.values())
        saida.append({
            "dominio": dominio, "ranking": metodo, "tabela_prevista": f"tabela_{tp}" if metodo == "ranking-2010" else "eficiencia_planejadores.csv", "tabela_observada": f"tabela_{to}",
            "acerto_declarado": declarado if metodo == "ranking-2010" else "", "posicao_exata": f"{exata:.0%}",
            "posicao_com_empates": f"{empates:.0%}", "top5_conjunto": f"{top5:.0%}",
            "spearman": f"{rho:.2f}".replace(".", ","), "acerta_melhor": "sim" if melhor else "não",
            "empatados_no_topo": sum(v == max(nota.values()) for v in nota.values()),
        })
    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(saida[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(saida)
    for s in saida:
        print(s)
    previstos = {d: [p for p, _ in ler(tp)] for d, (tp, _, _) in PARES.items()}
    dominios = list(previstos)
    for i in range(len(dominios)):
        for j in range(i + 1, len(dominios)):
            a, b = previstos[dominios[i]], previstos[dominios[j]]
            rho = spearman([-a.index(p) for p in a], [-b.index(p) for p in a])
            print(f"Spearman entre rankings previstos {dominios[i]} × {dominios[j]}: {rho:.2f}")


if __name__ == "__main__":
    main()
