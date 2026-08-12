# Processes Performed by Systems

Some treatment processes are performed by an assembly rather than by one piece
of equipment. A backwash pump pumps, a tank stores water, and valves control
flow, while the collection of those components performs backwashing. A
treatment train similarly performs a compound process whose steps occur in
several tanks and other pieces of equipment.

Model the collection as an `s223:System`, relate its components with
`s223:hasMember`, and state the collection-level process on the system:

```ttl
@prefix : <urn:example/> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <urn:nawi-water-ontology#> .

:backwashSystem a s223:System ;
    s223:hasMember :backwashPump, :backwashTank, :backwashValve ;
    watr:hasProcess watr:Process-Backwashing .
```

`watr:hasProcess` and `watr:hasTreatmentObjective` can be used on either an
`s223:Equipment` instance or an `s223:System`. The process should be stated at
the level where it is performed.

## Compound treatment processes

Processes such as activated sludge, MLE, A2O, UCT, and Bardenpho comprise
several activities. The compound process is stated on the system, while its
members state the activities they perform:

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
    watr:hasProcess watr:Process-Sedimentation,
                    watr:Process-Recirculation ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Clarification .
```

The roles identify the commissioned zones and treatment stage. The processes
identify the activities carried out in those zones.

## Describing the steps of a compound process

`watr:includesProcess` relates a compound process to the activities that must be
represented in the system:

```ttl
watr:Process-A2O
    watr:includesProcess watr:Process-Nitrification,
                         watr:Process-Denitrification,
                         watr:Process-EnhancedBiologicalPhosphorusRemoval,
                         watr:Process-Recirculation .
```

The relation means that A2O includes these steps. It does not mean that A2O is a
kind of nitrification, denitrification, or recirculation. The process hierarchy
continues to describe kinds of activities; `watr:includesProcess` describes
composition.

A required step may name a process family. For example, activated sludge
includes `watr:Process-SolidLiquidSeparation`. A sedimentation tank,
microfiltration membrane, dissolved-air flotation unit, or centrifuge can
satisfy that step through a more specific process.

## Coverage checking

The system process coverage check examines every step included by a claimed
compound process. A step is covered when the system itself, a member, or a
member of a nested subsystem performs that process or a more specific process.

The following query shows the same coverage test in a form suitable for
inspecting a model:

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX watr: <urn:nawi-water-ontology#>

SELECT ?system ?missingStep WHERE {
  ?system watr:hasProcess ?compound .
  ?compound rdfs:subClassOf*/watr:includesProcess ?missingStep .

  FILTER NOT EXISTS {
    ?system s223:hasMember* ?performer .
    ?performer watr:hasProcess ?actualProcess .
    ?actualProcess rdfs:subClassOf* ?missingStep .
  }
}
```

Coverage findings have severity `sh:Warning`. This allows a system to be
modeled before every component has been entered while still identifying the
missing treatment steps for review.

```{note}
Class-default inference targets `s223:Equipment`, not `s223:System`. State a
system's compound process and treatment objective directly on the system. Equipment members
can still receive class-defined processes and treatment objectives when inference runs.
```
