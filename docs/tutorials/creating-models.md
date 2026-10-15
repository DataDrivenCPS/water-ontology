# Creating a Model

This walkthrough builds a gravity thickener, resolves the ontology imports,
infers its treatment function, and validates its physical ports. Run the shell
commands and Python examples from the repository root.

## Prepare the ontology

```sh
uv sync
make build-ontology
```

The build refreshes the source index in `.ontoenv/` and emits both published
ontology documents. Import resolution provides S223 and QUDT definitions during
validation; parsing the water Turtle files alone does not resolve their imports.

## Describe the equipment and its ports

```python
from rdflib import Graph, Namespace

WATR = Namespace("https://watermetadata.org/ontology/watr#")
EX = Namespace("urn:example/first-model#")
model = Graph().parse(data="""
@prefix : <urn:example/first-model#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:thickener a watr:GravityThickener ;
    rdfs:label "Gravity thickener" ;
    s223:hasConnectionPoint :supernatant, :sludge .
:supernatant a s223:OutletConnectionPoint ;
    rdfs:label "Supernatant outlet" ;
    s223:isConnectionPointOf :thickener ;
    s223:hasMedium s223:Fluid-Water .
:sludge a s223:OutletConnectionPoint ;
    rdfs:label "Sludge outlet" ;
    s223:isConnectionPointOf :thickener ;
    s223:hasMedium watr:Fluid-Sludge .
""", format="turtle")
```

The thickener class supplies settling and thickening intent. The model supplies
the distinct liquid and sludge outlets. Their labels help users identify the
modeled entities. A complete plant model can connect these ports to pipes and
other equipment; unconnected boundary ports may produce information-level findings.

## Resolve imports, infer, and validate

```python
from ontoenv import OntoEnv
import shifty

ontology = Graph().parse("build/watr.ttl", format="turtle")
with OntoEnv.connect(".", read_only=True) as env:
    shapes, _imports = env.get_dependencies(ontology, fetch_missing=False)
shapes += ontology

inferred = shifty.infer(model, shapes_graph=shapes).graph()
assert (EX.thickener, WATR.hasProcess, WATR["Process-Settling"]) in inferred
assert (EX.thickener, WATR.hasTreatmentObjective,
        WATR["TreatmentObjective-Thickening"]) in inferred

valid, report, text = shifty.validate(
    inferred, shacl_graph=shapes, minimum_severity="violation"
)
assert valid, text
print(text)
```

`shifty.validate` also runs inference by default. Calling `infer` separately
makes the resulting statements available for subsequent queries. With
`infer=False`, class-required processes and objectives must already be present.
Physical ports are always supplied by the model. Repository examples must be
free of warnings and violations; applications can choose their failure severity.

## Query the result

Include the ontology when following process, objective, or equipment hierarchies:

```python
query_graph = inferred + shapes
rows = list(query_graph.query("""
PREFIX watr: <https://watermetadata.org/ontology/watr#>
SELECT ?process ?objective WHERE {
  <urn:example/first-model#thickener> watr:hasProcess ?process ;
                                      watr:hasTreatmentObjective ?objective .
}
"""))
assert rows
for row in rows:
    print(row.process, row.objective)
```

Local instances of process and objective types also participate in inference
and validation. The [query guide](../guides/querying_treatment_function.md)
shows the optional `rdf:type` path needed to query them and how to resolve
explicit constituent targets before inherited targets.

See [treatment function](../explanation/equipment_function.md) for roles and
additional processes, [system processes](../explanation/system_processes.md) for
compound-process coverage, and [composition](../explanation/processes.md#media-and-constituents)
for complete and partial medium descriptions.
