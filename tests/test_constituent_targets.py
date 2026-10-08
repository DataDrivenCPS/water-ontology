"""What an objective is aimed at, and the local objective that extension buys.

``watr:targetsConstituent`` names the constituent a treatment objective removes,
converts or controls. It is stated on the objective rather than on the units
that serve it, and it is inherited: clarification names no constituent of its
own because its parent, suspended solids removal, names suspended solids.

The point of the target is that it makes the constituent-removal branch
extensible. A plant treating something this ontology does not carry writes its
own objective, types it ``watr:TreatmentObjective-ConstituentRemoval`` and points
it at a constituent; the objective is then in the hierarchy and answerable
without any change to the vocabulary. Two shapes in ``ontology/watr.ttl`` keep
that usable:

``watr:ConstituentTargetValueShape``
    guards that the value of ``watr:targetsConstituent`` is an
    ``s223:Medium-Constituent`` and not something from one of the other
    vocabularies.

``watr:ConstituentRemovalTargetShape``
    warns when a constituent-removal objective neither states a target nor
    inherits one -- a warning rather than a violation, because an objective
    naming a constituent we have not modeled yet is incomplete, not wrong.
"""

import shifty
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS


SH = Namespace("http://www.w3.org/ns/shacl#")
WATR = Namespace("https://watermetadata.org/ontology/watr#")
S223 = Namespace("http://data.ashrae.org/standard223#")

PREFIX = (
    "@prefix watr: <https://watermetadata.org/ontology/watr#> .\n"
    "@prefix s223: <http://data.ashrae.org/standard223#> .\n"
    "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    "@prefix ex: <urn:constituents#> .\n"
)


def _findings(data_ttl: str, shapes: Graph, shape) -> list[str]:
    data = Graph().parse(data=PREFIX + data_ttl, format="ttl")
    _, report, _ = shifty.validate(data, shacl_graph=shapes)
    return [
        str(report.value(r, SH.resultMessage))
        for r in report.subjects(SH.sourceShape, shape)
    ]


# --- the vocabulary's own targets --------------------------------------------


def test_named_objectives_carry_a_target(ontology_shapes_graph):
    """Every constituent-removal objective the ontology names resolves to a
    constituent, either its own or an ancestor's."""
    untargeted = []
    for objective in ontology_shapes_graph.subjects(
        RDFS.subClassOf * "+", WATR["TreatmentObjective-ConstituentRemoval"]
    ):
        targets = set()
        for ancestor in ontology_shapes_graph.objects(objective, RDFS.subClassOf * "*"):
            targets |= set(ontology_shapes_graph.objects(ancestor, WATR.targetsConstituent))
        if not targets:
            untargeted.append(objective)
    assert not untargeted, f"constituent-removal objectives with no target: {untargeted}"


def test_clarification_inherits_the_solids_target(ontology_shapes_graph):
    """Clarification states no target of its own; it removes what suspended solids removal
    removes, and the hierarchy is what says so."""
    assert not list(
        ontology_shapes_graph.objects(
            WATR["TreatmentObjective-Clarification"], WATR.targetsConstituent
        )
    )
    assert (
        WATR["TreatmentObjective-SuspendedSolidsRemoval"],
        WATR.targetsConstituent,
        WATR["Constituent-SuspendedSolids"],
    ) in ontology_shapes_graph


def test_disinfection_targets_pathogens_without_being_a_removal(ontology_shapes_graph):
    """Chlorination inactivates pathogens where they are rather than taking them
    out, so disinfection is not a constituent removal -- but it still names the
    constituent, so a query by constituent finds it."""
    assert (
        WATR["TreatmentObjective-Disinfection"],
        WATR.targetsConstituent,
        WATR["Constituent-Pathogens"],
    ) in ontology_shapes_graph
    assert (
        WATR["TreatmentObjective-Disinfection"],
        RDFS.subClassOf,
        WATR["TreatmentObjective-ConstituentRemoval"],
    ) not in ontology_shapes_graph


# --- a modeler's local objective ---------------------------------------------


LOCAL_OBJECTIVE = (
    "ex:Constituent-Selenium a s223:Medium-Constituent ;\n"
    "    rdfs:subClassOf s223:Medium-Constituent .\n"
    "ex:removeSelenium a watr:TreatmentObjective-ConstituentRemoval ;\n"
    "    watr:targetsConstituent ex:Constituent-Selenium .\n"
    "ex:column a watr:IonExchangeUnit ;\n"
    "    watr:hasProcess watr:Process-IonExchange ;\n"
    "    watr:hasTreatmentObjective ex:removeSelenium .\n"
)


def test_local_objective_is_accepted_as_a_treatment_objective(ontology_shapes_graph):
    """A plant may name an objective the vocabulary does not carry. Typing it
    under the hierarchy is all that watr:hasTreatmentObjective asks for."""
    assert not _findings(
        LOCAL_OBJECTIVE, ontology_shapes_graph, WATR.TreatmentObjectiveValueShape
    )
    assert not _findings(
        LOCAL_OBJECTIVE, ontology_shapes_graph, WATR.ConstituentRemovalTargetShape
    )


