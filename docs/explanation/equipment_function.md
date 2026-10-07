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

A treatment objective is the intended, meaningful change to the treated stream.
Examples include clarification, disinfection, desalination, thickening, and
nitrogen removal. Treatment-objective values use `watr:hasTreatmentObjective` and come
from the `watr:TreatmentObjective-*` vocabulary.

The treatment objective is not always determined by the physical mechanism. A sedimentation
process can clarify a water stream or thicken a solids stream:

```ttl
:primaryClarifier a watr:Clarifier ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Clarification ;
    watr:hasProcess watr:Process-Settling ;
    s223:hasRole watr:Role-Primary .

:sludgeThickener a watr:GravityThickener ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Thickening ;
    watr:hasProcess watr:Process-Settling .
```

The process is the same in both units. The treatment objective distinguishes what each unit
is designed to accomplish.

## Process: what the equipment does

A process is a physical, chemical, or biological activity performed by a piece
of equipment or by a system. Examples include sedimentation, chlorination,
ultraviolet irradiation, filtration, aeration, and denitrification. Process
values use `watr:hasProcess` and come from the `watr:Process-*` vocabulary.

Several processes can achieve the same treatment objective:

```ttl
:chlorineContactor a watr:ChlorinationUnit ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection ;
    watr:hasProcess watr:Process-Chlorination .

:uvUnit a watr:UltravioletLightUnit ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection ;
    watr:hasProcess watr:Process-UVIrradiation .
```

The process hierarchy describes kinds of activities. For example,
`watr:Process-ReverseOsmosis` is a kind of membrane process and filtration
process. The treatment objective hierarchy separately organizes treatment objectives.

### Processes with a fixed treatment objective

When a process has the same treatment objective wherever it is performed, the process type
is related to that treatment objective with `watr:achievesTreatmentObjective`:

```ttl
watr:Process-Chlorination
    watr:achievesTreatmentObjective watr:TreatmentObjective-Disinfection .

watr:Process-Denitrification
    watr:achievesTreatmentObjective watr:TreatmentObjective-NitrogenRemoval .
```

Some processes imply a broad objective without choosing a specific target.
Settling can clarify or thicken, and chemical precipitation can soften water or
remove phosphorus, metals, sulfate, or silica. Both imply constituent removal;
the specific objective comes from equipment design or plant intent.

`achievesTreatmentObjective` belongs to the process vocabulary. The
`ProcessObjectiveRule` uses it to materialize `hasTreatmentObjective` on the
performing equipment or system. No rule derives a process from an objective.

### Decision rule, including filtration

Use a process term for the mechanism or operating method; use a treatment
objective for the change the unit is intended to deliver. A process may carry a
selectivity qualifier without entailing a universal objective. For example,
microfiltration, ultrafiltration, nanofiltration, and reverse osmosis specify a
membrane method and retention range. They do not, by themselves, assert every
possible target removed at that range.

State a target-specific treatment objective only when the equipment design or
plant intent supports it: a polishing filter can state turbidity removal, an RO
unit can state desalination, and a reuse barrier can additionally state organics
removal. The same restraint applies to ozone and thermal treatment: their broad
process terms do not infer disinfection, because either may serve another
objective. Do not infer these from generic method hierarchies. This keeps the
model useful for practitioner queries without treating a method label as a
complete treatment claim.

## Role: where the equipment sits

A role describes the commissioned function or position of an entity in a
particular system. Roles include treatment stages such as `watr:Role-Primary`,
zone regimes such as `watr:Role-Anoxic`, and connection-point purposes such as
`watr:Role-Drain`.

Moving a clarifier from the primary stage to the secondary stage does not change
its sedimentation process or its clarification treatment objective. It does change its
role:

```ttl
:primaryClarifier a watr:Clarifier ;
    s223:hasRole watr:Role-Primary .

:secondaryClarifier a watr:Clarifier ;
    s223:hasRole watr:Role-Secondary .
```

Roles describe commissioned use, not instantaneous operating conditions. An
aerobic/anoxic swing zone can carry both roles because it is commissioned to
serve in either regime. Its current dissolved-oxygen concentration is modeled
as an observable property, as shown in
[`swing-zone-dissolved-oxygen.ttl`](../../examples/swing-zone-dissolved-oxygen.ttl).

````{important}
The equipment class supplies process and treatment objective values that are fixed by that
class, but it cannot supply an installation-specific role. After SHACL-AF
inference, the following short model has `watr:Process-Settling` and
`watr:TreatmentObjective-Thickening`:

```ttl
:sludgeThickener a watr:GravityThickener .
```

The inferred process comes from `watr:GravityThickener`, and the inferred
treatment objective comes from its `watr:Thickener` ancestor. A role is never inferred by
this rule. If the thickener serves a particular stage or function in the plant,
state that role on the instance:

