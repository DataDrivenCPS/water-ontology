"""Membrane use and filtration are independent process classifications."""

import pytest
import shifty
from rdflib import Graph, Namespace
from rdflib.namespace import RDFS, SH

WATR = Namespace("https://watermetadata.org/ontology/watr#")
EX = Namespace("urn:membrane-classification#")


@pytest.mark.parametrize("process,filtration,solid_liquid", [
    ("Microfiltration", True, True),
    ("Ultrafiltration", True, True),
    ("ReverseOsmosis", True, False),
    ("ClosedCircuitReverseOsmosis", True, False),
    ("FeedReversalReverseOsmosis", True, False),
    ("OsmoticallyAssistedReverseOsmosis", True, False),
    ("MembraneDistillation", False, False),
    ("Electrodialysis", False, False),
])
def test_membrane_process_families(process, filtration, solid_liquid, water_graph):
    ancestors = set(water_graph.objects(WATR[f"Process-{process}"], RDFS.subClassOf * "+"))
    assert WATR["Process-MembraneProcess"] in ancestors
    assert WATR["Process-Separation"] in ancestors
    assert (WATR["Process-Filtration"] in ancestors) == filtration
    assert (WATR["Process-SolidLiquidSeparation"] in ancestors) == solid_liquid


@pytest.mark.parametrize("process,satisfies_filtration", [
    ("Microfiltration", True),
    ("Ultrafiltration", True),
    ("ReverseOsmosis", True),
    ("MembraneDistillation", False),
    ("Electrodialysis", False),
])
def test_explicit_process_overrides_filter_default(process, satisfies_filtration,
                                                   ontology_shapes_graph):
    # Additional processes are allowed on filters. A membrane process that is
    # not filtration cannot replace the class's required filtration process.
    data = Graph().parse(data=f"""
        @prefix : <urn:membrane-classification#> .
        @prefix watr: <https://watermetadata.org/ontology/watr#> .
        :filter a watr:Filter ; watr:hasProcess watr:Process-{process} .
    """, format="turtle")
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    processes = set(inferred.objects(EX.filter, WATR.hasProcess))
    assert WATR[f"Process-{process}"] in processes
    assert processes == {WATR[f"Process-{process}"]}
    _, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    missing_filtration = any(
        report.value(result, SH.focusNode) == EX.filter
        and report.value(result, SH.resultPath) == WATR.hasProcess
        for result in report.subjects(SH.resultSeverity, SH.Violation)
    )
    assert missing_filtration != satisfies_filtration


def test_membrane_example_inherits_only_general_removal(ontology_shapes_graph):
    data = Graph().parse("examples/membrane-process-classification.ttl")
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    example = Namespace("urn:example/membrane-process-classification#")
    for system in (example.microfiltrationUnit, example.distillationUnit,
                   example.electrodialysisUnit):
        assert set(inferred.objects(system, WATR.hasTreatmentObjective)) == {
            WATR["TreatmentObjective-ConstituentRemoval"]
        }
