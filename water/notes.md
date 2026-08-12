Sept 30, 2025
For modelign data quality, quality will be measured as quantifiable properties. 
We discussed not relating a property to a property, but it makes a little more sense because there is more data attached to some of these properties, like if it is a duration, how to interpret it. 

I think we have decided not to be perscriptive about encodings (e.g. using ISO standard duration).
Perhaps units will be different, or notes should be attached. Ultimately I think it probably makes more sense to bind to a property, as we do in s223
Alternative is to accept external reference or a literal, or better, constraining that to some xsd datatype so we know we can process what we have. something like 
```
  sh:property [
      sh:path s223:hasTemporalResolution ;
      rdfs:comment "" ;
      sh:or (
          [
            sh:class ref:ExternalReference ;
          ]
          [
            sh:nodeKind sh:Literal ;
          ]
          [
            sh:datatype xsd:duration ;
          ]
        ) ;
  ]
.
```

Notes on modeling of equipment June, 2024
- Fletch: Separator and Reactor are basic ways to distinguish between things
- Used an LLM for the descriptions, and checked some against pypes. Not sure exactly what the water-domain definitions for all of these things are
- Many equipment are named for the process they perform. Added "Unit" to several entries in the list to make them equipment rather than referring to a process. 
- We may want an alias system like brick for synonymous equipment types. In brick, has this been helpful? I think we can skip it or just note it in the description as well
    - A: We choose one name and make people use it
    - A: May need feedback from pilot projects on these decisions
- Should screen, sedimentation tank, and grit chamber be a subclass of some higher level class like Separator?
    - Could alternatively be described by a role like Role-Separator, like how in 223 we have roles like Condensor and Evaporator, to describe what is accomplished by heat-exchangers. I think we may want to avoid this.
    - A: Deciding when to make a subclass will be important, through discussion with teams
- Is UV light a specific UV light unit? Or could UV light be installed in some other kind of equipment?
    - UV Light, air compression, go inside reactors but should be treated as their own pieces of euqipment
- For pond, should we talk about aeration?
  - Ponds can be used for different things- e.g. aeration, settling, unsure if these deserve subclass
- Some things like a cogenerator seem a bit niche, what does a cogenerator look like, how many components does it have? Is it just an engine with a heat exchanger?
    - A: Common in wastewater, worth having
- Several are already represented in 223 like battery. Adding the water version as a subclass of the 223 version for now
    - Lots of baggage comes with the s223 version of Filter (and for that matter, several other s223 equipment classes) we probably need our own version of filter to accommodate different mediums.
- Should all of the filters be named with "filter"? Like NanofiltrationFilter? I think we are referring to something larger than the filter (which will in itself just be a membrane). So a NanofiltrationUnit will be it's own equipment, and it will contain a filter.
    - A: dependent on situation
    - A: Want to distinguish different columns
    - A: Could make superclass separator, then have all filters and related things under that - Fletch and Scott approved
    - A: may be distinguished based on particle size, other relevant properties.
    - A: next step to look at Zahi 
- Should we separate units and membranes for certain filteration systems? Should we have several types of membranes be defined like RO and Ion Exchange, or should we just define the relevant filter system?
    - A bioactive filter both reacts and separates, should it be a subclass of reactor and separator? Do we want multi-parent subclassing like brick? or single parent like 223.
        - Single parent is my opinion if the equipment list does not grow too much beyond this.
        - A: may want roles, multiple inheritance also fine, can cross bridge when we get there
- Should we call everything equipment, system, unit? 
    - Should I avoid words like "system" in the rdfs:comments?
    - We have this issue in 223P too, should the parent to everything be s223:Equipment? 
    - some things like pond and resevoir really don't make sense to call equipment.
    - A: Scott- Asset as superclass
- Some things like evaporator have relevant roles in 223P, will we be adopting roles in addition to other features?
- We haven't really subclassed sensors in 223P. 223P relies on property information.
    - A: May want some subclass sensors, not exactly what is in Pypes most likely 
- Not sure how to describe level sensor - this is about water level in a tank? Is it a kind of volume sensor?
    - A: Would be a float sensor, could be linked to the actual property measured (e.g. volume based on dimension of tank)
