"""Connection points of a sequencing batch reactor."""

import pytest
import shifty
from rdflib import Graph, Namespace
from rdflib.namespace import SH

EX = Namespace("urn:example/sbr#")
S223 = Namespace("http://data.ashrae.org/standard223#")

SBR = """
@prefix : <urn:example/sbr#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .

:sbr a watr:SequencingBatchReactor ; rdfs:label "SBR" .
:fill a s223:InletConnectionPoint ; rdfs:label "Fill" ;
    s223:hasMedium s223:Fluid-Water ; s223:isConnectionPointOf :sbr .
:decant a s223:OutletConnectionPoint ; rdfs:label "Decant" ;
    s223:hasMedium s223:Fluid-Water ; s223:isConnectionPointOf :sbr .
:was a s223:OutletConnectionPoint ; rdfs:label "Waste sludge" ;
    s223:hasMedium watr:Fluid-Sludge ; s223:isConnectionPointOf :sbr .
:overflow a s223:OutletConnectionPoint ; rdfs:label "Overflow" ;
    s223:hasMedium s223:Fluid-Water ; s223:isConnectionPointOf :sbr .
:fillAndDraw a s223:BidirectionalConnectionPoint ; rdfs:label "Fill and draw" ;
    s223:hasMedium s223:Fluid-Water ; s223:isConnectionPointOf :sbr .
"""


@pytest.mark.parametrize("ports,expected_valid", [
    # Fill, decant and waste sludge: the ordinary SBR.
    (("fill", "decant", "was"), True),
    # A fill-and-draw port in addition is allowed. It used to fail an
    # exactly-one-of choice between inlet/outlet and bidirectional ports.
    (("fill", "decant", "was", "fillAndDraw"), True),
    # The waste sludge outlet is the SBR's own requirement: two water outlets
    # meet the separation tank's count but not this.
    (("fill", "decant", "overflow"), False),
    # A bidirectional port does not replace the reactor's inlet and outlet.
    (("fillAndDraw", "was"), False),
])
def test_sbr_ports(ports, expected_valid, ontology_shapes_graph):
    data = Graph().parse(data=SBR, format="turtle")
    for port in ports:
        data.add((EX.sbr, S223.hasConnectionPoint, EX[port]))
    for port in {"fill", "decant", "was", "overflow", "fillAndDraw"} - set(ports):
        data.remove((EX[port], None, None))
    _, report, report_text = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    violations = [r for r in report.subjects(SH.resultSeverity, SH.Violation)
                  if report.value(r, SH.focusNode) == EX.sbr]
    assert (not violations) == expected_valid, report_text
