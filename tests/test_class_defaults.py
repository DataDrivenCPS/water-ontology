"""Defaults fill missing predicates without replacing authored values."""

from pathlib import Path

import pytest
import shifty
import yaml
from rdflib import Graph, Literal, Namespace, RDF


WATR = Namespace("https://watermetadata.org/ontology/watr#")
EX = Namespace("urn:example/class-defaults#")
ROOT = Path(__file__).resolve().parents[1]
PREFIXES = """
@prefix : <urn:example/class-defaults#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
"""


def _infer(data: str, water_graph: Graph, schema: str = "") -> Graph:
    shapes = water_graph + Graph().parse(data=PREFIXES + schema, format="ttl")
    graph = Graph().parse(data=PREFIXES + data, format="ttl")
    return shifty.infer(graph, shapes_graph=shapes).graph()


@pytest.mark.parametrize(
    ("equipment", "processes"),
    [
        ("StaticMixer", {"Process-Mixing"}),
        ("ImhoffTank", {"Process-Sedimentation"}),
        ("RapidSandFilter", {"Process-RapidSandFiltration"}),
        (
            "ElectroDialyticCrystallizer",
            {"Process-Electrodialysis", "Process-Crystallization"},
        ),
    ],
)
def test_equipment_gets_most_specific_process_defaults(
    water_graph: Graph, equipment: str, processes: set[str]
):
    inferred = _infer(f":unit a watr:{equipment} .", water_graph)
    assert set(inferred.objects(EX.unit, WATR.hasProcess)) == {
        WATR[process] for process in processes
    }


@pytest.mark.parametrize(
    "values",
    [
        "watr:Process-SlowSandFiltration",
        ":customProcess",
        "watr:Process-SlowSandFiltration, :customProcess",
    ],
)
def test_explicit_process_values_suppress_all_process_defaults(
    water_graph: Graph, values: str
):
    data = f":unit a watr:RapidSandFilter ; watr:hasProcess {values} ."
    original = Graph().parse(data=PREFIXES + data, format="ttl")
    inferred = _infer(data, water_graph)
    assert set(inferred.objects(EX.unit, WATR.hasProcess)) == set(
        original.objects(EX.unit, WATR.hasProcess)
    )


def test_objective_defaults_are_independent_of_explicit_process(water_graph: Graph):
    inferred = _infer(
        ":unit a :SpecialMixer ; watr:hasProcess :customProcess .",
        water_graph,
        """
        :SpecialMixer rdfs:subClassOf watr:StaticMixer ;
            sh:property [ sh:path :treatmentObjective ;
                          sh:defaultValue :Homogenization ] .
        """,
    )
    assert set(inferred.objects(EX.unit, WATR.hasProcess)) == {EX.customProcess}
    assert set(inferred.objects(EX.unit, EX.treatmentObjective)) == {
        EX.Homogenization
    }


def test_explicit_objective_suppresses_defaults_but_process_is_inferred(
    water_graph: Graph,
):
    inferred = _infer(
        ':unit a :SpecialMixer ; :treatmentObjective "site-specific goal" .',
        water_graph,
        """
        :SpecialMixer rdfs:subClassOf watr:StaticMixer ;
            sh:property [ sh:path :treatmentObjective ;
                          sh:defaultValue :Homogenization ] .
        """,
    )
    assert set(inferred.objects(EX.unit, WATR.hasProcess)) == {WATR["Process-Mixing"]}
    assert set(inferred.objects(EX.unit, EX.treatmentObjective)) == {
        Literal("site-specific goal")
    }


def test_most_specific_defaults_work_with_explicit_ancestor_types(water_graph: Graph):
    inferred = _infer(
        ":unit a watr:RapidSandFilter, watr:Filter .", water_graph
    )
    assert set(inferred.objects(EX.unit, WATR.hasProcess)) == {
        WATR["Process-RapidSandFiltration"]
    }


def test_unrelated_class_defaults_are_combined(water_graph: Graph):
    inferred = _infer(
        ":unit a watr:StaticMixer, watr:Screen .", water_graph
    )
    assert set(inferred.objects(EX.unit, WATR.hasProcess)) == {
        WATR["Process-Mixing"], WATR["Process-Screening"]
    }


