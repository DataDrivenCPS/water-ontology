# Processes Classes

## Water Process

**Description:** A physical, chemical, or biological activity performed by a piece of equipment or by a system.

## Physical Process

**Description:** A unit process that relies on physical forces to separate or treat water.

**Superclass:** Process

## Separation

**Description:** The most generic process for separation of any two constituents.

**Superclass:** Process-PhysicalProcess

## Solid-Liquid Separation

**Description:** Separation of suspended solids from the liquid carrying them, by settling, flotation, filtration or centrifugal force. Distinguished from separations that act on dissolved or gaseous constituents.

**Superclass:** Process-Separation

## Elutriation

**Description:** A process that uses a stream of fluid flowing upward to separate a mixture of particles based on their size, shape, and density.

**Superclass:** Process-Separation

## Screening

**Description:** A unit process that removes large solids from water, such as leaves, branches, and other debris.

**Superclass:** Process-Separation

## Sedimentation

**Description:** A unit process that allows solids to settle out of water by gravity.

**Superclass:** Process-SolidLiquidSeparation

## Stripping

**Description:** Gas stripping for removal of dissolved gases such as ammonia and volatile organic compounds.

**Superclass:** Process-Separation

## Filtration

**Description:** A unit process that separates constituents from water by passing it through a filter or membrane, retaining what will not pass.

**Superclass:** Process-Separation

## Media Filtration

**Description:** A filtration process that uses a bed of media (as opposed to a membrane-based process).

**Superclass:** Process-Filtration

## Media Filtration

**Description:** A filtration process that uses a bed of media (as opposed to a membrane-based process).

**Superclass:** Process-SolidLiquidSeparation

## Slow Sand Filtration

**Description:** A filtration process that uses a bed of sand to remove impurities at low flow rates.

**Superclass:** Process-MediaFiltration

## Rapid Sand Filtration

**Description:** A filtration process that uses a bed of sand to remove impurities at high flow rates.

**Superclass:** Process-MediaFiltration

## Flotation

**Description:** A unit process that uses buoyancy to separate solids from water, often using air bubbles.

**Superclass:** Process-SolidLiquidSeparation

## Gas Transfer

**Description:** A unit process that transfers gases, such as oxygen or carbon dioxide, into or out of water.

**Superclass:** Process-PhysicalProcess

## Aeration

**Description:** A unit process that aerates (i.e., transfers oxygen into water).

**Superclass:** Process-GasTransfer

## Mixing

**Description:** A unit process that mixes water with chemicals or other substances to achieve a desired effect.

**Superclass:** Process-PhysicalProcess

## Recirculation

**Description:** A process that returns a portion of a treated or intermediate flow back upstream to maintain hydraulic, solids, or biological performance.

**Superclass:** Process-PhysicalProcess

## Centrifugation

**Description:** A process that uses centrifugal force to separate substances of different densities.

**Superclass:** Process-SolidLiquidSeparation

## Solidification

**Description:** A process of turning a liquid into a solid (e.g., freezing).

**Superclass:** Process-PhysicalProcess

## Crystallization

**Description:** A process of forming solid crystals from a solution.

**Superclass:** Process-Solidification

## Evaporation

**Description:** A process of turning a liquid into a vapor.

**Superclass:** Process-PhysicalProcess

## Condensation

**Description:** A process of turning a vapor into a liquid.

**Superclass:** Process-PhysicalProcess

## Adsorption

**Description:** A process by which substances bind to a surface.

**Superclass:** Process-PhysicalProcess

## Granular Activated Carbon (GAC)

**Description:** A process that uses an activated carbon filter to adsorb impurities from water.

**Superclass:** Process-Adsorption

## Granular Activated Carbon (GAC)

**Description:** A process that uses an activated carbon filter to adsorb impurities from water.

**Superclass:** Process-Filtration

## Membrane Process

**Description:** A process that uses a semi-permeable membrane to separate substances.

**Superclass:** Process-Filtration

## Reverse Osmosis (RO)

**Description:** Separation across a semi-permeable membrane under an applied pressure greater than the osmotic pressure of the feed, so that water passes and dissolved salts are retained.

**Superclass:** Process-MembraneProcess

