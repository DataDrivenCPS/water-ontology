"""watr:Pump is not an s223:Pump, but is reflected into one when it meets the
S223 pump shape, so a sludge pump stays clear of the S223 medium warning."""

import shifty
from rdflib import RDF, RDFS, Graph, Namespace


S223 = Namespace("http://data.ashrae.org/standard223#")
WATR = Namespace("https://watermetadata.org/ontology/watr#")
SH = Namespace("http://www.w3.org/ns/shacl#")
EX = Namespace("urn:example/pump#")

PREFIXES = """
@prefix ex: <urn:example/pump#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
"""


def _pump(name: str, medium: str) -> str:
    return f"""
ex:{name} a watr:Pump ; s223:hasConnectionPoint ex:{name}In, ex:{name}Out .
ex:{name}In a s223:InletConnectionPoint ; s223:hasMedium {medium} .
ex:{name}Out a s223:OutletConnectionPoint ; s223:hasMedium {medium} .
"""


def _data(*pumps: str) -> Graph:
    return Graph().parse(data=PREFIXES + "".join(pumps), format="ttl")


def test_water_pump_is_reflected_as_s223_pump(ontology_shapes_graph: Graph):
    data = _data(_pump("water", "s223:Fluid-Water"))
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    assert (EX.water, RDF.type, S223.Pump) in inferred


def test_sludge_pump_is_not_reflected_and_draws_no_warning(
    ontology_shapes_graph: Graph,
):
    data = _data(_pump("sludge", "watr:Fluid-Sludge"))
    inferred = shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()
    assert (EX.sludge, RDF.type, S223.Pump) not in inferred
    _valid, report, _text = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    severities = {
        report.value(r, SH.resultSeverity)
        for r in report.subjects(SH.focusNode, EX.sludge)
    }
    assert severities <= {SH.Info}


def test_s223_pump_is_a_watr_pump(water_graph: Graph):
    assert (S223.Pump, RDFS.subClassOf, WATR.Pump) in water_graph


def _info_messages(data: Graph, shapes_graph: Graph, node) -> list[str]:
    _valid, report, _text = shifty.validate(data, shacl_graph=shapes_graph)
    return [
        str(report.value(r, SH.resultMessage))
        for r in report.subjects(SH.focusNode, node)
        if report.value(r, SH.resultSeverity) == SH.Info
    ]


def test_sludge_pump_reports_the_workaround_at_info(ontology_shapes_graph: Graph):
    data = _data(_pump("sludge", "watr:Fluid-Sludge"))
    messages = _info_messages(data, ontology_shapes_graph, EX.sludge)
    assert any("Workaround" in m for m in messages)


def test_water_pump_does_not_report_the_workaround(ontology_shapes_graph: Graph):
    data = _data(_pump("water", "s223:Fluid-Water"))
    assert not _info_messages(data, ontology_shapes_graph, EX.water)
