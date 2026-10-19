"""Complete compositions must permit 100%; partial descriptions need not."""

import pytest
import shifty
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import SH

from test_inference import _fraction, _graph_with

WATR = Namespace("https://watermetadata.org/ontology/watr#")
S223 = Namespace("http://data.ashrae.org/standard223#")
EX = Namespace("urn:example/complement#")
QUDT = Namespace("http://qudt.org/schema/qudt/")
KINDS = Namespace("http://qudt.org/vocab/quantitykind/")


@pytest.mark.parametrize("salt,water,aspect,expected", [
    (10, 80, None, True),
    (10, 90, None, False),
    (10, 80, "HighLimit", True),
    (20, 90, "HighLimit", False),
    (10, 80, "LowLimit", False),
    (10, None, None, False),
    (None, None, None, False),
])
@pytest.mark.parametrize("kind", ["MassFraction", "VolumeFraction"])
def test_complete_composition_feasibility(salt, water, aspect, expected, kind, water_graph):
    data = _graph_with(
        _fraction("salt", WATR["Salt-NaCl"], salt)
        + _fraction("water", S223["Constituent-H2O"], water), ":salt, :water",
    )
    for fraction in (EX.salt, EX.water):
        data.set((fraction, QUDT.hasQuantityKind, KINDS[kind]))
        if aspect:
            data.add((fraction, S223.hasAspect, S223[f"Aspect-{aspect}"]))
    _, report, _ = shifty.validate(data, shacl_graph=water_graph)
    results = list(report.subjects(SH.sourceShape, WATR.CompleteCompositionShape))
    assert bool(results) == expected
    assert all(report.value(result, SH.resultSeverity) == SH.Violation for result in results)


@pytest.mark.parametrize("complete", [None, False])
def test_partial_composition_may_total_less_than_100(complete, water_graph):
    data = _graph_with(
        _fraction("salt", WATR["Salt-NaCl"], 10)
        + _fraction("water", S223["Constituent-H2O"], 80), ":salt, :water",
    )
    data.remove((EX.medium, WATR.hasCompleteComposition, None))
    if complete is not None:
        data.add((EX.medium, WATR.hasCompleteComposition, Literal(complete)))
    _, report, _ = shifty.validate(data, shacl_graph=water_graph)
    assert not list(report.subjects(SH.sourceShape, WATR.CompleteCompositionShape))


def test_duplicate_upper_bounds_use_the_tightest_bound(water_graph):
    data = _graph_with(
        _fraction("saltA", WATR["Salt-NaCl"], 20)
        + _fraction("saltB", WATR["Salt-NaCl"], 10)
        + _fraction("water", S223["Constituent-H2O"], 80), ":saltA, :saltB, :water",
    )
    for fraction in (EX.saltA, EX.saltB, EX.water):
        data.add((fraction, S223.hasAspect, S223["Aspect-HighLimit"]))
    _, report, _ = shifty.validate(data, shacl_graph=water_graph)
    assert list(report.subjects(SH.sourceShape, WATR.CompleteCompositionShape))


def test_complete_composition_does_not_combine_different_bases(water_graph):
    data = _graph_with(
        _fraction("salt", WATR["Salt-NaCl"], 10)
        + _fraction("water", S223["Constituent-H2O"], 80), ":salt, :water",
    )
    data.set((EX.salt, QUDT.hasQuantityKind, KINDS.VolumeFraction))
    _, report, _ = shifty.validate(data, shacl_graph=water_graph)
    assert not list(report.subjects(SH.sourceShape, WATR.CompleteCompositionShape))


def test_nonconforming_example_fails_the_completeness_shape(water_graph):
    data = Graph().parse("examples/nonconforming/complete-composition-below-100-percent.ttl")
    _, report, _ = shifty.validate(data, shacl_graph=water_graph)
    assert list(report.subjects(SH.sourceShape, WATR.CompleteCompositionShape))
