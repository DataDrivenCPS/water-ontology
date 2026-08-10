# `gtf-watr-constituent-mixtures` vs. `main`

Each section covers one thing the ontology could not say, or said wrongly. It
gives the definition on `main`, how a model has to be written against it, the
fix on this branch, and what can be written instead.

---

## 1. Aqueous media that could not share a pipe

### On `main`

The four aqueous media are bare subclasses of `s223:Fluid-Water`, with
placeholder comments:

```ttl
watr:Water-Seawater
  a watr:Class, watr:Water-Seawater, sh:NodeShape ;
  rdfs:comment "Water-Seawater" ;
  rdfs:subClassOf s223:Fluid-Water .

watr:Water-Brine
  rdfs:comment "Water-Brine" ;
  rdfs:subClassOf s223:Fluid-Water .
```

### Current modeling

S223 decides whether two media may meet by comparing the *constituents* they are
`s223:composedOf`. Two pure media are compatible only when one is a subclass of
the other. Seawater and brine are siblings, so they are incompatible — and the
central object of the domain cannot be modelled:

```ttl
:roUnit a watr:ReverseOsmosisMembrane ;
    s223:hasConnectionPoint :feed, :permeate, :concentrate .

:feed        s223:hasMedium watr:Water-Seawater .     # in
:permeate    s223:hasMedium watr:Water-Freshwater .   # out
:concentrate s223:hasMedium watr:Water-Brine .        # out
```

Three streams that are all water are treated as three mutually incompatible
fluids on one piece of equipment.

### The fix on this branch

Each medium declares what it is made of, and every one of them shares
`s223:Constituent-H2O`:

```ttl
watr:Water-Seawater
  rdfs:comment "Saline surface water (typical salinity ~3.5%) modeled as a
                constituent-bearing mixture of water and dissolved salt..." ;
  rdfs:subClassOf s223:Fluid-Water ;
  s223:composedOf [ a s223:QuantifiableProperty ;
                    s223:ofConstituent s223:Constituent-H2O ;
                    qudt:hasQuantityKind quantitykind:MassFraction ;
                    qudt:hasUnit unit:PERCENT ;
                    rdfs:label "Water fraction" ] ;
  s223:composedOf [ a s223:QuantifiableProperty ;
                    s223:ofConstituent watr:Salt-NaCl ;
                    qudt:hasQuantityKind quantitykind:MassFraction ;
                    qudt:hasUnit unit:PERCENT ;
                    rdfs:label "Salt fraction" ] .
```

### Why this works

Mixture media are compatible when they share a constituent. Seawater, brine,
brackish and fresh water now all do, so the RO model above validates unchanged.
The media differ by the *proportions* of shared constituents, which is what they
actually differ by — freshwater declares only water, the saline ones add salt.

`examples/ro-mixture-test.ttl` and `examples/brine-composition.ttl` keep this
honest as validated examples.

---

## 2. Equipment that could not validate at all

Three separate defects, each silent because a broken shape still parses.

### 2a. The disjoint flag

On `main`, every process requirement carries `sh:qualifiedValueShapesDisjoint`:

```ttl
watr:Screen                                    # main
    rdfs:subClassOf s223:Equipment, watr:UnitProcess ;
    sh:property [
        sh:path watr:hasProcess ;
        sh:qualifiedValueShape [ sh:class watr:Process-Screening ] ;
        sh:qualifiedValueShapesDisjoint true ;
        sh:qualifiedMinCount 1 ;
        sh:qualifiedMaxCount 1 ;
        sh:message "Instances of Screen must have the Screening process." ;
    ] .
```

The obvious model of a screen:

```ttl
:bar-screen a watr:Screen ;
    watr:hasProcess watr:Process-Screening .
```

**fails**, reporting "Instances of Screen must have the Screening process" — the
very process it was given. Nearly every equipment class with a process
requirement behaves this way. Deleting the one `sh:qualifiedValueShapesDisjoint`
line makes the model pass; deleting `sh:qualifiedMaxCount` instead does not.