def test_class_constraints_alone_do_not_invent_defaults(water_graph: Graph):
    inferred = _infer(":unit a watr:UnitProcess .", water_graph)
    assert not list(inferred.objects(EX.unit, WATR.hasProcess))


@pytest.mark.parametrize(
    "declaration",
    [
        "sh:deactivated true ; sh:path :goal ; sh:defaultValue :value",
        "sh:path [ sh:inversePath :goal ] ; sh:defaultValue :value",
    ],
)
def test_inactive_or_complex_property_shapes_are_ignored(
    water_graph: Graph, declaration: str
):
    inferred = _infer(
        ":unit a :Equipment .", water_graph,
        f":Equipment sh:property [ {declaration} ] .",
    )
    assert not list(inferred.objects(EX.unit, EX.goal))
    assert not list(inferred.subjects(EX.goal, EX.unit))


def test_inactive_subclass_default_does_not_hide_active_ancestor(water_graph: Graph):
    inferred = _infer(
        ":unit a :Equipment .", water_graph,
        """
        :Equipment rdfs:subClassOf watr:StaticMixer ;
            sh:deactivated true ;
            sh:property [ sh:path watr:hasProcess ; sh:defaultValue :custom ] .
        """,
    )
    assert set(inferred.objects(EX.unit, WATR.hasProcess)) == {WATR["Process-Mixing"]}


def test_inference_is_idempotent_and_does_not_mutate_input(water_graph: Graph):
    data = Graph().parse(data=PREFIXES + ":unit a watr:StaticMixer .", format="ttl")
    inferred = shifty.infer(data, shapes_graph=water_graph).graph()
    again = shifty.infer(inferred, shapes_graph=water_graph).graph()
    assert set(data) == {(EX.unit, RDF.type, WATR.StaticMixer)}
    assert set(again) == set(inferred)


def test_defaults_example_infers_missing_values(water_graph: Graph):
    data = Graph().parse(ROOT / "examples/class-defaults.ttl")
    inferred = shifty.infer(data, shapes_graph=water_graph).graph()
    assert set(inferred.objects(EX.mixer, WATR.hasProcess)) == {WATR["Process-Mixing"]}
    assert set(inferred.objects(EX.customMixer, WATR.hasProcess)) == {
        EX.siteMixingProcess
    }


@pytest.mark.parametrize(
    ("template_name", "process"),
    [
        ("uv-reactor", "Process-UVDisinfection"),
        ("contact-chamber", "Process-Disinfection"),
        ("flocculation-basin", "Process-Flocculation"),
        ("sedimentation-tank", "Process-Sedimentation"),
        ("filtration", "Process-Filtration"),
        ("disinfection-unit", "Process-Disinfection"),
        ("chlorination-unit", "Process-Chlorination"),
        ("rapid-sand-filter", "Process-RapidSandFiltration"),
    ],
)
def test_equipment_templates_infer_their_process(
    water_graph: Graph, template_name: str, process: str
):
    templates = yaml.safe_load(
        (ROOT / "libraries/templates/equipment.yml").read_text()
    )
    data = Graph().parse(data=templates[template_name]["body"], format="ttl")
    equipment = Namespace("urn:___param___#").name
    assert not list(data.objects(equipment, WATR.hasProcess))

    inferred = shifty.infer(data, shapes_graph=water_graph).graph()
    assert set(inferred.objects(equipment, WATR.hasProcess)) == {WATR[process]}


def test_ro_example_infers_its_process(water_graph: Graph):
    data = Graph().parse(ROOT / "examples/ro-mixture-test.ttl")
    ro = Namespace("urn:example/ro-mixture-test#").ro
    assert not list(data.objects(ro, WATR.hasProcess))

    inferred = shifty.infer(data, shapes_graph=water_graph).graph()
    assert set(inferred.objects(ro, WATR.hasProcess)) == {
        WATR["Process-ReverseOsmosis"]
    }
