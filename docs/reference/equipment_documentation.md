# Equipment Classes

## Aeration Basin

**Description:** A basin in a biological treatment train where air or oxygen is transferred into the mixed liquor to sustain the aerobic biomass. Named for the aeration equipment installed, not for the regime it is run in: a swing zone with diffusers that is operated unaerated is still an aeration basin, carrying Role-Anoxic.

**Superclasses:** `watr:Reactor`

## Aerobic Digester

**Description:** A container to promote decomposition of organic waste in aerobic conditions

**Superclasses:** `watr:Digester`

## Air Release Valve

**Description:** Valve for vent trapped air pockets

**Superclasses:** `s223:Valve`

## Air Stripper

**Description:** A vessel, typically a packed tower, in which air is contacted with water to transfer dissolved gases and volatile organic compounds out of the water and into an off-gas stream

**Superclasses:** `watr:SeparationTank`

## Anaerobic Digester

**Description:** A container to promote decomposition of organic waste in anaerobic conditions

**Superclasses:** `watr:Digester`

## Anode

**Description:** An electrode where oxidation occurs, often a sacrificial component in electrocoagulation.

**Superclasses:** `watr:Electrode`

## Ball Valve

**Description:** A valve which operates using a spherical ball with a hole (also known as a bore) through the middle.

**Superclasses:** `s223:Valve`

## Battery

**Description:** A device that stores energy for later use

**Superclasses:** `s223:Battery`

## Belt Filter Press

**Description:** A dewatering unit that uses a belt system to separate solids from liquids

**Superclasses:** `watr:DewateringUnit`

## Belt Thickener

**Description:** A thickener that uses a belt system to separate solids from liquids

**Superclasses:** `watr:Thickener`

## Biological Aerated Filter (BAF)

**Description:** A filter that uses biological processes to remove contaminants.

**Superclasses:** `watr:Filter`, `watr:Reactor`

## Boiler

**Description:** A device for heating water

**Superclasses:** `s223:Boiler`, `watr:UnitProcess`

## Butterfly Valve

**Description:** A quarter-turn rotary valve used to isolate, start, stop, or regulate the flow of fluids

**Superclasses:** `s223:Valve`

## Cartridge Filtration Unit

**Description:** A filter system using a cartridge to remove contaminants from fluids

**Superclasses:** `watr:Filter`

## Cathode

**Description:** An electrode where reduction occurs.

**Superclasses:** `watr:Electrode`

## Centrifugal Dewatering Unit

**Description:** A dewatering unit that uses centrifugal force to separate solids from liquids

**Superclasses:** `watr:DewateringUnit`

## Centrifugal Thickener

**Description:** A thickener that uses centrifugal force to separate solids from liquids

**Superclasses:** `watr:Thickener`

## Check Valve

**Description:** A valve that normally allows fluid (liquid or gas) to flow through it in only one direction

**Superclasses:** `s223:Valve`

## Chlorination Unit

**Description:** A unit that uses chlorine or chlorine compounds for disinfection.

**Superclasses:** `watr:DisinfectionUnit`

## Clarifier

**Description:** A sedimentation tank operated for its clarified overflow, which passes to the next stage of treatment

**Superclasses:** `watr:SedimentationTank`

## Coagulation Basin

**Description:** A basin where coagulation occurs to destabilize particles in water

**Superclasses:** `watr:Reactor`

## Cogenerator

**Description:** An equipment that produces both electricity and heat from the same energy source

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Compressor

**Description:** An equipment that increases the pressure of a gas

**Superclasses:** `s223:Compressor`

## Concentration Sensor

**Description:** A sensor used to measure the concentration of specific substances (e.g., Total Dissolved Solids)

**Superclasses:** `s223:ConcentrationSensor`

## Condenser

**Description:** A device used to condense a gaseous substance back into a liquid

**Superclasses:** `s223:HeatExchanger`, `watr:UnitProcess`

## Conditioner

**Description:** An equipment used to prepare raw biogas from a digester by removing impurities

**Superclasses:** `s223:Equipment`

## Conductivity Sensor

**Description:** A sensor used to measure the electrical conductivity of a solution

**Superclasses:** `s223:Sensor`

## ContinuouslyStirredTankReactor

