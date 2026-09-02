# Treatment model: what the ontology defines, what units inherit, what the modeler writes

**Status:** design proposal, written after the review of PR #39. This document
describes the model we intend to implement. The branch does not implement it
yet. Sections 1 through 7 and the example in section 9 are the target design,
including class names, defaults, and inference rules that do not exist on the
branch today.
[treatment_model_work.md](treatment_model_work.md) lists what has to change on
the branch to match this document.

## 1. The model

- **Two layers.**
  - The ontology defines the vocabulary: equipment classes, processes, treatment objectives, and roles. WaTr maintains it. A plant modeler never edits it.
  - The plant model describes one plant. A modeler writes it. It contains the plant's units, systems, and connection points. Each one is typed with an equipment class from the ontology and annotated with processes, objectives, and roles from the ontology.
- **Each attribute below says who fills it in.** There are three possibilities.
  - *Defined by the ontology:* WaTr wrote the value into the vocabulary. Used in section 1a.
  - *Inherited from the class* or *inherited from the process:* inference copies the value onto the instance from its equipment class or from a process it performs. The modeler does not write anything. Used in section 1b.
  - *Added by the modeler:* the modeler must write the value in the plant model, because the ontology does not know it or because the ontology allows more than one option.

Section 1a lists the things in the ontology and their attributes. Section 1b lists the things in a plant model and their attributes.

## 1a. The ontology

### Equipment class

An equipment class is a kind of treatment equipment: `watr:SedimentationTank`, `watr:GravityThickener`, `watr:ReverseOsmosisMembrane`. Equipment classes live in the ontology. Each class carries requirements that apply to every unit of that class.

- `rdfs:subClassOf` → another equipment class. This means "is a kind of." Equipment classes form a hierarchy. A class inherits every requirement below from every class above it. `watr:GravityThickener` is a kind of `watr:Thickener`, so gravity thickeners carry every requirement the ontology puts on thickeners, including the thickening objective.
  - *Defined by the ontology.*
