# NAWI Water Ontology

## Layout

- `s223/` contains ontology files from the 223P ontology
- `water/` contains our ontology files
- `libraries/` contains libraries and templates for building models
    - `nrel-223p-templates` contains some generic templates for the 223P ontology
    - `templates` contains some water-specific templates
    - `223p.ttl` is a recent copy of the 223P ontology
    - `water.ttl` is the water ontology we are developing in this repository
- `notebooks/` contains code showing how to build and query models.

## Development Setup

0. (to update 223, run the `download-s223.sh` script; this will only work for those with existing access to that repo)
1. Install [`uv`](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) for working with Python
2. Install the dependencies with `uv sync`

## Building the Ontology

Build the ontology with `make libraries/water.ttl`

## BMotif Libraries and Template Documentation

`libraries` contains a few libraries that can be used to build up the treatment train models

See the ModelBuilder notebook for more information on how to use these libraries and templates to build models

To document the templates, run `make local-docs` and open `docs/_build/html/index.html` in a browser. This should also auto-build when you push to the repostitory, making the docs available at https://datadrivencps.github.io/water-ontology/