**Description:** A reactor in which contents are well mixed and reactants are added continuously

**Superclasses:** `watr:Reactor`

## Controller

**Description:** A piece of equipment for regulation of a system or component in normal operation, which executes one or more `Function`s.

**Superclasses:** `s223:Controller`

## Crystallizer

**Description:** An equipment used to produce solid crystals from a solution

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Dimethyl Ether (DME) Recovery System

**Description:** A system designed to recover a high percentage of Dimethyl Ether solvent in solvent-driven processes.

**Superclasses:** `s223:Equipment`

## Dewatering Unit

**Description:** A unit used to remove water from solid material

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Digester

**Description:** A container to promote decomposition of organic waste

**Superclasses:** `watr:Reactor`, `watr:UnitProcess`

## Disinfection Unit

**Description:** A unit used to eliminate or reduce harmful microorganisms

**Superclasses:** `watr:Reactor`

## Dissolved Air Flotation Thickener

**Description:** A thickener that uses dissolved air to separate solids from liquids

**Superclasses:** `watr:Thickener`

## Efficiency Sensor

**Description:** A sensor used to measure the efficiency of a system or equipment

**Superclasses:** `s223:Sensor`

## Electrically Conducting Membrane

**Description:** A membrane capable of conducting electricity, used for in-situ cleaning or electro-oxidation processes.

**Superclasses:** `watr:Filter`

## Electro-Dialytic Crystallizer (EDC)

**Description:** A modular system designed for brine concentration and crystallization, integrating electrodialysis and crystallization.

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Electrocoagulation Unit

**Description:** A unit that uses electrocoagulation for contaminant removal.

**Superclasses:** `s223:Equipment`, `watr:Reactor`

## Electrode

**Description:** A component where electrochemical reactions occur in electrified processes.

**Superclasses:** `s223:Equipment`

## Electrodialysis

**Description:** A unit that uses electricity to drive ion movement through a membrane

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Electrolyzer

**Description:** An equipment that uses electricity to split liquids into constituent elements

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Electromagnetic Field (EMF) Device

**Description:** A device that generates an electromagnetic field, used as a pretreatment method for membrane scaling and fouling control.

**Superclasses:** `s223:Equipment`

## Equipment Region

**Description:** An identifiable functional portion of a piece of equipment, distinguished by its treatment activity. It need not be physically partitioned or independently installed. Each region has exactly one direct equipment parent, at least one process, and at least one connection point. Nested regions must ultimately belong to equipment that is not itself a region. Roles are optional.

**Superclasses:** `s223:Equipment`

## Evaporator

**Description:** A device used to turn the liquid form of a substance into its gaseous form

**Superclasses:** `s223:HeatExchanger`, `watr:UnitProcess`

## Filter

**Description:** An equipment used to remove impurities from liquids or gases

**Superclasses:** `s223:Filter`, `watr:UnitProcess`

## Flare

**Description:** A device used to burn off unwanted gas

**Superclasses:** `s223:Equipment`

## Flocculation Basin

**Description:** A tank where flocculation occurs to aggregate particles in water

**Superclasses:** `watr:Reactor`

## Flow Sensor

**Description:** A sensor used to measure the flow rate of liquids or gases

**Superclasses:** `s223:FlowSensor`

## Frequency Sensor

**Description:** A sensor used to measure the frequency of a signal or mechanical vibration

**Superclasses:** `s223:Sensor`

## Gate

**Description:** Tool to control water flow and isolate sections

**Superclasses:** `s223:Valve`

## Globe Valve

**Description:** A linear-motion valve primarily used for stopping, starting, and regulating (throttling) fluid flow

**Superclasses:** `s223:Valve`

## Granular Activated Carbon (GAC) Adsorber

**Description:** A unit that uses granulated activated carbon to adsorb impurities from water.

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Gravity Belt Thickener

**Description:** A belt thickener in which gravity drains water through a porous moving belt. It uses filtration rather than the sedimentation mechanism of a conventional gravity thickener.

**Superclasses:** `watr:BeltThickener`

## Gravity Thickener

**Description:** A thickener that uses gravity to separate solids from liquids

**Superclasses:** `watr:Thickener`

## Grinder

**Description:** Machine that shreds solid waste into tiny particles

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Grit Chamber

