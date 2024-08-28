# NAWI Water Ontology

## Layout

- `s223/` contains ontology files from the 223P ontology
- `water/` contains our ontology files
- `src/` contains the Python code for building the ontology

## Development Setup

0. (to update 223, run the `download-s223.sh` script; this will only work for those with existing access to that repo)
1. Install [`uv`](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) for working with Python
2. Install the dependencies with `uv sync`

## Building the Ontology

1. Build the ontology with `uv run python src/water_ontology/build.py` . This generates a `water.ttl` in the current directory
