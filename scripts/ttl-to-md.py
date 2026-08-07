import rdflib
from rdflib.namespace import RDF, RDFS, OWL, SKOS
import os

g = rdflib.Graph()

def get_local_name(g, uri):
    _, _, local_name = g.compute_qname(uri)
    return local_name

def get_md_description(g, title):

    # Equipment and enumeration kinds describe themselves with rdfs:comment;
    # process and outcome types use skos:definition. Accept either, so that one
    # renderer serves all four vocabularies.
    query = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    SELECT ?class ?label ?comment ?superclass
    WHERE {
        ?class rdfs:label ?label .
        { ?class rdfs:comment ?comment }
        UNION
        { ?class skos:definition ?comment
          FILTER NOT EXISTS { ?class rdfs:comment [] } }
        OPTIONAL { ?class rdfs:subClassOf ?superclass . }
        FILTER NOT EXISTS { ?class a owl:Ontology . }
    }
    """

    # Execute the query
    results = g.query(query)

    # Prepare the Markdown content
    md_content = f"# {title} Classes\n\n"

    for row in results:
        class_uri = row['class']
        label = row.label
        comment = row.comment
        superclass = row.superclass

        md_content += f"## {label}\n\n"
        md_content += f"**Description:** {comment}\n\n"
        if superclass:
            md_content += f"**Superclass:** {get_local_name(g,superclass)}\n\n"
    return md_content

# Write the Markdown content to a file
g.parse('../water/equipment.ttl', format="turtle")
with open("../docs/reference/equipment_documentation.md", "w") as f:
    g = rdflib.Graph()
    g.parse('../water/equipment.ttl', format="turtle")
    f.write(get_md_description(g, 'Equipment'))

with open("../docs/reference/processes_documentation.md", "w") as f:
    g = rdflib.Graph()
    g.parse('../water/processtypes.ttl', format="turtle")
    f.write(get_md_description(g, 'Processes'))

with open("../docs/reference/outcomes_documentation.md", "w") as f:
    g = rdflib.Graph()
    g.parse('../water/outcomes.ttl', format="turtle")
    f.write(get_md_description(g, 'Treatment Outcomes'))

with open("../docs/reference/substances_documentation.md", "w") as f:
    g = rdflib.Graph()
    g.parse('../water/enumerationkinds.ttl', format="turtle")
    f.write(get_md_description(g, 'EnumerationKinds'))