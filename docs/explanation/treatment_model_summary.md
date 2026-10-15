# Equipment Classes and Treatment Vocabulary

This page explains specific equipment classes and vocabulary choices: which
connection points each class requires, how the process and objective hierarchies
are arranged, and why. The general pattern of type, objective, process and role is
in [Equipment Type, Treatment Objective, Process, and Role](equipment_function.md).
The [review disposition](treatment_review.md) records the review comments behind
these choices.

## Tanks, reactors, and separation tanks

### Requirements

| Class | Subclass of | Connection points | Process |
|---|---|---|---|
| `Tank` | `s223:Equipment` | at least one carrying a fluid, in any direction; any drain or overflow point must be a fluid outlet | none |
| `Reactor` | `Tank`, `UnitProcess` | at least one fluid inlet and one fluid outlet that is not a drain; any recirculating or return point must be a fluid outlet | any process |
| `SeparationTank` | `Tank`, `UnitProcess` | at least two fluid outlets | a `Process-Separation` |
| `SequencingBatchReactor` | `Reactor`, `SeparationTank` | adds at least one sludge outlet; a bidirectional fill-and-draw port may be added but does not replace the inlet and outlet | `Process-ActivatedSludge` and `Process-Settling` |

A fluid here is any `s223:Mix-Fluid`, which covers water, sludge and air. The
drain and overflow roles are `watr:Role-Drain` and `watr:Role-Overflow`; the
recirculating and return roles are S223's `Role-Recirculating` and `Role-Return`.

### Rationale

`Tank` says nothing about shape. It means a vessel that holds a fluid, and a
storage tank filled and emptied through one bidirectional port is a tank. A
reactor is flow-through, so it needs a distinct way in and out. Its drain does not
count as the outlet, because a drain empties the vessel rather than passing the
treated stream on. A separation tank splits its feed, so it needs at least two
outlets. A sequencing batch reactor settles in the same vessel it treats in, so
its waste sludge leaves from it directly rather than from a downstream
clarifier.

A drain, overflow or recirculation point is optional. When one is modeled, the
role says which way it flows, so a drain marked on an inlet is an error.

### Validation

Each requirement is a violation. The role rules carry their own messages, such
as "A drain connection point on a Tank must be an outlet carrying a fluid." The
reactor's inlet and outlet requirements carry none, so a missing outlet is
reported with SHACL's generic message: "Fewer than 1 values on path
s223:hasConnectionPoint conform to the qualified shape".

