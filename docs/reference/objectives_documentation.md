# Treatment Objectives Classes

## Treatment Objective

**Description:** An objective that a piece of equipment or a system is intended to achieve.

## Ammonia Control

**Description:** Reduction or conversion of ammonia in the treated stream, typically by nitrification. Distinct from nitrogen removal, which requires nitrogen to leave the water altogether; nitrification converts ammonia to nitrate and removes no nitrogen.

**Superclasses:** `watr:TreatmentObjective-ConstituentRemoval`

## Arsenic Removal

**Description:** Reduction of arsenic species in the treated stream.

**Superclasses:** `watr:TreatmentObjective-DissolvedSolidsRemoval`

## Biosolids Disposal

**Description:** Final disposition of biosolids, by land application, landfilling, incineration or another route.

**Superclasses:** `watr:TreatmentObjective`

## Chlorine Residual Removal

**Description:** Removal of the free and combined chlorine residual left by disinfection, before discharge or before a downstream process that the residual would damage.

**Superclasses:** `watr:TreatmentObjective-ConstituentRemoval`

## Clarification

**Description:** Production of a clarified liquid stream by removing suspended solids from it. The objective of every clarifier, whatever the stage it serves and whatever mechanism it separates by.

**Superclasses:** `watr:TreatmentObjective-SolidsRemoval`

## Constituent Removal

**Description:** Net removal, conversion or control of a named constituent of the treated stream. The parent of the objectives that name what comes out of the water; the constituent each one is aimed at is stated with watr:targetsConstituent.

**Superclasses:** `watr:TreatmentObjective`

## Desalination

**Description:** Reduction of the dissolved salt content of the treated stream, whether by a membrane, an electrical or a thermal process.

**Superclasses:** `watr:TreatmentObjective-DissolvedSolidsRemoval`

## Dewatering

**Description:** Removing water from a sludge or slurry to the point that the product is a handleable cake rather than a pumpable liquid.

**Superclasses:** `watr:TreatmentObjective-VolumeReduction`

## Disinfection

**Description:** Inactivation or removal of pathogenic organisms from the treated stream. Reached by chlorination, ozonation, ultraviolet irradiation or thermal treatment, none of which is the outcome itself.

**Superclasses:** `watr:TreatmentObjective`

## Dissolved Solids Removal

**Description:** Reduction of the dissolved solids content of the treated stream. The parent of the objectives aimed at a particular dissolved constituent.

**Superclasses:** `watr:TreatmentObjective-ConstituentRemoval`

## Drying

**Description:** Removing water from biosolids beyond the cake stage, to a dry product.

**Superclasses:** `watr:TreatmentObjective-Dewatering`

## Equipment Cleaning

**Description:** Removal of accumulated foulants or residual materials from equipment to maintain or restore operation. Distinct from removing a constituent from the treated product stream.

**Superclasses:** `watr:TreatmentObjective`

## Lead Removal

**Description:** Reduction of lead in the treated stream.

**Superclasses:** `watr:TreatmentObjective-MetalsRemoval`

## Metals Removal

**Description:** Removal of dissolved metals from the treated stream, typically by raising pH or dosing sulfide so that they precipitate as hydroxides or sulfides and are then separated out.

**Superclasses:** `watr:TreatmentObjective-DissolvedSolidsRemoval`

## Neutralization

**Description:** pH adjustment to neutral, typically with a base, as in high-density sludge treatment.

**Superclasses:** `watr:TreatmentObjective-pHControl`

## Nitrogen Removal

**Description:** Net removal of nitrogen from the treated stream, typically by converting nitrate to nitrogen gas so that it leaves as a gas.

**Superclasses:** `watr:TreatmentObjective-NutrientRemoval`

## Nutrient Removal

**Description:** Net removal of nitrogen or phosphorus from the treated stream, as opposed to its conversion from one form to another.

**Superclasses:** `watr:TreatmentObjective-ConstituentRemoval`

## Organics Removal

**Description:** Net removal of biodegradable or dissolved organic material, measured as BOD, COD or TOC.

**Superclasses:** `watr:TreatmentObjective-ConstituentRemoval`

## Phosphorus Removal

**Description:** Net removal of phosphorus from the treated stream, by taking it into biomass or precipitating it into a solid that is then wasted.

**Superclasses:** `watr:TreatmentObjective-NutrientRemoval`

## Resource Recovery

**Description:** Recovery of a usable product -- water, energy or nutrients -- from a stream that would otherwise be discharged. A placeholder: the specific recovery objectives are not yet modeled.

**Superclasses:** `watr:TreatmentObjective`

## Silica Removal

**Description:** Reduction of the dissolved silica content of the treated stream, generally to protect downstream membranes from silica scaling.

**Superclasses:** `watr:TreatmentObjective-DissolvedSolidsRemoval`

## Softening

**Description:** Reduction of hardness by removing calcium and magnesium from the treated stream.

**Superclasses:** `watr:TreatmentObjective-DissolvedSolidsRemoval`

## Solids Removal

**Description:** Net removal of suspended or settleable solids from the treated stream.

**Superclasses:** `watr:TreatmentObjective-ConstituentRemoval`

## Stabilization

**Description:** Reduction of the volatile solids, pathogen content and odour potential of biosolids so that they can be stored, used or disposed of.

**Superclasses:** `watr:TreatmentObjective`

## Sulfate Removal

**Description:** Reduction of the dissolved sulfate content of the treated stream, as in acid mine drainage treatment where it is precipitated as gypsum or ettringite.

**Superclasses:** `watr:TreatmentObjective-DissolvedSolidsRemoval`

## Thickening

**Description:** Raising the solids concentration of a sludge or slurry while it remains pumpable. Distinguished from dewatering by the state of the product.

**Superclasses:** `watr:TreatmentObjective-VolumeReduction`

## Turbidity Removal

**Description:** Reduction of the turbidity of the treated stream, the objective of polishing filtration.

**Superclasses:** `watr:TreatmentObjective-SolidsRemoval`

## Volume Reduction

**Description:** Reduction of the volume of a sludge or slurry by removing water from it. The parent of thickening, dewatering and drying, which differ in the state of the product.

**Superclasses:** `watr:TreatmentObjective`

## pH Control

**Description:** Bringing the pH of the treated stream to a target value, or holding it there.

**Superclasses:** `watr:TreatmentObjective`
