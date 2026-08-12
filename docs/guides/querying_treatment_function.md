# Querying Treatment Function

WaTr separates treatment objectives, performed activities, and
installation-specific roles. Queries can therefore select equipment by what it
is for, what it does, or where it is used without depending on a particular
equipment class name.

The examples below use these prefixes:

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX watr: <urn:nawi-water-ontology#>
```

The queries assume that the dataset contains both the instance model and the
WaTr ontology, including the process and treatment objective hierarchies.

```{important}
Run SHACL-AF inference before querying class-supplied processes and treatment objectives.
For example, `:membrane a watr:ReverseOsmosisMembrane` receives its reverse
osmosis process and desalination treatment objective from its class definitions during
inference. Roles are installation-specific and are never supplied by this rule.
```

## Find equipment by treatment objective

Use `watr:hasTreatmentObjective` to find equipment intended to achieve a treatment
objective. Following the treatment objective hierarchy includes more specific treatment objectives:

```sparql
SELECT DISTINCT ?unit ?treatment objective WHERE {
  ?unit watr:hasTreatmentObjective ?treatment objective .
  ?treatment objective rdfs:subClassOf* watr:TreatmentObjective-NutrientRemoval .
}
ORDER BY ?unit ?treatment objective
```

For an exact treatment objective such as desalination, the query can be shorter:

```sparql
SELECT DISTINCT ?unit WHERE {
  ?unit watr:hasTreatmentObjective watr:TreatmentObjective-Desalination .
}
ORDER BY ?unit
```

## Find equipment by process

Use `watr:hasProcess` when the activity matters. This query finds equipment
performing any membrane process, including reverse osmosis, microfiltration, and
ultrafiltration:

```sparql
SELECT DISTINCT ?unit ?process WHERE {
  ?unit watr:hasProcess ?process .
  ?process rdfs:subClassOf* watr:Process-MembraneProcess .
}
ORDER BY ?unit ?process
```

The path through `rdfs:subClassOf*` is important. Class-default inference adds
the values required by equipment classes; it does not add every ancestor of a
process value as another `watr:hasProcess` triple.

## Compare treatment objectives for the same process

Sedimentation is used for both clarification and thickening. Querying both axes
shows the intended treatment function of each unit:

```sparql
SELECT DISTINCT ?unit ?treatment objective ?role WHERE {
  ?unit watr:hasProcess watr:Process-Sedimentation ;
        watr:hasTreatmentObjective ?treatment objective .
  OPTIONAL { ?unit s223:hasRole ?role }
}
ORDER BY ?unit ?treatment objective ?role
```

## Find equipment by role

Roles identify where equipment is used in a particular system. This query finds
clarification equipment commissioned for the primary treatment stage:

```sparql
SELECT DISTINCT ?unit WHERE {
  ?unit watr:hasTreatmentObjective ?treatment objective ;
        s223:hasRole watr:Role-Primary .
  ?treatment objective rdfs:subClassOf* watr:TreatmentObjective-Clarification .
}
ORDER BY ?unit
```

Do not substitute equipment type or process for the role. A primary and a
secondary clarifier can have the same type, process, and treatment objective.

## Inspect treatment objectives associated with processes

Some process types declare a treatment objective that follows wherever the process is
performed. This query finds those associations for processes present in the
model:

```sparql
SELECT DISTINCT ?unit ?process ?treatment objective WHERE {
  ?unit watr:hasProcess ?process .
  ?process rdfs:subClassOf*/watr:achievesTreatmentObjective ?treatment objective .
}
ORDER BY ?unit ?process ?treatment objective
```

This query is useful for checking or enriching query results, but it should not
be used to assume that every process has a fixed treatment objective. Processes such as
sedimentation and chemical precipitation intentionally have no
`watr:achievesTreatmentObjective` value.

## Return the three axes together

The following query gives a practical equipment summary. Optional clauses keep
equipment in the results when an installation-specific role is not applicable:

```sparql
SELECT DISTINCT ?unit ?type ?treatment objective ?process ?role WHERE {
  ?unit rdf:type ?type .
  ?type rdfs:subClassOf* s223:Equipment .
  OPTIONAL { ?unit watr:hasTreatmentObjective ?treatment objective }
  OPTIONAL { ?unit watr:hasProcess ?process }
  OPTIONAL { ?unit s223:hasRole ?role }
}
ORDER BY ?unit ?treatment objective ?process ?role
```

Because an instance can have several treatment objectives, processes, or roles, this query
may return several rows for one piece of equipment. Applications that need one
record per unit can group the values after querying or use an aggregate suited
to their triplestore.
