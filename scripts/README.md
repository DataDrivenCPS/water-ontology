# scripts

Build and validation utilities for the water ontology.

- `compile-water-ontology.py` — compiles `ontology/*.ttl` into `libraries/water.ttl` (run via `make build-ontology`).
- `build_llms_txt.py` — generates `docs/_build/html/llms.txt` from the Jupyter Book TOC (run via `make local-docs` / `make llms-txt`).
- `check_watr_terms.py` — checks that every `watr:` term used in a directory of TTL files is defined in the ontology (see `CONTRIBUTING.md`).

Ad-hoc exploration and ontology browsing belong in `notebooks/`, not here.
