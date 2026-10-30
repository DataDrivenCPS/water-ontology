# Equipment Type, Treatment Objective, Process, and Role

A treatment model describes a piece of equipment along four lines. Its
`rdf:type` says what it is, such as `watr:Clarifier`.
`watr:hasTreatmentObjective` says what it is for, such as clarification.
`watr:hasProcess` says what it does to get there, such as settling. `s223:hasRole`
says where it sits in this plant, such as the primary stage. The first three
describe the equipment and travel with it; the role describes one installation.

```ttl
@prefix : <urn:example/> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .

:primaryClarifier a watr:Clarifier ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Clarification ;
    watr:hasProcess watr:Process-Settling ;
    s223:hasRole watr:Role-Primary .
```

The fragments on this page show function only. A complete model also needs the
connection points each class requires, such as a clarifier's water and sludge
outlets; see [equipment classes](treatment_model_summary.md).

## Treatment objective and process

### Definitions

A treatment objective is the intended change to the treated stream:
clarification, disinfection, desalination, thickening, nitrogen removal. A process
is the physical, chemical or biological activity that brings it about:
settling, chlorination, ultraviolet irradiation, filtration, denitrification.
Objectives come from the `watr:TreatmentObjective-*` vocabulary and processes from
`watr:Process-*`. No term is in both. Either relation may be stated on equipment
or on an `s223:System`.

A value may be a vocabulary term or a local instance of one, such as
`:myProcess a watr:Process-Denitrification`. Rules and shapes treat them alike.

### Rationale

The two are separate because neither determines the other. Settling clarifies
water in one tank and thickens sludge in another:

```ttl
:primaryClarifier a watr:Clarifier ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Clarification ;
    watr:hasProcess watr:Process-Settling .

:sludgeThickener a watr:GravityThickener ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Thickening ;
    watr:hasProcess watr:Process-Settling .
```

And one objective is reached by several processes:

```ttl
:chlorineContactor a watr:ChlorinationUnit ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection ;
    watr:hasProcess watr:Process-Chlorination .

:uvUnit a watr:UltravioletLightUnit ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection ;
    watr:hasProcess watr:Process-UVIrradiation .
```

A query can then ask for every disinfection unit regardless of how it
disinfects, or every settling tank regardless of what it settles for. Both
relations state design intent. Neither certifies measured performance or permit
compliance.

### Validation

Four shapes in `watr.ttl` check the relations, each as a violation.
`ProcessBearerShape` rejects either relation on anything but equipment or a
system: "A process is performed by a machine or by a collection of them."
`ProcessValueShape` requires every `hasProcess` value to be a `watr:Process`, and
`TreatmentObjectiveValueShape` every `hasTreatmentObjective` value to be a
`watr:TreatmentObjective`, so an objective stated as a process is rejected with
"An objective belongs on watr:hasTreatmentObjective", and the reverse likewise.
`TreatmentObjectiveRequiresProcessShape` requires anything that states an
objective to state a process too, since an objective with no mechanism cannot be
checked. It runs after inference, so a process supplied by the equipment class
counts.

These are shapes rather than `rdfs:domain` and `rdfs:range` axioms on purpose. An
axiom would infer that a `PhysicalSpace` with a process is equipment, instead of
rejecting it.

A local process or objective instance is checked by the `watr:Process` or
`watr:TreatmentObjective` shape, which requires exactly one `rdfs:label` and one
`rdfs:comment`. Give it both:

```ttl
:secondStageDenitrification a watr:Process-Denitrification ;
    rdfs:label "Second-stage denitrification" ;
    rdfs:comment "Post-anoxic denitrification with methanol dosing." .
```

## Objectives implied by a process

### Definitions

When a process has the same objective wherever it is performed, the process type
states it once with `watr:achievesTreatmentObjective`:

```ttl
watr:Process-Denitrification
    watr:achievesTreatmentObjective watr:TreatmentObjective-NitrogenRemoval .

watr:Process-Chlorination
    watr:achievesTreatmentObjective watr:TreatmentObjective-Disinfection .
```

The relation belongs in process definitions. Plant models use
`hasTreatmentObjective` on equipment and systems instead.

### Rationale

Only a fixed objective belongs on a process. Every separation process implies
broad constituent removal, but which constituent depends on the plant, so the
modeler states the specific objective: desalination for an RO unit at one plant,
PFAS removal at another. Settling clarifies or thickens, and chemical
precipitation softens or removes phosphorus, metals, sulfate or silica depending on
the reagent. Generic UV irradiation, ozonation and thermal treatment imply no
objective, because each also serves purposes other than disinfection.
Nitrification implies ammonia control, not nitrogen removal: it changes ammonia
into nitrate and leaves the nitrogen in the water.

### Validation

`ProcessObjectiveRule` in `class-defaults.ttl` is a SHACL-AF rule. It adds
`hasTreatmentObjective` to anything that performs a process, for every objective
the process or one of its ancestors declares. It reaches systems as well as
equipment, so a train performing `Process-A2O` gains nitrogen and phosphorus
removal. Inference runs before validation. No rule works the other way, deriving
a process from an objective.

