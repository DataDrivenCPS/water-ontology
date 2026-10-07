"""Materializing an instance's process and objective, from its class and its process.

``ontology/class-defaults.ttl`` holds a SHACL-AF rule: typing something as a
``watr:GravityThickener`` already says it thickens by settling, so the rule
writes those triples onto the instance rather than making every model repeat
them.

The file is part of the ontology's import closure, and ``shifty.validate`` runs
SHACL-AF rules as part of validation, so the rule fires wherever the ontology is
used. The last two tests pin that class requirements are supplied during inference and remain enforceable when inference is disabled.
"""

import pytest
import shifty
from rdflib import Graph, Namespace


SH = Namespace("http://www.w3.org/ns/shacl#")
WATR = Namespace("https://watermetadata.org/ontology/watr#")
EX = Namespace("urn:defaults#")

PREFIX = (
    "@prefix watr: <https://watermetadata.org/ontology/watr#> .\n"
    "@prefix s223: <http://data.ashrae.org/standard223#> .\n"
    "@prefix ex: <urn:defaults#> .\n"
)


def _materialize(body: str, shapes: Graph) -> Graph:
    data = Graph().parse(data=PREFIX + body, format="ttl")
    return shifty.infer(data, shapes_graph=shapes).graph()


def test_process_and_outcome_are_both_materialized(ontology_shapes_graph):
    """The outcome comes from watr:Thickener and the process from the subclass,
    so a bare instance picks up one from each level of the hierarchy."""
    out = _materialize("ex:gt a watr:GravityThickener .\n", ontology_shapes_graph)
    assert (EX.gt, WATR.hasProcess, WATR["Process-Settling"]) in out
    assert (EX.gt, WATR.hasTreatmentObjective, WATR["TreatmentObjective-Thickening"]) in out


def test_the_settling_split_is_carried_by_the_subclasses(ontology_shapes_graph):
    """Clarifiers and gravity thickeners assign different product objectives.

    watr:SedimentationTank carries the process and no objective, so a unit typed
    with it settles and claims nothing about its product. The two subclasses
    carry one objective each, and both inherit the process from the parent.
    """
    out = _materialize(
        "ex:clarifier a watr:Clarifier .\n"
        "ex:thickener a watr:GravityThickener .\n"
        "ex:settler a watr:SedimentationTank .\n",
        ontology_shapes_graph,
    )
    for unit in (EX.clarifier, EX.thickener, EX.settler):
        assert (unit, WATR.hasProcess, WATR["Process-Settling"]) in out

    assert (
        EX.clarifier,
        WATR.hasTreatmentObjective,
        WATR["TreatmentObjective-Clarification"],
    ) in out
    assert (
        EX.thickener,
        WATR.hasTreatmentObjective,
        WATR["TreatmentObjective-Thickening"],
    ) in out
    assert set(out.objects(EX.settler, WATR.hasTreatmentObjective)) == {
        WATR["TreatmentObjective-ConstituentRemoval"]
    }


def test_the_generic_settler_takes_the_objective_the_modeler_states(ontology_shapes_graph):
    """The modeler who knows the plant uses the underflow says so on the instance,
    and the class adds nothing that would contradict it."""
    out = _materialize(
        "ex:settler a watr:SedimentationTank ;\n"
        "    watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .\n",
        ontology_shapes_graph,
    )
    assert set(out.objects(EX.settler, WATR.hasTreatmentObjective)) == {
        WATR["TreatmentObjective-Thickening"],
        WATR["TreatmentObjective-ConstituentRemoval"],
    }


def test_a_membrane_implies_only_broad_constituent_removal(ontology_shapes_graph):
    """Reverse osmosis desalinates seawater at one plant and removes PFAS from
    groundwater at another, so the class supplies the process and stops there."""
    out = _materialize("ex:ro a watr:ReverseOsmosisMembrane .\n", ontology_shapes_graph)
    assert (EX.ro, WATR.hasProcess, WATR["Process-ReverseOsmosis"]) in out
    assert set(out.objects(EX.ro, WATR.hasTreatmentObjective)) == {
        WATR["TreatmentObjective-ConstituentRemoval"]
    }


