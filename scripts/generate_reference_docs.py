"""Generate one reference section per term, listing all its parents together."""
from pathlib import Path

from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "equipment": ("Equipment", ("equipment",)),
    "processes": ("Processes", ("processtypes",)),
    "objectives": ("Treatment Objectives", ("objectives",)),
    "substances": ("Substances and Enumerations", ("substances", "enumerationkinds")),
}


def render(graph: Graph, title: str) -> str:
    lines = [f"# {title} Classes", ""]
    terms = sorted(set(graph.subjects(RDFS.label, None)), key=str)
    for term in terms:
        if not isinstance(term, URIRef) or (term, RDF.type, OWL.Ontology) in graph:
            continue
        description = graph.value(term, RDFS.comment) or graph.value(term, SKOS.definition)
        if description is None:
            continue
        lines.extend([f"## {graph.value(term, RDFS.label)}", "",
                      f"**Description:** {description}", ""])
        parents = sorted(graph.objects(term, RDFS.subClassOf), key=str)
        if parents:
            names = ", ".join(f"`{graph.namespace_manager.normalizeUri(parent)}`" for parent in parents)
            lines.extend([f"**Superclasses:** {names}", ""])
    return "\n".join(lines)


def main() -> None:
    for output, (title, modules) in SOURCES.items():
        graph = Graph()
        for module in modules:
            graph.parse(ROOT / "ontology" / f"{module}.ttl")
        path = ROOT / "docs" / "reference" / f"{output}_documentation.md"
        path.write_text(render(graph, title))
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
