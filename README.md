# NAWI Water Ontology

## URIs and Versioning

Terms live in a single, permanently unversioned namespace:

```
https://watermetadata.org/ontology/watr#Pump
```

A version identifies a *document*, never a term — the convention QUDT, Brick,
and ASHRAE 223P all follow. `watr:Pump` means the same thing in every release,
so upgrading the ontology never requires rewriting existing models.

| Role | IRI |
| --- | --- |
| Term namespace (`watr:`) | `https://watermetadata.org/ontology/watr#` |
| Published document, latest | `https://watermetadata.org/ontology/watr` |
| Published document, versioned | `https://watermetadata.org/ontology/0.2/watr` |
| Development modules (not published) | `https://watermetadata.org/ontology/modules/{equipment,processtypes,substances,enumerationkinds}` |

The two published documents have identical term definitions. They differ only
in their ontology IRI, `owl:versionIRI`, and the `rdfs:isDefinedBy` each term
carries. Version numbers are two-part; patch-level fixes ship as an updated
`latest` rather than a new versioned document.

Terms are never renamed or re-namespaced when they change. Retire one with
`owl:deprecated true` plus `dcterms:isReplacedBy` pointing at its successor.

To cut a release, bump `ONTOLOGY_VERSION` in
`scripts/compile-water-ontology.py` and the matching variable in the `Makefile`.

## Layout

- `ontology/` contains our ontology source modules — edit these
- `build/` contains the compiled ontology documents (generated, not tracked)
- `s223/` contains ontology files from the 223P ontology
- `libraries/` contains BuildingMOTIF libraries and templates for building models
    - `templates` contains some water-specific templates
    - `nrel-223p-templates` contains some generic templates for the 223P ontology
    - `223p.ttl` is a recent copy of the 223P ontology
- `notebooks/` contains code showing how to build and query models.

## Development Setup

0. (to update 223, run the `download-s223.sh` script; this will only work for those with existing access to that repo)
1. Install [`uv`](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) for working with Python
2. Install the dependencies with `uv sync`
3. `uv sync` installs OntoEnv 0.6 or later for both the Python API and CLI. Run it as `uv run ontoenv`; no separate CLI installation is needed. If you need a system-wide CLI, use `cargo install --locked ontoenv-cli`.

## Building the Ontology

Run `make build-ontology` to build the ontology, or `make test` to build and
run the test suite. Neither needs a separate setup step: the OntoEnv
environment in `.ontoenv/` is created on first use and then left alone.

It only has to resolve the external dependencies (223P, QUDT, SHACL) — the
compiler and the tests both read `ontology/` straight off disk — so editing a
module never requires refreshing it. After updating `s223/`, run
`uv run ontoenv update`, or delete `.ontoenv/` (`make clean`) to rebuild it.

One compile emits both published documents:

- `build/water.ttl` — the unversioned "latest" copy
- `build/water-0.2.ttl` — the immutable versioned snapshot

Only the modules under `ontology/` are merged. External dependencies (223P, QUDT,
SHACL) stay as `owl:imports` on the published ontology rather than being copied
in, so consumers resolve them at whatever version they already have. Loading the
published document therefore requires an import resolver (OntoEnv, or
BuildingMOTIF with 223P loaded alongside).

Publishing means copying these to the site repo behind `watermetadata.org` as
`/ontology/watr` and `/ontology/0.2/watr`. Note that GitHub Pages serves an
extensionless file as `application/octet-stream`, so consumers may need to be
told the format explicitly (`Graph().parse(url, format="turtle")`).

## BMotif Libraries and Template Documentation

`libraries` contains a few libraries that can be used to build up the treatment train models

See the ModelBuilder notebook for more information on how to use these libraries and templates to build models

To document the templates, run `make local-docs` and open `docs/_build/html/index.html` in a browser. This should also auto-build when you push to the repostitory, making the docs available at https://datadrivencps.github.io/water-ontology/
# water-models
