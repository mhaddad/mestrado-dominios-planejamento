"""EXP-23: versão ofuscada das instâncias do X1 (nomes trocados por rótulos sem significado).

Troca, em cada domínio e na sua instância p01, todos os nomes definidos pelo modelador (nome do domínio e do
problema, tipos, constantes, predicados, ações, variáveis e objetos) por rótulos aleatórios de 5 letras, com
semente fixa. Palavras reservadas do PDDL (`define`, `and`, `not`, `object`, `either` etc.) e tudo o que começa
com `:` ficam como estão; comentários são retirados. O significado lógico não muda: só os nomes. É a mesma ideia
do Mystery Blocksworld de `valmeekam2023planbench`, aplicada aos 8 domínios do X1.

Os arquivos ofuscados vão para experimentos/ferramentas/x1-ofuscado/ (fora do git, como o Autoscale de origem);
o mapa de nomes, para llm/x1-planejador/resultados/ofuscacao-mapa.csv.

Uso: python3 llm/x1-planejador/ofuscar.py            (gera os arquivos e o mapa)
     python3 llm/x1-planejador/ofuscar.py conferir   (equivalência: plano do lama-first traduzido pelo mapa
                                                      tem de ser válido no VAL do outro lado, nos dois sentidos)
"""
import csv
import random
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "llm/x1-planejador"))
import x1_planejador as X1  # noqa: E402

DESTINO = RAIZ / "experimentos/ferramentas/x1-ofuscado"
MAPA = RAIZ / "llm/x1-planejador/resultados/ofuscacao-mapa.csv"
SEMENTE = 2026
RESERVADAS = {"define", "domain", "problem", "and", "not", "or", "either", "object", "forall", "exists", "when",
              "imply", "number"}
NOME = re.compile(r"(?<![:\w?-])([a-z][a-z0-9_-]*)")
VARIAVEL = re.compile(r"\?([a-z][a-z0-9_-]*)")
CONSOANTES, VOGAIS = "bcdfghjklmnpqrstvwxz", "aeiou"


def rotulos(rng, usados):
    while True:
        r = "".join(rng.choice(CONSOANTES if i % 2 == 0 else VOGAIS) for i in range(5))
        if r not in usados and r not in RESERVADAS:
            usados.add(r)
            return r


def limpar(texto):
    return "\n".join(l.split(";", 1)[0].rstrip() for l in texto.lower().splitlines())


def main():
    rng = random.Random(SEMENTE)
    usados = set()
    linhas_mapa = []
    for dominio in X1.DOMINIOS:
        dom, prob = X1.arquivos(dominio)
        textos = [limpar(dom.read_text(encoding="utf-8")), limpar(prob.read_text(encoding="utf-8"))]
        mapa, mapa_var = {}, {}
        for t in textos:
            for n in NOME.findall(t):
                if n not in RESERVADAS and n not in mapa:
                    mapa[n] = rotulos(rng, usados)
            for v in VARIAVEL.findall(t):
                if v not in mapa_var:
                    mapa_var[v] = rotulos(rng, usados)
        saida = []
        for t in textos:
            t = VARIAVEL.sub(lambda m: "?" + mapa_var[m.group(1)], t)
            t = NOME.sub(lambda m: m.group(1) if m.group(1) in RESERVADAS else mapa[m.group(1)], t)
            saida.append(t)
        pasta = DESTINO / dominio
        pasta.mkdir(parents=True, exist_ok=True)
        (pasta / "domain.pddl").write_text(saida[0] + "\n", encoding="utf-8")
        (pasta / f"{X1.INSTANCIA}.pddl").write_text(saida[1] + "\n", encoding="utf-8")
        for original, novo in sorted(mapa.items()):
            linhas_mapa.append({"dominio": dominio, "tipo": "nome", "original": original, "ofuscado": novo})
        for original, novo in sorted(mapa_var.items()):
            linhas_mapa.append({"dominio": dominio, "tipo": "variavel", "original": "?" + original, "ofuscado": "?" + novo})
        print(f"{dominio:22s} {len(mapa):4d} nomes, {len(mapa_var):3d} variáveis")
    MAPA.parent.mkdir(parents=True, exist_ok=True)
    with MAPA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas_mapa[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas_mapa)


def conferir():
    """Traduz o plano do lama-first do original para o ofuscado e de volta, e valida cada um no VAL."""
    import subprocess
    import tempfile
    mapas = {}
    with MAPA.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["tipo"] == "nome":
                mapas.setdefault(r["dominio"], {})[r["original"]] = r["ofuscado"]
    ok_total = True
    for dominio in X1.DOMINIOS:
        ida = mapas[dominio]
        volta = {v: k for k, v in ida.items()}
        planos = {}
        for lado in (False, True):
            X1.OFUSCADO = lado
            dom, prob = X1.arquivos(dominio)
            with tempfile.TemporaryDirectory() as tmp:
                subprocess.run([sys.executable, str(X1.FD), "--overall-time-limit", "300", "--alias", "lama-first",
                                str(dom), str(prob)], cwd=tmp, capture_output=True, text=True)
                planos[lado] = [l.strip().lower() for l in (Path(tmp) / "sas_plan").read_text().splitlines()
                                if l.startswith("(")]
        resultado = []
        for origem, destino, mapa in ((False, True, ida), (True, False, volta)):
            traduzido = ["(" + " ".join(mapa[x] for x in l.strip("()").split()) + ")" for l in planos[origem]]
            X1.OFUSCADO = destino
            valido, msg = X1.validar(dominio, traduzido)
            ok_total &= valido
            resultado.append(msg)
        X1.OFUSCADO = False
        print(f"{dominio:22s} original→ofuscado: {resultado[0]:10s} ofuscado→original: {resultado[1]:10s} "
              f"(tamanhos {len(planos[False])} e {len(planos[True])})")
    print("equivalência conferida" if ok_total else "FALHA na equivalência")
    return ok_total


if __name__ == "__main__":
    if sys.argv[1:] == ["conferir"]:
        sys.exit(0 if conferir() else 1)
    main()
