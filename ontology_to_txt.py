from rdflib import Graph, Namespace, RDF, RDFS

def equipment_to_json (equipment_file):
    # Load ontology
    g = Graph()
    g.parse(equipment_file, format="turtle", publicID="equipment.ttl")


    # Namespaces
    WATR = Namespace("urn:nawi-water-ontology#")
    SH = Namespace("http://www.w3.org/ns/shacl#")

    def local_name(uri):
        return uri.split("#")[-1]

    equipment = []

    for cls in g.subjects(RDF.type, WATR.Class):
        cls_name = local_name(str(cls))

        # definition
        definition = None
        for c in g.objects(cls, RDFS.comment):
            definition = str(c)
            break

        # subclasses (ignore UnitProcess)
        sub_equips = []
        for parent in g.objects(cls, RDFS.subClassOf):
            parent_name = local_name(str(parent))
            if parent_name != "UnitProcess":
                sub_equips.append(parent_name)

        # unit processes (from sh:hasValue where sh:path == watr:hasProcess)
        unit_processes = []
        for prop in g.objects(cls, SH.property):
            for path in g.objects(prop, SH.path):
                if path == WATR.hasProcess:
                    for val in g.objects(prop, SH.hasValue):
                        unit_processes.append(local_name(str(val)))

        equipment.append({
            "id": cls_name,
            "def": definition,
            "subEquip": sub_equips if sub_equips else None,
            "UnitProcess": unit_processes if unit_processes else None
        })

    # Print result
    for e in equipment:
        print(e)
    return equipment

equipment = equipment_to_json("water/equipment.ttl")
