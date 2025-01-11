# Definitions and Concepts 

The ontology is inspired by two ontologies developed to represent metadata used in building operations, Brick and ASHRAE 223P. The concepts present in this ontology can be used to represent the information described in the previous section. The WaTr ontology is a graph model, and relies on several graph data concepts. All WaTr models use several high level classes that describe the structure and content of a WaTr model. 

## Graph Data Concepts

 - **Entity:** An entity is an abstraction of the actual "things" in a water treatment train. For example, mechanical equipment such as pumps, tanks, reactors, spatial elements like treatment zones, the area of these zones served by certain mechanical equipment, or the stages these areas may be grouped into based on how the equipment is controlled.

 - **Class:** A named category with intensional meaning (a definition) used for grouping entities.
Classes are organized into a hierarchy, and entities are an instance of a given class. Classes are defined using SHACL shapes ensuring that they are instantiated correctly.

 - **Relationship:** Defines the nature of a link between two related entities.
Examples of relationships are *encapsulation* (one entity is contained within another), *sequence* (one entity takes effect before another in some process) and *instantiation* (one entity's type is given by another).

- **Relation:** A predicate (RDF property) used to describe a given relationship.
Examples of a relation are the WaTr relation `sWaTr:contains`, which defines the relationship between two pieces of equipment in which one contains another.  

 - **Graph:** An abstract organizational data structure representing a set of entities (nodes) and relationships (edges) described in triple-structure. WaTr models are represented by a directed, labeled graph, and use the RDF standard. We recommend reading the [Wikipedia page on the abstract graph data structure](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) for more information.

 - **A WaTr Model:** A WaTr model is a digital representation of a water treatment train in RDF graph structure that uses the WaTr standard. This means that elements of the water treatment train are represented using the modeling constructs defined in the standard. The standard leverages semantic web technologies, allowing easy integration with other types of models based on RDF.

## WaTr Top Level Classes

The WaTr standard defines a hierarchy of classes used to define the entities within a water treatment train. This section provides a basic definition of the classes at the top level of the hierarchy to help users understand what the standard aims to represent, which is described in the [overview](WaTr-overview). 

 - **Connection:** A modeling construct for representing a physical thing (e.g., pipe, duct, wire) that connects and conveys a medium between two Connectable things.

 - **ConnectionPoint:** An abstract modeling construct representing the point where one Connectable thing connects to another.

 - **Domain:** A categorization of water treatment service or specialization used to characterize equipment or spaces (e.g., filtration, chemical treatment, sedimentation).

 - **Connectable:** This is the top level entity that defines the classes that may be connected via ConnectionPoints and Connections. There are three major sub-classes of connectable

    - **DomainSpace:** A portion or entirety of a PhysicalSpace associated with a Domain. Often a DomainSpace is served by a particular piece of equipment, like a single pump, and thus they can be connected to equipment. Multiple DomainSpaces controlled similarly can be grouped together, forming a Stage.

    - **Equipment:** A modeling construct used to represent a mechanical device designed to accomplish a specific task (e.g. pump, fan, heat exchanger, luminaire, temperature sensor, flow meter). Equipment may contain and connect to other equipment, allowing detailed modeling of mechanical systems. Certain pieces of equipment (i.e. Sensors, Actuators, Controllers) may have unique relationships to properties to define how they act on the properties of other entities.

    - **Junction:** A Junction is a modeling construct used to represent important branching points within a Connection.

 - **PhysicalSpace:** An architectural concept representing a tank, reactor, or any physical space in a water treatment train. These PhysicalSpaces (e.g. a tank) can contain other PhysicalSpaces (e.g. a reactor).

 - **System:** A task-oriented collection of interacting or interrelated Equipment defined by the modeler.

 - **Stage:** A collection of DomainSpaces grouped together based on water treatment services or controls.

 - **Properties:** Properties often represent the actuation and measurement points within a water treatment train. They may be associated with real-time data. They also may define the attributes of other entities (e.g. Equipment, DomainSpaces, Stages). They can be further contextualized using enumerations.

 - **Enumerations:** The standard uses enumerations to convey groups of useful values for describing attributes of Properties, Equipment, and other things in the model. For example, the enumeration `Role-Cooling` describes that the equipment in question provides cooling.

 - **FunctionBlock:** Is used to model transfer and/or transformation of information (e.g. control algorithms). It has relations to input properties and output properties, that represent input and output data. The actual algorithms that perform the transformations are not modeled in WaTr.