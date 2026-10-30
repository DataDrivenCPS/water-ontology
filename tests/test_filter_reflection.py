"""watr:Filter is not an s223:Filter, but is reflected into one when it meets
the S223 filter shape, so a filter with air scour or vent ports beside its water
ports stays clear of the S223 medium violation."""

import shifty
from rdflib import RDF, RDFS, Graph, Namespace


S223 = Namespace("http://data.ashrae.org/standard223#")
WATR = Namespace("https://watermetadata.org/ontology/watr#")
SH = Namespace("http://www.w3.org/ns/shacl#")
EX = Namespace("urn:example/filter#")

PREFIXES = """
@prefix ex: <urn:example/filter#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
"""

WATER_FILTER = """
ex:water a watr:Filter ; watr:hasProcess watr:Process-Filtration ;
    s223:hasConnectionPoint ex:waterIn, ex:waterOut .
ex:waterIn a s223:InletConnectionPoint ; s223:hasMedium s223:Fluid-Water .
ex:waterOut a s223:OutletConnectionPoint ; s223:hasMedium s223:Fluid-Water .
"""

AIR_SCOURED_FILTER = """
ex:baf a watr:BiologicalAeratedFilter ;
    watr:hasProcess watr:Process-BiologicallyActiveFiltration ;
    s223:hasConnectionPoint ex:bafTop, ex:bafBottom, ex:bafAirIn, ex:bafAirVent .
ex:bafTop a s223:BidirectionalConnectionPoint ; s223:hasMedium s223:Fluid-Water .
ex:bafBottom a s223:BidirectionalConnectionPoint ; s223:hasMedium s223:Fluid-Water .
ex:bafAirIn a s223:InletConnectionPoint ; s223:hasMedium s223:Fluid-Air .
ex:bafAirVent a s223:OutletConnectionPoint ; s223:hasMedium s223:Fluid-Air .
"""

WATER_OIL_FILTER = """
ex:oil a watr:Filter ; watr:hasProcess watr:Process-Filtration ;
    s223:hasConnectionPoint ex:oilIn, ex:oilOut .
ex:oilIn a s223:InletConnectionPoint ; s223:hasMedium s223:Fluid-Water .
ex:oilOut a s223:OutletConnectionPoint ; s223:hasMedium s223:Fluid-Oil .
"""


def _data(*filters: str) -> Graph:
    return Graph().parse(data=PREFIXES + "".join(filters), format="ttl")


def _results(data: Graph, shapes_graph: Graph, node) -> list[tuple]:
    _valid, report, _text = shifty.validate(data, shacl_graph=shapes_graph)
    return [
        (report.value(r, SH.resultSeverity), str(report.value(r, SH.resultMessage)))
        for r in report.subjects(SH.focusNode, node)
    ]


def test_water_filter_is_reflected_as_s223_filter(ontology_shapes_graph: Graph):
    inferred = shifty.infer(_data(WATER_FILTER), shapes_graph=ontology_shapes_graph).graph()
    assert (EX.water, RDF.type, S223.Filter) in inferred


def test_air_scoured_filter_is_not_reflected_and_draws_no_violation(
    ontology_shapes_graph: Graph,
):
    data = _data(AIR_SCOURED_FILTER)
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    assert (EX.baf, RDF.type, S223.Filter) not in inferred
    severities = {severity for severity, _ in _results(data, ontology_shapes_graph, EX.baf)}
    assert severities <= {SH.Info}


def test_air_scoured_filter_reports_the_workaround_at_info(ontology_shapes_graph: Graph):
    results = _results(_data(AIR_SCOURED_FILTER), ontology_shapes_graph, EX.baf)
    assert any(severity == SH.Info and "Workaround" in message for severity, message in results)


def test_water_filter_does_not_report_the_workaround(ontology_shapes_graph: Graph):
    results = _results(_data(WATER_FILTER), ontology_shapes_graph, EX.water)
    assert not [message for _, message in results if "Workaround" in message]


def test_non_air_media_are_still_compared(ontology_shapes_graph: Graph):
    """Leaving air out of the comparison must not silence S223's other cases."""
    results = _results(_data(WATER_OIL_FILTER), ontology_shapes_graph, EX.oil)
    assert any(
        severity == SH.Violation and "incompatible" in message
        for severity, message in results
    )


def test_watr_filter_is_not_an_s223_filter(water_graph: Graph):
    """The workaround: watr:Filter sits beside s223:Filter, not under it."""
    assert (WATR.Filter, RDFS.subClassOf, S223.Filter) not in water_graph
    assert (WATR.Filter, RDFS.subClassOf, S223.Equipment) in water_graph
