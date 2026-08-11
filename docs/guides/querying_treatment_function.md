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
WaTr ontology, including the process and outcome hierarchies.

```{important}
Run SHACL-AF inference before querying class-supplied processes and outcomes.
For example, `:membrane a watr:ReverseOsmosisMembrane` receives its reverse
osmosis process and desalination outcome from its class definitions during
inference. Roles are installation-specific and are never supplied by this rule.
```

## Find equipment by outcome

Use `watr:hasOutcome` to find equipment intended to achieve a treatment
objective. Following the outcome hierarchy includes more specific outcomes:

```sparql
SELECT DISTINCT ?unit ?outcome WHERE {
  ?unit watr:hasOutcome ?outcome .
  ?outcome rdfs:subClassOf* watr:Outcome-NutrientRemoval .
}
ORDER BY ?unit ?outcome
```

For an exact outcome such as desalination, the query can be shorter:

```sparql
SELECT DISTINCT ?unit WHERE {
  ?unit watr:hasOutcome watr:Outcome-Desalination .
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

## Compare outcomes for the same process

Sedimentation is used for both clarification and thickening. Querying both axes
shows the intended treatment function of each unit:

```sparql
SELECT DISTINCT ?unit ?outcome ?role WHERE {
  ?unit watr:hasProcess watr:Process-Sedimentation ;
        watr:hasOutcome ?outcome .
  OPTIONAL { ?unit s223:hasRole ?role }
}
ORDER BY ?unit ?outcome ?role
```

## Find equipment by role

Roles identify where equipment is used in a particular system. This query finds
clarification equipment commissioned for the primary treatment stage:

```sparql
SELECT DISTINCT ?unit WHERE {
  ?unit watr:hasOutcome ?outcome ;
        s223:hasRole watr:Role-Primary .
  ?outcome rdfs:subClassOf* watr:Outcome-Clarification .
}
ORDER BY ?unit
```

Do not substitute equipment type or process for the role. A primary and a
secondary clarifier can have the same type, process, and outcome.

## Inspect outcomes associated with processes

Some process types declare an outcome that follows wherever the process is
performed. This query finds those associations for processes present in the
model:

```sparql
SELECT DISTINCT ?unit ?process ?outcome WHERE {
  ?unit watr:hasProcess ?process .
  ?process rdfs:subClassOf*/watr:achievesOutcome ?outcome .
}
ORDER BY ?unit ?process ?outcome
```

This query is useful for checking or enriching query results, but it should not
be used to assume that every process has a fixed outcome. Processes such as
sedimentation and chemical precipitation intentionally have no
`watr:achievesOutcome` value.

## Return the three axes together

The following query gives a practical equipment summary. Optional clauses keep
equipment in the results when an installation-specific role is not applicable:

```sparql
SELECT DISTINCT ?unit ?type ?outcome ?process ?role WHERE {
  ?unit rdf:type ?type .
  ?type rdfs:subClassOf* s223:Equipment .
  OPTIONAL { ?unit watr:hasOutcome ?outcome }
  OPTIONAL { ?unit watr:hasProcess ?process }
  OPTIONAL { ?unit s223:hasRole ?role }
}
ORDER BY ?unit ?outcome ?process ?role
```

Because an instance can have several outcomes, processes, or roles, this query
may return several rows for one piece of equipment. Applications that need one
record per unit can group the values after querying or use an aggregate suited
to their triplestore.
