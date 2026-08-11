.PHONY: install-jupyter-venv local-docs llms-txt clean build-ontology

DOC_SOURCES := $(shell find docs -path 'docs/_build' -prune -o \( -name '*.md' -o -name '*.rst' -o -name '*.ipynb' \) -print)

libraries/water.ttl:
	uv run scripts/compile-water-ontology.py

install-jupyter-venv:
	uv add ipykernel
	uv run ipython kernel install --user --name=nawi-water-ontology

local-docs:
	uv run jupyter-book build docs
	uv run jupyter-book build docs
	uv run python scripts/build_llms_txt.py

llms-txt: docs/_build/html/llms.txt

docs/_build/html/llms.txt: docs/_config.yml docs/_toc.yml scripts/build_llms_txt.py $(DOC_SOURCES)
	uv run python scripts/build_llms_txt.py

test: libraries/water.ttl
	uv run pytest tests

clean:
	rm -rf .ontoenv
	uv run jupyter-book clean docs
	rm -f libraries/water.ttl
