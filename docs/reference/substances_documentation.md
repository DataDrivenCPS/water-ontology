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

## Median

**Description:** Middle value of sorted data points

**Superclass:** DataProcessing-Aggregate

## Maximum

**Description:** Maximum value from data points

**Superclass:** DataProcessing-Aggregate

## Minimum

**Description:** Minimum value from data points

**Superclass:** DataProcessing-Aggregate

## Sum

**Description:** Sum of all data points

**Superclass:** DataProcessing-Aggregate

## Count

**Description:** Count of data points

**Superclass:** DataProcessing-Aggregate

## Standard Deviation

**Description:** Standard deviation of data points

**Superclass:** DataProcessing-Aggregate

## Variance

**Description:** Variance of data points

**Superclass:** DataProcessing-Aggregate

## Range

**Description:** Difference between maximum and minimum values

**Superclass:** DataProcessing-Aggregate

## Mode

**Description:** Most frequently occurring value in data points

**Superclass:** DataProcessing-Aggregate

## Aggregation

**Description:** EnumerationKind for aggregation semantics carried by a property, such as total, mean, maximum, or minimum.

**Superclass:** EnumerationKind-Aspect

## Total

**Description:** The associated property represents the total amount of the characterized quantity or substance.

**Superclass:** EnumerationKind-Aggregation

## Maximum

**Description:** The associated property represents the maximum value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Minimum

**Description:** The associated property represents the minimum value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Mean

**Description:** The associated property represents the arithmetic mean over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Median

**Description:** The associated property represents the median value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Percentile

**Description:** The associated property represents the percentile value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Sum

**Description:** The associated property represents the sum over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Count

**Description:** The associated property represents a count over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Range

**Description:** The associated property represents the difference between maximum and minimum over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Mode

**Description:** The associated property represents the most frequently occurring value over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Variance

**Description:** The associated property represents the variance over an aggregation scope.

**Superclass:** EnumerationKind-Aggregation

## Standard Deviation

**Description:** The associated property represents the standard deviation over an aggregation scope.

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

**Description:** Deprecated. Model backwashing as watr:hasProcess watr:Process-Backwashing on the equipment or system that performs it.

**Superclass:** EnumerationKind-Role

## Role-Drain

**Description:** A connection point that empties a vessel below its working level, for maintenance or solids removal.

**Superclass:** Role-Discharge

## Role-Overflow

**Description:** A connection point that discharges liquid above a tank's working level.

**Superclass:** Role-Discharge

## MakeUp

**Description:** A connection point that admits water to replace what a process consumes or loses.

**Superclass:** EnumerationKind-Role

## Feed

**Description:** A connection point that admits the stream a process acts on.

**Superclass:** EnumerationKind-Role

## Permeate

**Description:** A connection point carrying the stream that has passed through a membrane.

**Superclass:** EnumerationKind-Role

## Storage

**Description:** The equipment holds water or sludge for later use rather than acting on it.

**Superclass:** EnumerationKind-Role

## Aerobic

**Description:** The zone is commissioned to run in an aerobic regime, with dissolved oxygen present. A design claim, not a reading: a basin whose blowers are off still carries it.

**Superclass:** EnumerationKind-Role

## Anaerobic

**Description:** The zone is commissioned to run in an anaerobic regime, without dissolved oxygen or nitrate.

**Superclass:** EnumerationKind-Role

## Anoxic

**Description:** The zone is commissioned to run in an anoxic regime, without dissolved oxygen and with nitrate present.

**Superclass:** EnumerationKind-Role

## Equalization

**Description:** The equipment buffers variation in flow or load so that the processes downstream of it see a steadier stream.

**Superclass:** EnumerationKind-Role

## Detention

**Description:** The equipment holds flow for a designed interval, typically to allow a reaction or settling to complete.

**Superclass:** EnumerationKind-Role

## Retention

**Description:** The equipment holds flow to attenuate a peak, typically stormwater, and releases it at a controlled rate.

**Superclass:** EnumerationKind-Role

## Containment

**Description:** The equipment confines a spill or an off-specification stream to keep it out of the rest of the plant.

**Superclass:** EnumerationKind-Role

## Pretreatment

**Description:** The equipment sits ahead of the main treatment train and conditions the influent for it.

**Superclass:** EnumerationKind-Role

## Primary

**Description:** Primary treatment: the equipment belongs to the stage that removes settleable and floatable solids ahead of biological treatment. Not to be confused with s223:Role-Primary, which denotes a primary loop.

**Superclass:** EnumerationKind-Role

## Secondary

**Description:** Secondary treatment: the equipment belongs to the stage that removes biodegradable organics and suspended solids, typically biologically. Not to be confused with s223:Role-Secondary, which denotes a secondary loop.

**Superclass:** EnumerationKind-Role

## Extended

**Description:** The equipment is operated at an extended solids retention time.

**Superclass:** EnumerationKind-Role

## Stepfeed

**Description:** The equipment is fed at multiple points along its length rather than only at its head.

**Superclass:** EnumerationKind-Role

## Tertiary

**Description:** Tertiary treatment: the equipment belongs to the polishing stage downstream of secondary treatment, for residual solids, nutrients or specific constituents.

**Superclass:** EnumerationKind-Role

## Posttreatment

**Description:** The equipment sits after the main treatment train and conditions the effluent for discharge or reuse.

**Superclass:** EnumerationKind-Role
