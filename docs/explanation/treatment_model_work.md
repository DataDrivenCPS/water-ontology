# Implementation plan

This is the plan for implementing
[treatment_model_summary.md](treatment_model_summary.md) on the
`gtf-watr-constituent-mixtures` branch. That document describes the target
model; this one says what to change, in what order, and how to know it worked.

Each step names the files it touches and the section of the design document
that describes the end state. Steps marked *not in the design document* are
implementation detail with no design content behind them.

## How to work

**File map.** The vocabulary lives in `water/`. `ontology.ttl` is the root: it
declares the properties and the SHACL shapes, and `owl:imports` the other five
files.

| file | holds | changed by |
|---|---|---|
| `water/ontology.ttl` | properties, validation shapes, prefix declarations | steps 2.3, 5.2 |
| `water/substances.ttl` | constituents, media, chemicals | step 1 |
| `water/outcomes.ttl` | treatment objectives | step 2, renamed in step 7.1 |
| `water/processtypes.ttl` | processes | step 3 |
| `water/equipment.ttl` | equipment classes and their requirements | step 4 |
| `water/class-defaults.ttl` | the SHACL-AF inference rules | step 5 |
| `water/enumerationkinds.ttl` | roles and other enumerations | unchanged — the role list in section 7 already matches |

**Build and test.**

```sh
make                # compiles libraries/water.ttl through ontoenv
make test           # uv run pytest tests
cd scripts && uv run python ttl-to-md.py          # regenerates docs/reference/*_documentation.md
uv run python scripts/generate-process-outcome-map.py   # regenerates the process/objective map
uv run python scripts/check_watr_terms.py examples      # every watr: term used is defined
```

CI (`.github/workflows/static.yml`) runs `make` then `make test`, and builds
the docs. Run `check_watr_terms.py` after every rename: it is the fastest way
to catch a term that some example or template still points at.

**Conventions to follow.** They are already in the files; match them.

- Every term self-types: `watr:Process-Foo a watr:Class, watr:Process-Foo ;`.
  This is what makes `sh:class watr:Process` accept the term as a value, and it
  is also what lets a modeler write a local instance of a class (step 2.3).
- Processes and objectives describe themselves with `skos:definition`;
  equipment and enumeration kinds use `rdfs:comment`. `scripts/ttl-to-md.py`
  accepts either. Step 7.4 documents the split.
- Renames on this branch are hard renames with a comment left at the old term's
  former position saying what happened and why. `Process-Dechlorination` and
  `Process-LandApplication` were removed that way; follow the same pattern.
  There are no deprecation stubs, because nothing outside this repository
  consumes the vocabulary yet. `watr:Role-Backwash` is the one exception, and
  it stays as it is.

**Decide these before starting.** Each one changes what gets written.

| question | where it bites | recommendation |
|---|---|---|
| Does `watr:ElectrodialysisUnit` keep its desalination default? | step 4.3 | Keep it if the team considers electrodialysis desalination-specific; drop it if ED is used for other separations. *Not in the design document* — flagged as an open question in the original work list. |
| Is `watr:TreatmentObjective-pHControl` a rename of the existing `-pHAdjustment`, or a new parent above it? | step 2.2 | Rename. The design document's objective tree has pH Control with Neutralization under it and no pHAdjustment, so a rename reproduces the tree exactly. |
| Which of the remaining class-level design objectives survive the "every unit of the class" rule? | step 4.3 | Proposed dispositions are in the table there. They need a sign-off, not a code change. |

## 1. Constituents — done

*`water/substances.ttl`. Described in section 7, constituents.*

Objectives point at constituents, so this goes first. The three terms that
sat at the top of the file, away from the rest, moved down into one
constituent section with a header comment, so the whole hierarchy reads in
one place. Nothing was dropped: every term the file defined before it still
defines.

1.1. Add fourteen terms, each `a watr:Class, a watr:Constituent-X, a sh:NodeShape` with `rdfs:label`, `rdfs:comment`, and `rdfs:subClassOf`, following the block at the end of the file:
`DissolvedSolids`, `Hardness` (calcium and magnesium), `Silica`, `Sulfate`,
`VolatileOrganicCompounds`, `PFAS`, `Nitrogen`, `OrganicNitrogen`,
`Phosphorus`, `Phosphate`, `Pathogens`, `Viruses`, `Protozoa`,
`ChlorineResidual`.

