import ontoenv
import rdflib

cfg = ontoenv.Config(
    ["water", "s223"],
    strict=False,
    offline=False,
)
env = ontoenv.OntoEnv(cfg, recreate=True)

def main():
    g = rdflib.Graph()
    env.get_closure("urn:nawi-water-ontology", g)
    g.serialize("water.ttl", format="turtle")

if __name__ == "__main__":
    main()
