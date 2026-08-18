# NAWI Water Equipment Ontology

## NAWI Water Equipment Ontology

**Description:** An ontology for water equipment used in the NAWI project

**URI:** https://watermetadata.org/ontology/modules/equipment

## Tank

**Description:** A tank with at least one inlet and one outlet for liquid; may include optional drain or overflow connection points. Used for storage and as the base for reactors and separation tanks.

**URI:** https://watermetadata.org/ontology/watr#Tank

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Reactor

**Description:** A tank used for reaction or biological/chemical treatment; may include recirculation or return connection points (e.g. for RAS, internal recycle).

**URI:** https://watermetadata.org/ontology/watr#Reactor

**Superclass URI :** https://watermetadata.org/ontology/watr#Tank

## SeparationTank

**Description:** A tank that separates phases or streams; must have at least two outlets (e.g. clarified flow and sludge, or overflow and underflow).

**URI:** https://watermetadata.org/ontology/watr#SeparationTank

**Superclass URI :** https://watermetadata.org/ontology/watr#Tank

## SequencingBatchReactor

**Description:** A type of activated sludge process for wastewater treatment

**URI:** https://watermetadata.org/ontology/watr#SequencingBatchReactor

**Superclass URI :** https://watermetadata.org/ontology/watr#Reactor, https://watermetadata.org/ontology/watr#SeparationTank

## PlugFlowReactor

**Description:** A type of reactor where the fluid flows in one direction through the tube

**URI:** https://watermetadata.org/ontology/watr#PlugFlowReactor

**Superclass URI :** https://watermetadata.org/ontology/watr#Reactor

## ContinuouslyStirredTankReactor

**Description:** A reactor in which contents are well mixed and reactants are added continuously

**URI:** https://watermetadata.org/ontology/watr#ContinuouslyStirredTankReactor

**Superclass URI :** https://watermetadata.org/ontology/watr#Reactor

## StaticMixer

**Description:** A device for mixing liquids without moving components

**URI:** https://watermetadata.org/ontology/watr#StaticMixer

**Superclass URI :** https://watermetadata.org/ontology/watr#Reactor

## AerationBasin

**Description:** A tank where water is aerated to remove gases and volatile organic compounds

**URI:** https://watermetadata.org/ontology/watr#AerationBasin

**Superclass URI :** https://watermetadata.org/ontology/watr#Reactor

## MixingBasin

**Description:**  A tank where mixed liquor is stirred without aeration

**URI:** https://watermetadata.org/ontology/watr#MixingBasin

**Superclass URI :** https://watermetadata.org/ontology/watr#Reactor

## Digester

**Description:** A container to promote decomposition of organic waste

**URI:** https://watermetadata.org/ontology/watr#Digester

**Superclass URI :** https://watermetadata.org/ontology/watr#Reactor

## AnaerobicDigester

**Description:** A container to promote decomposition of organic waste in anaerobic conditions

**URI:** https://watermetadata.org/ontology/watr#AnaerobicDigester

**Superclass URI :** https://watermetadata.org/ontology/watr#Digester

## AerobicDigester

**Description:** A container to promote decomposition of organic waste in aerobic conditions

**URI:** https://watermetadata.org/ontology/watr#AerobicDigester

**Superclass URI :** https://watermetadata.org/ontology/watr#Digester

## Disinfection

**Description:** A unit used to eliminate or reduce harmful microorganisms

**URI:** https://watermetadata.org/ontology/watr#DisinfectionUnit

**Superclass URI :** https://watermetadata.org/ontology/watr#Tank

## UltravioletlightUnit

**Description:** A unit using ultraviolet light for disinfection

**URI:** https://watermetadata.org/ontology/watr#UltravioletLightUnit

**Superclass URI :** https://watermetadata.org/ontology/watr#DisinfectionUnit

## ChlorinationUnit

**Description:** A unit that uses chlorine or chlorine compounds for disinfection.

**URI:** https://watermetadata.org/ontology/watr#ChlorinationUnit

**Superclass URI :** https://watermetadata.org/ontology/watr#DisinfectionUnitUnit

## SedimentationTank

**Description:** A tank used to remove solids from liquids through sedimentation

**URI:** https://watermetadata.org/ontology/watr#SedimentationTank

**Superclass URI :** https://watermetadata.org/ontology/watr#SeparationTank

## SepticTank

**Description:** A septic tank for on-site wastewater treatment