1.2. Re-parent seven existing terms, currently all direct subclasses of `s223:Medium-Constituent`:

| term | new parent |
|---|---|
| `watr:Constituent-Salt` | `watr:Constituent-DissolvedSolids` |
| `watr:Constituent-Metals` | `watr:Constituent-DissolvedSolids` |
| `watr:Constituent-Ammonia` | `watr:Constituent-Nitrogen` |
| `watr:Constituent-Nitrate` | `watr:Constituent-Nitrogen` |
| `watr:Constituent-Nitrite` | `watr:Constituent-Nitrogen` |
| `watr:Constituent-Bacteria` | `watr:Constituent-Pathogens` |

`Constituent-Particles`, `-Solids`, `-SuspendedSolids`, `-Organics`,
`-OrganicCarbon`, `-Inorganics`, `-InorganicCarbon`, `-DissolvedOxygen`,
`-NitrogenOxides`, `-Cyanide` and `Salt-NaCl` already sit where the design
document puts them. Add `VolatileOrganicCompounds` and `PFAS` under
`Constituent-Organics`.

1.3. Fix the labels while in the file. `Constituent-Metals`,
`Constituent-Salt`, `Constituent-Organics`, `Constituent-Particles` and
several others carry their own identifier as their `rdfs:label` and
`rdfs:comment`. Give them a human label ("Metals", "Salt") and a real
definition, the way `Constituent-Ammonia` and `Constituent-DissolvedOxygen`
already do. *Not in the design document.*

1.4. Note for step 7.3: `scripts/ttl-to-md.py` generates
`docs/reference/substances_documentation.md` from `enumerationkinds.ttl`, not
from `substances.ttl`, so none of these terms currently reach the published
reference. Decide there whether to add a generator entry for `substances.ttl`.

## 2. Treatment objectives — done

*`water/outcomes.ttl`, `water/ontology.ttl`. Described in sections 1a, 7 and 4.*

Two things came out differently than written here. `watr:ConstituentRemovalTargetShape`
skips nodes typed `watr:Class`, so it checks plant models and not this
vocabulary's own terms: every term self-types, which makes
`watr:TreatmentObjective-ConstituentRemoval` a target of the shape's own
`sh:targetClass`, and the abstract parent of the branch names no constituent
by design. That the named objectives all resolve to a constituent is checked
in `tests/test_constituent_targets.py` instead, which is the new home of the
2.5 tests — `test_validation.py` validates the ontology against itself and had
no room for model-level cases. The comments in `processtypes.ttl` that named
the deleted disposal objectives were updated here rather than in step 3, so
that no comment outlives the term it points at.

2.1. **Add five parents.** `TreatmentObjective-ConstituentRemoval`,
`-DissolvedSolidsRemoval`, `-VolumeReduction`, `-pHControl`,
`-ResourceRecovery`. `ResourceRecovery` is a placeholder with no children;
say so in its definition.

2.2. **Restructure the tree.** The target is the objectives tree in section 7.
Every line below is an `rdfs:subClassOf` change or an addition to the existing
file.

| objective | parent today | parent after |
|---|---|---|
| `-SolidsRemoval` | `TreatmentObjective` | `-ConstituentRemoval` |
| `-Clarification` | `TreatmentObjective` | `-SolidsRemoval` |
| `-TurbidityRemoval` | `-SolidsRemoval` | unchanged |
| `-DissolvedSolidsRemoval` | new | `-ConstituentRemoval` |
| `-Desalination` | `TreatmentObjective` | `-DissolvedSolidsRemoval` |
| `-Softening` | `TreatmentObjective` | `-DissolvedSolidsRemoval` |
| `-SilicaRemoval` | `TreatmentObjective` | `-DissolvedSolidsRemoval` |
| `-SulfateRemoval` | `TreatmentObjective` | `-DissolvedSolidsRemoval` |
| `-MetalsRemoval` | `TreatmentObjective` | `-DissolvedSolidsRemoval` |
| `-OrganicsRemoval` | `TreatmentObjective` | `-ConstituentRemoval` |
| `-NutrientRemoval` | `TreatmentObjective` | `-ConstituentRemoval` |
| `-NitrogenRemoval`, `-PhosphorusRemoval` | `-NutrientRemoval` | unchanged |
| `-AmmoniaControl` | `TreatmentObjective` | `-ConstituentRemoval`, as a sibling of `-NutrientRemoval`, not a child |
| `-ChlorineResidualRemoval` | renamed from `-Dechlorination` | `-ConstituentRemoval` |
| `-Thickening` | `TreatmentObjective` | `-VolumeReduction` |
| `-Dewatering` | `TreatmentObjective` | `-VolumeReduction` |
| `-Drying` | `-Dewatering` | unchanged |
| `-Neutralization` | `-pHAdjustment` | `-pHControl` |
| `-Disinfection`, `-Stabilization`, `-BiosolidsDisposal` | `TreatmentObjective` | unchanged |

