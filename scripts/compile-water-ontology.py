import rdflib
import ontoenv

with ontoenv.OntoEnv.connect(".") as env:
    env.update()
    compiled, included = env.copy_closure(
        "urn:nawi-water-ontology", recursion_depth=1
    )
print("Included graphs:", included)
compiled.bind("watr", rdflib.Namespace("urn:nawi-water-ontology#"))
compiled.serialize("libraries/water.ttl")
