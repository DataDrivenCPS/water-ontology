from pathlib import Path
from tempfile import TemporaryDirectory

import rdflib
import ontoenv

ROOT = Path(__file__).resolve().parents[1]

with TemporaryDirectory() as environment_dir:
    env = ontoenv.OntoEnv.create(
        environment_dir,
        search_directories=[str(ROOT / "water"), str(ROOT / "s223")],
        includes=["*.ttl"],
    )
    env.update(force=True)
    compiled, included = env.copy_closure(
        "urn:nawi-water-ontology", recursion_depth=1
    )

print("Included graphs:", included)
compiled.bind("watr", rdflib.Namespace("urn:nawi-water-ontology#"))
compiled.serialize("libraries/water.ttl")
