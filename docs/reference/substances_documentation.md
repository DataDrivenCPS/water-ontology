# EnumerationKinds Classes

## DataQuality

**Description:** This EnumerationKind describes methods of data processing, aggregation, or imputation

**Superclass:** EnumerationKind

## Filter

**Description:** Parent class for filtering methods to remove outliers or unwanted data points

**Superclass:** EnumerationKind-DataProcessing

## Aggregate

**Description:** Parent class for aggregation functions that combine multiple data points

**Superclass:** EnumerationKind-DataProcessing

## Mean

**Description:** Arithmetic mean (average) of data points

**Superclass:** DataProcessing-Aggregate

## Mean

**Description:** The associated property represents the arithmetic mean over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Median

**Description:** Middle value of sorted data points

**Superclass:** DataProcessing-Aggregate

## Median

**Description:** The associated property represents the median value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Maximum

**Description:** Maximum value from data points

**Superclass:** DataProcessing-Aggregate

## Maximum

**Description:** The associated property represents the maximum value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Minimum

**Description:** Minimum value from data points

**Superclass:** DataProcessing-Aggregate

## Minimum

**Description:** The associated property represents the minimum value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Sum

**Description:** Sum of all data points

**Superclass:** DataProcessing-Aggregate

## Sum

**Description:** The associated property represents the sum over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Count

**Description:** Count of data points

**Superclass:** DataProcessing-Aggregate

## Count

**Description:** The associated property represents a count over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Standard Deviation

**Description:** Standard deviation of data points

**Superclass:** DataProcessing-Aggregate

## Standard Deviation

**Description:** The associated property represents the standard deviation over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Variance

**Description:** Variance of data points

**Superclass:** DataProcessing-Aggregate

## Variance

**Description:** The associated property represents the variance over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Range

**Description:** Difference between maximum and minimum values

**Superclass:** DataProcessing-Aggregate

## Range

**Description:** The associated property represents the difference between maximum and minimum over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Mode

**Description:** Most frequently occurring value in data points

**Superclass:** DataProcessing-Aggregate

## Mode

**Description:** The associated property represents the most frequently occurring value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Aggregation

**Description:** EnumerationKind for aggregation semantics carried by a property, such as total, mean, maximum, or minimum.

**Superclass:** EnumerationKind-Aspect

## Total

**Description:** The associated property represents the total amount of the characterized quantity or substance.

**Superclass:** EnumerationKind-Aggregation

## Percentile

**Description:** The associated property represents the percentile value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Interpolation

**Description:** Parent class for interpolation methods to estimate values between known data points

**Superclass:** EnumerationKind-DataProcessing

## Linear Interpolation

**Description:** Linear interpolation between two adjacent data points

**Superclass:** DataProcessing-Interpolation

## Spline Interpolation

**Description:** Cubic spline interpolation for smooth curves

**Superclass:** DataProcessing-Interpolation

## Polynomial Interpolation

**Description:** Polynomial interpolation using multiple data points

**Superclass:** DataProcessing-Interpolation

## Nearest Neighbor

**Description:** Use the value of the nearest known data point

**Superclass:** DataProcessing-Interpolation

## Forward Fill

**Description:** Propagate last valid observation forward to fill gaps

**Superclass:** DataProcessing-Interpolation

## Backward Fill

**Description:** Propagate next valid observation backward to fill gaps

**Superclass:** DataProcessing-Interpolation

## Normalization

**Description:** Parent class for normalization methods to scale data to a standard range

**Superclass:** EnumerationKind-DataProcessing

## Min-Max Normalization

**Description:** Scale data to a fixed range, typically [0, 1]

**Superclass:** DataProcessing-Normalization

## Z-Score Normalization

**Description:** Standardize data to have mean=0 and standard deviation=1

**Superclass:** DataProcessing-Normalization

## Decimal Scaling

**Description:** Normalize by moving the decimal point of values

**Superclass:** DataProcessing-Normalization

## Synchronization

**Description:** Parent class for synchronization methods to align data from multiple sources to common time intervals

**Superclass:** EnumerationKind-DataProcessing

## Resampling

**Description:** Resample data to a different frequency or time interval

**Superclass:** DataProcessing-Synchronization

## Upsampling

**Description:** Increase the sampling frequency of data to a higher rate

**Superclass:** DataProcessing-Synchronization

## Downsampling

**Description:** Decrease the sampling frequency of data to a lower rate

**Superclass:** DataProcessing-Synchronization

## Time Alignment

**Description:** Align data points from different sources to common timestamps

**Superclass:** DataProcessing-Synchronization

## Error Metrics

**Description:** Parent class for error and uncertainty measurements

**Superclass:** EnumerationKind-DataProcessing

## Absolute Error

**Description:** Absolute difference between measured and true/reference value

**Superclass:** DataProcessing-ErrorMetrics

## Relative Error

**Description:** Error expressed as a percentage of the true/reference value

**Superclass:** DataProcessing-ErrorMetrics

## Mean Absolute Error (MAE)

**Description:** Average of absolute errors across multiple measurements

**Superclass:** DataProcessing-ErrorMetrics

## Mean Squared Error (MSE)

**Description:** Average of squared errors

**Superclass:** DataProcessing-ErrorMetrics

## Root Mean Squared Error (RMSE)

**Description:** Square root of MSE, in same units as measurements

**Superclass:** DataProcessing-ErrorMetrics

## Mean Absolute Percentage Error (MAPE)

**Description:** Average of absolute percentage errors

**Superclass:** DataProcessing-ErrorMetrics

## Bias

**Description:** Systematic deviation from true value (trueness measure)