def test_renamed_uv_unit_gets_both_axes(ontology_shapes_graph):
    out = _materialize("ex:uv a watr:UltravioletLightUnit .\n", ontology_shapes_graph)
    assert (EX.uv, WATR.hasProcess, WATR["Process-UVIrradiation"]) in out
    assert (EX.uv, WATR.hasTreatmentObjective, WATR["TreatmentObjective-Disinfection"]) in out


def test_the_objective_follows_from_the_process(ontology_shapes_graph):
    """The second rule. A mixing basin only mixes as a class, so the modeler says
    the plant runs this one to denitrify -- and nitrogen removal follows from
    denitrification without anyone writing it."""
    out = _materialize(
        "ex:anoxic a watr:MixingBasin ;\n"
        "    watr:hasProcess watr:Process-Denitrification .\n",
        ontology_shapes_graph,
    )
    assert (EX.anoxic, WATR.hasProcess, WATR["Process-Mixing"]) in out
    assert (
        EX.anoxic,
        WATR.hasTreatmentObjective,
        WATR["TreatmentObjective-NitrogenRemoval"],
    ) in out


def test_nitrification_controls_ammonia_and_removes_no_nitrogen(ontology_shapes_graph):
    """The distinction the entailments exist to keep. Nitrification oxidizes
    ammonia to nitrate, which leaves the nitrogen in the water, so an aerobic
    zone must not come out claiming nitrogen removal. The train it belongs to
    does; the zone is found through its membership."""
    out = _materialize(
        "ex:aerobic a watr:AerationBasin ;\n"
        "    s223:hasRole watr:Role-Aerobic ;\n"
        "    watr:hasProcess watr:Process-Nitrification .\n",
        ontology_shapes_graph,
    )
    assert set(out.objects(EX.aerobic, WATR.hasTreatmentObjective)) == {
        WATR["TreatmentObjective-AmmoniaControl"]
    }


def test_the_two_rules_compose(ontology_shapes_graph):
    """Nothing but a type, and two rules away from a complete unit.

    A bare chlorine contact tank has no watr:hasProcess for the process rule to
    target until the class rule supplies Process-Chlorination. The objective then
    arrives by both routes at once -- from watr:DisinfectionUnit, and from
    chlorination, which always disinfects -- and they agree.
    """
    out = _materialize("ex:contact a watr:ChlorinationUnit .\n", ontology_shapes_graph)
    assert (EX.contact, WATR.hasProcess, WATR["Process-Chlorination"]) in out
    assert set(out.objects(EX.contact, WATR.hasTreatmentObjective)) == {
        WATR["TreatmentObjective-Disinfection"]
    }


def test_a_system_inherits_the_objectives_of_its_process(ontology_shapes_graph):
    """A system has no equipment class, so the class rule reaches it with nothing.
    The process rule targets watr:hasProcess instead, which a system carries, so a
    train that claims A2O removes nitrogen and phosphorus -- and organics, through
    Process-ActivatedSludge above it."""
    out = _materialize(
        "ex:train a s223:System ;\n"
        "    watr:hasProcess watr:Process-A2O .\n",
        ontology_shapes_graph,
    )
    assert set(out.objects(EX.train, WATR.hasTreatmentObjective)) == {
        WATR["TreatmentObjective-NitrogenRemoval"],
        WATR["TreatmentObjective-PhosphorusRemoval"],
        WATR["TreatmentObjective-OrganicsRemoval"],
    }


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
    data = Graph().parse("examples/gravity-thickener-outlets.ttl")
    out = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    valid, _, text = shifty.validate(
        out, shacl_graph=ontology_shapes_graph, minimum_severity="violation"
    )
    assert valid, text


# --- what including the rule in the closure changes --------------------------


def test_class_defaults_complete_function_with_explicit_ports(ontology_shapes_graph):
    """The point of shipping the rule in the closure.

    The type supplies the process and objective during validation. Physical
    connection points must still be explicitly supplied by the model.
    """
    data = Graph().parse("examples/gravity-thickener-outlets.ttl")
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
    assert any("Settling process" in m for m in messages), messages
    assert any("Thickening treatment objective" in m for m in messages), messages
