.PHONY: install-jupyter-venv local-docs clean build-ontology initialize-environment

libraries/water.ttl: initialize-environment
	uv run scripts/compile-water-ontology.py

initialize-environment:
	uv run ontoenv init --offline -- water
	uv run ontoenv config set offline true
	uv run ontoenv config set remote_cache_ttl_secs 31536000

install-jupyter-venv:
	uv add ipykernel
	uv run ipython kernel install --user --name=nawi-water-ontology

local-docs:
	uv run jupyter-book build docs
	uv run jupyter-book build docs

test: libraries/water.ttl
	uv run pytest tests

clean:
	rm -rf .ontoenv
	uv run jupyter-book clean docs
	rm -f libraries/water.ttl
