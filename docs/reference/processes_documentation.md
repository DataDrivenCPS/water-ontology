# Processes Classes

## Water Treatment Process

**Description:** A physical, chemical, or biological activity performed by a piece of equipment or by a system.

## Anaerobic-Anoxic-Oxic (A2O)

**Description:** Anaerobic-anoxic-aerobic process for simultaneous biological nitrogen and phosphorus removal.

**Superclasses:** `watr:Process-ActivatedSludge`

## Anoxic-Aerobic

**Description:** Two-stage process with anoxic zone followed by aerobic zone for biological nitrogen removal.

**Superclasses:** `watr:Process-ActivatedSludge`

## Activated Sludge

**Description:** Suspended-growth biological treatment in which biomass is aerated and subsequently separated from the treated water.

**Superclasses:** `watr:Process-BiologicalProcess`

## Adsorption

**Description:** A process by which substances bind to a surface.

**Superclasses:** `watr:Process-PhysicalProcess`

## Advanced Oxidation Process (AOP)

**Description:** Processes combining UV light with oxidants (e.g., UV-AOP) to destroy contaminants.

**Superclasses:** `watr:Process-Oxidation`

## Aeration

**Description:** A unit process that aerates (i.e., transfers oxygen into water).

**Superclasses:** `watr:Process-GasTransfer`

## Aerobic Digestion

**Description:** A biological process that breaks down organic matter in the presence of oxygen.

**Superclasses:** `watr:Process-Digestion`

## Air Scouring

**Description:** A cleaning process that uses injected air to dislodge accumulated foulants or solids from filter media or membrane surfaces.

**Superclasses:** `watr:Process-Cleaning`

## Anaerobic Digestion

**Description:** A biological process that breaks down organic matter in the absence of oxygen.

**Superclasses:** `watr:Process-Digestion`

## Backwashing

**Description:** A cleaning process in which water, and sometimes air, is driven backward through a filter or membrane system to remove accumulated solids.

**Superclasses:** `watr:Process-Cleaning`

## Biofiltration

**Description:** A filtration method that uses biological processes to remove contaminants.

**Superclasses:** `watr:Process-BiologicalProcess`, `watr:Process-Filtration`

## Biological Process

**Description:** A unit process that utilizes biological activity for water treatment.

**Superclasses:** `watr:Process`

## Biologically Active Filtration (BAF)

**Description:** A biologically activated filtration column.

**Superclasses:** `watr:Process-Biofiltration`

## BiosolidsDisposal (deprecated)

**Description:** Deprecated designation; use TreatmentObjective-BiosolidsDisposal. The replacement distinguishes treatment mechanism from objective.

## Centrifugation

**Description:** A process that uses centrifugal force to separate substances of different densities.

**Superclasses:** `watr:Process-SolidLiquidSeparation`

## ChemicalAddition (deprecated)

**Description:** Deprecated process designation; use Process-Dosing.

**Superclasses:** `watr:Process-Dosing`

## Chemical Precipitation

**Description:** Addition of a reagent that converts a dissolved constituent into an insoluble solid, so that it can be separated from the water. This process implies general constituent removal. Which constituent it targets depends on the reagent, so the modeler states the specific removal objective on the equipment.

**Superclasses:** `watr:Process-ChemicalProcess`

## Chemical Process

**Description:** A unit process that uses chemical reaction, chemical addition, or both to achieve a desired effect.

**Superclasses:** `watr:Process`

## Chlorination

**Description:** Dosing chlorine or a chlorine compound into water with contact time designed for disinfection. The intended objective is disinfection; actual performance depends on dose, contact time and water quality.

**Superclasses:** `watr:Process-Dosing`

## ChlorineDosing (deprecated)

**Description:** Deprecated designation; use Process-Chlorination. The replacement distinguishes treatment mechanism from objective.

## Cleaning

