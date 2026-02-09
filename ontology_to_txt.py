from rdflib import Graph, Namespace, RDF, RDFS

SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

#list of equipment to skip : 
skip_equip = [
    "ElectromagneticFieldDevice","SolventExtractionSystem", "DMERecoverySystem",
    "StanderdizedFlowCell"
]
skip_parent_suffixes = ["Sensor", "Valve", "Controller", "Electrode"]
def equipment_to_txt (equipment_file):
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

        # check for equipment to skip:
        if cls_name in skip_equip:
            continue

        # definition
        definition = None
        for c in g.objects(cls, RDFS.comment):
            definition = str(c)
            break

        # subclasses (ignore UnitProcess, Equipment, and s223 namespace items)
        sub_equips = []
        has_parent_suffix = False
        
        for parent in g.objects(cls, RDFS.subClassOf):
            parent_uri = str(parent)
            parent_name = local_name(parent_uri)
            # Check if any parent name ends with suffix to skip:
            for suffix in skip_parent_suffixes:
                if parent_name.endswith(suffix):
                    has_parent_suffix = True
                    break
            # Only include watr namespace items, exclude s223 namespace
            if (parent_name != "UnitProcess" and 
                parent_name != "Equipment" and
                not parent_uri.startswith("http://data.ashrae.org/standard223#")):
                sub_equips.append(parent_name)

        # Skip this equipment if it has a Sensor parent
        if has_parent_suffix :
            continue

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
            "SubEquipmentOf": sub_equips if sub_equips else None,
            "UnitProcess": unit_processes if unit_processes else None
        })
    return equipment

def processtypes_to_txt(process_file):
    # Load ontology
    g = Graph()
    g.parse(process_file, format="turtle", publicID="processtypes.ttl")

    # Namespaces
    WATR = Namespace("urn:nawi-water-ontology#")

    def local_name(uri):
        return uri.split("#")[-1]

    processes = []

    for cls in g.subjects(RDF.type, WATR.Class):
        cls_name = local_name(str(cls))

        # definition (using skos:definition)
        definition = None
        for c in g.objects(cls, SKOS.definition):
            definition = str(c)
            break

        # parent processes (ignore ProcessType and Process)
        sub_process_of = []
        for parent in g.objects(cls, RDFS.subClassOf):
            parent_name = local_name(str(parent))
            if parent_name != "ProcessType" and parent_name != "Process":
                sub_process_of.append(parent_name)

        processes.append({
            "id": cls_name,
            "def": definition,
            "subProcessOf": sub_process_of if sub_process_of else None
        })
    return processes

def roles_to_txt(enumerationkinds_file):
    # Load ontology
    g = Graph()
    g.parse(enumerationkinds_file, format="turtle", publicID="enumerationkinds.ttl")

    # Namespaces
    WATR = Namespace("urn:nawi-water-ontology#")
    S223 = Namespace("http://data.ashrae.org/standard223#")

    def local_name(uri):
        return uri.split("#")[-1]

    roles = []

    for cls in g.subjects(RDF.type, WATR.Class):
        cls_name = local_name(str(cls))
        
        # Only process Role-* items
        if not cls_name.startswith("Role-"):
            continue

        # parent roles (ignore EnumerationKind-Role)
        sub_role_of = []
        for parent in g.objects(cls, RDFS.subClassOf):
            parent_name = local_name(str(parent))
            if parent_name != "EnumerationKind-Role":
                sub_role_of.append(parent_name)

        roles.append({
            "id": cls_name,
            "SubRoleOf": sub_role_of if sub_role_of else None
        })
    return roles


def main():
    equipment = equipment_to_txt("water/equipment.ttl")
    print("\n--- Process Types ---\n")
    processes = processtypes_to_txt("water/processtypes.ttl")
    print("\n--- Roles ---\n")
    roles = roles_to_txt("water/enumerationkinds.ttl")


    # Save to text file in compact format
    with open("ontology_output.txt", "w") as f:
        f.write("EQUIPMENTS:\n")
        for eq in equipment:
            parts = [eq['id']]
            if eq.get('def'):
                parts.append(eq['def'])
            if eq.get('SubEquipmentOf'):
                parts.append(f"SubEquip: {', '.join(eq['SubEquipmentOf'])}")
            if eq.get('UnitProcess'):
                parts.append(f"Process: {', '.join(eq['UnitProcess'])}")
            f.write(" | ".join(parts) + "\n")
        
        f.write("\n########################\n")
        f.write("PROCESSES:\n")
        for proc in processes:
            parts = [proc['id']]
            if proc.get('def'):
                parts.append(proc['def'])
            if proc.get('subProcessOf'):
                parts.append(f"SubProcess: {', '.join(proc['subProcessOf'])}")
            f.write(" | ".join(parts) + "\n")
        
        f.write("\n########################\n")
        f.write("ROLES:\n")
        for role in roles:
            parts = [role['id']]
            if role.get('SubRoleOf'):
                parts.append(f"SubRole: {', '.join(role['SubRoleOf'])}")
            f.write(" | ".join(parts) + "\n")

    print("\nOutput saved to ontology_output.txt")

if __name__ == "__main__":
    main()