Also in this file:

- Rename `-Dechlorination` to `-ChlorineResidualRemoval`, with
  `skos:altLabel "Dechlorination"`. Leave a comment at the old position.
- Rename `-pHAdjustment` to `-pHControl` (see the decision table).
- **Delete** `-LandApplication` and `-Landfill`, and the comment block above
  them arguing that the disposal routes are objectives. Step 3.3 makes them
  processes instead. Everything that referenced them now references
  `-BiosolidsDisposal`, which they were subclasses of.

2.3. **Declare `watr:targetsConstituent`** in `water/ontology.ttl`, next to
`watr:achievesTreatmentObjective`, with the same shape of comment: what it
relates and why it is on the class rather than the instance.

```ttl
watr:targetsConstituent
    a rdf:Property ;
    rdfs:label "targets constituent" ;
    rdfs:comment "Relates a constituent-removal objective to the constituent it removes or controls." ;
    rdfs:domain watr:Class ;
    rdfs:range s223:Medium-Constituent ;
.
```

Add two shapes beside the existing value guards:

- `watr:ConstituentTargetValueShape`: `sh:targetObjectsOf watr:targetsConstituent ; sh:class s223:Medium-Constituent`. Mirrors `watr:ProcessValueShape`.
- `watr:ConstituentRemovalTargetShape`: every `watr:TreatmentObjective-ConstituentRemoval` states at least one `watr:targetsConstituent`. `sh:Warning`, not `sh:Violation` — a modeler's local objective for a constituent the vocabulary does not carry yet is incomplete, not wrong.

2.4. **Declare a target on every named constituent-removal objective**, in
`outcomes.ttl`, from the mapping in section 7:

| objective | `watr:targetsConstituent` |
|---|---|
| `-SolidsRemoval` | `watr:Constituent-SuspendedSolids` (Clarification and TurbidityRemoval inherit it) |
| `-DissolvedSolidsRemoval` | `watr:Constituent-DissolvedSolids` |
| `-Desalination` | `watr:Constituent-Salt` |
| `-Softening` | `watr:Constituent-Hardness` |
| `-SilicaRemoval` | `watr:Constituent-Silica` |
| `-SulfateRemoval` | `watr:Constituent-Sulfate` |
| `-MetalsRemoval` | `watr:Constituent-Metals` |
| `-OrganicsRemoval` | `watr:Constituent-Organics` |
| `-NutrientRemoval` | `watr:Constituent-Nitrogen`, `watr:Constituent-Phosphorus` |
| `-NitrogenRemoval` | `watr:Constituent-Nitrogen` |
| `-PhosphorusRemoval` | `watr:Constituent-Phosphorus` |
| `-AmmoniaControl` | `watr:Constituent-Ammonia` |
| `-ChlorineResidualRemoval` | `watr:Constituent-ChlorineResidual` |
| `-Disinfection` | `watr:Constituent-Pathogens` — not a constituent-removal objective, but it carries a target anyway |

2.5. **The modeler's local objective needs no new machinery**, but it needs a
test. Because every ontology term self-types, `watr:TreatmentObjectiveValueShape`
(`sh:class watr:TreatmentObjective`) already accepts

```ttl
:removeSelenium a watr:TreatmentObjective-ConstituentRemoval ;
    watr:targetsConstituent :Selenium .

:ixColumn a watr:IonExchangeUnit ;
    watr:hasTreatmentObjective :removeSelenium .
```

