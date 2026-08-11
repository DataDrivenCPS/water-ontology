# Equipment Type, Outcome, Process, and Role

A treatment model commonly needs to answer four questions about a piece of
equipment:

| question | relation | value |
|---|---|---|
| What is it? | `rdf:type` | an equipment class, such as `watr:SedimentationTank` |
| What is it for? | `watr:hasOutcome` | a treatment objective, such as `watr:Outcome-Clarification` |
| What does it do? | `watr:hasProcess` | an activity, such as `watr:Process-Sedimentation` |
| Where does it sit? | `s223:hasRole` | an installation-specific role, such as `watr:Role-Primary` |

The outcome and process describe the equipment itself. The role describes how
that equipment is used in a particular treatment system.

```ttl
@prefix : <urn:example/> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <urn:nawi-water-ontology#> .

:primaryClarifier a watr:SedimentationTank ;
    watr:hasOutcome watr:Outcome-Clarification ;
    watr:hasProcess watr:Process-Sedimentation ;
    s223:hasRole watr:Role-Primary .
```

This model says that the equipment is a sedimentation tank, that its treatment
objective is clarification, that it accomplishes that objective by
sedimentation, and that it occupies the primary stage of this treatment system.

## Outcome: what the equipment is for

An outcome is the treatment objective that the equipment or system is intended
to achieve. Examples include clarification, disinfection, desalination,
thickening, and nitrogen removal. Outcome values use `watr:hasOutcome` and come
from the `watr:Outcome-*` vocabulary.

The outcome is not always determined by the physical mechanism. A sedimentation
process can clarify a water stream or thicken a solids stream:

```ttl
:primaryClarifier a watr:SedimentationTank ;
    watr:hasOutcome watr:Outcome-Clarification ;
    watr:hasProcess watr:Process-Sedimentation ;
    s223:hasRole watr:Role-Primary .

:sludgeThickener a watr:GravityThickener ;
    watr:hasOutcome watr:Outcome-Thickening ;
    watr:hasProcess watr:Process-Sedimentation .
```

The process is the same in both units. The outcome distinguishes what each unit
is designed to accomplish.

## Process: what the equipment does

A process is a physical, chemical, or biological activity performed by a piece
of equipment or by a system. Examples include sedimentation, chlorination,
ultraviolet irradiation, filtration, aeration, and denitrification. Process
values use `watr:hasProcess` and come from the `watr:Process-*` vocabulary.

Several processes can achieve the same outcome:

```ttl
:chlorineContactor a watr:ChlorinationUnit ;
    watr:hasOutcome watr:Outcome-Disinfection ;
    watr:hasProcess watr:Process-Chlorination .

:uvUnit a watr:UltravioletLightUnit ;
    watr:hasOutcome watr:Outcome-Disinfection ;
    watr:hasProcess watr:Process-UVIrradiation .
```

The process hierarchy describes kinds of activities. For example,
`watr:Process-ReverseOsmosis` is a kind of membrane process and filtration
process. The outcome hierarchy separately organizes treatment objectives.

### Processes with a fixed outcome

When a process has the same outcome wherever it is performed, the process type
is related to that outcome with `watr:achievesOutcome`:

```ttl
watr:Process-Chlorination
    watr:achievesOutcome watr:Outcome-Disinfection .

watr:Process-Denitrification
    watr:achievesOutcome watr:Outcome-NitrogenRemoval .
```

Many processes do not have a fixed outcome. Sedimentation can clarify or
thicken, and chemical precipitation can soften water or remove phosphorus,
metals, sulfate, or silica. For these processes, the outcome must be obtained
from the equipment model rather than from the process type.

`watr:achievesOutcome` supports consistency checking and queries. It does not
replace `watr:hasOutcome` on the equipment or system. Validation reports a
warning when equipment or a system states a process with a fixed outcome but
does not state a compatible outcome.

## Role: where the equipment sits

A role describes the commissioned function or position of an entity in a
particular system. Roles include treatment stages such as `watr:Role-Primary`,
zone regimes such as `watr:Role-Anoxic`, and connection-point purposes such as
`watr:Role-Drain`.

Moving a clarifier from the primary stage to the secondary stage does not change
its sedimentation process or its clarification outcome. It does change its
role:

```ttl
:primaryClarifier a watr:SedimentationTank ;
    s223:hasRole watr:Role-Primary .

:secondaryClarifier a watr:SedimentationTank ;
    s223:hasRole watr:Role-Secondary .
```

Roles describe commissioned use, not instantaneous operating conditions. An
aerobic/anoxic swing zone can carry both roles because it is commissioned to
serve in either regime. Its current dissolved-oxygen concentration is modeled
as an observable property, as shown in
[`swing-zone-dissolved-oxygen.ttl`](../../examples/swing-zone-dissolved-oxygen.ttl).

````{important}
The equipment class supplies process and outcome values that are fixed by that
class, but it cannot supply an installation-specific role. After SHACL-AF
inference, the following short model has `watr:Process-Sedimentation` and
`watr:Outcome-Thickening`:

```ttl
:sludgeThickener a watr:GravityThickener .
```

The inferred process comes from `watr:GravityThickener`, and the inferred
outcome comes from its `watr:Thickener` ancestor. A role is never inferred by
this rule. If the thickener serves a particular stage or function in the plant,
state that role on the instance:

```ttl
:sludgeThickener a watr:GravityThickener ;
    s223:hasRole watr:Role-Primary .
```

Run inference before querying for class-supplied process and outcome values. A
triplestore that only loads the Turtle source will not contain those inferred
triples.
````

## Class requirements and additional processes

Equipment classes state the processes and outcomes that define their instances.
Requirements on ancestor classes also apply. A reverse-osmosis membrane, for
example, is a filter and must perform reverse osmosis, which is a kind of
filtration. It also has desalination as an outcome.

An equipment instance may perform additional activities. A filter may be
cleaned or backwashed, and a reactor may mix, aerate, or recirculate water.
Equipment families list plausible additional activities with
`watr:mayAlsoPerform`.

```ttl
:membrane a watr:ReverseOsmosisMembrane ;
    watr:hasProcess watr:Process-ReverseOsmosis,
                    watr:Process-Cleaning ;
    watr:hasOutcome watr:Outcome-Desalination .
```

An additional process outside the required or permitted process families
produces a validation warning. The warning identifies an unusual combination
without declaring that combination impossible.

## Validation rules

WaTr applies the following checks to these statements:

- Every value of `watr:hasProcess` must be a `watr:Process`.
- Every value of `watr:hasOutcome` must be a `watr:Outcome`.
- An equipment or system that states an outcome must also state a process.
- Only equipment and systems may carry `watr:hasProcess` or
  `watr:hasOutcome`.
- A process with a fixed outcome produces a warning when that outcome is not
  stated.
- An equipment process outside the processes required or permitted by its class
  produces a plausibility warning.

Warnings are intended for practitioner review. They do not make a graph invalid
when validation is configured to fail only on `sh:Violation` results.
