"""Published template examples must match sources and use current vocabulary."""

from pathlib import Path
from textwrap import dedent

import pytest
import yaml
from buildingmotif import BuildingMOTIF
from buildingmotif.dataclasses import Library
from rdflib import Graph, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import RDF, RDFS

ROOT = Path(__file__).resolve().parents[1]
WATR = "https://watermetadata.org/ontology/watr#"
S223 = "http://data.ashrae.org/standard223#"
TEMPLATES = {
    name: template
    for path in sorted((ROOT / "libraries/templates").glob("*.yml"))
    for name, template in yaml.safe_load(path.read_text()).items()
}


@pytest.mark.parametrize("name", sorted(TEMPLATES))
def test_template_vocabulary_is_defined(name, ontology_shapes_graph):
    body = Graph().parse(data=TEMPLATES[name]["body"], format="turtle")
    missing = {
        node for triple in body for node in triple
        if isinstance(node, URIRef)
        and str(node).startswith((WATR, S223, "http://qudt.org/"))
        and (node, None, None) not in ontology_shapes_graph
    }
    assert not missing, f"{name} refers to undefined vocabulary: {missing}"
    for process in body.objects(None, URIRef(WATR + "hasProcess")):
        if str(process).startswith(WATR):
            assert URIRef(WATR + "Process") in set(ontology_shapes_graph.objects(
                process, RDF.type / (RDFS.subClassOf * "*")
            )), f"{name} uses a retired objective designation as a process"


@pytest.mark.parametrize("name", sorted(TEMPLATES))
def test_template_reference_matches_yaml_body(name):
    page = ROOT / f"docs/libraries/templates/{name}.rst"
    text = page.read_text().split(".. code-block:: turtle", 1)[1]
    turtle = dedent(text.split("With dependencies", 1)[0]).strip()
    documented = Graph().parse(data=turtle, format="turtle")
    source = Graph().parse(data=TEMPLATES[name]["body"], format="turtle")
    assert isomorphic(source, documented), f"Regenerate the reference for {name}"


def test_templates_can_expand_declared_dependencies():
    BuildingMOTIF("sqlite://")
    library = Library.load(directory=str(ROOT / "libraries/templates"),
                           infer_templates=False, run_shacl_inference=False)
    for template in library.get_templates():
        template.check_dependencies()
        assert len(template.inline_dependencies().body) >= len(template.body)
