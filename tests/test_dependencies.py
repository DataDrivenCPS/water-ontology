"""The offline vocabulary must cover actual input terms and inference needs."""

from pathlib import Path

import shifty
from rdflib import Graph, Namespace, RDF, URIRef


ROOT = Path(__file__).resolve().parents[1]
QUDT = Namespace("http://qudt.org/schema/qudt/")
UNIT = Namespace("http://qudt.org/vocab/unit/")
QUANTITY_KIND = Namespace("http://qudt.org/vocab/quantitykind/")
S223 = Namespace("http://data.ashrae.org/standard223#")
EX = Namespace("urn:test:dependencies:")


def test_qudt_snapshot_covers_source_and_example_terms(qudt_graph: Graph):
    missing = set()
    for directory in ("ontology", "examples", "s223"):
        for path in (ROOT / directory).rglob("*.ttl"):
            graph = Graph().parse(path)
            for term in graph.all_nodes():
                if not isinstance(term, URIRef):
                    continue
                for namespace, cls in (
                    (UNIT, QUDT.Unit), (QUANTITY_KIND, QUDT.QuantityKind)
                ):
                    if str(term).startswith(str(namespace)):
                        if (term, RDF.type, cls) not in qudt_graph:
                            missing.add(term)
    assert not missing, (
        f"QUDT test snapshot is missing {sorted(map(str, missing))}; "
        "regenerate it with scripts/extract_test_qudt.py"
    )


def test_duration_quantity_kind_is_inferred_from_hour_unit(
    ontology_shapes_graph: Graph,
):
    data = Graph()
    data.add((EX.duration, RDF.type, S223.QuantifiableProperty))
    data.add((EX.duration, QUDT.hasUnit, UNIT.HR))
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    assert set(inferred.objects(EX.duration, QUDT.hasQuantityKind)) == {
        QUANTITY_KIND.Time
    }
