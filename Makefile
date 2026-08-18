.PHONY: install-jupyter-venv local-docs llms-txt clean build-ontology initialize-environment test

DOC_SOURCES := $(shell find docs -path 'docs/_build' -prune -o \( -name '*.md' -o -name '*.rst' -o -name '*.ipynb' \) -print)

# Two-part version of the published ontology document; must match
# ONTOLOGY_VERSION in scripts/compile-water-ontology.py.
ONTOLOGY_VERSION := 0.2

ONTOLOGY_SOURCES := $(wildcard ontology/*.ttl)

ONTOENV_DIR := .ontoenv

# --- ontology environment -------------------------------------------------

# Built once, then left alone. The environment exists to resolve the external
# dependencies (223P, QUDT, SHACL); the compile and the tests both read ontology/
# straight off disk, so editing a module needs no refresh here. After updating
# s223/, run `uv run ontoenv update` or delete the directory to rebuild it.
$(ONTOENV_DIR):
	uv run ontoenv init ontology s223
	uv run ontoenv config set offline true
	uv run ontoenv config set remote_cache_ttl_secs 31536000
	uv run ontoenv config add excludes 'build/water.ttl'
	uv run ontoenv config add excludes 'build/water-*.ttl'

initialize-environment: $(ONTOENV_DIR)

# --- published ontology ---------------------------------------------------

# One compile emits both published documents: the unversioned "latest" copy and
# the immutable versioned snapshot. It reads ontology/ directly rather than going
# through ontoenv, so it does not depend on the environment.
build-ontology: build/water.ttl build/water-$(ONTOLOGY_VERSION).ttl

build/water.ttl: $(ONTOLOGY_SOURCES) scripts/compile-water-ontology.py
	uv run scripts/compile-water-ontology.py

# Written by the same compile as build/water.ttl, so it only needs its own
# recipe when it has gone missing on its own.
build/water-$(ONTOLOGY_VERSION).ttl: build/water.ttl
	@test -f $@ || uv run scripts/compile-water-ontology.py

# --- everything else ------------------------------------------------------

install-jupyter-venv:
	uv add ipykernel
	uv run ipython kernel install --user --name=nawi-water-ontology

local-docs: | $(ONTOENV_DIR)
	uv run jupyter-book build docs
	uv run jupyter-book build docs
	uv run python scripts/build_llms_txt.py

llms-txt: docs/_build/html/llms.txt

docs/_build/html/llms.txt: docs/_config.yml docs/_toc.yml scripts/build_llms_txt.py $(DOC_SOURCES)
	uv run python scripts/build_llms_txt.py

test: build-ontology | $(ONTOENV_DIR)
	uv run pytest tests

clean:
	rm -rf $(ONTOENV_DIR)
	uv run jupyter-book clean docs
	rm -f build/water.ttl build/water-$(ONTOLOGY_VERSION).ttl
