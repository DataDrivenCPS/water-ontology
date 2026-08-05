"""Processes performed by a collection rather than by one machine.

Some processes are performed by an assembly and by no member of it: a backwash
pump only pumps, a backwash tank only holds water, and backwashing is what the
collection does. Those are asserted on the ``s223:System``.

Two pieces of machinery support that, both in ``water/ontology.ttl``:

``watr:ProcessBearerShape``
    guards that ``watr:hasProcess`` is only asserted on something that can
    perform a process -- an ``s223:Equipment`` or an ``s223:System``.

``watr:ProcessValueShape``
    guards that the object of every ``watr:hasProcess`` assertion is actually a
    ``watr:Process``.

``watr:SystemProcessCoverageShape``
    warns when a system claims a compound process (``Process-MLE``, the
    Bardenphos) but nothing inside it performs one of the constituent steps
    recorded by ``watr:includesProcess``.
"""

import pytest
import shifty
from rdflib import Graph, Namespace, RDFS


SH = Namespace("http://www.w3.org/ns/shacl#")
WATR = Namespace("urn:nawi-water-ontology#")

PREFIX = (
    "@prefix watr: <urn:nawi-water-ontology#> .\n"
    "@prefix s223: <http://data.ashrae.org/standard223#> .\n"
    "@prefix sh: <http://www.w3.org/ns/shacl#> .\n"
    "@prefix ex: <urn:systest#> .\n"
)

# A member that owes nothing structurally, so the only findings are the ones
# under test. watr:Pump has no connection point or process requirements.
def _member(name: str, *processes: str) -> str:
    procs = (
        " ; watr:hasProcess " + ", ".join(f"watr:Process-{p}" for p in processes)
        if processes
        else ""
    )
    return f"ex:{name} a watr:Pump{procs} .\n"


def _findings(data_ttl: str, shapes: Graph, shape) -> list[str]:
    data = Graph().parse(data=PREFIX + data_ttl, format="ttl")
    _, report, _ = shifty.validate(data, shacl_graph=shapes)
    return [
        str(report.value(r, SH.resultMessage))
        for r in report.subjects(SH.sourceShape, shape)
    ]


# --- class-reference guard ---------------------------------------------------


@pytest.mark.parametrize(
    "constraint",
    [
        "sh:in ( watr:Process-Aeration ex:UndefinedProcess )",
        (
            "sh:qualifiedValueShape "
            "[ sh:in ( watr:Process-Aeration ex:UndefinedProcess ) ] ; "
            "sh:qualifiedMinCount 1"
        ),
    ],
    ids=["direct-sh-in", "qualified-sh-in"],
)
def test_undefined_class_in_process_list_is_rejected(
    constraint, ontology_shapes_graph
):
    """The guard must traverse every member of direct and qualified sh:in lists."""
    body = (
        "ex:BrokenEquipmentShape a sh:NodeShape ;\n"
        "    sh:property [\n"
        "        sh:path watr:hasProcess ;\n"
        f"        {constraint}\n"
        "    ] .\n"
    )
    assert _findings(
        body,
        ontology_shapes_graph,
        WATR.ProcessAndRoleConstraintsReferenceDefinedClasses,
    )


# --- watr:ProcessBearerShape -------------------------------------------------


def test_system_may_carry_a_process(ontology_shapes_graph):
    """The whole point: a collection can be the thing that performs a process."""
    body = (
        "ex:BackwashSystem a s223:System ;\n"
        "    s223:hasMember ex:pump, ex:tank ;\n"
        "    watr:hasProcess watr:Process-Backwashing .\n"
        + _member("pump")
        + "ex:tank a watr:Tank .\n"
    )
    assert not _findings(body, ontology_shapes_graph, WATR.ProcessBearerShape)


def test_equipment_may_carry_a_process(ontology_shapes_graph):
    body = _member("aerator", "Aeration")
    assert not _findings(body, ontology_shapes_graph, WATR.ProcessBearerShape)


def test_process_on_something_that_cannot_perform_one_is_rejected(
    ontology_shapes_graph,
):
    """A property is not a performer. Catches hasProcess on the wrong subject."""
    body = (
        "ex:bogus a s223:QuantifiableProperty ;\n"
        "    watr:hasProcess watr:Process-Aeration .\n"
    )
    assert _findings(body, ontology_shapes_graph, WATR.ProcessBearerShape)


def test_has_process_object_must_be_a_process(ontology_shapes_graph):
    """Systems do not inherit UnitProcess's all-values process constraint."""
    body = (
        "ex:system a s223:System ;\n"
        "    watr:hasProcess ex:NotAProcess .\n"
        "ex:NotAProcess a s223:Equipment .\n"
    )
    assert _findings(body, ontology_shapes_graph, WATR.ProcessValueShape)