**URI:** https://watermetadata.org/ontology/watr#SepticTank

**Superclass URI :** https://watermetadata.org/ontology/watr#SedimentationTank

## ImhoffTank

**Description:** A sedimentation tank specifically designed for septic treatment

**URI:** https://watermetadata.org/ontology/watr#ImhoffTank

**Superclass URI :** https://watermetadata.org/ontology/watr#SepticTank

## Screen

**Description:** An equipment used for separation

**URI:** https://watermetadata.org/ontology/watr#Screen

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Grit Chamber

**Description:** A chamber used to remove grit from wastewater

**URI:** https://watermetadata.org/ontology/watr#GritChamber

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Reservoir

**Description:** A large natural or artificial body of water used for water supply

**URI:** https://watermetadata.org/ontology/watr#Reservoir

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Pond

**Description:** A body of still water smaller than a lake, used for treatment or storage

**URI:** https://watermetadata.org/ontology/watr#Pond

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Battery

**Description:** A device that stores energy for later use

**URI:** https://watermetadata.org/ontology/watr#Battery

**Superclass URI :** http://data.ashrae.org/standard223#Battery

## Cogenerator

**Description:** An equipment that produces both electricity and heat from the same energy source

**URI:** https://watermetadata.org/ontology/watr#Cogenerator

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Boiler

**Description:** A device for heating water

**URI:** https://watermetadata.org/ontology/watr#Boiler

**Superclass URI :** http://data.ashrae.org/standard223#Boiler

## Conditioner

**Description:** An equipment used to prepare raw biogas from a digester by removing impurities

**URI:** https://watermetadata.org/ontology/watr#Conditioner

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Flare

**Description:** A device used to burn off unwanted gas

**URI:** https://watermetadata.org/ontology/watr#Flare

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Pump

**Description:** A device used to move fluids by mechanical action

**URI:** https://watermetadata.org/ontology/watr#Pump

**Superclass URI :** http://data.ashrae.org/standard223#Pump

## PressureExchanger

**Description:** A device used to transfer pressure energy from one fluid to another

**URI:** https://watermetadata.org/ontology/watr#PressureExchanger

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Dewatering

**Description:** A unit used to remove water from solid material

**URI:** https://watermetadata.org/ontology/watr#DewateringUnit

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Thickener

**Description:** A device used to increase the solids concentration of a slurry

**URI:** https://watermetadata.org/ontology/watr#Thickener

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## DissolvedAirFlotationThickener

**Description:** A thickener that uses dissolved air to separate solids from liquids

**URI:** https://watermetadata.org/ontology/watr#DissolvedAirFlotationThickener

**Superclass URI :** https://watermetadata.org/ontology/watr#Thickener

## Centrifuge

**Description:** A thickener that uses centrifugal force to separate solids from liquids

**URI:** https://watermetadata.org/ontology/watr#Centrifuge

**Superclass URI :** https://watermetadata.org/ontology/watr#Thickener

## GravityThickener

**Description:** A thickener that uses gravity to separate solids from liquids

**URI:** https://watermetadata.org/ontology/watr#GravityThickener

**Superclass URI :** https://watermetadata.org/ontology/watr#Thickener

## BeltThickener

**Description:** A thickener that uses a belt system to separate solids from liquids

**URI:** https://watermetadata.org/ontology/watr#BeltThickener

**Superclass URI :** https://watermetadata.org/ontology/watr#Thickener

## Gravity Belt Thickener

**Description:** A thickener that combines gravity separation with a belt system

**URI:** https://watermetadata.org/ontology/watr#GravityBeltThickener

**Superclass URI :** https://watermetadata.org/ontology/watr#BeltThickener

## Rotary Drum Thickener

**Description:** A thickener that uses a rotating drum to separate solids from liquids

**URI:** https://watermetadata.org/ontology/watr#RotaryDrumThickener

**Superclass URI :** https://watermetadata.org/ontology/watr#Thickener

## Filter

**Description:** An equipment used to remove impurities from liquids or gases

**URI:** https://watermetadata.org/ontology/watr#Filter

**Superclass URI :** http://data.ashrae.org/standard223#Filter

## ReverseOsmosisMembrane

**Description:** A membrane used for reverse osmosis

**URI:** https://watermetadata.org/ontology/watr#ReverseOsmosisMembrane

**Superclass URI :** https://watermetadata.org/ontology/watr#Filter

## TricklingFilter