**Description:** A chamber used to remove grit from wastewater

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Imhoff Tank

**Description:** A sedimentation tank specifically designed for septic treatment

**Superclasses:** `watr:SepticTank`

## Ion Exchange Membrane

**Description:** A membrane that selectively allows ions to pass through while blocking other substances

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Level Sensor

**Description:** A sensor used to detect the level of liquids or solids in a tank

**Superclasses:** `s223:Sensor`

## Manual Measurement Port

**Description:** A location where manual measurements are taken

**Superclasses:** `s223:Sensor`

## MediaFiltration Unit

**Description:** A filter system that uses a bed of material to filter out contaminants

**Superclasses:** `watr:Filter`

## Membrane Aerated Biofilm Reactor

**Description:** A reactor that grows biofilm on membranes supplied with air

**Superclasses:** `watr:Reactor`

## Membrane Bioreactor

**Description:** A filter system that combines a membrane process like microfiltration with a biological reactor

**Superclasses:** `watr:Filter`, `watr:Reactor`, `watr:SeparationTank`

## Microfiltration Unit

**Description:** A filter system which removes contaminants from a liquid by passing it through a microporous membrane

**Superclasses:** `watr:Filter`

## Mixing Basin

**Description:** A tank where mixed liquor is stirred without aeration

**Superclasses:** `watr:Reactor`

## Molybdenum Sulfide (MoS2)-based Membrane

**Description:** A specific material demonstrating effectiveness in removing heavy metals and oxyanions with high selectivity.

**Superclasses:** `watr:Filter`

## Moving Bed Bioreactor (MBBR)

**Description:** MBBR process using suspended growth media a tank

**Superclasses:** `watr:Filter`, `watr:Reactor`

## Multifunctional Membrane

**Description:** A membrane integrating multiple processes (e.g., reduction, adsorption, filtration) for selective removal and recovery of contaminants.

**Superclasses:** `watr:Filter`

## Nanofiltration Unit

**Description:** A membrane filter with a pore size between ultrafiltration and reverse osmosis, which rejects divalent ions and larger organic molecules while passing most monovalent salts

**Superclasses:** `watr:Filter`

## Oxidation Ditch

**Description:** Modified activated sludge process that uses a ring-shaped channel to biologically remove pollutants

**Superclasses:** `watr:Reactor`

## OxygenDemand Sensor

**Description:** A sensor used to measure Chemical Oxygen Demand (COD) and Biological Oxygen Demand (BOD)

**Superclasses:** `s223:Sensor`

## Oxygen Meter

**Description:** A sensor used to measure the concentration of oxygen

**Superclasses:** `s223:ConcentrationSensor`

## Ozonation Unit

**Description:** A unit that uses ozone for water treatment.

**Superclasses:** `watr:UnitProcess`

## PlugFlowReactor

**Description:** A type of reactor where the fluid flows in one direction through the tube

**Superclasses:** `watr:Reactor`

## Plug Valve

**Description:** A valve with cylindrical or conically tapered plugs which can be rotated inside the valve body to control flow through the valve

**Superclasses:** `s223:Valve`

## Pond

**Description:** A body of still water smaller than a lake, used for treatment or storage.

**Superclasses:** `s223:Equipment`

## PressureExchanger

**Description:** A device used to transfer pressure energy from one fluid to another

**Superclasses:** `s223:Equipment`

## Pressure Sensor

**Description:** A sensor used to measure pressure

**Superclasses:** `s223:PressureSensor`

## Pump

**Description:** A device used to move fluids by mechanical action

**Superclasses:** `s223:Pump`

## Rapid Sand Filter

**Description:** A type of media filter that uses sand as the filter medium and operates at high filtration rates.

**Superclasses:** `watr:MediaFiltrationUnit`

## Reactor

**Description:** A vessel in which a reaction or biological/chemical treatment process takes place

**Superclasses:** `watr:Tank`, `watr:UnitProcess`

## Reservoir

**Description:** A large natural or artificial body of water used for water supply

**Superclasses:** `s223:Equipment`

## Reverse Osmosis Membrane

**Description:** A membrane used for reverse osmosis

**Superclasses:** `watr:Filter`

## Rotary Drum Thickener

**Description:** A thickener that uses a rotating drum to separate solids from liquids

