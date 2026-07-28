"""Plausibility warnings for additional watr:hasProcess values.

``watr:hasProcess`` constraints say "performs at least this process", so they
permit further processes deliberately -- real equipment does more than its
defining process. ``watr:mayAlsoPerform`` records which further processes an
equipment family plausibly performs, and
``watr:ProcessPlausibilityShape`` (ontology.ttl) warns about the rest.

These are warnings, not violations: implausible is not impossible. The cases
below are the domain claims the permission table encodes, written out so a
reader can check them against what plants actually do.
"""

import pytest
import shifty
from rdflib import Graph, Namespace


SH = Namespace("http://www.w3.org/ns/shacl#")
WATR = Namespace("urn:nawi-water-ontology#")

PREFIX = "@prefix watr: <urn:nawi-water-ontology#> .\n@prefix ex: <urn:plausibility#> .\n"

# (equipment class, processes, expect_warning, why)
PLAUSIBLE = [
    ("MovingBedBioreactor", ["Biofiltration", "Aeration"],
     "an MBBR aerates to oxygenate and to keep its carriers moving"),
    ("BiologicalAeratedFilter", ["BiologicallyActiveFiltration", "Aeration"],
     "a BAF aerates, as the name says"),
    ("RotatingBiologicalContactor", ["Biofiltration", "Aeration"],
     "an RBC aerates its biofilm by rotating it clear of the liquid"),
    ("MicrofiltrationUnit", ["Microfiltration", "Backwashing"],
     "membranes are backwashed"),
    ("RapidSandFilter", ["RapidSandFiltration", "AirScouring"],
     "media filters are air scoured"),
    ("AnaerobicDigester", ["AnaerobicDigestion", "Mixing"],
     "digesters are mixed"),
    ("AnaerobicDigester", ["AnaerobicDigestion", "GasTransfer"],
     "digesters draw off biogas"),
    ("ChlorinationUnit", ["Chlorination", "Mixing"],
     "contact basins mix"),
    ("SequencingBatchReactor", ["ActivatedSludge", "Aeration"],
     "SBRs aerate"),
    ("SequencingBatchReactor", ["ActivatedSludge", "Recirculation"],
     "SBRs return sludge"),
]

IMPLAUSIBLE = [
    ("ChlorinationUnit", ["Chlorination", "ReverseOsmosis"],
     "a chlorination unit does not do membrane separation"),
    ("Screen", ["Screening", "AnaerobicDigestion"],
     "a screen does not digest"),
    ("MicrofiltrationUnit", ["Microfiltration", "Chlorination"],
     "a microfiltration unit does not dose chlorine"),
    ("RapidSandFilter", ["RapidSandFiltration", "Crystallization"],
     "a sand filter does not crystallize"),
]


def _probe_id(cls: str, procs: list[str]) -> str:
    """Stable identifier for one probe instance, used as its URI local name."""
    return f"{cls}_{'_'.join(procs)}"


@pytest.fixture(scope="module")
def plausibility_warnings(ontology_shapes_graph: Graph) -> dict[str, list[str]]:
    """Warnings per probe, from a single validation.

    Every probe is an independent focus node, so they all go in one graph and are
    validated once. Validating each separately costs a full pass over the import
    closure per case, which dominated the runtime of this module.
    """
    bodies = []
    for cls, procs, _ in PLAUSIBLE + IMPLAUSIBLE:
        node = _probe_id(cls, procs)
        bodies.append(
            f"ex:{node} a watr:{cls} ; watr:hasProcess "
            + ", ".join(f"watr:Process-{p}" for p in procs)
            + " ."
        )
    data = Graph().parse(data=PREFIX + "\n".join(bodies), format="ttl")

    _, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    found: dict[str, list[str]] = {_probe_id(c, p): [] for c, p, _ in PLAUSIBLE + IMPLAUSIBLE}
    for result in report.subjects(SH.sourceShape, WATR.ProcessPlausibilityShape):
        focus = str(report.value(result, SH.focusNode)).rsplit("#", 1)[-1]
        found.setdefault(focus, []).append(str(report.value(result, SH.resultMessage)))
    return found


@pytest.mark.parametrize(
    "cls,procs,why", PLAUSIBLE, ids=[f"{c}+{p[-1]}" for c, p, _ in PLAUSIBLE]
)
def test_plausible_combinations_are_not_flagged(cls, procs, why, plausibility_warnings):
    msgs = plausibility_warnings[_probe_id(cls, procs)]
    assert not msgs, f"{cls} with {procs} should be allowed ({why}):\n" + "\n".join(msgs)


@pytest.mark.parametrize(
    "cls,procs,why", IMPLAUSIBLE, ids=[f"{c}+{p[-1]}" for c, p, _ in IMPLAUSIBLE]
)
def test_implausible_combinations_are_flagged(cls, procs, why, plausibility_warnings):
    msgs = plausibility_warnings[_probe_id(cls, procs)]
    assert msgs, f"{cls} with {procs} should be flagged ({why})"


def test_plausibility_findings_are_warnings_not_violations(ontology_shapes_graph):
    """An implausible process must not make a model invalid.

    watr:Screen is used because it owes nothing else (it is not a Tank, so it
    has no connection point requirements), which makes the plausibility warning
    the only finding and lets us assert on the overall verdict.
    """
    body = (
        "ex:x a watr:Screen ; "
        "watr:hasProcess watr:Process-Screening, watr:Process-AnaerobicDigestion ."
    )
    data = Graph().parse(data=PREFIX + body, format="ttl")

    valid, report, _ = shifty.validate(data, shacl_graph=ontology_shapes_graph)
    severities = {
        report.value(r, SH.resultSeverity)
        for r in report.subjects(SH.sourceShape, WATR.ProcessPlausibilityShape)
    }
    assert severities == {SH.Warning}, severities
    assert not valid, "the implausible process should be reported at warning level"

    valid_at_violation, _, _ = shifty.validate(
        data, shacl_graph=ontology_shapes_graph, minimum_severity="violation"
    )
    assert valid_at_violation, (
        "a plausibility warning must not fail violation-level validation, "
        "which is the level tests/test_validation.py and the example tests use"
    )
