import shifty
from rdflib import Graph, Literal, Namespace, URIRef


S223 = Namespace("http://data.ashrae.org/standard223#")
EX = Namespace("urn:example/brine-inferred-complement#")


def _inferred_values(data_graph: Graph, ontology_shapes_graph: Graph) -> Graph:
    """Run the ontology's SHACL-AF rules over an example graph."""
    return shifty.infer(data_graph, shapes_graph=ontology_shapes_graph).graph()


def _water_value(graph: Graph, medium: URIRef):
    """Return the value on the medium's water fraction, however it is named."""
    for fraction in graph.objects(medium, S223.composedOf):
        if graph.value(fraction, S223.ofConstituent) == S223["Constituent-H2O"]:
            return graph.value(fraction, S223.hasValue)
    raise AssertionError(f"no water fraction on {medium}")


def test_unquantified_blank_node_fraction_gets_the_complement(
    ontology_shapes_graph: Graph,
):
    """A percent composition missing one value is completed to 100%."""
    data_graph = Graph().parse("examples/brine-inferred-complement.ttl")
    medium = EX["Brine-12Percent"]
    assert _water_value(data_graph, medium) is None

    inferred = _inferred_values(data_graph, ontology_shapes_graph)
    assert _water_value(inferred, medium) == Literal(88)


def test_unquantified_named_fraction_gets_the_complement(
    ontology_shapes_graph: Graph,
):
    """Naming the fraction instead of leaving it anonymous works the same way."""
    data_graph = Graph().parse("examples/brine-inferred-complement.ttl")
    assert data_graph.value(EX["WaterFraction"], S223.hasValue) is None

    inferred = _inferred_values(data_graph, ontology_shapes_graph)
    assert inferred.value(EX["WaterFraction"], S223.hasValue) == Literal(88)


def _fraction(name: str, constituent: URIRef, value=None) -> str:
    """Render one percent composition fraction in Turtle."""
    value_line = f"    s223:hasValue {value} ;\n" if value is not None else ""
    return (
        f":{name} a s223:QuantifiableProperty ;\n"
        f"{value_line}"
        f"    s223:ofConstituent <{constituent}> ;\n"
        f"    qudt:hasUnit unit:PERCENT .\n"
    )


def _graph_with(fractions: str, composed: str) -> Graph:
    """Build a one-medium example graph from rendered fraction Turtle."""
    return Graph().parse(
        data=(
            "@prefix : <urn:example/complement#> .\n"
            "@prefix qudt: <http://qudt.org/schema/qudt/> .\n"
            "@prefix s223: <http://data.ashrae.org/standard223#> .\n"
            "@prefix unit: <http://qudt.org/vocab/unit/> .\n"
            f":medium s223:composedOf {composed} .\n" + fractions
        ),
        format="ttl",
    )


WATR = Namespace("https://watermetadata.org/ontology/watr#")
COMPLEMENT = Namespace("urn:example/complement#")


def test_complement_is_silent_when_two_constituents_are_unquantified(
    ontology_shapes_graph: Graph,
):
    """The remainder cannot be split between two unknown constituents."""
    data_graph = _graph_with(
        _fraction("salt", WATR["Salt-NaCl"], 20)
        + _fraction("solids", WATR["Constituent-SuspendedSolids"])
        + _fraction("water", S223["Constituent-H2O"]),
        ":salt, :solids, :water",
    )
    inferred = _inferred_values(data_graph, ontology_shapes_graph)
    assert inferred.value(COMPLEMENT["water"], S223.hasValue) is None
    assert inferred.value(COMPLEMENT["solids"], S223.hasValue) is None


def test_complement_is_silent_when_nothing_is_quantified(
    ontology_shapes_graph: Graph,
):
    """A composition that names a lone constituent is not forced to 100%."""
    data_graph = _graph_with(
        _fraction("water", S223["Constituent-H2O"]),
        ":water",
    )
    inferred = _inferred_values(data_graph, ontology_shapes_graph)
    assert inferred.value(COMPLEMENT["water"], S223.hasValue) is None


def test_complement_is_silent_when_siblings_are_ranges(
    ontology_shapes_graph: Graph,
):
    """A range has no single complement, so no value is invented."""
    data_graph = _graph_with(
        _fraction("saltLow", WATR["Salt-NaCl"], 5)
        + _fraction("saltHigh", WATR["Salt-NaCl"], 10)
        + _fraction("water", S223["Constituent-H2O"]),
        ":saltLow, :saltHigh, :water",
    )
    data_graph.add((COMPLEMENT["saltLow"], S223.hasAspect, S223["Aspect-LowLimit"]))
    data_graph.add((COMPLEMENT["saltHigh"], S223.hasAspect, S223["Aspect-HighLimit"]))
    inferred = _inferred_values(data_graph, ontology_shapes_graph)
    assert inferred.value(COMPLEMENT["water"], S223.hasValue) is None


def test_complement_is_silent_when_the_remainder_would_be_negative(
    ontology_shapes_graph: Graph,
):
    """An over-100% composition is reported, not patched with a negative value."""
    data_graph = _graph_with(
        _fraction("salt", WATR["Salt-NaCl"], 120)
        + _fraction("water", S223["Constituent-H2O"]),
        ":salt, :water",
    )
    inferred = _inferred_values(data_graph, ontology_shapes_graph)
    assert inferred.value(COMPLEMENT["water"], S223.hasValue) is None
