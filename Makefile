.PHONY: install-jupyter-venv local-docs llms-txt clean build-ontology initialize-environment test

DOC_SOURCES := $(shell find docs -path 'docs/_build' -prune -o \( -name '*.md' -o -name '*.rst' -o -name '*.ipynb' \) -print)

ONTOLOGY_SOURCES := $(wildcard ontology/*.ttl)

ONTOENV_DIR := .ontoenv

# --- ontology environment -------------------------------------------------

# Index source modules and bundled 223P for compilation. External vocabularies
# stay as imports in the published ontology. Pytest uses its own isolated
# offline environment and a pinned QUDT vocabulary subset.
$(ONTOENV_DIR):
	uv run ontoenv init --offline ontology libraries
	uv run ontoenv config set offline true
	uv run ontoenv config set remote_cache_ttl_secs 31536000
	uv run ontoenv config add excludes 'build/*'

initialize-environment: $(ONTOENV_DIR)

# Refresh the environment from the sources. The compile resolves owl:imports
# through OntoEnv, so a module added or re-pointed since the last run has to be
# re-indexed before the closure is correct. `update` is incremental: it only
# re-reads sources whose modification times changed.
.PHONY: update-environment
update-environment: | $(ONTOENV_DIR)
	uv run ontoenv update --quiet

# --- published ontology ---------------------------------------------------

# One compile emits both published documents: the unversioned "latest" copy and
# the immutable versioned snapshot. Which modules it merges is driven by the
# owl:imports closure of ontology/watr.ttl, resolved through OntoEnv -- hence
# the update-environment order-only prerequisite.
build-ontology: build/watr.ttl

build/watr.ttl: $(ONTOLOGY_SOURCES) scripts/compile-water-ontology.py | update-environment
	mkdir -p build
	uv run scripts/compile-water-ontology.py

install-jupyter-venv:
	uv add ipykernel
	uv run ipython kernel install --user --name=nawi-water-ontology

.PHONY: reference-docs
reference-docs:
	uv run python scripts/generate_reference_docs.py
	uv run python scripts/generate-process-objective-map.py
	uv run python scripts/generate_template_docs.py

local-docs: reference-docs | $(ONTOENV_DIR)
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
	rm -rf build/