Confirm it does, in `tests/test_validation.py`, and confirm the warning in 2.3
fires when `watr:targetsConstituent` is left off. Described in section 1a,
treatment objective.

## 3. Processes — done

*`water/processtypes.ttl`. Described in sections 4 and 7.*

One departure from 3.4 below: `Process-GACFiltration` keeps adsorption as a
parent but takes `Process-MediaFiltration` in place of `Process-Filtration`,
which is where the design document's tree puts GAC filtration. Media
filtration is a filtration, so nothing that matched before stops matching.
The step 3.6 reconciliation found no other gap: the twenty processes that
declare an objective are exactly the twenty the design names, and the tree
otherwise differs from section 7 only by carrying extra parents the document
does not contradict — combustion is both physical and chemical, flocculation
is both chemical and mixing, and so on.

3.1. **Rename `Process-ChlorineDosing` to `Process-Chlorination`**, label
"Chlorination". Widen the definition: the process is dosing plus contact time,
not dosing alone. It keeps
`watr:achievesTreatmentObjective watr:TreatmentObjective-Disinfection` and its
`Process-Dosing` parent. Callers to update: `water/equipment.ttl`
(`watr:ChlorinationUnit`), `libraries/templates/equipment.yml:441`,
`tests/test_process_plausibility.py`, `tests/test_system_processes.py`,
`examples/`.

3.2. **Add `Process-SulfiteDosing`** under `Process-Dosing`, with
`watr:achievesTreatmentObjective watr:TreatmentObjective-ChlorineResidualRemoval`.
Replace the comment block left where `Process-Dechlorination` used to be: it
still says the objective is `TreatmentObjective-Dechlorination`, and it should
now name the renamed objective and point at sulfite dosing as the one mechanism
that gets its own term.

3.3. **Add `Process-LandApplication` and `Process-Landfilling`** under
`Process-PhysicalProcess`, each with
`watr:achievesTreatmentObjective watr:TreatmentObjective-BiosolidsDisposal`.
This reverses the earlier removal; replace the comment at lines 219–221 that
records it. Note the spelling: the process is `Landfilling`, the deleted
objective was `Landfill`.

3.4. **Rename `Process-GranularActivatedCarbon` to `Process-GACFiltration`**,
label "GAC Filtration". It keeps both parents, `Process-Adsorption` and
`Process-Filtration`, which is what the design document's "GAC Filtration (also
adsorption)" means. Update `watr:GranularActivatedCarbonAdsorber` in
`equipment.ttl`, whose `sh:message` also misspells the class as
"GranulatedActivatedCarbonAdsorber".

3.5. **Relabel the root.** `watr:Process` reads "Water Process"; the design
document calls it "Water Treatment Process". The identifier does not change.

3.6. **Reconcile the rest of the tree against section 7.** Everything else in
the design document's process tree already exists with the right parent and the
right `achievesTreatmentObjective`; walk the list once and confirm, rather than
assuming. The entailments that should be present when you finish: UV
irradiation, chlorination, sulfite dosing, land application, landfilling, both
incinerations, composting, high-density sludge, nitrification, denitrification,
EBPR, digestion, activated sludge, AO, MLE, A2O, UCT, and both Bardenphos.
Nothing else declares one — in particular filtration, the membrane processes,
chemical precipitation, adsorption and sedimentation must not.

## 4. Equipment classes — done

*`water/equipment.ttl`. Described in sections 1a, 2, 4 and 6.*

The 4.3 audit was signed off with all four borderline classes dropping their
objective, electrodialysis included: an electrodialysis stack desalinates,
recovers acids and concentrates brine, and the ontology already carries
Electro-Dialytic Crystallization as one of those routes. Ten classes still
carry a design objective, the nine keeps below plus the new `watr:Clarifier`.
4.5 needed no edit: `watr:Clarifier` reaches `watr:SeparationTank`'s
recirculation permission and `watr:Tank`'s cleaning permission by
inheritance. The secondary clarifier in `examples/a2o-train.ttl` was retyped
here rather than in step 6, because its comment claimed a class default that
this step removed.