The flag exists to stop one value counting toward two sibling qualified shapes.
On single-class requirements like this one it has nothing to do, and where two
requirements legitimately overlap it is harmful: `Process-ReverseOsmosis` *is* a
`Process-Filtration`, so an RO membrane's single process should answer both its
own requirement and the one it inherits from `watr:Filter`. The flag forbids
that.

It is removed everywhere, and the requirement now reads as intended:

```ttl
watr:Screen
    sh:property [
        sh:path watr:hasProcess ;
        sh:qualifiedValueShape [ sh:class watr:Process-Screening ] ;
        sh:qualifiedMinCount 1 ;
        sh:message "Instances of Screen must have a Screening process." ;
    ] .
```

### 2b. Requirements naming classes that do not exist

```ttl
watr:Boiler                                    # main
    rdfs:subClassOf s223:Boiler, watr:UnitProcess ;
    sh:property [
        sh:path watr:hasProcess ;
        sh:qualifiedValueShape [ sh:class watr:Process-Incineration ] ;
        sh:qualifiedMinCount 1 ;
    ] .
```

`watr:Process-Incineration` was renamed to `watr:Process-Combustion` and this
shape was not updated. Nothing complains, because a shape naming an undefined
class is still well-formed — but no value can ever carry the missing type, so
**no boiler could validate**. `watr:Tank` had the same problem with
`s223:Role-Overflow`, which S223 does not define.

Both are fixed, and the class of defect is now caught by a shape rather than by
eye:

```ttl
# For any watr:hasProcess / watr:hasOutcome / s223:hasRole constraint, every
# class it names must carry at least one rdf:type somewhere in the import
# closure. Traverses sh:class, sh:hasValue and sh:in lists, in both the direct
# and the qualified form.
watr:ProcessAndRoleConstraintsReferenceDefinedClasses
    a sh:NodeShape ;
    sh:targetSubjectsOf sh:path ;
    sh:or ( [ ... not a process/outcome/role shape ... ]
            [ ... every class it names is defined ... ] ) .
```

The existing "the ontology validates against itself" test enforces it, so the
next rename cannot leave a shape stranded.

### 2c. Constraints that asserted nothing

```ttl
watr:Tank                                      # main
    sh:property [
        sh:path s223:hasConnectionPoint ;
        rdfs:comment "A tank may have a drain connection point" ;
        sh:qualifiedMinCount 0 ;
        sh:qualifiedValueShape [ ... a fluid outlet carrying Role-Drain ... ] ;
    ] .
```

`sh:qualifiedMinCount 0` is satisfied by every graph — including one where the
drain is an *inlet*. The block reads as "a drain must look like this" and checks
nothing.

It now states the rule as the absence of a counterexample:

```ttl
watr:Tank
    sh:property [
        sh:path s223:hasConnectionPoint ;
        rdfs:comment "A tank's drain connection point, if it has one, is a fluid outlet" ;
        sh:qualifiedMaxCount 0 ;
        sh:qualifiedValueShape [
            sh:property [ sh:path s223:hasRole ; sh:hasValue watr:Role-Drain ;
                          sh:minCount 1 ] ;
            sh:not [ sh:class s223:OutletConnectionPoint ; ... ] ;
        ] ;
        sh:message "A drain connection point on a Tank must be an outlet carrying a fluid." ;
    ] .
```

Zero connection points that are drains *and not* fluid outlets. A tank with no
drain still passes; a tank whose drain is an inlet is now rejected.

---

## 3. Saying what else a piece of equipment does

### On `main`

```ttl
watr:Filter                                    # main
    sh:property [
        sh:path watr:hasProcess ;
        sh:qualifiedValueShape [ sh:class watr:Process-Filtration ] ;
        sh:qualifiedMinCount 1 ;
        sh:qualifiedMaxCount 1 ;
    ] .
```

### Current modeling

A real filter backwashes, a digester mixes, an SBR aerates and settles. The
`sh:qualifiedMaxCount 1` caps how many processes from a constrained family a
piece of equipment may carry, so a filter cannot claim two filtration-family
processes.