# --- watr:SystemProcessCoverageShape ----------------------------------------


def test_covered_compound_process_is_not_flagged(ontology_shapes_graph):
    """Process-MLE expands to nitrification, denitrification, aeration,
    sedimentation and recirculation; all are present across the members."""
    body = (
        "ex:MLE a s223:System ;\n"
        "    s223:hasMember ex:anoxic, ex:aerobic, ex:clarifier ;\n"
        "    watr:hasProcess watr:Process-MLE .\n"
        + _member("anoxic", "Denitrification")
        + _member("aerobic", "Nitrification", "Aeration")
        + _member("clarifier", "Sedimentation", "Recirculation")
    )
    assert not _findings(body, ontology_shapes_graph, WATR.SystemProcessCoverageShape)


def test_missing_constituent_process_is_flagged(ontology_shapes_graph):
    """Drop the denitrifying member and the shape should name what is missing."""
    body = (
        "ex:MLEGap a s223:System ;\n"
        "    s223:hasMember ex:aerobic2, ex:clarifier2 ;\n"
        "    watr:hasProcess watr:Process-MLE .\n"
        + _member("aerobic2", "Nitrification", "Aeration")
        + _member("clarifier2", "Sedimentation", "Recirculation")
    )
    msgs = _findings(body, ontology_shapes_graph, WATR.SystemProcessCoverageShape)
    assert msgs, "a missing constituent process should be reported"
    assert any("Denitrification" in m for m in msgs), msgs


def test_nested_subsystem_satisfies_coverage(ontology_shapes_graph):
    """hasMember is transitive for this check: systems contain systems."""
    body = (
        "ex:Outer a s223:System ;\n"
        "    s223:hasMember ex:Inner ;\n"
        "    watr:hasProcess watr:Process-ActivatedSludge .\n"
        "ex:Inner a s223:System ;\n"
        "    s223:hasMember ex:basin, ex:settler .\n"
        + _member("basin", "Aeration")
        + _member("settler", "Sedimentation")
    )
    assert not _findings(body, ontology_shapes_graph, WATR.SystemProcessCoverageShape)


def test_membrane_filtration_satisfies_activated_sludge_separation(
    ontology_shapes_graph,
):
    """Activated sludge requires separation, not sedimentation specifically."""
    body = (
        "ex:MBR a s223:System ;\n"
        "    s223:hasMember ex:bioreactor, ex:membrane ;\n"
        "    watr:hasProcess watr:Process-ActivatedSludge .\n"
        + _member("bioreactor", "Aeration")
        + _member("membrane", "Microfiltration")
    )
    assert not _findings(body, ontology_shapes_graph, WATR.SystemProcessCoverageShape)


def test_activated_sludge_without_separation_is_flagged(ontology_shapes_graph):
    body = (
        "ex:NoSeparator a s223:System ;\n"
        "    s223:hasMember ex:basinOnly ;\n"
        "    watr:hasProcess watr:Process-ActivatedSludge .\n"
        + _member("basinOnly", "Aeration")
    )
    msgs = _findings(body, ontology_shapes_graph, WATR.SystemProcessCoverageShape)
    assert any("Process-Separation" in m for m in msgs), msgs


def test_system_may_state_a_step_itself(ontology_shapes_graph):
    """The zero-length hasMember* match: a train may carry a step directly."""
    body = (
        "ex:Direct a s223:System ;\n"
        "    s223:hasMember ex:m1, ex:m2 ;\n"
        "    watr:hasProcess watr:Process-ActivatedSludge ,\n"
        "                    watr:Process-Aeration ,\n"
        "                    watr:Process-Sedimentation .\n"
        + _member("m1")
        + _member("m2")
    )
    assert not _findings(body, ontology_shapes_graph, WATR.SystemProcessCoverageShape)


