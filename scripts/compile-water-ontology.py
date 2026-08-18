"""Compile the development modules into the two published ontology documents.

The five files under `ontology/` are development modules; they are never published.
What ships is a single merged document, emitted twice:

    build/water.ttl      IRI https://watermetadata.org/ontology/watr
    build/water-0.2.ttl  IRI https://watermetadata.org/ontology/0.2/watr

Only the water modules are merged. External dependencies (223P, QUDT, SHACL)
stay as `owl:imports` on the published ontology, so consumers resolve them
themselves rather than receiving a pinned copy baked into our distribution.

Both documents contain identical term definitions in the unversioned `watr:`
namespace. Only the ontology IRI, `owl:versionIRI`, and the `rdfs:isDefinedBy`
values differ, following QUDT's convention that a version identifies a document
and never a term.
"""

from datetime import date
from pathlib import Path

import rdflib
from rdflib import OWL, RDF, RDFS, Literal, URIRef
from rdflib.namespace import DCTERMS, XSD

# Bump this when cutting a release. Two-part, per QUDT: patch-level changes
# ship as an updated "latest" without minting a new versioned document.
ONTOLOGY_VERSION = "0.2"

BASE = "https://watermetadata.org/ontology"
WATR = rdflib.Namespace(f"{BASE}/watr#")
LATEST_IRI = URIRef(f"{BASE}/watr")
VERSIONED_IRI = URIRef(f"{BASE}/{ONTOLOGY_VERSION}/watr")

# The development modules are read straight off disk rather than through
# ontoenv: ontoenv indexes the whole repository, so a previously compiled
# build/water.ttl would shadow ontology/watr.ttl and fold the entire
# external closure back into the next build.
SOURCE_DIR = Path(__file__).resolve().parent.parent / "ontology"

BUILD_DIR = Path(__file__).resolve().parent.parent / "build"
LATEST_PATH = "build/water.ttl"
VERSIONED_PATH = f"build/water-{ONTOLOGY_VERSION}.ttl"


def load_modules() -> tuple[rdflib.Graph, set[URIRef]]:
    """Merge every development module, and report the ontology IRIs they declare."""
    graph = rdflib.Graph()
    sources = sorted(SOURCE_DIR.glob("*.ttl"))
    if not sources:
        raise SystemExit(f"no ontology sources found in {SOURCE_DIR}")
    for path in sources:
        graph.parse(path, format="turtle")
    internal = {
        s for s in graph.subjects(RDF.type, OWL.Ontology) if isinstance(s, URIRef)
    }
    if LATEST_IRI not in internal:
        raise SystemExit(f"{LATEST_IRI} is not declared in {SOURCE_DIR}")
    return graph, internal


def collect_external_imports(
    graph: rdflib.Graph, internal: set[URIRef]
) -> list[URIRef]:
    """Return the non-water ontologies imported by the merged modules.

    Imports between water modules are an artifact of how the sources are split
    up; once merged they mean nothing, so only external targets survive.
    """
    return sorted(
        {
            o
            for o in graph.objects(None, OWL.imports)
            if isinstance(o, URIRef) and o not in internal
        }
    )


def strip_module_metadata(graph: rdflib.Graph, internal: set[URIRef]) -> None:
    """Drop the module ontology declarations and every `owl:imports` statement.

    The modules are an authoring convenience, not part of the published
    distribution, so their IRIs should not appear in it. Imports are re-added to
    the published ontology node by `add_ontology_header`.
    """
    for triple in list(graph.triples((None, OWL.imports, None))):
        graph.remove(triple)
    for module in internal - {LATEST_IRI}:
        for triple in list(graph.triples((module, None, None))):
            graph.remove(triple)
        for triple in list(graph.triples((None, None, module))):
            graph.remove(triple)


def add_ontology_header(
    graph: rdflib.Graph, iri: URIRef, imports: list[URIRef]
) -> None:
    """Declare `iri` as the ontology, carrying over the root's own metadata."""
    if iri != LATEST_IRI:
        for _s, p, o in graph.triples((LATEST_IRI, None, None)):
            graph.add((iri, p, o))
        for triple in list(graph.triples((LATEST_IRI, None, None))):
            graph.remove(triple)

    graph.add((iri, RDF.type, OWL.Ontology))
    graph.add((iri, OWL.versionIRI, iri))
    graph.add((iri, OWL.versionInfo, Literal(ONTOLOGY_VERSION)))
    graph.add((iri, RDFS.isDefinedBy, iri))
    graph.add((iri, DCTERMS.modified, Literal(date.today().isoformat(), datatype=XSD.date)))
    graph.set(
        (iri, RDFS.label, Literal(f"NAWI Water Ontology - Version {ONTOLOGY_VERSION}"))
    )
    for target in imports:
        graph.add((iri, OWL.imports, target))


def add_is_defined_by(graph: rdflib.Graph, iri: URIRef) -> int:
    """Point every `watr:` term at the ontology document that defines it."""
    terms = {
        s
        for s in graph.subjects()
        if isinstance(s, URIRef) and str(s).startswith(str(WATR))
    }
    for term in terms:
        graph.remove((term, RDFS.isDefinedBy, None))
        graph.add((term, RDFS.isDefinedBy, iri))
    return len(terms)


def bind_prefixes(graph: rdflib.Graph) -> None:
    graph.bind("watr", WATR)
    graph.bind("s223", rdflib.Namespace("http://data.ashrae.org/standard223#"))
    graph.bind("qudt", rdflib.Namespace("http://qudt.org/schema/qudt/"))
    graph.bind("unit", rdflib.Namespace("http://qudt.org/vocab/unit/"))
    graph.bind("quantitykind", rdflib.Namespace("http://qudt.org/vocab/quantitykind/"))
    graph.bind("dcterms", DCTERMS)


def build(iri: URIRef, path: str) -> None:
    graph, internal = load_modules()
    imports = collect_external_imports(graph, internal)
    strip_module_metadata(graph, internal)
    add_ontology_header(graph, iri, imports)
    term_count = add_is_defined_by(graph, iri)
    bind_prefixes(graph)
    graph.serialize(path)
    print(f"{path}: {iri}")
    print(f"  {len(graph)} triples, {term_count} watr: terms")
    for target in imports:
        print(f"  imports {target}")


def main() -> None:
    BUILD_DIR.mkdir(exist_ok=True)
    build(LATEST_IRI, LATEST_PATH)
    build(VERSIONED_IRI, VERSIONED_PATH)


if __name__ == "__main__":
    main()
