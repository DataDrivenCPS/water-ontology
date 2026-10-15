# Treatment mechanisms, objectives, and operating roles

**Status:** implemented for PR #39 release preparation, including merged PR #46.
The [review disposition](treatment_review.md) records Fletcher's comments and
supporting treatment references.

## What the ontology and modeler supply

### Modeling

| Question | Model relation | Meaning |
| --- | --- | --- |
| What equipment is present? | `rdf:type` | Equipment design and its intrinsic requirements. |
| What mechanism does it perform? | `watr:hasProcess` | Physical, chemical, or biological activity. |
| What is the intended result? | `watr:hasTreatmentObjective` | Constituent control, product state, cleaning, or recovery intent. |
| How is it used in this plant? | `s223:hasRole` | Explicit installation or operating context. |

Use `watr:hasTreatmentObjective` and `watr:hasProcess` on equipment or systems to
state their objectives and processes. `watr:achievesTreatmentObjective` belongs
in process definitions: it ties a process type to an objective that applies
wherever the process is performed. Do not use it on individual equipment.

### Rationale

An equipment class supplies required processes and a design objective only when
every unit of that class has that function. The modeler states plant intent and
any processes beyond the defaults. A more specific process satisfies a general
requirement: reverse osmosis satisfies filtration, and one value can satisfy
both slots. Additional processes are allowed with no plausibility check.

Inference never derives a mechanism from an objective. Neither relation
certifies measured treatment efficiency or permit compliance.

### Validation

Two SHACL-AF rules in `class-defaults.ttl` run before the constraints:

- `ClassDefaultsRule` copies the processes and objective a class requires onto
  each instance of it.
- `ProcessObjectiveRule` adds the objectives intrinsic to each performed process,
  including those inherited from parent processes.

Both work for named vocabulary terms and for locally typed process or objective
instances. Roles are never inferred. Because the rules run first, a class's
process and objective requirements cannot fail for an instance that only
declares its type.

Shapes in `watr.ttl` check the relations themselves:

| Shape | Requires |
| --- | --- |
| bearer guard | `hasProcess` and `hasTreatmentObjective` appear only on `s223:Equipment` or `s223:System`. |
| `ProcessValueShape` | Every `hasProcess` value is a `watr:Process`. |
| `TreatmentObjectiveValueShape` | Every `hasTreatmentObjective` value is a `watr:TreatmentObjective`. |
| `TreatmentObjectiveRequiresProcessShape` | Equipment with an objective also states at least one `hasProcess`. |

## Filtration and membrane processes

### Definitions

| Process | Parents |
| --- | --- |
| `Process-Filtration` | `Process-Separation` |
| `Process-MembraneProcess` | `Process-Separation` |
| Media filtration | `Process-Filtration`, `Process-SolidLiquidSeparation` |
| Microfiltration, ultrafiltration | `Process-MembraneProcess`, `Process-Filtration`, `Process-SolidLiquidSeparation` |
| Reverse osmosis | `Process-MembraneProcess`, `Process-Filtration` (not solid-liquid separation) |
| Membrane distillation, electrodialysis | `Process-MembraneProcess` only |

A `Filter` requires at least one `Process-Filtration`.

### Rationale

EPA's [Membrane Filtration Guidance Manual, Chapter 2](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=901V0500.TXT)
includes MF, UF and RO in membrane filtration and distinguishes electrodialysis
from filtration. DOE's [solar-desalination projects](https://www.energy.gov/cmei/systems/solar-desalination)
describe thermally driven membrane distillation. These mechanisms support the
classification; the hierarchy itself is an ontology design choice.

### Validation

Membrane use alone does not satisfy a filter's filtration requirement, since
membrane distillation and electrodialysis have no filtration parent. Reverse
osmosis does not satisfy a suspended-solids (solid-liquid) separation
requirement. Existing term URIs are retained, but queries that previously found
membrane distillation through the filtration hierarchy now need
`Process-MembraneProcess` to find every membrane separation.

See the {download}`membrane-process example <../../examples/membrane-process-classification.ttl>`.

## Solids-removal terminology

### Definitions

- `TreatmentObjective-SuspendedSolidsRemoval` covers suspended solids, including
  settleable solids. Clarification and turbidity removal are its children.