**Description:** A maintenance-oriented process that removes accumulated solids, foulants, or residual materials from water treatment equipment.

**Superclasses:** `watr:Process-PhysicalProcess`

## Closed Circuit Reverse Osmosis (CCRO)

**Description:** Reverse osmosis operated as a batch, with the concentrate recirculated to the feed side of the same module until a target recovery is reached and then displaced, rather than run as a once-through stage.

**Superclasses:** `watr:Process-ReverseOsmosis`

## Coagulation

**Description:** A unit process that adds chemicals to water to cause small particles to clump together.

**Superclasses:** `watr:Process-Dosing`

## Cogeneration

**Description:** A process that combusts biosolids or biogas to produce electricity and heat simultaneously.

**Superclasses:** `watr:Process-Combustion`

## Combustion

**Description:** A process that combusts biosolids or biogas.

**Superclasses:** `watr:Process-ChemicalProcess`, `watr:Process-PhysicalProcess`

## Comminution

**Description:** Process of reducing solid materials into smaller particles through mechanical forces such as crushing, grinding, impact, shear, or compression.

**Superclasses:** `watr:Process-PhysicalProcess`

## Composting

**Description:** Biological degradation of organic materials under controlled aerobic conditions.

**Superclasses:** `watr:Process-BiologicalProcess`

## Condensation

**Description:** A process of turning a vapor into a liquid.

**Superclasses:** `watr:Process-PhysicalProcess`

## Crystallization

**Description:** A process of forming solid crystals from a solution.

**Superclasses:** `watr:Process-Solidification`

## Dechlorination (deprecated)

**Description:** Deprecated designation; use TreatmentObjective-ChlorineResidualRemoval. The replacement distinguishes treatment mechanism from objective.

## Denitrification

**Description:** Process by which nitrate is deoxidized to nitrogen gas and nitrogen oxides.

**Superclasses:** `watr:Process-BiologicalProcess`

## Dewatering (deprecated)

**Description:** Deprecated designation; use TreatmentObjective-Dewatering. The replacement distinguishes treatment mechanism from objective.

## Digestion

**Description:** A biological process that breaks down organic matter over a long duration in a tank.

**Superclasses:** `watr:Process-BiologicalProcess`

## Disinfection (deprecated)

**Description:** Deprecated designation; use TreatmentObjective-Disinfection. The replacement distinguishes treatment mechanism from objective.

## Dosing

**Description:** Metered addition of a reagent to water, such as chlorine, coagulant, polymer, acid, base, or sulfite.

**Superclasses:** `watr:Process-ChemicalProcess`

## Drying (deprecated)

**Description:** Deprecated designation; use TreatmentObjective-Drying. The replacement distinguishes treatment mechanism from objective.

## Electro-Dialytic Crystallization (EDC)

**Description:** A novel integrated process combining electrodialysis and crystallization for energy-efficient Zero-Liquid Discharge (ZLD) by maintaining a saturated brine stream.

**Superclasses:** `watr:Process-Crystallization`, `watr:Process-Electrodialysis`

## Electrocoagulation (EC)

**Description:** An electrified pretreatment technology using sacrificial anodes to release coagulant precursors for contaminant removal.

**Superclasses:** `watr:Process-Coagulation`, `watr:Process-PhysicalProcess`

## Electrodialysis

**Description:** A process that uses ion-exchange membranes and an electric potential to separate ions from water.

**Superclasses:** `watr:Process-ChemicalProcess`, `watr:Process-Separation`

## Electrolysis

**Description:** A process that uses a direct electric current to drive an otherwise non-spontaneous chemical reaction.

**Superclasses:** `watr:Process-ChemicalProcess`

## Electrooxidation (EO)

**Description:** Oxidation of contaminants at the surface of an anode, and by oxidants generated there, under an applied electric current rather than by a dosed reagent.

**Superclasses:** `watr:Process-Oxidation`, `watr:Process-PhysicalProcess`

