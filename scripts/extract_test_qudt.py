"""Extract the QUDT 3.3.0 descriptions used by the offline test suite.

Download https://qudt.org/3.3.0/vocab/unit and
https://qudt.org/3.3.0/vocab/quantitykind as Turtle, then run:

    uv run python scripts/extract_test_qudt.py units.ttl quantitykinds.ttl
"""

import argparse
import re
from pathlib import Path

from rdflib import BNode, Graph, Namespace, URIRef


ROOT = Path(__file__).resolve().parents[1]
QUDT = Namespace("http://qudt.org/schema/qudt/")
VOCABULARIES = (
    "http://qudt.org/vocab/unit/",
    "http://qudt.org/vocab/quantitykind/",
)


def referenced_terms() -> set[URIRef]:
    """Find vocabulary IRIs in our source graphs and the bundled 223P graphs."""
    terms = set()
    for directory in ("ontology", "examples", "s223"):
        for path in sorted((ROOT / directory).rglob("*.ttl")):
            graph = Graph().parse(path)
            terms.update(
                node for node in graph.all_nodes()
                if isinstance(node, URIRef)
                and str(node).startswith(VOCABULARIES)
            )
    return terms


def extract(vocabularies: list[Graph], terms: set[URIRef]) -> Graph:
    """Copy full descriptions and blank-node objects, plus units' quantity kinds."""
    for term in list(terms):
        for graph in vocabularies:
            terms.update(graph.objects(term, QUDT.hasQuantityKind))

    result = Graph()
    for graph in vocabularies:
        for prefix, namespace in graph.namespaces():
            result.bind(prefix, namespace)
    pending = list(sorted(terms))
    visited = set()
    while pending:
        subject = pending.pop()
        if subject in visited:
            continue
        visited.add(subject)
        triples = [
            triple for graph in vocabularies
            for triple in graph.triples((subject, None, None))
        ]
        if not triples:
            raise ValueError(f"QUDT does not define {subject}")
        for triple in triples:
            result.add(triple)
            if isinstance(triple[2], BNode):
                pending.append(triple[2])
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("units", type=Path)
    parser.add_argument("quantitykinds", type=Path)
    args = parser.parse_args()
    vocabularies = [Graph().parse(path) for path in (args.units, args.quantitykinds)]
    terms = referenced_terms()
    subset = extract(vocabularies, terms)
    destination = ROOT / "tests/fixtures/qudt-3.3.0.ttl"
    destination.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# QUDT.org, CC BY 4.0: https://creativecommons.org/licenses/by/4.0/\n"
        "# Extracted from https://qudt.org/3.3.0/vocab/unit and\n"
        "# https://qudt.org/3.3.0/vocab/quantitykind.\n"
        "# This is a test vocabulary subset, not either complete ontology.\n"
        "# Regenerate with scripts/extract_test_qudt.py.\n\n"
    )
    serialized = subset.serialize(format="turtle").rstrip() + "\n"
    # Preserve whitespace in upstream multiline literals using Turtle escapes.
    serialized = re.sub(
        r"[ \t]+(?=\n)",
        lambda match: "".join(f"\\u{ord(char):04X}" for char in match[0]),
        serialized,
    )
    destination.write_text(header + serialized)
    print(f"{destination}: {len(terms)} terms, {len(subset)} triples")


if __name__ == "__main__":
    main()