- Required process → a [Process](#process). The process that every unit of this class performs. A sedimentation tank settles solids by gravity. A filter passes water through a medium that retains particles. Some classes name only a family of processes, and leave the specific one open: `watr:Filter` requires "some kind of filtration." Some classes name no biological process at all: `watr:MixingBasin` requires only mixing, because whether a given basin denitrifies is up to the plant.
  - *Defined by the ontology.* The ontology writes this as a SHACL constraint on `watr:hasProcess`.
- Design objective → a [Treatment objective](#treatment-objective). The result that every unit of this class is built to produce. Every thickener is built to concentrate sludge. Every disinfection unit is built to inactivate pathogens. Every clarifier is built to produce clarified water. A class carries a design objective only when every unit of the class is built for the same result. Many classes therefore have none, because their process produces different results in different plants: an RO membrane class does not say whether its units desalinate or remove PFAS, and a generic settling tank does not say whether the plant uses its clarified overflow or its thickened underflow.
  - *Defined by the ontology.* The ontology writes this as a SHACL constraint on `watr:hasTreatmentObjective`.
- `watr:mayAlsoPerform` → a [Process](#process). Extra processes that units of this class commonly perform in addition to the required one. Validation uses this list to avoid warning about ordinary combinations. A filter may also backwash. A reactor may also mix, aerate, and recirculate.
  - *Defined by the ontology.*
- Permitted roles → a set of [Roles](#role). On a few classes, the roles that units of the class are allowed to carry. An aeration basin may be aerobic or anoxic. A mixing basin may be anoxic or anaerobic. Most classes do not restrict roles.
  - *Defined by the ontology.* The ontology writes this as a SHACL constraint on `s223:hasRole`.

### Process

A process is what physically, chemically, or biologically happens to the water inside a unit. It describes the action, not the result. Solids settle under gravity (`watr:Process-Sedimentation`). Pressure forces water through a semipermeable membrane and leaves salts behind (`watr:Process-ReverseOsmosis`). Chlorine is dosed and reacts with the water (`watr:Process-Chlorination`). Bacteria oxidize ammonia to nitrate (`watr:Process-Nitrification`). The word "mechanism" in this document always means a process.

The test for whether a term is a process: you can describe it without saying what it removes or what it is for. "Solids settle under gravity" is a process. "Solids are removed" is a result, and belongs in the treatment objective.

- `rdfs:subClassOf` → the parent process. This means "is a kind of." Processes form a hierarchy. A specific process counts as every process above it. Reverse osmosis is a kind of membrane process, and a membrane process is a kind of filtration, so a unit that performs reverse osmosis satisfies a requirement for "some kind of filtration." A process may have two parents: media filtration is a kind of filtration and also a kind of solid-liquid separation.
  - *Defined by the ontology.*
- `watr:achievesTreatmentObjective` → a [Treatment objective](#treatment-objective). A result that this process always produces, no matter which unit performs it or in which plant. The ontology sets it only when the process name already says what result it produces.
  - *Defined by the ontology.* Denitrification always removes nitrogen, so it achieves nitrogen removal. Chlorination always disinfects, so it achieves disinfection. Sedimentation achieves nothing on its own, because the same settling produces clarified water in a clarifier and denser sludge in a thickener; there the equipment class decides.
  - Every unit and system that performs the process receives the objective automatically. The modeler writes nothing.
- `watr:includesProcess` → a [Process](#process). This applies only to compound processes, which are treatment schemes made of several steps. It lists the steps that a system must perform, across its member units, to claim the compound process.
  - *Defined by the ontology.* A2O includes nitrification, denitrification, enhanced biological phosphorus removal, and recirculation, and inherits aeration and solid-liquid separation from activated sludge. A system that claims A2O must have members that perform all of them.

### Treatment objective

A treatment objective is the result that treatment is meant to produce in the water or sludge. It describes the outcome, not the action: a constituent is reduced, pathogens are inactivated, a sludge is concentrated. Examples are `watr:TreatmentObjective-Clarification` (the liquid leaving the unit is clarified), `-Disinfection` (pathogens are inactivated), `-Thickening` (the sludge leaving the unit is denser), and `-NitrogenRemoval` (less nitrogen leaves than entered). Objectives answer "what is this unit or system for," and they are the level at which a permit limit or performance target would attach.

- `rdfs:subClassOf` → the parent objective. This means "is a kind of." Objectives form a hierarchy. A specific objective counts as every objective above it. Clarification is a kind of solids removal, so a query for everything that removes solids returns the clarifiers as well.
  - *Defined by the ontology.*
- `watr:targetsConstituent` → a [Constituent](#constituents). This applies only to constituent-removal objectives. It names the substance that the objective reduces. Nitrogen removal targets nitrogen. Softening targets hardness. Section 7 lists the constituent vocabulary and the target of every named objective.
  - *Defined by the ontology* for every named objective.
  - *Added by the modeler* only when the plant targets a constituent that has no named objective. The modeler creates a local objective typed `watr:TreatmentObjective-ConstituentRemoval` and points it at the constituent. For PFAS:

    ```ttl
    :pfasRemoval a watr:TreatmentObjective-ConstituentRemoval ;
        watr:targetsConstituent watr:Constituent-PFAS .

    :gacAdsorber a watr:GranularActivatedCarbonAdsorber ;
        watr:hasTreatmentObjective :pfasRemoval .
    ```

    A query for constituent removal returns the adsorber, and a query for what it targets returns PFAS. If the constituent itself is missing from the ontology, the modeler declares it locally as a subclass of the nearest constituent in section 7 and uses that.

### Role

A role is a position or duty that a plant assigns to a unit or a connection point. `watr:Role-Primary` means the unit serves the primary stage. `watr:Role-Anoxic` means the plant runs the zone without dissolved oxygen. `watr:Role-Equalization` means the vessel evens out flow. `s223:Role-Return` means the port carries return sludge. A role describes the unit's place in one plant, not what the unit is or what happens inside it.

- `rdfs:subClassOf` → the parent role. This means "is a kind of." Overflow is a kind of discharge. The role hierarchy is one level deep and exists only to group related roles.
  - *Defined by the ontology.*
- Roles have no other attributes. A role is a label that the modeler attaches to a unit or a connection point.

## 1b. The plant model

### Unit

A unit is one piece of treatment equipment in the plant: a specific clarifier, basin, filter, or membrane skid. Every unit is an instance of one equipment class, and inference copies that class's requirements, and its superclasses' requirements, onto the unit.

- `rdf:type` → an [Equipment class](#equipment-class). The kind of equipment this unit is.
  - *Added by the modeler:* always. Choose the most specific class that fits. Every inherited attribute below depends on this choice.
- `watr:hasProcess` → a [Process](#process). What physically, chemically, or biologically happens to the water inside this unit. Not the result; the action.
  - *Inherited from the class:* the unit receives the required process of its class. A unit typed `watr:SedimentationTank` gets sedimentation. A unit typed `watr:GravityThickener` gets sedimentation.
  - *Added by the modeler:* when the class leaves the process open. A unit typed `watr:MixingBasin` gets mixing from its class; if the plant runs it as a denitrifying zone, the modeler adds denitrification.
- `watr:hasTreatmentObjective` → a [Treatment objective](#treatment-objective). The result this unit is meant to produce in the water or sludge passing through it. Not the action; the outcome.
  - A unit may have more than one treatment objective. State every result the plant relies on.
  - *Inherited from the class:* the unit receives the design objective of its class. A unit typed `watr:GravityThickener` gets thickening. A unit typed `watr:Clarifier` gets clarification.
  - *Inherited from the process:* the unit receives the achieved objective of every process it performs. A unit that performs denitrification gets nitrogen removal. A unit that performs chlorination gets disinfection.
  - *Added by the modeler:* when neither the class nor the process fixes the result, because the same equipment serves different purposes in different plants. A unit typed `watr:ReverseOsmosisMembrane` gets reverse osmosis from its class but no objective; the modeler adds desalination, or PFAS removal, according to what this plant uses it for. A unit typed `watr:SedimentationTank` gets sedimentation but no objective; the modeler adds clarification, thickening, or both.
- `s223:hasRole` → a [Role](#role). Where this unit sits in the plant's treatment train, or what duty the plant assigned to it.
  - *Inherited:* nothing. An equipment class cannot know how a plant commissioned a particular unit. The same sedimentation tank class serves as a primary clarifier in one plant and a secondary clarifier in another.
  - *Added by the modeler:* always, whenever the unit has a stage, an operating regime, or a duty worth recording.
- There is no attribute for "helps with an objective it does not achieve alone." The aerobic zone of an A2O train nitrifies, which removes no nitrogen, yet the train's nitrogen removal depends on it. The model already records that: the zone is a member of a system whose objective is nitrogen removal. A query that wants "everything involved in nitrogen removal" follows system membership. See section 9.

### System

A system, `s223:System`, is a set of units that together carry out a compound process. A biological treatment train is a system. A return-sludge loop of a valve and a pump is a system.

- `s223:hasMember` → the units and sub-systems that belong to the system.
  - *Added by the modeler:* always.
- `watr:hasProcess` → a [Process](#process). The compound process the system as a whole carries out, such as A2O or activated sludge.
  - *Added by the modeler:* always. A system has no equipment class, so nothing is inherited. The modeler names the process.
- `watr:hasTreatmentObjective` → a [Treatment objective](#treatment-objective). The result the system as a whole is meant to produce.
  - *Inherited from the process:* the system receives the achieved objectives of its compound process. A system that performs A2O gets nitrogen removal, phosphorus removal, and organics removal.
  - *Added by the modeler:* any further objective the plant has for the system.
- Coverage check. Validation warns when the members of a system do not, between them, perform every step that the system's process includes. If a system claims A2O but no member denitrifies, the modeler sees a warning.

### Connection point

A connection point, `s223:ConnectionPoint`, is a port on a unit where a pipe or channel attaches.

- `s223:hasRole` → a [Role](#role). The purpose of this port in this plant: feed, permeate, drain, return sludge, internal recirculation.
  - *Added by the modeler:* always.

### What the modeler writes

- The equipment class of every unit. Always.
- The role of every unit and connection point that has one.
- The treatment objective, whenever it is plant intent that the class and process do not fix.
- The process, whenever the equipment class leaves a choice.
- The members and the process of every system.
- The ontology supplies everything else through inference.

## 2. The two design distinctions

The model rests on two distinctions. Each one separates two of the attributes in section 1. In the examples, `# inherited` marks a triple that inference adds, either because the unit's class carries it or because a process the unit performs always produces it. `# modeler` marks a triple the modeler writes. "Carries" means the class declares the value in the ontology, so every instance of the class inherits it.

- **Distinction 1: what the unit is versus how the plant uses it.** This separates process from role, with treatment objective in between.
  - Process belongs to the unit itself. It follows from what the unit is. It is on the equipment's datasheet. It stays the same if the unit moves to another plant. The equipment class supplies it.
  - Role belongs to the installation. The plant decides it when it commissions the unit. It changes when the plant moves or reassigns the unit. The modeler supplies it.
  - Treatment objective is intent, and intent has two sources. Some equipment is built for one result, and the class supplies the objective. Other equipment can serve more than one result, and the plant decides. See "Where the treatment objective comes from" below.
  - Test: move a clarifier from the primary stage to the secondary stage.

    ```ttl
    # modeler
    :clarifier a watr:Clarifier ;

        # inherited from watr:SedimentationTank; unchanged by the move
        watr:hasProcess watr:Process-Sedimentation ;

        # inherited from watr:Clarifier; unchanged by the move
        watr:hasTreatmentObjective watr:TreatmentObjective-Clarification ;

        # modeler; was watr:Role-Primary before the move
        s223:hasRole watr:Role-Secondary .
    ```

- **Distinction 2: what happens inside the unit versus what result it is for.** This separates process from treatment objective.
  - Process is the action: the physical, chemical, or biological thing that happens to the water. The plain-language description is the definition of the process term in the ontology. The unit carries only the term.
    - Solids settle under gravity. The ontology defines `watr:Process-Sedimentation` as that.

      ```ttl
      # modeler
      :clarifier a watr:Clarifier .

      # inherited; every watr:SedimentationTank carries it
      :clarifier watr:hasProcess watr:Process-Sedimentation .
      ```

    - Chlorine is dosed and reacts with the water. The ontology defines `watr:Process-Chlorination` as that.

      ```ttl
      # modeler
      :contactTank a watr:ChlorinationUnit .

      # inherited; every watr:ChlorinationUnit carries it
      :contactTank watr:hasProcess watr:Process-Chlorination .
      ```

    - Bacteria oxidize ammonia to nitrate. The ontology defines `watr:Process-Nitrification` as that.

      ```ttl
      # modeler
      :aerobicZone a watr:AerationBasin .

      # inherited; every watr:AerationBasin carries it
      :aerobicZone watr:hasProcess watr:Process-Aeration .

      # modeler; an aeration basin is not required to nitrify, so the class leaves this open
      :aerobicZone watr:hasProcess watr:Process-Nitrification .
      ```

  - Treatment objective is the result: the change the unit is meant to produce in the water or sludge. Again, the description is the definition of the objective term, and the unit carries only the term.
    - Sludge is concentrated. The ontology defines `watr:TreatmentObjective-Thickening` as that.

      ```ttl
      # modeler
      :thickener a watr:GravityThickener .

      # inherited; every watr:Thickener carries it
      :thickener watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .
      ```

    - Pathogens are inactivated. The ontology defines `watr:TreatmentObjective-Disinfection` as that.

      ```ttl
      # modeler
      :contactTank a watr:ChlorinationUnit .

      # inherited by two routes: from the class, because every watr:DisinfectionUnit carries it; and from the unit's own process, because the ontology says watr:Process-Chlorination always produces disinfection
      :contactTank watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection .
      ```

    - Solids are removed. The ontology defines `watr:TreatmentObjective-SolidsRemoval` as that.

      ```ttl
      # modeler
      :settler a watr:SedimentationTank .

      # inherited; every watr:SedimentationTank carries it
      :settler watr:hasProcess watr:Process-Sedimentation .

      # modeler; sedimentation serves several objectives and the generic class names none, so the plant states which
      :settler watr:hasTreatmentObjective watr:TreatmentObjective-SolidsRemoval .
      ```

  - The model keeps process and objective separate because they do not line up one to one.
    - One process serves several objectives.

      ```ttl
      :clarifier a watr:Clarifier ;

          # inherited
          watr:hasProcess watr:Process-Sedimentation ;

          # inherited from watr:Clarifier
          watr:hasTreatmentObjective watr:TreatmentObjective-Clarification .

      :thickener a watr:GravityThickener ;

          # inherited; same process
          watr:hasProcess watr:Process-Sedimentation ;

          # inherited from watr:Thickener; different objective
          watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .
      ```

    - One objective is reached by several processes.

      ```ttl
      :contactTank a watr:ChlorinationUnit ;

          # inherited
          watr:hasProcess watr:Process-Chlorination ;

          # inherited
          watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection .

      :uvUnit a watr:UltravioletLightUnit ;

          # inherited; different process
          watr:hasProcess watr:Process-UVIrradiation ;

          # inherited; same objective
          watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection .
      ```

  - The rule behind the split: a process can put out more than one stream, and the treatment objective names what the plant relies on the unit producing. Sometimes that is a choice of stream: a settling tank puts out a clarified overflow and a thickened underflow, and clarification or thickening says which one the plant uses. Sometimes it is a change to the one stream: disinfection says the plant relies on the water leaving with its pathogens inactivated. Either way, the process is a fact about the unit, and the objective is a fact about what the plant does with the output.
  - Test: if you can describe the term without saying what it removes or what it is for, it is a process. If the term names what is removed, what state the stream ends up in, or which output stream the plant relies on, it is a treatment objective. Section 4 applies this test to every contested term.
- **Where the treatment objective comes from.** A treatment objective has two possible origins, and the model treats them the same way.
  - Design intent: the equipment was built for this result. The equipment class supplies it, and the unit inherits it.

    ```ttl
    # modeler
    :thickener a watr:GravityThickener .

    # inherited; every thickener is built to concentrate sludge
    :thickener watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .
    ```

  - Plant intent: this plant uses the equipment for this result. The modeler supplies it.

    ```ttl
    # modeler
    :ro a watr:ReverseOsmosisMembrane .

    # inherited
    :ro watr:hasProcess watr:Process-ReverseOsmosis .

    # modeler; an RO membrane can desalinate seawater or remove PFAS from groundwater, and the class does not say which
    :ro watr:hasTreatmentObjective watr:TreatmentObjective-Desalination .
    ```

  - Both use `watr:hasTreatmentObjective`, because both answer "what is this unit for." Plant intent is also where a permit limit or performance target attaches, once the model supports targets.
- **A unit may have more than one treatment objective.** State every result the plant relies on.

  ```ttl
  :primaryClarifier a watr:Clarifier ;

      # inherited; the clarified overflow goes to secondary treatment
      watr:hasTreatmentObjective watr:TreatmentObjective-Clarification ;

      # modeler; this plant sends the underflow straight to digestion and relies on it being thickened
      watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .
  ```

- **Rule for when a class carries a design objective.** An equipment class carries a design objective only when every unit of that class is built for the same result. When units of a class serve different results in different plants, the class carries no objective, and the modeler states it.
  - Passes the rule: `watr:Thickener` carries `watr:TreatmentObjective-Thickening`, because every thickener concentrates sludge, so every thickener instance inherits it. `watr:DisinfectionUnit` carries `watr:TreatmentObjective-Disinfection`, because every disinfection unit inactivates pathogens, so every disinfection unit instance inherits it.
  - Generic settling vessel: `watr:SedimentationTank` carries `watr:Process-Sedimentation` and no objective. Its instances inherit the process and nothing else. A settling tank always produces both a clarified overflow and a thickened underflow. The process is a fact about the tank. Which stream the plant relies on downstream is the objective, and that is a fact about the plant.
    - `watr:Clarifier`, a subclass, is built for the clarified overflow and carries `watr:TreatmentObjective-Clarification`. Every clarifier instance inherits it.
    - `watr:GravityThickener` is built for the thickened underflow and carries `watr:TreatmentObjective-Thickening`. Every gravity thickener instance inherits it.
    - The modeler picks the class that matches the product the plant uses, or uses the generic class and writes the objective.

      ```ttl
      # modeler knows the overflow is the product; clarification is inherited
      :unitA a watr:Clarifier .

      # modeler knows the underflow is the product; thickening is inherited
      :unitB a watr:GravityThickener .

      # modeler only knows it settles
      :unitC a watr:SedimentationTank ;

          # modeler; this would need to be asserted on the sedimentation tank instance,
          # as the generic class carries no objective
          watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .
      ```

## 3. The four annotations on a unit

| question | predicate | belongs to | who supplies it | vocabulary |
|---|---|---|---|---|
| What is it? | `rdf:type` | the unit | the modeler, always | `watr:*` equipment classes |
| What does it do? | `watr:hasProcess` | the unit | inherited from the class; the modeler when the class leaves a choice | `watr:Process-*` |
| What is it for? | `watr:hasTreatmentObjective` | the unit (design intent) or the plant (plant intent) | inherited from the class and from the process; the modeler for plant intent | `watr:TreatmentObjective-*` |
| Where does it sit? | `s223:hasRole` | the plant | the modeler, always | `watr:Role-*`, `s223:Role-*` |

## 4. Three tests for placing a term

- **Mechanism test.** Can you describe it without naming what it removes or changes? Then it is a **process**.
  - Sedimentation, filtration, ozonation, chlorination, nitrification, denitrification pass.
- **Change test.** Does it name a change to the stream that more than one mechanism can produce? Then it is a **treatment objective**.
  - Solids removal, clarification, disinfection, thickening, dewatering, nitrogen removal, chlorine residual removal pass.
- **Move test.** Does it change when the plant moves or reassigns the unit without rebuilding it? Then it is a **role**.
  - Primary and secondary, the commissioned oxygen regime, return and recirculation on a connection, storage and equalization duty pass.
- **Tie-break.** Some words pass the change test but practitioners use them as process names. Keep the word as the objective. Give the mechanism its own name. The rule from section 2 decides: the process is a fact about the unit, and the objective is what the plant relies on the unit producing.
  - Clarification is the objective. Sedimentation is the process. Every settling tank settles; only some plants rely on the overflow.
  - Softening is the objective. Chemical precipitation and ion exchange are the processes.
  - An activity whose output the plant does not rely on as a product, such as backwashing, is a process with no objective.
- **Entailment rule.** Some processes always produce the same result. For those, the ontology declares `watr:achievesTreatmentObjective` on the process, and every unit that performs the process inherits the objective. The ontology declares it only when the name of the process already names the result.
  - Examples that declare one: denitrification, nitrification, chlorination, sulfite dosing, UV irradiation, digestion, composting, EBPR, incineration, land application, landfilling, and the named activated-sludge configurations. Each always produces the same result.
  - Examples that declare none: filtration, membrane processes, chemical precipitation, adsorption, and sedimentation. Each produces different results in different units, so the class or the modeler supplies the objective.

Placement of the contested terms. Each entry gives:

- *Vocabulary:* which of the three lists the term goes in.
- *Parent in the hierarchy:* the term's `rdfs:subClassOf`. A specific term counts as its parent, so a query for the parent also returns units with the specific term.
- *Objective every unit inherits:* for processes only. The `watr:achievesTreatmentObjective` the ontology declares on the process. Inference adds this objective to every unit that performs the process. "None" means the unit's objective comes from its class or from the modeler instead.
- *Basis:* whether a source supports the placement, or whether it is a decision we made. Footnotes point to section 10. Where the basis is a decision, the reasoning given is the whole justification, and the team can overrule it.

- **Sedimentation**
  - Vocabulary: process, `watr:Process-Sedimentation`
  - Parent in the hierarchy: `watr:Process-SolidLiquidSeparation`
  - Objective every unit inherits: none. It clarifies in a clarifier and thickens in a thickener, so the class or the modeler supplies the objective.
  - Why: you can describe it without naming a result. Solids settle under gravity.
  - Basis: source. Metcalf & Eddy lists sedimentation as a unit operation, defined by the physical force applied[^me]. WEF calls it "the physical process where gravity forces account for the separation"[^wef].
- **Clarification**
  - Vocabulary: objective, `watr:TreatmentObjective-Clarification`
  - Parent in the hierarchy: `watr:TreatmentObjective-SolidsRemoval`
  - Why: names a result. Sedimentation produces a clarified overflow and a thickened underflow in every tank; clarification says the plant relies on the overflow. WEF lists it as a clarifier function next to thickening.
  - Basis: source, with a caveat. WEF names clarification as one of four functions a clarifier serves, alongside thickening, with sedimentation as the process[^wef]. Metcalf & Eddy also uses "high-rate clarification" as the name of a unit operation[^me], so the word is used both ways in the literature. We follow WEF because it is the only source that separates the two.
- **Thickening, dewatering, drying**
  - Vocabulary: objective, `watr:TreatmentObjective-Thickening`, `-Dewatering`, `-Drying`
  - Parent in the hierarchy: `watr:TreatmentObjective-VolumeReduction`
  - Why: names the state of the product. Sedimentation, flotation, centrifugation, and filtration all reach it.
  - Basis: source. WEF lists thickening as a clarifier function[^wef]. The CWNS data dictionary describes a biosolids facility as "designed to thicken, stabilize, dewater, or store"[^cwns], which is purpose language.
- **Chlorination**
  - Vocabulary: process, `watr:Process-Chlorination`
  - Parent in the hierarchy: `watr:Process-Dosing`
  - Objective every unit inherits: `watr:TreatmentObjective-Disinfection`
  - Why: names the action. Chlorine is dosed and reacts. It always disinfects, so the ontology declares the objective on the process.
  - Basis: source for the name, decision for the definition. Every simulator library and Metcalf & Eddy call it chlorination[^sims][^me]. That the process means dosing plus contact time, not dosing alone, is a decision taken from the review.
- **Dechlorination**
  - Vocabulary: objective, `watr:TreatmentObjective-ChlorineResidualRemoval`, with "Dechlorination" as an alternate label
  - Parent in the hierarchy: `watr:TreatmentObjective-ConstituentRemoval`
  - Why: names a result. The chlorine residual is gone. Sulfite dosing, carbon adsorption, and UV are the processes that reach it.
  - Basis: decision. This is the weakest call in the list. Metcalf & Eddy treats dechlorination as a step within the disinfection chapter, which reads as a process. We chose objective because three unrelated mechanisms reach it and none of them is named "dechlorination." The team can overrule this; if it becomes a process, sulfite dosing folds into it.
- **Nitrification**
  - Vocabulary: process, `watr:Process-Nitrification`
  - Parent in the hierarchy: `watr:Process-BiologicalProcess`
  - Objective every unit inherits: `watr:TreatmentObjective-AmmoniaControl`
  - Why: names the action. Bacteria oxidize ammonia to nitrate. It always controls ammonia. It never removes nitrogen on its own, so it does not declare nitrogen removal.
  - Basis: source. The CWNS data dictionary lists "Ammonia Removal" and "Nitrogen Removal" as separate permit requirements[^cwns], and nitrification satisfies only the first.
- **Denitrification**
  - Vocabulary: process, `watr:Process-Denitrification`
  - Parent in the hierarchy: `watr:Process-BiologicalProcess`
  - Objective every unit inherits: `watr:TreatmentObjective-NitrogenRemoval`
  - Why: names the action. Bacteria reduce nitrate to nitrogen gas. Nitrogen leaves the water, so it always removes nitrogen.
  - Basis: source. Metcalf & Eddy lists nitrification and denitrification variations as the processes for the nitrogen constituent[^me]. Denitrification is the step in which nitrogen leaves the water.
- **Reverse osmosis**
  - Vocabulary: process, `watr:Process-ReverseOsmosis`
  - Parent in the hierarchy: `watr:Process-MembraneProcess`
  - Objective every unit inherits: none. Whether the plant wants desalination or PFAS removal is plant intent, so the modeler writes the objective.
  - Why: names the action. Pressure forces water through a membrane.
  - Basis: source. The Treatability Database lists reverse osmosis against many contaminants, not only salts[^tdb]. Metcalf & Eddy lists membranes under the colloidal and dissolved solids constituent generally[^me].
- **Land application, landfilling**
  - Vocabulary: process, `watr:Process-LandApplication`, `watr:Process-Landfilling`
  - Parent in the hierarchy: `watr:Process-PhysicalProcess`
  - Objective every unit inherits: `watr:TreatmentObjective-BiosolidsDisposal`
  - Why: names an activity, not a result. The result is that the biosolids are disposed of.
  - Basis: decision, taken from the review. Metcalf & Eddy treats land application and landfilling as biosolids disposal methods, which is consistent with process-that-achieves-disposal, but no source states the split.
- **Aerobic, anoxic, anaerobic**
  - Vocabulary: role, `watr:Role-Aerobic`, `-Anoxic`, `-Anaerobic`
  - Parent in the hierarchy: `watr:Role`
  - Why: the plant decides which regime a zone runs in. A sensor reads the actual dissolved oxygen.
  - Basis: source for "not a process," decision for "role." ISO 6107 defines all three as conditions of the medium[^iso6107]. That the commissioned regime is a role, and the actual dissolved oxygen a reading, follows the function-versus-role distinction in BFO[^bfo].
- **Primary, secondary, tertiary**
  - Vocabulary: role, `watr:Role-Primary`, `-Secondary`, `-Tertiary`
  - Parent in the hierarchy: `watr:Role`
  - Why: changes when the plant moves the unit to another stage.
  - Basis: source. WEF calls primary and secondary the "type of unit process" that determines which functions a clarifier performs[^wef]. Under BFO a position that changes without physical change is a role[^bfo].
- **Recirculation**
  - Vocabulary: role on the connection point, `s223:Role-Recirculating`, `s223:Role-Return`
  - Parent in the hierarchy: `s223:Role`
  - Why: the plant decides where a stream goes. `watr:Process-Recirculation` still exists, because system definitions such as A2O list it as an included step.
  - Basis: decision, taken from the review. No source addresses it.
- **Backwashing, air scour**
  - Vocabulary: process, auxiliary, `watr:Process-Backwashing`, `watr:Process-AirScouring`
  - Parent in the hierarchy: `watr:Process-Cleaning`
  - Objective every unit inherits: none.
  - Why: names an action, so it is a process. It is auxiliary because the plant does not rely on its output as a product: backwash water goes back to the head of the plant. Classes list it under `watr:mayAlsoPerform` so it raises no warning.
  - Basis: source for "process," rule for "auxiliary." ISO 6107 defines air scour as a process[^iso6107]. "Auxiliary" follows the rule in section 2: no output stream the plant relies on, so no objective.
- **A2O aerobic zone and nitrogen removal**
  - Vocabulary: nothing new. The zone carries `watr:TreatmentObjective-AmmoniaControl`, inherited from nitrification, and is a member of a system that carries `watr:TreatmentObjective-NitrogenRemoval`, inherited from A2O.
  - Why: the zone nitrifies, which removes no nitrogen, so it must not carry nitrogen removal itself. The train's nitrogen removal depends on it, and system membership already says so. A query follows `s223:hasMember` to find it; section 9 shows the query.
  - Basis: decision. The membership query is our design; no source addresses partial contribution.

## 5. Where each triple comes from

- **The modeler writes**
  - `rdf:type`. The most specific class you can defend.
  - `s223:hasRole`. Whenever the unit has a stage, regime, or duty.
  - `watr:hasTreatmentObjective` for plant intent. RO for desalination, a polishing filter for turbidity, a reuse barrier for organics.
  - `watr:hasProcess` when the class names only a family. `Reactor` and `MixingBasin` require nothing biological. The modeler says whether the basin denitrifies, nitrifies, or releases phosphorus.
- **Inherited from the class** (SHACL-AF rules in `water/class-defaults.ttl`)
  - Every `hasProcess` and `hasTreatmentObjective` requirement on the class and its ancestors.
  - A `GravityThickener` gets `Process-Sedimentation` from `GravityThickener` and `TreatmentObjective-Thickening` from `Thickener`.
  - Never a role.
- **Inherited from the process** (a second SHACL-AF rule)
  - The `achievesTreatmentObjective` of every process the instance has.
  - A basin with `Process-Denitrification` gets `TreatmentObjective-NitrogenRemoval`.
  - This makes objective queries reliable. The modeler does not repeat what the vocabulary already says.
- **Checked by validation**
  - Violation: a `hasProcess` value that is not a `watr:Process`. A `hasTreatmentObjective` value that is not a `watr:TreatmentObjective`. An objective with no process.
  - Warning: a process outside the class's required and `mayAlsoPerform` families.
  - Warning: a system claims a compound process and its members do not cover the included steps.

## 6. Worked examples

Each example shows what the modeler writes, then what inference adds, then which of the written triples the class could not have supplied.

- **Gravity thickener**
  ```ttl
  :thickener a watr:GravityThickener .
  ```
  - Inference adds `Process-Sedimentation` from `GravityThickener` and `TreatmentObjective-Thickening` from `Thickener`.
  - The modeler adds nothing. Add a role if the thickener has one.
- **Primary clarifier**
  ```ttl
  :primary a watr:Clarifier ;
      s223:hasRole watr:Role-Primary .
  ```
  - Inference adds `Process-Sedimentation` from `SedimentationTank` and `TreatmentObjective-Clarification` from `Clarifier`. Clarification is a `SolidsRemoval`, so a solids-removal query returns this unit.
  - The modeler adds the role. A secondary clarifier is the same class with `Role-Secondary`.
  - If the plant also relies on the underflow as thickened sludge, the modeler adds `TreatmentObjective-Thickening`.
- **Generic settling tank**
  ```ttl
  :settler a watr:SedimentationTank ;
      watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .
  ```
  - Inference adds `Process-Sedimentation`. No objective, because a generic settling tank serves either product.
  - The modeler adds the objective. Here the plant uses the underflow, so thickening.
- **Reverse osmosis unit for desalination**
  ```ttl
  :ro a watr:ReverseOsmosisMembrane ;
      watr:hasTreatmentObjective watr:TreatmentObjective-Desalination .
  ```
  - Inference adds `Process-ReverseOsmosis`. RO is a membrane process and a filtration.
  - The modeler adds desalination, because it is plant intent. A reuse barrier also states `OrganicsRemoval`.
- **Chlorine contact tank**
  ```ttl
  :contact a watr:ChlorinationUnit .
  ```
  - Inference adds `Process-Chlorination` from `ChlorinationUnit` and `TreatmentObjective-Disinfection` from `DisinfectionUnit`. Chlorination also entails disinfection, so the objective arrives twice.
  - The modeler adds nothing.
- **Zone in an A2O train**
  ```ttl
  :aerobicZone a watr:AerationBasin ;
      s223:hasRole watr:Role-Aerobic ;
      watr:hasProcess watr:Process-Nitrification .

  :train a s223:System ;
      s223:hasMember :anaerobicZone, :anoxicZone, :aerobicZone, :clarifier ;
      watr:hasProcess watr:Process-A2O .
  ```
  - Inference adds `Process-Aeration` to the zone from its class, and `TreatmentObjective-AmmoniaControl` because nitrification entails it. The zone does not get nitrogen removal, because nitrification alone removes no nitrogen. The train does, and the zone is a member of the train, which is how a query finds it.
  - Inference adds `NitrogenRemoval`, `PhosphorusRemoval`, and `OrganicsRemoval` to the train, because A2O and its parent activated sludge entail them.
  - Validation checks that the members cover the steps A2O includes: nitrification, denitrification, EBPR, and recirculation, plus aeration and solid-liquid separation inherited from activated sludge.
  - The modeler adds the regime, the zone's process, and the membership. `AerationBasin` fixes none of them.
- **Repurposed unit**
  ```ttl
  :oldClarifier a watr:SedimentationTank ;
      s223:hasRole watr:Role-Equalization .
  ```
  - The plant now uses an unchanged clarifier to equalize flow. Keep the class. Add the role. The vessel still settles, so it keeps sedimentation and clarification.
  - The plant rebuilt it with diffusers. Retype it as `watr:AerationBasin`. Class defaults follow the current type.
  - The model does not record when or from what the plant converted a unit.

## 7. Vocabulary

Indentation is the hierarchy: each indented item is a subclass (`rdfs:subClassOf`) of the item above it, and counts as it. In the process tree, `→ objective:` names the treatment objective that the process always produces. The ontology declares it on the process with `watr:achievesTreatmentObjective`, and every unit or system that performs the process inherits that objective. A process with no arrow produces different results in different units, so its objective comes from the equipment class or from the modeler.

### Processes (mechanisms)

- Water Treatment Process
  - Physical Process
    - Separation
      - Solid-Liquid Separation
        - Sedimentation
        - Flotation
        - Centrifugation
      - Filtration
        - Media Filtration (also solid-liquid)
          - Rapid Sand Filtration
          - Slow Sand Filtration
          - GAC Filtration (also adsorption)
        - Membrane Process
          - Microfiltration
          - Ultrafiltration (also solid-liquid)
          - Reverse Osmosis
            - Closed Circuit Reverse Osmosis
            - Feed Reversal Reverse Osmosis
            - Osmotically Assisted Reverse Osmosis
          - Membrane Distillation
      - Screening
      - Elutriation
      - Stripping
    - Adsorption
    - Gas Transfer
      - Aeration
    - Mixing
    - Recirculation (systems use it; on equipment use the connection-point role instead)
    - Thermal Treatment
    - Evaporation
    - Condensation
    - Solidification
      - Crystallization
    - Comminution
    - Ultraviolet Irradiation → objective: Disinfection
    - Cleaning (auxiliary, via `mayAlsoPerform`)
      - Backwashing
      - Air Scouring
      - Purging
    - Land Application → objective: Biosolids Disposal
    - Landfilling → objective: Biosolids Disposal
  - Chemical Process
    - Dosing
      - Chlorination → objective: Disinfection
      - Sulfite Dosing → objective: Chlorine Residual Removal
      - Coagulation
        - Electrocoagulation
    - Flocculation (also mixing)
    - Chemical Precipitation
    - Chemical Reduction
    - Oxidation
      - Ozonation
      - Advanced Oxidation
      - Electrooxidation
    - Ion Exchange
    - Electrodialysis
      - Electro-Dialytic Crystallization
    - Electrolysis
    - Hydrolysis
      - Thermal Hydrolysis
    - Solvent Extraction
    - High-Density Sludge → objective: Neutralization
    - Combustion
      - Fluidized Bed Incineration → objective: Biosolids Disposal
      - Multiple Hearth Incineration → objective: Biosolids Disposal
      - Cogeneration
  - Biological Process
    - Nitrification → objective: Ammonia Control
    - Denitrification → objective: Nitrogen Removal
    - Enhanced Biological Phosphorus Removal → objective: Phosphorus Removal
    - Activated Sludge → objective: Organics Removal (compound; `includesProcess` lists its steps)
      - AO → objective: Nitrogen Removal
        - MLE
      - A2O → objectives: Nitrogen Removal, Phosphorus Removal
        - UCT
      - Four-Stage Bardenpho → objective: Nitrogen Removal
      - Five-Stage Bardenpho → objectives: Nitrogen Removal, Phosphorus Removal
    - Biofiltration (also filtration)
      - Biologically Active Filtration
      - Trickling Filtration
    - Digestion → objective: Stabilization
      - Aerobic Digestion
      - Anaerobic Digestion
    - Composting → objectives: Stabilization, Biosolids Disposal

### Treatment objectives (intended changes)

- Treatment Objective
  - Constituent Removal (each child names its target with `watr:targetsConstituent`; see the constituent list below)
    - Solids Removal
      - Clarification (the WEF clarifier function: a clarified liquid stream)
      - Turbidity Removal
    - Dissolved Solids Removal
      - Desalination
      - Softening
      - Silica Removal
      - Sulfate Removal
      - Metals Removal
    - Organics Removal
    - Nutrient Removal
      - Nitrogen Removal
      - Phosphorus Removal
    - Ammonia Control (a sibling of Nutrient Removal, not a child)
    - Chlorine Residual Removal (alternate label: Dechlorination)
  - Disinfection
  - Volume Reduction (solids side)
    - Thickening
    - Dewatering
      - Drying
  - Stabilization
  - Biosolids Disposal
  - pH Control
    - Neutralization
  - Resource Recovery (placeholder for water reuse, energy recovery, and nutrient recovery; no children yet)

### Constituents

The targets of constituent-removal objectives. Every constituent is a subclass of `s223:Medium-Constituent`, the s223 class for a substance carried in a medium. Indentation is the hierarchy. The water itself is `s223:Constituent-H2O`, from s223.

- `watr:Constituent-Particles`
  - `watr:Constituent-Solids`
    - `watr:Constituent-SuspendedSolids`
- `watr:Constituent-DissolvedSolids`
  - `watr:Constituent-Salt`
    - `watr:Salt-NaCl`
  - `watr:Constituent-Hardness` (calcium and magnesium)
  - `watr:Constituent-Silica`
  - `watr:Constituent-Sulfate`
  - `watr:Constituent-Metals`
- `watr:Constituent-Organics`
  - `watr:Constituent-OrganicCarbon`
  - `watr:Constituent-VolatileOrganicCompounds`
  - `watr:Constituent-PFAS`
- `watr:Constituent-Nitrogen`
  - `watr:Constituent-Ammonia`
  - `watr:Constituent-Nitrate`
  - `watr:Constituent-Nitrite`
  - `watr:Constituent-OrganicNitrogen`
- `watr:Constituent-Phosphorus`
  - `watr:Constituent-Phosphate`
- `watr:Constituent-Pathogens`
  - `watr:Constituent-Bacteria`
  - `watr:Constituent-Viruses`
  - `watr:Constituent-Protozoa`
- `watr:Constituent-ChlorineResidual`
- `watr:Constituent-DissolvedOxygen`
- `watr:Constituent-InorganicCarbon`
- `watr:Constituent-Inorganics`
- `watr:Constituent-NitrogenOxides`
- `watr:Constituent-Cyanide`

What each named objective targets:

- Solids Removal → `watr:Constituent-SuspendedSolids`. Clarification and Turbidity Removal inherit the same target.
- Dissolved Solids Removal → `watr:Constituent-DissolvedSolids`
  - Desalination → `watr:Constituent-Salt`
  - Softening → `watr:Constituent-Hardness`
  - Silica Removal → `watr:Constituent-Silica`
  - Sulfate Removal → `watr:Constituent-Sulfate`
  - Metals Removal → `watr:Constituent-Metals`
- Organics Removal → `watr:Constituent-Organics`
- Nutrient Removal → `watr:Constituent-Nitrogen` and `watr:Constituent-Phosphorus`
  - Nitrogen Removal → `watr:Constituent-Nitrogen`
  - Phosphorus Removal → `watr:Constituent-Phosphorus`
- Ammonia Control → `watr:Constituent-Ammonia`
- Chlorine Residual Removal → `watr:Constituent-ChlorineResidual`
- Disinfection is not a constituent-removal objective, but it also carries a target: `watr:Constituent-Pathogens`.

### Roles (contextual)

The role list is flat. Every WaTr role is a direct subclass of `s223:Role`, except drain and overflow, which are subclasses of `s223:Role-Discharge`. The headings below are groupings for reading; they are not classes in the ontology. Each role names its identifier, what it says about the unit or port, and where the modeler puts it.

- **Stage of the treatment train.** Put on a unit. Says which stage of the plant the unit belongs to.
  - `watr:Role-Pretreatment`: the unit sits ahead of the main train and conditions the influent for it.
  - `watr:Role-Primary`: the unit belongs to the stage that removes settleable and floatable solids ahead of biological treatment. Not the same as `s223:Role-Primary`, which means a primary loop.
  - `watr:Role-Secondary`: the unit belongs to the stage that removes biodegradable organics and suspended solids, usually biologically. Not the same as `s223:Role-Secondary`, which means a secondary loop.
  - `watr:Role-Tertiary`: the unit belongs to the polishing stage after secondary treatment.
  - `watr:Role-Posttreatment`: the unit sits after the main train and conditions the effluent for discharge or reuse.
- **Configuration of a stage.** Put on a unit. Says how the plant runs a biological stage.
  - `watr:Role-Extended`: the unit runs at an extended solids retention time.
  - `watr:Role-Stepfeed`: the unit is fed at several points along its length rather than only at its head.
- **Commissioned regime of a zone.** Put on a unit. Says which oxygen regime the plant designed the zone to run in. A design claim, not a reading: a basin whose blowers are off still carries aerobic. A swing zone commissioned for either regime carries two.
  - `watr:Role-Aerobic`: dissolved oxygen present.
  - `watr:Role-Anoxic`: no dissolved oxygen, nitrate present.
  - `watr:Role-Anaerobic`: no dissolved oxygen and no nitrate.
- **Duty of a vessel.** Put on a unit. Says what the plant uses a holding vessel for.
  - `watr:Role-Storage`: holds water or sludge for later use rather than acting on it.
  - `watr:Role-Equalization`: buffers variation in flow or load so downstream processes see a steadier stream.
  - `watr:Role-Detention`: holds flow for a designed interval so a reaction or settling can complete.
  - `watr:Role-Retention`: holds flow to attenuate a peak, typically stormwater, and releases it at a controlled rate.
  - `watr:Role-Containment`: confines a spill or an off-specification stream to keep it out of the rest of the plant.
- **Purpose of a connection point.** Put on a connection point, not on the unit. Says what the port carries.
  - `watr:Role-Feed`: admits the stream the process acts on.
  - `watr:Role-Permeate`: carries the stream that has passed through a membrane.
  - `watr:Role-MakeUp`: admits water to replace what the process consumes or loses.
  - `watr:Role-Drain` (a kind of `s223:Role-Discharge`): empties the vessel below its working level, for maintenance or solids removal.
  - `watr:Role-Overflow` (a kind of `s223:Role-Discharge`): discharges liquid above the tank's working level.
  - `s223:Role-Return`: carries a stream back upstream, such as return activated sludge.
  - `s223:Role-Recirculating`: carries an internal recycle, such as mixed liquor from the aerobic zone back to the anoxic zone.
- **Deprecated.** `watr:Role-Backwash` is kept only so old models still validate. Write `watr:hasProcess watr:Process-Backwashing` on the unit instead.

## 8. How the review comments are addressed

Each entry quotes a comment from the review of PR #39, links to it, and says what this design does about it. Comments the design does not address are listed at the end.

### Whether the split is worth it

> "Overall my conclusion is that these definitions are very blurry and there will be a bit of inconsistency no matter what we decide, so it's really about what is easiest from the end user's perspective." Fletch, review summary.

**Answer.** Agreed that no standard draws the process-versus-objective line. The closest is Metcalf & Eddy's table of constituents against unit operations and processes[^me], which is the model this design follows. Section 2 states the two distinctions in plain terms, and section 4 gives three tests so a modeler can place a term without guessing. Section 1 makes the modeler's job explicit: type, role, plant intent, and a process only where the class leaves a choice. Everything else is inherited.

> "I think the treatment objectives generally make sense to distinguish, with the caveat that they will make an already-complicated ontology more complicated for non-data-savvy users to navigate. ... Maybe a UI could default the process from the equipment class and only offer a choice of objective when the process/equipment doesn't already specify it." Daly, [issue comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#issuecomment-5332011106).

**Answer.** That is how the model works. Section 1b: process is inherited from the class unless the class leaves a choice, and objective is inherited from the class or the process unless it is plant intent. A UI can read the class's requirements to decide which fields to show.

> "To me clarification and sedimentation are synonyms, so this emphasizes the blurriness between process/outcome that's making me reconsider if this overhaul makes sense." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3813728427).

**Answer.** This is the key distinction the model makes, so please tell me if the new definitions below are not clear. Sedimentation is what the tank does: solids settle under gravity. It is true of every settling tank, so it is the process, and the class supplies it. Sedimentation always produces two streams, a clarified overflow and a thickened underflow. Which of those the plant relies on downstream is what the tank is *for*, and that is the treatment objective. If the overflow goes on to treatment, the objective is clarification. If the underflow goes on to digestion, the objective is thickening. If the plant relies on both, the tank carries both. The process is a fact about the tank; the objective is a fact about how the plant uses what comes out of it. The WEF sedimentation fact sheet makes the same split, listing clarification and thickening as two functions of a clarifier, with sedimentation as the process[^wef].

### Clarification

> "I'd remove this as I think it's covered by `SolidsRemoval`." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814715750). "I'd call Clarification a process that achieves Objective SolidsRemoval as well." Daly, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3806441049).

**Answer.** Clarification stays, as an objective under solids removal. Section 4 explains why: it names a result, practitioners use the word, and WEF lists it as a clarifier function[^wef]. Dropping it would make a search for "clarification" return nothing. The caveat in section 4 applies: Metcalf & Eddy also uses the word for a unit operation[^me], so this is a choice between sources.

> "A sedimentation process can remove solids or thicken a solids stream. ... the question is the outcome focused on thickening (the waste stream) or solids removal (to clean water)." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3813763458).

**Answer.** That is exactly the reason the objective is separate from the process. Section 2 adds the rule that a class carries a design objective only when every unit of the class is built for the same result. The generic settling tank therefore carries no objective. A clarifier subclass carries clarification, the gravity thickener carries thickening, and a unit may carry both when the plant relies on both products.

> "When thinking about things like `Thickening` it's unclear whether `Thickening` would be the process or the outcome (or both?)." Fletch, [issue comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#issuecomment-5299295592).

**Answer.** Thickening is an objective, for the same reason clarification is. A thickener settles, floats, spins, or filters; that is the process, and it is a fact about the unit. Every one of those processes puts out a liquid stream and a dense stream. Thickening says the plant relies on the dense stream. A gravity thickener and a primary clarifier perform the same process; they differ in which output the plant uses, and that is what the objective records. Basis: WEF lists thickening as a clarifier function next to clarification[^wef], and the CWNS data dictionary describes biosolids facilities as "designed to thicken"[^cwns]. Section 4.

### Objective hierarchy

> "There are a lot of 'xRemoval' TreatmentObjectives that will likely continue to expand ... 'ConstituentRemoval' could be a class that takes in a specific 'substance' or 'constituent'." Daly, [issue comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#issuecomment-5332011106). "Things that utilities actually want to achieve: ConstituentRemoval ... MassReduction / VolumeReduction ... ProductRecovery." Daly, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3833337044).

**Answer.** Adopted. Section 7 restructures the objectives under constituent removal, volume reduction, disinfection, stabilization, biosolids disposal, pH control, and a resource recovery placeholder. Section 1a adds `watr:targetsConstituent`, with a worked PFAS example showing that a new contaminant needs no new class.

> "I would make this [Organics Removal] a subclass of `SolidsRemoval`. ... I'd make this [Softening] a subclass of `ChemicalRemoval`. But these are also dissolved solids, so this is where I wonder if the new structure gets confusing." Fletch, [comments](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814733340) [and](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814747186).

**Answer.** Section 7 puts desalination, softening, silica, sulfate, and metals removal under a dissolved solids removal parent, and organics removal as its own child of constituent removal. The structure follows the constituent rows in Metcalf & Eddy[^me] rather than a chemistry taxonomy, which is what caused the confusion.

> "Objectives could be a nice place to house permitted limit values for the facility." Daly, [issue comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#issuecomment-5332011106).

**Answer.** Section 2 says plant intent is where a permit limit or target attaches. Targets are not modeled yet; the design leaves the hook.

### Processes that name a result

> "Landfill (maybe rename to Landfilling) and Land Application to me still fit more as Processes, where the TreatmentObjective for both would be BiosolidsDisposal." Daly, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3806427762).

**Answer.** Adopted. Section 4 and section 7 make land application and landfilling processes that achieve biosolids disposal. Basis: decision, taken from this comment.

> "Dechlorination also feels like more of a process than an Objective." Daly, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3806446730). "If keeping it as an objective, I might make it a child class of something like ConstituentRemoval." Daly, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3833381136).

**Answer.** It stays an objective, named chlorine residual removal with dechlorination as an alternate label, under constituent removal. Section 4 explains: it names a result, and sulfite dosing, carbon adsorption, and UV all reach it. Sulfite dosing is added as the process most plants use. Basis: decision. Section 4 marks this as the weakest placement in the list, and it can go the other way.

> "I would not call the dosing itself the process, but rather the combination of dosing + contact time." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3813789080). "Maybe keep this as 'chlorination' if we have 'coagulation'?" Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3815210207).

**Answer.** Renamed back to chlorination, defined as dosing plus contact. Every simulator library and Metcalf & Eddy use the name[^sims][^me]. Section 4 and section 7.

> "Reverse osmosis is not strictly for desalination, so I wouldn't infer that." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814228114). "I believe that RO can be used for resource recovery as well." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814891926).

**Answer.** Adopted, and the resource recovery point is the reason. Reverse osmosis is a fact about the membrane: pressure pushes water through and leaves solutes behind. It always puts out a permeate and a concentrate. Desalination says the plant relies on the permeate as low-salt water. PFAS removal says the plant relies on the permeate as PFAS-free water. Resource recovery says the plant relies on the concentrate. The membrane cannot know which, so the class carries no objective and the modeler writes it. The Treatability Database bears this out by listing RO against many contaminants[^tdb]. Section 2, section 4, and the RO example in section 6.

### Whether objectives can be trusted

> "In a non-UI version where specifying objectives isn't mandated, only a handful of processes automatically imply an objective. Queries for e.g., everything involved with nitrogen removal would only get back whatever people remembered to manually input. Is the objective meant to be queryable reliably?" Daly, [issue comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#issuecomment-5332011106).

**Answer.** Yes. Section 5: the class writes its design objective onto every unit, and an inference rule writes a process's achieved objective onto every unit that performs it. The modeler writes only plant intent. A unit that denitrifies is found by a nitrogen removal query whether or not the modeler typed the objective.

> "I could see this being a major issue because water treatment folks will assume that the process guarantees an outcome." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3813826498). "Is `achievesTreatmentObjective` different than `hasTreatmentObjective`?" Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814467830).

**Answer.** The unit guarantees the process. The process guarantees the objective only when it has one product used one way. Denitrification sends nitrogen off as gas, so every unit that denitrifies removes nitrogen, and the ontology says so. Sedimentation puts out two streams, so the guarantee stops at the process, and the plant says which stream it relies on. Section 4, entailment rule. The two predicates are explained in section 1a: `achievesTreatmentObjective` sits on the process in the ontology; `hasTreatmentObjective` sits on the unit, and inference copies the first onto the second.

> "Maybe components of a process (e.g. anoxic zone of an A2O process system) could indicate that they 'contribute to' an objective like nitrogen removal, even if that zone doesn't completely achieve it itself." Daly, [issue comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#issuecomment-5332011106).

**Answer.** Handled without a new relation. The zone is a member of a system whose objective is nitrogen removal, and that membership is already in the model. A query for "everything involved in nitrogen removal" unions units that carry the objective with members of systems that carry it. Section 9 shows the query and its results. A dedicated relation was considered and dropped, because there was no rule for when a modeler should write it.

### Roles

> "With the new structure, I'm wondering if anoxic, anaerobic, etc would be a process." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3813881314).

**Answer.** They stay roles. Section 4: the plant decides which regime a zone runs in, and a sensor reads the actual dissolved oxygen. ISO 6107 defines aerobic, anoxic, and anaerobic as conditions of the medium, not processes[^iso6107]. That a commissioned condition is a role follows BFO's function-versus-role distinction[^bfo].

> "What if a chlorination unit is converted to a storage tank? ... I don't have a good resolution to this point." Fletch, [comments](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3813894974) [and](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3813900086). "For plant retrofits and upgrades, they might repurpose equipment like a clarifier to an aeration basin. Should repurposed equipment change to a more generic equipment type?" Daly, [issue comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#issuecomment-5332011106).

**Answer.** Section 6, repurposed unit. If the vessel is unchanged, keep the class and add a role such as storage or equalization. If the plant rebuilt it, retype it, and class defaults follow the new type. Conversion history is not modeled. Basis: BFO, which says repurposing an artifact without physical change gives it a new role, not a new function[^bfo].

> "Recirculation is a bit tricky. It seems more like a Role applied to a connection stream rather than a Process." Daly, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3806523244). "Backwashing and recirculation seem to fit in a common category of 'features' applied to a piece of equipment." Daly, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3833343423). "Is backwashing really a process? Or an outcome?" Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3813919264).

**Answer.** Recirculation on equipment is a role on the connection point, using the s223 return and recirculating roles. The process term stays because compound processes such as A2O list it as an included step. Backwashing is a process, because it is something the filter does, and it has no objective, because the plant does not rely on its output as a product. It sits under cleaning and is allowed through `mayAlsoPerform`. Basis: decision for recirculation; ISO 6107 defines air scour as a process[^iso6107], and "no objective" follows the rule in section 2. Section 4 and section 7.

### Things the reviewers liked

> "I really like this formalism!" on system processes, Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814169339). "I like this approach to raise a warning but not invalidate the graph in these cases!" Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814698764). "I like this distinction between solid-liquid and liquid-gas separations." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814967884). "I agree that these biosolids terms make a lot more sense as treatment objectives than the previous designation as processes." Fletch, [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814789597).

**Answer.** Kept as is. Systems and coverage checks are in section 1b, warnings in section 5, the separation hierarchy and biosolids objectives in section 7.

### Not addressed in this design

These are outside the process, objective, and role model. The mechanical ones are on the [work list](treatment_model_work.md).

- Rename `outcomes.ttl` and the process-outcome map to say "objective" ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814627809), [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814505529)); "Water Treatment Process" label ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814962839)); GAC duplicate in the generated docs ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3815178332)); `MakeUp` prefix ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814952879)); duplicated aeration basin description ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814494921)); `rdfs:comment` versus `skos:definition` ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814581696)); test docstring wording ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814662725)); severity levels ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814680503)).
- Whether a tank may have a single port serving as both inlet and outlet ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814479492)).
- Sampling and dosing points as junctions or observation locations ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814529050), [comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814569320)).
- Zones inside one long basin rather than separate tanks ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814547441)).
- Media compatibility when a reaction changes the constituents ([comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814151705)).
- Mete's validation warning on BAF and GAC units in the DPR model ([issue comment](https://github.com/DataDrivenCPS/water-ontology/pull/39#issuecomment-5074790336)) needs a re-run against the current branch.

