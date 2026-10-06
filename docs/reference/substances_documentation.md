# Substances and Enumerations Classes

## Expanded Uncertainty

**Description:** Total uncertainty multiplied by coverage factor

**Superclasses:** `watr:DataProcessing-AccuracyMetrics`

## Percent Recovery

**Description:** Ratio of measured to known value (for spike/recovery tests)

**Superclasses:** `watr:DataProcessing-AccuracyMetrics`

## R-Squared

**Description:** Coefficient of determination for calibration curves

**Superclasses:** `watr:DataProcessing-AccuracyMetrics`

## Total Uncertainty

**Description:** Combined standard uncertainty from all sources

**Superclasses:** `watr:DataProcessing-AccuracyMetrics`

## Count

**Description:** Count of data points

**Superclasses:** `watr:DataProcessing-Aggregate`

## Maximum

**Description:** Maximum value from data points

**Superclasses:** `watr:DataProcessing-Aggregate`

## Mean

**Description:** Arithmetic mean (average) of data points

**Superclasses:** `watr:DataProcessing-Aggregate`

## Median

**Description:** Middle value of sorted data points

**Superclasses:** `watr:DataProcessing-Aggregate`

## Minimum

**Description:** Minimum value from data points

**Superclasses:** `watr:DataProcessing-Aggregate`

## Mode

**Description:** Most frequently occurring value in data points

**Superclasses:** `watr:DataProcessing-Aggregate`

## Range

**Description:** Difference between maximum and minimum values

**Superclasses:** `watr:DataProcessing-Aggregate`

## Standard Deviation

**Description:** Standard deviation of data points

**Superclasses:** `watr:DataProcessing-Aggregate`

## Sum

**Description:** Sum of all data points

**Superclasses:** `watr:DataProcessing-Aggregate`

## Variance

**Description:** Variance of data points

**Superclasses:** `watr:DataProcessing-Aggregate`

## Count

**Description:** The associated property represents a count over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Maximum

**Description:** The associated property represents the maximum value over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Mean

**Description:** The associated property represents the arithmetic mean over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Median

**Description:** The associated property represents the median value over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Minimum

**Description:** The associated property represents the minimum value over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Mode

**Description:** The associated property represents the most frequently occurring value over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Percentile

**Description:** The associated property represents the percentile value over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Range

**Description:** The associated property represents the difference between maximum and minimum over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Standard Deviation

**Description:** The associated property represents the standard deviation over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Sum

**Description:** The associated property represents the sum over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Total

**Description:** The associated property represents the total amount of the characterized quantity or substance.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Variance

**Description:** The associated property represents the variance over an aggregation scope.

**Superclasses:** `watr:EnumerationKind-Aggregation`

## Coagulant

**Description:** Class for coagulants used in wastewater treatment

**Superclasses:** `watr:WastewaterTreatmentChemical`

## Alum

**Description:** Aluminum sulfate (alum), a common coagulant

**Superclasses:** `watr:Coagulant`

## Ferric Chloride

**Description:** Ferric chloride, a coagulant for wastewater treatment

**Superclasses:** `watr:Coagulant`

## Polyaluminum Chloride

**Description:** Polyaluminum chloride (PAC), a coagulant

**Superclasses:** `watr:Coagulant`

## Composition Complement Rule

**Description:** Completes an explicitly complete, common-basis percent composition (watr:hasCompleteComposition true) that leaves exactly one constituent unquantified: that fraction is inferred to be the remainder of the others, 100 minus their sum. A medium declared as 12% salt plus a water fraction with no value gains an inferred water value of 88. The fraction may be a blank node or a named one. The rule stays silent when more than one fraction is unquantified, when none is quantified, when any quantified fraction is a range (s223:Aspect-LowLimit / s223:Aspect-HighLimit), and when the remainder would be negative; watr:CompositionPercentageShape reports that last case.

## Composition Fraction Bounds

**Description:** Each declared constituent percentage must lie between zero and 100, inclusive.

## Composition Interval Consistency

