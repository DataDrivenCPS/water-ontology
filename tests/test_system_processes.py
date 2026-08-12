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
    "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
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


# --- watr:hasTreatmentObjective ---------------------------------------------------------


def test_outcome_and_process_together_are_accepted(ontology_shapes_graph):
    """The normal shape of an equipment description: what it is for, and what it
    does to get there."""
    body = (
        "ex:gt a watr:GravityThickener ;\n"
        "    watr:hasTreatmentObjective watr:TreatmentObjective-Thickening ;\n"
        "    watr:hasProcess watr:Process-Sedimentation .\n"
    )
    data = Graph().parse(data=PREFIX + body, format="ttl")
    valid, _, text = shifty.validate(
        data, shacl_graph=ontology_shapes_graph, minimum_severity="violation"
    )
    assert valid, text


def test_one_process_serves_several_outcomes(ontology_shapes_graph):
    """Sedimentation is the process of a clarifier and of a gravity thickener
    alike; the objective is what differs, and it is stated separately."""
    body = (
        "ex:clarifier a watr:SedimentationTank ;\n"
        "    watr:hasTreatmentObjective watr:TreatmentObjective-Clarification ;\n"
        "    watr:hasProcess watr:Process-Sedimentation ;\n"
        "    s223:hasRole watr:Role-Primary .\n"
        "ex:thickener a watr:GravityThickener ;\n"
        "    watr:hasTreatmentObjective watr:TreatmentObjective-Thickening ;\n"
        "    watr:hasProcess watr:Process-Sedimentation .\n"
    )
    assert not _findings(body, ontology_shapes_graph, WATR.TreatmentObjectiveValueShape)
    assert not _findings(body, ontology_shapes_graph, WATR.ProcessValueShape)


def test_an_outcome_may_not_be_stated_as_a_process(ontology_shapes_graph):
    """The two vocabularies are disjoint, which is what makes the axes decidable.
    This is the breaking change: Process-Thickening no longer exists."""
    body = (
        "ex:bad a watr:Pump ;\n"
        "    watr:hasProcess watr:TreatmentObjective-Thickening .\n"
    )
    assert _findings(body, ontology_shapes_graph, WATR.ProcessValueShape)


def test_a_process_may_not_be_stated_as_an_outcome(ontology_shapes_graph):
    body = (
        "ex:bad2 a watr:Pump ;\n"
        "    watr:hasProcess watr:Process-Sedimentation ;\n"
        "    watr:hasTreatmentObjective watr:Process-Sedimentation .\n"
    )
    assert _findings(body, ontology_shapes_graph, WATR.TreatmentObjectiveValueShape)


def test_outcome_without_a_process_is_rejected(ontology_shapes_graph):
    """An objective is reached by doing something. Stating only the objective
    says nothing checkable."""
    body = "ex:m a watr:Pump ; watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .\n"
    assert _findings(
        body, ontology_shapes_graph, WATR.TreatmentObjectiveRequiresProcessProperty
    )


def test_outcome_on_something_that_cannot_have_one_is_rejected(
    ontology_shapes_graph,
):
    body = (
        "ex:bogus2 a s223:QuantifiableProperty ;\n"
        "    watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .\n"
    )
    assert _findings(body, ontology_shapes_graph, WATR.ProcessBearerShape)


def test_process_types_declare_the_outcome_they_achieve(water_graph):
    """watr:achievesTreatmentObjective carries the outcome that follows from the process
    itself, so it need not be repeated on every machine performing it."""
    for process, outcome in [
        ("Process-Denitrification", "TreatmentObjective-NitrogenRemoval"),
        ("Process-EnhancedBiologicalPhosphorusRemoval", "TreatmentObjective-PhosphorusRemoval"),
        ("Process-ChlorineDosing", "TreatmentObjective-Disinfection"),
        ("Process-UVIrradiation", "TreatmentObjective-Disinfection"),
        ("Process-Digestion", "TreatmentObjective-Stabilization"),
        ("Process-MLE", "TreatmentObjective-NitrogenRemoval"),
        ("Process-A2O", "TreatmentObjective-PhosphorusRemoval"),
    ]:
        assert (WATR[process], WATR.achievesTreatmentObjective, WATR[outcome]) in water_graph, (
            f"{process} should declare it achieves {outcome}"
        )