In the other direction the requirement says "performs *at least* filtration",
which is right — but it means nothing objects to this:

```ttl
:contact-basin a watr:ChlorinationUnit ;
    watr:hasProcess watr:Process-Chlorination ,
                    watr:Process-ReverseOsmosis .   # nobody complains
```

Too tight to describe real equipment, too loose to catch a nonsensical model.

### The fix on this branch

The cap is gone, and a family declares what it may *also* do:

```ttl
watr:Filter
    watr:mayAlsoPerform watr:Process-Cleaning ;      # backwash, air scour, purge
    sh:property [
        sh:path watr:hasProcess ;
        sh:qualifiedValueShape [ sh:class watr:Process-Filtration ] ;
        sh:qualifiedMinCount 1 ;
    ] .

watr:Reactor
    watr:mayAlsoPerform watr:Process-Mixing, watr:Process-Aeration,
                        watr:Process-Recirculation ;
    watr:mayAlsoPerform watr:Process-Nitrification, watr:Process-Denitrification,
                        watr:Process-EnhancedBiologicalPhosphorusRemoval .
```

`watr:ProcessPlausibilityShape` warns about any value outside the union of what
an instance's class and its ancestors require or permit. A membrane may now be
backwashed and a digester mixed, while the chlorination unit above is finally
told that reverse osmosis is not something it does.

Declaring this on the abstract families is enough: `watr:AnaerobicDigester` needs
no statement of its own, since mixing reaches it through `watr:Reactor` and
biogas through `watr:Digester`. Add one to a specific class only when it does
something its family does not.

### Warning, not violation

Implausible is not impossible. Every finding here is `sh:Warning`, so an unusual
piece of equipment is reported without making the model invalid.

It also means a disagreement between two checks can go unnoticed. This check and
the train coverage check of §5 initially conflicted: coverage expects a
nutrient-removal train's zones to declare nitrification and denitrification, and
plausibility flagged those declarations because no family permitted them. Both
being warnings, nothing failed, so every correctly modelled train emitted a
spurious warning per zone. `watr:Reactor` carries the three biological
conversions above for that reason.

---

## 4. What equipment is *for*, versus what it *does*

This is the largest change on the branch.

### On `main`

```ttl
watr:SedimentationTank                         # main
    rdfs:comment "A tank used to remove solids from liquids through sedimentation" ;
    rdfs:subClassOf watr:SeparationTank ;
    sh:property [
        sh:path watr:hasProcess ;
        sh:qualifiedValueShape [ sh:class watr:Process-Sedimentation ] ;
        sh:qualifiedMinCount 1 ;
    ] .

watr:Thickener                                 # main -- no requirement at all
    rdfs:subClassOf s223:Equipment, watr:UnitProcess .

watr:GravityThickener
    rdfs:subClassOf watr:Thickener ;
    sh:property [
        sh:path watr:hasProcess ;
        sh:qualifiedValueShape [ sh:class watr:Process-Sedimentation ] ;
        sh:qualifiedMinCount 1 ;
    ] .
```

### Current modeling

Both classes end up saying the same thing, and neither says what it is for:

```ttl
:primary-clarifier a watr:SedimentationTank ;
    watr:hasProcess watr:Process-Sedimentation .

:gravity-thickener a watr:GravityThickener ;
    watr:hasProcess watr:Process-Sedimentation .
```

Two pieces of equipment with different jobs, indistinguishable in the model. An
engineer
would not say a clarifier's job *is* sedimentation — they would say its job is to
clarify, and that it does so by settling. `SedimentationTank`'s own
`rdfs:comment` says precisely that: *"remove solids from liquids through
sedimentation."* The comment names an objective the shape cannot express, because
there is one `Process-*` tree holding both objectives and activities, and
`watr:hasProcess` is the only place to put either.

The same conflation seen from the other side:

```ttl
watr:Process-Chlorination    rdfs:subClassOf watr:Process-Disinfection .
watr:Process-UVDisinfection  rdfs:subClassOf watr:Process-Disinfection .
```

