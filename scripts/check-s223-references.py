"""
Check that every s223: term referenced in the ontology modules is actually
defined in the vendored ASHRAE 223P library.

Usage:
    uv run scripts/check-s223-references.py [--ontology-dir ontology/] [--library libraries/223p.ttl]

Exits non-zero if any s223: URI is used (as subject, predicate, or object)
without being defined as a subject in the 223P library.
"""

import argparse
import sys
from collections import defaultdict
from pathlib import Path

from rdflib import Graph, URIRef

S223_NS = "http://data.ashrae.org/standard223#"


def defined_terms(library: Path) -> set[URIRef]:
    g = Graph().parse(library, format="turtle")
    return {s for s in g.subjects() if isinstance(s, URIRef) and str(s).startswith(S223_NS)}


def named_subject(g: Graph, node):
    """Walk up blank-node parents until a named subject is found."""
    seen = 0
    while not isinstance(node, URIRef) and seen < 20:
        parents = list(g.subjects(None, node))
        if not parents:
            return node
        node = parents[0]
        seen += 1
    return node


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ontology-dir", type=Path, default=Path("ontology"))
    ap.add_argument("--library", type=Path, default=Path("libraries/223p.ttl"))
    args = ap.parse_args()

    defined = defined_terms(args.library)
    total_missing = 0
    for ttl in sorted(args.ontology_dir.glob("*.ttl")):
        g = Graph().parse(ttl, format="turtle")
        uses: dict[URIRef, set[tuple[str, str]]] = defaultdict(set)
        for s, p, o in g:
            for term in (s, p, o):
                if isinstance(term, URIRef) and str(term).startswith(S223_NS) and term not in defined:
                    subj = named_subject(g, s)
                    label = g.qname(subj) if isinstance(subj, URIRef) else "_:bnode"
                    uses[term].add((label, g.qname(p)))
        if uses:
            print(f"{ttl}:")
            for term in sorted(uses):
                print(f"  undefined s223:{str(term)[len(S223_NS):]}")
                for label, pred in sorted(uses[term]):
                    print(f"      used by {label} via {pred}")
            total_missing += len(uses)

    if total_missing:
        print(f"\n{total_missing} undefined s223: term(s) found", file=sys.stderr)
        return 1
    print("All s223: references resolve against", args.library)
    return 0


if __name__ == "__main__":
    sys.exit(main())