## Closed Circuit Reverse Osmosis (CCRO)

**Description:** Reverse osmosis operated as a batch, with the concentrate recirculated to the feed side of the same module until a target recovery is reached and then displaced, rather than run as a once-through stage.

**Superclass:** Process-ReverseOsmosis

## Osmotically Assisted Reverse Osmosis (OARO)

**Description:** Reverse osmosis in which a saline sweep stream on the permeate side lowers the osmotic pressure difference across the membrane, so that a hypersaline feed can be concentrated further than the applied pressure would otherwise allow.

**Superclass:** Process-ReverseOsmosis

## Feed Reversal Reverse Osmosis (FRRO)

**Description:** Reverse osmosis in which the direction of feed flow through the train is periodically reversed, so that the elements which saw the most concentrated water see the feed next and scale that has begun to form is redissolved.

**Superclass:** Process-ReverseOsmosis

## Membrane Distillation (MD)

**Description:** Separation driven by a vapour pressure difference across a hydrophobic membrane: water evaporates on the warm feed side, crosses the membrane as vapour, and condenses on the cool permeate side, while the liquid feed is held back.

**Superclass:** Process-MembraneProcess

## Electrodialysis

**Description:** A process that uses ion-exchange membranes and an electric potential to separate ions from water.

**Superclass:** Process-ChemicalProcess

## Electrodialysis

**Description:** A process that uses ion-exchange membranes and an electric potential to separate ions from water.

**Superclass:** Process-PhysicalProcess

## Electro-Dialytic Crystallization (EDC)

**Description:** A novel integrated process combining electrodialysis and crystallization for energy-efficient Zero-Liquid Discharge (ZLD) by maintaining a saturated brine stream.

**Superclass:** Process-Electrodialysis

## Electro-Dialytic Crystallization (EDC)

**Description:** A novel integrated process combining electrodialysis and crystallization for energy-efficient Zero-Liquid Discharge (ZLD) by maintaining a saturated brine stream.

**Superclass:** Process-Crystallization

## Comminution

**Description:** Process of reducing solid materials into smaller particles through mechanical forces such as crushing, grinding, impact, shear, or compression.

**Superclass:** Process-PhysicalProcess

## Composting

**Description:** Biological degradation of organic materials under controlled aerobic conditions.

**Superclass:** Process-BiologicalProcess

## Chemical Process

**Description:** A unit process that uses chemical reaction, chemical addition, or both to achieve a desired effect.

**Superclass:** Process

## Dosing

**Description:** Metered addition of a reagent to water, such as chlorine, coagulant, polymer, acid, base, or sulfite.

**Superclass:** Process-ChemicalProcess

## Coagulation

**Description:** A unit process that adds chemicals to water to cause small particles to clump together.

**Superclass:** Process-Dosing

## Electrocoagulation (EC)

**Description:** An electrified pretreatment technology using sacrificial anodes to release coagulant precursors for contaminant removal.

**Superclass:** Process-Coagulation

## Electrocoagulation (EC)

**Description:** An electrified pretreatment technology using sacrificial anodes to release coagulant precursors for contaminant removal.

**Superclass:** Process-PhysicalProcess

## Flocculation

**Description:** A unit process that gently mixes water to allow coagulated particles to form larger clumps.

**Superclass:** Process-ChemicalProcess

## Flocculation

**Description:** A unit process that gently mixes water to allow coagulated particles to form larger clumps.

**Superclass:** Process-Mixing

## Ultraviolet Irradiation

**Description:** Exposure of water to ultraviolet light. Named for what it does rather than what it is for: the same irradiation serves disinfection and, combined with an oxidant, advanced oxidation.

**Superclass:** Process-PhysicalProcess

## Chlorine Dosing

**Description:** Dosing of chlorine or chlorine compounds into water.

**Superclass:** Process-Dosing

## Thermal Treatment

**Description:** Heating of water or biosolids, as in pasteurization. The process alone does not establish whether the intended treatment objective is disinfection, drying, hydrolysis, or another thermal result.

**Superclass:** Process-PhysicalProcess

## Oxidation

**Description:** A unit process that adds oxidizing agents to water to remove contaminants or improve water quality.

**Superclass:** Process-ChemicalProcess

