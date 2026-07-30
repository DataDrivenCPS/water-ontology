# Equipment Classes

## Tank

**Description:** A flow-through vessel with at least one fluid inlet and one fluid outlet. Names a connection-point pattern rather than a geometry: in-line devices such as static mixers qualify.

**Superclass:** Equipment

## Reactor

**Description:** A vessel in which a reaction or biological/chemical treatment process takes place

**Superclass:** Tank

## Reactor

**Description:** A vessel in which a reaction or biological/chemical treatment process takes place

**Superclass:** UnitProcess

## Separation Tank

**Description:** A tank that has at least two outlets (e.g. overflow and underflow)

**Superclass:** Tank

## Separation Tank

**Description:** A tank that has at least two outlets (e.g. overflow and underflow)

**Superclass:** UnitProcess

## SequencingBatchReactor

**Description:** A type of activated sludge process for wastewater treatment

**Superclass:** Reactor

## SequencingBatchReactor

**Description:** A type of activated sludge process for wastewater treatment

**Superclass:** SeparationTank

## PlugFlowReactor

**Description:** A type of reactor where the fluid flows in one direction through the tube

**Superclass:** Reactor

## ContinuouslyStirredTankReactor

**Description:** A reactor in which contents are well mixed and reactants are added continuously

**Superclass:** Reactor

## StaticMixer

**Description:** A device for mixing liquids without moving components

**Superclass:** Reactor

## Aeration Basin

**Description:** A tank where water is aerated to remove gases and volatile organic compounds

**Superclass:** Reactor

## Mixing Basin

**Description:** A tank where mixed liquor is stirred without aeration

**Superclass:** Reactor

## Membrane Aerated Biofilm Reactor

**Description:** A reactor that grows biofilm on membranes supplied with air

**Superclass:** Reactor

## Coagulation Basin

**Description:** A basin where coagulation occurs to destabilize particles in water

**Superclass:** Reactor

## Flocculation Basin

**Description:** A tank where flocculation occurs to aggregate particles in water

**Superclass:** Reactor

## Digester

**Description:** A container to promote decomposition of organic waste

**Superclass:** Reactor

## Digester

**Description:** A container to promote decomposition of organic waste

**Superclass:** UnitProcess

## Anaerobic Digester

**Description:** A container to promote decomposition of organic waste in anaerobic conditions

**Superclass:** Digester

## Aerobic Digester

**Description:** A container to promote decomposition of organic waste in aerobic conditions

**Superclass:** Digester

## Disinfection Unit

**Description:** A unit used to eliminate or reduce harmful microorganisms

**Superclass:** Reactor

## Chlorination Unit

**Description:** A unit that uses chlorine or chlorine compounds for disinfection.

**Superclass:** DisinfectionUnit

## Ultravioletlight Unit

**Description:** A unit using ultraviolet light for disinfection

**Superclass:** DisinfectionUnit

## Sedimentation Tank

**Description:** A tank used to remove solids from liquids through sedimentation

**Superclass:** SeparationTank

## Septic Tank

**Description:** A septic tank for on-site wastewater treatment

**Superclass:** SedimentationTank

## Imhoff Tank

**Description:** A sedimentation tank specifically designed for septic treatment

**Superclass:** SepticTank

## Screen

**Description:** An equipment used for separation

**Superclass:** Equipment

## Screen

**Description:** An equipment used for separation

**Superclass:** UnitProcess

## Grit Chamber

**Description:** A chamber used to remove grit from wastewater

**Superclass:** Equipment

## Grit Chamber

**Description:** A chamber used to remove grit from wastewater

**Superclass:** UnitProcess

## Reservoir

**Description:** A large natural or artificial body of water used for water supply

**Superclass:** Equipment

## Pond

**Description:** A body of still water smaller than a lake, used for treatment or storage.

**Superclass:** Equipment

## Wetland

**Description:** A marsh or bog-like area that is permanently or seasonally saturated with water, used for pre- or post-treatment.

**Superclass:** Equipment

## Battery

**Description:** A device that stores energy for later use

**Superclass:** Battery

## Cogenerator

**Description:** An equipment that produces both electricity and heat from the same energy source

**Superclass:** Equipment

## Cogenerator

**Description:** An equipment that produces both electricity and heat from the same energy source

**Superclass:** UnitProcess

## Boiler

**Description:** A device for heating water

**Superclass:** Boiler

## Boiler

**Description:** A device for heating water

**Superclass:** UnitProcess

## Conditioner