## Elutriation

**Description:** A process that uses a stream of fluid flowing upward to separate a mixture of particles based on their size, shape, and density.

**Superclasses:** `watr:Process-Separation`

## Enhanced Biological Phosphorus Removal (EBPR)

**Description:** Uptake of phosphorus into biomass beyond ordinary metabolic requirements, achieved by cycling the biomass through anaerobic and aerobic conditions.

**Superclasses:** `watr:Process-BiologicalProcess`

## Evaporation

**Description:** A process of turning a liquid into a vapor.

**Superclasses:** `watr:Process-PhysicalProcess`

## Feed Reversal Reverse Osmosis (FRRO)

**Description:** Reverse osmosis in which the direction of feed flow through the train is periodically reversed, so that the elements which saw the most concentrated water see the feed next and scale that has begun to form is redissolved.

**Superclasses:** `watr:Process-ReverseOsmosis`

## Filtration

**Description:** A unit process that separates constituents from water by passing it through a filter or membrane, retaining what will not pass.

**Superclasses:** `watr:Process-Separation`

## Five-Stage BARDENPHO (BARnard DENitrification and PHOsphorus removal)

**Description:** A five-stage biological nutrient removal process specifically designed for nitrogen and phosphorus.

**Superclasses:** `watr:Process-ActivatedSludge`

## Flocculation

**Description:** A unit process that gently mixes water to allow coagulated particles to form larger clumps.

**Superclasses:** `watr:Process-ChemicalProcess`, `watr:Process-Mixing`

## Flotation

**Description:** A unit process that uses buoyancy to separate solids from water, often using air bubbles.

**Superclasses:** `watr:Process-SolidLiquidSeparation`

## Fluidized Bed Incineration

**Description:** A process that combusts a constantly moving bed of biosolids.

**Superclasses:** `watr:Process-Combustion`

## Four-Stage BARDENPHO (BARnard DENitrification and PHOsphorus removal)

**Description:** A four-stage biological nutrient removal process with two anoxic and two aerobic zones.

**Superclasses:** `watr:Process-ActivatedSludge`

## GAC Filtration

**Description:** Filtration through a bed of granular activated carbon, which retains particles as any granular medium does and adsorbs dissolved constituents onto the carbon's surface.

**Superclasses:** `watr:Process-Adsorption`, `watr:Process-MediaFiltration`

## Gas Transfer

**Description:** A unit process that transfers gases, such as oxygen or carbon dioxide, into or out of water.

**Superclasses:** `watr:Process-PhysicalProcess`

## GranularActivatedCarbon (deprecated)

**Description:** Deprecated process designation; use Process-GACFiltration.

**Superclasses:** `watr:Process-GACFiltration`

## High-Density Sludge (HDS) Process

**Description:** Lime neutralization of an acidic stream, typically acid mine drainage, in which previously formed sludge is recycled into the reaction so that metal hydroxides precipitate onto existing particles and settle as a denser sludge.

**Superclasses:** `watr:Process-ChemicalProcess`, `watr:Process-PhysicalProcess`

## Hydrolysis

**Description:** A process reaction in which a water molecule is consumed to split a larger molecule into smaller fragments.

**Superclasses:** `watr:Process-ChemicalProcess`

## Ion Exchange

**Description:** A process in which ions are exchanged between a solution and an ion-exchange resin or membrane.

**Superclasses:** `watr:Process-ChemicalProcess`, `watr:Process-PhysicalProcess`

## Land Application

**Description:** Spreading treated biosolids on agricultural or reclamation land, where they serve as a soil amendment.

**Superclasses:** `watr:Process-PhysicalProcess`

## Landfill (deprecated)

**Description:** Deprecated designation; use Process-Landfilling. The replacement distinguishes treatment mechanism from objective.

## Landfilling

**Description:** Placing treated biosolids in a landfill, whether in a dedicated cell or with municipal solid waste.