**Description:** A filter system that treats wastewater by trickling it over a bed of rocks or plastic

**URI:** https://watermetadata.org/ontology/watr#TricklingFilter

**Superclass URI :** https://watermetadata.org/ontology/watr#Filter

## MovingBedBioreactor

**Description:** MBBR process using suspended growth media in a tank

**URI:** https://watermetadata.org/ontology/watr#MovingBedBioreactor

**Superclass URI :** https://watermetadata.org/ontology/watr#Filter

## MembraneBioreactor

**Description:** A filter system that combines a membrane process like microfiltration with a biological reactor

**URI:** https://watermetadata.org/ontology/watr#MembraneBioreactor

**Superclass URI :** https://watermetadata.org/ontology/watr#Filter, https://watermetadata.org/ontology/watr#Reactor, https://watermetadata.org/ontology/watr#SeparationTank

## MicrofiltrationUnit

**Description:** A filter system which removes contaminants from a liquid by passing it through a microporous membrane

**URI:** https://watermetadata.org/ontology/watr#MicrofiltrationUnit

**Superclass URI :** https://watermetadata.org/ontology/watr#Filter

## UltrafiltrationUnit

**Description:** A filter system that uses a pressure-driven barrier to separate particles and solutes in a fluid

**URI:** https://watermetadata.org/ontology/watr#UltrafiltrationUnit

**Superclass URI :** https://watermetadata.org/ontology/watr#Filter

## NanofiltrationUnit

**Description:** A filter system that uses a membrane to soften water and remove organic contaminants

**URI:** https://watermetadata.org/ontology/watr#NanofiltrationUnit

**Superclass URI :** https://watermetadata.org/ontology/watr#Filter

## MediaFiltrationUnit

**Description:** A filter system that uses a bed of material to filter out contaminants

**URI:** https://watermetadata.org/ontology/watr#MediaFiltrationUnit

**Superclass URI :** https://watermetadata.org/ontology/watr#Filter

## CartridgeFiltrationUnit

**Description:** A filter system using a cartridge to remove contaminants from fluids

**URI:** https://watermetadata.org/ontology/watr#CartridgeFiltrationUnit

**Superclass URI :** https://watermetadata.org/ontology/watr#Filter

## IonExchangeMembrane

**Description:** A membrane that selectively allows ions to pass through while blocking other substances

**URI:** https://watermetadata.org/ontology/watr#IonExchangeMembrane

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Electrodialysis

**Description:** A unit that uses electricity to drive ion movement through a membrane

**URI:** https://watermetadata.org/ontology/watr#ElectrodialysisUnit

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Electrolyzer

**Description:** An equipment that uses electricity to split liquids into constituent elements

**URI:** https://watermetadata.org/ontology/watr#Electrolyzer

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Crystallizer

**Description:** An equipment used to produce solid crystals from a solution

**URI:** https://watermetadata.org/ontology/watr#Crystallizer

**Superclass URI :** http://data.ashrae.org/standard223#Equipment

## Compressor

**Description:** An equipment that increases the pressure of a gas

**URI:** https://watermetadata.org/ontology/watr#Compressor

**Superclass URI :** http://data.ashrae.org/standard223#Compressor

## Evaporator

**Description:** A device used to turn the liquid form of a substance into its gaseous form

**URI:** https://watermetadata.org/ontology/watr#Evaporator

**Superclass URI :** http://data.ashrae.org/standard223#HeatExchanger

## Condenser

**Description:** A device used to condense a gaseous substance back into a liquid

**URI:** https://watermetadata.org/ontology/watr#Condenser

**Superclass URI :** http://data.ashrae.org/standard223#HeatExchanger

## FlowSensor

**Description:** A sensor used to measure the flow rate of liquids or gases

**URI:** https://watermetadata.org/ontology/watr#FlowSensor

**Superclass URI :** http://data.ashrae.org/standard223#FlowSensor

## VolumeSensor

**Description:** A sensor used to measure the volume of a substance

**URI:** https://watermetadata.org/ontology/watr#VolumeSensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## LevelSensor

**Description:** A sensor used to detect the level of liquids or solids in a tank

**URI:** https://watermetadata.org/ontology/watr#LevelSensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## PressureSensor

**Description:** A sensor used to measure pressure

**URI:** https://watermetadata.org/ontology/watr#PressureSensor

**Superclass URI :** http://data.ashrae.org/standard223#PressureSensor

## TemperatureSensor