## 9. A whole train: what the modeler writes and what inference adds

This answers the concern that the model asks too much of the modeler. The plant below is a small municipal train: screen, primary clarifier, A2O biological train, secondary clarifier, chlorine contact tank, and a gravity thickener and digester on the sludge side. Units are joined with `s223:connectedTo`, which is directed: `A s223:connectedTo B` means flow leaves A and enters B. The edges that run backward, from the aerobic zone to the anoxic zone and from the secondary clarifier to the anaerobic zone, are the internal recycle and the return sludge. Connection points are left out to keep the example short; in a model that has them, 223 infers `connectedTo` from the connection points and the modeler does not write it.

### What the modeler writes

```ttl
@prefix : <urn:example/> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <urn:nawi-water-ontology#> .

# Liquid train

:barScreen a watr:Screen ;
    s223:hasRole watr:Role-Pretreatment ;
    s223:connectedTo :primaryClarifier .

:primaryClarifier a watr:Clarifier ;
    s223:hasRole watr:Role-Primary ;
    s223:connectedTo :anaerobicZone, :thickener .

# A mixing basin only mixes, as a class. The plant runs this one for
# biological phosphorus release, so the modeler names the process.
:anaerobicZone a watr:MixingBasin ;
    s223:hasRole watr:Role-Anaerobic ;
    watr:hasProcess watr:Process-EnhancedBiologicalPhosphorusRemoval ;
    s223:connectedTo :anoxicZone .

:anoxicZone a watr:MixingBasin ;
    s223:hasRole watr:Role-Anoxic ;
    watr:hasProcess watr:Process-Denitrification ;
    s223:connectedTo :aerobicZone .

# An aeration basin aerates, as a class. This one also nitrifies, and it
# pumps mixed liquor back to the anoxic zone.
:aerobicZone a watr:AerationBasin ;
    s223:hasRole watr:Role-Aerobic ;
    watr:hasProcess watr:Process-Nitrification, watr:Process-Recirculation ;
    s223:connectedTo :secondaryClarifier, :anoxicZone .

:secondaryClarifier a watr:Clarifier ;
    s223:hasRole watr:Role-Secondary ;
    s223:connectedTo :contactTank, :anaerobicZone, :thickener .

:contactTank a watr:ChlorinationUnit .

# Sludge train

:thickener a watr:GravityThickener ;
    s223:connectedTo :digester .

:digester a watr:AnaerobicDigester .

# The biological train as a system. A system has no class, so the modeler
# names its process.
:bioTrain a s223:System ;
    s223:hasMember :anaerobicZone, :anoxicZone, :aerobicZone, :secondaryClarifier ;
    watr:hasProcess watr:Process-A2O .
```