- Renamed thermometer to temperature sensor.
- Are Run Time and Run Status real sensors? In 223 sensors all represent the physical sensors rather than a virtual point (like they can in brick).
    - Are we using the brick representation of sensors in this ontology, or the 223?
    - A: Sensors in pypes are not all necessarily real sensors, these are SCADA data from controllers
- Are Humidity Sensors used?
- In 223 we have separate particulate and concentration sensors. Does this also fit conventions in the water industry?
- In 223P oxygen meter would just be a concentration center that measures oxygen. Modeling it as a subclass of concentration sensor here. 
    - Do we want to have subclasses of sensors, and all sorts of validation rules to assert how they should be modeled using 223?
- I need more info on COD/BOD sensor. Is it a single sensor? is it something only done by Sentry?
    - Changed COD/BOD to OxygenDemandSensor.
- Need to model human/manual measurements
    - A: ManualMeasurementPort, or something similar, will also want external reference flavor
- pH also a subclass of concentration sensor.
- Should all Sensors be named sensor (not meter)?
- Are Rotation, Efficiency, StateOfCharge, Speed, and Frequency true sensors?
    - What is a rotation sensor? Is it about rotational speed? What quantitykind would it have?
    - A: Will not have own sensor class, reported by controllers
- since we aren't using sameAs, all equipment borrowed from s223 should be redeclaired in nawi namespace to make querying easier.
    - Not sure if we should do something similar for properties or other concepts, since it's a little unclear what does what
    - Definitely want to reduce namespace annoyances for people querying - may want to just redeclare everything...

- is there a way to do some string processing inside templates in buildingMotif, so that I can optionally expose less inputs for the dictionary? 

- June 2, 2025 - Aside from questions about ontology management and what to subclass from 223, questions in this notees document are resolved. 
- getting rid of qudt subset file for now since its empty, though I think its probably worth having. 
- Still some confusion between roles and equipment, and if equipment can be multiclassed. For example, plug flow reactors can also be ultraviolet disinfection units. Will that be somethign that is A UltravioletUnit and A plug flow reactor, or should one of these things be moved to a role. 
- in Brick we would probably create a new class like UltraVioletDisinfectionPlugFlowReacotr. 


hasProcess modeling (abstract parents, concrete children)
----------------------------------------------------------
Every watr:hasProcess constraint in equipment.ttl is
sh:qualifiedValueShape [ sh:class ... ] + sh:qualifiedMinCount 1, with NO
sh:qualifiedValueShapesDisjoint. It reads "performs at least this process".

"Abstract" equipment classes (Filter, Digester, DisinfectionUnit, SeparationTank,
MediaFiltrationUnit) name the general kind, e.g. a Filter performs at least one
Process-Filtration. Concrete subclasses (ReverseOsmosisMembrane,
AnaerobicDigester, ChlorinationUnit, SedimentationTank, RapidSandFilter, ...) name
the specific process. Because the specific process is an rdfs:subClassOf the
general one (Process-ReverseOsmosis -> Process-MembraneProcess ->
Process-Filtration), a single specific process on an instance satisfies BOTH the
inherited general slot and the concrete one.

Qualified process constraints have no upper bound and are not disjoint, allowing
one specific process to satisfy its class's requirement and inherited general
requirements. They also allow equipment to perform additional processes.

The bare sh:class constraint on watr:UnitProcess applies to every hasProcess
value and ensures that each value is a watr:Process.

Process, treatment objective, role, and system
---------------------------------
watr:hasProcess states a physical, chemical, or biological activity performed
by equipment or a system. watr:hasTreatmentObjective states the treatment objective that
the equipment or system is intended to achieve. The two values come from
separate vocabularies: every hasProcess value is a watr:Process, and every
hasTreatmentObjective value is a watr:TreatmentObjective.

s223:hasRole states the function an entity is commissioned to serve within a
particular system, in the sense s223 gives it: a heating coil keeps Role-Heating
while it is switched off. It does not describe state at a particular time.
Process and treatment objective are intrinsic to equipment; role is installation-specific.
Class-default inference can materialize process and treatment objective requirements from an
equipment class and its ancestors, but it never supplies a role. Any applicable
role must be stated on the instance.