**Description:** Exact values and lower/upper bounds on each constituent and fraction basis must have a common feasible value.

## Composition Percentage Shape

**Description:** A medium's constituent mass or volume fractions expressed in percent cannot add up to more than 100%. Where a constituent is given as a range (s223:Aspect-LowLimit / s223:Aspect-HighLimit), the greatest declared lower bound for that constituent is the one that counts, since only the lower bounds must all be simultaneously satisfiable.

## Ammonia

**Description:** Ammonia present as a dissolved nitrogen-bearing constituent of a treatment medium.

**Superclasses:** `watr:Constituent-Nitrogen`

## Arsenic

**Description:** Arsenic species in water, including dissolved arsenite and arsenate.

**Superclasses:** `watr:Constituent-DissolvedSolids`

## Bacteria

**Description:** Bacteria present as constituents of a treatment medium.

**Superclasses:** `watr:Constituent-Pathogens`

## Chlorine Residual

**Description:** Chlorine remaining in the water after disinfection, free or combined. Wanted in a distribution system and unwanted in a discharge, which is why removing it is an objective of its own.

**Superclasses:** `s223:Medium-Constituent`

## Cyanide

**Description:** Cyanide present as a constituent of a treatment medium. Highly toxic to aquatic life.

**Superclasses:** `s223:Medium-Constituent`

## Dissolved Oxygen

**Description:** Molecular oxygen dissolved in a treatment medium.

**Superclasses:** `s223:Medium-Constituent`

## Dissolved Solids

**Description:** Material dissolved in a treatment medium rather than suspended in it, measured together as total dissolved solids.

**Superclasses:** `s223:Medium-Constituent`

## Hardness

**Description:** Calcium and magnesium dissolved in a treatment medium, taken together as one constituent because that is what a hardness measurement reports and what softening removes.

**Superclasses:** `watr:Constituent-DissolvedSolids`

## Inorganic Carbon

**Description:** Inorganic carbon species present as constituents of a treatment medium.

**Superclasses:** `s223:Medium-Constituent`

## Inorganics

**Description:** Inorganic chemical matter present as a constituent of a treatment medium.

**Superclasses:** `s223:Medium-Constituent`

## Lead

**Description:** Lead species in water.

**Superclasses:** `watr:Constituent-Metals`

## Metals

**Description:** Metal species present as constituents of a treatment medium, dissolved or complexed.

**Superclasses:** `watr:Constituent-DissolvedSolids`

## Nitrate

**Description:** Nitrate present as an oxidized nitrogen-bearing constituent of a treatment medium.

**Superclasses:** `watr:Constituent-Nitrogen`

## Nitrite

**Description:** Nitrite present as an intermediate nitrogen-bearing constituent of a treatment medium.

**Superclasses:** `watr:Constituent-Nitrogen`

## Nitrogen

**Description:** Nitrogen present as a constituent of a treatment medium in any form: ammonia, nitrite, nitrate and organic nitrogen together.

**Superclasses:** `s223:Medium-Constituent`

## Nitrogen Oxides

**Description:** Nitrogen oxide species present as constituents of a treatment medium, including gaseous or dissolved forms.

**Superclasses:** `s223:Medium-Constituent`

## Organic Carbon

**Description:** Organic carbon present as a constituent of a treatment medium.

**Superclasses:** `watr:Constituent-Organics`

## Organic Nitrogen

**Description:** Nitrogen bound in organic matter present as a constituent of a treatment medium, which hydrolysis releases as ammonia.

**Superclasses:** `watr:Constituent-Nitrogen`

## Organics

**Description:** Organic chemical matter present as a constituent of a treatment medium.

**Superclasses:** `s223:Medium-Constituent`

## PFAS

**Description:** Per- and polyfluoroalkyl substances present as constituents of a treatment medium.

**Superclasses:** `watr:Constituent-Organics`

## Particles

**Description:** Particulate matter present as a constituent of a medium.

**Superclasses:** `s223:Medium-Constituent`

## Pathogens

**Description:** Disease-causing organisms present as constituents of a treatment medium. The constituent disinfection targets.