## Processes and objectives required by a class

### Requirements

An equipment class lists the processes and objectives every instance must have.
Each is a minimum of one value of a given type, and a subclass inherits its
ancestors' requirements:

| Class | Subclass of | Required process | Required objective |
|---|---|---|---|
| `Filter` | `s223:Equipment`, `UnitProcess` | a `Process-Filtration` | none |
| `ReverseOsmosisMembrane` | `Filter` | a `Process-ReverseOsmosis` | none |
| `NanofiltrationUnit` | `Filter` | inherited only | none |
| `MembraneBioreactor` | `Filter`, `Reactor`, `SeparationTank` | exactly one of microfiltration or ultrafiltration, and a `Process-Biofiltration` | none |
| `SedimentationTank` | `SeparationTank` | a `Process-Settling` | none |
| `Clarifier` | `SedimentationTank` | inherited | `TreatmentObjective-Clarification` |
| `Thickener` | `UnitProcess` | any process | `TreatmentObjective-Thickening` |
| `GravityThickener` | `Thickener` | a `Process-Settling` | inherited |
| `DisinfectionUnit` | `Reactor` | any process | `TreatmentObjective-Disinfection` |
| `UltravioletLightUnit` | `DisinfectionUnit` | a `Process-UVIrradiation` | inherited |

`UnitProcess`, an ancestor of most treatment classes, requires at least one
process of any kind. The [equipment reference](../reference/equipment_documentation.md)
lists every class.

### Rationale

A class carries a process or objective only when every unit of that class has it.
An RO membrane always performs reverse osmosis, but desalinates at one plant and
removes PFAS at another, so the objective is left to the modeler. The same
reasoning removed softening from nanofiltration and turbidity removal from media
filtration. A clarifier, by contrast, exists for its clarified overflow wherever
it is installed, so `Clarifier` carries clarification and differs from
`SedimentationTank` by exactly that.

A requirement means "performs at least this". A more specific value meets a
general requirement, so one `Process-ReverseOsmosis` meets both the RO
requirement and the inherited filtration one. Further processes are allowed: a
moving bed bioreactor also aerates, and a membrane is also cleaned:

```ttl
:mbbr a watr:MovingBedBioreactor ;
    watr:hasProcess watr:Process-Biofiltration ,   # required by the class
                    watr:Process-Aeration .        # additional

:membrane a watr:ReverseOsmosisMembrane ;
    watr:hasProcess watr:Process-ReverseOsmosis , watr:Process-Cleaning ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Desalination .
```

