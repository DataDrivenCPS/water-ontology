"""Regenerate the Sphinx template reference from the BuildingMOTIF library."""

from io import StringIO
from pathlib import Path

from buildingmotif import BuildingMOTIF
from buildingmotif.dataclasses import Library
from rdflib import Graph, Namespace
from rdflib.tools.rdf2dot import rdf2dot

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/libraries/templates"


def _block(text: str, indentation: int = 4) -> str:
    return "\n".join(" " * indentation + line.expandtabs(4).rstrip() if line.strip() else ""
                     for line in text.splitlines())


class _OrderedGraph(Graph):
    def __iter__(self):
        return iter(sorted(super().__iter__(), key=lambda triple: tuple(map(str, triple))))


def _prepare(graph: Graph) -> Graph:
    for prefix, uri in {
        "P": "urn:___param___#",
        "s223": "http://data.ashrae.org/standard223#",
        "watr": "https://watermetadata.org/ontology/watr#",
        "qudt": "http://qudt.org/schema/qudt/",
        "quantitykind": "http://qudt.org/vocab/quantitykind/",
        "unit": "http://qudt.org/vocab/unit/",
    }.items():
        graph.bind(prefix, Namespace(uri), replace=True)
    return graph


def _graphviz(graph: Graph) -> str:
    stream = StringIO()
    ordered = _prepare(_OrderedGraph())
    ordered += graph
    rdf2dot(ordered, stream)
    return ".. graphviz::\n\n" + _block(stream.getvalue())


def render(template) -> str:
    """Show the actual body, expanded dependencies, and binding parameters."""
    template.check_dependencies()
    expanded = template.inline_dependencies()
    name = str(template.name)
    _prepare(template.body)
    _prepare(expanded.body)
    lines = [name, "=" * max(8, len(name)), "",
             "Generated from ``libraries/templates`` by",
             "``scripts/generate_template_docs.py``. Bind the ``P:`` parameters",
             "before using these graph fragments as a plant model.", "",
             "Template", "--------", "", ".. code-block:: turtle", "",
             _block(template.body.serialize(format="turtle")), "",
             "With dependencies", "-----------------", "", ".. code-block:: turtle", "",
             _block(expanded.body.serialize(format="turtle")), "",
             "Parameters", "----------", ""]
    lines.extend(f"- ``{parameter}``" for parameter in sorted(expanded.parameters))
    lines.extend(["", "Dependencies", "------------", ""])
    dependencies = sorted({str(dep.template.name) for dep in template.get_dependencies()})
    lines.extend([f"- :doc:`{name}`" for name in dependencies] or ["None."])
    lines.extend(["", "Graph", "-----", "", _graphviz(template.body), ""])
    return "\n".join(lines)


def main() -> None:
    BuildingMOTIF("sqlite://")
    library = Library.load(directory=str(ROOT / "libraries/templates"),
                           infer_templates=False, run_shacl_inference=False)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    templates = sorted(library.get_templates(), key=lambda template: str(template.name))
    for template in templates:
        (OUTPUT / f"{template.name}.rst").write_text(render(template))
    (OUTPUT / "index.rst").write_text(
        "Template Reference\n==================\n\n"
        "These pages are generated from the current BuildingMOTIF YAML library.\n"
        "Choose a template from the navigation to inspect its parameters,\n"
        "dependencies, and RDF graph. Run ``uv run python\n"
        "scripts/generate_template_docs.py`` after changing template definitions.\n"
    )
    print(f"Generated {len(templates)} template reference pages.")


if __name__ == "__main__":
    main()
