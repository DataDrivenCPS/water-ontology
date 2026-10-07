# PR #39 review disposition

Merged PR #46 supplies aqueous-media constituents, RO compatibility, quantified
composition validation, and complement inference. Main also supplies the
`ontology/` layout, watermetadata.org URIs, and compilation to `build/watr*.ttl`.

Fletcher's September 21–22 review is addressed as follows:

| Request | Release preparation |
| --- | --- |
| Filtration wording includes membranes | Definitions distinguish filters, media beds, and membranes. |
| Settling rather than sedimentation as the mechanism | Active process is `Process-Settling`; the published sedimentation URI remains deprecated with a replacement link. Clarification remains an objective. |
| Default constituent removal for separation | Declared on `Process-Separation` and inherited by its descendants, without choosing a target or guaranteeing performance. |
| Chemical processes may imply removal | Adsorption, ion exchange, and precipitation declare broad constituent removal; generic oxidation, reduction, dosing, and mixing do not universally imply it. |
| Microfiltration also solid–liquid | Both microfiltration and ultrafiltration have membrane and solid–liquid parents. |
| Thermal hydrolysis also thermal treatment | Both hydrolysis and thermal-treatment parents are declared. |
| Add arsenic and lead | Constituents and targeted removal objectives added. Arsenic is under dissolved solids; lead is under metals. |
| Backwashing has an objective | Cleaning and its descendants imply `EquipmentCleaning`, distinct from product-water constituent removal. |
| Additional processes beyond defaults | Allowed explicitly while preserving required processes and process-value validation. Plausibility checks are deferred. |
| Clarifier versus SedimentationTank | Clarifier is a specialization with the clarification design objective, not an alias. |
| Clarifier underflow wording | Both overflow and sludge underflow are produced; sludge may go to additional thickening. |
| Chlorine-removal and reuse wording | Prose uses chlorine removal and water reuse treatment unit. |
| Additional cleaning activities | Stated directly through `hasProcess` and imply `EquipmentCleaning`; no separate activity category or permission list. |
| Anoxic/aerobic/anaerobic classification | Retained as explicit roles, as accepted in Fletcher's later comment. |
| Repurposed equipment | Current type and operating context in timestamped models; no conversion-history vocabulary. |

Earlier review points are also covered: chlorination includes dosing and contact
time; GAC is a filtration activity; RO does not imply desalination; objective
hierarchies group named targets; process/objective files use objective names;
reference descriptions list multiple parents once; `hasTreatmentObjective` and
`achievesTreatmentObjective` have distinct documented subjects; sensor examples
use specific observation locations; storage tanks permit a single bidirectional
fluid port; and SHACL severity and RDF/source comments are explained.

Composition arithmetic now requires an explicit complete-composition premise
before filling in a remainder. It does not sum mass and volume fractions together,
and individual percentages must lie between zero and 100. Partial compositions
remain valid and retain unknown values. Published process and role URIs retired
by this work remain present with deprecation and replacement metadata.

Some earlier suggestions remain intentionally outside this PR: numerical permit
limits and dedicated resource-recovery subtypes require their own design. The
existing generic objective permits a modeler to state resource-recovery intent.

Potential chemical-conversion modeling and recirculation inference from topology
are tracked in [Pending Ontology Features](pending_features.md).

## Perspective from treatment references

Flowing media (water, brine, aqueous sludge) and filter media (carbon, sand,
resin) have different roles in the model. GAC is a material used by an adsorption
or filtration activity; it should not become the medium carried by a water pipe.
EPA describes GAC and adsorptive beds as treatment materials and RO as a
membrane process used against several contaminants. This supports keeping
mechanisms independent of specific targets. [EPA treatment overview](https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies).

EPA distinguishes arsenic pre-oxidation from subsequent removal: changing
arsenite to arsenate improves later separation but does not itself remove total
arsenic. Therefore generic oxidation/reduction imply no removal objective.
[Arsenic treatment guidance](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=20017IDW.TXT).

UV irradiation also supports photolysis of organic contaminants, so the generic
process implies no universal disinfection objective. The disinfection equipment
class retains that intended objective. Lead removal is distinct from preventing
lead release through corrosion control; no phosphate-dosing implication is added.
[EPA treatment overview](https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies).

Gravity thickening produces concentrated solids and relatively clear supernatant.
That supports using settling for the common mechanism and distinguishing the
intended product through clarification/thickening objectives.
[EPA gravity thickening](https://www.epa.gov/biosolids/fact-sheet-gravity-thickening).

Thermal hydrolysis exposes wet organics to heat and pressure, supporting both
hydrolysis and thermal-treatment parents. Product-specific benefits require
process configuration and are not universal inferred objectives.
[Cambi process description](https://www.cambi.com/process).

Shared constituents establish S223 topology compatibility, not equivalent
composition, material balance, membrane selectivity, or equipment suitability.
For example, retaining an aqueous-sludge designation on pump ports does not
certify that a particular pump is suitable for that sludge.

The local documentation build also removes an obsolete Sphinx directive: the
current template package exposes a MyST plugin, while this Jupyter Book uses
Sphinx. The book links the existing rendered template pages.
