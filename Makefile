.PHONY: install-jupyter-venv local-docs clean

libraries/water.ttl:
	ontoenv init water libraries
	ontoenv get-closure urn:nawi-water-ontology libraries/water.ttl

install-jupyter-venv:
	uv add ipykernel
	uv run ipython kernel install --user --name=nawi-water-ontology

local-docs:
	uv run jupyter-book build docs
	uv run jupyter-book build docs

clean:
	ontoenv reset
	uv run jupyter-book clean docs
	rm -f libraries/water.ttl
