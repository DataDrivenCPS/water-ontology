# Treatment Objectives Classes

## Treatment Objective

**Description:** An objective that a piece of equipment or a system is intended to achieve.

## Clarification

**Description:** Production of a clarified liquid stream by removing suspended solids from it. The objective of every clarifier, whatever the stage it serves and whatever mechanism it separates by.

**Superclass:** TreatmentObjective

## Solids Removal

**Description:** Net removal of suspended or settleable solids from the treated stream.

**Superclass:** TreatmentObjective

## Turbidity Removal

**Description:** Reduction of the turbidity of the treated stream, the objective of polishing filtration.

**Superclass:** TreatmentObjective-SolidsRemoval

## Organics Removal

**Description:** Net removal of biodegradable or dissolved organic material, measured as BOD, COD or TOC.

**Superclass:** TreatmentObjective

## Desalination

**Description:** Reduction of the dissolved salt content of the treated stream, whether by a membrane, an electrical or a thermal process.

**Superclass:** TreatmentObjective

## Softening

**Description:** Reduction of hardness by removing calcium and magnesium from the treated stream.

**Superclass:** TreatmentObjective

## pH Adjustment

**Description:** Bringing the pH of the treated stream to a target value.

**Superclass:** TreatmentObjective

## Neutralization

**Description:** pH adjustment to neutral, typically with a base, as in high-density sludge treatment.

**Superclass:** TreatmentObjective-pHAdjustment

## Metals Removal

**Description:** Removal of dissolved metals from the treated stream, typically by raising pH or dosing sulfide so that they precipitate as hydroxides or sulfides and are then separated out.

**Superclass:** TreatmentObjective

## Sulfate Removal

**Description:** Reduction of the dissolved sulfate content of the treated stream, as in acid mine drainage treatment where it is precipitated as gypsum or ettringite.

**Superclass:** TreatmentObjective

## Silica Removal

**Description:** Reduction of the dissolved silica content of the treated stream, generally to protect downstream membranes from silica scaling.

**Superclass:** TreatmentObjective

## Disinfection

**Description:** Inactivation or removal of pathogenic organisms from the treated stream. Reached by chlorination, ozonation, ultraviolet irradiation or thermal treatment, none of which is the outcome itself.

**Superclass:** TreatmentObjective

## Dechlorination

**Description:** Removal of the free and combined chlorine residual left by disinfection, before discharge or before a downstream process that the residual would damage.

**Superclass:** TreatmentObjective

## Ammonia Control

**Description:** Reduction or conversion of ammonia in the treated stream, typically by nitrification. Distinct from nitrogen removal, which requires nitrogen to leave the water altogether; nitrification converts ammonia to nitrate and removes no nitrogen.

**Superclass:** TreatmentObjective

## Nutrient Removal

**Description:** Net removal of nitrogen or phosphorus from the treated stream, as opposed to its conversion from one form to another.

**Superclass:** TreatmentObjective

## Nitrogen Removal

**Description:** Net removal of nitrogen from the treated stream, typically by converting nitrate to nitrogen gas so that it leaves as a gas.

**Superclass:** TreatmentObjective-NutrientRemoval

## Phosphorus Removal

**Description:** Net removal of phosphorus from the treated stream, by taking it into biomass or precipitating it into a solid that is then wasted.

**Superclass:** TreatmentObjective-NutrientRemoval

## Thickening

**Description:** Raising the solids concentration of a sludge or slurry while it remains pumpable. Distinguished from dewatering by the state of the product.

**Superclass:** TreatmentObjective

## Dewatering

**Description:** Removing water from a sludge or slurry to the point that the product is a handleable cake rather than a pumpable liquid.

**Superclass:** TreatmentObjective

## Drying

**Description:** Removing water from biosolids beyond the cake stage, to a dry product.

**Superclass:** TreatmentObjective-Dewatering

## Stabilization

**Description:** Reduction of the volatile solids, pathogen content and odour potential of biosolids so that they can be stored, used or disposed of.

**Superclass:** TreatmentObjective

## Biosolids Disposal

**Description:** Final disposition of biosolids, by land application, landfilling, incineration or another route.

**Superclass:** TreatmentObjective

## Land Application

**Description:** Final disposition of biosolids by beneficial reuse on agricultural or reclamation land.

**Superclass:** TreatmentObjective-BiosolidsDisposal

## Landfill

**Description:** Final disposition of biosolids by landfilling.

**Superclass:** TreatmentObjective-BiosolidsDisposal

