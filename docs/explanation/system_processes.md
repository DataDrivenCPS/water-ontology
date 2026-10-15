# Processes Performed by Systems

## Where a process is stated

### Requirements

`watr:hasProcess` and `watr:hasTreatmentObjective` may be asserted on an
`s223:Equipment` or an `s223:System`, and nothing else. State a process at the
level where it is performed. Relate a system's components with `s223:hasMember`:

```ttl
@prefix : <urn:example/> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .

:backwashSystem a s223:System ;
    s223:hasMember :backwashPump, :backwashTank, :backwashValve ;
    watr:hasProcess watr:Process-Backwashing .
```

### Rationale

Some processes are performed by an assembly, not one machine. A backwash pump
pumps, a tank stores water and valves control flow, while the collection performs
backwashing. A treatment train likewise performs a compound process whose steps
occur in several tanks and other equipment.

### Validation

A bearer guard in `watr.ttl` rejects either relation on anything that is not
equipment or a system. `ProcessValueShape` and `TreatmentObjectiveValueShape`
require every value to be a `watr:Process` and a `watr:TreatmentObjective`
respectively, so the two vocabularies cannot be swapped.

## Compound treatment processes

### Modeling

Activated sludge, MLE, A2O, UCT and Bardenpho each comprise several activities.
State the compound process on the system and the activities on its members:

```ttl
:a2oTrain a s223:System ;
    s223:hasMember :anaerobicZone, :anoxicZone,
                   :aerobicZone, :finalClarifier ;
    watr:hasProcess watr:Process-A2O ;
    watr:hasTreatmentObjective watr:TreatmentObjective-NitrogenRemoval,
                    watr:TreatmentObjective-PhosphorusRemoval .

:anaerobicZone a watr:MixingBasin ;
    s223:hasRole watr:Role-Anaerobic ;
    watr:hasProcess watr:Process-Mixing,
                    watr:Process-EnhancedBiologicalPhosphorusRemoval .

:anoxicZone a watr:MixingBasin ;
    s223:hasRole watr:Role-Anoxic ;
    watr:hasProcess watr:Process-Mixing,
                    watr:Process-Denitrification .

:aerobicZone a watr:AerationBasin ;
    s223:hasRole watr:Role-Aerobic ;
    watr:hasProcess watr:Process-Aeration,
                    watr:Process-Nitrification .

:finalClarifier a watr:SedimentationTank ;
    s223:hasRole watr:Role-Secondary ;
    watr:hasProcess watr:Process-Settling,
                    watr:Process-Recirculation ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Clarification .
```

### Rationale

Roles identify the commissioned zones and treatment stage. Processes identify
the activities carried out in those zones.

### Validation

Class-default inference targets `s223:Equipment`, not `s223:System`. State a
system's compound process directly on the system. Process-to-objective inference
supplies the process's intrinsic objectives; state any additional objectives
explicitly. Equipment members still receive class-defined processes and
objectives when inference runs.

## Steps of a compound process

### Definitions

`watr:includesProcess` relates a compound process to the activities that must be
represented in the system:

```ttl
watr:Process-A2O
    watr:includesProcess watr:Process-Nitrification,
                         watr:Process-Denitrification,
                         watr:Process-EnhancedBiologicalPhosphorusRemoval,
                         watr:Process-Recirculation .
```

A step may name a process family. Activated sludge includes
`watr:Process-SolidLiquidSeparation`, which a sedimentation tank, microfiltration
membrane, dissolved-air flotation unit or centrifuge satisfies through a more
specific process.

### Rationale

The relation says A2O includes these steps, not that A2O is a kind of
nitrification, denitrification or recirculation. The process hierarchy describes
kinds of activities; `includesProcess` describes composition.

### Validation

`includesProcess` has no shape of its own. The coverage check below reads it.

## Coverage checking

### Requirements

For every step included by a compound process a system claims, one of these
performs that step or a more specific process:

- the system itself;
- a member, or a member of a nested subsystem;
- equipment contained within those members, including functional regions and
  their hardware.

### Rationale

A basin's region need not be repeated as a direct system member, and its process
need not be copied onto the basin. Unrelated equipment outside the membership and
containment chain cannot cover a step. A compound process includes its steps
rather than subclassing them, which keeps the claimed process from satisfying its
own coverage.

### Validation

`SystemProcessCoverageShape` in `watr.ttl` reports each uncovered step with
severity `sh:Warning`. A system can therefore be modeled before every component
is entered, while the missing steps stay visible for review. Evidence is read
from the system and its members; no process is copied onto enclosing equipment.

The same test as a query, for inspecting a model:

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX watr: <https://watermetadata.org/ontology/watr#>

SELECT ?system ?missingStep WHERE {
  ?system watr:hasProcess ?compound .
  ?compound rdf:type?/rdfs:subClassOf*/watr:includesProcess ?missingStep .

  FILTER NOT EXISTS {
    ?system s223:hasMember*/s223:contains* ?performer .
    ?performer watr:hasProcess ?actualProcess .
    ?actualProcess rdf:type?/rdfs:subClassOf* ?missingStep .
  }
}
```
