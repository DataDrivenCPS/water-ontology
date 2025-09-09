import logging
import rdflib
from ontoenv import OntoEnv
from brick_tq_shacl import validate


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def test_ontology_validates():
    env = OntoEnv(offline=False, recreate=True)
    env.add("https://open223.info/223p.ttl")
    g = rdflib.Graph().parse("libraries/water.ttl")
    imported = env.import_dependencies(g)
    print(f"Imported {imported}")
    valid, _, report_string = validate(g, min_iterations=5)
    print(report_string)
    assert valid, f"Ontology does not pass SHACL validation:\n{report_string}"