4.1. **Remove the clarification default from `watr:SedimentationTank`** (the
`sh:property` block on `watr:hasTreatmentObjective` at lines 521–526, and the
comment above it at 518–520). The tank
keeps its `Process-Sedimentation` requirement. Replace the comment above it
with the reasoning from section 2: a settling tank always puts out both a
clarified overflow and a thickened underflow, so which one the plant relies on
is a fact about the plant.

4.2. **Add `watr:Clarifier`** as a subclass of `watr:SedimentationTank`,
carrying `TreatmentObjective-Clarification` as a qualified requirement. Put it
next to `watr:SepticTank` and `watr:ImhoffTank`, the other subclasses. This is
the class the design document's worked examples and its whole-train example
type their clarifiers with, so nothing else works until it exists.

4.3. **Audit every other class-level design objective** against the rule from
section 2: a class carries a design objective only when every unit of the class
is built for the same result. The fifteen that carry one today:

| class | objective | proposed disposition |
|---|---|---|
| `watr:Thickener` | Thickening | keep — named in section 2 as passing |
| `watr:DisinfectionUnit` | Disinfection | keep — named in section 2 as passing |
| `watr:Digester` | Stabilization | keep — every digester stabilizes |
| `watr:DewateringUnit` | Dewatering | keep — the class is named for its result |
| `watr:Screen` | SolidsRemoval | keep — section 9 shows the bar screen inheriting it |
| `watr:GritChamber` | SolidsRemoval | keep |
| `watr:SedimentationTank` | Clarification | **drop** — step 4.1 |
| `watr:ReverseOsmosisMembrane` | Desalination | **drop** — step 4.4 |
| `watr:ElectrodialysisUnit` | Desalination | **open** — see the decision table |
| `watr:NanofiltrationUnit` | Softening | **drop** — NF also serves organics and sulfate removal; plant intent |
| `watr:MediaFiltrationUnit` | TurbidityRemoval | **drop** — a media filter serves turbidity in a polishing duty and solids removal elsewhere |
| `watr:GranularActivatedCarbonAdsorber` | OrganicsRemoval | **drop** — GAC also serves PFAS removal and chlorine residual removal |
| `watr:SequencingBatchReactor` | OrganicsRemoval | keep — activated sludge always removes organics |
| `watr:OxidationDitch` | OrganicsRemoval | keep — same reason |
| `watr:UVH2O2Reactor` | OrganicsRemoval | keep — an AOP reactor is built to oxidize organics |

Each drop is one `sh:property` block deleted, plus a comment saying why the
class carries no objective, in the style of the existing note on
`watr:AirStripper`. Each keep gets no edit. The dispositions are proposals:
they need the team's sign-off, and they are the one part of this plan that is
judgment rather than transcription.

4.4. **Drop the desalination default on `watr:ReverseOsmosisMembrane`**
(lines 830–839, comment included). Section 6's worked example has the modeler write the objective
instead. Check the subclasses — closed-circuit, feed-reversal and osmotically
assisted RO — in case any of them restates it.

4.5. **Re-check `mayAlsoPerform`** on the classes touched above. Dropping a
required objective does not affect it, but `watr:Clarifier` inherits
`SedimentationTank`'s permissions and should not need its own.

## 5. Inference and validation

*`water/class-defaults.ttl`, `water/ontology.ttl`. Described in sections 1a, 1b and 5.*

5.1. **Add the process-to-objective rule.** Sections 1b and 5 treat the
objective of a process as inherited, and section 9's expected output has the
anoxic zone getting nitrogen removal from denitrification with nothing written
by the modeler. Today that inference does not exist: the objective is only
*warned about*. Add a second SHACL-AF rule beside `watr:ClassDefaultsRule`:

```ttl
CONSTRUCT { $this watr:hasTreatmentObjective ?objective . }
WHERE {
    $this watr:hasProcess ?process .
    ?process rdfs:subClassOf*/watr:achievesTreatmentObjective ?objective .
}
```

Three things to get right:

- **Target both equipment and systems.** `watr:ClassDefaultsRule` targets
  `s223:Equipment` only. Section 9 expects `:bioTrain`, an `s223:System`, to
  inherit nitrogen, phosphorus and organics removal from `Process-A2O`, so this
  rule needs `s223:System` too. `sh:targetSubjectsOf watr:hasProcess` covers
  both in one shape.
