"""Additional processes remain explicit and must have valid process types."""
import shifty
from rdflib import Graph, Namespace
from rdflib.namespace import SH

EX = Namespace("urn:additional#")
WATR = Namespace("https://watermetadata.org/ontology/watr#")
PREFIXES = """
@prefix : <urn:additional#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
"""


def test_additional_process_has_no_equipment_permission_requirement(ontology_shapes_graph):
    data = Graph().parse(data=PREFIXES + """
        :screen a watr:Screen;
            watr:hasProcess watr:Process-Screening, watr:Process-AnaerobicDigestion .
    """, format="turtle")
    _, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    findings = [r for r in report.subjects(SH.focusNode, EX.screen)
                if report.value(r, SH.resultSeverity) in {SH.Warning, SH.Violation}]
    assert not findings


def test_additional_value_must_still_be_a_process(ontology_shapes_graph):
    data = Graph().parse(data=PREFIXES + """
        :screen a watr:Screen;
            watr:hasProcess watr:Process-Screening, watr:TreatmentObjective-Disinfection .
    """, format="turtle")
    _, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    assert any(report.value(r, SH.focusNode) == EX.screen and
               report.value(r, SH.resultPath) == WATR.hasProcess
               for r in report.subjects(SH.resultSeverity, SH.Violation))