- `TreatmentObjective-DissolvedSolidsRemoval` is a separate child of
  `TreatmentObjective-ConstituentRemoval`, with desalination, softening and other
  dissolved-constituent objectives beneath it.
- `TreatmentObjective-SolidsRemoval` is deprecated with
  `dcterms:isReplacedBy TreatmentObjective-SuspendedSolidsRemoval`.

### Rationale

The published `SolidsRemoval` URI was ambiguous between suspended and dissolved
solids. It keeps its original suspended-solids meaning and subclasses the
replacement, so existing models remain compatible. Use the explicit replacement
in new models.

### Validation

No shape applies; this is vocabulary. See the
{download}`suspended and dissolved solids example <../../examples/solids-removal-objectives.ttl>`.

## Settling, clarification, and thickening

`Process-Settling` names separation under gravity. `Process-Sedimentation` remains
as a deprecated published URI with `dcterms:isReplacedBy Process-Settling`.
Sedimentation remains an alternate label familiar to practitioners.

### Requirements

| Class | Subclass of | Process | Objective | Outlet connection points |
|---|---|---|---|---|
| `SedimentationTank` | `SeparationTank` | at least one `Process-Settling` | none | at least two |
| `Clarifier` | `SedimentationTank` | inherited | at least one `TreatmentObjective-Clarification` | at least one water outlet and at least one sludge outlet |
| `GravityThickener` | `Thickener` | at least one `Process-Settling` | at least one `TreatmentObjective-Thickening` (inherited from `Thickener`) | at least one water outlet and at least one sludge outlet |

### Rationale

A clarifier and a gravity thickener each split their feed into a clarified water
stream and a sludge stream. They differ in which stream they exist for: the
clarifier for the overflow, the thickener for the underflow. A unit missing
either outlet is not doing that job, so both are required. Whether the plant uses
both streams as products is not asserted.

`SedimentationTank` does not carry the outlet requirement. It also covers septic
tanks, which retain solids for periodic pump-out and have no sludge outlet.
`Clarifier` is a specialization of `SedimentationTank`, not an alias, because it
adds the clarification objective.

### Validation

Both classes apply `watr:LiquidSludgeOutletShape`, which makes two independent
checks on `s223:hasConnectionPoint`. Each needs at least one match:

- a water outlet: an `s223:OutletConnectionPoint` whose medium is an `s223:Fluid-Water`;
- a sludge outlet: an `s223:OutletConnectionPoint` whose medium is a `watr:Fluid-Sludge`.

Sludge is an `s223:Mix-Fluid`, not an `s223:Fluid-Water`, so a sludge port never
satisfies the water check. A unit with only sludge outlets fails it.

These are minimum counts. Multiple sludge outlets and intermittent withdrawal
are valid. The shapes do not check solids concentration, clarification
efficiency, or whether both streams flow at once, and connection-point roles
stay optional.

See the {download}`conforming gravity thickener <../../examples/gravity-thickener-outlets.ttl>`
and {download}`nonconforming thickener with two sludge outlets <../../examples/nonconforming/gravity-thickener-without-liquid-outlet.ttl>`.

```ttl
@prefix : <urn:example/treatment-function#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .

:clarifier a watr:Clarifier .
:thickener a watr:GravityThickener .
:settler a watr:SedimentationTank ;
    watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .
```

This fragment shows function metadata; connection points belong in a complete
plant model. Inference supplies settling on all three units, clarification on
the clarifier, thickening on the thickener, and broad constituent removal from
the separation process. It preserves the modeler's thickening objective.

## General removal and specific targets

### Definitions

All separation processes inherit `TreatmentObjective-ConstituentRemoval`, which
records separation from a stream rather than loss from the whole plant. Adsorption,
ion exchange and precipitation also declare it. Generic oxidation, reduction,
dosing, mixing and gas transfer do not.