- **Ordering.** A bare `watr:ChlorinationUnit` has no asserted `hasProcess`;
  `Process-Chlorination` arrives from the class-defaults rule. This rule must
  see that output. Confirm whether `shifty.infer` runs rules to a fixpoint; if
  it does not, give the class-defaults rule `sh:order 0` and this one
  `sh:order 1`. Pin the behaviour with a test either way — a bare
  `ChlorinationUnit` must come out with `TreatmentObjective-Disinfection`, and
  a bare `MixingBasin` with an asserted `Process-Denitrification` must come out
  with `TreatmentObjective-NitrogenRemoval`.
- **No `FILTER NOT EXISTS`.** The class-defaults rule suppresses a general
  value when a more specific one is present, because a class requirement is a
  minimum. An entailment is not: if the process achieves the objective, the
  unit has it, and asserting it twice is harmless.

5.2. **Remove `watr:TreatmentObjectiveCompletenessShape`** from
`ontology.ttl`, with its long comment. It warns that a unit performs a process
achieving an objective it does not state — which, once 5.1 lands, can never
happen, because the rule states it. The comment's second half, on why the
converse check would be wrong, is worth keeping somewhere near
`watr:achievesTreatmentObjective`.

5.3. **Update the tests that assert the warning.**
`tests/test_system_processes.py` lines 529–587 exercise the shape directly;
`tests/test_a2o_train.py:131` mentions it. Rewrite them as inference tests: the
objective is now *added*, so assert on the materialized graph the way
`tests/test_class_defaults.py` does.

5.4. **Leave the other shapes alone.** `ProcessBearerShape`,
`ProcessValueShape`, `TreatmentObjectiveValueShape`,
`TreatmentObjectiveRequiresProcessShape`, `SystemProcessCoverageShape` and the
plausibility warning all still hold. Section 5 lists exactly this set.

## 6. Examples, templates and tests

*Not in the design document, except where noted.*

6.1. `examples/a2o-train.ttl`, `examples/swing-zone-dissolved-oxygen.ttl` and
`examples/union-dpr-model.ttl` reference renamed terms. Retype clarifiers to
`watr:Clarifier`, rename the chlorination process, and delete any
`hasTreatmentObjective` the model now inherits.

6.2. Add the whole train from section 9 as an example
(`examples/municipal-train.ttl` or similar). It is the design document's own
statement of what a modeler writes, and it exercises the class defaults, the
process entailment, the system coverage check and the membership query in one
file. `tests/test_examples.py` will validate it automatically once it is in
`examples/`.

6.3. `libraries/templates/equipment.yml`: line 380 types a unit as
`watr:SedimentationTank` — check whether it means a clarifier; line 441 uses
`watr:Process-ChlorineDosing`.

6.4. `examples/nonconforming/` — add a case for each new violation and warning:
a constituent-removal objective with no `targetsConstituent`, a
`targetsConstituent` value that is not a constituent.

6.5. Run `uv run python scripts/check_watr_terms.py examples` and repeat for
`libraries/templates` if the script accepts it. Every rename in steps 2 and 3
should show up here if anything was missed.

## 7. Documentation

7.1. **Rename the objectives files.** *Item from section 8's list of things
not addressed in the design.*

- `water/outcomes.ttl` → `water/objectives.ttl`, ontology URI
  `urn:nawi-water-ontology/outcomes` → `.../objectives`, and the `owl:imports`
  in `water/ontology.ttl`.
- `docs/reference/outcomes_documentation.md` →
  `objectives_documentation.md`, and `docs/reference/process_outcome_map.md` →
  `process_objective_map.md`.
- `scripts/generate-process-outcome-map.py` →
  `generate-process-objective-map.py`; update its output path and the
  "Generated by" line it writes into the page.
- `scripts/ttl-to-md.py`: the source and output paths.
- `docs/_toc.yml`: both reference entries.
- `tests/conftest.py` globs `water/*.ttl`, so it needs no change; the
  docstrings in `tests/test_class_defaults.py` say "outcome" and should say
  "objective".

7.2. **Fix and extend the query guide.** `docs/guides/querying_treatment_function.md`.
*Described in section 9.*

- Every variable named `?treatment objective` contains a space and is not
  valid SPARQL — the residue of an earlier rename. Lines 33–37, 73–78, 88–90,
  105–109 and 123–130. Rename them `?objective`.
