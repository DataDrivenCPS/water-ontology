.PHONY: install-jupyter-venv

water.ttl:
	uv run python src/water_ontology/build.py

install-jupyter-venv:
	uv add ipykernel
	uv run ipython kernel install --user --name=nawi-water-ontology

local-docs:
	uv run jupyter-book build docs
	uv run jupyter-book build docs

clean:
	uv run jupyter-book clean docs
	rm water.ttl
