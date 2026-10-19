"""Referenced vocabulary does not make an example own imported definitions."""

import pytest
import shifty
from rdflib import BNode, Graph, Literal, Namespace
from rdflib.namespace import RDF, SH

from conftest import (
    _has_example_violations,
    _has_example_warnings_or_violations,
)


EX = Namespace("urn:validation-scope:")


def _shapes(severity):
    shapes = Graph()
    shapes.add((EX.quantity_kind, RDF.type, EX.VocabularyTerm))
    shapes.add((EX.shape, RDF.type, SH.NodeShape))
    shapes.add((EX.shape, SH.targetObjectsOf, EX.observes))
    shapes.add((EX.shape, SH.property, EX.required_value))
    shapes.add((EX.required_value, SH.path, EX.value))
    shapes.add((EX.required_value, SH.minCount, Literal(1)))
    shapes.add((EX.required_value, SH.severity, severity))
    return shapes


@pytest.mark.parametrize("severity", [SH.Violation, SH.Warning, SH.Info])
@pytest.mark.parametrize(
    "focus, described, in_scope",
    [
        (EX.quantity_kind, False, False),
        (EX.quantity_kind, True, True),
        (EX.local_property, False, True),
        (BNode(), False, True),
    ],
    ids=["referenced-import", "edited-import", "local-object", "blank-node"],
)
def test_example_validation_scope(focus, described, in_scope, severity):
    data = Graph()
    data.add((EX.sensor, EX.observes, focus))
    if described:
        data.add((focus, EX.label, Literal("Locally described")))
    shapes = _shapes(severity)

    _, report, _ = shifty.validate(data, shacl_graph=shapes, infer=False)

    # Use a real SHACL result; only its ownership and severity affect filtering.
    assert (None, SH.focusNode, focus) in report
    assert (None, SH.resultSeverity, severity) in report
    assert _has_example_violations(data, report, shapes) is (
        in_scope and severity == SH.Violation
    )
    assert _has_example_warnings_or_violations(data, report, shapes) is (
        in_scope and severity in {SH.Warning, SH.Violation}
    )


@pytest.mark.parametrize("severity", [SH.Violation, SH.Warning])
def test_imported_result_does_not_hide_local_failure(severity):
    data = Graph()
    data.add((EX.sensor, EX.observes, EX.quantity_kind))
    data.add((EX.sensor, EX.observes, EX.local_property))
    shapes = _shapes(severity)

    _, report, _ = shifty.validate(data, shacl_graph=shapes, infer=False)

    assert (None, SH.focusNode, EX.quantity_kind) in report
    assert (None, SH.focusNode, EX.local_property) in report
    assert _has_example_warnings_or_violations(data, report, shapes)
    assert _has_example_violations(data, report, shapes) is (severity == SH.Violation)