**Description:** An equipment used to prepare raw biogas from a digester by removing impurities

**Superclass:** Equipment

## Flare

**Description:** A device used to burn off unwanted gas

**Superclass:** Equipment

## Pump

**Description:** A device used to move fluids by mechanical action

**Superclass:** Pump

## PressureExchanger

**Description:** A device used to transfer pressure energy from one fluid to another

**Superclass:** Equipment

## Dewatering Unit

**Description:** A unit used to remove water from solid material

**Superclass:** Equipment

## Dewatering Unit

**Description:** A unit used to remove water from solid material

**Superclass:** UnitProcess

## Thickener

**Description:** A device used to increase the solids concentration of a slurry

**Superclass:** Equipment

## Thickener

**Description:** A device used to increase the solids concentration of a slurry

**Superclass:** UnitProcess

## Dissolved Air Flotation Thickener

**Description:** A thickener that uses dissolved air to separate solids from liquids

**Superclass:** Thickener

## Centrifugal Thickener

**Description:** A thickener that uses centrifugal force to separate solids from liquids

**Superclass:** Thickener

## Gravity Thickener

**Description:** A thickener that uses gravity to separate solids from liquids

**Superclass:** Thickener

## Belt Thickener

**Description:** A thickener that uses a belt system to separate solids from liquids

**Superclass:** Thickener

## Gravity Belt Thickener

**Description:** A belt thickener in which gravity drains water through a porous moving belt. It uses filtration rather than the sedimentation mechanism of a conventional gravity thickener.

**Superclass:** BeltThickener

## Rotary Drum Thickener

**Description:** A thickener that uses a rotating drum to separate solids from liquids

**Superclass:** Thickener

## Belt Filter Press

**Description:** A dewatering unit that uses a belt system to separate solids from liquids

**Superclass:** DewateringUnit

## Centrifugal Dewatering Unit

**Description:** A dewatering unit that uses centrifugal force to separate solids from liquids

**Superclass:** DewateringUnit

## Filter

**Description:** An equipment used to remove impurities from liquids or gases

**Superclass:** Filter

## Filter

**Description:** An equipment used to remove impurities from liquids or gases

**Superclass:** UnitProcess

## Reverse Osmosis Membrane

**Description:** A membrane used for reverse osmosis

**Superclass:** Filter

## Rotating Biological Contactor (RBC)

**Description:** Fixed-film process using a slowly rotating discs partially submerged in a tank

**Superclass:** Reactor

## Rotating Biological Contactor (RBC)

**Description:** Fixed-film process using a slowly rotating discs partially submerged in a tank

**Superclass:** Filter

## Moving Bed Bioreactor (MBBR)

**Description:** MBBR process using suspended growth media a tank

**Superclass:** Reactor

## Moving Bed Bioreactor (MBBR)

**Description:** MBBR process using suspended growth media a tank

**Superclass:** Filter

## Trickling Filter

**Description:** A filter system that treats wastewater by trickling it over a bed of rocks or plastic

**Superclass:** Filter

## Oxidation Ditch

**Description:** Modified activated sludge process that uses a ring-shaped channel to biologically remove pollutants

**Superclass:** Reactor

## Membrane Bioreactor

**Description:** A filter system that combines a membrane process like microfiltration with a biological reactor

**Superclass:** Filter

## Membrane Bioreactor

**Description:** A filter system that combines a membrane process like microfiltration with a biological reactor

**Superclass:** Reactor

## Membrane Bioreactor

**Description:** A filter system that combines a membrane process like microfiltration with a biological reactor

**Superclass:** SeparationTank

## Microfiltration Unit

**Description:** A filter system which removes contaminants from a liquid by passing it through a microporous membrane

**Superclass:** Filter

## Ultrafiltration Unit

**Description:** A filter system that uses a pressure-driven barrier to separate particles and solutes in a fluid

**Superclass:** Filter

## Nanofiltration Unit

**Description:** A filter system that uses a membrane to soften water and remove organic contaminants

**Superclass:** Filter

## MediaFiltration Unit

**Description:** A filter system that uses a bed of material to filter out contaminants

**Superclass:** Filter

## Rapid Sand Filter

**Description:** A type of media filter that uses sand as the filter medium and operates at high filtration rates.

**Superclass:** MediaFiltrationUnit

## Cartridge Filtration Unit

**Description:** A filter system using a cartridge to remove contaminants from fluids

**Superclass:** Filter

## Ion Exchange Membrane

