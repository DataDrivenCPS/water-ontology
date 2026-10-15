# Equipment Type, Treatment Objective, Process, and Role

A treatment model commonly needs to answer four questions about a piece of
equipment:

| question | relation | value |
|---|---|---|
| What is it? | `rdf:type` | an equipment class, such as `watr:SedimentationTank` |
| What is it for? | `watr:hasTreatmentObjective` | a treatment objective, such as `watr:TreatmentObjective-Clarification` |
| What does it do? | `watr:hasProcess` | an activity, such as `watr:Process-Settling` |
| Where does it sit? | `s223:hasRole` | an installation-specific role, such as `watr:Role-Primary` |

The treatment objective and process describe the equipment itself. The role describes how
that equipment is used in a particular treatment system.

```ttl
@prefix : <urn:example/> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .

:primaryClarifier a watr:Clarifier ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Clarification ;
    watr:hasProcess watr:Process-Settling ;
    s223:hasRole watr:Role-Primary .
```

This model says that the equipment is a sedimentation tank, that its treatment
objective is clarification, that it accomplishes that objective by
sedimentation, and that it occupies the primary stage of this treatment system.

## Treatment objective: what the equipment is for

### Definitions

A treatment objective is the intended, meaningful change to the treated stream,
such as clarification, disinfection, desalination, thickening or nitrogen
removal. Values use `watr:hasTreatmentObjective` and come from the
`watr:TreatmentObjective-*` vocabulary.

### Rationale

The physical mechanism does not always determine the objective. Settling can
clarify a water stream or thicken a solids stream:

```ttl
:primaryClarifier a watr:Clarifier ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Clarification ;
    watr:hasProcess watr:Process-Settling ;
    s223:hasRole watr:Role-Primary .

:sludgeThickener a watr:GravityThickener ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Thickening ;
    watr:hasProcess watr:Process-Settling .
```

The process is the same in both units. The objective distinguishes what each is
designed to accomplish. A process specifies a mechanism and an objective its
intended result; neither certifies measured performance or permit compliance.

### Validation

- `TreatmentObjectiveValueShape`: every value is a `watr:TreatmentObjective`.
- `TreatmentObjectiveRequiresProcessShape`: equipment or a system that states an
  objective also states at least one `watr:hasProcess`.
- A bearer guard allows the relation only on equipment and systems.

## Process: what the equipment does

### Definitions

A process is a physical, chemical or biological activity performed by equipment
or by a system, such as sedimentation, chlorination, ultraviolet irradiation,
filtration, aeration or denitrification. Values use `watr:hasProcess` and come
from the `watr:Process-*` vocabulary. The process hierarchy describes kinds of
activities: `watr:Process-ReverseOsmosis` is a kind of membrane process and
filtration process. The objective hierarchy is separate.

### Rationale

Several processes can serve the same objective:

```ttl
:chlorineContactor a watr:ChlorinationUnit ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection ;
    watr:hasProcess watr:Process-Chlorination .

:uvUnit a watr:UltravioletLightUnit ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection ;
    watr:hasProcess watr:Process-UVIrradiation .
```

### Validation

- `ProcessValueShape`: every value is a `watr:Process`.
- A bearer guard allows the relation only on equipment and systems.

## Fixed objectives and the decision rule

### Definitions

When a process has the same objective wherever it is performed, the process type
carries it with `watr:achievesTreatmentObjective`:

```ttl
watr:Process-Chlorination
    watr:achievesTreatmentObjective watr:TreatmentObjective-Disinfection .

watr:Process-Denitrification
    watr:achievesTreatmentObjective watr:TreatmentObjective-NitrogenRemoval .
```

Some processes imply only a broad objective. Settling can clarify or thicken, and
chemical precipitation can soften water or remove phosphorus, metals, sulfate or
silica. Both imply constituent removal; the specific objective comes from
equipment design or plant intent.

### Rationale

Use a process term for the mechanism or operating method, and an objective for the
change the unit is meant to deliver. A process may carry a selectivity qualifier
without a universal objective. Microfiltration, ultrafiltration, nanofiltration
and reverse osmosis specify a membrane method and retention range, not every
target removed at that range.

State a target-specific objective only when design or plant intent supports it: a
polishing filter can state turbidity removal, an RO unit desalination, and a
water reuse unit organics removal. The same restraint applies to ozone and thermal
treatment, whose broad process terms do not infer disinfection. Do not infer
objectives from generic method hierarchies; a method label is not a complete
treatment claim.

### Validation

`ProcessObjectiveRule` uses `achievesTreatmentObjective` to add
`hasTreatmentObjective` to the performing equipment or system. Inference runs
before validation. No rule derives a process from an objective.

## Role: where the equipment sits

### Definitions

A role is the commissioned function or position of an entity in a particular
system. Roles include treatment stages (`watr:Role-Primary`), zone regimes
(`watr:Role-Anoxic`) and connection-point purposes (`watr:Role-Drain`).

