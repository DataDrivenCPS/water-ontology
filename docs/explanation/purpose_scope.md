# Purpose and Design

## 1. Purpose

The WaTr ontology aims to provide a standardized graph-oriented metadata schema for treatment systems, regardless of the technologies, processes, or vendors utilized. It harmonizes existing human-readable representations of water metadata including process flow diagrams (PFDs) and process & instrumentation diagrams (P&IDs) along with historical data and provides the means for effective data management and data-driven science for water treatment systems. The focus of this project and this alpha release is on novel small-scale water treatment pilots. The alpha release of the ontology provides a core set of concepts, an ontology structure, and a couple examples of ontology application. This release is focused on providing resources that will later be used for communication with other NAWI pilot teams during demonstration of the ontology and data management platform. 

## 2. Design of the WaTr Ontology

The WaTr ontology represents information critical to the operation of water treatment systems, currently present in multiple different sources, to enable automated analytics, control, and data science in water treatment systems. The existing sources of metadata and how they are integrated into the proposed ontology are enumerated below.

### Piping and Instrumentation Diagrams (P&ID)

These diagrams represent the topology and connectivity of water treatment systems. They represent the physical topology including mechanical equipment, the pipes connecting them, and the physical locations of sensors and actuators. They also link the physical representation to the digital by providing network names or addresses of instrumentation. P&IDs may be referenced frequently throughout operation of water treatment systems and are critical to the development of controls or analytics.

In the WaTr ontology, standard constructs are provided to represent the physical equipment, sensors, actuators, connection points, and connections between them (e.g. pipes) present in a treatment train and their relevant metadata. This information is directly linked to the network information used for example by a SCADA system, and the information necessary for retrieval of historical information.

### Process Flow Diagrams (PFDs)

PFDs show the flow of various contents through a treatment train at a high level. While not showing all the detailed topological information that a P&ID shows, PFDs may include more detailed information about design specifications (e.g. reactor volumes, flow rates) and the media flowing through the treatment process.

In the WaTr ontology, design information like reactor volumes, flow rates, and expected chemical concentrations at different points in the treatment can be represented and tied directly to the system topology contained in a P&ID. The proposed ontology is designed to enable systematic comparison of this design information with real data provided by SCADA or a historian, enabling data-driven processes like fault detection.

### Supervisory Control and Data Acquisition (SCADA)

These systems are used for real-time control and measurement in water systems.

The WaTr ontology provides the means to represent SCADA network data, tied directly to physical representations and design intent, as normally conveyed through P&ID and PFD representations. Information required to access real-time control and measurement information is exposed in a standard, machine-readable method to allow any software to utilize it. This will also be supported by the data management platform developed through this project.

### Data Historians

Many methods of data collection are used in water treatment systems beyond simple scalar telemetry data. Spectrometers and cameras provide multi-dimensional data. Digital logbooks provide text data at irregular timesteps. All of this data supports operation of digitized water treatment systems.

The ontology provides the ability to reference multiple kinds of historical data, tied directly to the other (physical and network) representations of the water treatment system. Historical data of different types, real-time data through SCADA, and design data can all be linked and easily referenced in the context of the physical water treatment system.