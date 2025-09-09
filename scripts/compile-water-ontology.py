import rdflib
from brick_tq_shacl import validate, infer
import pyshacl
import sys
import ontoenv

env = ontoenv.OntoEnv()
compiled, included = env.get_closure("urn:nawi-water-ontology", recursion_depth=1)
print("Included graphs:", included)
compiled.serialize("libraries/water.ttl")