def test_local_objective_without_a_target_warns(ontology_shapes_graph):
    body = (
        "ex:removeSomething a watr:TreatmentObjective-ConstituentRemoval .\n"
        "ex:column a watr:IonExchangeUnit ;\n"
        "    watr:hasProcess watr:Process-IonExchange ;\n"
        "    watr:hasTreatmentObjective ex:removeSomething .\n"
    )
    messages = _findings(body, ontology_shapes_graph, WATR.ConstituentRemovalTargetShape)
    assert messages, "a constituent removal that names no constituent should warn"
    assert "watr:targetsConstituent" in messages[0]


def test_local_objective_inherits_its_class_target(ontology_shapes_graph):
    """An instance of a named objective needs no target of its own: it is aimed
    at whatever the class it is typed with is aimed at."""
    body = (
        "ex:softenTheFeed a watr:TreatmentObjective-Softening .\n"
        "ex:column a watr:IonExchangeUnit ;\n"
        "    watr:hasProcess watr:Process-IonExchange ;\n"
        "    watr:hasTreatmentObjective ex:softenTheFeed .\n"
    )
    assert not _findings(
        body, ontology_shapes_graph, WATR.ConstituentRemovalTargetShape
    )


def test_target_must_be_a_constituent(ontology_shapes_graph):
    """The third vocabulary gets the same guard as the other two: a process or
    another objective is not a thing in the water."""
    body = (
        "ex:removeSomething a watr:TreatmentObjective-ConstituentRemoval ;\n"
        "    watr:targetsConstituent watr:Process-IonExchange .\n"
    )
    assert _findings(body, ontology_shapes_graph, WATR.ConstituentTargetValueShape)


def test_suspended_and_dissolved_objectives_have_distinct_targets(ontology_shapes_graph):
    data = Graph().parse("examples/solids-removal-objectives.ttl")
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    example = Namespace("urn:example/solids-removal-objectives#")
    assert (example.screen, WATR.hasTreatmentObjective,
            WATR["TreatmentObjective-SuspendedSolidsRemoval"]) in inferred
    assert WATR["TreatmentObjective-DissolvedSolidsRemoval"] not in set(
        inferred.objects(example.screen, WATR.hasTreatmentObjective)
    )
    assert WATR["TreatmentObjective-SuspendedSolidsRemoval"] not in set(
        inferred.objects(example.membrane, WATR.hasTreatmentObjective)
    )
    for objective, target in [
        ("SuspendedSolidsRemoval", "SuspendedSolids"),
        ("DissolvedSolidsRemoval", "DissolvedSolids"),
    ]:
        term = WATR[f"TreatmentObjective-{objective}"]
        assert (term, RDFS.subClassOf,
                WATR["TreatmentObjective-ConstituentRemoval"]) in ontology_shapes_graph
        assert (term, WATR.targetsConstituent,
                WATR[f"Constituent-{target}"]) in ontology_shapes_graph
    for objective in ("Clarification", "TurbidityRemoval"):
        assert (WATR[f"TreatmentObjective-{objective}"], RDFS.subClassOf,
                WATR["TreatmentObjective-SuspendedSolidsRemoval"]) in ontology_shapes_graph


def test_legacy_solids_objective_remains_compatible(ontology_shapes_graph):
    old = WATR["TreatmentObjective-SolidsRemoval"]
    new = WATR["TreatmentObjective-SuspendedSolidsRemoval"]
    assert (old, OWL.deprecated, Literal(True)) in ontology_shapes_graph
    assert (old, DCTERMS.isReplacedBy, new) in ontology_shapes_graph
    data = Graph().parse("examples/solids-removal-objectives.ttl")
    example = Namespace("urn:example/solids-removal-objectives#")
    # A legacy objective instance still satisfies the screen's new requirement.
    data.set((example.screen, WATR.hasTreatmentObjective, example.legacyObjective))
    data.add((example.legacyObjective, RDF.type, old))
    data.add((example.legacyObjective, RDFS.label, Literal("Legacy solids objective")))
    data.add((example.legacyObjective, RDFS.comment,
              Literal("Removal of suspended and settleable solids.")))
    _, report, report_text = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    example_nodes = set(data.all_nodes())
    assert not any(report.value(result, SH.focusNode) in example_nodes
                   for severity in (SH.Violation, SH.Warning)
                   for result in report.subjects(SH.resultSeverity, severity)), report_text
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    # Query the model with the vocabulary: validation recognizes subclassing,
    # but the inference result need not materialize every inherited rdf:type.
    query_graph = inferred + ontology_shapes_graph
    assert new in set(query_graph.objects(
        example.legacyObjective, RDF.type / (RDFS.subClassOf * "*")
    ))
    inherited_targets = set(query_graph.objects(
        example.legacyObjective, RDF.type / (RDFS.subClassOf * "*") / WATR.targetsConstituent
    ))
    assert inherited_targets == {WATR["Constituent-SuspendedSolids"]}