def test_nitrification_controls_ammonia_but_does_not_remove_nitrogen(water_graph):
    """Nitrification converts ammonia; it does not remove nitrogen from water."""
    achieved = set(water_graph.objects(WATR["Process-Nitrification"], WATR.achievesTreatmentObjective))
    assert WATR["TreatmentObjective-AmmoniaControl"] in achieved, achieved
    assert WATR["TreatmentObjective-NitrogenRemoval"] not in achieved, achieved

    # ... and the outcome itself must stay off the nutrient-removal branch, or
    # the distinction would be undone one level up.
    ancestors = set(
        water_graph.transitive_objects(WATR["TreatmentObjective-AmmoniaControl"], RDFS.subClassOf)
    )
    assert WATR["TreatmentObjective-NutrientRemoval"] not in ancestors, ancestors


def test_chemical_precipitation_is_left_unattached(water_graph):
    """Most processes declare no outcome; this one is worth pinning because it is
    a tempting wiring. Chemical precipitation is a phosphorus-removal method, but
    it is equally a metals-removal method, so what it achieves depends on the
    equipment and belongs there."""
    achieved = set(
        water_graph.objects(WATR["Process-ChemicalPrecipitation"], WATR.achievesTreatmentObjective)
    )
    assert not achieved, achieved


@pytest.mark.parametrize("process", ["Process-Ozonation", "Process-ThermalTreatment"])
def test_context_dependent_disinfection_methods_are_left_unattached(process, water_graph):
    """Ozone and heat can disinfect, but their general process terms do not promise it."""
    achieved = set(water_graph.objects(WATR[process], WATR.achievesTreatmentObjective))
    assert not achieved, achieved


@pytest.mark.parametrize(
    "outcome",
    ["TreatmentObjective-MetalsRemoval", "TreatmentObjective-SulfateRemoval", "TreatmentObjective-SilicaRemoval",
     "TreatmentObjective-Softening", "TreatmentObjective-PhosphorusRemoval"],
)
def test_precipitation_targets_exist_but_stay_unwired(outcome, water_graph):
    """The objectives a precipitation step may serve are named so equipment can
    state one, and left unattached to the process because which of them applies
    depends on the reagent and the target."""
    assert (WATR[outcome], RDFS.subClassOf, None) in water_graph, (
        f"{outcome} should be defined"
    )
    assert (
        WATR["Process-ChemicalPrecipitation"],
        WATR.achievesTreatmentObjective,
        WATR[outcome],
    ) not in water_graph, f"{outcome} must not be wired to chemical precipitation"


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
    assert any("Process-SolidLiquidSeparation" in m for m in msgs), msgs


@pytest.mark.parametrize(
    "process,why",
    [
        ("Sedimentation", "a conventional train settles the biomass out"),
        ("Microfiltration", "an MBR separates it with a membrane"),
        ("Flotation", "a DAF floats it off"),
        ("Centrifugation", "a centrifuge spins it out"),
    ],
)
def test_any_solid_liquid_separator_covers_activated_sludge(
    process, why, ontology_shapes_graph
):
    """The step is the mechanism family, not one mechanism."""
    body = (
        "ex:AS a s223:System ;\n"
        "    s223:hasMember ex:basin, ex:separator ;\n"
        "    watr:hasProcess watr:Process-ActivatedSludge .\n"
        + _member("basin", "Aeration")
        + _member("separator", process)
    )
    msgs = _findings(body, ontology_shapes_graph, WATR.SystemProcessCoverageShape)
    assert not msgs, f"{process} should cover the separation step ({why}):\n" + "\n".join(msgs)


