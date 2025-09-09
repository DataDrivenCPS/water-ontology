.PHONY: install-jupyter-venv local-docs clean build-ontology initialize-environment

libaries/water.ttl: initialize-environment
	uv run scripts/compile-water-ontology.py

initialize-environment:
	uv run python -m ontoenv.init --offline --search-dir water

install-jupyter-venv:
	uv add ipykernel
	uv run ipython kernel install --user --name=nawi-water-ontology

local-docs:
	uv run jupyter-book build docs
	uv run jupyter-book build docs

clean:
	ontoenv reset -f
	uv run jupyter-book clean docs
	rm -f libraries/water.ttl