WaTr roles cover treatment stages, zone regimes, operational purposes, and
connection-point purposes. Role-Aerobic, Role-Anoxic and Role-Anaerobic say which
regime a zone is commissioned to run in, which is why the role slots on
AerationBasin and MixingBasin discriminate between zones of a train at all -- read
as bare capability they would be vacuous, since any basin with diffusers can be
run aerobic and any stirred basin can be run anoxic given the right feed. A swing
zone commissioned for either regime carries both Role-Aerobic and Role-Anoxic. The
dissolved oxygen at a point in time is a reading, not a role: it belongs on an
s223:QuantifiableObservableProperty of the medium, which is what a
watr:OxygenMeter observes. See examples/swing-zone-dissolved-oxygen.ttl.

watr:Role-Primary and watr:Role-Secondary refer to wastewater treatment stages.
s223:Role-Primary and s223:Role-Secondary refer to primary and secondary loops.

AerationBasin and AirStripper are two classes, not one, because air serves two
purposes. In a basin it is the oxygen supply for the biomass (Process-Aeration,
gas transfer into the water, a redox role); in a stripper it is the carrier that
sweeps ammonia and volatile organics out (Process-Stripping, a separation, no
biology). AerationBasin once carried the stripper's description alongside the
basin's constraints. A stripper does oxygenate incidentally, which is why
Process-Aeration stays permitted on it via watr:mayAlsoPerform.

Processes performed by a collection, not by a machine
----------------------------------------------------
Some processes are performed by an assembly and by no member of it. The backwash
pump only pumps, the tank only holds water; backwashing is what the collection
does. The claim therefore goes on the s223:System.

  :BackwashSystem a s223:System ;
      s223:hasMember :pump, :tank, :valve ;
      watr:hasProcess watr:Process-Backwashing .

Backwashing is represented with Process-Backwashing, a subclass of
Process-Cleaning, on the equipment or system that performs it. Role-Backwash is
deprecated.

watr:ProcessBearerShape enforces the subject boundary: hasProcess only on
s223:Equipment or s223:System. watr:ProcessValueShape enforces the object
boundary: every value is a watr:Process. Shapes rather than rdfs:domain/range
deliberately -- axioms would *infer* types onto invalid data instead of rejecting
it.

watr:includesProcess
--------------------
watr:includesProcess records what a compound process decomposes into, stated once
on the process type rather than per model. It may name a process family:
Process-ActivatedSludge includes Process-SolidLiquidSeparation, which is satisfied
by sedimentation in a conventional train, microfiltration/ultrafiltration in an
MBR, flotation in a DAF and centrifugation in a centrifuge. It deliberately does
not name Process-Separation, the family above: screening and stripping are
separations too, and neither is the step in which a train parts its biomass from
the treated water. Flotation and Centrifugation sat outside the separation family
entirely until that step was tightened, so the two mechanisms the family most
needed were the two it did not cover.

Solid-liquid separation cuts across filtration rather than containing it.
Process-Filtration is a Process-Separation, and Process-MembraneProcess is a
Process-Filtration, but reverse osmosis and membrane distillation retain
dissolved species rather than suspended ones, so the family as a whole is not a
solid-liquid separation. The subtypes that do part solids from liquid --
MediaFiltration, Microfiltration, Ultrafiltration -- declare both parents. That
is what lets an MBR satisfy the activated-sludge separation step with its
membrane while an RO train does not. Recirculation is configuration-specific and is declared on MLE, A2O, UCT
(by inheritance), and the Bardenpho processes rather than on ActivatedSludge.
watr:SystemProcessCoverageShape then warns when a system claims a compound process
but neither it nor any member (hasMember*, so nested subsystems count and the
system itself counts) performs one of the steps. Warning, not violation: a model
may describe the train before every member is entered.

A compound process uses rdfs:subClassOf for its process family and
watr:includesProcess for its constituent steps. It is not a subclass of those
steps.

TreatmentObjective and process
-------------------
What equipment is for and what it does are separate vocabularies. watr:TreatmentObjective-*
names objectives, watr:Process-* names activities, and no term is both. Neither
relation between them is a hierarchy, which is why one tree could not hold both:

  one process, several treatment objectives    a primary clarifier, a secondary clarifier and
                                   a gravity thickener all sediment
  one treatment objective, several processes   chlorination, ozonation, UV irradiation and
                                   thermal treatment all disinfect

