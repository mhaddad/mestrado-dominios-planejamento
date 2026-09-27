"""EXP-22: tempo e memória do Nível 3 (EXP-05), a parte da F5 que 2010 não mediu.

Método fixado antes de ver os resultados (27/09/2026):
- Tempo: tempo de relógio de cada execução resolvida (`tempo_relogio_s`). Escore de tempo no mesmo formato
  do escore de qualidade do EXP-20: em cada problema, T* ÷ T, onde T* é o menor tempo entre os planejadores que
  resolveram; 0 se não resolveu. Os tempos têm piso de 1 s (1.787 de 2.263 planos saem em menos de 1 s, e abaixo
  disso a diferença é de inicialização do processo). Somado por domínio e dividido pelo número de problemas
  (0 a 1). LPG-TD: média das 3 sementes.
- Comparação com a cobertura: correlação de postos (Spearman) entre o escore de cobertura (fração resolvida)
  e o escore de tempo dos 10 planejadores, em cada domínio.
- Memória: memória máxima de cada execução (`memoria_max_kb`); execuções que chegam a 3,5 GB ou mais estão perto
  do teto dos binários de 32 bits (cerca de 4 GB) e são contadas por situação.
- Os limites de tempo diferem por planejador (calibrados, 7 a 13 min); o escore de tempo só compara resolvidos.

Entrada: experimentos/execucoes/nivel3-2010-gcp.csv (a mesma do EXP-19 e do EXP-20).
Uso: python3 experimentos/analise/nivel3_tempo_memoria.py
Saída: experimentos/analise/nivel3/tempo.csv (por par), tempo-ranking.csv (por domínio), memoria.csv (por planejador).
"""
import csv
import statistics
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ENTRADA = RAIZ / "experimentos/execucoes/nivel3-2010-gcp.csv"
SAIDA = RAIZ / "experimentos/analise/nivel3"
PISO_S = 1.0
TETO_32BIT_KB = int(3.5 * 1024 * 1024)


def postos(valores):
    ordem = sorted(range(len(valores)), key=lambda i: valores[i])
    p = [0.0] * len(valores)
    i = 0
    while i < len(ordem):
        j = i
        while j + 1 < len(ordem) and valores[ordem[j + 1]] == valores[ordem[i]]:
            j += 1
        for k in range(i, j + 1):
            p[ordem[k]] = (i + j) / 2 + 1
        i = j + 1
    return p


def spearman(a, b):
    pa, pb = postos(a), postos(b)
    ma, mb = statistics.mean(pa), statistics.mean(pb)
    num = sum((x - ma) * (y - mb) for x, y in zip(pa, pb))
    den = (sum((x - ma) ** 2 for x in pa) * sum((y - mb) ** 2 for y in pb)) ** 0.5
    return num / den if den else float("nan")


def main():
    with ENTRADA.open(encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))

    # tempo por (planejador, domínio, problema, semente); None se não resolveu
    tempo = {}
    problemas = defaultdict(set)
    sementes = defaultdict(set)
    for r in linhas:
        chave = (r["planejador"], r["dominio"], r["problema"])
        problemas[r["dominio"]].add(r["problema"])
        sementes[(r["planejador"], r["dominio"])].add(r["semente"])
        tempo[chave + (r["semente"],)] = (max(float(r["tempo_relogio_s"]), PISO_S)
                                          if r["situacao"] == "resolvido" else None)

    planejadores = sorted({r["planejador"] for r in linhas})
    dominios = sorted(problemas)
    melhor = {}
    for (pl, dom, prob, sem), t in tempo.items():
        if t is not None:
            melhor[(dom, prob)] = min(t, melhor.get((dom, prob), float("inf")))

    por_par = []
    for dom in dominios:
        for pl in planejadores:
            if (pl, dom) not in sementes:
                continue
            escores, cobertura, resolvidos_t = [], [], []
            for sem in sorted(sementes[(pl, dom)]):
                soma_t = soma_c = 0.0
                for prob in sorted(problemas[dom]):
                    t = tempo.get((pl, dom, prob, sem))
                    if t is not None:
                        soma_t += melhor[(dom, prob)] / t
                        soma_c += 1
                        resolvidos_t.append(t)
                n = len(problemas[dom])
                escores.append(soma_t / n)
                cobertura.append(soma_c / n)
            por_par.append({
                "planejador": pl, "dominio": dom, "problemas": len(problemas[dom]),
                "sementes": len(sementes[(pl, dom)]),
                "escore_cobertura": round(statistics.mean(cobertura), 3),
                "escore_tempo": round(statistics.mean(escores), 3),
                "tempo_mediano_resolvidos_s": round(statistics.median(resolvidos_t), 2) if resolvidos_t else "",
                "resolvidos_acima_de_60s": sum(t > 60 for t in resolvidos_t),
            })

    ranking = []
    for dom in dominios:
        pares = [p for p in por_par if p["dominio"] == dom]
        rho = spearman([p["escore_cobertura"] for p in pares], [p["escore_tempo"] for p in pares])
        lider_c = max(pares, key=lambda p: p["escore_cobertura"])
        lider_t = max(pares, key=lambda p: p["escore_tempo"])
        ranking.append({"dominio": dom, "planejadores": len(pares), "spearman_cobertura_tempo": round(rho, 2),
                        "lider_cobertura": lider_c["planejador"], "lider_tempo": lider_t["planejador"]})

    memoria = []
    for pl in planejadores:
        mem = [(int(r["memoria_max_kb"]), r["situacao"]) for r in linhas if r["planejador"] == pl and r["memoria_max_kb"]]
        res = [m for m, s in mem if s == "resolvido"]
        perto = defaultdict(int)
        for m, s in mem:
            if m >= TETO_32BIT_KB:
                perto[s] += 1
        memoria.append({
            "planejador": pl, "execucoes": len(mem),
            "memoria_mediana_resolvidos_mb": round(statistics.median(res) / 1024, 1) if res else "",
            "memoria_max_mb": round(max(m for m, _ in mem) / 1024, 1),
            "perto_do_teto_resolvido": perto["resolvido"], "perto_do_teto_estourou": perto["estourou"],
            "perto_do_teto_sem_plano": perto["sem-plano"],
        })

    SAIDA.mkdir(parents=True, exist_ok=True)
    for nome, dados in (("tempo.csv", por_par), ("tempo-ranking.csv", ranking), ("memoria.csv", memoria)):
        with (SAIDA / nome).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(dados[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(dados)

    print("Média nos domínios (cobertura, tempo):")
    for pl in planejadores:
        ps = [p for p in por_par if p["planejador"] == pl]
        print(f"  {pl:14} {statistics.mean(p['escore_cobertura'] for p in ps):.3f}  "
              f"{statistics.mean(p['escore_tempo'] for p in ps):.3f}  ({len(ps)} domínios)")
    print("Spearman cobertura × tempo por domínio:")
    for r in ranking:
        print(f"  {r['dominio']:12} {r['spearman_cobertura_tempo']:5}  líder cobertura {r['lider_cobertura']:14} "
              f"líder tempo {r['lider_tempo']}")
    print("Memória:")
    for m in memoria:
        print("  ", m)


if __name__ == "__main__":
    main()