**Superclasses:** `s223:Medium-Constituent`

## Phosphate

**Description:** Phosphate present as a dissolved phosphorus-bearing constituent of a treatment medium, the form biological and chemical phosphorus removal act on.

**Superclasses:** `watr:Constituent-Phosphorus`

## Phosphorus

**Description:** Phosphorus present as a constituent of a treatment medium in any form, the constituent a total phosphorus limit is written against.

**Superclasses:** `s223:Medium-Constituent`

## Protozoa

**Description:** Protozoa present as constituents of a treatment medium, including the cysts and oocysts that resist chlorination.

**Superclasses:** `watr:Constituent-Pathogens`

## Salt

**Description:** Dissolved inorganic salt present as a constituent of a treatment medium. The constituent desalination removes.

**Superclasses:** `watr:Constituent-DissolvedSolids`

## Silica

**Description:** Silica present as a constituent of a treatment medium, dissolved or colloidal. A scalant on membranes and in evaporators.

**Superclasses:** `watr:Constituent-DissolvedSolids`

## Solids

**Description:** Solid material present as a constituent of a treatment medium.

**Superclasses:** `watr:Constituent-Particles`

## Sulfate

**Description:** Sulfate present as a dissolved constituent of a treatment medium.

**Superclasses:** `watr:Constituent-DissolvedSolids`

## Suspended Solids

**Description:** Solid particulate matter suspended in water rather than dissolved, including organic and inorganic material carried in the fluid.

**Superclasses:** `watr:Constituent-Solids`

## Viruses

**Description:** Viruses present as constituents of a treatment medium.

**Superclasses:** `watr:Constituent-Pathogens`

## Volatile Organic Compounds

**Description:** Organic compounds volatile enough to leave the water into an off-gas stream, which is why air stripping removes them and settling does not.

**Superclasses:** `watr:Constituent-Organics`

## Accuracy Metrics

**Description:** Combined accuracy measures (precision and trueness)

**Superclasses:** `s223:EnumerationKind-DataProcessing`

## Aggregate

**Description:** Parent class for aggregation functions that combine multiple data points

**Superclasses:** `s223:EnumerationKind-DataProcessing`

## Error Metrics

**Description:** Parent class for error and uncertainty measurements

**Superclasses:** `s223:EnumerationKind-DataProcessing`

## Filter

**Description:** Parent class for filtering methods to remove outliers or unwanted data points

**Superclasses:** `s223:EnumerationKind-DataProcessing`

## Interpolation

**Description:** Parent class for interpolation methods to estimate values between known data points

**Superclasses:** `s223:EnumerationKind-DataProcessing`

## Normalization

**Description:** Parent class for normalization methods to scale data to a standard range

**Superclasses:** `s223:EnumerationKind-DataProcessing`

## Precision Metrics

**Description:** Metrics for precision and repeatability measurements

**Superclasses:** `s223:EnumerationKind-DataProcessing`

## Synchronization

**Description:** Parent class for synchronization methods to align data from multiple sources to common time intervals

**Superclasses:** `s223:EnumerationKind-DataProcessing`

## Disinfectant

**Description:** Class for disinfectants used in wastewater treatment

**Superclasses:** `watr:WastewaterTreatmentChemical`

## Chlorine

**Description:** Chlorine, a common disinfectant

**Superclasses:** `watr:Disinfectant`

## Ozone

**Description:** Ozone, an advanced disinfectant

**Superclasses:** `watr:Disinfectant`

## Aggregation

**Description:** EnumerationKind for aggregation semantics carried by a property, such as total, mean, maximum, or minimum.

**Superclasses:** `s223:EnumerationKind-Aspect`

## DataQuality

**Description:** This EnumerationKind describes methods of data processing, aggregation, or imputation

**Superclasses:** `s223:EnumerationKind`

## Runtime

**Description:** An enumeration kind describing the accumulated operating time of a piece of equipment.

**Superclasses:** `s223:EnumerationKind`

## Absolute Error

