import logging

import shifty
from rdflib import Graph


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_ontology_validates(water_graph: Graph, ontology_shapes_graph: Graph):
    # Default graph_mode="union" selects focus nodes from water_graph alone
    # (so we only validate the water ontology's own classes/shapes, not every
    # node in the imported closure) while still evaluating constraints (e.g.
    # sh:class checks against qudt-defined types) against the full closure.
    valid, _, report_string = shifty.validate(
        water_graph,
        shacl_graph=ontology_shapes_graph,
        # match conftest.py's examples: only sh:Violation fails the test,
        # not sh:Warning/sh:Info (shifty's own default is "info").
        minimum_severity="violation",
    )
    print(report_string)
    assert valid, f"Ontology does not pass SHACL validation:\n{report_string}"