- The intro at line 23 says an RO unit gets its desalination objective from its
  class. After step 4.4 it does not; rewrite the example.
- Add the system-membership query from section 9 — "what is involved in
  nitrogen removal", the `UNION` over carrying the objective and being a member
  of a system that carries it — with the note on narrowing the membership
  branch by `includesProcess`.

7.3. **Regenerate the reference pages** and fix the generator.

- `scripts/ttl-to-md.py` emits one section per superclass, so any class with
  two parents appears twice: `Process-GACFiltration`
  (`Adsorption` + `Filtration`) is the visible case, and the same bug produces
  twenty-seven repeated descriptions in `equipment_documentation.md`. Group the
  superclasses into one row and list them together.
- Decide whether `substances_documentation.md` should be generated from
  `substances.ttl` as well as `enumerationkinds.ttl`; today the constituents
  from step 1 would not appear anywhere in the published reference.
- The duplicated aeration basin description is already fixed — `watr:AirStripper`
  was split out of `watr:AerationBasin` and carries its own text. Confirm and
  strike it from the list.

7.4. **Prose pages.** `docs/explanation/processes.md`,
`equipment_function.md`, `system_processes.md` and `definitions.md` all state
the old model in places.

- The repurposing rule, from section 6: an unchanged vessel gains a role; a
  rebuilt vessel gets a new type; the model does not record the conversion.
  `equipment_function.md` is the natural home.
- The rule for when a class carries a design objective (section 2), so the
  audit in step 4.3 has something to point at.
- `processes.md:279` writes `Role-MakeUp` in a table of connection-point roles
  as `MakeUp` — prefix it.
- Explain `rdfs:comment` versus `skos:definition`: which vocabularies use
  which, and why the renderer accepts both.
- Link the shifty severity levels where the pages talk about warnings and
  violations.

7.5. **Update the design document's own status line.** The header of
`treatment_model_summary.md` says the branch does not implement the design yet.
When this plan is finished, that sentence changes.

## Verification

Run in this order. Each catches a different class of mistake.

1. `make` — the ontology parses and the closure resolves.
2. `uv run python scripts/check_watr_terms.py examples` — no example points at
   a term the renames removed.
3. `make test` — validation, class defaults, plausibility, system processes,
   and every example in `examples/`.
4. Regenerate the reference docs and the process/objective map; the diff should
   show the new hierarchy and no duplicate sections.
5. `uv run jupyter-book build docs` twice, as CI does.
6. Against the section 9 example, by hand: run each of the seven queries in
   section 9 and check the results tables match. This is the end-to-end check
   that the two inference rules together produce what the design document
   promises, and nothing in the test suite covers it as a whole.

## Suggested commits

One per step group, in order, each leaving `make test` green:

1. constituents (step 1)
2. objective hierarchy and `targetsConstituent` (step 2)
3. processes (step 3)
4. `watr:Clarifier` and the class-objective audit (step 4)
5. the process-to-objective rule, and the warning it replaces (step 5)
6. examples, templates and tests (step 6)
7. documentation (step 7.2, 7.4)
8. the `outcomes` → `objectives` rename and the generator fixes (steps 7.1, 7.3)

Steps 1 through 5 are ordered by dependency and should not be reordered.

## Where the original work list went

The eleven items of the previous checklist map onto the steps above.

| item | step |
|---|---|
| 1. objective hierarchy | 2.1, 2.2 |
| 2. `targetsConstituent` and local objectives | 2.3, 2.5 |
| 3. constituent vocabulary and targets | 1, 2.4 |
| 4. land application and landfill as processes | 2.2 (delete the objectives), 3.3 |
| 5. clarification default, `watr:Clarifier`, class audit | 4.1, 4.2, 4.3 |
| 6. chlorination, sulfite dosing, chlorine residual removal | 2.2, 3.1, 3.2 |
| 7. RO desalination default | 4.4, and the decision table for electrodialysis |
| 8. membership query and the guide's variable names | 7.2 |
| 9. process-to-objective inference, warning removed | 5.1, 5.2, 5.3 |
| 10. repurposing rule | 7.4 |
| 11. mechanical fixes | 3.4, 3.5, 7.1, 7.3, 7.4 |
