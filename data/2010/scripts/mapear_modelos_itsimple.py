"""Mapa final domínio -> modelo itSIMPLE usado em 2010, com a evidência de cada escolha.

Reusa a contagem de comparar_modelos_itsimple.py (itSIMPLE 3.0.10, acervo) e acrescenta
auto-associações. Confronta com metricas_dominios.csv (Tabelas 8-9, 26, 32, 38).

Saída: data/2010/modelos_itsimple_2010.csv

Para Pathways e TPP a escolha do modelo foi feita pela comparação VISUAL das Figuras 26
(TPP) e 27 (Pathways) da dissertação com o conteúdo do XML (ver data/2010/figuras/):
  - TPP: a figura tem a classe Level -> TPPPropositionalDomainv1.xml (a versão Metric não tem Level)
  - Pathways: a figura tem as mesmas 6 classes, 2 associações, 2 generalizações e as 5
    ações do Agent que o XML; PathwaysSimplePreferencesDomainv1.xml tem contagens idênticas
    e não se distingue pela figura.
"""
import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.argv = sys.argv[:1]  # comparar_modelos_itsimple lê argv no import; aqui usa o padrão (acervo)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from comparar_modelos_itsimple import AUXILIARES, DADOS, EX, conta  # noqa: E402

MODELO = {  # domínio -> arquivo escolhido
    "blocksworld": "BlocksDomainv1.xml", "depots": "DepotDomain.xml", "driverlog": "DriverLogDomain.xml",
    "gripper": "GripperDomainv1.xml", "logistics": "LogisticDomainv1.xml", "mystery": "MysteryDomainv1.xml",
    "pathways": "PathwaysDomainv1.xml", "pipesworld": "PipesworldDomainv1.xml",
    "satellite": "SatelliteDomainv1.xml", "tpp": "TPPPropositionalDomainv1.xml",
    "storage": "StorageDomainv1.xml", "zenotravel": "ZenoTravelDomainv1.xml",
    "elevator": "ElevatorDomainv1.xml",
}
OBS = {
    "pathways": "Figura 27 = XML (6 classes, 2 associações, 2 generalizações, 5 ações do Agent). "
                "Tabela 9 tem 4 associações; XML e figura mostram 2. Ver achado G11. "
                "PathwaysSimplePreferencesDomainv1.xml tem contagens idênticas; escolhida a versão base.",
    "tpp": "Figura 26 = XML Propositional (tem a classe Level; o Metric não). "
           "Tabela 9 tem 2 generalizações; XML e figura mostram 4 pares filho-pai. Ver achado G12.",
}
M = {"classes": "Número total de Classes", "metodos": "Número total de Métodos",
     "associacoes": "Número total de Associações", "generalizacoes": "Número total de Generalização"}


def auto_associacoes(xml):
    raiz = ET.parse(xml).getroot()
    n = 0
    for ca in raiz.findall("elements/classAssociations/classAssociation"):
        ids = [e.get("element-id") for e in ca.findall("associationEnds/associationEnd")]
        n += len(ids) == 2 and ids[0] == ids[1]
    return n


def main():
    ref = {(r["dominio"], r["metrica"]): int(float(r["valor"])) for r in
           csv.DictReader(open(DADOS / "metricas_dominios.csv", encoding="utf-8")) if r["valor"]}
    linhas = []
    for dom, arq in MODELO.items():
        c = conta(EX / arq)
        tab = {k: ref[(dom, v)] for k, v in M.items()}
        dif = [k for k in M if k != "classes" and c[k] != tab[k]]
        if tab["classes"] not in (c["classes"], c["classes_sem_aux"]):
            dif.append("classes")
        aux = c["classes"] != c["classes_sem_aux"] and tab["classes"] == c["classes_sem_aux"]
        status = "bate_4_de_4" if not dif else f"diverge_em_{'+'.join(dif)}"
        linhas.append([dom, arq, c["classes"], c["classes_sem_aux"], tab["classes"], c["metodos"], tab["metodos"],
                       c["associacoes"], tab["associacoes"], c["generalizacoes"], tab["generalizacoes"],
                       auto_associacoes(EX / arq), aux, status, OBS.get(dom, "")])
    cab = ["dominio", "arquivo_itsimple_3_0_10", "classes_xml", "classes_xml_sem_auxiliares", "classes_tabela",
           "metodos_xml", "metodos_tabela", "associacoes_xml", "associacoes_tabela",
           "generalizacoes_xml", "generalizacoes_tabela", "auto_associacoes_xml",
           "so_bate_sem_classe_auxiliar", "status", "observacao"]
    with open(DADOS / "modelos_itsimple_2010.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(cab)
        w.writerows(linhas)
    for l in linhas:
        print(f"{l[0]:12} {l[1]:30} {l[13]}")


if __name__ == "__main__":
    main()