### Rationale

Moving a clarifier from the primary to the secondary stage keeps its settling
process and clarification objective. Only its role changes:

```ttl
:primaryClarifier a watr:Clarifier ;
    s223:hasRole watr:Role-Primary .

:secondaryClarifier a watr:Clarifier ;
    s223:hasRole watr:Role-Secondary .
```

Roles describe commissioned use, not instantaneous operating conditions. An
aerobic/anoxic swing zone can carry both roles because it is commissioned to
serve in either regime. Its current dissolved-oxygen concentration is an
observable property, as in
{download}`swing-zone-dissolved-oxygen.ttl <../../examples/swing-zone-dissolved-oxygen.ttl>`.

### Validation

Roles are never inferred. After inference this model has
`watr:Process-Settling` and `watr:TreatmentObjective-Thickening`:

```ttl
:sludgeThickener a watr:GravityThickener .
```

The process comes from `watr:GravityThickener` and the objective from its
`watr:Thickener` ancestor. A stage or function in the plant must be stated:

```ttl
:sludgeThickener a watr:GravityThickener ;
    s223:hasRole watr:Role-Primary .
```

Run inference before querying for class-supplied processes and objectives. A
triplestore loaded from the Turtle source alone does not contain them.

## Class requirements and additional processes

### Requirements

An equipment class states the processes and objectives that define its instances,
and requirements on ancestor classes also apply. A reverse-osmosis membrane is a
filter and must perform reverse osmosis, which is a kind of filtration. Its class
supplies broad constituent removal; the modeler states desalination when that is
the plant intent.

### Rationale

A class carries a specific design objective only when every unit of that class is
built for it. `Clarifier` specializes `SedimentationTank` by adding the
clarification objective. Separation processes imply broad constituent removal, so
RO does not imply desalination, and cleaning processes such as backwashing imply
equipment cleaning rather than product-water removal.

An instance may perform further activities. A filter may be backwashed, and a
reactor may mix, aerate or recirculate. State them with `watr:hasProcess`; no
equipment/process permission list exists.

```ttl
:membrane a watr:ReverseOsmosisMembrane ;
    watr:hasProcess watr:Process-ReverseOsmosis,
                    watr:Process-Cleaning ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Desalination .
```

### Validation

`ClassDefaultsRule` copies the class's required processes and objectives onto
the instance, unless a stated value already satisfies the slot. Named vocabulary
terms and local instances of process or objective types both satisfy a slot.
Additional processes are accepted when their type is valid and the class
requirements still hold. There is no equipment/process plausibility check.

## Repurposing equipment

### Modeling

Keep the instance URI and replace the obsolete equipment type with one that fits
the current use. Update the asserted roles, processes and objectives too. A vessel
converted from chlorination to storage should become a storage-tank type with the
obsolete treatment assertions removed.

### Rationale

Keeping the old specialized type keeps its intrinsic defaults, even after an
explicit process assertion is removed. Model versioning and historical
configurations are outside this ontology's scope and must be managed by another
system.

### Validation

None. Nothing detects a stale type.

## Functional regions within equipment

### Requirements

`watr:EquipmentRegion` is an identifiable functional portion of equipment that
performs a treatment activity, even without a physical partition. It must have:

- exactly one direct parent through `s223:contains`, which must be equipment;
- at least one `watr:hasProcess`;
- at least one `s223:hasConnectionPoint`;
- an acyclic containment ancestry that ends at equipment that is not a region.

Roles are optional. Regions may contain nested regions or component equipment.

### Rationale

One basin can hold an anoxic and an aerobic region, each with its own processes
and optional operating role. Connection points mark flow boundaries and use the
S223 direction and medium constraints; they need not be physical fittings. Use
connections between region ports for flow order, and `s223:mapsTo` to map the
outermost region ports to the parent's ports. Locate a sensor with
`s223:hasObservationLocation` at the region or connection point whose property it
observes. Operating roles stay explicit and are not inferred from readings.

Regions differ from spatial representations: `PhysicalSpace` is location,
`DomainSpace` a service space and an S223 `Zone` a group of domain spaces. An
actual sub-basin can use an existing basin or reactor class when its constraints
fit.

### Validation

Each requirement is a shape on `watr:EquipmentRegion` with its own `sh:message`
(for example "An EquipmentRegion must have exactly one direct parent Equipment
through s223:contains."). Process-to-objective inference applies to each region,
and system coverage checks inspect regions and the hardware inside system
members. Containment does not propagate a child's processes or objectives to its
parent.

See {download}`the single-basin regions example <../../examples/single-basin-regions.ttl>`
for a basin with two functional regions, their component hardware, their internal
flow connection, and sensors observing the regions directly.

## Severities

`sh:Violation` marks invalid data, `sh:Warning` incomplete data and `sh:Info` an
advisory. Applications decide which fail validation. See
[data quality](data_quality.md).
