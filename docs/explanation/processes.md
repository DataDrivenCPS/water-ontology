# Modeling Composition, Topology, and Treatment Function

The WaTr ontology supports modeling the **treatment function** of equipment,
the **composition** of the system and its components (for example, "this
reactor contains a lamp"), and the **topology** of the system (for example,
"this pump is connected to this reactor").

To explain these concepts, we will use the following model of a ultraviolet disinfection system:

![](Topology.png)

All of the polygons in this image represent a WaTr entity (a node in the graph) and the edges represent the relationships between them (the edges in the graph).

## Composition

WaTr uses the concept of **composition** to represent how entities are made up of other entities. For example, our UV disinfection system is made up of 2 UV lamps and a plug flow reactor.
We model this using the `s223:contains` relationship between the lamps and the unit process equipment, and the reactor and the unit process equipment.

```ttl
@prefix watr: <urn:nawi-water-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix qudtqk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix : <urn:uv_example/> .

:UVDisinfectionSystem a watr:UnitProcess ;
    s223:contains :myPFR, :myUVLamp1, :myUVLamp2 .

:myPFR a watr:PlugFlowReactor .

:myUVLamp1 a watr:Lamp ;
    s223:hasProperty [
        a s223:QuantifiableObservableProperty ;
        qudt:hasQuantityKind qudtqk:Wavelength ;
        s223:hasValue 250 ;
        s223:hasUnit unit:NanoM ;
    ] .
:myUVLamp2 a watr:Lamp ;
    s223:hasProperty [
        a s223:QuantifiableObservableProperty ;
        qudt:hasQuantityKind qudtqk:Wavelength ;
        s223:hasValue 250 ;
        s223:hasUnit unit:NanoM ;
    ] .
```

To maintain that these are UV lamps, we included the modeling of the wavelength of the light they emit, which is a characteristic of the lamp. This is done using a `QuantifiableObservableProperty` that has a value of 250 nanometers and a unit of measurement.

## Topology

