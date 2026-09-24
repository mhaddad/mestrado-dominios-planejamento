"""Nível 1 da reexecução (auditoria/reexecucao.md): reproduz por script o método de 2010
sobre os dados publicados e compara cada etapa com as tabelas da dissertação.

Etapas reproduzidas:
  3. discretização das métricas (Tabelas 10–11, 26, 32, 38);
  5. conversão da eficiência em nota 0–10 (Tabelas 16–17);
  7. relação característica × técnica (Tabelas 19–20);
  8. relevância das características (Tabelas 21–23);
  validação: médias por técnica e planejador e *ranking* nos domínios de validação
  (Tabelas 27–30, 33–36, 39–42).

Uso: python experimentos/analise/reproducao_2010.py
Saídas: experimentos/analise/reproducao-2010/*.csv e um resumo na saída padrão.
"""
import csv
import statistics
import unicodedata
from collections import defaultdict
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data/2010"
TAB = DADOS / "extraido"
SAIDA = RAIZ / "experimentos/analise/reproducao-2010"


def norm(s: str) -> str:
    """Chave de comparação: sem acento, minúsculas, sem espaço, hífen nem ponto."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.lower().replace("heuristc", "heurist").replace("heuristic", "heurist")
    s = "".join(c for c in s if c.isalnum())
    # As Tabelas 19–25 rotulam três métricas de outro modo que as Tabelas 8–11
    for de, para in (("numeromediodeatoresporcasodeuso", "numerodecasosdeusoporatores"),
                     ("agregacaoparestodoparte", "agregacao"), ("generalizacaoparespaifilho", "generalizacao")):
        s = s.replace(de, para)
    return s


def meio_para_cima(x: float, casas: int = 0) -> float:
    q = Decimal(1).scaleb(-casas)
    return float(Decimal(str(x)).quantize(q, ROUND_HALF_UP))


def num(s: str) -> float:
    return float(s.strip().replace(",", ".").replace("%", ""))


def ler(nome):
    with (DADOS / nome).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def tabela(n):
    with (TAB / f"tabela_{n:02d}.csv").open(encoding="utf-8") as f:
        return list(csv.reader(f))


def gravar(nome, linhas):
    SAIDA.mkdir(parents=True, exist_ok=True)
    with (SAIDA / nome).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)


# ---------------------------------------------------------------- etapa 3
def discretizar(metricas):
    """Regra aplicada em 2010 (inferida; ver achado G23): em cada métrica, o menor valor dos
    domínios de treino é Baixo, o maior é Alto, o resto é Médio. Domínios de validação: Baixo
    se <= mínimo do treino, Alto se >= máximo do treino."""
    faixa = defaultdict(list)
    for r in metricas:
        if r["papel"] == "treino":
            faixa[r["metrica"]].append(num(r["valor"]))
    linhas = []
    for r in metricas:
        lo, hi = min(faixa[r["metrica"]]), max(faixa[r["metrica"]])
        v = num(r["valor"])
        classe = "Baixo" if v <= lo else "Alto" if v >= hi else "Médio"
        linhas.append({"dominio": r["dominio"], "papel": r["papel"], "metrica": r["metrica"], "valor": v,
                       "classe_publicada": r["classe"], "classe_reproduzida": classe,
                       "confere": classe == r["classe"]})
    return linhas


# ---------------------------------------------------------------- etapa 5
def notas(eficiencia):
    precisa = {(r["dominio"], r["planejador"]): num(r["eficiencia_pct_sql"])
               for r in csv.DictReader((DADOS / "conferencia/eficiencia_precisa_sql.csv").open(encoding="utf-8"))}
    linhas = []
    for r in eficiencia:
        p = precisa.get((r["dominio"], r["planejador"]), num(r["eficiencia_completa_pct"]))
        nota = int(meio_para_cima(p / 10))
        linhas.append({"dominio": r["dominio"], "planejador": r["planejador"], "eficiencia_precisa_pct": p,
                       "nota_publicada": int(r["nota"]), "nota_reproduzida": nota, "confere": nota == int(r["nota"])})
    return linhas


# ---------------------------------------------------------------- etapa 7
def relacao(classes, notas_, tecnicas):
    """Média das notas dos pares domínio × planejador em que o domínio tem a característica
    (métrica + classe) e o planejador usa a técnica (Tabela 18 de 2010)."""
    tec_de = defaultdict(set)
    for r in tecnicas:
        tec_de[r["planejador"]].add(r["tecnica"])
    nota = {(r["dominio"], r["planejador"]): r["nota_publicada"] for r in notas_}
    carac = defaultdict(set)  # característica -> domínios de treino que a têm
    for r in classes:
        if r["papel"] == "treino":
            carac[f"{r['metrica']} {r['classe_publicada']}"].add(r["dominio"])
    todas_tec = sorted({t for ts in tec_de.values() for t in ts})
    linhas = []
    for c, doms in carac.items():
        for t in todas_tec:
            vals = [n for (d, p), n in nota.items() if d in doms and t in tec_de[p]]
            if vals:
                linhas.append({"caracteristica": c, "tecnica": t, "n_pares": len(vals),
                               "media": round(statistics.mean(vals), 4)})
    return linhas


def comparar_relacao(rel):
    publicada = {}
    for n in (19, 20):
        t = tabela(n)
        cab = t[0]
        for linha in t[1:]:
            for j in range(1, len(cab)):
                if j < len(linha) and linha[j].strip():
                    try:
                        publicada[(norm(linha[0]), norm(cab[j]))] = num(linha[j])
                    except ValueError:
                        pass  # cabeçalho repetido na quebra de página
    linhas = []
    for r in rel:
        k = (norm(r["caracteristica"]), norm(r["tecnica"]))
        if k in publicada:
            rep = meio_para_cima(r["media"])
            linhas.append({**r, "publicada": publicada[k], "reproduzida_inteira": rep,
                           "confere": rep == publicada[k]})
    faltam = set(publicada) - {(norm(r["caracteristica"]), norm(r["tecnica"])) for r in rel}
    return linhas, faltam


# ---------------------------------------------------------------- etapa 8
def valores_publicados_19_20():
    """Tabelas 19–20 publicadas: característica normalizada -> {técnica normalizada: valor}."""
    linhas = defaultdict(dict)
    for n in (19, 20):
        t = tabela(n)
        for linha in t[1:]:
            for j in range(1, len(t[0])):
                try:
                    linhas[norm(linha[0])][norm(t[0][j])] = num(linha[j])
                except (ValueError, IndexError):
                    pass
    return linhas


def relevancia(pub):
    """Diferença entre o maior e o menor valor da característica nas 11 técnicas:
    até 3 não relevante, 4–5 pouco relevante, 6 ou mais muito relevante (texto de 2010)."""
    publicada = {}
    for n, classe in ((21, "não relevante"), (22, "pouco relevante"), (23, "muito relevante")):
        for linha in tabela(n)[1:]:
            try:
                publicada[norm(linha[0])] = (classe, num(linha[2]), num(linha[3]), num(linha[4]), num(linha[1]))
            except (ValueError, IndexError):
                pass
    linhas = []
    for c, (classe, menor, maior, dif, var) in publicada.items():
        v = list(pub[c].values())
        d = max(v) - min(v)
        rep = "não relevante" if d <= 3 else "pouco relevante" if d <= 5 else "muito relevante"
        linhas.append({"caracteristica": c, "diferenca_publicada": dif, "diferenca_reproduzida": d,
                       "classe_publicada": classe, "classe_reproduzida": rep,
                       "confere": rep == classe and (min(v), max(v)) == (menor, maior),
                       "variancia_publicada": var})
    return linhas


def marcas(pub, corte=3):
    """Tabelas 24–25: [HIPÓTESE] 'x' quando a diferença entre as classes Baixo/Médio/Alto da
    métrica, na técnica, é >= corte. A regra não está escrita em 2010."""
    linhas = []
    for n in (24, 25):
        t = tabela(n)
        for linha in t[1:]:
            for j in range(1, len(t[0])):
                m, tec = norm(linha[0]), norm(t[0][j])
                v = [pub[m + c][tec] for c in ("baixo", "medio", "alto") if tec in pub.get(m + c, {})]
                rep = bool(v) and max(v) - min(v) >= corte
                pubx = linha[j].strip().lower() == "x"
                linhas.append({"metrica": linha[0], "tecnica": t[0][j], "marca_publicada": pubx,
                               "marca_reproduzida": rep, "confere": rep == pubx})
    return linhas


# ---------------------------------------------------------------- validação
VALIDACAO = {"storage": (27, 28, 29, 30), "zenotravel": (33, 34, 35, 36), "elevator": (39, 40, 41, 42)}
NOME_PLANEJADOR = {"fastd": "fastdownward", "fastdownward": "fastdownward"}


def validacao(pub, tecnicas):
    tec_de = defaultdict(set)
    for r in tecnicas:
        tec_de[norm(r["planejador"])].add(norm(r["tecnica"]))
    celulas, medias, planejadores, rankings = [], [], [], []
    for dom, (ta, tb, tp, tr) in VALIDACAO.items():
        media_tec = {}
        for n in (ta, tb):
            t = tabela(n)
            cab = t[0]
            for j in range(2, len(cab)):
                tec = norm(cab[j])
                vals = []
                for linha in t[1:]:
                    if norm(linha[0]).startswith("media"):
                        pub_media = num(linha[j])
                        continue
                    if not linha[j].strip():
                        continue
                    try:
                        num(linha[j])
                    except ValueError:
                        continue  # cabeçalho repetido
                    esperado = pub[norm(linha[0] + linha[1])].get(tec)
                    celulas.append({"dominio": dom, "caracteristica": f"{linha[0]} {linha[1]}", "tecnica": cab[j],
                                    "publicada": num(linha[j]), "tabela_19_20": esperado,
                                    "confere": esperado == num(linha[j])})
                    vals.append(num(linha[j]))
                m = statistics.mean(vals)
                media_tec[tec] = m
                casas = len(str(pub_media).split(".")[1]) if "." in str(pub_media) else 0
                medias.append({"dominio": dom, "tecnica": cab[j], "publicada": pub_media, "reproduzida": round(m, 3),
                               "confere": abs(pub_media - m) <= 0.5 * 10 ** -2 + 1e-9 or
                               abs(pub_media - int(m * 100) / 100) < 1e-9})
        t = tabela(tp)
        cab = t[0]
        pub_pl = {norm(cab[j]): num(t[-1][j]) for j in range(1, len(cab))}
        nota_pl = {}
        for pl, ts in tec_de.items():
            chave = NOME_PLANEJADOR.get(pl, pl)
            vals = [media_tec[x] for x in ts if x in media_tec]
            nota_pl[chave] = statistics.mean(vals)
        for pl_pub, v in pub_pl.items():
            chave = NOME_PLANEJADOR.get(pl_pub, pl_pub)
            planejadores.append({"dominio": dom, "planejador": pl_pub, "publicada": v,
                                 "reproduzida": round(nota_pl.get(chave, float("nan")), 3)})
        ordem_pub = [norm(l[1]) for l in tabela(tr)[1:]]
        ordem_rep = sorted(nota_pl, key=lambda p: -nota_pl[p])
        rankings.append({"dominio": dom, "ordem_publicada": " > ".join(ordem_pub),
                         "ordem_reproduzida": " > ".join(ordem_rep),
                         "confere": [NOME_PLANEJADOR.get(p, p) for p in ordem_pub] == ordem_rep})
    return celulas, medias, planejadores, rankings


def main():
    metricas = ler("metricas_dominios.csv")
    disc = discretizar(metricas)
    gravar("discretizacao.csv", disc)
    print(f"Etapa 3, discretização: {sum(r['confere'] for r in disc)} de {len(disc)} classes reproduzidas")
    for r in disc:
        if not r["confere"]:
            print(f"   diverge: {r['dominio']} / {r['metrica']} = {r['valor']}: "
                  f"publicada {r['classe_publicada']}, regra {r['classe_reproduzida']}")

    nt = notas(ler("eficiencia_planejadores.csv"))
    gravar("notas.csv", nt)
    print(f"Etapa 5, nota 0–10: {sum(r['confere'] for r in nt)} de {len(nt)} notas reproduzidas")

    rel = relacao(disc, nt, ler("planejadores_tecnicas.csv"))
    comp, faltam = comparar_relacao(rel)
    gravar("relacao-caracteristica-tecnica.csv", comp)
    print(f"Etapa 7, relação característica × técnica: {sum(r['confere'] for r in comp)} de {len(comp)} "
          f"células reproduzidas; {len(faltam)} células publicadas sem correspondente")
    pub = valores_publicados_19_20()
    rv = relevancia(pub)
    gravar("relevancia.csv", rv)
    print(f"Etapa 8, relevância (Tabelas 21–23): {sum(r['confere'] for r in rv)} de {len(rv)} características "
          f"reproduzidas (classe, menor, maior); a coluna 'Variância' não se reproduz por nenhuma fórmula testada")
    mk = marcas(pub)
    gravar("marcas-impacto.csv", mk)
    print(f"Etapa 8, marcas de impacto (Tabelas 24–25, regra inferida): {sum(r['confere'] for r in mk)} de {len(mk)}")

    cel, med, pl, rk = validacao(pub, ler("planejadores_tecnicas.csv"))
    gravar("validacao-celulas.csv", cel)
    gravar("validacao-medias-tecnicas.csv", med)
    gravar("validacao-planejadores.csv", pl)
    gravar("validacao-rankings.csv", rk)
    print(f"Validação: {sum(r['confere'] for r in cel)} de {len(cel)} células copiadas das Tabelas 19–20; "
          f"{sum(r['confere'] for r in med)} de {len(med)} médias por técnica; "
          f"{sum(r['confere'] for r in rk)} de {len(rk)} rankings na mesma ordem")
    return disc, nt, rel, comp


if __name__ == "__main__":
    main()