Named objectives group common targets beneath it: suspended solids, dissolved
solids (desalination, hardness, silica, sulfate, arsenic), metals (lead), organics,
nutrients and chlorine residual. `targetsConstituent` names the constituent.
Explicit targets take precedence over ancestor targets; without one, use the
nearest declaring ancestor on each inheritance branch. The
[constituent query](../guides/querying_treatment_function.md#find-equipment-by-constituent)
implements this rule.

### Rationale

- RO inherits the broad objective without assuming desalination. A plant may
  state PFAS removal or resource recovery, including from concentrate.
- Converting arsenite to arsenate is pretreatment for later removal, not removal
  of total arsenic, so generic oxidation and reduction carry no removal objective.
- Disinfection targets pathogens but sits outside the removal branch, because
  inactivation need not physically separate organisms.
- Ammonia control differs from nitrogen removal: nitrification changes ammonia
  species but leaves nitrogen in the water.
- The broad parent names no target on purpose. A local target-specific objective
  supplies one.

### Validation

| Shape | Requires |
| --- | --- |
| `ConstituentTargetValueShape` | Every `targetsConstituent` value is an `s223:Medium-Constituent`. |
| `ConstituentRemovalTargetShape` (warning) | A plant's constituent-removal objective states a target or inherits one. Vocabulary terms are exempt; `tests/test_constituent_targets.py` checks them instead. |

A plant can extend the target vocabulary without editing WaTr:

```ttl
@prefix : <urn:example/local-objective#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
@prefix s223: <http://data.ashrae.org/standard223#> .

:selenium a s223:Medium-Constituent .
:removeSelenium a watr:TreatmentObjective-ConstituentRemoval ;
    watr:targetsConstituent :selenium .
```

See the [generated process/objective map](../reference/process_objective_map.md)
for the complete hierarchies and intrinsic objective relationships.

## Filtration, thermal treatment, and disinfection

### Definitions

| Mechanism | Intrinsic objective |
| --- | --- |
| Media filtration (sand, granular carbon) | none specific. GAC filtration also performs adsorption. |
| Microfiltration, ultrafiltration | none specific. Both are membrane and solid-liquid processes. |
| Thermal hydrolysis | none. It is both hydrolysis and thermal treatment. |
| Chlorination | disinfection |
| UV disinfection equipment class | disinfection, from its design |
| Generic UV irradiation | none |
| Ozonation, thermal treatment | none; design or plant intent supplies it |
| Sulfite dosing | chlorine residual removal |

### Rationale

The contaminants a filter removes depend on its material and application, so the
mechanism does not supply every target-specific objective. Thermal hydrolysis has
possible benefits but no single universal product objective. Chlorination covers
dosing and contact time designed for disinfection, not just metering; its objective
describes intended treatment, and performance depends on operating conditions.
Generic UV can support photolysis or advanced oxidation, so it has no universal
disinfection objective.

### Validation

No extra shape applies. Equipment classes carry their required processes, and
inference adds the intrinsic objectives from the table.

## Maintenance, tanks, zones, and repurposing

### Requirements

| Class | Requirement |
| --- | --- |
| `Tank` | At least one fluid connection point. A single bidirectional port is enough. A drain or overflow point, if present, must be an outlet carrying a fluid. |
| `Reactor` | An outlet carrying a fluid. Any recirculation or return point must be an outlet carrying a fluid. |
| `SeparationTank` | At least two outlet connection points and a `Process-Separation`. |
| `EquipmentRegion` | Exactly one direct equipment parent through `s223:contains`, at least one process, at least one connection point, no containment cycle, and ultimately contained by equipment that is not a region. |

Cleaning processes (backwashing, air scouring, purging) inherit
`TreatmentObjective-EquipmentCleaning`. Roles are optional.

### Rationale

- Restoring operation is an objective even when the output is not a product
  stream, so cleaning has its own objective. Modelers state cleaning activities
  directly with `watr:hasProcess`, alongside the equipment's other processes.
- A storage tank may have one bidirectional port; flow-through reactors and
  separation tanks need distinct inlets and outlets.
- Aerobic, anoxic and anaerobic roles stay explicit operating contexts, following
  Fletcher's later acceptance of that choice.
- A region is a functional portion of a basin, not a separate installed unit.
  Sensors observe the relevant region or connection point with
  `hasObservationLocation`. See
  [functional regions](equipment_function.md#functional-regions-within-equipment)
  for the containment constraints and a worked example. Recirculation has
  connection-point roles as well as an activity term used in compound process
  definitions.

### Validation

Each requirement above is a SHACL shape on the class and fails as a violation.
The `sh:message` on each names the rule that was broken.

Repurposing is not validated. When the same physical equipment changes use, keep
its instance URI, replace its obsolete equipment type with a suitable current
one, and update its roles, processes and objectives. Retaining the old
specialized type retains its intrinsic defaults. Model versioning and
historical configurations are outside this ontology's scope and must be managed
by another system.

## Systems and queries

### Modeling

Compound processes are asserted on an `s223:System`. `includesProcess` lists the
steps its members should cover. A2O includes nitrification, denitrification,
phosphorus removal and recirculation, and inherits aeration and solid-liquid
separation requirements from activated sludge.

### Rationale

`includesProcess` does not make the compound process a subclass of each step. A
system's objective does not assert that every member independently achieves it.
Inspection does not propagate child processes or objectives onto enclosing
equipment.

### Validation

`SystemProcessCoverageShape` (warning) reports a system that claims a compound
process when neither it, a nested member, nor equipment contained within a member
performs one of the steps. Coverage follows nested system membership and
equipment containment, including regions and their hardware.

Queries for involvement can include both objective bearers and system members:

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX watr: <https://watermetadata.org/ontology/watr#>
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?unit WHERE {
  { ?unit watr:hasTreatmentObjective/rdf:type?/rdfs:subClassOf* watr:TreatmentObjective-NitrogenRemoval }
  UNION
  { ?system watr:hasTreatmentObjective/rdf:type?/rdfs:subClassOf* watr:TreatmentObjective-NitrogenRemoval ;
            s223:hasMember+ ?unit }
}
```

Run inference first and include the ontology in the query dataset. To limit
system-member results to process-performing members, match their processes
against the system process's `includesProcess` requirements. See the
[query guide](../guides/querying_treatment_function.md) for additional patterns
and [system processes](system_processes.md) for examples.

## Flowing media and composition

### Modeling

The flowing medium is water, brine, or sludge. Filter media such as sand,
carbon or resin are treatment materials, not the water pipe's medium. A
specialized medium states its own constituents; composition is not copied
through subclassing.

### Rationale

Shared constituents establish S223 topology compatibility. They do not establish
equivalent composition, equipment suitability, membrane selectivity or mass
balance.

### Validation

| Rule | Requires |
| --- | --- |
| Range | Each constituent percentage lies between 0 and 100. |
| Consistency | A constituent has no conflicting exact values or bounds. |
| Total | Percentages on a common mass or volume basis do not exceed 100%. |
| Complete composition | An explicitly complete composition can reach 100%. Exact values or upper bounds that cannot are rejected. |

Partial compositions are allowed. Complement inference additionally requires
`hasCompleteComposition true`, a common basis and percent units, exactly one
missing value, and no ranges or duplicated constituent declarations.

## Validation, reference generation, and migration

SHACL validation findings have three severity levels. In this repository,
we use them as follows:

| Severity | Meaning | Example |
| --- | --- | --- |
| `sh:Violation` | A required constraint is not satisfied. Correct the model to meet that requirement. | A clarifier is missing its required sludge outlet, or a composition percentage is outside zero to 100. |
| `sh:Warning` | A description is incomplete and needs review. Supply the missing information or check whether the declared treatment description is appropriate. | A system declares a compound process but neither it nor its members perform one of the required steps. |
| `sh:Info` | An advisory finding that may help improve the model. Review it in context; it does not necessarily require a correction. | A connection point has no associated connection, which may be intentional at a model boundary. |

Severity classifies a finding; the validation caller decides which levels cause
validation to fail. This repository requires conforming examples to have no
warnings or violations. Information-level findings are allowed. Nonconforming
examples must produce at least one violation. These checks are implemented in
`tests/test_examples.py` and `tests/test_nonconforming_examples.py`.

Turtle `#` comments are source comments; `rdfs:comment` and `skos:definition` are
queryable RDF properties. Published terms use `rdfs:comment`; the reference
generator accepts either and lists all parents under one term description.

Source modules live in `ontology/`; the build emits `build/watr.ttl` and its
versioned document. Term URIs remain unversioned. Retired published process and
role designations remain present with `owl:deprecated` and replacement links.
Update models to use active treatment-objective and process terms rather than
retired role/result designations.