WaTr gets its topological model from the [ASHRAE 223 Standard](https://docs.open223.info/explanation/223_overview.html). This describes how `Connectables` connect to other `Connectables` through `Connections` and `ConnectionPoints`.

There is some nuance to the model to account for real-world complexities, but the basics are:
- `Connectables` are entities that can connect to other entities (e.g. a pump, a reactor, a valve, a unit process)
- `ConnectionPoints` are the "ports" on a `Connectable` that can connect to other `Connectables` (e.g. the inlet and outlet of a reactor). `ConnectionPoints` have a direction (inlet or outlet) and a medium (e.g. water, air, chemical). (See the docs [here](https://explore.open223.info/s223/ConnectionPoint.html)).
    - use the subclasses `InletConnectionPoint`, `OutletConnectionPoint`, `BidirectionalConnectionPoint` to represent the direction of the connection
    - WaTr defines a set of media that can be associated with the `ConnectionPoint`
- `Connections` are the physical things that connect `Connectables` together (e.g. a pipe, a channel, a duct). They have a `ConnectionPoint` on each end, and they convey a medium (e.g. water, air, chemical). (See the docs [here](https://explore.open223.info/s223/Connection.html).

You can see the connections (the `Pipe`s) and connection points in the image at the top of this page. `Equipment` is a subclass of `Connectable`, so it can have `ConnectionPoints` and `Connections`.

```ttl
@prefix watr: <urn:nawi-water-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix qudtqk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix : <urn:uv_example/> .

# defines the "interface" to the unit process
:UVDisinfectionSystem a watr:UnitProcess ;
    s223:cnx :UVInlet, :UVOutlet .
:UVInlet a s223:InletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water .
:UVOutlet a s223:OutletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water .

# PFR participates with the inlet and outlet because
# water flows through it from the inlet to the outlet of
# the unit process
:myPFR a watr:PlugFlowReactor ;
    s223:cnx :PFRInlet, :PFROutlet .
:PFRInlet a s223:InletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water ;
    s223:mapsTo :UVInlet .
:PFROutlet a s223:OutletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water ;
    s223:mapsTo :UVOutlet .
```

We use [`s223:mapsTo`](https://explore.open223.info/s223/mapsTo.html) to relate the connection points of internal equipment to the connection points of the containing equipment. This allows us to model the connections between the unit process and the equipment inside it, for example.

### Media and Constituents

A `ConnectionPoint` or `Connection` carries a *medium*, the substance flowing through it (e.g. water, a chemical, air). S223 decides whether two media are *compatible* (so a connection point and a connection can be joined, or two connection points on the same equipment can carry different streams) by comparing the *constituents* the media are `s223:composedOf`. Two pure media are compatible only if one is a subclass of the other; two mixture media are compatible when they share at least one constituent (either the same one, or one that is a subclass of the other).

WaTr defines several aqueous media as subclasses of `s223:Fluid-Water`: `Water-Seawater`, `Water-Brackish`, `Water-Freshwater`, and `Water-Brine`. To make S223's compatibility rules recognize that these are all, fundamentally, water, each is declared `s223:composedOf` one or more constituents, sharing `s223:Constituent-H2O` with `s223:Fluid-Water` itself:

```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <urn:nawi-water-ontology#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

watr:Water-Seawater
    rdfs:subClassOf s223:Fluid-Water ;
    s223:composedOf [
        a s223:QuantifiableProperty ;
        s223:ofConstituent s223:Constituent-H2O ;
        qudt:hasQuantityKind quantitykind:MassFraction ;
        qudt:hasUnit unit:PERCENT ;
    ] ;
    s223:composedOf [
        a s223:QuantifiableProperty ;
        s223:ofConstituent watr:Salt-NaCl ;
        qudt:hasQuantityKind quantitykind:MassFraction ;
        qudt:hasUnit unit:PERCENT ;
    ] .
```

Because seawater, brackish water, brine, and freshwater all declare `s223:Constituent-H2O`, S223 treats them as mutually compatible: a single piece of equipment can accept a seawater feed and emit freshwater and brine streams without the validator flagging the distinct media as inconsistent. This compatibility claim means only that the media share a compatible constituent; it does not say that their compositions are equivalent or check a material balance. `Water-Freshwater` declares only `Constituent-H2O`, reflecting its negligible salt content in this abstraction, while the saline media additionally declare `watr:Salt-NaCl`.

WaTr follows S223's self-enumerated medium pattern: a reusable medium designation is both a class and an instance of itself, and it is used directly as the value of `s223:hasMedium`. For a reusable salinity such as 15-percent brine, mint a more specific medium class, type it as itself, subclass it from `Water-Brine`, and assert its quantified composition directly. The [`brine-composition.ttl`](../../examples/brine-composition.ttl) example demonstrates this pattern.

Composition is **not inherited** through `rdfs:subClassOf`. A specialized medium does not acquire the `s223:composedOf` statements of `Water-Brine`; it must repeat every constituent needed to describe its own composition. The superclass organizes the medium vocabulary and participates in class compatibility, but it is not an RDF template that copies constituent properties to subclasses or ordinary instances.

## Processes

The complete equipment modeling pattern is described in [Equipment Type,
Treatment Objective, Process, and Role](equipment_function.md). This section introduces the
process portion of that pattern in the context of the UV system.

WaTr differentiates what a treatment unit does from how that unit is put
together. For example, the UV system performs ultraviolet irradiation for the
treatment objective of disinfection, but it is made up of a plug flow reactor and two UV
lamps. Another UV system might use a different kind of reactor or a different
number of lamps, but it would still perform ultraviolet irradiation. Consumers
can query for all units that have disinfection as their treatment objective regardless of
how they are constructed.

The process enacted by a unit process is defined by the `watr:hasProcess` property.

```ttl
@prefix watr: <urn:nawi-water-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix qudtqk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix : <urn:uv_example/> .
:UVDisinfectionSystem a watr:UnitProcess ;
    watr:hasProcess watr:Process-UVIrradiation ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection ;
.
```

WaTr defines a set of process types that can be used to describe the processes enacted by unit processes. These process types are defined in the `watr:Process` class and its subclasses. The process type is a high-level description of what the unit process does, without specifying how it is constructed.

### Abstract and Concrete Process Requirements

Process types form a subclass hierarchy (e.g. `Process-ReverseOsmosis` is a `Process-MembraneProcess`, which is a `Process-Filtration`), and the equipment classes mirror that hierarchy: a `ReverseOsmosisMembrane` is a kind of `Filter`. WaTr expresses the `hasProcess` requirement as a pair of constraints that line up with these two hierarchies. An *abstract* parent says *what kind* of process the equipment performs, and a *concrete* subclass pins down *which one*:

```ttl
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix watr: <urn:nawi-water-ontology#> .

watr:Filter
    sh:property [
        sh:path watr:hasProcess ;
        sh:qualifiedValueShape [ sh:class watr:Process-Filtration ] ;   # any filtration process
        sh:qualifiedMinCount 1 ;
    ] .

watr:ReverseOsmosisMembrane
    sh:property [
        sh:path watr:hasProcess ;
        sh:qualifiedValueShape [ sh:class watr:Process-ReverseOsmosis ] ;   # specifically RO
        sh:qualifiedMinCount 1 ;
    ] .
```

Because `Process-ReverseOsmosis` is an `rdfs:subClassOf` `Process-Filtration`, a single `watr:hasProcess watr:Process-ReverseOsmosis` on an instance satisfies *both* the inherited general requirement and the concrete one, because the specific process counts as the general kind. The parents are effectively abstract: they describe the family of process the equipment performs, and the concrete subclass narrows it to the exact process. The same pattern is used for the digester, disinfection, and separation families (e.g. a `Digester` requires a `Process-Digestion`; an `AnaerobicDigester` requires a `Process-AnaerobicDigestion`).

### Additional processes

Each slot means "performs **at least** this process". Equipment may declare further processes beyond the one its class requires. A moving bed bioreactor aerates, a granular media filter backwashes, an anaerobic digester mixes:

```ttl
:myMBBR a watr:MovingBedBioreactor ;
    watr:hasProcess watr:Process-Biofiltration ,   # satisfies MBBR and, transitively, Filter
                    watr:Process-Aeration .        # additional
```

The required process is still required: an MBBR declaring only aeration does not validate, nor does a `ReverseOsmosisMembrane` declaring only microfiltration.

This is why the constraints are `sh:qualifiedValueShape` with `sh:qualifiedMinCount 1`. A bare `sh:class` applies to *every* value on the path, so it would forbid the additional processes; `sh:maxCount` caps the path and has the same effect. Use `sh:qualifiedMaxCount 1` when a particular process must appear exactly once, and avoid `sh:qualifiedValueShapesDisjoint`, which prevents a value from satisfying both a parent's slot and a child's.

`watr:UnitProcess` is the one class that uses a bare `sh:class`: it requires every value to be a `watr:Process`.

### Plausible additional processes

`watr:mayAlsoPerform` records processes that an equipment class may perform in addition to its required processes. `watr:ProcessPlausibilityShape` warns about any `watr:hasProcess` value outside the union of

- what the equipment's class, or any ancestor, **requires**, and
- what those classes list via **`watr:mayAlsoPerform`**.

Permissions declared on an equipment family apply to its subclasses:

| family | may also perform |
|---|---|---|
| `Tank` | Cleaning |
| `Reactor` | Mixing, Aeration, Recirculation |
| `SeparationTank` | Recirculation |
| `Filter` | Cleaning |
| `Digester` | GasTransfer |

```ttl
watr:Filter
    watr:mayAlsoPerform watr:Process-Cleaning .
```

Plausibility findings have severity `sh:Warning`. A warning does not make the graph invalid at violation-level validation. The property grants permission; it does not assert that an equipment instance performs the process.

### Process vs. Role

A WaTr equipment model separates four claims:

| claim | representation |
|---|---|
| equipment identity | `rdf:type`, such as `a watr:BeltThickener` |
| treatment objective | `watr:hasTreatmentObjective` |
| performed process | `watr:hasProcess` |
| commissioned function in a system | `s223:hasRole` |

An treatment objective is a treatment objective, such as thickening or disinfection. A
process is an activity performed by equipment or by a system, such as
filtration, sedimentation, or backwashing. A role identifies the commissioned
function of an entity within a system, such as a treatment stage, a zone regime,
or the purpose of a connection point.

S223 roles describe commissioned function, not instantaneous operating state — a heating coil keeps `Role-Heating` while it is switched off. `Role-Aerobic`, `Role-Anoxic` and `Role-Anaerobic` say which regime a zone is commissioned to run in, which is what makes the role slots on `AerationBasin` and `MixingBasin` discriminate between the zones of a train: read as bare capability they would be vacuous, since any basin with diffusers *can* be run aerobic. A swing zone commissioned for either regime carries both `Role-Aerobic` and `Role-Anoxic`, and keeps both whatever its blowers are doing.

The dissolved oxygen present at a point in time is a reading, not a role. It belongs on an `s223:QuantifiableObservableProperty` of the medium, which is what a `watr:OxygenMeter` observes:

```ttl
:swing_zone a watr:AerationBasin ;
    s223:hasRole watr:Role-Aerobic, watr:Role-Anoxic ;      # commissioned for either
    watr:hasProcess watr:Process-Aeration, watr:Process-Denitrification ;
    watr:hasTreatmentObjective watr:TreatmentObjective-NitrogenRemoval .

:do_meter a watr:OxygenMeter ;
    s223:hasObservationLocation :swing_zone ;
    s223:observes :dissolved_oxygen .

:dissolved_oxygen a s223:QuantifiableObservableProperty ;    # what it is doing now
    s223:ofMedium s223:Fluid-Water ;
    s223:ofSubstance watr:Constituent-DissolvedOxygen ;
    qudt:hasQuantityKind quantitykind:MassConcentration ;
    qudt:hasUnit unit:MilliGM-PER-L .
```

A reading near zero does not withdraw `Role-Aerobic` from the basin, and a reading of 2 mg/L does not withdraw `Role-Anoxic`. `examples/swing-zone-dissolved-oxygen.ttl` is the whole model, validated with the rest of the examples.

WaTr defines roles in these groups:

| group | roles |
|---|---|
| treatment stage | `Role-Primary`, `Role-Secondary`, `Role-Tertiary`, `Role-Pretreatment`, `Role-Posttreatment` |
| zone regime | `Role-Aerobic`, `Role-Anoxic`, `Role-Anaerobic` |
| operational purpose | `Role-Storage`, `Role-Equalization`, `Role-Detention`, `Role-Retention`, `Role-Containment`, `Role-Extended`, `Role-Stepfeed` |
| connection point | `Role-Drain`, `Role-Overflow`, `Role-Feed`, `Role-Permeate`, `Role-MakeUp` |

`watr:Role-Primary` and `watr:Role-Secondary` refer to wastewater treatment stages. The similarly named S223 roles refer to primary and secondary loops.

### Processes performed by systems

See [Processes Performed by Systems](system_processes.md) for the complete
treatment-train pattern and coverage queries.

Some processes belong to a collection rather than to one member. A backwash pump pumps, a tank stores water, and valves control flow; the backwash system performs backwashing:

```ttl
:BackwashSystem a s223:System ;
    s223:hasMember :myBackwashPump, :myBackwashTank, :myBackwashValve ;
    watr:hasProcess watr:Process-Backwashing .
```

`watr:ProcessBearerShape` enforces the subject boundary: `watr:hasProcess` may be asserted on an `s223:Equipment` or an `s223:System`, and nothing else. `watr:ProcessValueShape` enforces the other end of the relation: every value must be a `watr:Process`. These are shapes rather than `rdfs:domain` and `rdfs:range` axioms on purpose — axioms would infer types onto an invalid model instead of rejecting it.

Treatment-train processes such as MLE, A2O, UCT, and Bardenpho are asserted on the system whose members perform their constituent steps. An integrated unit such as a sequencing batch reactor may carry a compound process itself.

`watr:includesProcess` records what a compound process decomposes into, stated once on the process type rather than repeated in every model:

```ttl
watr:Process-ActivatedSludge
    watr:includesProcess watr:Process-Aeration ,
                         watr:Process-SolidLiquidSeparation .

watr:Process-AO
    watr:includesProcess watr:Process-Nitrification ,
                         watr:Process-Denitrification .
```

`Process-SolidLiquidSeparation` is a process family. Sedimentation satisfies it in a conventional activated-sludge train, microfiltration or ultrafiltration in a membrane bioreactor, flotation in a DAF, centrifugation in a centrifuge. The step names that family rather than `Process-Separation` above it, because screening and stripping are separations too and neither is the step in which a train parts its biomass from the treated water. Recirculation is declared on configurations that require it, including MLE, A2O, UCT, and the Bardenpho processes.

Solid-liquid separation cuts across filtration rather than sitting above or below it. `Process-Filtration` is a `Process-Separation` and `Process-MembraneProcess` is a `Process-Filtration`, but reverse osmosis and membrane distillation retain dissolved species, so filtration as a family is not a solid-liquid separation. The subtypes that part solids from liquid — media filtration, microfiltration, ultrafiltration — declare both parents:

```ttl
watr:Process-Microfiltration
    rdfs:subClassOf watr:Process-MembraneProcess ,
                    watr:Process-SolidLiquidSeparation .

watr:Process-ReverseOsmosis
    rdfs:subClassOf watr:Process-MembraneProcess .
```

`watr:SystemProcessCoverageShape` warns when neither a system nor any transitively nested member performs a required constituent process:

```ttl
:MLESystem a s223:System ;
    s223:hasMember :anoxicZone, :aerationBasin, :secondaryClarifier, :rasPump ;
    watr:hasProcess watr:Process-MLE .

:anoxicZone a watr:MixingBasin ;
    watr:hasProcess watr:Process-Mixing , watr:Process-Denitrification ;
    s223:hasRole watr:Role-Anoxic .
```

Coverage findings have severity `sh:Warning`, allowing partial system models. A compound process uses `watr:includesProcess` for its steps; it is not an `rdfs:subClassOf` those steps.

### Process assertions

| strength | meaning | stated on | expressed by |
|---|---|---|---|
| **required** | an equipment class requires the process | equipment class | `sh:qualifiedValueShape` + `sh:qualifiedMinCount 1` |
| **constituent** | a compound process includes the step | process class | `watr:includesProcess` |
| **plausible** | an equipment family permits an additional process | equipment class | `watr:mayAlsoPerform` |

### Treatment Objective and process

What a piece of equipment is *for* is separate from what it *does*, and the two are separate vocabularies. `watr:TreatmentObjective-*` names objectives; `watr:Process-*` names activities. No term is both.

The separation is needed because neither relation between them is a hierarchy. One process serves several treatment objectives:

```ttl
:primaryClarifier   watr:hasProcess Process-Sedimentation ;
                    watr:hasTreatmentObjective TreatmentObjective-Clarification ;
                    s223:hasRole    watr:Role-Primary .

:gravityThickener   watr:hasProcess Process-Sedimentation ;
                    watr:hasTreatmentObjective TreatmentObjective-Thickening .
```

and one treatment objective is reached by several processes:

```ttl
:chlorinationUnit   watr:hasProcess Process-ChlorineDosing ;
                    watr:hasTreatmentObjective TreatmentObjective-Disinfection .

:uvUnit             watr:hasProcess Process-UVIrradiation ;
                    watr:hasTreatmentObjective TreatmentObjective-Disinfection .
```

A practitioner reads a clarifier the same way: its job is to clarify, and it
does so by settling. Naming the mechanism alone leaves the objective unstated.
Ultraviolet irradiation likewise names the activity, while disinfection names
the treatment objective.

Treatment Objective and process are both intrinsic, so both survive the P&ID test. What moves with position is the role: a primary and a secondary clarifier share their treatment objective and their process and differ only in their stage.

#### Relating a process to its fixed treatment objective

Where a process achieves the same thing wherever it is performed, the process type says so once with `watr:achievesTreatmentObjective`, rather than every machine repeating it:

```ttl
watr:Process-Denitrification  watr:achievesTreatmentObjective watr:TreatmentObjective-NitrogenRemoval .
watr:Process-ChlorineDosing     watr:achievesTreatmentObjective watr:TreatmentObjective-Disinfection .
watr:Process-MLE              watr:achievesTreatmentObjective watr:TreatmentObjective-NitrogenRemoval .
```

Most processes declare no treatment objective: filtration, sedimentation, ozonation, and thermal treatment serve whatever objective the equipment is built for, so the objective is stated on the equipment. Two cases are worth spelling out. `Process-Nitrification` achieves `TreatmentObjective-AmmoniaControl` and *not* `TreatmentObjective-NitrogenRemoval`, which is also why `TreatmentObjective-AmmoniaControl` sits outside `TreatmentObjective-NutrientRemoval`. `Process-ChemicalPrecipitation` declares nothing, because which constituent it targets depends on the reagent. The objectives it may serve are named so the equipment has something to point at — `TreatmentObjective-Softening`, `TreatmentObjective-PhosphorusRemoval`, `TreatmentObjective-MetalsRemoval`, `TreatmentObjective-SulfateRemoval`, `TreatmentObjective-SilicaRemoval` — and all are left unwired to the process.

#### Constraints

- `watr:ProcessValueShape` and `watr:TreatmentObjectiveValueShape` keep the vocabularies apart: an objective asserted with `watr:hasProcess` is rejected, and an activity asserted with `watr:hasTreatmentObjective` likewise.
- `watr:TreatmentObjectiveRequiresProcessShape` rejects equipment that states what it is for without stating what it does.
- `watr:ProcessBearerShape` restricts both predicates to `s223:Equipment` and `s223:System`.

#### Equipment carrying several processes

Two patterns remain, and both keep every value on `watr:hasProcess`. **Refinement** states one activity at two levels: a `ReverseOsmosisMembrane` requires `Process-Filtration` from `watr:Filter` and `Process-ReverseOsmosis` of its own, and a single value satisfies both. **Co-occurrence** is several activities in one vessel, as a `SequencingBatchReactor` aerates and settles in successive phases.

Requirements from ancestors combine conjunctively, as everywhere in SHACL.


## Putting It All Together

All of this information is captured in a single graph (the "WaTr model" of a treatment train). Below is the complete example of the UV disinfection system, including the composition, topology, and process information of this unit process.

```ttl
@prefix watr: <urn:nawi-water-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix qudtqk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix : <urn:uv_example/> .
:UVDisinfectionSystem a watr:UnitProcess ;
    watr:hasProcess watr:Process-UVIrradiation ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection ;
    s223:contains :myPFR, :myUVLamp1, :myUVLamp2 ;
    s223:cnx :UVInlet, :UVOutlet .

:UVInlet a s223:InletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water .
:UVOutlet a s223:OutletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water .

:myPFR a watr:PlugFlowReactor ;
    s223:cnx :PFRInlet, :PFROutlet .
:PFRInlet a s223:InletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water ;
    s223:mapsTo :UVInlet .
:PFROutlet a s223:OutletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water ;
    s223:mapsTo :UVOutlet .

:myUVLamp1 a watr:Lamp ;
    s223:hasProperty [
        a s223:QuantifiableObservableProperty ;
        qudt:hasQuantityKind qudtqk:Wavelength ;
        s223:hasValue 250 ;
        s223:hasUnit unit:NanoM ;
    ] .
:myUVLamp2 a watr:Lamp ;
    s223:hasProperty [
        a s223:QuantifiableObservableProperty ;
        qudt:hasQuantityKind qudtqk:Wavelength ;
        s223:hasValue 250 ;
        s223:hasUnit unit:NanoM ;
    ] .
```
