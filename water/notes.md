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
The watr:hasProcess constraint on "abstract" equipment classes (Filter, Digester,
DisinfectionUnit, SeparationTank, MediaFiltration) is expressed as a plain
sh:class + sh:minCount 1, e.g. a Filter must have at least one Process-Filtration.
Concrete subclasses (ReverseOsmosisMembrane, AnaerobicDigester, ChlorinationUnit,
SedimentationTank, RapidSandFilter, ...) narrow that with their own sh:class for
the more specific process (Process-ReverseOsmosis, etc.).

Because the specific process is an rdfs:subClassOf the general one
(Process-ReverseOsmosis -> Process-MembraneProcess -> Process-Filtration), a
single specific process on an instance satisfies BOTH the inherited general
constraint and the concrete one. The parents are effectively abstract: they
define the kind of process the equipment performs, and the concrete subclass pins
down exactly which one.

This is why BOTH the parent shapes AND the concrete subclass shapes use sh:class
+ sh:minCount 1 instead of sh:qualifiedValueShape + sh:qualifiedValueShapesDisjoint.
With disjoint qualified slots, the one specific process conforms to both the
parent's slot and the child's, and the disjoint rule forbids a value from
counting toward two sibling qualified shapes -- so the value is rejected from
both and no concrete instance can ever validate. (Empirically the disjoint flag
on the *child's* block is what fires the failure, so converting only the parent
is not enough; the children must be sh:class too.)
sh:qualifiedMaxCount 1 (already present) is what actually enforces "one process
per equipment" if that's desired; the disjoint flag is only meaningful on a
single sh:property block that has multiple sh:qualifiedValueShape siblings
(e.g. MembraneBioreactor, which requires both MF/UF and Biofiltration).

Purpose goes on the role axis, not the process axis
---------------------------------------------------
The refinement pattern above only works when the child's process is an
rdfs:subClassOf the parent's, so that one value satisfies both. It broke for
thickeners and dewatering units, where the parent named a *purpose*
(Process-Thickening, Process-Dewatering) and the child named the *mechanism* that
achieves it (Process-Filtration, Process-Centrifugation). Those are siblings, not
subclasses, so an instance had to carry both values -- which a bare sh:class
cannot express, because it has to hold for EVERY watr:hasProcess value.

Rather than work around that in the shapes, the purposes were moved to the axis
that already models function: s223:hasRole. Process-Thickening and
Process-Dewatering are gone; watr:Role-Thickening and watr:Role-Dewatering
(both rdfs:subClassOf watr:Role-SolidsHandling) replace them.

  Thickener        -> s223:hasRole watr:Role-Thickening      (purpose)
    BeltThickener  -> watr:hasProcess Process-Filtration     (mechanism)
  DewateringUnit   -> s223:hasRole watr:Role-Dewatering      (purpose)
    BeltFilterPress-> watr:hasProcess Process-Filtration     (mechanism)

watr:hasProcess therefore carries mechanisms only. This keeps the refinement
invariant in tests/test_processtype_consistency.py strict: a subclass must refine
the process its ancestors require, and a failure there now signals that a purpose
has been modeled as a process type by mistake.

Two slots in this family stay qualified rather than bare sh:class:

- The role slots, because equipment may carry other, unrelated roles
  (Role-Primary, Role-SolidsHandling, ...) and a bare sh:class would reject them.
  This holds for every s223:hasRole constraint, and sh:in fails the same way:
  AerationBasin and MixingBasin state their required role as a qualified sh:in
  for this reason, so a basin can also be Role-Primary, Role-Detention, etc.
- The mechanism slots on the concrete subclasses, because multiple inheritance
  can combine two mechanisms: GravityBeltThickener is both a BeltThickener and a
  GravityThickener, so it needs Filtration AND Sedimentation. A bare sh:class on
  either parent would demand every process be its own kind and reject the other.

The general rule: use a bare sh:class only where every watr:hasProcess value must
be of that kind (the abstract families -- Filter, Digester, SeparationTank).
Where a class asserts "performs at least this mechanism", use
sh:qualifiedValueShape + sh:qualifiedMinCount 1, with NO
sh:qualifiedValueShapesDisjoint. Note the qualified form drops the upper bound;
add sh:qualifiedMaxCount 1 per slot if "exactly one of each" is wanted.

One exception to that rule is watr:ElectroDialyticCrystallizer, which carries two
bare sh:class constraints (Process-Electrodialysis and Process-Crystallization)
that look mutually unsatisfiable. They are fine, because
Process-ElectroDialyticCrystallization is an rdfs:subClassOf both, so one value
satisfies both. There is a comment in equipment.ttl saying so.

Guards against this whole family of mistakes
--------------------------------------------
Two checks exist so these do not have to be caught by eye:

1. watr:ProcessAndRoleConstraintsReferenceDefinedClasses (in ontology.ttl) is a
   SHACL shape, so tests/test_validation.py's "the ontology validates against
   itself" test enforces it. It flags a watr:hasProcess or s223:hasRole
   constraint naming a class that is defined nowhere in the import closure --
   the leftover of a rename. Such a shape still parses, but no value can ever
   carry the missing type, so the equipment silently becomes impossible to
   validate. It caught two live cases when it was added: watr:Boiler still
   required Process-Incineration after that class was renamed to
   Process-Combustion, and watr:Tank referenced s223:Role-Overflow, which S223
   does not define (WaTr now defines watr:Role-Overflow next to watr:Role-Drain).

2. tests/test_processtype_consistency.py checks that a subclass refines the
   processes its ancestors require, and -- where the ancestor states its
   requirement as a bare sh:class -- that EVERY process the subclass requires
   refines it, since a bare sh:class must hold for every value on the path.

Avoid sh:qualifiedMinCount 0. It asserts nothing at all: it reads as "may have
one of these" but permits any graph whatsoever. Tank's drain and overflow
constraints and Reactor's recirculation constraint were written that way and were
silently vacuous. They now say what they meant -- "if such a connection point
exists it must be a fluid outlet" -- expressed as sh:qualifiedMaxCount 0 over the
counterexample (a connection point carrying the role that is NOT a fluid outlet).
