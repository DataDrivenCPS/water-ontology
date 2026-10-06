"""Containment and process constraints for functional equipment regions."""
import pytest
import shifty
from rdflib import Graph, Namespace
from rdflib.namespace import SH

EX = Namespace("urn:regions#")
WATR = Namespace("https://watermetadata.org/ontology/watr#")
PREFIXES = """
@prefix : <urn:regions#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
"""


@pytest.mark.parametrize("triples,valid", [
    # No role or ports are needed; a generic equipment parent is sufficient.
    (":parent a s223:Equipment; s223:contains :region .", True),
    # Nested regions require a non-region equipment ancestor.
    (":parent a watr:EquipmentRegion; watr:hasProcess watr:Process-Mixing; "
     "s223:contains :region . :root a s223:Equipment; s223:contains :parent .", True),
    ("", False),
    (":parent a s223:PhysicalSpace; s223:contains :region .", False),
    (":p1 a s223:Equipment; s223:contains :region . "
     ":p2 a s223:Equipment; s223:contains :region .", False),
    (":region s223:contains :region .", False),
    (":parent a watr:EquipmentRegion; watr:hasProcess watr:Process-Mixing; "
     "s223:contains :region . :region s223:contains :parent .", False),
    # A non-region ancestor does not excuse a containment cycle above the region.
    (":parent a s223:Equipment; s223:contains :region, :parent .", False),
    # The outer region cannot be standalone even when the inner region has a parent.
    (":parent a watr:EquipmentRegion; watr:hasProcess watr:Process-Mixing; "
     "s223:contains :region .", False),
])
def test_region_containment(triples, valid, ontology_shapes_graph):
    data = Graph().parse(data=PREFIXES +
        ":region a watr:EquipmentRegion; watr:hasProcess watr:Process-Denitrification ." +
        triples, format="turtle")
    _, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    violations = [r for r in report.subjects(SH.resultSeverity, SH.Violation)
                  if report.value(r, SH.focusNode) in set(data.all_nodes())]
    assert bool(violations) is not valid


def test_role_does_not_replace_region_process(ontology_shapes_graph):
    data = Graph().parse(data=PREFIXES + """
        :parent a s223:Equipment; s223:contains :region .
        :region a watr:EquipmentRegion; s223:hasRole watr:Role-Anoxic .
    """, format="turtle")
    _, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    assert any(report.value(r, SH.focusNode) == EX.region and
               report.value(r, SH.resultPath) == WATR.hasProcess
               for r in report.subjects(SH.resultSeverity, SH.Violation))


def test_region_inherits_its_process_objective(ontology_shapes_graph):
    data = Graph().parse(data=PREFIXES + """
        :parent a s223:Equipment; s223:contains :region .
        :region a watr:EquipmentRegion; watr:hasProcess watr:Process-Denitrification .
    """, format="turtle")
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    assert (EX.region, WATR.hasTreatmentObjective,
            WATR["TreatmentObjective-NitrogenRemoval"]) in inferred
    assert not list(inferred.objects(EX.parent, WATR.hasTreatmentObjective))
