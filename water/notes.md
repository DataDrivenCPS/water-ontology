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

Process, role, and system
-------------------------
watr:hasProcess states an activity or treatment outcome performed by equipment
or a system. s223:hasRole states how an entity can serve within a system. S223
roles describe capabilities rather than the active state at a particular time.

WaTr roles cover treatment stages, zone capabilities, operational purposes, and
connection-point purposes. A swing zone may carry both Role-Aerobic and
Role-Anoxic; its active regime belongs on a time-varying property.

watr:Role-Primary and watr:Role-Secondary refer to wastewater treatment stages.
s223:Role-Primary and s223:Role-Secondary refer to primary and secondary loops.

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
Process-ActivatedSludge includes Process-Separation, which is satisfied by
sedimentation in a conventional train or by microfiltration/ultrafiltration in an
MBR. Recirculation is configuration-specific and is declared on MLE, A2O, UCT
(by inheritance), and the Bardenpho processes rather than on ActivatedSludge.
watr:SystemProcessCoverageShape then warns when a system claims a compound process
but neither it nor any member (hasMember*, so nested subsystems count and the
system itself counts) performs one of the steps. Warning, not violation: a model
may describe the train before every member is entered.

A compound process uses rdfs:subClassOf for its process family and
watr:includesProcess for its constituent steps. It is not a subclass of those
steps.

Outcome + mechanism, when the child does not refine the parent
-------------------------------------------------------------
The refinement pattern only works when the child's process is an rdfs:subClassOf
the parent's, so one value satisfies both slots. Thickeners are the exception:
Process-Thickening names the outcome, Process-Filtration the mechanism, and they
are siblings under Process-Separation. An instance carries both.

  Thickener        -> watr:hasProcess Process-Thickening     (outcome)
    BeltThickener  -> watr:hasProcess Process-Filtration     (mechanism)
  DewateringUnit   -> watr:hasProcess Process-Dewatering     (outcome)
    BeltFilterPress-> watr:hasProcess Process-Filtration     (mechanism)

Both requirements use sh:qualifiedValueShape so that each process can satisfy its
own slot.

A GravityBeltThickener is a BeltThickener, not a GravityThickener: gravity drains
water through a porous belt, while a conventional GravityThickener separates by
sedimentation. It therefore needs Filtration alongside Thickening, not
Sedimentation.

Digestion and composting are kinds of stabilization, so they are subclasses of
Process-Stabilization. Thickening mechanisms remain siblings of
Process-Thickening because they describe a separate axis.

Nutrient-removal outcomes may be asserted on a system while its members carry the
constituent mechanisms. Denitrification is a nitrogen-removal process;
nitrification converts nitrogen without removing it. EBPR is a
phosphorus-removal process. Chemical precipitation is not a phosphorus-removal
subclass because it also applies to other constituents.

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
