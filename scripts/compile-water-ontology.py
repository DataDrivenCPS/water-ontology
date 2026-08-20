"""Compile the development modules into the two published ontology documents.

The files under `ontology/` are development modules; they are never published.
What ships is a single merged document, emitted twice:

    build/watr.ttl      IRI https://watermetadata.org/ontology/watr
    build/watr-0.2.ttl  IRI https://watermetadata.org/ontology/0.2/watr

Which modules get merged is decided by `owl:imports`, not by what happens to
sit in the directory. The compile starts at `ontology/watr.ttl` and walks the
import closure, keeping every graph whose IRI is under
`https://watermetadata.org/ontology/`. A module is therefore included because
something imports it: dropping a new .ttl into `ontology/` does nothing until
`watr.ttl` (or a module it already reaches) imports it.

Imports that leave that namespace -- 223P, QUDT, SHACL -- are not followed.
They are re-declared as `owl:imports` on the published ontology, so consumers
resolve them at whatever version they already have rather than receiving a
pinned copy baked into our distribution.

Both documents contain identical term definitions in the unversioned `watr:`
namespace. Only the ontology IRI, `owl:versionIRI`, and the `rdfs:isDefinedBy`
values differ, following QUDT's convention that a version identifies a document
and never a term.

Import resolution goes through OntoEnv, so the environment must be current:
run `make build-ontology`, which refreshes it first, or `uv run ontoenv update`
by hand.
"""

from datetime import date
from pathlib import Path

import ontoenv
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

# Graphs under this prefix are ours: merged into the published document.
# Anything else is an external dependency and stays an owl:imports.
INTERNAL_PREFIX = f"{BASE}/"

REPO_ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = REPO_ROOT / "build"
LATEST_PATH = "build/watr.ttl"
VERSIONED_PATH = f"build/watr-{ONTOLOGY_VERSION}.ttl"


def is_internal(iri: URIRef) -> bool:
    return str(iri).startswith(INTERNAL_PREFIX)


def connect() -> ontoenv.OntoEnv:
    """Open the OntoEnv environment, explaining how to create it if absent."""
    try:
        return ontoenv.OntoEnv.connect(str(REPO_ROOT), read_only=True)
    except Exception as exc:  # noqa: BLE001 - surfaced verbatim below
        raise SystemExit(
            f"could not open the OntoEnv environment: {exc}\n"
            "Run `make build-ontology`, or `uv run ontoenv update` to refresh it."
        ) from exc


def check_not_shadowed(env: ontoenv.OntoEnv) -> None:
    """Fail loudly if a compiled artifact is standing in for the sources.

    A published document declares the same ontology IRI as ontology/watr.ttl,
    so an environment that indexes build/ will resolve the root to a previous
    build and fold the whole external closure back in.
    """
    location = str(env.get_ontology(str(LATEST_IRI)).location)
    if "/ontology/" not in location:
        raise SystemExit(
            f"{LATEST_IRI} resolves to {location}, not the sources in ontology/.\n"
            "The environment is indexing a build artifact. Re-create it with "
            "`make clean && make build-ontology`."
        )


def walk_closure(env: ontoenv.OntoEnv) -> tuple[rdflib.Graph, list[URIRef], list[URIRef]]:
    """Merge the internal import closure rooted at the published ontology.

    Returns the merged graph, the internal IRIs that were merged, and the
    external IRIs to re-declare as imports.
    """
    graph = rdflib.Graph()
    merged: list[URIRef] = []
    external: set[URIRef] = set()
    queue = [LATEST_IRI]
    seen: set[URIRef] = set()

    while queue:
        iri = queue.pop(0)
        if iri in seen:
            continue
        seen.add(iri)
        try:
            module = env.copy_graph(str(iri))
        except Exception as exc:  # noqa: BLE001 - surfaced verbatim below
            raise SystemExit(
                f"could not resolve {iri}, imported within the water ontology: {exc}\n"
                "If you just added a module, run `uv run ontoenv update`."
            ) from exc
        graph += module
        merged.append(iri)
        for target in sorted(module.objects(None, OWL.imports)):
            if not isinstance(target, URIRef):
                continue
            if is_internal(target):
                queue.append(target)
            else:
                external.add(target)

    return graph, merged, sorted(external)


def strip_module_metadata(graph: rdflib.Graph, merged: list[URIRef]) -> None:
    """Drop the module ontology declarations and every `owl:imports` statement.

    The modules are an authoring convenience, not part of the published
    distribution, so their IRIs should not appear in it. Imports are re-added to
    the published ontology node by `add_ontology_header`.
    """
    for triple in list(graph.triples((None, OWL.imports, None))):
        graph.remove(triple)
    for module in set(merged) - {LATEST_IRI}:
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


def build(env: ontoenv.OntoEnv, iri: URIRef, path: str) -> None:
    graph, merged, imports = walk_closure(env)
    strip_module_metadata(graph, merged)
    add_ontology_header(graph, iri, imports)
    term_count = add_is_defined_by(graph, iri)
    bind_prefixes(graph)
    graph.serialize(path)
    print(f"{path}: {iri}")
    print(f"  {len(graph)} triples, {term_count} watr: terms")
    for module in merged:
        if module != LATEST_IRI:
            print(f"  merged  {module}")
    for target in imports:
        print(f"  imports {target}")


def main() -> None:
    env = connect()
    check_not_shadowed(env)
    BUILD_DIR.mkdir(exist_ok=True)
    build(env, LATEST_IRI, LATEST_PATH)
    build(env, VERSIONED_IRI, VERSIONED_PATH)


if __name__ == "__main__":
    main()
