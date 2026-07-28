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

## Role-Overflow

**Description:** A connection point that discharges liquid above a tank's working level.

**Superclass:** Role-Discharge

## Thickening

**Description:** Increasing the solids concentration of a sludge or slurry.

**Superclass:** Role-SolidsHandling

## Dewatering

**Description:** Removing or separating water from another material, typically solids.

**Superclass:** Role-SolidsHandling

