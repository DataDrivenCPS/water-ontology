# Treatment mechanisms, objectives, and operating roles

**Status:** implemented for PR #39 release preparation, including merged PR #46.
The [review disposition](treatment_review.md) records Fletcher's comments and
supporting treatment references.

## What the ontology and modeler supply

| Question | Model relation | Meaning |
| --- | --- | --- |
| What equipment is present? | `rdf:type` | Equipment design and its intrinsic requirements. |
| What mechanism does it perform? | `watr:hasProcess` | Physical, chemical, or biological activity. |
| What is the intended result? | `watr:hasTreatmentObjective` | Constituent control, product state, cleaning, or recovery intent. |
| How is it used in this plant? | `s223:hasRole` | Explicit installation or operating context. |

An equipment class supplies required processes and a specific design objective
only when every unit of that class has that intended function. SHACL-AF inference
materializes those requirements. `ProcessObjectiveRule` then adds objectives
intrinsic to each performed process, including those inherited from its parents.
Roles remain explicit.

The modeler states plant intent and any additional processes beyond defaults.
A more specific process satisfies a general class requirement: reverse osmosis
satisfies filtration, and one value can satisfy both slots. Additional processes
are permitted without an equipment/process plausibility check.

`achievesTreatmentObjective` relates a process type to an intrinsic intended
objective. `hasTreatmentObjective` relates equipment or a system to its objective.
Inference uses the former to add the latter. It never derives a mechanism from
an objective. Neither relation certifies measured treatment efficiency or permit
compliance.

## Settling, clarification, and thickening

`Process-Settling` names separation under gravity. `Process-Sedimentation` remains
as a deprecated published URI with `dcterms:isReplacedBy Process-Settling`.
Sedimentation remains an alternate label familiar to practitioners.

`SedimentationTank` requires settling. `Clarifier` specializes that equipment
class with clarification as a design objective; it is not an alias.
`GravityThickener` requires settling and inherits thickening from `Thickener`.
A clarifier produces overflow and sludge underflow; the sludge may be sent to a
separate thickening process. Production of both streams does not mean the plant
relies on both as finished products.

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

All separation processes inherit `TreatmentObjective-ConstituentRemoval`.
It records separation from a stream, not loss from the entire plant. RO therefore
inherits this broad objective without assuming desalination. A plant may instead
state PFAS removal or resource recovery, including recovery from concentrate.

Adsorption, ion exchange, and precipitation also declare broad constituent
removal. Generic oxidation and reduction do not: converting arsenite to arsenate
is pretreatment that helps later removal, not removal of total arsenic. Dosing,
mixing, and gas transfer likewise do not universally imply removal.

Named objectives group common targets under constituent removal: suspended
solids, dissolved solids, organics, nutrients, and chlorine residual. Dissolved
solids include desalination, hardness, silica, sulfate, and arsenic removal;
metals removal includes lead removal. `targetsConstituent` names the relevant
constituent and can be inherited through an objective's parents.

A plant can extend the target vocabulary without editing WaTr:

```ttl
@prefix : <urn:example/local-objective#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
@prefix s223: <http://data.ashrae.org/standard223#> .

:selenium a s223:Medium-Constituent .
:removeSelenium a watr:TreatmentObjective-ConstituentRemoval ;
    watr:targetsConstituent :selenium .
```

The broad removal parent intentionally names no target. A local target-specific
objective should supply one. Disinfection also targets pathogens but is outside
the removal branch, because inactivation need not physically separate organisms.
Ammonia control is distinct from nitrogen removal: nitrification changes ammonia
species but leaves nitrogen in the water.

See the [generated process/objective map](../reference/process_objective_map.md)
for the complete hierarchies and intrinsic objective relationships.

## Filtration, thermal treatment, and disinfection

Filtration passes a stream through a filter or membrane. Media filtration uses
a bed such as sand or granular carbon; membrane processes use a membrane.
Microfiltration and ultrafiltration are both membrane and solid–liquid processes.
GAC filtration also performs adsorption. The particular contaminants removed
depend on the treatment material and application, so the mechanism does not
supply every possible target-specific objective.