`Process-UVDisinfection` names what equipment is *for*; `Process-Chlorination`
names what it *does*. Sitting side by side under one parent, they cannot be
compared and neither can be substituted for the other in a query.

### The fix on this branch

Objectives are their own vocabulary, in `water/outcomes.ttl`:

```ttl
watr:Outcome-Clarification a watr:Class, watr:Outcome-Clarification ;
    rdfs:label "Clarification" ;
    skos:definition """Production of a clarified liquid stream by removing
        suspended solids from it. The objective of every clarifier, whatever the
        stage it serves and whatever mechanism it separates by.""" ;
    rdfs:subClassOf watr:Outcome .

watr:Outcome-Thickening a watr:Class, watr:Outcome-Thickening ;
    rdfs:label "Thickening" ;
    skos:definition """Raising the solids concentration of a sludge or slurry
        while it remains pumpable. Distinguished from dewatering by the state of
        the product.""" ;
    rdfs:subClassOf watr:Outcome .
```

Thickening, dewatering and drying form one axis: the state of the product —
pumpable, a cake, dry.

BIG TODO: do we want to have validation on the *product* of a process? downstream
things would need to have the right substance associated with them.

The equipment then states both axes:

```ttl
watr:SedimentationTank
    sh:property [ sh:path watr:hasOutcome ;
                  sh:qualifiedValueShape [ sh:class watr:Outcome-Clarification ] ;
                  sh:qualifiedMinCount 1 ] ;
    sh:property [ sh:path watr:hasProcess ;
                  sh:qualifiedValueShape [ sh:class watr:Process-Sedimentation ] ;
                  sh:qualifiedMinCount 1 ] .

watr:Thickener                                 # the objective, on the family
    sh:property [ sh:path watr:hasOutcome ;
                  sh:qualifiedValueShape [ sh:class watr:Outcome-Thickening ] ;
                  sh:qualifiedMinCount 1 ] .

watr:GravityThickener                          # the mechanism, on the model
    rdfs:subClassOf watr:Thickener ;
    sh:property [ sh:path watr:hasProcess ;
                  sh:qualifiedValueShape [ sh:class watr:Process-Sedimentation ] ;
                  sh:qualifiedMinCount 1 ] .
```

The two are now distinguishable, and each says what an engineer would
say about it:

```ttl
:primary-clarifier a watr:SedimentationTank ;
    watr:hasOutcome watr:Outcome-Clarification ;   # what it is for
    watr:hasProcess watr:Process-Sedimentation ;   # what it does
    s223:hasRole    watr:Role-Primary .            # where it sits

:gravity-thickener a watr:GravityThickener ;
    watr:hasOutcome watr:Outcome-Thickening ;
    watr:hasProcess watr:Process-Sedimentation .
```

### Why two vocabularies, not one deeper tree

Because neither relation between them is a hierarchy, so no arrangement of
`rdfs:subClassOf` can hold both.

**One process serves several objectives.** Sedimentation is the mechanism in a
primary clarifier, a secondary clarifier and a gravity thickener alike. Making
`Process-Sedimentation` a subclass of any one objective would be wrong for the
other two.

**One objective is reached by several processes.** Chlorination, ozonation,
ultraviolet irradiation and thermal treatment all disinfect:

```ttl
:contact-basin a watr:ChlorinationUnit ;
    watr:hasProcess watr:Process-Chlorination ;
    watr:hasOutcome watr:Outcome-Disinfection .

:lpuv-1 a watr:UltravioletLightUnit ;
    watr:hasProcess watr:Process-UVIrradiation ;
    watr:hasOutcome watr:Outcome-Disinfection .
```

Two renames were needed before that was sayable, because the old names had the
objective baked into the activity:

```
Process-UVDisinfection       →  Process-UVIrradiation    + Outcome-Disinfection
Process-ThermalDisinfection  →  Process-ThermalTreatment + Outcome-Disinfection
```

Ultraviolet irradiation is now named for what it is, which is also why it can
serve advanced oxidation without the term lying about it.