**Description:** A sensor used to measure temperature

**URI:** https://watermetadata.org/ontology/watr#TemperatureSensor

**Superclass URI :** http://data.ashrae.org/standard223#TemperatureSensor

## RunTimeSensor

**Description:** A sensor used to measure the operating time of equipment

**URI:** https://watermetadata.org/ontology/watr#RunTimeSensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## RunStatusSensor

**Description:** A sensor used to monitor the operational status of equipment

**URI:** https://watermetadata.org/ontology/watr#RunStatusSensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## ConcentrationSensor

**Description:** A sensor used to measure the concentration of specific substances (e.g., Total Dissolved Solids)

**URI:** https://watermetadata.org/ontology/watr#ConcentrationSensor

**Superclass URI :** http://data.ashrae.org/standard223#ConcentrationSensor

## Oxygen Meter

**Description:** A sensor used to measure the concentration of oxygen

**URI:** https://watermetadata.org/ontology/watr#OxygenMeter

**Superclass URI :** http://data.ashrae.org/standard223#ConcentrationSensor

## OxygenDemandSensor

**Description:** A sensor used to measure Chemical Oxygen Demand (COD) and Biological Oxygen Demand (BOD)

**URI:** https://watermetadata.org/ontology/watr#OxygenDemandSensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## pHSensor

**Description:** A sensor used to measure the pH of a solution

**URI:** https://watermetadata.org/ontology/watr#pHSensor

**Superclass URI :** https://watermetadata.org/ontology/watr#ConcentrationSensor

## ConductivitySensor

**Description:** A sensor used to measure the electrical conductivity of a solution

**URI:** https://watermetadata.org/ontology/watr#ConductivitySensor

**Superclass URI :** https://watermetadata.org/ontology/watr#Sensor

## TurbidityMeter

**Description:** A sensor used to measure the turbidity (clarity) of a fluid

**URI:** https://watermetadata.org/ontology/watr#TurbidityMeter

**Superclass URI :** https://watermetadata.org/ontology/watr#Sensor

## RotationSensor

**Description:** A sensor used to measure the rotational speed or position of an object

**URI:** https://watermetadata.org/ontology/watr#RotationSensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## EfficiencySensor

**Description:** A sensor used to measure the efficiency of a system or equipment

**URI:** https://watermetadata.org/ontology/watr#EfficiencySensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## State of Charge Sensor

**Description:** A sensor used to measure the remaining charge in a battery or energy storage system

**URI:** https://watermetadata.org/ontology/watr#StateOfChargeSensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## Speed Sensor

**Description:** A sensor used to measure the speed of an object or fluid

**URI:** https://watermetadata.org/ontology/watr#SpeedSensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## Frequency Sensor

**Description:** A sensor used to measure the frequency of a signal or mechanical vibration

**URI:** https://watermetadata.org/ontology/watr#FrequencySensor

**Superclass URI :** http://data.ashrae.org/standard223#Sensor

## NAWI Water Substances Ontology

**Description:** An ontology for water substances used in the NAWI project

**URI:** https://watermetadata.org/ontology/modules/substances

## Constituent-Metals

**Description:** Constituent-Metals

**URI:** https://watermetadata.org/ontology/watr#Constituent-Metals

**Superclass URI :** http://data.ashrae.org/standard223#Medium-Constituent

## Constituent-Salt

**Description:** Constituent-Salt

**URI:** https://watermetadata.org/ontology/watr#Constituent-Salt

**Superclass URI :** http://data.ashrae.org/standard223#Medium-Constituent

## Salt-NaCl

**Description:** Salt-NaCl

**URI:** https://watermetadata.org/ontology/watr#Salt-NaCl

**Superclass URI :** https://watermetadata.org/ontology/watr#Constituent-Salt

## Water-Brine

**Description:** Water-Brine

**URI:** https://watermetadata.org/ontology/watr#Water-Brine

**Superclass URI :** http://data.ashrae.org/standard223#Fluid-Water

## Brine-15Percent

**Description:** Brine-15Percent

**URI:** https://watermetadata.org/ontology/watr#Brine-15Percent

**Superclass URI :** https://watermetadata.org/ontology/watr#Water-Brine

## Brine-5to10Percent

**Description:** Brine-5to10Percent

**URI:** https://watermetadata.org/ontology/watr#Brine-5to10Percent

**Superclass URI :** https://watermetadata.org/ontology/watr#Water-Brine

