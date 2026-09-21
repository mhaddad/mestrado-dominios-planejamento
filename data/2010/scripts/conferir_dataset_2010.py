"""Confere o dataset extraído da dissertação contra o script.sql do acervo.

Não altera nenhum dado: apenas lê e produz um relatório em
data/2010/conferencia/ (conferencia_sql.md + divergencias_*.csv).

Diferenças aqui NÃO significam que a dissertação está errada; significam que
duas fontes de 2009/2010 discordam e alguém precisa decidir qual vale.
"""
import csv
import io
import re
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SQL = RAIZ / "acervo-2010/planejadores_analise_resultados/comp/script.sql"
DADOS = RAIZ / "data/2010"
SAIDA = DADOS / "conferencia"

INSERT = re.compile(r"INSERT INTO (\w+)\s*(?:\(([^)]*)\))?\s*VALUES\((.*?)\);(.*)$")
FRAGMENTO = re.compile(r"(\w*)\s*VALUES\((.*?)\);")


FRAGMENTOS = []  # (n_linha, texto_solto, valores) — restos de INSERT truncados no script.sql


def le_sql():
    """Devolve {tabela: [bloco, ...]}; bloco = linhas INSERT contíguas da mesma tabela.

    O script.sql do acervo tem a mesma tabela em mais de um bloco (ex.: dominios_caracteristicas
    aparece duas vezes), então a separação por bloco importa para a conferência.
    Texto solto depois de um INSERT completo (edição manual) vai para FRAGMENTOS e
    NÃO entra nos blocos.
    """
    tabelas = defaultdict(list)
    ultima = None
    for n, linha in enumerate(SQL.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        m = INSERT.match(linha.strip())
        if not m:
            continue
        nome, cols, vals, resto = m.groups()
        if resto.strip():
            f = FRAGMENTO.search(resto)
            FRAGMENTOS.append((n, resto.strip(), f.group(2) if f else ""))
        campos = next(csv.reader(io.StringIO(vals), quotechar='"', skipinitialspace=True))
        if nome != ultima:
            tabelas[nome].append([])
            ultima = nome
        tabelas[nome][-1].append([c.strip() for c in campos])
    return tabelas


def le_csv(nome):
    with open(DADOS / nome, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def sem_acento(s):
    return (s.replace("é", "e").replace("É", "E").replace("ã", "a").replace("ç", "c"))


def grava(nome, cab, linhas):
    with open(SAIDA / nome, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(cab)
        w.writerows(linhas)


def main():
    SAIDA.mkdir(exist_ok=True)
    sql = le_sql()
    rel = ["# Conferência: dissertação (docx) × `script.sql` do acervo", "",
           "Gerado por `data/2010/scripts/conferir_dataset_2010.py`. Não editar à mão.", ""]

    # mapeamentos por id (a ordem de inserção do SQL coincide com a da dissertação)
    dominios = [d["dominio"] for d in le_csv("dominios.csv")][:10]
    planejadores = [p["planejador"] for p in le_csv("planejadores.csv")]
    metricas = [m["metrica"] for m in le_csv("metricas.csv")]
    tec_sql = {int(r[0]): r[1] for r in sql["tecnicas"][0]}
    pl_sql = {int(r[0]): r[1] for r in sql["planejadores"][0]}
    dom_sql = {int(r[0]): r[1] for r in sql["dominios"][0]}

    rel += ["## 0. Mapeamento de ids", "",
            "| id | domínio (SQL) → slug | planejador (SQL) → canônico |", "|---|---|---|"]
    for i in range(1, 11):
        rel.append(f"| {i} | {dom_sql[i]} → {dominios[i-1]} | {pl_sql[i]} → {planejadores[i-1]} |")
    rel.append("")

    # --- 1. classes das características ---------------------------------
    doc = {(r["dominio"], r["metrica"]): sem_acento(r["classe"]) for r in le_csv("metricas_dominios.csv")}
    blocos = sql["dominios_caracteristicas"]
    principal = {(int(d), int(c)): sem_acento(v) for d, c, v in blocos[0]}
    extra = {(int(d), int(c)): sem_acento(v) for d, c, v in blocos[1]} if len(blocos) > 1 else {}

    div = [[dominios[d - 1], metricas[c - 1], doc[(dominios[d - 1], metricas[c - 1])], v]
           for (d, c), v in sorted(principal.items()) if v != doc[(dominios[d - 1], metricas[c - 1])]]
    grava("divergencias_classes.csv", ["dominio", "metrica", "classe_docx", "classe_sql_bloco1"], div)

    extra_17 = {k: v for k, v in extra.items() if k[1] <= 17}
    extra_novas = {k: v for k, v in extra.items() if k[1] > 17}
    dif_extra = [[dominios[d - 1], metricas[c - 1], principal[(d, c)], v]
                 for (d, c), v in sorted(extra_17.items()) if principal.get((d, c)) != v]
    grava("divergencias_bloco2_vs_bloco1.csv", ["dominio", "metrica", "classe_bloco1", "classe_bloco2"], dif_extra)
    grava("caracteristicas_18_a_20.csv", ["dominio", "id_caracteristica", "classe"],
          [[dominios[d - 1], c, v] for (d, c), v in sorted(extra_novas.items())])
    rel += ["## 1. Classes Alto/Médio/Baixo (`dominios_caracteristicas`)", "",
            f"O SQL tem **{len(blocos)} blocos** desta tabela: "
            f"bloco 1 = {len(blocos[0])} linhas; bloco 2 = {len(blocos[1]) if len(blocos) > 1 else 0} linhas.", "",
            f"- **Bloco 1** cobre {len({d for d, _ in principal})} domínios × 17 características = {len(principal)} pares (esperado 170).",
            f"  - Coincide com a dissertação em {len(principal) - len(div)}/{len(principal)} pares; divergências: {len(div)} (`divergencias_classes.csv`).",
            f"- **Bloco 2** cobre os domínios {sorted({d for d, _ in extra})} com características 1 a {max(c for _, c in extra) if extra else 0}.",
            f"  - Nas características 1–17 ({len(extra_17)} pares) difere do bloco 1 em {len(dif_extra)} pares (`divergencias_bloco2_vs_bloco1.csv`).",
            f"  - As características **18, 19 e 20** ({len(extra_novas)} valores) não existem na tabela `caracteristicas` do SQL "
            f"nem na dissertação (`caracteristicas_18_a_20.csv`).", ""]

    # --- 2. eficiência e nota --------------------------------------------
    docx_ef = {(r["dominio"], r["planejador"]): r for r in le_csv("eficiencia_planejadores.csv")}
    linhas_ef, ok_e, ok_n, dif_arred = [], 0, 0, 0
    for pl, d, ef, nota in sql["planejamentos"][0]:
        chave = (dominios[int(d) - 1], planejadores[int(pl) - 1])
        r = docx_ef[chave]
        ef, nota = float(ef), float(nota)
        e_doc = float(r["eficiencia_completa_pct"])
        n_doc = float(r["nota"])
        if round(ef) == round(e_doc):
            ok_e += 1
            if abs(ef - e_doc) > 1e-9:
                dif_arred += 1
        else:
            linhas_ef.append([*chave, "eficiencia", e_doc, ef])
        if nota == n_doc:
            ok_n += 1
        else:
            linhas_ef.append([*chave, "nota", n_doc, nota])
    grava("eficiencia_precisa_sql.csv", ["dominio", "planejador", "eficiencia_pct_sql", "nota_sql"],
          [[dominios[int(d) - 1], planejadores[int(pl) - 1], ef, nota] for pl, d, ef, nota in sql["planejamentos"][0]])
    grava("divergencias_eficiencia.csv", ["dominio", "planejador", "campo", "valor_docx", "valor_sql"], linhas_ef)
    rel += ["## 2. Eficiência e nota (`planejamentos`)", "",
            f"- Linhas no SQL: {len(sql['planejamentos'][0])} (esperado 100)",
            f"- Eficiência coincide com a dissertação após arredondar para inteiro: {ok_e}/100 "
            f"(dos quais {dif_arred} têm casas decimais no SQL que a dissertação arredondou)",
            f"- Nota coincide exatamente: {ok_n}/100",
            f"- Divergências: {len(linhas_ef)} (detalhe em `divergencias_eficiencia.csv`)", ""]

    # --- 3. planejadores x técnicas --------------------------------------
    doc_pt = {(r["planejador"], r["tecnica"].replace(" ", "")) for r in le_csv("planejadores_tecnicas.csv")}
    blocos_pt = [{(planejadores[int(p) - 1], tec_sql[int(t)].replace(" ", "")) for p, t in b} for b in sql["planejadores_tecnicas"]]
    rel += ["## 3. Planejadores × técnicas (`planejadores_tecnicas`)", "",
            f"- Blocos no SQL: {len(blocos_pt)}, com {[len(b) for b in sql['planejadores_tecnicas']]} linhas.",
            f"- Blocos idênticos entre si: {len(blocos_pt) > 1 and blocos_pt[0] == blocos_pt[1]}",
            f"- Pares na dissertação (Tabela 4): {len(doc_pt)}"]
    for i, b in enumerate(blocos_pt, 1):
        rel.append(f"- Bloco {i} × dissertação: só no SQL = {len(b - doc_pt)}, só na dissertação = {len(doc_pt - b)}")
    rel.append("")
    grava("divergencias_tecnicas.csv", ["planejador", "tecnica", "so_em"],
          [[p, t, "sql_bloco1"] for p, t in sorted(blocos_pt[0] - doc_pt)] + [[p, t, "docx"] for p, t in sorted(doc_pt - blocos_pt[0])])

    rel += ["## 4. Anomalias de integridade do `script.sql`", ""]
    if FRAGMENTOS:
        for n, resto, vals in FRAGMENTOS:
            rel.append(f"- Linha {n}: texto solto após um INSERT completo: `{resto}`. "
                       "Parece o final de um `INSERT INTO dominios_caracteristicas` truncado por edição manual "
                       "`[HIPÓTESE]`. Não foi incluído em nenhum bloco.")
    else:
        rel.append("- Nenhuma.")
    rel.append("")
    (SAIDA / "conferencia_sql.md").write_text("\n".join(rel) + "\n", encoding="utf-8")
    print("\n".join(rel))


if __name__ == "__main__":
    main()
