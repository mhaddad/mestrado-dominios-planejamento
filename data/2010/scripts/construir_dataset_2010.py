"""Constrói o dataset de 2010 (CSVs "tidy") a partir das tabelas extraídas do docx.

Entrada : data/2010/extraido/tabela_NN.csv  (gerado por extrair_dissertacao.py)
Saída   : data/2010/*.csv

Fonte de verdade: as tabelas PUBLICADAS na dissertação. O script.sql do acervo
é usado apenas para conferência (ver conferir_dataset_2010.py).

Convenções das saídas: UTF-8, vírgula como separador, ponto decimal,
eficiência em pontos percentuais (25% -> 25), célula vazia = dado ausente.
"""
import csv
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
EXTRAIDO = RAIZ / "data/2010/extraido"
SAIDA = RAIZ / "data/2010"

# --- vocabulário canônico -------------------------------------------------

# rótulo na dissertação -> (slug, nome, papel, pasta em acervo-2010/.../comp)
DOMINIOS = {
    "Blocks W.":   ("blocksworld", "Blocks World", "treino", "blocksworld"),
    "Depots":      ("depots", "Depots", "treino", "depots"),
    "DriverLog":   ("driverlog", "Driver Log", "treino", "driverlog"),
    "Gripper":     ("gripper", "Gripper", "treino", "gripper"),
    "Logistic W.": ("logistics", "Logistics", "treino", "logistic"),
    "Mystery":     ("mystery", "Mystery", "treino", "mystery"),
    "Pathways":    ("pathways", "Pathways", "treino", "pathways"),
    "Pipes W.":    ("pipesworld", "Pipesworld", "treino", "pipesworld"),
    "Satellite":   ("satellite", "Satellite", "treino", "sattelite"),
    "TPP":         ("tpp", "TPP", "treino", "tpp"),
    "Storage":     ("storage", "Storage", "validacao", "storage"),
    "Zeno-travel": ("zenotravel", "Zeno-travel", "validacao", ""),
    "Elevator":    ("elevator", "Elevator", "validacao", ""),
}

# variantes de grafia nas tabelas -> nome canônico
PLANEJADORES = {
    "Blackbox": "Blackbox", "IPP": "IPP", "FF": "FF", "R": "R", "LPG": "LPG",
    "Fast Downward": "Fast Downward", "Fast Fownward": "Fast Downward", "Fast D.": "Fast Downward",
    "YAHSP": "YAHSP", "SGPlan": "SGPlan",
    "SATPlan": "SATPlan", "SatPlan": "SATPlan",
    "MAXPLAN": "MaxPlan", "MaxPlan": "MaxPlan",
}
PASTA_PLANEJADOR = {  # comp/planners/<pasta>
    "Blackbox": "blackbox", "IPP": "ipp", "FF": "ffv-2.3", "R": "r", "LPG": "lpg",
    "Fast Downward": "fastdownward", "YAHSP": "yahsp", "SGPlan": "sgplan6",
    "SATPlan": "satplan", "MaxPlan": "maxplan",
}

FAMILIA = {  # diagrama UML de origem (Tabelas 5, 6 e 7)
    "casos_de_uso": ["Número de Atores", "Número de Casos de Uso", "Número de Casos de Uso por Atores"],
    "classes": ["Número total de Classes", "Número total de Atributos", "Número total de Métodos",
                "Número total de Associações", "Número total de Agregação", "Número total de Generalização",
                "Número total de Hierarquias", "DIT Máximo", "HAgg Máximo"],
    "estados": ["Número total de estados", "Número total de ações de entrada", "Número total de ações de saída",
                "Número total de ações", "Número total de transições"],
}
ORDEM_METRICAS = [m for f in ("casos_de_uso", "classes", "estados") for m in FAMILIA[f]]
FAMILIA_DA_METRICA = {m: f for f, ms in FAMILIA.items() for m in ms}

