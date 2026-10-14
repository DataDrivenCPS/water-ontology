"""Named vocabulary terms and locally typed values share function semantics."""

import pytest
import shifty
from rdflib import Graph, Namespace
from rdflib.namespace import SH

WATR = Namespace("https://watermetadata.org/ontology/watr#")
EX = Namespace("urn:local-processes#")
PREFIXES = """
@prefix : <urn:local-processes#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
"""


def _graph(body):
    return Graph().parse(data=PREFIXES + body, format="turtle")


@pytest.mark.parametrize("process,definition", [
    ("watr:Process-Denitrification", ""),
    (":process", ":process a watr:Process-Denitrification ."),
    (":process", ":process a :LocalProcess . "
     ":LocalProcess rdfs:subClassOf watr:Process-Denitrification ."),
    (":process", ":process a :process; rdfs:subClassOf watr:Process-Denitrification ."),
])
def test_process_values_inherit_objectives(process, definition, water_graph):
    data = _graph(f":unit a s223:Equipment; watr:hasProcess {process} . {definition}")
    inferred = shifty.infer(data, shapes_graph=water_graph).graph()
    assert set(inferred.objects(EX.unit, WATR.hasTreatmentObjective)) == {
        WATR["TreatmentObjective-NitrogenRemoval"]
    }


@pytest.mark.parametrize("predicate,unit_type,value_type", [
    ("hasProcess", "MicrofiltrationUnit", "Process-Microfiltration"),
    ("hasTreatmentObjective", "Screen", "TreatmentObjective-SuspendedSolidsRemoval"),
])
def test_local_values_suppress_satisfied_defaults(predicate, unit_type, value_type, water_graph):
    data = _graph(f"""
        :unit a watr:{unit_type}; watr:{predicate} :value .
        :value a watr:{value_type} .
    """)
    inferred = shifty.infer(data, shapes_graph=water_graph).graph()
    assert (EX.unit, WATR[predicate], WATR[value_type]) not in inferred
    if predicate == "hasProcess":
        assert set(inferred.objects(EX.unit, WATR.hasProcess)) == {EX.value}


def _coverage(data, shapes):
    _, report, _ = shifty.validate(data, shacl_graph=shapes)
    return [str(message)
            for result in report.subjects(SH.sourceShape, WATR.SystemProcessCoverageShape)
            for message in report.objects(result, SH.resultMessage)]


def test_local_compound_process_cannot_bypass_coverage(water_graph):
    data = _graph("""
        :system a s223:System; watr:hasProcess :process .
        :process a watr:Process-ActivatedSludge .
    """)
    findings = _coverage(data, water_graph)
    assert any("Process-Aeration" in message for message in findings)
    assert any("Process-SolidLiquidSeparation" in message for message in findings)


@pytest.mark.parametrize("local_member,expected_missing", [(True, False), (False, True)])
def test_coverage_recognizes_local_member_processes(local_member, expected_missing, water_graph):
    data = _graph("""
        :system a s223:System; watr:hasProcess watr:Process-ActivatedSludge;
            s223:hasMember :aerator, :separator .
        :aerator a s223:Equipment; watr:hasProcess :process .
        :separator a s223:Equipment; watr:hasProcess watr:Process-Settling .
    """ + (":process a watr:Process-Aeration ." if local_member else
             ":process a watr:Process-Mixing ."))
    findings = _coverage(data, water_graph)
    assert any("Process-Aeration" in message for message in findings) == expected_missing
