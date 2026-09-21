"""Compara contagens extraídas dos XML do itSIMPLE (examples/) com as métricas de 2010.

Objetivo: descobrir qual versão de cada modelo candidato corresponde à medição da
dissertação. Só compara o que dá para contar direto do XML; as métricas de 2010 foram
contadas VISUALMENTE e MANUALMENTE (etapa 2 do método), então bater em tudo não é esperado.

Métricas comparadas (nome na dissertação <- contagem no XML):
  Número total de Classes       <- elements/classes/class com <type> != Primitive
  Número total de Métodos       <- elements/classes/class/operators/operator
  Número total de Associações   <- elements/classAssociations/classAssociation
  Número total de Generalização <- classes não primitivas com <generalization id> não vazio
Classes auxiliares "Utility" e "Global" (sem semântica de domínio) são testadas de duas formas:
contadas e não contadas. Se a dissertação só bate sem elas, a marca é '+' em vez de '*'.
Atributos não são comparados: na dissertação parecem incluir extremos de associação
(Blocks World: 2 atributos no XML contra 5 na Tabela 8).
Saída: data/2010/conferencia/modelos_itsimple.csv e resumo no stdout.
"""
import csv
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
EX = RAIZ / "acervo-2010/planejadores_analise_resultados/itSIMPLE/examples"
DADOS = RAIZ / "data/2010"

CANDIDATOS = {
    "blocksworld": ["BlocksDomainv1.xml", "BlocksDomainv2.xml", "BlocksDomain_tf.xml"],
    "depots": ["DepotDomain.xml", "DepotDomainv2.xml"],
    "driverlog": ["DriverLogDomain.xml"],
    "gripper": ["GripperDomainv1.xml"],
    "logistics": ["LogisticDomainv1.xml", "LogisticDomainv2.xml"],
    "mystery": ["MysteryDomainv1.xml"],
    "pathways": ["PathwaysDomainv1.xml", "PathwaysSimplePreferencesDomainv1.xml"],
    "pipesworld": ["PipesworldDomainv1.xml"],
    "satellite": ["SatelliteDomainv1.xml"],
    "tpp": ["TPPMetricDomainv1.xml", "TPPPropositionalDomainv1.xml"],
    "storage": ["StorageDomainv1.xml"],
    "zenotravel": ["ZenoTravelDomainv1.xml", "ZenoTravelDomainv2.xml"],
    "elevator": ["ElevatorDomain.xml", "ElevatorDomainv0.xml", "ElevatorDomainv1.xml"],
}
AUXILIARES = {"Utility", "Global"}
COMPARAR = {
    "classes": "Número total de Classes",
    "metodos": "Número total de Métodos",
    "associacoes": "Número total de Associações",
    "generalizacoes": "Número total de Generalização",
}


def conta(xml):
    raiz = ET.parse(xml).getroot()
    classes = [c for c in raiz.findall("elements/classes/class")
               if (c.findtext("type") or "").strip() != "Primitive"]
    gen = [c for c in classes if c.find("generalization") is not None and c.find("generalization").get("id")]
    metodos = sum(len(c.findall("operators/operator")) for c in classes)
    assoc = len(raiz.findall("elements/classAssociations/classAssociation"))
    aux = [c for c in classes if (c.findtext("name") or "").strip() in AUXILIARES]
    return {"classes": len(classes), "classes_sem_aux": len(classes) - len(aux),
            "metodos": metodos, "associacoes": assoc, "generalizacoes": len(gen)}


def main():
    ref = {}
    for r in csv.DictReader(open(DADOS / "metricas_dominios.csv", encoding="utf-8")):
        ref[(r["dominio"], r["metrica"])] = float(r["valor"]) if r["valor"] else None
    linhas = []
    print(f"{'domínio':12} {'arquivo':38} " + " ".join(f"{k[:5]:>11}" for k in COMPARAR) + "  acertos")
    for dom, arqs in CANDIDATOS.items():
        for a in arqs:
            c = conta(EX / a)
            ok = 0
            cel = []
            for k, m in COMPARAR.items():
                alvo = ref[(dom, m)]
                bate = alvo is not None and int(alvo) == c[k]
                ajustado = k == "classes" and not bate and alvo is not None and int(alvo) == c["classes_sem_aux"]
                ok += bate or ajustado
                marca = "*" if bate else ("+" if ajustado else " ")
                cel.append(f"{c[k]:>3} vs {int(alvo) if alvo is not None else '-':>2}{marca}")
            print(f"{dom:12} {a:38} " + " ".join(f"{x:>11}" for x in cel) + f"  {ok}/4")
            linhas.append([dom, a, *[c[k] for k in COMPARAR], c["classes_sem_aux"], *[ref[(dom, m)] for m in COMPARAR.values()], ok])
    with open(DADOS / "conferencia/modelos_itsimple.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dominio", "arquivo", *[f"xml_{k}" for k in COMPARAR], "xml_classes_sem_aux", *[f"dissertacao_{k}" for k in COMPARAR], "acertos_de_4"])
        w.writerows(linhas)


if __name__ == "__main__":
    main()
