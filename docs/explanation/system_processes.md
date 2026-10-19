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

The same shapes apply as on equipment: `ProcessBearerShape` rejects either relation
on anything else, and the value shapes require a `watr:Process` and a
`watr:TreatmentObjective`. See
[equipment function](equipment_function.md#treatment-objective-and-process).

## Compound treatment processes

### Modeling

Activated sludge, AO, MLE, A2O, UCT and the Bardenpho processes each comprise
several activities. State the compound process on the system and the activities
on its members:

```ttl
:a2oTrain a s223:System ;
    s223:hasMember :anaerobicZone, :anoxicZone,
                   :aerobicZone, :finalClarifier, :rasSystem ;
    watr:hasProcess watr:Process-A2O .

:anaerobicZone a watr:MixingBasin ;
    s223:hasRole watr:Role-Anaerobic ;
    watr:hasProcess watr:Process-EnhancedBiologicalPhosphorusRemoval .

:anoxicZone a watr:MixingBasin ;
    s223:hasRole watr:Role-Anoxic ;
    watr:hasProcess watr:Process-Denitrification .

:aerobicZone a watr:AerationBasin ;
    s223:hasRole watr:Role-Aerobic ;
    watr:hasProcess watr:Process-Nitrification .

:finalClarifier a watr:Clarifier ;
    s223:hasRole watr:Role-Secondary .

:rasSystem a s223:System ;
    s223:hasMember :rasPump, :rasValve ;
    watr:hasProcess watr:Process-Recirculation .
```

Inference adds mixing to both mixing basins, aeration to the aerobic zone, and
settling and clarification to the clarifier, from their classes. Recirculation
is performed by the return activated sludge assembly, a nested system, since a
pump alone only pumps.

### Rationale

The compound process belongs to the train because no single zone performs it.
Roles identify the commissioned zones and treatment stage; processes identify the
activities carried out in them. An integrated unit that performs every step in
one vessel, such as a sequencing batch reactor, may carry a compound process
itself.

### Validation

`ProcessObjectiveRule` gives the system the objectives its process implies:
`Process-A2O` brings nitrogen and phosphorus removal, and organics removal through
`Process-ActivatedSludge`. State any other objective explicitly.
The built-in equipment-class defaults do not apply to a system,
but its equipment members still do. Whether the steps are covered is checked
below.

## Steps of a compound process

### Definitions

`watr:includesProcess` relates a compound process type to the steps a system
performing it must cover:

```ttl
watr:Process-ActivatedSludge
    watr:includesProcess watr:Process-Aeration ,
                         watr:Process-SolidLiquidSeparation .

watr:Process-A2O
    rdfs:subClassOf watr:Process-ActivatedSludge ;
    watr:includesProcess watr:Process-Nitrification ,
                         watr:Process-Denitrification ,
                         watr:Process-EnhancedBiologicalPhosphorusRemoval ,
                         watr:Process-Recirculation .
```

Steps are inherited down the process hierarchy, so an A2O system must also cover
aeration and solid-liquid separation. Recirculation is a step of the
configurations that need it: MLE, A2O and the Bardenpho processes, and UCT
through A2O.

A step may name a process family. `Process-SolidLiquidSeparation` is met by
settling in a conventional train, by microfiltration or ultrafiltration in a
membrane bioreactor, by flotation in a DAF unit, or by centrifugation.

### Rationale

The relation says A2O includes these steps, not that A2O is a kind of
nitrification or recirculation. The process hierarchy describes kinds of
activities; `includesProcess` describes composition.

The step names the family, not `Process-Separation` above it, because screening
and stripping are separations too, and neither is the step that parts the biomass
from the treated water. Reverse osmosis is a membrane filtration but not a
solid-liquid separation, so it does not meet that step.

### Validation

`includesProcess` has no shape of its own. The coverage check below reads it.

## Coverage checking

### Requirements

For every step of a compound process a system claims, something within the
system must perform that step or a more specific process: the system itself, a
member, a member of a nested subsystem, or equipment contained within any of
those, including functional regions and their hardware.

### Rationale

A basin's region need not be repeated as a direct system member, and its process
need not be copied onto the basin. Equipment outside the membership and
containment chain cannot cover a step, however close it sits in the plant.
Because a compound process includes its steps rather than subclassing them,
claiming the compound process never covers its own steps.

### Validation

`SystemProcessCoverageShape` in `watr.ttl` reports each uncovered step as a
`sh:Warning`: "{$this} claims a process that includes {?missing}, but neither it,
any member, nor equipment contained within a member performs that process." A
system can therefore be modeled before all its equipment is entered, with the
missing steps visible for review. The shape targets `s223:System` only, so an
integrated unit carrying a compound process is not checked for its steps; that is
why `SequencingBatchReactor` requires settling as well as activated sludge.

In {download}`a2o-train.ttl <../../examples/a2o-train.ttl>`, the zones and the
clarifier cover the biological steps and settling, and two nested recycle
assemblies, each a pump and a valve, cover recirculation. Remove both assemblies
from the train's members and the shape warns that `Process-Recirculation` is not
covered.

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

To find every unit involved in a system's objective, including members that do
not carry it themselves, see the
[query guide](../guides/querying_treatment_function.md#find-units-contributing-to-a-system-objective).