That is nine units and one system. The modeler wrote the type of every unit, a role on six of them, a process on three, the system's members and process, and the connections.

### What inference adds

Every triple below is added automatically. The comment says where it comes from.

```ttl
# from watr:Screen
:barScreen watr:hasProcess watr:Process-Screening .
:barScreen watr:hasTreatmentObjective watr:TreatmentObjective-SolidsRemoval .

# from watr:SedimentationTank, the parent of watr:Clarifier
:primaryClarifier watr:hasProcess watr:Process-Sedimentation .
# from watr:Clarifier
:primaryClarifier watr:hasTreatmentObjective watr:TreatmentObjective-Clarification .

# from watr:MixingBasin
:anaerobicZone watr:hasProcess watr:Process-Mixing .
# from the process: EBPR always removes phosphorus
:anaerobicZone watr:hasTreatmentObjective watr:TreatmentObjective-PhosphorusRemoval .

# from watr:MixingBasin
:anoxicZone watr:hasProcess watr:Process-Mixing .
# from the process: denitrification always removes nitrogen
:anoxicZone watr:hasTreatmentObjective watr:TreatmentObjective-NitrogenRemoval .

# from watr:AerationBasin
:aerobicZone watr:hasProcess watr:Process-Aeration .
# from the process: nitrification always controls ammonia
:aerobicZone watr:hasTreatmentObjective watr:TreatmentObjective-AmmoniaControl .

# from watr:SedimentationTank and watr:Clarifier, as for the primary
:secondaryClarifier watr:hasProcess watr:Process-Sedimentation .
:secondaryClarifier watr:hasTreatmentObjective watr:TreatmentObjective-Clarification .

# from watr:ChlorinationUnit
:contactTank watr:hasProcess watr:Process-Chlorination .
# from watr:DisinfectionUnit, and again from the process: chlorination always disinfects
:contactTank watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection .

# from watr:GravityThickener
:thickener watr:hasProcess watr:Process-Sedimentation .
# from watr:Thickener
:thickener watr:hasTreatmentObjective watr:TreatmentObjective-Thickening .

# from watr:AnaerobicDigester
:digester watr:hasProcess watr:Process-AnaerobicDigestion .
# from watr:Digester, and again from the process: digestion always stabilizes
:digester watr:hasTreatmentObjective watr:TreatmentObjective-Stabilization .

# from the process: A2O always removes nitrogen and phosphorus, and its
# parent, activated sludge, always removes organics
:bioTrain watr:hasTreatmentObjective watr:TreatmentObjective-NitrogenRemoval ,
                                    watr:TreatmentObjective-PhosphorusRemoval ,
                                    watr:TreatmentObjective-OrganicsRemoval .
```