**Description:** Absolute difference between measured and true/reference value

**Superclasses:** `watr:DataProcessing-ErrorMetrics`

## Bias

**Description:** Systematic deviation from true value (trueness measure)

**Superclasses:** `watr:DataProcessing-ErrorMetrics`

## Mean Absolute Error (MAE)

**Description:** Average of absolute errors across multiple measurements

**Superclasses:** `watr:DataProcessing-ErrorMetrics`

## Mean Absolute Percentage Error (MAPE)

**Description:** Average of absolute percentage errors

**Superclasses:** `watr:DataProcessing-ErrorMetrics`

## Mean Squared Error (MSE)

**Description:** Average of squared errors

**Superclasses:** `watr:DataProcessing-ErrorMetrics`

## Relative Error

**Description:** Error expressed as a percentage of the true/reference value

**Superclasses:** `watr:DataProcessing-ErrorMetrics`

## Root Mean Squared Error (RMSE)

**Description:** Square root of MSE, in same units as measurements

**Superclasses:** `watr:DataProcessing-ErrorMetrics`

## Flocculant

**Description:** Class for flocculants used in wastewater treatment

**Superclasses:** `watr:WastewaterTreatmentChemical`

## Polyacrylamide

**Description:** Polyacrylamide, a common flocculant

**Superclasses:** `watr:Flocculant-Polymer`

## Polymer Flocculant

**Description:** Flocculant that is a type of polymer

**Superclasses:** `watr:Flocculant`

## Sludge

**Description:** A semi-solid slurry composed of water and solids.

**Superclasses:** `s223:Fluid-Water`

## Heavy Metal Removal Agent

**Description:** Class for chemicals used to remove heavy metals

**Superclasses:** `watr:WastewaterTreatmentChemical`

## Sodium Sulfide

**Description:** Sodium sulfide, used to precipitate heavy metals

**Superclasses:** `watr:HeavyMetalRemovalAgent`

## High Purity Oxygen

**Description:** Class for high purity oxygen used in wastewater treatment

**Superclasses:** `watr:WastewaterTreatmentChemical`

## Backward Fill

**Description:** Propagate next valid observation backward to fill gaps

**Superclasses:** `watr:DataProcessing-Interpolation`

## Forward Fill

**Description:** Propagate last valid observation forward to fill gaps

**Superclasses:** `watr:DataProcessing-Interpolation`

## Linear Interpolation

**Description:** Linear interpolation between two adjacent data points

**Superclasses:** `watr:DataProcessing-Interpolation`

## Nearest Neighbor

**Description:** Use the value of the nearest known data point

**Superclasses:** `watr:DataProcessing-Interpolation`

## Polynomial Interpolation

**Description:** Polynomial interpolation using multiple data points

**Superclasses:** `watr:DataProcessing-Interpolation`

## Spline Interpolation

**Description:** Cubic spline interpolation for smooth curves

**Superclasses:** `watr:DataProcessing-Interpolation`

## Decimal Scaling

**Description:** Normalize by moving the decimal point of values

**Superclasses:** `watr:DataProcessing-Normalization`

## Min-Max Normalization

**Description:** Scale data to a fixed range, typically [0, 1]

**Superclasses:** `watr:DataProcessing-Normalization`

## Z-Score Normalization

**Description:** Standardize data to have mean=0 and standard deviation=1

**Superclasses:** `watr:DataProcessing-Normalization`

## Odor Control Agent

**Description:** Class for chemicals used for odor control

**Superclasses:** `watr:WastewaterTreatmentChemical`

## Activated Carbon

**Description:** Activated carbon, used to absorb odors

**Superclasses:** `watr:OdorControlAgent`

## Oxidizing Agent

**Description:** Class for oxidizing agents used in water treatment

**Superclasses:** `watr:WastewaterTreatmentChemical`

## Hydrogen Peroxide

**Description:** Hydrogen peroxide, an oxidizing agent commonly used in advanced oxidation processes

**Superclasses:** `watr:OxidizingAgent`

## Coefficient of Variation

