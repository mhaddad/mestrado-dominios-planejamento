"""Liga os problemas da IPC 2011 no WebPlan aos arquivos PDDL locais (Fase 4B).

O WebPlan identifica cada problema por um hash próprio (a coluna `problema` de
ipc2011_problemas.csv), que não é o SHA-1 do arquivo. Mas o repositório arquivado no
Software Heritage tem uma pasta `problems/prob-<hash>/` com o `problem.pddl` de cada
problema, e a API devolve o SHA-1 do arquivo sem baixá-lo. Esse SHA-1 é comparado com o dos
arquivos das pastas *-opt11-* e *-sat11-* do downward-benchmarks incluído no Planner Museum
(experimentos/ferramentas/planner-museum/benchmarks/downward-benchmarks).

Primeira versão (27/09/2026) comparava com o pddl-instances (experimentos/benchmarks/ipc/).
Descartada: lá a pasta do floortile ótimo de 2011 é cópia da satisficing, e elevators e
openstacks só casavam depois de normalizar espaços. Com o downward-benchmarks, os 150
problemas consultados até a troca casaram todos por SHA-1.

A API anônima permite 120 requisições por hora, e cada problema custa uma. O script guarda o
que já consultou em brutos/2011/webplan/sha1_problemas.json e para quando a cota acaba; basta
rodá-lo de novo mais tarde para continuar. Ordem: todos os problemas do visitall (cujos
arquivos originais não têm número), depois um problema de cada par trilha × domínio, depois o
resto.

Ligação na saída:
  sha1    o SHA-1 do problem.pddl do WebPlan é igual ao do arquivo local (conferido)
  sha1+numero  o SHA-1 casa com mais de um arquivo idêntico da pasta; vale o do número
  texto   o SHA-1 difere, mas o problem.pddl do WebPlan (baixado para brutos/2011/webplan/
          problemas/) é igual ao arquivo do número original depois de tirar comentários,
          espaços e diferenças de maiúsculas
  numero  ainda não consultado; ligado pelo número final do nome do arquivo (ex.:
          pfile03-011.pddl -> 11, opt-p08-015.pddl -> 15, p07.pddl -> 7).
No visitall o número não serve: os arquivos se chamam problemNN-full/half.pddl. O visitall só é
ligado por SHA-1 (os 40 problemas foram consultados).

Uso: python data/ipc-2011-2023/scripts/webplan_2011_arquivos.py
Saída: data/ipc-2011-2023/ipc2011_arquivos.csv
"""

import csv
import hashlib
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PDDL = Path(__file__).resolve().parents[3] / "experimentos/ferramentas/planner-museum/benchmarks/downward-benchmarks"
CACHE = RAIZ / "brutos" / "2011" / "webplan" / "sha1_problemas.json"
TEXTOS = RAIZ / "brutos" / "2011" / "webplan" / "problemas"
CONTEUDO = "https://archive.softwareheritage.org/api/1/content/sha1:{}/raw/"
SAIDA = RAIZ / "ipc2011_arquivos.csv"
# Pasta `problems` da revisão 531fd510 (ver brutos/2011/webplan/PROVENIENCIA.txt).
PROBLEMAS = "https://archive.softwareheritage.org/api/1/directory/69e6fa176c8f0e4029badc417852b88c18024987/"
TRILHAS = {"seq-opt": "opt11", "seq-sat": "sat11"}


def pasta(trilha, dominio):
    return PDDL / f"{dominio}-{TRILHAS[trilha]}-strips"


def problemas_locais(trilha, dominio):
    return [a for a in pasta(trilha, dominio).glob("*.pddl")
            if not a.name.startswith("domain") and not a.stem.endswith("-domain")]


def por_numero_original(trilha, dominio):
    """número final do nome do arquivo -> arquivo local."""
    return {int(re.findall(r"\d+", a.stem)[-1]): a for a in problemas_locais(trilha, dominio)}


def normalizado(texto):
    return re.sub(r";[^\n]*", "", texto).lower().split()


class CotaEsgotada(Exception):
    pass