**Superclasses:** `watr:Thickener`

## Rotating Biological Contactor (RBC)

**Description:** Fixed-film process using a slowly rotating discs partially submerged in a tank

**Superclasses:** `watr:Filter`, `watr:Reactor`

## Rotation Sensor

**Description:** A sensor used to measure the rotational speed or position of an object

**Superclasses:** `s223:Sensor`

## Screen

**Description:** An equipment used for separation

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Sedimentation Tank

**Description:** A tank in which suspended solids separate from water by settling under gravity

**Superclasses:** `watr:SeparationTank`

## Separation Tank

**Description:** A tank that has at least two outlets (e.g. overflow and underflow)

**Superclasses:** `watr:Tank`, `watr:UnitProcess`

## Septic Tank

**Description:** A septic tank for on-site wastewater treatment

**Superclasses:** `watr:SedimentationTank`

## SequencingBatchReactor

**Description:** A type of activated sludge process for wastewater treatment

**Superclasses:** `watr:Reactor`, `watr:SeparationTank`

## Sluice Gate

**Description:** Large gate that slide vertically to control flow in channels, reservoirs, or treatment basins

**Superclasses:** `watr:Gate`

## Solvent Extraction System

**Description:** A system that uses a solvent to selectively extract water from highly saline brines.

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Speed Sensor

**Description:** A sensor used to measure the speed of an object or fluid

**Superclasses:** `s223:Sensor`

## Standardized Flow Cell

**Description:** An experimental apparatus developed for research experiments, for example in Electrocoagulation (EC), in continuous flow mode.

**Superclasses:** `s223:Equipment`

## State of Charge Sensor

**Description:** A sensor used to measure the remaining charge in a battery or energy storage system

**Superclasses:** `s223:Sensor`

## StaticMixer

**Description:** A device for mixing liquids without moving components

**Superclasses:** `watr:Reactor`

## Tank

**Description:** A vessel with at least one fluid connection point. A storage tank may use a single bidirectional port; flow-through subclasses require the appropriate inlet and outlet points.

**Superclasses:** `s223:Equipment`

## Temperature Sensor

**Description:** A sensor used to measure temperature

**Superclasses:** `s223:TemperatureSensor`

## Thickener

**Description:** A device used to increase the solids concentration of a slurry

**Superclasses:** `s223:Equipment`, `watr:UnitProcess`

## Three Way Valve

**Description:** A valve that features three ports (connections)

**Superclasses:** `s223:Valve`

## TOC Sensor

**Description:** A sensor used to measure the total organic compound concentration

**Superclasses:** `watr:ConcentrationSensor`

## Trickling Filter

**Description:** A filter system that treats wastewater by trickling it over a bed of rocks or plastic

**Superclasses:** `watr:Filter`

## Turbidity Meter

**Description:** A sensor used to measure the turbidity (clarity) of a fluid

**Superclasses:** `s223:Sensor`

## UV/H2O2 Reactor

**Description:** A specific reactor used in Advanced Oxidation Processes (AOPs) combining UV light with hydrogen peroxide.

**Superclasses:** `watr:Reactor`

## Ultrafiltration Unit

**Description:** A filter system that uses a pressure-driven barrier to separate particles and solutes in a fluid

**Superclasses:** `watr:Filter`

## Ultravioletlight Unit

**Description:** A unit using ultraviolet light for disinfection

**Superclasses:** `watr:DisinfectionUnit`

## Valve

**Description:** A device that regulates, directs or controls the flow of a fluid (gases or liquids) by opening, closing, or partially obstructing various passageways.

**Superclasses:** `s223:Valve`

## Variable Frequency Drive

**Description:** A type of AC motor drive that controls speed and torque by varying the frequency of the input electricity.

**Superclasses:** `s223:VariableFrequencyDrive`

## Volume Sensor

**Description:** A sensor used to measure the volume of a substance

**Superclasses:** `s223:Sensor`

## Wetland

**Description:** A marsh or bog-like area that is permanently or seasonally saturated with water, used for pre- or post-treatment.

**Superclasses:** `s223:Equipment`

## pH Sensor

**Description:** A sensor used to measure the pH of a solution

**Superclasses:** `watr:ConcentrationSensor`