Validation also runs the coverage check on `:bioTrain`. A2O includes nitrification, denitrification, EBPR, and recirculation, and inherits aeration and solid-liquid separation from its parent, activated sludge. The members perform all six: the zones nitrify, denitrify, release phosphorus, aerate, and recirculate, and the secondary clarifier settles, which is a solid-liquid separation. There is no warning. If the modeler had left recirculation off the aerobic zone, validation would warn that the train claims A2O but no member recirculates.

### What the plant model can now answer

The queries run against the model after inference. Each uses `rdfs:subClassOf*` on the objective or process, so a query for a parent term also returns units carrying a child term. The results show what comes back, and what the modeler wrote to make it come back.

**Which units remove solids?**

```sparql
SELECT ?unit ?objective WHERE {
  ?unit watr:hasTreatmentObjective ?objective .
  ?objective rdfs:subClassOf* watr:TreatmentObjective-SolidsRemoval .
}
```

| unit | objective |
|---|---|
| `:barScreen` | `watr:TreatmentObjective-SolidsRemoval` |
| `:primaryClarifier` | `watr:TreatmentObjective-Clarification` |
| `:secondaryClarifier` | `watr:TreatmentObjective-Clarification` |

The clarifiers match because clarification is a subclass of solids removal. The modeler wrote none of these objectives; all three came from the equipment classes.

