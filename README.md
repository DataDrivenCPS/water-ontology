
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23087793.svg)](https://doi.org/10.5281/zenodo.23087793)

# Water Treatment (WaTr) Ontology

## URIs and Versioning

Terms live in a single, permanently unversioned namespace:

```
https://watermetadata.org/ontology/watr#Pump
```

A version identifies a *document*, never a term — the convention QUDT, Brick,
and ASHRAE 223P all follow. `watr:Pump` means the same thing in every release,
so upgrades do not require changing term namespaces. Deprecated terms identify
their replacements; modeling constraints may still require a model update.

| Role | IRI |
| --- | --- |
| Term namespace (`watr:`) | `https://watermetadata.org/ontology/watr#` |
| Published document, latest | `https://watermetadata.org/ontology/watr` |
| Published document, versioned | `https://watermetadata.org/ontology/0.2/watr` |
| Development modules (not published) | `https://watermetadata.org/ontology/modules/{equipment,processtypes,objectives,class-defaults,substances,enumerationkinds}` |

The two published documents have identical term definitions. They differ only
in their ontology IRI, `owl:versionIRI`, and the `rdfs:isDefinedBy` each term
carries. Version numbers are two-part; patch-level fixes ship as an updated
`latest` rather than a new versioned document.

Terms are never renamed or re-namespaced when they change. Retire one with
`owl:deprecated true` plus `dcterms:isReplacedBy` pointing at its successor.

To cut a release, bump `ONTOLOGY_VERSION` in
`scripts/compile-water-ontology.py`.

## Layout

- `ontology/` contains our ontology source modules — edit these
- `build/` contains the compiled ontology documents (generated, not tracked)
- `libraries/` contains BuildingMOTIF libraries and templates for building models
    - `templates` contains some water-specific templates
    - `nrel-223p-templates` contains some generic templates for the 223P ontology
    - `223p.ttl` is the vendored 223P ontology (from [open223.info](https://open223.info/223p.ttl)), resolved by OntoEnv and loaded by BuildingMOTIF
- `notebooks/` contains code showing how to build and query models.

## Development Setup

0. (to update 223P, run the `download-s223.sh` script, which fetches the current release from open223.info)
1. Install [`uv`](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) for working with Python
2. Install the dependencies with `uv sync`
3. `uv sync` installs OntoEnv 0.6 or later for both the Python API and CLI. Run it as `uv run ontoenv`; no separate CLI installation is needed. If you need a system-wide CLI, use `cargo install --locked ontoenv-cli`.

## Building the Ontology

Run `make build-ontology` to build the ontology, or `make test` to build and
run the test suite. Neither needs a separate setup step: the OntoEnv
environment in `.ontoenv/` is created on first use, and refreshed
(incrementally) before each compile.

One compile emits both published documents:

- `build/watr.ttl` — the unversioned "latest" copy
- `build/watr-0.2.ttl` — the immutable versioned snapshot

Which modules get merged is driven by the `owl:imports` closure of
`ontology/watr.ttl`, not by the directory listing — a module is included because
something imports it. External dependencies (223P, QUDT, SHACL) are not
followed; they stay as `owl:imports` on the published ontology rather than being
copied in, so consumers resolve them at whatever version they already have.
Loading the published document therefore requires an import resolver (OntoEnv,
or BuildingMOTIF with 223P loaded alongside).

Publishing means copying these to the site repo behind `watermetadata.org` as
`/ontology/watr` and `/ontology/0.2/watr`. Note that GitHub Pages serves an
extensionless file as `application/octet-stream`, so consumers may need to be
told the format explicitly (`Graph().parse(url, format="turtle")`).

## BMotif Libraries and Template Documentation

`libraries` contains a few libraries that can be used to build up the treatment train models

Start with [Creating a Model](docs/tutorials/creating-models.md) and the
[treatment function](docs/explanation/equipment_function.md) explanation.
[BuildingMOTIF templates](docs/libraries/index.rst) provide reusable graph fragments.

To document the templates, run `make local-docs` and open `docs/_build/html/index.html` in a browser. This should also auto-build when you push to the repository, making the docs available at https://datadrivencps.github.io/water-ontology/