There is no list of processes each class may perform, and no warning for unusual
combinations. See [pending features](pending_features.md#equipmentprocess-plausibility-checks).

### Validation

Each requirement is a property shape on the class, reported as a violation with a
message such as "Instances of GravityThickener must have a Settling process."

`ClassDefaultsRule` in `class-defaults.ttl` is a SHACL-AF rule that fills these
requirements in first. For each requirement it copies the required type onto the
instance as a `hasProcess` or `hasTreatmentObjective` value, unless a stated value
already meets it. After inference this model has `Process-Settling` and
`TreatmentObjective-Thickening`, the latter from `Thickener`:

```ttl
:sludgeThickener a watr:GravityThickener .
```

Because the rule runs before the constraints, a requirement for a specific process
or objective type cannot fail for an instance that declares only its type. It
fails only when inference is off (`infer=False`) and the value is not stated. The
`UnitProcess` requirement names no type, so the rule cannot fill it: a bare
`:t a watr:Thickener` fails it, and also fails
`TreatmentObjectiveRequiresProcessShape` once its thickening objective is
inferred. Choose the subclass that names the mechanism, or state the process.
Likewise a `MembraneBioreactor` must state whether it uses microfiltration or
ultrafiltration, since the rule cannot choose between them. The rule targets
`s223:Equipment`, so it does not apply to systems. Run inference before querying
for class-supplied values: a triplestore loaded from the Turtle source alone does
not contain them.

When adding a class, write each requirement as an `sh:qualifiedValueShape` with
`sh:qualifiedMinCount 1`, as the existing classes do. A bare `sh:class` or an
`sh:maxCount` would apply to every value and forbid additional processes, and
`sh:qualifiedValueShapesDisjoint` would stop one value from meeting both a
parent's requirement and a child's. `ClassDefaultsRule` fills in only qualified
requirements that name a single class with `sh:class`.

`ProcessAndRoleConstraintsReferenceDefinedClasses` checks the ontology itself:
every class named in a `hasProcess`, `hasTreatmentObjective` or `hasRole`
requirement must be defined. A requirement left pointing at a renamed class would
otherwise be impossible to satisfy.

## Role

### Definitions

A role is the commissioned function or position of an entity in a particular
system, stated with `s223:hasRole`. WaTr's roles fall into four groups. Treatment
stage roles are `Role-Pretreatment`, `Role-Primary`, `Role-Secondary`,
`Role-Tertiary` and `Role-Posttreatment`. Zone regime roles are `Role-Aerobic`,
`Role-Anoxic` and `Role-Anaerobic`. Operational purpose roles include
`Role-Storage`, `Role-Equalization` and `Role-Detention`. Connection point roles
are `Role-Drain`, `Role-Overflow`, `Role-Feed`, `Role-Permeate` and
`Role-MakeUp`.

`watr:Role-Primary` and `watr:Role-Secondary` are treatment stages; the similarly
named S223 roles are primary and secondary loops. Older roles that named an
objective or an activity, such as `Role-NitrogenRemoval` and `Role-Backwash`, are
deprecated in favor of the matching objective or process.

### Rationale

A role is about position, not design. Moving a clarifier from the primary to the
secondary stage keeps its settling process and clarification objective; only its
role changes:

```ttl
:primaryClarifier a watr:Clarifier ; s223:hasRole watr:Role-Primary .
:secondaryClarifier a watr:Clarifier ; s223:hasRole watr:Role-Secondary .
```

Roles describe commissioned use, not momentary state, as in S223, where a heating
coil keeps `Role-Heating` while it is switched off. A swing zone commissioned to
run either aerobic or anoxic carries both roles, whatever its blowers are doing.
Its dissolved oxygen at a given moment is a reading, which belongs on an
observable property:

```ttl
:swingZone a watr:AerationBasin ;
    s223:hasRole watr:Role-Aerobic , watr:Role-Anoxic ;    # commissioned for either
    watr:hasProcess watr:Process-Aeration , watr:Process-Denitrification .

:doMeter a watr:OxygenMeter ;
    s223:hasObservationLocation :swingZone ;
    s223:observes :dissolvedOxygen .                         # what it is doing now
```

See {download}`swing-zone-dissolved-oxygen.ttl <../../examples/swing-zone-dissolved-oxygen.ttl>`
for the complete model.

### Validation

Roles are never inferred, from the class, the process or any reading. Two classes
require a regime role, because the regime is what tells the zones of a
biological train apart. An `AerationBasin` needs `Role-Aerobic` or `Role-Anoxic`
("Instances of AerationBasin must have the aerobic or anoxic role"), and a
`MixingBasin` needs `Role-Anoxic` or `Role-Anaerobic`. An unaerated swing zone
built with diffusers is still an aeration basin, which is why `Role-Anoxic` is
allowed there. Both are violations, and both allow further roles such as
`Role-Primary`. On
tanks and reactors, connection point roles constrain the port they mark; see
[tanks and reactors](treatment_model_summary.md#tanks-reactors-and-separation-tanks).
Nothing checks a role against readings: a dissolved-oxygen reading near zero does
not withdraw `Role-Aerobic`.

## Repurposing equipment

### Modeling

When the same physical equipment changes use, keep its instance URI and replace
its type with one that fits the new use. Update its roles, processes and
objectives too. A vessel converted from chlorination to storage becomes a storage
tank type, with the chlorination assertions removed.

### Rationale

Keeping the old type keeps its class requirements, so inference would put the
removed process back. Model versioning and historical configurations are outside
this ontology's scope and must be managed by another system.

### Validation

None. Nothing detects a stale type.

## Functional regions within equipment

### Requirements

`watr:EquipmentRegion` is an identifiable functional portion of equipment that
performs a treatment activity, with or without a physical partition. It must have
exactly one direct parent through `s223:contains`, which must be equipment. It
must have at least one `watr:hasProcess` and at least one
`s223:hasConnectionPoint`. Its containment ancestry must have no cycle and must
end at equipment that is not a region. Roles are optional, and a region may
contain nested regions or component equipment.

### Rationale

One basin can hold an anoxic and an aerobic region, each with its own processes
and role. A region's connection points mark flow boundaries rather than physical
fittings. Connections between region ports give the flow order, and
`s223:mapsTo` maps the outermost region ports to the parent's ports. A sensor is
located with `s223:hasObservationLocation` at the region or connection point
whose property it observes.

A region is not a space. `PhysicalSpace` is a location, `DomainSpace` a served
space and an S223 `Zone` a group of domain spaces. A sub-basin that is a
separately installed unit can use an existing basin or reactor class instead.

### Validation

Each requirement is a violation on `watr:EquipmentRegion` with its own message,
such as "An EquipmentRegion must have exactly one direct parent Equipment through
s223:contains." A region does not inherit a tank's connection-point requirements.
Process-to-objective inference applies to each region. Containment does not copy a
region's processes or objectives to its parent, but
[system coverage](system_processes.md#coverage-checking) does look inside members
and their regions.

See {download}`the single-basin regions example <../../examples/single-basin-regions.ttl>`
for a basin with two functional regions, their component hardware, their internal
flow connection, and sensors observing the regions directly.