def baixar(url):
    try:
        with urllib.request.urlopen(url) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code == 429:
            raise CotaEsgotada from e
        raise


def main():
    problemas = list(csv.DictReader((RAIZ / "ipc2011_problemas.csv").open(encoding="utf-8")))
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    vistos, ordem = set(), []
    for p in problemas:
        if p["dominio"] == "visitall":
            ordem.append(p)
    for p in problemas:
        if (p["trilha"], p["dominio"]) not in vistos and p["dominio"] != "visitall":
            vistos.add((p["trilha"], p["dominio"]))
            ordem.append(p)
    ordem += [p for p in problemas if p not in ordem]

    locais = {}
    for trilha in TRILHAS:
        for dominio in {p["dominio"] for p in problemas}:
            for arq in problemas_locais(trilha, dominio):
                locais.setdefault(hashlib.sha1(arq.read_bytes()).hexdigest(), []).append(arq)
    consultas = 0
    TEXTOS.mkdir(parents=True, exist_ok=True)
    try:
        for p in ordem:
            if p["problema"] not in cache:
                cache[p["problema"]] = json.loads(baixar(PROBLEMAS + f"prob-{p['problema']}/problem.pddl/"))["checksums"]["sha1"]
                consultas += 1
            sha1 = cache[p["problema"]]
            if sha1 not in locais and not (TEXTOS / f"{sha1}.pddl").exists():
                (TEXTOS / f"{sha1}.pddl").write_bytes(baixar(CONTEUDO.format(sha1)))
                consultas += 1
    except CotaEsgotada:
        print("cota da API esgotada; rode de novo mais tarde para continuar")
    CACHE.write_text(json.dumps(cache, indent=0, sort_keys=True))
    linhas, divergencias = [], []
    for p in problemas:
        numero = (None if p["dominio"] == "visitall"
                  else por_numero_original(p["trilha"], p["dominio"]).get(int(p["numero"])))
        sha1 = cache.get(p["problema"])
        if sha1:
            candidatos = [a for a in locais.get(sha1, []) if a.parent == pasta(p["trilha"], p["dominio"])]
            texto = TEXTOS / f"{sha1}.pddl"
            if len(candidatos) > 1 and numero in candidatos:
                # Arquivos idênticos na mesma pasta (ex.: parcprinter-opt11 p11 e p18): o SHA-1
                # não decide; vale o número, que é um dos candidatos.
                arquivo, ligacao = numero, "sha1+numero"
            elif len(candidatos) == 1:
                arquivo, ligacao = candidatos[0], "sha1"
                if numero is not None and numero != arquivo:
                    divergencias.append((p["trilha"], p["dominio"], p["numero"], arquivo.name, numero.name))
            elif not candidatos and texto.exists() and numero is not None:
                arquivo, ligacao = numero, "texto"
                if normalizado(texto.read_text(errors="replace")) != normalizado(numero.read_text(errors="replace")):
                    divergencias.append((p["trilha"], p["dominio"], p["numero"], "texto difere", numero.name))
            elif not candidatos and numero is not None:
                arquivo, ligacao = numero, "numero"
            else:
                raise SystemExit(f"ligação ambígua para {p}: {candidatos}")
        elif numero is not None:
            arquivo, ligacao = numero, "numero"
        else:
            arquivo, ligacao = None, ""
        linhas.append({"trilha": p["trilha"], "dominio": p["dominio"], "problema": p["problema"],
                       "numero": p["numero"], "arquivo": arquivo.name if arquivo else "",
                       "ligacao": ligacao})
    with SAIDA.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    conta = {}
    for l in linhas:
        conta[l["ligacao"] or "sem ligação"] = conta.get(l["ligacao"] or "sem ligação", 0) + 1
    print(f"{consultas} consultas nesta execução; ligações: {conta}")
    print(f"divergências entre SHA-1 e número original: {len(divergencias)}")
    for d in divergencias:
        print("  ", *d)
    print(f"{len(linhas)} linhas -> {SAIDA.name}")


if __name__ == "__main__":
    main()
