"""Documented processing values must satisfy S223's enumeration type guard."""

import pytest
import shifty
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, SH

WATR = Namespace("https://watermetadata.org/ontology/watr#")
S223 = Namespace("http://data.ashrae.org/standard223#")
EX = Namespace("urn:data-processing-aspects#")


@pytest.mark.parametrize("value,expected", [
    ("DataProcessing-Filter", True),
    ("Aggregate-Mean", True),
    ("Interpolation-Linear", True),
    ("Normalization-ZScore", True),
    ("Synchronization-Resampling", True),
    ("Error-Bias", True),
    ("Precision-RepeatabilityStdDev", True),
    ("Accuracy-RSquared", True),
    ("Process-Denitrification", False),
])
def test_processing_values_are_enumeration_aspects(value, expected, water_graph):
    data = Graph()
    data.add((EX.property, S223.hasAspect, WATR[value]))
    shapes = Graph() + water_graph
    shapes.add((EX.aspectGuard, RDF.type, SH.NodeShape))
    shapes.add((EX.aspectGuard, SH.targetObjectsOf, S223.hasAspect))
    shapes.add((EX.aspectGuard, SH['class'], S223.EnumerationKind))
    _, report, _ = shifty.validate(data, shacl_graph=shapes)
    failures = list(report.subjects(SH.sourceShape, EX.aspectGuard))
    assert (not failures) == expected