**Superclass:** DataProcessing-ErrorMetrics

## Precision Metrics

**Description:** Metrics for precision and repeatability measurements

**Superclass:** EnumerationKind-DataProcessing

## Repeatability Standard Deviation

**Description:** Standard deviation under repeatability conditions (same operator, equipment, short time)

**Superclass:** DataProcessing-PrecisionMetrics

## Reproducibility Standard Deviation

**Description:** Standard deviation under reproducibility conditions (different operators, equipment, time)

**Superclass:** DataProcessing-PrecisionMetrics

## Coefficient of Variation

**Description:** Ratio of standard deviation to mean (relative precision)

**Superclass:** DataProcessing-PrecisionMetrics

## Confidence Interval

**Description:** Range within which true value likely falls with specified confidence level

**Superclass:** DataProcessing-PrecisionMetrics

## Accuracy Metrics

**Description:** Combined accuracy measures (precision and trueness)

**Superclass:** EnumerationKind-DataProcessing

## Total Uncertainty

**Description:** Combined standard uncertainty from all sources

**Superclass:** DataProcessing-AccuracyMetrics

## Expanded Uncertainty

**Description:** Total uncertainty multiplied by coverage factor

**Superclass:** DataProcessing-AccuracyMetrics

## Percent Recovery

**Description:** Ratio of measured to known value (for spike/recovery tests)

**Superclass:** DataProcessing-AccuracyMetrics

## R-Squared

**Description:** Coefficient of determination for calibration curves

**Superclass:** DataProcessing-AccuracyMetrics

## Role-Backwash

**Description:** A role for a stream or operating mode that reverses flow through a filter to dislodge and carry away accumulated solids.

**Superclass:** EnumerationKind-Role

## Role-Drain

**Description:** A role for a connection or stream that removes liquid from equipment, typically for emptying or maintenance.

**Superclass:** Role-Discharge

## Role-NutrientRemoval

**Description:** A role for a process whose purpose is the removal of nutrients, principally nitrogen and phosphorus.

**Superclass:** EnumerationKind-Role

## Role-NitrogenRemoval

**Description:** A role for a process whose purpose is the removal of nitrogen species from water.

**Superclass:** Role-NutrientRemoval

## Role-PhosphorusRemoval

**Description:** A role for a process whose purpose is the removal of phosphorus from water.

**Superclass:** Role-NutrientRemoval

## MakeUp

**Description:** A role for a stream that adds water or chemical to replace losses and maintain volume or concentration.

**Superclass:** EnumerationKind-Role

## Feed

**Description:** A role for a stream or vessel that supplies influent to a process.

**Superclass:** EnumerationKind-Role

## Permeate

**Description:** A role for the stream that has passed through a membrane, as opposed to the retained concentrate.

**Superclass:** EnumerationKind-Role

## Storage

**Description:** A role for a vessel that holds water or material for later use.

**Superclass:** EnumerationKind-Role

## Aerobic

**Description:** A role for a process or vessel operated in the presence of dissolved oxygen, supporting aerobic microbial metabolism.

**Superclass:** EnumerationKind-Role

## Anaerobic

**Description:** A role for a process or vessel operated in the absence of both dissolved oxygen and nitrate, supporting anaerobic microbial metabolism.

**Superclass:** EnumerationKind-Role

## Anoxic

**Description:** A role for a process or vessel operated without dissolved oxygen but with nitrate or nitrite present, supporting denitrification.

**Superclass:** EnumerationKind-Role

## Stabilization

**Description:** A role for a process that reduces the biodegradability, odor, or pathogen content of solids.

**Superclass:** EnumerationKind-Role

## Equalization

**Description:** A role for a vessel that buffers variation in flow rate or load so that downstream processes receive a steadier input.

**Superclass:** EnumerationKind-Role

## Detention

**Description:** A role for a vessel that holds water for a defined period so that a treatment process can take place.

**Superclass:** EnumerationKind-Role

## Retention

**Description:** A role for a vessel that holds water or solids for storage or continued settling.

**Superclass:** EnumerationKind-Role

## Containment

**Description:** A role for a vessel or structure that holds material to prevent its release to the environment.

**Superclass:** EnumerationKind-Role

## Pretreatment

**Description:** A role for a process applied ahead of the main treatment stages to remove material that would otherwise impair them.

**Superclass:** EnumerationKind-Role

## Primary

**Description:** A role for the first major treatment stage, typically removing settleable and floatable solids.

**Superclass:** EnumerationKind-Role

## Secondary

**Description:** A role for the treatment stage following primary treatment, typically the biological removal of dissolved and colloidal organics.

**Superclass:** EnumerationKind-Role

## Extended

**Description:** A role for an activated sludge process operated at long hydraulic and solids retention times, as in extended aeration.

**Superclass:** EnumerationKind-Role

## Stepfeed

**Description:** A role for an activated sludge configuration in which influent is introduced at multiple points along the reactor.

**Superclass:** EnumerationKind-Role

## Tertiary

**Description:** A role for treatment applied after secondary treatment to further improve effluent quality.

**Superclass:** EnumerationKind-Role

## Solids handling (e.g., biosolids disposal)

**Description:** A role for processes that thicken, stabilize, dewater, or dispose of solids removed from the liquid stream.

**Superclass:** EnumerationKind-Role

## Posttreatment

**Description:** A role for a process applied after the main treatment stages to condition the effluent for discharge or reuse.

**Superclass:** EnumerationKind-Role

## Runtime

**Description:** An enumeration kind describing the accumulated operating time of a piece of equipment.

**Superclass:** EnumerationKind