def test_realistic_train_of_basins_draws_no_process_warnings(ontology_shapes_graph):
    """An A2O train built from the vessels a plant actually uses.

    The other coverage cases above use watr:Pump members so that the only
    findings are the ones under test. That isolation hid a collision between the
    two warning-level shapes: watr:SystemProcessCoverageShape expects the members
    of a nutrient-removal train to declare nitrification, denitrification and
    EBPR, while watr:ProcessPlausibilityShape flagged exactly those declarations
    because no equipment family permitted them. Both are warnings, so nothing
    failed -- every correctly modelled train just emitted a spurious warning per
    zone. Reactor now permits the three conversions.

    Only the two process shapes are inspected. Real basins carry s223 connection
    point requirements that are not what this test is about.
    """
    body = (
        "ex:A2O a s223:System ;\n"
        "    s223:hasMember ex:anaerobicZone, ex:anoxicZone, ex:aerobicZone,\n"
        "                   ex:finalClarifier ;\n"
        "    watr:hasProcess watr:Process-A2O .\n"
        "ex:anaerobicZone a watr:MixingBasin ;\n"
        "    s223:hasRole watr:Role-Anaerobic ;\n"
        "    watr:hasProcess watr:Process-Mixing ,\n"
        "                    watr:Process-EnhancedBiologicalPhosphorusRemoval .\n"
        "ex:anoxicZone a watr:MixingBasin ;\n"
        "    s223:hasRole watr:Role-Anoxic ;\n"
        "    watr:hasProcess watr:Process-Mixing, watr:Process-Denitrification .\n"
        "ex:aerobicZone a watr:AerationBasin ;\n"
        "    s223:hasRole watr:Role-Aerobic ;\n"
        "    watr:hasProcess watr:Process-Aeration, watr:Process-Nitrification .\n"
        "ex:finalClarifier a watr:SedimentationTank ;\n"
        "    watr:hasProcess watr:Process-Sedimentation, watr:Process-Recirculation .\n"
    )
    data = Graph().parse(data=PREFIX + body, format="ttl")
    _, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)

    for shape in (WATR.SystemProcessCoverageShape, WATR.ProcessPlausibilityShape):
        msgs = [
            str(report.value(r, SH.resultMessage))
            for r in report.subjects(SH.sourceShape, shape)
        ]
        assert not msgs, f"{shape.split('#')[-1]} on a well-formed A2O train:\n" + "\n".join(msgs)


def test_coverage_findings_are_warnings_not_violations(ontology_shapes_graph):
    """A partial model is still a valid model: the train may be described before
    every member has been entered.

    The system is deliberately given no members, so that the coverage findings are
    the only results and the overall verdict can be asserted on. That is legal
    here because s223's "a System should have at least two members" is itself only
    a warning. Adding equipment members would drag in their own s223 requirements
    and confound the verdict.
    """
    body = "ex:Partial a s223:System ;\n    watr:hasProcess watr:Process-MLE .\n"
    data = Graph().parse(data=PREFIX + body, format="ttl")

    _, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    severities = {
        report.value(r, SH.resultSeverity)
        for r in report.subjects(SH.sourceShape, WATR.SystemProcessCoverageShape)
    }
    assert severities == {SH.Warning}, severities

    valid_at_violation, _, _ = shifty.validate(
        data, shacl_graph=ontology_shapes_graph, minimum_severity="violation"
    )
    assert valid_at_violation, (
        "an incomplete train must not fail violation-level validation, which is "
        "the level tests/test_validation.py and the example tests use"
    )


# --- the invariant the coverage check depends on -----------------------------


COMPOUND_PROCESSES = [
    "Process-ActivatedSludge",
    "Process-AO",
    "Process-MLE",
    "Process-A2O",
    "Process-UCT",
    "Process-FourStageBardenpho",
    "Process-FiveStageBardenpho",
]


@pytest.mark.parametrize("name", COMPOUND_PROCESSES)
def test_compound_process_is_not_a_subclass_of_its_own_steps(name, water_graph):
    """A compound process comprises its steps; it is not a kind of them.

    Otherwise the compound claim itself satisfies the coverage check for each
    constituent step.
    """
    process = WATR[name]
    ancestors = set(water_graph.transitive_objects(process, RDFS.subClassOf))
    steps = {
        step
        for anc in ancestors
        for step in water_graph.objects(anc, WATR.includesProcess)
    }
    overlap = {s for s in steps if s in ancestors}
    assert not overlap, (
        f"{name} both includes and is a subclass of "
        f"{sorted(str(o).split('#')[-1] for o in overlap)}, which makes the "
        f"coverage check vacuous for those steps"
    )


def test_nitrification_alone_does_not_remove_nitrogen(water_graph):
    """Nitrification converts ammonia to nitrate and leaves the nitrogen in the
    water, so it must not satisfy a Process-NitrogenRemoval claim. Denitrification
    must."""
    assert (
        WATR["Process-Denitrification"],
        RDFS.subClassOf,
        WATR["Process-NitrogenRemoval"],
    ) in water_graph, "denitrification does remove nitrogen"

    nitrification_ancestors = set(
        water_graph.transitive_objects(WATR["Process-Nitrification"], RDFS.subClassOf)
    )
    assert WATR["Process-NitrogenRemoval"] not in nitrification_ancestors, (
        "nitrification converts nitrogen rather than removing it"
    )