**Description:** A membrane that selectively allows ions to pass through while blocking other substances

**Superclass:** Equipment

## Ion Exchange Membrane

**Description:** A membrane that selectively allows ions to pass through while blocking other substances

**Superclass:** UnitProcess

## Electrodialysis

**Description:** A unit that uses electricity to drive ion movement through a membrane

**Superclass:** Equipment

## Electrodialysis

**Description:** A unit that uses electricity to drive ion movement through a membrane

**Superclass:** UnitProcess

## Electrolyzer

**Description:** An equipment that uses electricity to split liquids into constituent elements

**Superclass:** Equipment

## Electrolyzer

**Description:** An equipment that uses electricity to split liquids into constituent elements

**Superclass:** UnitProcess

## Crystallizer

**Description:** An equipment used to produce solid crystals from a solution

**Superclass:** Equipment

## Crystallizer

**Description:** An equipment used to produce solid crystals from a solution

**Superclass:** UnitProcess

## Compressor

**Description:** An equipment that increases the pressure of a gas

**Superclass:** Compressor

## Evaporator

**Description:** A device used to turn the liquid form of a substance into its gaseous form

**Superclass:** HeatExchanger

## Evaporator

**Description:** A device used to turn the liquid form of a substance into its gaseous form

**Superclass:** UnitProcess

## Condenser

**Description:** A device used to condense a gaseous substance back into a liquid

**Superclass:** HeatExchanger

## Condenser

**Description:** A device used to condense a gaseous substance back into a liquid

**Superclass:** UnitProcess

## Flow Sensor

**Description:** A sensor used to measure the flow rate of liquids or gases

**Superclass:** FlowSensor

## Volume Sensor

**Description:** A sensor used to measure the volume of a substance

**Superclass:** Sensor

## Level Sensor

**Description:** A sensor used to detect the level of liquids or solids in a tank

**Superclass:** Sensor

## Pressure Sensor

**Description:** A sensor used to measure pressure

**Superclass:** PressureSensor

## Temperature Sensor

**Description:** A sensor used to measure temperature

**Superclass:** TemperatureSensor

## Concentration Sensor

**Description:** A sensor used to measure the concentration of specific substances (e.g., Total Dissolved Solids)

**Superclass:** ConcentrationSensor

## Oxygen Meter

**Description:** A sensor used to measure the concentration of oxygen

**Superclass:** ConcentrationSensor

## OxygenDemand Sensor

**Description:** A sensor used to measure Chemical Oxygen Demand (COD) and Biological Oxygen Demand (BOD)

**Superclass:** Sensor

## pH Sensor

**Description:** A sensor used to measure the pH of a solution

**Superclass:** ConcentrationSensor

## Conductivity Sensor

**Description:** A sensor used to measure the electrical conductivity of a solution

**Superclass:** Sensor

## Turbidity Meter

**Description:** A sensor used to measure the turbidity (clarity) of a fluid

**Superclass:** Sensor

## Rotation Sensor

**Description:** A sensor used to measure the rotational speed or position of an object

**Superclass:** Sensor

## Efficiency Sensor

**Description:** A sensor used to measure the efficiency of a system or equipment

**Superclass:** Sensor

## State of Charge Sensor

**Description:** A sensor used to measure the remaining charge in a battery or energy storage system

**Superclass:** Sensor

## Speed Sensor

**Description:** A sensor used to measure the speed of an object or fluid

**Superclass:** Sensor

## Frequency Sensor

**Description:** A sensor used to measure the frequency of a signal or mechanical vibration

**Superclass:** Sensor

## TOC Sensor

**Description:** A sensor used to measure the total organic compound concentration

**Superclass:** ConcentrationSensor

## Valve

**Description:** A device that regulates, directs or controls the flow of a fluid (gases or liquids) by opening, closing, or partially obstructing various passageways.

**Superclass:** Valve

## Variable Frequency Drive

**Description:** A type of AC motor drive that controls speed and torque by varying the frequency of the input electricity.

**Superclass:** VariableFrequencyDrive

## Three Way Valve

**Description:** A valve that features three ports (connections)

**Superclass:** Valve

## Check Valve

**Description:** A valve that normally allows fluid (liquid or gas) to flow through it in only one direction

**Superclass:** Valve

## Ball Valve

**Description:** A valve which operates using a spherical ball with a hole (also known as a bore) through the middle.

**Superclass:** Valve

## Butterfly Valve

**Description:** A quarter-turn rotary valve used to isolate, start, stop, or regulate the flow of fluids

