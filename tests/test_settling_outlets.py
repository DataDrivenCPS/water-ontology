"""Liquid and sludge outlet requirements shared by clarifiers and thickeners."""

import pytest
import shifty
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, SH

WATR = Namespace("https://watermetadata.org/ontology/watr#")
S223 = Namespace("http://data.ashrae.org/standard223#")
EX = Namespace("urn:example/gravity-thickener-outlets#")


@pytest.mark.parametrize("equipment_class", ["Clarifier", "GravityThickener"])
@pytest.mark.parametrize("case,expected_valid", [
    ("separate_outlets", True),
    ("specific_sludge", True),
    ("multiple_sludge_outlets", True),
    ("only_sludge_outlets", False),
    ("only_water_outlets", False),
    ("missing_liquid_medium", False),
    ("liquid_inlet_instead_of_outlet", False),
    ("one_outlet_with_both_media", False),
])
def test_separated_outlet_media(equipment_class, case, expected_valid,
                                ontology_shapes_graph):
    data = Graph().parse("examples/gravity-thickener-outlets.ttl")
    data.set((EX.thickener, RDF.type, WATR[equipment_class]))
    if case == "specific_sludge":
        data.set((EX.sludge, S223.hasMedium, WATR["Sludge-MixedLiquor"]))
    elif case == "multiple_sludge_outlets":
        data.add((EX.thickener, S223.hasConnectionPoint, EX.extraSludge))
        data.add((EX.extraSludge, RDF.type, S223.OutletConnectionPoint))
        data.add((EX.extraSludge, S223.hasMedium, WATR["Fluid-Sludge"]))
        data.add((EX.extraSludge, S223.isConnectionPointOf, EX.thickener))
    elif case == "only_sludge_outlets":
        data.set((EX.supernatant, S223.hasMedium, WATR["Fluid-Sludge"]))
    elif case == "only_water_outlets":
        data.set((EX.sludge, S223.hasMedium, S223["Fluid-Water"]))
    elif case == "missing_liquid_medium":
        data.remove((EX.supernatant, S223.hasMedium, None))
    elif case == "liquid_inlet_instead_of_outlet":
        data.set((EX.supernatant, RDF.type, S223.InletConnectionPoint))
    elif case == "one_outlet_with_both_media":
        data.remove((EX.sludge, None, None))
        data.remove((None, None, EX.sludge))
        data.add((EX.supernatant, S223.hasMedium, WATR["Fluid-Sludge"]))
    _, report, report_text = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    example_nodes = set(data.all_nodes())
    violations = [result for result in report.subjects(SH.resultSeverity, SH.Violation)
                  if report.value(result, SH.focusNode) in example_nodes]
    assert (not violations) == expected_valid, report_text
    if not expected_valid:
        # Assert rejection by the new requirements, not merely inherited shapes.
        assert any(report.value(result, SH.sourceShape) == WATR[equipment_class]
                   and report.value(result, SH.sourceConstraintComponent)
                   == SH.NodeConstraintComponent
                   and report.value(result, SH.focusNode) == EX.thickener
                   for result in violations), report_text
