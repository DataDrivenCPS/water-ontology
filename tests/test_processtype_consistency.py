"""Structural consistency checks on the compiled water ontology.

Complements the SHACL validation tests by asserting one structural invariant:

For every equipment class that constrains ``watr:hasProcess``, and for every
process required by any of its ancestor equipment classes, at least one of the
equipment's own required processes must be the same as, or a (transitive)
subclass of, that ancestor-required process. In other words, a subclass may
only *refine* (never contradict) the process rules it inherits
(e.g. ``BiologicalAeratedFilter.hasProcess`` must be a subclass of
``Filter.hasProcess``'s required class).

An equipment may pin more than one process (e.g. ``MembraneBioreactor`` requires
both a filtration and a biofiltration process); each ancestor-required process
just needs to be refined by *one* of them.

Where the ancestor states its requirement as a bare ``sh:class``, the check is
stricter: a bare ``sh:class`` has to hold for *every* value on the path, so every
process the subclass requires must refine it as well, otherwise no instance can
satisfy the parent and the child at the same time.

This invariant holds only because ``watr:hasProcess`` carries *mechanisms* alone.
A purpose a subclass achieves by some unrelated mechanism (thickening by
filtration, dewatering by centrifugation) belongs on ``s223:hasRole``, not here --
see ``docs/explanation/processes.md``. So a failure of this test usually means a
purpose has been modeled as a process type by mistake, rather than that the
invariant needs loosening.

Process rules are read from both the legacy shape (``sh:class`` directly on the
``hasProcess`` property shape) and the qualified-cardinality shape
(``sh:qualifiedValueShape`` carrying ``sh:class`` or an ``sh:in`` list).
"""
import sys
from pathlib import Path

import pytest
from rdflib import Graph, Namespace, URIRef


ROOT = Path(__file__).resolve().parents[1]
WATER_DIR = ROOT / "water"
WATR = Namespace("urn:nawi-water-ontology#")


CACHE = {}


def _qname(g: Graph, uri) -> str:
    try:
        prefix, _, local = g.compute_qname(uri)
        return f"{prefix}:{local}"
    except Exception:
        return str(uri)


def _find_equipments(g: Graph):
    """Return a set of all equipment classes."""
    q = """
    PREFIX watr: <urn:nawi-water-ontology#>
    PREFIX s223: <http://data.ashrae.org/standard223#>
    PREFIX sh: <http://www.w3.org/ns/shacl#>

    SELECT DISTINCT ?cls WHERE {
        ?cls a watr:Class .
        ?cls rdfs:subClassOf* s223:Equipment .
    }
    """
    if 'equipments' not in CACHE:
        CACHE['equipments'] = set(row.cls for row in g.query(q))
    return CACHE['equipments']


def _find_process_of_equip(equip_cls: URIRef, g: Graph):
    """Return the set of process classes required by an equipment via watr:hasProcess.

    Handles the legacy shape (``sh:class`` on the property shape) and the
    qualified-cardinality shape (``sh:qualifiedValueShape`` carrying ``sh:class``
    or an ``sh:in`` list of alternatives).
    """
    q = """
    PREFIX watr: <urn:nawi-water-ontology#>
    PREFIX sh: <http://www.w3.org/ns/shacl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT DISTINCT ?process WHERE {
        ?equip_cls sh:property ?shape .
        ?shape sh:path watr:hasProcess .
        {
            ?shape sh:class ?process .
        } UNION {
            ?shape sh:qualifiedValueShape/sh:class ?process .
        } UNION {
            ?shape sh:qualifiedValueShape/sh:in/rdf:rest*/rdf:first ?process .
        }
    }
    """
    if ('process_of_equip', equip_cls) not in CACHE:
        CACHE[('process_of_equip', equip_cls)] = set(
            row.process for row in g.query(q, initBindings={'equip_cls': equip_cls})
        )
    return CACHE[('process_of_equip', equip_cls)]