See {download}`storage-tank-bidirectional.ttl <../../examples/storage-tank-bidirectional.ttl>`,
{download}`reactor-with-required-cps.ttl <../../examples/reactor-with-required-cps.ttl>`,
{download}`reactor-with-recirculation.ttl <../../examples/reactor-with-recirculation.ttl>`
and the rejected
{download}`reactor-missing-required-outlet.ttl <../../examples/nonconforming/reactor-missing-required-outlet.ttl>`,
a reactor with only an inlet. A functional region inside a basin is not a tank and
has its own rules; see [functional regions](equipment_function.md#functional-regions-within-equipment).

## Settling, clarification, and thickening

### Requirements

| Class | Subclass of | Process | Objective | Outlet connection points |
|---|---|---|---|---|
| `SedimentationTank` | `SeparationTank` | a `Process-Settling` | none | at least two fluid outlets (inherited) |
| `Clarifier` | `SedimentationTank` | inherited | `TreatmentObjective-Clarification` | at least one water outlet and at least one sludge outlet |
| `GravityThickener` | `Thickener` | a `Process-Settling` | `TreatmentObjective-Thickening` (inherited from `Thickener`) | at least one water outlet and at least one sludge outlet |

`Process-Settling` names separation under gravity. `Process-Sedimentation` is a
deprecated published URI with `dcterms:isReplacedBy Process-Settling`.

### Rationale

A clarifier and a gravity thickener each split their feed into a clarified water
stream and a sludge stream. They differ in which stream they exist for: the
clarifier for the overflow, the thickener for the underflow. A unit missing
either outlet is not doing that job, so both are required. Whether the plant uses
both streams as products is not asserted.

`SedimentationTank` does not carry the water and sludge outlet requirement. It
also covers septic tanks, which retain solids for periodic pump-out and have no
sludge outlet. `Clarifier` is a specialization of `SedimentationTank`, not an
alias, because it adds the clarification objective.

### Validation

Both classes apply `watr:LiquidSludgeOutletShape`, which makes two independent
checks on `s223:hasConnectionPoint`, each a violation. One needs an outlet whose
medium is an `s223:Fluid-Water`: "A clarifier or gravity thickener must have a
liquid outlet carrying water." The other needs an outlet whose medium is a
`watr:Fluid-Sludge`: "A clarifier or gravity thickener must have a separate sludge
outlet." Sludge is an `s223:Mix-Fluid`, not an `s223:Fluid-Water`, so a sludge
port never satisfies the water check, and a thickener with two sludge outlets
fails it.

These are minimum counts. Multiple sludge outlets and intermittent withdrawal
are valid. The shapes do not check solids concentration, clarification
efficiency, or whether both streams flow at once, and connection-point roles
stay optional.

See the {download}`conforming gravity thickener <../../examples/gravity-thickener-outlets.ttl>`
and the {download}`nonconforming thickener with two sludge outlets <../../examples/nonconforming/gravity-thickener-without-liquid-outlet.ttl>`.

## Pumps

### Requirements

`watr:Pump` is a subclass of `s223:Equipment`. It needs at least one inlet and at
least one outlet whose medium is an `s223:Mix-Fluid`, such as water, oil or
sludge, or an `s223:Constituent-Refrigerant`. Its connection points, other than
electrical ones, must carry compatible media.

### Rationale

A WaTr pump should be a subclass of `s223:Pump`. S223's pump shape, however,
warns on any medium other than water, oil or refrigerant, and a wastewater plant
pumps sludge and mixed liquor. A subclass cannot relax a constraint its superclass
imposes, so `watr:Pump` sits beside `s223:Pump` and restates the S223 checks with
the medium widened to any fluid mixture. This is a workaround. It goes away, and
`watr:Pump` becomes a subclass of `s223:Pump` again, once the S223 pump shape
accepts any `Mix-Fluid`.

### Validation

The inlet and outlet checks are warnings, matching S223's. The media
compatibility check is a violation. Three further pieces keep the two pump classes
aligned. The axiom `s223:Pump rdfs:subClassOf watr:Pump` makes every S223 pump a
WaTr pump, so a query for `watr:Pump` finds both. A SHACL-AF triple rule on
`watr:Pump` types a pump as `s223:Pump` when it conforms to the S223 pump shape,
so tools that select `s223:Pump` still find water pumps. A sludge pump does not
conform, so it is not typed `s223:Pump` and draws no S223 warning. Instead, an
`sh:Info` finding marks each pump that relies on the workaround: "Workaround:
{$this} has a connection point with medium {?medium}, which s223:Pump does not
accept (water, oil or refrigerant). It is validated as a watr:Pump only and is
not typed s223:Pump."

The recycle pumps in {download}`a2o-train.ttl <../../examples/a2o-train.ttl>`
carry mixed liquor and sludge and produce this Info finding. Validation of the
medium is a topology check only; it does not certify that a pump suits a
particular sludge.

## Filtration and membrane processes

### Definitions

`Process-Filtration` and `Process-MembraneProcess` are separate subtypes of
`Process-Separation`. Microfiltration, ultrafiltration and reverse osmosis are
subtypes of both. Media filtration, microfiltration and ultrafiltration also
declare `Process-SolidLiquidSeparation`; reverse osmosis does not. Membrane
distillation and electrodialysis are membrane processes with no filtration
parent: membrane distillation moves water as vapor, and electrodialysis moves ions
under an electric potential. GAC filtration is both adsorption and media
filtration.

### Rationale

EPA's [Membrane Filtration Guidance Manual, Chapter 2](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=901V0500.TXT)
includes MF, UF and RO in membrane filtration and distinguishes electrodialysis
from filtration. DOE's [solar-desalination projects](https://www.energy.gov/cmei/systems/solar-desalination)
describe thermally driven membrane distillation. These mechanisms support the
classification; the hierarchy itself is an ontology design choice.

### Validation

No shape checks the hierarchy itself, but the class requirements that use it
follow from it. A `Filter` requires a `Process-Filtration`, so membrane
distillation or electrodialysis alone does not meet it. Reverse osmosis does not
meet the solid-liquid separation step of activated sludge. Query
`Process-MembraneProcess` to find every membrane separation. See the
{download}`membrane-process example <../../examples/membrane-process-classification.ttl>`.

## Removal objectives and their targets

### Definitions

Every separation process implies `TreatmentObjective-ConstituentRemoval`, which
records separation from a stream rather than loss from the whole plant.
Adsorption, ion exchange and chemical precipitation also imply it. Generic
oxidation, reduction, dosing, mixing and gas transfer do not.

Named objectives beneath it group common targets: suspended solids, dissolved
solids (desalination, hardness, silica, sulfate, arsenic), metals (lead),
organics, nutrients and chlorine residual. `watr:targetsConstituent` names the
constituent an objective is aimed at. An objective without its own target
inherits one from its nearest ancestor that declares one; the
[constituent query](../guides/querying_treatment_function.md#find-equipment-by-constituent)
implements this.

`TreatmentObjective-SuspendedSolidsRemoval` covers suspended and settleable solids;
clarification and turbidity removal are beneath it.
`TreatmentObjective-DissolvedSolidsRemoval` is a separate branch, with desalination
and softening beneath it. The older `TreatmentObjective-SolidsRemoval` is deprecated
with `dcterms:isReplacedBy TreatmentObjective-SuspendedSolidsRemoval`.

### Rationale

The broad objective names no target on purpose. RO implies constituent removal
without assuming desalination, and a plant states PFAS removal or resource
recovery when that is the intent. Converting arsenite to arsenate prepares arsenic
for later removal without removing any, so generic oxidation and reduction carry no
removal objective. Disinfection targets pathogens but sits outside the removal
branch, because inactivation need not separate organisms from the water. Ammonia
control is not nitrogen removal: nitrification changes ammonia into nitrate and
leaves the nitrogen in the water.

The published `SolidsRemoval` URI was ambiguous between suspended and dissolved
solids. It keeps its original suspended-solids meaning and is a subclass of its
replacement, so existing models stay valid.

### Validation

Every `targetsConstituent` value must be an `s223:Medium-Constituent`
(`ConstituentTargetValueShape`, a violation). `ConstituentRemovalTargetShape`
warns when a constituent-removal objective in a plant model neither names a
target nor inherits one: "{$this} is a constituent-removal objective but names no
constituent." An objective naming a constituent the vocabulary lacks is incomplete
rather than wrong, which is why this is a warning. The vocabulary's own terms are
exempt; `tests/test_constituent_targets.py` checks that each of them resolves to a
constituent. Nothing reports use of a deprecated term.

A plant can extend the target vocabulary without editing WaTr. A local objective
is an instance, so the `watr:TreatmentObjective` shape requires it to carry one
label and one comment:

```ttl
@prefix : <urn:example/local-objective#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .

:selenium a s223:Medium-Constituent .
:removeSelenium a watr:TreatmentObjective-ConstituentRemoval ;
    rdfs:label "Selenium removal" ;
    rdfs:comment "Removal of selenium from mine drainage." ;
    watr:targetsConstituent :selenium .
```

See the {download}`suspended and dissolved solids example <../../examples/solids-removal-objectives.ttl>`,
the {download}`arsenic and lead example <../../examples/arsenic-lead-removal.ttl>`,
and the [generated process/objective map](../reference/process_objective_map.md)
for the complete hierarchies.

## Disinfection, oxidation, and thermal treatment

### Definitions

Chlorination implies disinfection, and `UltravioletLightUnit` carries disinfection
through `DisinfectionUnit`. Generic UV irradiation, ozonation and thermal treatment
imply no objective. Thermal hydrolysis is both hydrolysis and thermal treatment,
with no product objective. Sulfite dosing implies chlorine residual removal.
Cleaning processes, such as backwashing, air scouring and purging, imply
`TreatmentObjective-EquipmentCleaning`.

### Rationale

Chlorination covers dosing and contact time designed for disinfection, not just
metering, so the objective holds wherever it is performed. UV irradiation also
drives photolysis and advanced oxidation, and ozone also oxidizes taste, odor and
micropollutants, so neither process alone implies disinfection; the equipment
class or the modeler says so. Thermal hydrolysis has possible benefits but no single
universal product. Restoring a filter is a purpose even though it produces no
product water, so cleaning has its own objective.

### Validation

No extra shape applies. `ProcessObjectiveRule` adds the implied objectives during
inference, as described in [equipment function](equipment_function.md#objectives-implied-by-a-process).

## Severity levels

SHACL findings come in three levels. A `sh:Violation` means a requirement is not
met and the model must change, such as a clarifier with no sludge outlet or a
composition percentage above 100. A `sh:Warning` means the description is
incomplete or worth checking, such as a system claiming a compound process that no
member performs. An `sh:Info` is advisory and may be intentional, such as an
unconnected port at a model boundary, or a pump relying on the `watr:Pump`
workaround.

Severity classifies a finding; the caller decides which levels fail validation.
This repository requires conforming examples to have no warnings or violations
and allows Info findings. Nonconforming examples must produce at least one
violation. `tests/test_examples.py` and `tests/test_nonconforming_examples.py`
enforce this.

## Published documents and retired terms

Source modules live in `ontology/`. The build emits `build/watr.ttl` and a
versioned copy; term URIs stay unversioned. Retired process, role and objective
terms remain with `owl:deprecated true` and a `dcterms:isReplacedBy` link, so
existing models still parse and validate. Update models to the replacements; no
shape reports a deprecated term. `scripts/check_watr_terms.py` checks only that
every `watr:` term a model uses is defined.

Turtle `#` comments are source notes. `rdfs:comment` is the queryable
definition, and every term must have one (the `watr:Class` shape).