**Superclasses:** `watr:Process-PhysicalProcess`

## Modified Ludzack-Ettinger (MLE)

**Description:** Modification of AO with an internal recycle returning nitrate to the anoxic zone.

**Superclasses:** `watr:Process-AO`

## Media Filtration

**Description:** A filtration process that uses a bed of media (as opposed to a membrane-based process).

**Superclasses:** `watr:Process-Filtration`, `watr:Process-SolidLiquidSeparation`

## Membrane Distillation (MD)

**Description:** Separation driven by a vapour pressure difference across a hydrophobic membrane: water evaporates on the warm feed side, crosses the membrane as vapour, and condenses on the cool permeate side, while the liquid feed is held back.

**Superclasses:** `watr:Process-MembraneProcess`

## Membrane Process

**Description:** A process that uses a semi-permeable membrane to separate substances.

**Superclasses:** `watr:Process-Filtration`

## Microfiltration

**Description:** Membrane filtration at a pore size of roughly 0.1 to 1 micron, retaining suspended solids, bacteria and larger colloids. The pore-size range characterizes the method; a model states its intended treatment objective separately.

**Superclasses:** `watr:Process-MembraneProcess`, `watr:Process-SolidLiquidSeparation`

## Mixing

**Description:** A unit process that mixes water with chemicals or other substances to achieve a desired effect.

**Superclasses:** `watr:Process-PhysicalProcess`

## Multiple Hearth Incineration (MHI)

**Description:** A process that combusts biosolids as they move through a series of stacked hearths with controlled air flow.

**Superclasses:** `watr:Process-Combustion`

## Neutralization (deprecated)

**Description:** Deprecated designation; use TreatmentObjective-Neutralization. The replacement distinguishes treatment mechanism from objective.

## Nitrification

**Description:** Process by which ammonia is oxidized to nitrite and subsequently nitrate.

**Superclasses:** `watr:Process-BiologicalProcess`

## Osmotically Assisted Reverse Osmosis (OARO)

**Description:** Reverse osmosis in which a saline sweep stream on the permeate side lowers the osmotic pressure difference across the membrane, so that a hypersaline feed can be concentrated further than the applied pressure would otherwise allow.

**Superclasses:** `watr:Process-ReverseOsmosis`

## Oxidation

**Description:** A unit process that adds oxidizing agents to water to remove contaminants or improve water quality.

**Superclasses:** `watr:Process-ChemicalProcess`

## Ozonation

**Description:** A water treatment process that uses ozone as an oxidant. The process alone does not establish whether the intended treatment objective is disinfection, oxidation of a contaminant, or taste-and-odour control.

**Superclasses:** `watr:Process-Oxidation`

## Physical Process

**Description:** A unit process that relies on physical forces to separate or treat water.

**Superclasses:** `watr:Process`

## Purging

**Description:** A process that flushes retained liquid, solids, or gas from equipment or piping to restore operating conditions or prepare for another cycle.

**Superclasses:** `watr:Process-Cleaning`

## Rapid Sand Filtration

**Description:** A filtration process that uses a bed of sand to remove impurities at high flow rates.

**Superclasses:** `watr:Process-MediaFiltration`

## Recirculation

**Description:** A process that returns a portion of a treated or intermediate flow back upstream to maintain hydraulic, solids, or biological performance.

**Superclasses:** `watr:Process-PhysicalProcess`

## Chemical Reduction

**Description:** Mechanism by which contaminants are transformed through the gain of electrons.

**Superclasses:** `watr:Process-ChemicalProcess`

## Reverse Osmosis (RO)

**Description:** Separation across a semi-permeable membrane under an applied pressure greater than the osmotic pressure of the feed, so that water passes and dissolved salts are retained.

**Superclasses:** `watr:Process-MembraneProcess`

## Screening

**Description:** A unit process that removes large solids from water, such as leaves, branches, and other debris.