def _find_unqualified_process_of_equip(equip_cls: URIRef, g: Graph):
    """Return the processes an equipment requires of *every* watr:hasProcess value.

    That is only the bare ``sh:class`` form. A ``sh:qualifiedValueShape`` slot
    constrains one value, not all of them, so it imposes nothing on the other
    processes an instance may carry.
    """
    q = """
    PREFIX watr: <urn:nawi-water-ontology#>
    PREFIX sh: <http://www.w3.org/ns/shacl#>

    SELECT DISTINCT ?process WHERE {
        ?equip_cls sh:property ?shape .
        ?shape sh:path watr:hasProcess .
        ?shape sh:class ?process .
    }
    """
    if ('unqualified_process_of_equip', equip_cls) not in CACHE:
        CACHE[('unqualified_process_of_equip', equip_cls)] = set(
            row.process for row in g.query(q, initBindings={'equip_cls': equip_cls})
        )
    return CACHE[('unqualified_process_of_equip', equip_cls)]


def _find_equipment_class_ancestor_set(cls: URIRef, g: Graph):
    """Return the proper equipment superclasses of an equipment class."""
    q = """
    PREFIX watr: <urn:nawi-water-ontology#>
    PREFIX s223: <http://data.ashrae.org/standard223#>
    PREFIX sh: <http://www.w3.org/ns/shacl#>

    SELECT DISTINCT ?ancestor WHERE {
        ?cls rdfs:subClassOf* ?ancestor .
        ?ancestor rdfs:subClassOf* s223:Equipment .
        FILTER (?ancestor != ?cls) .
        FILTER (?ancestor != s223:Equipment) .
    }
    """
    return set(row.ancestor for row in g.query(q, initBindings={'cls': cls}))


def _find_process_class_ancestor_set(cls: URIRef, g: Graph):
    """Return the superclasses of a process class, including the class itself."""
    q = """
    PREFIX watr: <urn:nawi-water-ontology#>

    SELECT DISTINCT ?ancestor WHERE {
        ?cls rdfs:subClassOf* ?ancestor .
        FILTER (?ancestor != ?cls)
    }
    """
    ancestors = set(row.ancestor for row in g.query(q, initBindings={'cls': cls}))
    ancestors.add(cls)  # a process trivially refines itself
    return ancestors


@pytest.fixture(scope="module")
def water_graph() -> Graph:
    g = Graph()
    for path in sorted(WATER_DIR.glob("*.ttl")):
        g.parse(path, format="ttl")
    return g


def test_equipment_process_constraints_are_consistent(water_graph: Graph) -> None:
    g = water_graph
    equipments = _find_equipments(g)
    process_of_equip = {e: _find_process_of_equip(e, g) for e in equipments}
    unqualified_of_equip = {
        e: _find_unqualified_process_of_equip(e, g) for e in equipments
    }
    equipment_ancestors = {e: _find_equipment_class_ancestor_set(e, g) for e in equipments}

    referenced = set().union(*process_of_equip.values()) if process_of_equip else set()
    process_ancestors = {p: _find_process_class_ancestor_set(p, g) for p in referenced}

    # (equip, ancestor, ancestor_process, equip_processes)
    violations = []
    for equip, processes in process_of_equip.items():
        if not processes:
            continue
        for ancestor in equipment_ancestors[equip]:
            for ancestor_process in process_of_equip.get(ancestor, set()):
                # At least one of the equipment's processes must be the same as,
                # or a subclass of, the process the ancestor requires.
                refines = any(
                    ancestor_process in process_ancestors[p] for p in processes
                )
                if not refines:
                    violations.append((equip, ancestor, ancestor_process, processes))
                    continue
                # A bare sh:class on the ancestor is stronger than that: it has to
                # hold for EVERY value on the path, so every process this
                # equipment requires must refine it too, or no instance can
                # satisfy both at once.
                if ancestor_process in unqualified_of_equip.get(ancestor, set()):
                    stragglers = {
                        p for p in processes if ancestor_process not in process_ancestors[p]
                    }
                    if stragglers:
                        violations.append(
                            (equip, ancestor, ancestor_process, stragglers)
                        )

    if not violations:
        return

    lines = [f"{len(violations)} watr:hasProcess refinement inconsistency(ies):"]
    for equip, ancestor, ancestor_process, processes in violations:
        procs_str = ", ".join(sorted(_qname(g, p) for p in processes))
        lines.append(f"- {_qname(g, equip)} (subClassOf* {_qname(g, ancestor)})")
        lines.append(f"    ancestor requires: {_qname(g, ancestor_process)}")
        lines.append(f"    but equipment's processes are: {procs_str}")
        lines.append(
            f"    -> none of them is rdfs:subClassOf* {_qname(g, ancestor_process)}"
        )
    pytest.fail("\n".join(lines))
