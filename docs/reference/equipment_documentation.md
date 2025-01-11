# Equipment Classes

## Tank

**Description:** A tank for storing liquid

**Superclass:** Equipment

## Reactor

**Description:** An equipment used for chemical reaction

**Superclass:** Tank

## SequencingBatchReactor

**Description:** A type of activated sludge process for wastewater treatment

**Superclass:** Reactor

## PlugFlowReactor

**Description:** A type of reactor where the fluid flows in one direction through the tube

**Superclass:** Reactor

## ContinuouslyStirredTankReactor

**Description:** A reactor in which contents are well mixed and reactants are added continuously

**Superclass:** Reactor

## StaticMixer

**Description:** A device for mixing liquids without moving components

**Superclass:** Reactor

## AerationBasin

**Description:** A tank where water is aerated to remove gases and volatile organic compounds

**Superclass:** Reactor

## Digester

**Description:** A container to promote decomposition of organic waste

**Superclass:** Tank

## AnaerobicDigester

**Description:** A container to promote decomposition of organic waste in anaerobic conditions

**Superclass:** Digester

## AerobicDigester

**Description:** A container to promote decomposition of organic waste in aerobic conditions

**Superclass:** Digester

## Disinfection

**Description:** A unit used to eliminate or reduce harmful microorganisms

**Superclass:** Tank

## UltravioletlightUnit

**Description:** A unit using ultraviolet light for disinfection

**Superclass:** Disinfection

## ChlorinationBasin

**Description:** A basin where chlorine is added for disinfection

**Superclass:** Disinfection

## SedimentationTank

**Description:** A tank used to remove solids from liquids through sedimentation

**Superclass:** Tank

## Screen

**Description:** An equipment used for separation

**Superclass:** Equipment

## Grit Chamber

**Description:** A chamber used to remove grit from wastewater

**Superclass:** Equipment

## Reservoir

**Description:** A large natural or artificial body of water used for water supply

**Superclass:** Equipment

## Pond

**Description:** A body of still water smaller than a lake, used for treatment or storage

**Superclass:** Equipment

## Battery

**Description:** A device that stores energy for later use

**Superclass:** Battery

## Cogenerator

**Description:** An equipment that produces both electricity and heat from the same energy source

**Superclass:** Equipment

## Boiler

**Description:** A device for heating water

**Superclass:** Boiler

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

## Dewatering

**Description:** A unit used to remove water from solid material

**Superclass:** Equipment

## Thickener

**Description:** A device used to increase the solids concentration of a slurry

**Superclass:** Equipment

## DissolvedAirFlotationThickener

**Description:** A thickener that uses dissolved air to separate solids from liquids

**Superclass:** Thickener

## CentrifugalThickener

**Description:** A thickener that uses centrifugal force to separate solids from liquids

**Superclass:** Thickener

## GravityThickener

**Description:** A thickener that uses gravity to separate solids from liquids

**Superclass:** Thickener

## BeltThickener

**Description:** A thickener that uses a belt system to separate solids from liquids

**Superclass:** Thickener

## Gravity Belt Thickener

**Description:** A thickener that combines gravity separation with a belt system

**Superclass:** BeltThickener

## Rotary Drum Thickener

**Description:** A thickener that uses a rotating drum to separate solids from liquids

**Superclass:** Thickener

## Filter

**Description:** An equipment used to remove impurities from liquids or gases

**Superclass:** Filter

## ReverseOsmosisMembrane

**Description:** A membrane used for reverse osmosis

**Superclass:** Filter

## TricklingFilter

**Description:** A filter system that treats wastewater by trickling it over a bed of rocks or plastic

**Superclass:** Filter

## MembraneBioreactor

**Description:** A filter system that combines a membrane process like microfiltration with a biological reactor

**Superclass:** Filter

## MicrofiltrationUnit

**Description:** A filter system which removes contaminants from a liquid by passing it through a microporous membrane

**Superclass:** Filter

## UltrafiltrationUnit

**Description:** A filter system that uses a pressure-driven barrier to separate particles and solutes in a fluid

**Superclass:** Filter

## NanofiltrationUnit

**Description:** A filter system that uses a membrane to soften water and remove organic contaminants

**Superclass:** Filter

## MediaFiltrationUnit

**Description:** A filter system that uses a bed of material to filter out contaminants

**Superclass:** Filter

## CartridgeFiltrationUnit

**Description:** A filter system using a cartridge to remove contaminants from fluids

**Superclass:** Filter

## IonExchangeMembrane

**Description:** A membrane that selectively allows ions to pass through while blocking other substances

**Superclass:** Equipment

## Electrodialysis

**Description:** A unit that uses electricity to drive ion movement through a membrane

**Superclass:** Equipment

## Electrolyzer

**Description:** An equipment that uses electricity to split liquids into constituent elements

**Superclass:** Equipment

## Crystallizer

**Description:** An equipment used to produce solid crystals from a solution

**Superclass:** Equipment

## Compressor

**Description:** An equipment that increases the pressure of a gas

**Superclass:** Compressor

## Evaporator

**Description:** A device used to turn the liquid form of a substance into its gaseous form

**Superclass:** HeatExchanger

## Condenser

**Description:** A device used to condense a gaseous substance back into a liquid

**Superclass:** HeatExchanger

## FlowSensor

**Description:** A sensor used to measure the flow rate of liquids or gases

**Superclass:** FlowSensor

## VolumeSensor

**Description:** A sensor used to measure the volume of a substance

**Superclass:** Sensor

## LevelSensor

**Description:** A sensor used to detect the level of liquids or solids in a tank

**Superclass:** Sensor

## PressureSensor

**Description:** A sensor used to measure pressure

**Superclass:** PressureSensor

## TemperatureSensor

**Description:** A sensor used to measure temperature

**Superclass:** TemperatureSensor

## RunTimeSensor

**Description:** A sensor used to measure the operating time of equipment

**Superclass:** Sensor

## RunStatusSensor

**Description:** A sensor used to monitor the operational status of equipment

**Superclass:** Sensor

## ConcentrationSensor

**Description:** A sensor used to measure the concentration of specific substances (e.g., Total Dissolved Solids)

**Superclass:** ConcentrationSensor

## Oxygen Meter

**Description:** A sensor used to measure the concentration of oxygen

**Superclass:** ConcentrationSensor

## OxygenDemandSensor

**Description:** A sensor used to measure Chemical Oxygen Demand (COD) and Biological Oxygen Demand (BOD)

**Superclass:** Sensor

## pHSensor

**Description:** A sensor used to measure the pH of a solution

**Superclass:** ConcentrationSensor

## ConductivitySensor

**Description:** A sensor used to measure the electrical conductivity of a solution

**Superclass:** Sensor

## TurbidityMeter

**Description:** A sensor used to measure the turbidity (clarity) of a fluid

**Superclass:** Sensor

## RotationSensor

**Description:** A sensor used to measure the rotational speed or position of an object

**Superclass:** Sensor

## EfficiencySensor

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