**Description:** Ratio of standard deviation to mean (relative precision)

**Superclasses:** `watr:DataProcessing-PrecisionMetrics`

## Confidence Interval

**Description:** Range within which true value likely falls with specified confidence level

**Superclasses:** `watr:DataProcessing-PrecisionMetrics`

## Repeatability Standard Deviation

**Description:** Standard deviation under repeatability conditions (same operator, equipment, short time)

**Superclasses:** `watr:DataProcessing-PrecisionMetrics`

## Reproducibility Standard Deviation

**Description:** Standard deviation under reproducibility conditions (different operators, equipment, time)

**Superclasses:** `watr:DataProcessing-PrecisionMetrics`

## Reducing Agent

**Description:** Class for reducing agents used in water treatment

**Superclasses:** `watr:WastewaterTreatmentChemical`

## Aerobic

**Description:** The zone is commissioned to run in an aerobic regime, with dissolved oxygen present. A design claim, not a reading: a basin whose blowers are off still carries it.

**Superclasses:** `s223:EnumerationKind-Role`

## Anaerobic

**Description:** The zone is commissioned to run in an anaerobic regime, without dissolved oxygen or nitrate.

**Superclasses:** `s223:EnumerationKind-Role`

## Anoxic

**Description:** The zone is commissioned to run in an anoxic regime, without dissolved oxygen and with nitrate present.

**Superclasses:** `s223:EnumerationKind-Role`

## Role-Backwash

**Description:** Deprecated. Model backwashing as watr:hasProcess watr:Process-Backwashing on the equipment or system that performs it.

**Superclasses:** `s223:EnumerationKind-Role`

## Containment

**Description:** The equipment confines a spill or an off-specification stream to keep it out of the rest of the plant.

**Superclasses:** `s223:EnumerationKind-Role`

## Detention

**Description:** The equipment holds flow for a designed interval, typically to allow a reaction or settling to complete.

**Superclasses:** `s223:EnumerationKind-Role`

## Role-Drain

**Description:** A connection point that empties a vessel below its working level, for maintenance or solids removal.

**Superclasses:** `s223:Role-Discharge`

## Equalization

**Description:** The equipment buffers variation in flow or load so that the processes downstream of it see a steadier stream.

**Superclasses:** `s223:EnumerationKind-Role`

## Extended

**Description:** The equipment is operated at an extended solids retention time.

**Superclasses:** `s223:EnumerationKind-Role`

## Feed

**Description:** A connection point that admits the stream a process acts on.

**Superclasses:** `s223:EnumerationKind-Role`

## MakeUp

**Description:** A connection point that admits water to replace what a process consumes or loses.

**Superclasses:** `s223:EnumerationKind-Role`

## NitrogenRemoval (deprecated role)

**Description:** Deprecated objective designation formerly modeled as a role; use TreatmentObjective-NitrogenRemoval.

## NutrientRemoval (deprecated role)

**Description:** Deprecated objective designation formerly modeled as a role; use TreatmentObjective-NutrientRemoval.

## Role-Overflow

**Description:** A connection point that discharges liquid above a tank's working level.

**Superclasses:** `s223:Role-Discharge`

## Permeate

**Description:** A connection point carrying the stream that has passed through a membrane.

**Superclasses:** `s223:EnumerationKind-Role`

## PhosphorusRemoval (deprecated role)

**Description:** Deprecated objective designation formerly modeled as a role; use TreatmentObjective-PhosphorusRemoval.

## Posttreatment

**Description:** The equipment sits after the main treatment train and conditions the effluent for discharge or reuse.

**Superclasses:** `s223:EnumerationKind-Role`

## Pretreatment

**Description:** The equipment sits ahead of the main treatment train and conditions the influent for it.

**Superclasses:** `s223:EnumerationKind-Role`

## Primary

**Description:** Primary treatment: the equipment belongs to the stage that removes settleable and floatable solids ahead of biological treatment. Not to be confused with s223:Role-Primary, which denotes a primary loop.

**Superclasses:** `s223:EnumerationKind-Role`