### The third axis: role

Outcome and process are both intrinsic — on the datasheet. Role is positional:

> Move the equipment: same unit, new position in the train. If the answer
> changes, it is a role.

A gravity thickener thickens wherever you put it. Whether a clarifier is
*primary* depends entirely on what sits upstream — which is why a primary and a
secondary clarifier are identical in outcome and process and differ only in
`s223:hasRole`.

`main` had this confused in the vocabulary itself, carrying `Role-Thickening`,
`Role-Dewatering`, `Role-Stabilization`, `Role-SolidsHandling`,
`Role-NutrientRemoval`, `Role-NitrogenRemoval` and `Role-PhosphorusRemoval`
alongside process types covering the same ground. Those are retired. Aerobic /
anoxic / anaerobic stay, because they describe the regime a zone is operated in.
Primary / Secondary / Tertiary now carry definitions saying they are wastewater
treatment *stages*, each noting where this diverges from S223 —
`s223:Role-Secondary` denotes a secondary *loop*.

### `watr:achievesOutcome`

Where a process achieves the same thing wherever it is performed, the process
type says so, rather than every piece of equipment repeating it:

```ttl
watr:Process-Chlorination     watr:achievesOutcome watr:Outcome-Disinfection .
watr:Process-Denitrification  watr:achievesOutcome watr:Outcome-NitrogenRemoval .
watr:Process-Digestion        watr:achievesOutcome watr:Outcome-Stabilization .
```

This carries what the old subclass links were reaching for —
`Chlorination ⊑ Disinfection`, `Denitrification ⊑ NitrogenRemoval` — without
claiming an activity is a kind of an objective.

Most processes declare no outcome at all — filtration, sedimentation and
adsorption serve whatever objective the equipment is built for, so the objective
is stated there. Two cases are worth spelling out, because both look like
oversights and neither is.

**Nitrification and denitrification reach different objectives.**

```ttl
watr:Process-Nitrification    watr:achievesOutcome watr:Outcome-AmmoniaRemoval .
watr:Process-Denitrification  watr:achievesOutcome watr:Outcome-NitrogenRemoval .
```

`Outcome-AmmoniaRemoval` is deliberately not under `Outcome-NutrientRemoval`;
`water/outcomes.ttl` says why.

**`Process-ChemicalPrecipitation` declares nothing.** Lime softening, phosphorus
precipitation and acid mine drainage treatment are one activity aimed at
different constituents, so which objective applies depends on the reagent and the
target. The objectives it may serve are all named, so the equipment has something
to point at, and all are left unwired to the process: `Outcome-Softening`,
`Outcome-PhosphorusRemoval`, `Outcome-MetalsRemoval`, `Outcome-SulfateRemoval`
and `Outcome-SilicaRemoval`.

`watr:OutcomeCompletenessShape` reads these and warns when equipment performs a
process whose objective it has not stated. It runs in that direction only: the
converse, demanding every stated objective be achieved by some stated process,
would be wrong, since most objectives are not derivable from the mechanism. That
is the whole reason they are a separate axis.

Run against `examples/union-dpr-model.ttl` it produces one warning, and it is a
true one — `dpr:ozone-generator` performs ozonation, which disinfects, and the
model does not say so.

### Keeping the axes apart

```ttl
watr:ProcessValueShape   sh:targetObjectsOf watr:hasProcess ; sh:class watr:Process .
watr:OutcomeValueShape   sh:targetObjectsOf watr:hasOutcome ; sh:class watr:Outcome .
```

An objective written on `watr:hasProcess`, or an activity on `watr:hasOutcome`,
is a violation rather than a silent mismodelling.
`watr:OutcomeRequiresProcessShape` additionally rejects equipment that says what
it is for without saying what it does, and `watr:ProcessBearerShape` keeps both
predicates on `s223:Equipment` or `s223:System`.

### Materializing defaults from the class

Typing something as a `watr:GravityThickener` already says it thickens by
settling. `water/class-defaults.ttl` holds a SHACL-AF rule that fills that in:

