"""watr:Fluid-Sludge is a s223:Mix-Fluid, not a s223:Fluid-Water. What keeps it
compatible with water on S223 connection points is the s223:Constituent-H2O it
is composedOf. S223 reports a medium mismatch on a Filter's connection points at
severity sh:Warning, which test_examples_validate ignores, so these tests look at
every severity."""

from pathlib import Path

import shifty
from rdflib import Graph, Namespace


S223 = Namespace("http://data.ashrae.org/standard223#")
SH = Namespace("http://www.w3.org/ns/shacl#")
WATR = Namespace("https://watermetadata.org/ontology/watr#")

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "clarifier-sludge-compatibility.ttl"


def _compatibility_messages(data_graph: Graph, shapes_graph: Graph) -> list[str]:
    """Return every S223 medium-compatibility message raised on an example node."""
    _valid, report, _text = shifty.validate(data_graph, shacl_graph=shapes_graph)
    example_nodes = set(data_graph.all_nodes())
    messages = []
    for result in report.subjects(SH.focusNode, None):
        if report.value(result, SH.focusNode) not in example_nodes:
            continue
        message = str(report.value(result, SH.resultMessage) or "")
        if "compatible" in message.lower():
            messages.append(message)
    return sorted(set(messages))


def _without_water_in_sludge(shapes_graph: Graph) -> Graph:
    """Copy the shapes graph and drop the water fraction from Fluid-Sludge."""
    stripped = Graph()
    for triple in shapes_graph:
        stripped.add(triple)
    for fraction in list(stripped.objects(WATR["Fluid-Sludge"], S223.composedOf)):
        if stripped.value(fraction, S223.ofConstituent) == S223["Constituent-H2O"]:
            stripped.remove((WATR["Fluid-Sludge"], S223.composedOf, fraction))
    return stripped


def test_sludge_is_a_mixture_not_water(water_graph: Graph):
    """Sludge subclasses Mix-Fluid directly and no longer inherits from Fluid-Water."""
    from rdflib import RDFS

    parents = set(water_graph.objects(WATR["Fluid-Sludge"], RDFS.subClassOf))
    assert parents == {S223["Mix-Fluid"]}


def test_sludge_declares_water_and_solids_constituents(water_graph: Graph):
    constituents = {
        water_graph.value(fraction, S223.ofConstituent)
        for fraction in water_graph.objects(WATR["Fluid-Sludge"], S223.composedOf)
    }
    assert constituents == {
        S223["Constituent-H2O"],
        WATR["Constituent-OrganicSolids"],
        WATR["Constituent-InorganicSolids"],
    }


def test_sludge_and_water_are_compatible_in_both_directions(ontology_shapes_graph: Graph):
    """Water in and sludge out, then sludge in and water out, raise no medium result at any severity."""
    data_graph = Graph().parse(EXAMPLE)
    assert _compatibility_messages(data_graph, ontology_shapes_graph) == []


def test_shared_water_constituent_is_what_makes_sludge_compatible(ontology_shapes_graph: Graph):
    """Without Constituent-H2O on sludge, S223 flags the Filter's water and sludge connection points."""
    data_graph = Graph().parse(EXAMPLE)
    messages = _compatibility_messages(data_graph, _without_water_in_sludge(ontology_shapes_graph))
    assert messages, "expected S223 to report sludge and water as incompatible once the water fraction is removed"
    assert any("Fluid-Sludge" in message and "Fluid-Water" in message for message in messages)