```ttl
:sludgeThickener a watr:GravityThickener ;
    s223:hasRole watr:Role-Primary .
```

Run inference before querying for class-supplied process and treatment objective values. A
triplestore that only loads the Turtle source will not contain those inferred
triples.
````

## Class requirements and additional processes

Equipment classes state the processes and treatment objectives that define their instances.
Requirements on ancestor classes also apply. A reverse-osmosis membrane, for
example, is a filter and must perform reverse osmosis, which is a kind of
filtration. Its class supplies broad constituent removal; the modeler states desalination when that is the plant intent.

An equipment instance may perform additional activities. A filter may be
cleaned or backwashed, and a reactor may mix, aerate, or recirculate water.
The modeler states these activities explicitly with `watr:hasProcess`; no
equipment/process permission list is required.

```ttl
:membrane a watr:ReverseOsmosisMembrane ;
    watr:hasProcess watr:Process-ReverseOsmosis,
                    watr:Process-Cleaning ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Desalination .
```

WaTr accepts explicitly declared additional processes while checking their
types and preserving class requirements. It does not currently judge whether
an equipment/process combination is plausible.

## Validation rules

WaTr applies the following checks to these statements:

- Every value of `watr:hasProcess` must be a `watr:Process`.
- Every value of `watr:hasTreatmentObjective` must be a `watr:TreatmentObjective`.
- An equipment or system that states a treatment objective must also state a process.
- Only equipment and systems may carry `watr:hasProcess` or
  `watr:hasTreatmentObjective`.
- Inference supplies intrinsic process objectives before validation.

Warnings are intended for practitioner review. They do not make a graph invalid
when validation is configured to fail only on `sh:Violation` results.

## Design requirements, defaults, and operating context

`hasTreatmentObjective` relates a unit or system to its objective.
`achievesTreatmentObjective` relates a process type to an objective that follows
wherever it is performed. Inference uses the second relation to add the first.
A process specifies a treatment mechanism and an objective specifies its intended
result; neither certifies measured performance or permit compliance.

Equipment carries a specific design objective only when every unit of that class
is built for it. Separation processes imply broad constituent removal, while the
plant states the target-specific objective when the class cannot determine it.
RO therefore does not automatically imply desalination. Cleaning processes,
including backwashing, imply equipment cleaning rather than product-water removal.

A modeler can state additional processes beyond defaults. Their values must be
processes, and the class requirements still apply. No equipment/process
plausibility check is performed. A tank may have a single bidirectional fluid port.
Reactors keep inlet and outlet requirements. `Clarifier` specializes
`SedimentationTank` by adding the clarification objective.

Repurposing an unchanged vessel is represented by its current role, processes,
and objectives. A physically rebuilt vessel may require a different equipment
class. Historical conversions are represented by timestamped models. Keeping a
specialized equipment type retains its intrinsic defaults, so use a suitable
generic type if those requirements no longer describe the equipment.

A basin may contain several `watr:EquipmentRegion` instances. Locate a sensor
with `s223:hasObservationLocation` at the specific region or connection point
whose property it observes; aerobic, anoxic, and anaerobic roles describe that
region's operating context and remain explicit. See the functional-region
modeling pattern below.

Turtle `#` comments explain the source and are not RDF triples. `rdfs:comment`
and `skos:definition` are queryable RDF properties; the reference generator
accepts either. Published terms use `rdfs:comment` consistently.

SHACL severities distinguish `sh:Violation` (invalid data), `sh:Warning`
(incomplete data), and `sh:Info` (advisory findings). The examples
and tests inspect those severities explicitly; applications may choose how to
present warnings. See [data quality](data_quality.md).

## Functional regions within equipment

Use `watr:EquipmentRegion` for an identifiable functional portion of equipment
that performs a treatment activity, even if it has no physical partition. For
example, one basin can contain an anoxic region and an aerobic region. Each is
equipment in the WaTr model, with its own processes and optional operating roles.

Every region must have exactly one direct parent through `s223:contains`, and
the parent must be equipment. A region must declare at least one `watr:hasProcess`.
Regions can contain nested regions or component equipment, but containment
ancestry must be acyclic and must ultimately reach equipment that is not itself
an `EquipmentRegion`. Roles and connection points are optional; a conceptual
boundary does not require a physical port.

Sensors can use `s223:hasObservationLocation` to observe a region directly.
Process-to-objective inference applies to each region. Containment does not
propagate a child's processes or objectives to its parent, and operating roles
are stated explicitly rather than inferred from readings.

Equipment regions are distinct from spatial representations: `PhysicalSpace`
describes physical location, `DomainSpace` describes a service space, and an S223
`Zone` groups DomainSpaces for control or functional purposes. An actual
sub-basin can use an existing basin or reactor class when its constraints fit.

See [the single-basin regions example](../../examples/single-basin-regions.ttl)
for equipment regions, component hardware, sensors, and an optional spatial layer.