# Correções aprovadas pelo autor em 21/09/2026, com base nas figuras da dissertação (Figuras 26 e 27)
# e nos modelos itSIMPLE. O valor publicado NÃO é sobrescrito: entra em `valor_corrigido`.
# (dominio, metrica) -> (valor_corrigido, fonte, impacto_na_classe)
CORRECOES = {
    ("pathways", "Número total de Associações"): (
        2,
        "Figura 27 e PathwaysDomainv1.xml mostram 2 associações (synthesisReaction e next); a Tabela 9 diz 4",
        "Classe publicada: Médio. O valor 2 fica abaixo de todos os valores 'Baixo' observados (3); "
        "como a classe é monotônica com o valor nas 10 linhas, a classe passa provavelmente a Baixo "
        "[inferência]. Recalcular junto com o método de discretização (Fase 3).",
    ),
    ("tpp", "Número total de Generalização"): (
        4,
        "Figura 26 e TPPPropositionalDomainv1.xml mostram 4 pares filho-pai; a Tabela 9 diz 2",
        "Classe publicada: Médio. O valor 4 tem classe Médio em Logistics; sem mudança de classe "
        "[inferência]. Recalcular junto com o método de discretização (Fase 3).",
    ),
}

# linhas de cabeçalho repetidas no meio das tabelas por quebra de página
CABECALHOS_REPETIDOS = {"Métricas / Domínios", "Técnicas / Planejadores"}


# --- utilidades -----------------------------------------------------------

def le(n):
    with open(EXTRAIDO / f"tabela_{n:02d}.csv", encoding="utf-8", newline="") as f:
        return list(csv.reader(f))


def num(s):
    """'1,00' -> 1.0 ; '25%' -> 25 ; '' -> None ; '1°' -> 1"""
    s = s.strip().replace("°", "").replace("%", "").replace(",", ".")
    if s == "":
        return None
    v = float(s)
    return int(v) if "." not in s else v


def fmt(v):
    """Vazio para ausente; inteiro quando o float é integral (1.0 -> 1)."""
    if v is None:
        return ""
    return int(v) if isinstance(v, float) and v.is_integer() else v