## Advanced Oxidation Process (AOP)

**Description:** Processes combining UV light with oxidants (e.g., UV-AOP) to destroy contaminants.

**Superclass:** Process-Oxidation

## Electrooxidation (EO)

**Description:** Oxidation of contaminants at the surface of an anode, and by oxidants generated there, under an applied electric current rather than by a dosed reagent.

**Superclass:** Process-Oxidation

## Electrooxidation (EO)

**Description:** Oxidation of contaminants at the surface of an anode, and by oxidants generated there, under an applied electric current rather than by a dosed reagent.

**Superclass:** Process-PhysicalProcess

## Ozonation

**Description:** A water treatment process that uses ozone as an oxidant. The process alone does not establish whether the intended treatment objective is disinfection, oxidation of a contaminant, or taste-and-odour control.

**Superclass:** Process-Oxidation

## Chemical Precipitation

**Description:** Addition of a reagent that converts a dissolved constituent into an insoluble solid, so that it can be separated from the water. Which constituent it targets depends on the reagent, which is why the objective is stated on the equipment rather than here.

**Superclass:** Process-ChemicalProcess

## Chemical Reduction

**Description:** Mechanism by which contaminants are transformed through the gain of electrons.

**Superclass:** Process-ChemicalProcess

## Solvent-Based Extraction

**Description:** A non-membrane, non-thermal method using a solvent to selectively extract water from highly saline brines.

**Superclass:** Process-ChemicalProcess

## High-Density Sludge (HDS) Process

**Description:** Lime neutralization of an acidic stream, typically acid mine drainage, in which previously formed sludge is recycled into the reaction so that metal hydroxides precipitate onto existing particles and settle as a denser sludge.

**Superclass:** Process-ChemicalProcess

## High-Density Sludge (HDS) Process

**Description:** Lime neutralization of an acidic stream, typically acid mine drainage, in which previously formed sludge is recycled into the reaction so that metal hydroxides precipitate onto existing particles and settle as a denser sludge.

**Superclass:** Process-PhysicalProcess

## Ion Exchange

**Description:** A process in which ions are exchanged between a solution and an ion-exchange resin or membrane.

**Superclass:** Process-ChemicalProcess

## Ion Exchange

**Description:** A process in which ions are exchanged between a solution and an ion-exchange resin or membrane.

**Superclass:** Process-PhysicalProcess

## Electrolysis

**Description:** A process that uses a direct electric current to drive an otherwise non-spontaneous chemical reaction.

**Superclass:** Process-ChemicalProcess

## Combustion

**Description:** A process that combusts biosolids or biogas.

**Superclass:** Process-ChemicalProcess

## Combustion

**Description:** A process that combusts biosolids or biogas.

**Superclass:** Process-PhysicalProcess

## Fluidized Bed Incineration

**Description:** A process that combusts a constantly moving bed of biosolids.

**Superclass:** Process-Combustion

## Multiple Hearth Incineration (MHI)

**Description:** A process that combusts biosolids as they move through a series of stacked hearths with controlled air flow.

**Superclass:** Process-Combustion

## Cogeneration

**Description:** A process that combusts biosolids or biogas to produce electricity and heat simultaneously.

**Superclass:** Process-Combustion

## Biological Process

**Description:** A unit process that utilizes biological activity for water treatment.

**Superclass:** Process

## Nitrification

**Description:** Process by which ammonia is oxidized to nitrite and subsequently nitrate.

**Superclass:** Process-BiologicalProcess

## Denitrification

**Description:** Process by which nitrate is deoxidized to nitrogen gas and nitrogen oxides.

**Superclass:** Process-BiologicalProcess

## Enhanced Biological Phosphorus Removal (EBPR)

**Description:** Uptake of phosphorus into biomass beyond ordinary metabolic requirements, achieved by cycling the biomass through anaerobic and aerobic conditions.

**Superclass:** Process-BiologicalProcess

## Five-Stage BARDENPHO (BARnard DENitrification and PHOsphorus removal)

**Description:** A five-stage biological nutrient removal process specifically designed for nitrogen and phosphorus.

**Superclass:** Process-ActivatedSludge

## Four-Stage BARDENPHO (BARnard DENitrification and PHOsphorus removal)