Both axes are intrinsic and survive the P&ID test. What moves with position is
the role: a primary and a secondary clarifier share treatment objective and process, and
differ in their stage.

watr:hasTreatmentObjective states the objective on a piece of equipment or a system.
watr:hasProcess states the activity. watr:ProcessValueShape and
watr:TreatmentObjectiveValueShape keep the vocabularies apart in both directions;
watr:TreatmentObjectiveRequiresProcessShape rejects equipment that says what it is for
without saying what it does.

watr:achievesTreatmentObjective
--------------------
Class-level: what a process achieves wherever it is performed, stated once on the
process type instead of on every machine.

  Process-Nitrification    -> TreatmentObjective-AmmoniaControl
  Process-Denitrification  -> TreatmentObjective-NitrogenRemoval
  Process-EBPR             -> TreatmentObjective-PhosphorusRemoval
  Process-Digestion        -> TreatmentObjective-Stabilization
  Process-Composting       -> TreatmentObjective-Stabilization, TreatmentObjective-BiosolidsDisposal
  Process-ChlorineDosing     -> TreatmentObjective-Disinfection
  Process-UVIrradiation    -> TreatmentObjective-Disinfection
  Process-Ozonation        -> TreatmentObjective-Disinfection
  Process-ThermalTreatment -> TreatmentObjective-Disinfection
  Process-HighDensitySludge -> TreatmentObjective-Neutralization
  Process-ActivatedSludge  -> TreatmentObjective-OrganicsRemoval
  Process-FluidizedBedIncineration    -> TreatmentObjective-BiosolidsDisposal
  Process-MultipleHearthIncineration  -> TreatmentObjective-BiosolidsDisposal
  Process-AO / MLE / FourStageBardenpho    -> TreatmentObjective-NitrogenRemoval
  Process-A2O / UCT / FiveStageBardenpho   -> TreatmentObjective-NitrogenRemoval,
                                              TreatmentObjective-PhosphorusRemoval

Incineration declares TreatmentObjective-BiosolidsDisposal but its parent Process-Combustion
does not: combustion also covers burning biogas for energy, which disposes of
nothing. The other two disposal routes are not processes at all -- landfilling and
land application name where the biosolids end up rather than an activity, so they
are TreatmentObjective-Landfill and TreatmentObjective-LandApplication.

Most processes declare no treatment objective; filtration and sedimentation serve whatever
objective the equipment is built for. Two cases are worth spelling out.

Process-Nitrification -> TreatmentObjective-AmmoniaControl, NOT TreatmentObjective-NitrogenRemoval.
TreatmentObjective-AmmoniaControl is deliberately not under TreatmentObjective-NutrientRemoval; the
comment on it in treatment objectives.ttl says why.

Process-ChemicalPrecipitation declares nothing: which constituent it targets
depends on the reagent, so the treatment objective belongs on the equipment. The objectives
it may serve are named so the equipment has something to point at --
TreatmentObjective-Softening, TreatmentObjective-PhosphorusRemoval, TreatmentObjective-MetalsRemoval,
TreatmentObjective-SulfateRemoval, TreatmentObjective-SilicaRemoval -- and all are left unwired. Lime
softening, phosphorus precipitation and acid mine drainage treatment are one
activity aimed at different targets.

Which equipment classes require a treatment objective
------------------------------------------
Two grounds, and the second is the harder one.

The first is mechanical: if a class requires a process that declares
watr:achievesTreatmentObjective, the class states that treatment objective, or watr:TreatmentObjectiveCompletenessShape
reports every instance of it. OxidationDitch and SequencingBatchReactor require
Process-ActivatedSludge and now state TreatmentObjective-OrganicsRemoval; OzonationUnit
became a DisinfectionUnit, which is what ChlorinationUnit and UltravioletLightUnit
already were.