```ttl
ex:gt a watr:GravityThickener .
#  ->  watr:hasProcess watr:Process-Sedimentation   (from GravityThickener)
#      watr:hasOutcome watr:Outcome-Thickening      (inherited from Thickener)
```

One rule rather than one per class: it reads the values out of the
`sh:qualifiedValueShape` constraints the classes already carry, so adding a
requirement extends it automatically. Its semantics are *default*, not additive —
a class requiring `Process-Filtration` adds nothing to an instance already
declaring `Process-Microfiltration`, because the specific value already answers
the general requirement.

**The file ships inside the import closure**, imported by `water/ontology.ttl`,
so the rule fires wherever the ontology is used. `shifty.validate` runs SHACL-AF
rules as part of validation, so it fires *before* the constraints are checked and
satisfies them itself: a bare `ex:gt a watr:GravityThickener` stops being
reported as incomplete. That is what derivation means rather than a fault in the
rule, but it costs the ability to tell a model that *states* what a piece of
equipment does from one that merely types it. That distinction is recoverable
rather than lost: validate against the closure with `watr:ClassDefaultsRule`
removed, which is what `tests/test_class_defaults.py` does to pin the cost
alongside the benefit.

---

## 5. Treatment trains that were only labels

### On `main`

```ttl
watr:Process-A2O a watr:Class, watr:Process-A2O ;
    rdfs:label "Anaerobic-Anoxic-Oxic (A2O)" ;
    rdfs:subClassOf watr:Process-ActivatedSludge ;
    rdfs:subClassOf watr:Process-Nitrification ;
    rdfs:subClassOf watr:Process-Denitrification .
```

### Current modeling

This says an A2O process *is a kind of* nitrification. It is not — it *comprises*
nitrification, among several stages spread across several tanks. No single
piece of equipment performs an A2O, which is why no equipment class on `main`
requires one.

The reading is not merely infelicitous, it is load-bearing. Any check of the form
"does anything here nitrify?" is answered by the compound claim itself, so a
train that claims A2O and contains nothing that nitrifies looks complete.

### The fix on this branch

The family relation stays; the decomposition moves to its own predicate:

```ttl
watr:Process-A2O a watr:Class, watr:Process-A2O ;
    watr:includesProcess watr:Process-Nitrification ;
    watr:includesProcess watr:Process-Denitrification ;
    watr:includesProcess watr:Process-EnhancedBiologicalPhosphorusRemoval ;
    watr:includesProcess watr:Process-Recirculation ;
    watr:achievesOutcome watr:Outcome-NitrogenRemoval ,
                         watr:Outcome-PhosphorusRemoval ;
    rdfs:subClassOf watr:Process-ActivatedSludge .
```

A train is asserted on the `s223:System`, and its members carry the steps:

```ttl
:A2O a s223:System ;
    s223:hasMember :anaerobicZone, :anoxicZone, :aerobicZone, :finalClarifier ;
    watr:hasProcess watr:Process-A2O .

:anoxicZone a watr:MixingBasin ;
    s223:hasRole watr:Role-Anoxic ;
    watr:hasProcess watr:Process-Mixing, watr:Process-Denitrification .
```

`watr:hasProcess` is therefore valid on an `s223:System` as well as on equipment
— which is also how a backwash system is modelled, since a backwash pump only
pumps and a backwash tank only holds water, and backwashing is what the assembly
does.

### Why this works

`watr:SystemProcessCoverageShape` can now ask the question the subclass form made
unanswerable: for each step the claimed process includes, does anything in the
system perform it?

```sparql
$this watr:hasProcess ?claimed .
?claimed rdfs:subClassOf*/watr:includesProcess ?missing .
FILTER NOT EXISTS {
    $this s223:hasMember* ?performer .
    ?performer watr:hasProcess ?actual .
    ?actual rdfs:subClassOf* ?missing .
}
```

`hasMember*` rather than `hasMember+`: the zero-length match lets a train state a
step directly, and the transitive part reaches nested subsystems. Findings are
warnings, so a train may be described before every member has been entered.