**Superclasses:** `watr:Process-Separation`

## Sedimentation (deprecated)

**Description:** Deprecated process designation; use Process-Settling.

**Superclasses:** `watr:Process-Settling`

## Separation

**Description:** The most generic process for separation of any two constituents.

**Superclasses:** `watr:Process-PhysicalProcess`

## Settling

**Description:** A unit process that allows solids to settle out of water by gravity.

**Superclasses:** `watr:Process-SolidLiquidSeparation`

## Slow Sand Filtration

**Description:** A filtration process that uses a bed of sand to remove impurities at low flow rates.

**Superclasses:** `watr:Process-MediaFiltration`

## Softening (deprecated)

**Description:** Deprecated designation; use TreatmentObjective-Softening. The replacement distinguishes treatment mechanism from objective.

## Solid-Liquid Separation

**Description:** Separation of suspended solids from the liquid carrying them, by settling, flotation, filtration or centrifugal force. Distinguished from separations that act on dissolved or gaseous constituents.

**Superclasses:** `watr:Process-Separation`

## Solidification

**Description:** A process of turning a liquid into a solid (e.g., freezing).

**Superclasses:** `watr:Process-PhysicalProcess`

## Solvent-Based Extraction

**Description:** A non-membrane, non-thermal method using a solvent to selectively extract water from highly saline brines.

**Superclasses:** `watr:Process-ChemicalProcess`, `watr:Process-Separation`

## Stripping

**Description:** Gas stripping for removal of dissolved gases such as ammonia and volatile organic compounds.

**Superclasses:** `watr:Process-Separation`

## Sulfite Dosing

**Description:** Metered addition of sulfur dioxide, sodium sulfite, bisulfite or metabisulfite, which reduces free and combined chlorine to chloride.

**Superclasses:** `watr:Process-Dosing`

## ThermalDisinfection (deprecated)

**Description:** Deprecated designation; use Process-ThermalTreatment. The replacement distinguishes treatment mechanism from objective.

## Thermal Hydrolysis

**Description:** A process that breaks down complex organic matter into soluble compounds using heat and pressure.

**Superclasses:** `watr:Process-Hydrolysis`, `watr:Process-ThermalTreatment`

## Thermal Treatment

**Description:** Heating of water or biosolids, as in pasteurization. The process alone does not establish whether the intended treatment objective is disinfection, drying, hydrolysis, or another thermal result.

**Superclasses:** `watr:Process-PhysicalProcess`

## Thickening (deprecated)

**Description:** Deprecated designation; use TreatmentObjective-Thickening. The replacement distinguishes treatment mechanism from objective.

## TricklingFiltration

**Description:** Trickling filter using any media (e.g., plastic, sand, gravel, etc.)

**Superclasses:** `watr:Process-Biofiltration`

## University of Cape Town (UCT)

**Description:** Variant of A2O with modified recycle streams for phosphorus removal.

**Superclasses:** `watr:Process-A2O`

## UVDisinfection (deprecated)

**Description:** Deprecated process designation; use Process-UVIrradiation.

**Superclasses:** `watr:Process-UVIrradiation`

## Ultraviolet Irradiation

**Description:** Exposure of water to ultraviolet light. Named for what it does rather than what it is for: the same irradiation serves disinfection and, combined with an oxidant, advanced oxidation.

**Superclasses:** `watr:Process-PhysicalProcess`

## Ultrafiltration

**Description:** Membrane filtration at a pore size of roughly 0.01 to 0.1 micron, retaining colloids and macromolecules as well as the suspended solids microfiltration retains. The pore-size range characterizes the method; a model states its intended treatment objective separately.

**Superclasses:** `watr:Process-MembraneProcess`, `watr:Process-SolidLiquidSeparation`

## pHAdjustment (deprecated)

**Description:** Deprecated designation; use TreatmentObjective-pHControl. The replacement distinguishes treatment mechanism from objective.