## Retention

**Description:** The equipment holds flow to attenuate a peak, typically stormwater, and releases it at a controlled rate.

**Superclasses:** `s223:EnumerationKind-Role`

## Secondary

**Description:** Secondary treatment: the equipment belongs to the stage that removes biodegradable organics and suspended solids, typically biologically. Not to be confused with s223:Role-Secondary, which denotes a secondary loop.

**Superclasses:** `s223:EnumerationKind-Role`

## SolidsHandling (deprecated role)

**Description:** Deprecated objective designation formerly modeled as a role; use TreatmentObjective-VolumeReduction.

## Stabilization (deprecated role)

**Description:** Deprecated objective designation formerly modeled as a role; use TreatmentObjective-Stabilization.

## Stepfeed

**Description:** The equipment is fed at multiple points along its length rather than only at its head.

**Superclasses:** `s223:EnumerationKind-Role`

## Storage

**Description:** The equipment holds water or sludge for later use rather than acting on it.

**Superclasses:** `s223:EnumerationKind-Role`

## Tertiary

**Description:** Tertiary treatment: the equipment belongs to the polishing stage downstream of secondary treatment, for residual solids, nutrients or specific constituents.

**Superclasses:** `s223:EnumerationKind-Role`

## Sodium Chloride

**Description:** Sodium chloride dissolved in a treatment medium, the dominant salt in seawater and in most brackish sources.

**Superclasses:** `watr:Constituent-Salt`

## Sludge-MixedLiquor

**Description:** Mixed liquor is the mixture of wastewater and activated sludge in the aeration basin of a wastewater treatment plant. It contains suspended solids and water.

**Superclasses:** `watr:Fluid-Sludge`

## Downsampling

**Description:** Decrease the sampling frequency of data to a lower rate

**Superclasses:** `watr:DataProcessing-Synchronization`

## Resampling

**Description:** Resample data to a different frequency or time interval

**Superclasses:** `watr:DataProcessing-Synchronization`

## Time Alignment

**Description:** Align data points from different sources to common timestamps

**Superclasses:** `watr:DataProcessing-Synchronization`

## Upsampling

**Description:** Increase the sampling frequency of data to a higher rate

**Superclasses:** `watr:DataProcessing-Synchronization`

## Wastewater Treatment Chemical

**Description:** Base class for all chemicals used in wastewater treatment

**Superclasses:** `s223:Medium-Constituent`

## Water-Brackish

**Description:** Moderately saline water (typical salinity 0.5-3%) modeled as a constituent-bearing mixture of water and dissolved salt so that S223 can recognize the shared water constituent across aqueous media.

**Superclasses:** `s223:Fluid-Water`

## Water-Brine

**Description:** Concentrated saline water modeled as a constituent-bearing mixture of water and dissolved salt so that S223 can recognize the shared water constituent across aqueous media.

**Superclasses:** `s223:Fluid-Water`

## Water-Freshwater

**Description:** Low-salinity surface or ground water modeled as a constituent-bearing mixture dominated by the water constituent so that S223 can recognize the shared water constituent across aqueous media.

**Superclasses:** `s223:Fluid-Water`

## Water-Seawater

**Description:** Saline surface water (typical salinity ~3.5%) modeled as a constituent-bearing mixture of water and dissolved salt so that S223 can recognize the shared water constituent across aqueous media.

**Superclasses:** `s223:Fluid-Water`

## has complete composition

**Description:** When true, the declared constituent fractions exhaust this medium's composition. Enables complement inference when all fractions share a mass or volume basis and percent units; omitted constituents must not be inferred as part of another constituent.

## pH Adjuster

**Description:** Class for pH adjusters used in wastewater treatment

**Superclasses:** `watr:WastewaterTreatmentChemical`

## Lime

**Description:** Calcium hydroxide (lime), used to increase pH

**Superclasses:** `watr:pHAdjuster`

## Sulfuric Acid

**Description:** Sulfuric acid, used to decrease pH

**Superclasses:** `watr:pHAdjuster`
