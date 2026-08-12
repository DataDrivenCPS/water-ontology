"""Materializing an instance's process and outcome from its class.

``water/class-defaults.ttl`` holds a SHACL-AF rule: typing something as a
``watr:GravityThickener`` already says it thickens by settling, so the rule
writes those triples onto the instance rather than making every model repeat
them.

The file is part of the ontology's import closure, and ``shifty.validate`` runs
SHACL-AF rules as part of validation, so the rule fires wherever the ontology is
used. The last two tests pin what that costs and what it buys.
"""

import pytest
import shifty
from rdflib import Graph, Namespace


SH = Namespace("http://www.w3.org/ns/shacl#")
WATR = Namespace("urn:nawi-water-ontology#")
EX = Namespace("urn:defaults#")

PREFIX = "@prefix watr: <urn:nawi-water-ontology#> .\n@prefix ex: <urn:defaults#> .\n"


def _materialize(body: str, shapes: Graph) -> Graph:
    data = Graph().parse(data=PREFIX + body, format="ttl")
    return shifty.infer(data, shapes_graph=shapes).graph()


def test_process_and_outcome_are_both_materialized(ontology_shapes_graph):
    """The outcome comes from watr:Thickener and the process from the subclass,
    so a bare instance picks up one from each level of the hierarchy."""
    out = _materialize("ex:gt a watr:GravityThickener .\n", ontology_shapes_graph)
    assert (EX.gt, WATR.hasProcess, WATR["Process-Sedimentation"]) in out
    assert (EX.gt, WATR.hasTreatmentObjective, WATR["TreatmentObjective-Thickening"]) in out


def test_renamed_uv_unit_gets_both_axes(ontology_shapes_graph):
    out = _materialize("ex:uv a watr:UltravioletLightUnit .\n", ontology_shapes_graph)
    assert (EX.uv, WATR.hasProcess, WATR["Process-UVIrradiation"]) in out
    assert (EX.uv, WATR.hasTreatmentObjective, WATR["TreatmentObjective-Disinfection"]) in out


def test_a_stated_specific_value_is_not_overridden(ontology_shapes_graph):
    """Default semantics, not additive: Process-Microfiltration already satisfies
    watr:Filter's Process-Filtration requirement, so nothing is added for it."""
    out = _materialize(
        "ex:mf a watr:MicrofiltrationUnit ;\n"
        "    watr:hasProcess watr:Process-Microfiltration .\n",
        ontology_shapes_graph,
    )
    assert (EX.mf, WATR.hasProcess, WATR["Process-Filtration"]) not in out
    assert (EX.mf, WATR.hasProcess, WATR["Process-Microfiltration"]) in out


def test_materialized_instances_validate(ontology_shapes_graph):
    """What the rule produces must be a model the ontology accepts."""
    out = _materialize("ex:gt2 a watr:GravityThickener .\n", ontology_shapes_graph)
    valid, _, text = shifty.validate(
        out, shacl_graph=ontology_shapes_graph, minimum_severity="violation"
    )
    assert valid, text


# --- what including the rule in the closure changes --------------------------


def test_a_bare_typed_instance_is_now_complete(ontology_shapes_graph):
    """The point of shipping the rule in the closure.

    Nothing but the type, and the model validates: the requirement is met by
    derivation, because an instance of a class that requires Process-Sedimentation
    sediments whether or not the model troubles to say so.
    """
    data = Graph().parse(
        data=PREFIX + "ex:bare a watr:GravityThickener .\n", format="ttl"
    )
    valid, _, text = shifty.validate(
        data, shacl_graph=ontology_shapes_graph, minimum_severity="violation"
    )
    assert valid, text


def test_the_distinction_is_recoverable_without_the_rule(
    shapes_graph_without_class_defaults,
):
    """The cost, and the way back.

    With the rule in the closure the ontology can no longer distinguish a model
    that *states* what a piece of equipment does from one that only types it.
    Validating against a closure that does not import the rule restores that, so
    the distinction is available to anyone who needs it rather than lost.

    The closure is built by dropping the owl:imports rather than by filtering the
    rule's triples out of the merged graph: it is the import that puts the rule
    in the closure, so removing the import is what a consumer would actually do,
    and the test exercises the same resolution path they would.
    """
    assert (WATR.ClassDefaultsRule, None, None) not in shapes_graph_without_class_defaults, (
        "dropping the owl:imports should keep the rule out of the closure; if it "
        "is back, the resolver found it some other way and the rest of this test "
        "proves nothing"
    )

    data = Graph().parse(
        data=PREFIX + "ex:bare2 a watr:GravityThickener .\n", format="ttl"
    )
    _, report, _ = shifty.validate(
        data,
        shacl_graph=shapes_graph_without_class_defaults,
        minimum_severity="violation",
    )
    messages = [
        str(report.value(r, SH.resultMessage))
        for r in report.subjects(SH.resultSeverity, None)
    ]
    assert any("Sedimentation process" in m for m in messages), messages
    assert any("Thickening treatment objective" in m for m in messages), messages
