"""Structural consistency checks on the compiled water ontology.

Two invariants are asserted, complementing the SHACL validation tests:

1. Every process class — anything named `watr:Process-*` or used as
   `sh:class` on `watr:hasProcess` — must reach `watr:Process` via
   `rdfs:subClassOf+`.
2. For every device NodeShape that constrains a property path with
   `sh:class`, the required class must be a (transitive) subclass of the
   class required by any ancestor device class on the same path
   (e.g. `BiologicalAeratedFilter.hasProcess` must be a subclass of
   `Filter.hasProcess`'s required class).
"""
from collections import defaultdict
from pathlib import Path

import pytest
from rdflib import Graph, Namespace, RDFS, SH


ROOT = Path(__file__).resolve().parents[1]
WATER_TTL = ROOT / "libraries" / "water.ttl"
WATR = Namespace("urn:nawi-water-ontology#")
PROCESS = WATR.Process


def _qname(g: Graph, uri) -> str:
    try:
        prefix, _, local = g.compute_qname(uri)
        return f"{prefix}:{local}"
    except Exception:
        return str(uri)


def _transitive_superclasses(g: Graph, cls) -> set:
    seen = set()
    stack = [cls]
    while stack:
        current = stack.pop()
        for parent in g.objects(current, RDFS.subClassOf):
            if parent in seen or parent == cls:
                continue
            seen.add(parent)
            stack.append(parent)
    return seen


def _is_subclass_of(g: Graph, child, parent) -> bool:
    if child == parent:
        return True
    return parent in _transitive_superclasses(g, child)


def _collect_class_constraints(g: Graph) -> dict:
    """Return {device_class: {path: set(required_classes)}}."""
    constraints = defaultdict(lambda: defaultdict(set))
    for shape, _, prop in g.triples((None, SH.property, None)):
        path = g.value(prop, SH.path)
        cls = g.value(prop, SH["class"])
        if path is None or cls is None:
            continue
        constraints[shape][path].add(cls)
    return constraints


def _collect_process_classes(g: Graph) -> set:
    """Anything named watr:Process-* or used as sh:class on watr:hasProcess."""
    candidates = set()
    watr_str = str(WATR)
    for s in set(g.subjects()):
        s_str = str(s)
        if s_str.startswith(watr_str) and s_str[len(watr_str):].startswith("Process-"):
            candidates.add(s)
    for _, _, prop in g.triples((None, SH.property, None)):
        if g.value(prop, SH.path) == WATR.hasProcess:
            cls = g.value(prop, SH["class"])
            if cls is not None:
                candidates.add(cls)
    candidates.discard(PROCESS)
    return candidates


@pytest.fixture(scope="module")
def water_graph() -> Graph:
    g = Graph()
    g.parse(WATER_TTL, format="ttl")
    return g


def test_all_processes_are_subclass_of_process(water_graph: Graph) -> None:
    violations = []
    for cls in sorted(_collect_process_classes(water_graph), key=str):
        if PROCESS not in _transitive_superclasses(water_graph, cls):
            parents = list(water_graph.objects(cls, RDFS.subClassOf))
            violations.append((cls, parents))

    if not violations:
        return

    lines = [
        f"{len(violations)} process class(es) are NOT rdfs:subClassOf* {_qname(water_graph, PROCESS)}:"
    ]
    for cls, parents in violations:
        parents_str = (
            ", ".join(_qname(water_graph, p) for p in parents)
            if parents
            else "(no rdfs:subClassOf declared)"
        )
        lines.append(f"- {_qname(water_graph, cls)}")
        lines.append(f"    direct parents: {parents_str}")
    pytest.fail("\n".join(lines))


def test_subclass_shacl_constraints_are_consistent(water_graph: Graph) -> None:
    constraints = _collect_class_constraints(water_graph)
    violations = []

    for device_cls, paths in constraints.items():
        ancestors = _transitive_superclasses(water_graph, device_cls)
        for path, required_classes in paths.items():
            for ancestor in ancestors:
                ancestor_required = constraints.get(ancestor, {}).get(path)
                if not ancestor_required:
                    continue
                for child_cls in required_classes:
                    for anc_cls in ancestor_required:
                        if not _is_subclass_of(water_graph, child_cls, anc_cls):
                            violations.append((device_cls, ancestor, path, child_cls, anc_cls))

    if not violations:
        return

    lines = [f"{len(violations)} sh:class constraint inconsistency(ies):"]
    for device, ancestor, path, child_cls, anc_cls in violations:
        lines.append(
            f"- {_qname(water_graph, device)} (subClassOf* {_qname(water_graph, ancestor)})"
        )
        lines.append(f"    path: {_qname(water_graph, path)}")
        lines.append(f"    requires: {_qname(water_graph, child_cls)}")
        lines.append(f"    but ancestor requires: {_qname(water_graph, anc_cls)}")
        lines.append(
            f"    -> {_qname(water_graph, child_cls)} is NOT rdfs:subClassOf* "
            f"{_qname(water_graph, anc_cls)}"
        )
    pytest.fail("\n".join(lines))