Thermal hydrolysis is both hydrolysis and thermal treatment. Its possible
benefits do not imply one universal product objective.

Chlorination includes dosing and contact time designed for disinfection, rather
than just metering chlorine. Its objective describes intended treatment, with
performance dependent on operating conditions. Generic UV irradiation has no
universal disinfection objective: UV can support photolysis or advanced oxidation.
The UV disinfection equipment class inherits disinfection from its design.
Ozonation and thermal treatment also leave specific objectives to design or plant
intent. Sulfite dosing implies chlorine residual removal.

## Maintenance, tanks, zones, and repurposing

Backwashing, air scouring, and purging are cleaning processes and inherit
`TreatmentObjective-EquipmentCleaning`. Restoring operation is an objective,
even when the output is not a product stream. Modelers state cleaning activities
directly through `watr:hasProcess`, alongside the equipment's other processes.

A storage tank can have a single bidirectional fluid port. Reactors retain inlet
and outlet requirements; separation tanks retain their multiple outlets.

Aerobic, anoxic, and anaerobic roles remain explicit operating contexts, following
Fletcher's later acceptance of that choice. A basin can contain functional
`EquipmentRegion` instances, each with one equipment parent and at least one
process. Sensors observe the relevant equipment region or connection point using
`hasObservationLocation`. See [functional regions](equipment_function.md#functional-regions-within-equipment)
for containment constraints and the worked example. Recirculation has connection-point roles as well as an activity term used
in compound process definitions.

An unchanged repurposed vessel gets its current operating context and a suitable
equipment type; a physically rebuilt vessel may need a different type. Retaining
a specialized type retains its intrinsic defaults. Historical conversions belong
in timestamped models rather than a new conversion-history vocabulary.

## Systems and queries

Compound processes are asserted on an `s223:System`. `includesProcess` lists the
steps that its members should cover; it does not make the compound process a
subclass of each step. A2O includes nitrification, denitrification, phosphorus
removal, and recirculation, and inherits aeration and solid–liquid separation
requirements from activated sludge.

A system's objective does not assert that every member independently achieves
it. Queries for involvement can include both objective bearers and system members:

```sparql
PREFIX watr: <https://watermetadata.org/ontology/watr#>
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?unit WHERE {
  { ?unit watr:hasTreatmentObjective/rdfs:subClassOf* watr:TreatmentObjective-NitrogenRemoval }
  UNION
  { ?system watr:hasTreatmentObjective/rdfs:subClassOf* watr:TreatmentObjective-NitrogenRemoval ;
            s223:hasMember+ ?unit }
}
```

Run inference first and include the ontology in the query dataset. To limit
system-member results to process-performing members, match their processes
against the system process's `includesProcess` requirements. See the
[query guide](../guides/querying_treatment_function.md) for additional patterns
and [system processes](system_processes.md) for examples.

## Flowing media and composition

The flowing medium is water, brine, or aqueous sludge. Filter media such as sand,
carbon, or resin are treatment materials; they are not the water pipe's medium.
Shared constituents establish S223 topology compatibility, not equivalent
composition, equipment suitability, membrane selectivity, or mass balance.

Composition is not copied through subclassing. A specialized medium states its
own constituents. Percentages are checked on a common mass or volume basis;
individual values must lie between zero and 100 and declared intervals must be
consistent. Partial compositions are allowed. Complement inference additionally
requires `hasCompleteComposition true`, a common basis and percent units, exactly
one missing value, and no ranges or duplicated constituent declarations.

## Validation, reference generation, and migration

Violations identify invalid values or unmet structural requirements. Warnings
identify incomplete models, including missing system steps. Information-level findings are advisory. See
[data quality](data_quality.md).

Turtle `#` comments are source comments; `rdfs:comment` and `skos:definition` are
queryable RDF properties. Published terms use `rdfs:comment`; the reference
generator accepts either and lists all parents under one term description.

Source modules live in `ontology/`; the build emits `build/watr.ttl` and its
versioned document. Term URIs remain unversioned. Retired published process and
role designations remain present with `owl:deprecated` and replacement links.
Update models to use active treatment-objective and process terms rather than
retired role/result designations.