The second is the datasheet test: require a treatment objective only where the class fixes
it, not where the installation does. An RO membrane rejects salt wherever it is
plumbed (TreatmentObjective-Desalination), an electrodialysis stack likewise, a media bed
polishes turbidity (TreatmentObjective-TurbidityRemoval, inherited by the sand filters),
nanofiltration softens, a GAC adsorber takes out dissolved organics, an AOP
reactor destroys them, and a screen and a grit chamber take out solids.

Deliberately left unstated, because the objective moves with the installation:

  Filter                 a media bed polishes, an MBR's membrane separates
                         biomass, an RO membrane desalinates
  MicrofiltrationUnit,   turbidity removal in a drinking water train,
  UltrafiltrationUnit    clarification of mixed liquor in an MBR
  TricklingFilter,       organics removal, nitrification or denitrification,
  MovingBedBioreactor,   depending on the stage and the operating regime --
  RotatingBiological-    which is also why Process-Biofiltration declares no
  Contactor, BAF         treatment objective
  CoagulationBasin,      they condition the water; the clarifier downstream is
  FlocculationBasin      what meets the objective
  AerationBasin,         a zone of a train, serving the train's objective
  MixingBasin
  Crystallizer,          brine handling, where the objective is the
  Evaporator             configuration's rather than the vessel's

Renamed on the split
--------------------
Process-UVDisinfection  -> Process-UVIrradiation    + TreatmentObjective-Disinfection
Process-ThermalDisinfection -> Process-ThermalTreatment + TreatmentObjective-Disinfection
Process-Dechlorination  -> TreatmentObjective-Dechlorination   (no replacement process)

The first two had baked the objective into the name of the activity, which made
UV and chlorination incomparable: one named what it was for, the other what it
did.

Dechlorination went further and was only an objective, so nothing was left to
rename it to. It is the clearest one-treatment objective-several-processes case in the
vocabulary: sulfite dosing reduces the residual, activated carbon adsorbs and
catalyses it, ultraviolet light photolyses it. A dechlorination unit states the
activity it uses and TreatmentObjective-Dechlorination.

Solids handling
---------------
The objective is the state of the product; the process is how the water is taken
out. One process serves all three objectives, which is why they are on different
axes.

  Thickener      -> watr:hasTreatmentObjective TreatmentObjective-Thickening
  DewateringUnit -> watr:hasTreatmentObjective TreatmentObjective-Dewatering
  TreatmentObjective-Drying is a subclass of TreatmentObjective-Dewatering.

  GravityThickener               -> watr:hasProcess Process-Sedimentation
  BeltThickener, RotaryDrumThickener, GravityBeltThickener, BeltFilterPress
                                 -> watr:hasProcess Process-Filtration
  CentrifugalThickener, CentrifugalDewateringUnit
                                 -> watr:hasProcess Process-Centrifugation
  DissolvedAirFlotationThickener -> watr:hasProcess Process-Flotation

Any class may require a treatment objective, a process, or both. These families put the
treatment objective on the parent and the process on the subclass because there the objective
is common and the mechanism varies; that is an organizing choice, not a rule.
watr:SedimentationTank states both itself -- TreatmentObjective-Clarification and
Process-Sedimentation -- as does watr:Digester, with TreatmentObjective-Stabilization and
Process-Digestion.

Materializing class defaults (water/class-defaults.ttl)
------------------------------------------------------
Typing something as a watr:GravityThickener already says it thickens by settling.
A SHACL-AF rule writes that onto the instance, reading the values from the
sh:qualifiedValueShape constraints the classes already carry, so nothing has to
be kept in step:

  ex:gt a watr:GravityThickener .
    ->  watr:hasProcess watr:Process-Sedimentation   (from GravityThickener)
        watr:hasTreatmentObjective watr:TreatmentObjective-Thickening      (from Thickener)

Default semantics, not additive: a class requiring Process-Filtration adds
nothing to an instance already declaring Process-Microfiltration.

The file is INSIDE the import closure: water/ontology.ttl imports
<urn:nawi-water-ontology/class-defaults>, so the rule ships with the ontology and
fires wherever it is used. That is deliberate. shifty.validate runs SHACL-AF
rules as part of validation (infer=True by default), so the rule fires before the
constraints are checked and satisfies them itself: a bare
"ex:gt a watr:GravityThickener ." goes from five violations to zero.