**Superclass:** Valve

## Globe Valve

**Description:** A linear-motion valve primarily used for stopping, starting, and regulating (throttling) fluid flow

**Superclass:** Valve

## Plug Valve

**Description:** A valve with cylindrical or conically tapered plugs which can be rotated inside the valve body to control flow through the valve

**Superclass:** Valve

## Air Release Valve

**Description:** Valve for vent trapped air pockets

**Superclass:** Valve

## Controller

**Description:** A piece of equipment for regulation of a system or component in normal operation, which executes one or more `Function`s.

**Superclass:** Controller

## Manual Measurement Port

**Description:** A location where manual measurements are taken

**Superclass:** Sensor

## Multifunctional Membrane

**Description:** A membrane integrating multiple processes (e.g., reduction, adsorption, filtration) for selective removal and recovery of contaminants.

**Superclass:** Filter

## Molybdenum Sulfide (MoS2)-based Membrane

**Description:** A specific material demonstrating effectiveness in removing heavy metals and oxyanions with high selectivity.

**Superclass:** Filter

## Electrically Conducting Membrane

**Description:** A membrane capable of conducting electricity, used for in-situ cleaning or electro-oxidation processes.

**Superclass:** Filter

## Electro-Dialytic Crystallizer (EDC)

**Description:** A modular system designed for brine concentration and crystallization, integrating electrodialysis and crystallization.

**Superclass:** Equipment

## Electro-Dialytic Crystallizer (EDC)

**Description:** A modular system designed for brine concentration and crystallization, integrating electrodialysis and crystallization.

**Superclass:** UnitProcess

## Electrode

**Description:** A component where electrochemical reactions occur in electrified processes.

**Superclass:** Equipment

## Anode

**Description:** An electrode where oxidation occurs, often a sacrificial component in electrocoagulation.

**Superclass:** Electrode

## Cathode

**Description:** An electrode where reduction occurs.

**Superclass:** Electrode

## Electromagnetic Field (EMF) Device

**Description:** A device that generates an electromagnetic field, used as a pretreatment method for membrane scaling and fouling control.

**Superclass:** Equipment

## Solvent Extraction System

**Description:** A system that uses a solvent to selectively extract water from highly saline brines.

**Superclass:** Equipment

## Solvent Extraction System

**Description:** A system that uses a solvent to selectively extract water from highly saline brines.

**Superclass:** UnitProcess

## Dimethyl Ether (DME) Recovery System

**Description:** A system designed to recover a high percentage of Dimethyl Ether solvent in solvent-driven processes.

**Superclass:** Equipment

## Standardized Flow Cell

**Description:** An experimental apparatus developed for research experiments, for example in Electrocoagulation (EC), in continuous flow mode.

**Superclass:** Equipment

## UV/H2O2 Reactor

**Description:** A specific reactor used in Advanced Oxidation Processes (AOPs) combining UV light with hydrogen peroxide.

**Superclass:** Reactor

## Biological Aerated Filter (BAF)

**Description:** A filter that uses biological processes to remove contaminants.

**Superclass:** Reactor

## Biological Aerated Filter (BAF)

**Description:** A filter that uses biological processes to remove contaminants.

**Superclass:** Filter

## Electrocoagulation Unit

**Description:** A unit that uses electrocoagulation for contaminant removal.

**Superclass:** Equipment

## Electrocoagulation Unit

**Description:** A unit that uses electrocoagulation for contaminant removal.

**Superclass:** Reactor

## Ozonation Unit

**Description:** A unit that uses ozone for water treatment.

**Superclass:** Equipment

## Ozonation Unit

**Description:** A unit that uses ozone for water treatment.

**Superclass:** Reactor

## Granular Activated Carbon (GAC) Adsorber

**Description:** A unit that uses granulated activated carbon to adsorb impurities from water.

**Superclass:** Equipment

## Granular Activated Carbon (GAC) Adsorber

**Description:** A unit that uses granulated activated carbon to adsorb impurities from water.

**Superclass:** UnitProcess

## Grinder

**Description:** Machine that shreds solid waste into tiny particles

**Superclass:** Equipment

## Grinder

**Description:** Machine that shreds solid waste into tiny particles

**Superclass:** UnitProcess

## Gate

**Description:** Tool to control water flow and isolate sections

**Superclass:** Valve

## Sluice Gate

**Description:** Large gate that slide vertically to control flow in channels, reservoirs, or treatment basins

**Superclass:** Gate
