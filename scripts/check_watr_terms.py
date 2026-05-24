"""
Check that every watr: term used in a directory of TTL files is defined in the
water ontology.

Usage:
    python scripts/check_watr_terms.py <target-dir> [--ontology-dir water/]
"""

import argparse
import sys
from pathlib import Path

from rdflib import Graph, URIRef
from rdflib.namespace import RDF

WATR_NS = "urn:nawi-water-ontology#"


def collect_defined_terms(ontology_dir: Path) -> set[URIRef]:
    """Return every subject URI in the watr: namespace across all TTL files in ontology_dir."""
    defined = set()
    ttl_files = list(ontology_dir.glob("*.ttl"))
    if not ttl_files:
        print(f"Warning: no .ttl files found in ontology directory {ontology_dir}", file=sys.stderr)
    for ttl in ttl_files:
        g = Graph()
        try:
            g.parse(ttl, format="turtle")
        except Exception as e:
            print(f"Warning: could not parse {ttl}: {e}", file=sys.stderr)
            continue
        for s in g.subjects():
            if isinstance(s, URIRef) and str(s).startswith(WATR_NS):
                defined.add(s)
    return defined


def check_directory(target_dir: Path, defined: set[URIRef]) -> dict[Path, list[URIRef]]:
    """
    Walk target_dir recursively, parse every .ttl file, and collect watr: URIs
    that appear as subjects or objects but are not in `defined`.

    Returns a mapping of file path -> sorted list of undefined URIs.
    """
    problems: dict[Path, list[URIRef]] = {}
    ttl_files = sorted(target_dir.rglob("*.ttl"))
    if not ttl_files:
        print(f"Warning: no .ttl files found under {target_dir}", file=sys.stderr)
    for ttl in ttl_files:
        g = Graph()
        try:
            g.parse(ttl, format="turtle")
        except Exception as e:
            print(f"Warning: could not parse {ttl}: {e}", file=sys.stderr)
            continue

        undefined: set[URIRef] = set()
        for s, _p, o in g:
            for node in (s, o):
                if isinstance(node, URIRef) and str(node).startswith(WATR_NS) and node not in defined:
                    undefined.add(node)

        if undefined:
            problems[ttl] = sorted(undefined, key=str)

    return problems


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find watr: terms used in a directory that are not defined in the water ontology."
    )
    parser.add_argument(
        "target_dir",
        type=Path,
        help="Directory to check (searched recursively for .ttl files)",
    )
    parser.add_argument(
        "--ontology-dir",
        type=Path,
        default=None,
        help="Directory containing the water ontology TTL files (default: <repo-root>/water/)",
    )
    args = parser.parse_args()

    if args.ontology_dir is None:
        # Default: water/ relative to this script's parent (the repo root)
        args.ontology_dir = Path(__file__).parent.parent / "water"

    ontology_dir = args.ontology_dir.resolve()
    target_dir = args.target_dir.resolve()

    if not ontology_dir.is_dir():
        print(f"Error: ontology directory not found: {ontology_dir}", file=sys.stderr)
        sys.exit(1)
    if not target_dir.is_dir():
        print(f"Error: target directory not found: {target_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Loading ontology from: {ontology_dir}")
    defined = collect_defined_terms(ontology_dir)
    print(f"  {len(defined)} watr: terms defined\n")

    print(f"Checking files under: {target_dir}")
    problems = check_directory(target_dir, defined)

    if not problems:
        print("All watr: terms are defined in the ontology.")
        sys.exit(0)

    total_undefined = sum(len(v) for v in problems.values())
    print(f"\nFound {total_undefined} undefined watr: term(s) across {len(problems)} file(s):\n")
    for filepath, terms in sorted(problems.items()):
        rel = filepath.relative_to(target_dir) if filepath.is_relative_to(target_dir) else filepath
        print(f"  {rel}")
        for term in terms:
            local = str(term).removeprefix(WATR_NS)
            print(f"    watr:{local}")
    sys.exit(1)


if __name__ == "__main__":
    main()
