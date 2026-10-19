"""Regression checks for the September review and compiled release semantics."""
import runpy
from pathlib import Path

import shifty
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SH

WATR = Namespace("https://watermetadata.org/ontology/watr#")
S223 = Namespace("http://data.ashrae.org/standard223#")
EX = Namespace("urn:review#")
DCTERMS = Namespace("http://purl.org/dc/terms/")
PREFIXES = """
@prefix : <urn:review#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
"""


def test_separation_and_cleaning_objectives_do_not_choose_a_specific_target(ontology_shapes_graph):
    data = Graph().parse(data=PREFIXES + """
        :ro a watr:ReverseOsmosisMembrane .
        :wash a s223:System ; watr:hasProcess watr:Process-Backwashing .
        :doser a s223:System ; watr:hasProcess watr:Process-Dosing .
    """, format="ttl")
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    assert set(inferred.objects(EX.ro, WATR.hasTreatmentObjective)) == {
        WATR["TreatmentObjective-ConstituentRemoval"]
    }
    assert set(inferred.objects(EX.wash, WATR.hasTreatmentObjective)) == {
        WATR["TreatmentObjective-EquipmentCleaning"]
    }
    assert not list(inferred.objects(EX.doser, WATR.hasTreatmentObjective))


def test_reviewed_process_parents_and_contaminant_targets(water_graph):
    assert (WATR["Process-ThermalHydrolysis"], RDFS.subClassOf,
            WATR["Process-ThermalTreatment"]) in water_graph
    for method in ("Microfiltration", "Ultrafiltration"):
        assert (WATR[f"Process-{method}"], RDFS.subClassOf,
                WATR["Process-SolidLiquidSeparation"]) in water_graph
    for contaminant in ("Arsenic", "Lead"):
        assert (WATR[f"TreatmentObjective-{contaminant}Removal"],
                WATR.targetsConstituent, WATR[f"Constituent-{contaminant}"]) in water_graph


def test_storage_tank_accepts_a_bidirectional_port(ontology_shapes_graph):
    data = Graph().parse(data=PREFIXES + """
        :tank a watr:Tank ; rdfs:label "Storage tank" ; s223:hasConnectionPoint :port .
        :port a s223:BidirectionalConnectionPoint ; rdfs:label "Shared inlet/outlet" ;
            s223:hasMedium s223:Fluid-Water ; s223:isConnectionPointOf :tank .
    """, format="ttl")
    _, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    violations = [r for r in report.subjects(SH.resultSeverity, SH.Violation)
                  if report.value(r, SH.focusNode) in {EX.tank, EX.port}]
    assert not violations


def test_retired_published_terms_keep_replacement_links(water_graph):
    for old in ("Process-Sedimentation", "Process-Thickening", "Role-NutrientRemoval"):
        term = WATR[old]
        assert (term, OWL.deprecated, Literal(True)) in water_graph
        replacement = water_graph.value(term, DCTERMS.isReplacedBy)
        assert replacement is not None
        assert (replacement, RDF.type, None) in water_graph


def test_compilation_preserves_prefix_declarations(water_graph):
    compiler = runpy.run_path(str(Path(__file__).parents[1] / "scripts/compile-water-ontology.py"))
    graph = Graph() + water_graph
    modules = list(graph.subjects(RDF.type, OWL.Ontology))
    compiler["strip_module_metadata"](graph, modules)
    version = URIRef("https://watermetadata.org/ontology/0.2/watr")
    compiler["add_ontology_header"](graph, version, [])
    declarations = {str(graph.value(d, SH.prefix)) for d in graph.objects(version, SH.declare)}
    assert {"watr", "s223", "quantitykind", "qudt", "unit"} <= declarations
    for target in graph.objects(None, SH.prefixes):
        assert target == version
        assert list(graph.objects(target, SH.declare))


def test_conversion_and_irradiation_do_not_invent_removal_or_disinfection(ontology_shapes_graph):
    data = Graph().parse(data=PREFIXES + """
        :oxidation a s223:System ; watr:hasProcess watr:Process-Oxidation .
        :reduction a s223:System ; watr:hasProcess watr:Process-Reduction .
        :uv a s223:System ; watr:hasProcess watr:Process-UVIrradiation .
    """, format="ttl")
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    for unit in (EX.oxidation, EX.reduction, EX.uv):
        assert not list(inferred.objects(unit, WATR.hasTreatmentObjective))