def grava(nome, cabecalho, linhas):
    with open(SAIDA / nome, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(cabecalho)
        w.writerows(linhas)
    print(f"{nome}: {len(linhas)} linhas")


def grade(n):
    """Tabela 'linha x coluna' -> (rótulos_de_coluna, {(linha, coluna): célula})."""
    t = le(n)
    colunas = [c.strip() for c in t[0][1:]]
    d = {}
    for linha in t[1:]:
        if linha[0].strip() in CABECALHOS_REPETIDOS:
            continue
        for c, cel in zip(colunas, linha[1:]):
            d[(linha[0].strip(), c)] = cel
    return colunas, d


def canon_pl(nome):
    return PLANEJADORES[nome.strip()]


# --- 1. dimensões ---------------------------------------------------------

def dimensoes():
    grava("dominios.csv", ["dominio", "nome", "papel", "pasta_acervo"],
          [[s, n, p, pasta] for s, n, p, pasta in DOMINIOS.values()])
    grava("planejadores.csv", ["planejador", "pasta_acervo"],
          [[p, PASTA_PLANEJADOR[p]] for p in PASTA_PLANEJADOR])
    grava("metricas.csv", ["metrica", "diagrama_uml"],
          [[m, FAMILIA_DA_METRICA[m]] for m in ORDEM_METRICAS])


# --- 2. métricas dos domínios --------------------------------------------

def metricas():
    saida = {}  # (dominio, metrica) -> [valor, classe]
    # treino: valores brutos (T8-T9) e discretizados (T10-T11)
    for t_bruto, t_disc in ((8, 10), (9, 11)):
        cols, bruto = grade(t_bruto)
        _, disc = grade(t_disc)
        for col in cols:
            slug = DOMINIOS[col][0]
            for m in ORDEM_METRICAS:
                saida[(slug, m)] = [num(bruto[(m, col)]), disc[(m, col)].strip()]
    # validação: valor e classe na mesma tabela (T26 Storage, T32 Zeno, T38 Elevator)
    for n, rotulo in ((26, "Storage"), (32, "Zeno-travel"), (38, "Elevator")):
        slug = DOMINIOS[rotulo][0]
        for linha in le(n)[1:]:
            saida[(slug, linha[0].strip())] = [num(linha[1]), linha[2].strip()]
    papel = {v[0]: v[2] for v in DOMINIOS.values()}
    ordem_dom = [v[0] for v in DOMINIOS.values()]
    linhas = [[d, papel[d], m, fmt(saida[(d, m)][0]), saida[(d, m)][1],
               CORRECOES[(d, m)][0] if (d, m) in CORRECOES else ""]
              for d in ordem_dom for m in ORDEM_METRICAS]
    grava("metricas_dominios.csv", ["dominio", "papel", "metrica", "valor", "classe", "valor_corrigido"], linhas)
    grava("correcoes_2010.csv",
          ["dominio", "metrica", "valor_publicado", "valor_corrigido", "fonte", "impacto_na_classe", "aprovado_por", "data"],
          [[d, m, fmt(saida[(d, m)][0]), v, fonte, impacto, "autor", "21/09/2026"]
           for (d, m), (v, fonte, impacto) in CORRECOES.items()])


# --- 3. eficiência dos planejadores (domínios de treino) -------------------

def eficiencia():
    fontes = {"comp": (12, 13), "completa": (14, 15), "nota": (16, 17)}
    dados = {}  # (dominio, planejador) -> {comp, completa, nota}
    for chave, tabs in fontes.items():
        for t in tabs:
            _, g = grade(t)
            for (pl, col), cel in g.items():
                slug = DOMINIOS[col][0]
                dados.setdefault((slug, canon_pl(pl)), {})[chave] = num(cel)
    ordem_dom = [v[0] for v in DOMINIOS.values() if v[2] == "treino"]
    linhas = []
    for d in ordem_dom:
        for p in PASTA_PLANEJADOR:
            r = dados[(d, p)]
            origem = "competicao" if r["comp"] is not None else "execucao_propria"
            linhas.append([d, p, fmt(r["comp"]), fmt(r["completa"]), fmt(r["nota"]), origem])
    grava("eficiencia_planejadores.csv",
          ["dominio", "planejador", "eficiencia_competicao_pct", "eficiencia_completa_pct", "nota", "origem_do_dado"],
          linhas)


# --- 4. planejadores x técnicas ------------------------------------------

def tecnicas():
    linhas = []
    for linha in le(4)[1:]:
        pl = canon_pl(linha[0])
        for tec in linha[1].split(","):
            tec = re.sub(r"\s*-\s*", "-", tec.strip())  # 'State -Space' -> 'State-Space'
            linhas.append([pl, tec])
    grava("planejadores_tecnicas.csv", ["planejador", "tecnica"], linhas)


# --- 5. validação (Storage, Zeno-travel, Elevator) -------------------------

def validacao():
    linhas = []
    for dom, t_rank, t_real in (("storage", 30, 31), ("zenotravel", 36, 37), ("elevator", 42, 43)):
        prop = {canon_pl(l[1]): (num(l[0]), num(l[2])) for l in le(t_rank)[1:]}
        real = {canon_pl(l[1]): (num(l[0]), num(l[2])) for l in le(t_real)[1:]}
        for p in PASTA_PLANEJADOR:
            linhas.append([dom, p, prop[p][0], prop[p][1], real[p][0], real[p][1]])
    grava("validacao_ranking.csv",
          ["dominio", "planejador", "posicao_proposta", "media_proposta", "posicao_real", "nota_real"], linhas)


if __name__ == "__main__":
    dimensoes()
    metricas()
    eficiencia()
    tecnicas()
    validacao()