## Wastewater Treatment Chemical

**Description:** Base class for all chemicals used in wastewater treatment

**URI:** https://watermetadata.org/ontology/watr#WastewaterTreatmentChemical

**Superclass URI :** http://data.ashrae.org/standard223#Medium-Constituent

## Coagulant

**Description:** Class for coagulants used in wastewater treatment

**URI:** https://watermetadata.org/ontology/watr#Coagulant

**Superclass URI :** https://watermetadata.org/ontology/watr#WastewaterTreatmentChemical

## Alum

**Description:** Aluminum sulfate (alum), a common coagulant

**URI:** https://watermetadata.org/ontology/watr#Coagulant-Alum

**Superclass URI :** https://watermetadata.org/ontology/watr#Coagulant

## Ferric Chloride

**Description:** Ferric chloride, a coagulant for wastewater treatment

**URI:** https://watermetadata.org/ontology/watr#Coagulant-FerricChloride

**Superclass URI :** https://watermetadata.org/ontology/watr#Coagulant

## Polyaluminum Chloride

**Description:** Polyaluminum chloride (PAC), a coagulant

**URI:** https://watermetadata.org/ontology/watr#Coagulant-PolyaluminumChloride

**Superclass URI :** https://watermetadata.org/ontology/watr#Coagulant

## Flocculant

**Description:** Class for flocculants used in wastewater treatment

**URI:** https://watermetadata.org/ontology/watr#Flocculant

**Superclass URI :** https://watermetadata.org/ontology/watr#WastewaterTreatmentChemical

## Polyacrylamide

**Description:** Polyacrylamide, a common flocculant

**URI:** https://watermetadata.org/ontology/watr#Flocculant-Polyacrylamide

**Superclass URI :** https://watermetadata.org/ontology/watr#Flocculant

## pH Adjuster

**Description:** Class for pH adjusters used in wastewater treatment

**URI:** https://watermetadata.org/ontology/watr#pHAdjuster

**Superclass URI :** https://watermetadata.org/ontology/watr#WastewaterTreatmentChemical

## Lime

**Description:** Calcium hydroxide (lime), used to increase pH

**URI:** https://watermetadata.org/ontology/watr#pHAdjuster-Lime

**Superclass URI :** https://watermetadata.org/ontology/watr#pHAdjuster

## Sulfuric Acid

**Description:** Sulfuric acid, used to decrease pH

**URI:** https://watermetadata.org/ontology/watr#pHAdjuster-SulfuricAcid

**Superclass URI :** https://watermetadata.org/ontology/watr#pHAdjuster

## Disinfectant

**Description:** Class for disinfectants used in wastewater treatment

**URI:** https://watermetadata.org/ontology/watr#Disinfectant

**Superclass URI :** https://watermetadata.org/ontology/watr#WastewaterTreatmentChemical

## Chlorine

**Description:** Chlorine, a common disinfectant

**URI:** https://watermetadata.org/ontology/watr#Disinfectant-Chlorine

**Superclass URI :** https://watermetadata.org/ontology/watr#Disinfectant

## Ozone

**Description:** Ozone, an advanced disinfectant

**URI:** https://watermetadata.org/ontology/watr#Disinfectant-Ozone

**Superclass URI :** https://watermetadata.org/ontology/watr#Disinfectant

## Odor Control Agent

**Description:** Class for chemicals used for odor control

**URI:** https://watermetadata.org/ontology/watr#OdorControlAgent

**Superclass URI :** https://watermetadata.org/ontology/watr#WastewaterTreatmentChemical

## Activated Carbon

**Description:** Activated carbon, used to absorb odors

**URI:** https://watermetadata.org/ontology/watr#OdorControlAgent-ActivatedCarbon

**Superclass URI :** https://watermetadata.org/ontology/watr#OdorControlAgent

## Heavy Metal Removal Agent

**Description:** Class for chemicals used to remove heavy metals

**URI:** https://watermetadata.org/ontology/watr#HeavyMetalRemovalAgent

**Superclass URI :** https://watermetadata.org/ontology/watr#WastewaterTreatmentChemical

## Sodium Sulfide

**Description:** Sodium sulfide, used to precipitate heavy metals

**URI:** https://watermetadata.org/ontology/watr#HeavyMetalRemovalAgent-SodiumSulfide

**Superclass URI :** https://watermetadata.org/ontology/watr#HeavyMetalRemovalAgent

