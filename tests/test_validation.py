import logging
from pathlib import Path

import rdflib
from ontoenv import OntoEnv
import shifty


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ROOT = Path(__file__).resolve().parents[1]
WATER_DIR = ROOT / "water"
S223_DIR = ROOT / "s223"

def test_ontology_validates():
    g = rdflib.Graph()
    for path in sorted(WATER_DIR.glob("*.ttl")):
        g.parse(path, format="ttl")
    env = OntoEnv(
        path=ROOT,
        recreate=True,
        search_directories=[str(WATER_DIR), str(S223_DIR)],
        includes=["*.ttl"],
    )
    env.update(all=True)
    imported = env.import_dependencies(g, fetch_missing=True)
    print(f"Imported {imported}")
    valid, _, report_string = shifty.validate(g)
    print(report_string)
    assert valid, f"Ontology does not pass SHACL validation:\n{report_string}"