**Description:** A four-stage biological nutrient removal process with two anoxic and two aerobic zones.

**Superclass:** Process-ActivatedSludge

## Activated Sludge

**Description:** Suspended-growth biological treatment in which biomass is aerated and subsequently separated from the treated water.

**Superclass:** Process-BiologicalProcess

## Anoxic-Aerobic

**Description:** Two-stage process with anoxic zone followed by aerobic zone for biological nitrogen removal.

**Superclass:** Process-ActivatedSludge

## Modified Ludzack-Ettinger (MLE)

**Description:** Modification of AO with an internal recycle returning nitrate to the anoxic zone.

**Superclass:** Process-AO

## Anaerobic-Anoxic-Oxic (A2O)

**Description:** Anaerobic-anoxic-aerobic process for simultaneous biological nitrogen and phosphorus removal.

**Superclass:** Process-ActivatedSludge

## University of Cape Town (UCT)

**Description:** Variant of A2O with modified recycle streams for phosphorus removal.

**Superclass:** Process-A2O

## Biofiltration

**Description:** A filtration method that uses biological processes to remove contaminants.

**Superclass:** Process-BiologicalProcess

## Biofiltration

**Description:** A filtration method that uses biological processes to remove contaminants.

**Superclass:** Process-Filtration

## TricklingFiltration

**Description:** Trickling filter using any media (e.g., plastic, sand, gravel, etc.)

**Superclass:** Process-Biofiltration

## Biologically Active Filtration (BAF)

**Description:** A biologically activated filtration column.

**Superclass:** Process-Biofiltration

## Microfiltration

**Description:** Membrane filtration at a pore size of roughly 0.1 to 1 micron, retaining suspended solids, bacteria and larger colloids. The pore-size range characterizes the method; a model states its intended treatment objective separately.

**Superclass:** Process-MembraneProcess

## Microfiltration

**Description:** Membrane filtration at a pore size of roughly 0.1 to 1 micron, retaining suspended solids, bacteria and larger colloids. The pore-size range characterizes the method; a model states its intended treatment objective separately.

**Superclass:** Process-SolidLiquidSeparation

## Ultrafiltration

**Description:** Membrane filtration at a pore size of roughly 0.01 to 0.1 micron, retaining colloids and macromolecules as well as the suspended solids microfiltration retains. The pore-size range characterizes the method; a model states its intended treatment objective separately.

**Superclass:** Process-MembraneProcess

## Ultrafiltration

**Description:** Membrane filtration at a pore size of roughly 0.01 to 0.1 micron, retaining colloids and macromolecules as well as the suspended solids microfiltration retains. The pore-size range characterizes the method; a model states its intended treatment objective separately.

**Superclass:** Process-SolidLiquidSeparation

## Backwashing

**Description:** A cleaning process in which water, and sometimes air, is driven backward through a filter or membrane system to remove accumulated solids.

**Superclass:** Process-Cleaning

## Air Scouring

**Description:** A cleaning process that uses injected air to dislodge accumulated foulants or solids from filter media or membrane surfaces.

**Superclass:** Process-Cleaning

## Purging

**Description:** A process that flushes retained liquid, solids, or gas from equipment or piping to restore operating conditions or prepare for another cycle.

**Superclass:** Process-Cleaning

## Digestion

**Description:** A biological process that breaks down organic matter over a long duration in a tank.

**Superclass:** Process-BiologicalProcess

## Hydrolysis

**Description:** A process reaction in which a water molecule is consumed to split a larger molecule into smaller fragments.

**Superclass:** Process-ChemicalProcess

## Thermal Hydrolysis

**Description:** A process that breaks down complex organic matter into soluble compounds using heat and pressure.

**Superclass:** Process-Hydrolysis

## Cleaning

**Description:** A maintenance-oriented process that removes accumulated solids, foulants, or residual materials from water treatment equipment.

**Superclass:** Process-PhysicalProcess

## Anaerobic Digestion

**Description:** A biological process that breaks down organic matter in the absence of oxygen.

**Superclass:** Process-Digestion

## Aerobic Digestion

**Description:** A biological process that breaks down organic matter in the presence of oxygen.

**Superclass:** Process-Digestion
