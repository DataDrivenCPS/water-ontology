"""Render each documented ontology module as a Markdown reference page.

Every watr: term carries an rdfs:label and an rdfs:comment (CONTRIBUTING.md,
"Adding and changing terms"), which is enough to publish a browsable list of
what a module defines. This renders one page per module, in the order the terms
appear in the source, so the generated page keeps the grouping of the file it
came from.

Run via `make reference-docs`; `make local-docs` depends on it.
"""

from pathlib import Path

import rdflib
from rdflib.namespace import OWL, RDF, RDFS

ROOT = Path(__file__).resolve().parent.parent
ONTOLOGY_DIR = ROOT / "ontology"
REFERENCE_DIR = ROOT / "docs" / "reference"

# Source module -> (page, heading). The page names are the ones docs/_toc.yml
# publishes: substances_documentation.md is the enumeration-kind vocabulary.
PAGES = [
    ("equipment.ttl", "equipment_documentation.md", "Equipment"),
    ("enumerationkinds.ttl", "substances_documentation.md", "EnumerationKinds"),
]


def local_name(graph: rdflib.Graph, uri: rdflib.URIRef) -> str:
    """Return the trailing name of a URI, without its namespace."""
    _, _, name = graph.compute_qname(uri)
    return name


def documented_terms(graph: rdflib.Graph) -> list[rdflib.URIRef]:
    """Return the labelled, commented terms of a module, in source order."""
    terms = []
    for term in graph.subjects(RDFS.label, None, unique=True):
        if not isinstance(term, rdflib.URIRef):
            continue
        if (term, RDF.type, OWL.Ontology) in graph:
            continue
        if graph.value(term, RDFS.comment) is None:
            continue
        terms.append(term)
    return terms


def render(graph: rdflib.Graph, heading: str) -> str:
    """Render one module's terms as Markdown."""
    sections = [f"# {heading} Classes\n"]
    for term in documented_terms(graph):
        # A term may declare several parents (watr:Reactor is both a Tank and a
        # UnitProcess); name them all in one section rather than repeating the
        # term once per parent.
        parents = sorted(
            local_name(graph, parent)
            for parent in graph.objects(term, RDFS.subClassOf)
            if isinstance(parent, rdflib.URIRef)
        )
        section = [
            f"## {graph.value(term, RDFS.label)}\n",
            f"**Description:** {graph.value(term, RDFS.comment)}\n",
        ]
        if parents:
            label = "Superclass" if len(parents) == 1 else "Superclasses"
            section.append(f"**{label}:** {', '.join(parents)}\n")
        sections.append("\n".join(section))
    return "\n".join(sections)


def main() -> None:
    for module, page, heading in PAGES:
        graph = rdflib.Graph()
        graph.parse(ONTOLOGY_DIR / module, format="turtle")
        out = REFERENCE_DIR / page
        out.write_text(render(graph, heading))
        print(f"{out.relative_to(ROOT)}: {len(documented_terms(graph))} terms from {module}")


if __name__ == "__main__":
    main()