@pytest.mark.parametrize(
    "process,why",
    [
        ("Screening", "a bar screen removes debris, not biomass"),
        ("Stripping", "an air stripper separates gases, not solids"),
        ("ReverseOsmosis", "RO retains dissolved salts, not suspended solids"),
        ("MembraneDistillation", "MD separates by vapour pressure, not by size"),
    ],
)
def test_a_separation_that_is_not_solid_liquid_does_not_cover(
    process, why, ontology_shapes_graph
):
    """Why the step names Process-SolidLiquidSeparation and not its parent.

    All of these are a watr:Process-Separation, so naming the family here would
    accept them as the step in which an activated-sludge train separates its
    biomass from the treated water. The last two are a watr:Process-Filtration
    as well: filtration is not a solid-liquid separation as a family, only in the
    subtypes that retain what is suspended -- which is why Microfiltration and
    Ultrafiltration are declared as both and reverse osmosis is not.
    """
    body = (
        "ex:AS2 a s223:System ;\n"
        "    s223:hasMember ex:basin2, ex:notASeparator ;\n"
        "    watr:hasProcess watr:Process-ActivatedSludge .\n"
        + _member("basin2", "Aeration")
        + _member("notASeparator", process)
    )
    msgs = _findings(body, ontology_shapes_graph, WATR.SystemProcessCoverageShape)
    assert any("Process-SolidLiquidSeparation" in m for m in msgs), (
        f"{process} should not cover the separation step ({why}): {msgs}"
    )


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


def test_stated_process_implies_stated_treatment_objective(ontology_shapes_graph):
    """watr:achievesTreatmentObjective has a consumer: a machine that chlorinates disinfects,
    whether or not the model says so."""
    body = (
        "ex:doser a watr:Pump ;\n"
        "    watr:hasProcess watr:Process-ChlorineDosing .\n"
    )
    msgs = _findings(body, ontology_shapes_graph, WATR.TreatmentObjectiveCompletenessShape)
    assert any("Disinfection" in m for m in msgs), msgs


def test_stating_the_treatment_objective_silences_the_completeness_warning(
    ontology_shapes_graph,
):
    body = (
        "ex:doser2 a watr:Pump ;\n"
        "    watr:hasProcess watr:Process-ChlorineDosing ;\n"
        "    watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection .\n"
    )
    assert not _findings(body, ontology_shapes_graph, WATR.TreatmentObjectiveCompletenessShape)


def test_completeness_accepts_a_more_general_treatment_objective(ontology_shapes_graph):
    """Denitrification achieves nitrogen removal; a system claiming the broader
    nutrient removal has not contradicted it."""
    body = (
        "ex:zone a watr:Pump ;\n"
        "    watr:hasProcess watr:Process-Denitrification ;\n"
        "    watr:hasTreatmentObjective watr:TreatmentObjective-NutrientRemoval .\n"
    )
    assert not _findings(body, ontology_shapes_graph, WATR.TreatmentObjectiveCompletenessShape)


def test_context_dependent_treatment_objective_is_not_demanded(ontology_shapes_graph):
    """Sedimentation serves clarification and thickening alike, so it declares no
    watr:achievesTreatmentObjective and nothing may be inferred from it."""
    body = (
        "ex:settler a watr:Pump ;\n"
        "    watr:hasProcess watr:Process-Sedimentation .\n"
    )
    assert not _findings(body, ontology_shapes_graph, WATR.TreatmentObjectiveCompletenessShape)


@pytest.mark.parametrize(
    "process",
    [
        "Process-Filtration",
        "Process-Microfiltration",
        "Process-Ultrafiltration",
        "Process-ReverseOsmosis",
    ],
)
def test_membrane_method_does_not_imply_a_universal_treatment_objective(
    process, ontology_shapes_graph
):
    """Pore-size/process terms are mechanisms, not complete treatment claims.

    A class such as ReverseOsmosisMembrane can still require desalination, but a
    bare process assertion must not invent an objective that depends on the
    unit's design or the plant's intended service.
    """
    body = f"ex:unit a watr:Pump ; watr:hasProcess watr:{process} .\n"
    assert not _findings(
        body, ontology_shapes_graph, WATR.TreatmentObjectiveCompletenessShape
    )


def test_no_process_slot_uses_qualified_value_shapes_disjoint(water_graph):
    """The flag makes a requirement unsatisfiable by the very process it names.

    watr:Grinder kept it after the sweep that removed the other 51, and no
    Grinder could validate. This guards the sweep rather than the one class.
    """
    offenders = {
        str(water_graph.value(ps, SH.path))
        for ps in water_graph.subjects(SH.qualifiedValueShapesDisjoint, None)
    }
    assert not offenders, f"sh:qualifiedValueShapesDisjoint still present on {offenders}"