**Which units settle?**

```sparql
SELECT ?unit ?objective WHERE {
  ?unit watr:hasProcess ?process .
  ?process rdfs:subClassOf* watr:Process-Sedimentation .
  OPTIONAL { ?unit watr:hasTreatmentObjective ?objective }
}
```

| unit | objective |
|---|---|
| `:primaryClarifier` | `watr:TreatmentObjective-Clarification` |
| `:secondaryClarifier` | `watr:TreatmentObjective-Clarification` |
| `:thickener` | `watr:TreatmentObjective-Thickening` |

Same process on all three, different objective on the thickener. Nothing here was written by the modeler.

**What is involved in nitrogen removal?**

A unit is involved if it carries the objective itself, or if it belongs to a system that carries it. The second branch is how the aerobic zone is found: nitrification removes no nitrogen, so the zone must not carry nitrogen removal, but the train it belongs to does.

```sparql
SELECT ?unit ?how WHERE {
  {
    ?unit watr:hasTreatmentObjective ?objective .
    ?objective rdfs:subClassOf* watr:TreatmentObjective-NitrogenRemoval .
    BIND("carries the objective" AS ?how)
  } UNION {
    ?system watr:hasTreatmentObjective ?objective ;
            s223:hasMember+ ?unit .
    ?objective rdfs:subClassOf* watr:TreatmentObjective-NitrogenRemoval .
    BIND("member of a system that carries it" AS ?how)
  }
}
```