`Process-ActivatedSludge` includes `Process-SolidLiquidSeparation` — the family,
not sedimentation specifically — so a membrane bioreactor satisfies the step with
microfiltration, a DAF with flotation and a centrifuge with centrifugation, while
a bar screen and an air stripper, which are separations of something else, do
not.

---

## 6. Why two checks are SPARQL and the rest are not

Most of the shapes above are core SHACL. Two are not, and neither can be:

**Plausibility** needs the union of what a class *and all its ancestors* permit.
SHACL composes constraints conjunctively — were `watr:Tank` to declare
"permitted = {Cleaning}" and `watr:Reactor` "permitted = {Mixing, Aeration, …}",
both would apply to a reactor independently and both would have to hold, making
the effective permission set the *intersection*, which is empty.

**Coverage** needs correlated quantification: for each step derived from one
path, a witness on another. No core constraint component pairs two paths that
way; `sh:equals` and `sh:disjoint` compare value sets wholesale.

`sh:rule` does not avoid this. A rule could materialize the answer for a trivial
core constraint to check, but computing it needs the same traversal, and rules
would make validation depend on an inference pass having run — which these checks
currently do not.

One practical note, since no test would catch a regression: binding `sh:path` to
a **constant** in these queries is an index lookup, while a `VALUES` or `FILTER`
over a `?path` variable materializes every property shape in the closure first,
and was at one point the dominant cost of validating a large model.

---

## 7. Tests and tooling

`main` has four test functions, one per file, parametrized over the example
graphs. The branch adds modules that state the domain claims directly, so a
reader can check them against what plants do rather than against the shapes.
`tests/test_process_plausibility.py` writes the permission table out as accepted
and flagged pairings — a BAF aerating and a membrane backwashing on one side, a
chlorination unit doing reverse osmosis on the other.
`tests/test_system_processes.py` covers the bearer and value guards, train
coverage over nested subsystems, and the outcome/process contract in both
directions. `tests/test_class_defaults.py` pins the materialization rule, what
shipping it in the import closure buys, and how the distinction it costs is
recovered.

Tooling: `pyontoenv` 0.5.3 → 0.6.0 and `pyshifty` 0.2.4 → 0.2.7, with
`conftest.py` moved to the `OntoEnv.create(...)` context-manager API;
`testpaths = ["tests"]` so collection no longer descends into the vendored
`223standard` directory; OntoEnv persists offline mode with a long cache TTL to
prevent stale re-fetches. `scripts/build_llms_txt.py` generates `llms.txt` from
the Jupyter Book table of contents.

`scripts/ttl-to-md.py` now renders the process and outcome vocabularies too, and
accepts `skos:definition` where a class has no `rdfs:comment` — those two files
use it, so neither had ever appeared in `docs/reference/`.

---

## Open items

1. **`watr:Role-Backwash` is deprecated, not deleted.**
   `examples/union-dpr-model.ttl` asserts it on `dpr:backwash-dosing-pump` and
   `dpr:backwash-tank`, which are *also* `s223:hasMember` of
   `dpr:backwash_subsystem` — the redundancy being the argument for putting the
   process on the system in the first place. Migration is one
   `watr:hasProcess watr:Process-Backwashing` on the subsystem and two triples
   deleted. That file is currently untracked yet gates the test suite, which is
   worth resolving on its own.

2. **Most equipment classes still state no outcome.** Only `Thickener`,
   `DewateringUnit`, `DisinfectionUnit`, `Digester` and `SedimentationTank`
   require one. An RO membrane and a sand filter both have objectives the model
   can now express — `Outcome-Desalination`, `Outcome-TurbidityRemoval` — and do
   not state.

3. **`watr:entailsProcess` and friends** remain proposed only, recorded in
   `water/notes.md`: renaming `watr:UnitProcess` → `watr:TreatmentUnit`,
   inference for processes that are a natural consequence of another, system
   subclasses, and plausibility checking for systems. The first depends on
   whether Aquarium can rely on an inference step running — the same question the
   defaults rule in §4 raises.