Know what that costs. A class's process and treatment objective requirements can no longer
fail for an instance that merely declares its type, so the ontology no longer
distinguishes a model that states what a machine does from one that only types
it. If you need that distinction -- when the data comes from a plant rather than
from the ontology -- validate against the closure with watr:ClassDefaultsRule
removed. tests/test_class_defaults.py does exactly that, and pins both what
including the rule buys and what removing it restores.

Why equipment carries more than one process
------------------------------------------
Two patterns remain, and both keep every value on watr:hasProcess.

Refinement. The child's process is an rdfs:subClassOf the parent's, so one value
satisfies both slots: ReverseOsmosisMembrane requires Process-Filtration from
Filter and Process-ReverseOsmosis of its own. One axis stated at two levels.

Co-occurrence. Several activities in one vessel, none the means to another: a
SequencingBatchReactor aerates and settles in successive phases; an
ElectroDialyticCrystallizer performs a process that subclasses both
crystallization and electrodialysis.

Requirements from ancestors combine conjunctively, as everywhere in SHACL.

A GravityBeltThickener is a BeltThickener, not a GravityThickener: gravity drains
water through a porous belt, while a conventional GravityThickener separates by
sedimentation. Its process is therefore Filtration, inherited from BeltThickener,
not Sedimentation.

Nutrient-removal treatment objectives may be asserted on a system while its members carry the
processes that reach them.

Role slots are qualified for a related reason: equipment carries other unrelated
roles (Role-Primary, ...) and a bare sh:class would reject them. sh:in fails the
same way, which is why AerationBasin and MixingBasin state their required role as
a qualified sh:in.

Structural guards
-----------------
Two checks enforce the process and role constraints:

1. watr:ProcessAndRoleConstraintsReferenceDefinedClasses flags a watr:hasProcess
   or s223:hasRole constraint naming a class that is not defined in the import
   closure, including members of direct and qualified sh:in lists.

2. The process-type consistency test checks that a subclass refines processes
   required by its ancestors.

Optional drain, overflow, recirculation, and return points are constrained by
permitting zero nonconforming points. A matching point, when present, must be a
fluid outlet.

Plausibility of additional processes (watr:mayAlsoPerform)
----------------------------------------------------------
watr:mayAlsoPerform lists processes that an equipment class can plausibly perform
in addition to its requirements. watr:ProcessPlausibilityShape warns about values
outside the union of processes required or permitted by the class and its
ancestors.

Declared on the abstract families only; subclasses inherit:

  Tank            -> Process-Cleaning
  Reactor         -> Process-Mixing, Process-Aeration, Process-Recirculation
                     Process-Nitrification, Process-Denitrification,
                     Process-EnhancedBiologicalPhosphorusRemoval
  SeparationTank  -> Process-Recirculation
  Filter          -> Process-Cleaning
  Digester        -> Process-GasTransfer   (mixing comes from Reactor)

Digester and DisinfectionUnit are both Reactor subclasses, so digester mixing and
contact-basin mixing need no statement of their own. Add one to a specific class
only when it does something its family does not.

The three biological conversions on Reactor are what makes the permission table
agree with the coverage check. A nutrient-removal train states its compound
process on the system, watr:includesProcess expands it into those conversions,
and SystemProcessCoverageShape looks for them on the members. They are permitted
rather than required because which zone nitrifies or denitrifies is an operating
regime, not a property of the vessel: the same basin serves as an anoxic or an
aerobic zone depending on how it is run.

ProcessPlausibilityShape is a warning-level SHACL-SPARQL constraint. It combines
requirements and permissions across all equipment ancestors. Systems are not
subject to this equipment-family plausibility table.

watr:MovingBedBioreactor and watr:RotatingBiologicalContactor are both Reactors
and Filters. They inherit filtration requirements from Filter and the additional
mixing, aeration, and recirculation permissions from Reactor.

What watr:Tank means
--------------------
watr:Tank identifies a flow-through vessel pattern: at least one fluid inlet and
one fluid outlet, with constraints for optional drain and overflow points. It
does not assert geometry. watr:Reactor is a subclass of watr:Tank, so tubular
reactors and in-line mixers inherit the same connection-point pattern.