| unit | how |
|---|---|
| `:anoxicZone` | carries the objective |
| `:bioTrain` | carries the objective |
| `:anaerobicZone` | member of a system that carries it |
| `:anoxicZone` | member of a system that carries it |
| `:aerobicZone` | member of a system that carries it |
| `:secondaryClarifier` | member of a system that carries it |

The anoxic zone's objective came from denitrification. The train's came from A2O. The membership branch returns every member of the train, including the secondary clarifier, which returns the sludge the process depends on. The modeler wrote none of the objectives; the membership was the only input.

To narrow the membership branch to members that perform one of the system process's steps, add `?system watr:hasProcess ?p . ?p rdfs:subClassOf*/watr:includesProcess ?step . ?unit watr:hasProcess ?step .` to it. In this plant that keeps the same rows, because every member performs an A2O step.

**Which units disinfect?**

```sparql
SELECT ?unit ?process WHERE {
  ?unit watr:hasTreatmentObjective watr:TreatmentObjective-Disinfection ;
        watr:hasProcess ?process .
}
```

| unit | process |
|---|---|
| `:contactTank` | `watr:Process-Chlorination` |

The modeler wrote only the type. A UV unit added later would appear with `watr:Process-UVIrradiation` and no other change to the query.

**What does the sludge side do?**

