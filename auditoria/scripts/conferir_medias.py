"""Recalcula as linhas MÉDIA das tabelas extraídas da dissertação de 2010.

Para cada tabela em data/2010/extraido/ com uma linha cujo primeiro campo é
"MÉDIA", recalcula a média de cada coluna sobre as células numéricas não
vazias das linhas acima dela e compara com o valor publicado (tolerância de
meia unidade na última casa decimal publicada).

Também confere se os rankings publicados (tabelas 30, 36, 42) copiam as
médias das tabelas de origem (29, 35, 41).

Saídas: auditoria/extracao/conferencia-medias.csv e
auditoria/extracao/conferencia-transcricao-ranking.csv
Uso: python auditoria/scripts/conferir_medias.py
"""
import csv
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TABELAS = RAIZ / "data/2010/extraido"
SAIDA = RAIZ / "auditoria/extracao/conferencia-medias.csv"


def numero(celula: str):
    try:
        return float(celula.strip().replace(",", "."))
    except ValueError:
        return None


def main() -> None:
    saida = []
    for arq in sorted(TABELAS.glob("tabela_*.csv")):
        linhas = list(csv.reader(arq.open(encoding="utf-8")))
        idx = [i for i, l in enumerate(linhas) if l and l[0].strip().upper() in ("MÉDIA", "MEDIA")]
        if not idx:
            continue
        m = idx[0]
        cab = linhas[0]
        for j in range(1, len(cab)):
            publicado = linhas[m][j].strip() if j < len(linhas[m]) else ""
            p = numero(publicado)
            if p is None:
                continue
            valores = [v for l in linhas[1:m] if j < len(l) and (v := numero(l[j])) is not None]
            if not valores:
                continue
            calc = sum(valores) / len(valores)
            casas = len(publicado.split(",")[1]) if "," in publicado else 0
            tol = 0.5 * 10 ** -casas + 1e-9
            truncado = abs(p - int(calc * 10 ** casas + 1e-9) / 10 ** casas) < 1e-9
            saida.append({
                "tabela": arq.stem, "coluna": cab[j], "n_celulas": len(valores),
                "publicado": publicado, "recalculado": f"{calc:.3f}".replace(".", ","),
                "diferenca": f"{p - calc:+.3f}".replace(".", ","),
                "situacao": "confere" if abs(p - calc) <= tol else ("truncamento" if truncado else "diverge"),
            })
    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(saida[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(saida)
    div = [s for s in saida if s["situacao"] == "diverge"]
    trunc = sum(s["situacao"] == "truncamento" for s in saida)
    print(f"{len(saida)} médias conferidas; {trunc} só truncadas; {len(div)} divergem")
    for s in div:
        print(f"  {s['tabela']} {s['coluna']}: publicado {s['publicado']}, recalculado {s['recalculado']} ({s['diferenca']})")

    # Ordem das colunas (ranking) pela média publicada e pela recalculada
    for tabela in sorted({s["tabela"] for s in div}):
        cols = [s for s in saida if s["tabela"] == tabela]
        num = lambda v: float(v.replace(",", "."))
        pub = [c["coluna"] for c in sorted(cols, key=lambda c: -num(c["publicado"]))]
        rec = [c["coluna"] for c in sorted(cols, key=lambda c: -num(c["recalculado"]))]
        print(f"  {tabela} ordem publicada:   {pub}")
        print(f"  {tabela} ordem recalculada: {rec}{'  (MUDA)' if pub != rec else ''}")

    transcricao(saida)


def transcricao(medias) -> None:
    apelido = {"Fast D.": "Fast Downward"}
    linhas = []
    for origem, ranking in ((29, 30), (35, 36), (41, 42)):
        fonte = {apelido.get(m["coluna"], m["coluna"]): m for m in medias if m["tabela"] == f"tabela_{origem}"}
        with (TABELAS / f"tabela_{ranking}.csv").open(encoding="utf-8") as f:
            for l in list(csv.reader(f))[1:]:
                pl, pub = l[1].strip(), l[2].strip()
                m = fonte[pl]
                casas = len(pub.split(",")[1]) if "," in pub else 0
                p_rank, p_orig, calc = numero(pub), numero(m["publicado"]), numero(m["recalculado"])
                linhas.append({
                    "ranking": f"tabela_{ranking}", "planejador": pl, "no_ranking": pub,
                    "na_origem": m["publicado"], "recalculado": m["recalculado"],
                    "situacao": "confere" if abs(round(p_orig, casas) - p_rank) < 1e-9 or abs(round(calc, casas) - p_rank) < 1e-9 else "diverge",
                })
    with (RAIZ / "auditoria/extracao/conferencia-transcricao-ranking.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    div = [l for l in linhas if l["situacao"] == "diverge"]
    print(f"Transcrição para os rankings: {len(linhas)} valores; {len(div)} divergem")
    for l in div:
        print(f"  {l['ranking']} {l['planejador']}: ranking {l['no_ranking']}, origem {l['na_origem']}, recalculado {l['recalculado']}")


if __name__ == "__main__":
    main()