```sparql
SELECT ?unit ?process ?objective WHERE {
  :thickener s223:connectedTo* ?unit .
  ?unit watr:hasProcess ?process ;
        watr:hasTreatmentObjective ?objective .
}
```

| unit | process | objective |
|---|---|---|
| `:thickener` | `watr:Process-Sedimentation` | `watr:TreatmentObjective-Thickening` |
| `:digester` | `watr:Process-AnaerobicDigestion` | `watr:TreatmentObjective-Stabilization` |

The path `s223:connectedTo*` follows flow downstream from the thickener. The modeler wrote only the two types and the connection.

**Which zone is anoxic, and what does it do?**

```sparql
SELECT ?unit ?process ?objective WHERE {
  ?unit s223:hasRole watr:Role-Anoxic ;
        watr:hasProcess ?process .
  OPTIONAL { ?unit watr:hasTreatmentObjective ?objective }
}
```

| unit | process | objective |
|---|---|---|
| `:anoxicZone` | `watr:Process-Mixing` | `watr:TreatmentObjective-NitrogenRemoval` |
| `:anoxicZone` | `watr:Process-Denitrification` | `watr:TreatmentObjective-NitrogenRemoval` |

The role is the one thing only the modeler could answer. Mixing came from the class, denitrification from the modeler, and the objective from denitrification.

**Which objectives does the whole plant serve?**

```sparql
SELECT DISTINCT ?objective WHERE {
  ?unit watr:hasTreatmentObjective ?objective .
}
```

| objective |
|---|
| `watr:TreatmentObjective-SolidsRemoval` |
| `watr:TreatmentObjective-Clarification` |
| `watr:TreatmentObjective-PhosphorusRemoval` |
| `watr:TreatmentObjective-NitrogenRemoval` |
| `watr:TreatmentObjective-AmmoniaControl` |
| `watr:TreatmentObjective-OrganicsRemoval` |
| `watr:TreatmentObjective-Disinfection` |
| `watr:TreatmentObjective-Thickening` |
| `watr:TreatmentObjective-Stabilization` |

Nine objectives across the plant. The modeler wrote zero `watr:hasTreatmentObjective` triples.

## 10. References

Footnotes in sections 2, 4, and 8 point here. Each entry says what the source is and what this document takes from it. The intrinsic-versus-contextual distinction in section 2 follows the function-versus-role split in BFO[^bfo], the function-versus-realization split in OntoCAPE[^ontocape], and the function-versus-location aspects in IEC 81346[^iec]; section 2 states it without citations so it reads on its own.

[^wef]: Water Environment Federation, *Liquid Stream Fundamentals: Sedimentation*, fact sheet WSEC-2017-FS-022, Municipal Resource Recovery Design Committee, 2017. <https://www.wef.org/globalassets/assets-wef/direct-download-library/public/03---resources/wsec-2017-fs-022-liquid-stream-fundamentals--clarification-sedimentation_final.pdf>. Defines sedimentation as "the physical process where gravity forces account for the separation of solid particles." Lists four functions a clarifier is designed to serve: flocculation, clarification ("separation of solid and liquid fractions in the influent stream to produce a clarified effluent"), thickening ("production of thickened sludge streams"), and storage. Says "the extent of each function/role performed by a clarifier is dependent on the type of unit process (primary, secondary, tertiary, etc.)."

[^me]: Metcalf & Eddy, *Wastewater Engineering: Treatment and Reuse*, 4th ed., McGraw-Hill, 2003, chapter 1. <https://sswm.info/sites/default/files/reference_attachments/TCHOBANOGLOUS%20et%20al.%202003%20Wastewater%20Engineering.pdf>. Defines unit operations as methods "in which the application of physical forces predominate" and unit processes as methods "in which the removal of contaminants is brought about by chemical or biological reactions." Table 1-5, "Unit operations and processes used to remove constituents found in wastewater," is organized as constituent rows (suspended solids, biodegradable organics, nitrogen, phosphorus, pathogens, colloidal and dissolved solids, volatile organic compounds, odors) against the operations and processes that remove each.

[^cwns]: US EPA, *Clean Watersheds Needs Survey 2008 Data Dictionary*. <https://www.epa.gov/sites/default/files/2016-01/documents/cwns_-2008-data_dictionary2.pdf>. Defines a unit process as "the name of the treatment technology," grouped by treatment type (preliminary, primary, secondary, advanced, disinfection, solids handling). Defines advanced treatment by permit requirement: "Nitrogen Removal; Phosphorous Removal; Ammonia Removal; Metal Removal; Synthetic Organic Removal." Describes a biosolids handling facility as "designed to thicken, stabilize, dewater, or store biosolids."

[^tdb]: US EPA, *Drinking Water Treatability Database*. <https://www.epa.gov/water-research/drinking-water-treatability-database-tdb>. A matrix of 35 treatment processes against more than 160 contaminants, with removal data at each intersection. Reverse osmosis appears against many contaminants, not only salts.

[^iso6107]: ISO 6107:2021, *Water quality — Vocabulary*. <https://www.iso.org/standard/67643.html>. Defines aerobic condition as a condition "in which dissolved oxygen is present," anaerobic condition as one in which it is absent, and anoxic as a state in which dissolved oxygen is low enough that microorganisms use oxidized forms of nitrogen, sulfur, or carbon. Defines air scour as a process of forcing air upward through a filter.

[^bfo]: A. D. Spear, W. Ceusters, B. Smith, "Functions in Basic Formal Ontology," *Applied Ontology* 11 (2016). <http://ontology.buffalo.edu/smith/articles/Functions-in-BFO.pdf>. A function "exists in virtue of its bearer's physical make-up," which the bearer has "through intentional design ... in order to realize processes of a certain sort." A role exists because the bearer "is in some special physical, social, or institutional set of circumstances in which this bearer does not have to be." Repurposing an artifact gives it a new role, not a new function.

[^ontocape]: J. Morbach, A. Wiesner, W. Marquardt, "OntoCAPE: A (re)usable ontology for computer-aided process engineering," *Computers & Chemical Engineering* 33 (2009); and A. Wiesner et al., *Chemical Process Systems*, technical report LPT-2008-29, RWTH Aachen, 2008. <https://www.avt.rwth-aachen.de/global/show_document.asp?id=aaaaaaaaaatptsi>. "The class process step represents the desired function. The class plant item reflects its physical realization." Unit operations are classified by phenomenon: combination, enthalpy change, separation, fragmentation.

[^iec]: IEC 81346-1:2022, *Industrial systems, installations and equipment and industrial products — Structuring principles and reference designations — Part 1: Basic rules*. <https://www.iso.org/standard/82229.html>. Three aspects of an object: function ("what an object is intended to do or what it actually does"), product ("by which means"), and location.

[^sims]: Unit libraries of the common simulators: GPS-X <https://www.hydromantis.com/GPSX-unit-processes.html>, WaterTAP <https://watertap.readthedocs.io/en/stable/apidoc/watertap.unit_models.html>, QSDsan <https://qsdsan.readthedocs.io/en/latest/api/sanunits/clarifier.html>, Sumo <https://wiki.dynamita.com/en/process_units>. Used only for what practitioners call things: every library says "chlorination," and every library has separate clarifier and thickener units.
