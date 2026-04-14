# Data Quality Metadata

WaTr includes a set of metadata properties and enumeration kinds that allow models to capture the quality, characteristics, and processing history of sensor measurements. This metadata is attached to instances of `s223:QuantifiableProperty` (and in some cases directly to `s223:Sensor`) using `watr:` relations.

## Overview

Data quality metadata in WaTr serves two purposes:

1. **Characterizing raw measurements** — describing the physical and temporal limits of a sensor (e.g., its measurement range, accuracy, and response time).
2. **Describing processed data** — linking a raw property to derived versions of itself (e.g., aggregated, interpolated, or normalized streams) and characterizing the processing method applied.

The two mechanisms work together: a `QuantifiableProperty` representing a raw sensor reading can carry characterization relations directly, and can also point to one or more `QuantifiableProperty` instances representing processed forms of that data via `watr:hasProcessedData`.

## Data Quality Relations

The following relations may be applied to an `s223:QuantifiableProperty`. Each relation points to another `s223:QuantifiableProperty` whose value (and units) convey the metadata quantity.

### Measurement Characterization

| Relation | Range | Description |
|---|---|---|
| `watr:hasTemporalResolution` | `s223:QuantifiableProperty` | Minimum time interval between successive measurements or data points. |
| `watr:hasNumericResolution` | `s223:QuantifiableProperty` | Smallest distinguishable difference between two measured values, in engineering units. |
| `watr:hasResponseTime` | `s223:QuantifiableProperty` | Time required for the sensor or measurement system to respond to a step change in the measured variable. |
| `watr:hasCalibrationCurve` | `s223:QuantifiableProperty` | Mathematical relationship or lookup table between raw sensor output and calibrated engineering units. |

### Range Characterization

| Relation | Range | Description |
|---|---|---|
| `watr:hasTemporalRange` | `s223:QuantifiableProperty` | Start and end times for which data has been recorded. |
| `watr:hasNumericRange` | `s223:QuantifiableProperty` | Span between the minimum and maximum measured values in engineering units. |
| `watr:hasVariableRange` | `s223:QuantifiableProperty` | Expected maximum or minimum for the measured variable during normal operation. |
| `watr:hasMeasurementRange` | `s223:QuantifiableProperty` | Maximum or minimum that can physically be measured (e.g., by the sensor hardware). Also applicable directly to `s223:Sensor`. |

### Error and Uncertainty Characterization

| Relation | Range | Description |
|---|---|---|
| `watr:hasAccuracy` | `s223:QuantifiableProperty` | Maximum expected deviation between the measured value and the true value, in engineering units. |
| `watr:hasPrecision` | `s223:QuantifiableProperty` | Repeatability or reproducibility of measurements under identical conditions. |
| `watr:hasBias` | `s223:QuantifiableProperty` | Systematic offset or drift in measurements relative to the true value. |

### Data Availability

| Relation | Range | Description |
|---|---|---|
| `watr:hasDropRate` | `s223:QuantifiableProperty` | Number of data points lost within a unit of time due to latencies or other factors. |

### Processed Data

| Relation | Range | Description |
|---|---|---|
| `watr:hasProcessedData` | `s223:QuantifiableProperty` | Links to a `QuantifiableProperty` that represents a processed, filtered, or transformed form of the raw measurement. The processing method is conveyed via `s223:hasAspect` using a `watr:EnumerationKind-DataProcessing` value. |

## Data Processing Enumeration Kinds

When a `QuantifiableProperty` is linked via `watr:hasProcessedData`, the processing method applied to produce it is described by attaching an `s223:hasAspect` triple whose object is one of the `watr:EnumerationKind-DataProcessing` enumeration values below.

All of these enumeration kinds are subclasses of `watr:EnumerationKind-DataProcessing`, which is itself a subclass of `s223:EnumerationKind`.

### Aggregation (`watr:DataProcessing-Aggregate`)

Statistical functions that combine multiple data points into a single value.

| Enumeration Kind | Label | Description |
|---|---|---|
| `watr:Aggregate-Mean` | Mean | Arithmetic mean (average) of data points. |
| `watr:Aggregate-Median` | Median | Middle value of sorted data points. |
| `watr:Aggregate-Max` | Maximum | Maximum value from data points. |
| `watr:Aggregate-Min` | Minimum | Minimum value from data points. |
| `watr:Aggregate-Sum` | Sum | Sum of all data points. |
| `watr:Aggregate-Count` | Count | Count of data points. |
| `watr:Aggregate-StdDev` | Standard Deviation | Standard deviation of data points. |
| `watr:Aggregate-Variance` | Variance | Variance of data points. |
| `watr:Aggregate-Range` | Range | Difference between maximum and minimum values. |
| `watr:Aggregate-Mode` | Mode | Most frequently occurring value in data points. |

### Interpolation (`watr:DataProcessing-Interpolation`)

Methods for estimating values between or in place of missing data points.

| Enumeration Kind | Label | Description |
|---|---|---|
| `watr:Interpolation-Linear` | Linear Interpolation | Linear interpolation between two adjacent data points. |
| `watr:Interpolation-Spline` | Spline Interpolation | Cubic spline interpolation for smooth curves. |
| `watr:Interpolation-Polynomial` | Polynomial Interpolation | Polynomial interpolation using multiple data points. |
| `watr:Interpolation-NearestNeighbor` | Nearest Neighbor | Use the value of the nearest known data point. |
| `watr:Interpolation-ForwardFill` | Forward Fill | Propagate the last valid observation forward to fill gaps. |
| `watr:Interpolation-BackwardFill` | Backward Fill | Propagate the next valid observation backward to fill gaps. |

### Normalization (`watr:DataProcessing-Normalization`)

Methods for scaling data to a standard range or distribution.

| Enumeration Kind | Label | Description |
|---|---|---|
| `watr:Normalization-MinMax` | Min-Max Normalization | Scale data to a fixed range, typically [0, 1]. |
| `watr:Normalization-ZScore` | Z-Score Normalization | Standardize data to have mean = 0 and standard deviation = 1. |
| `watr:Normalization-Decimal` | Decimal Scaling | Normalize by moving the decimal point of values. |

### Synchronization (`watr:DataProcessing-Synchronization`)

Methods for aligning data from multiple sources to common time intervals.

| Enumeration Kind | Label | Description |
|---|---|---|
| `watr:Synchronization-Resampling` | Resampling | Resample data to a different frequency or time interval. |
| `watr:Synchronization-Upsampling` | Upsampling | Increase the sampling frequency of data to a higher rate. |
| `watr:Synchronization-Downsampling` | Downsampling | Decrease the sampling frequency of data to a lower rate. |
| `watr:Synchronization-TimeAlignment` | Time Alignment | Align data points from different sources to common timestamps. |

### Filtering (`watr:DataProcessing-Filter`)

Parent class for filtering methods that remove outliers or unwanted data points. Specific filter subclasses may be defined by model authors as needed.

### Error Metrics (`watr:DataProcessing-ErrorMetrics`)

Quantities that characterize the error or uncertainty of measurements.

| Enumeration Kind | Label | Description |
|---|---|---|
| `watr:Error-AbsoluteError` | Absolute Error | Absolute difference between measured and true/reference value. |
| `watr:Error-RelativeError` | Relative Error | Error expressed as a percentage of the true/reference value. |
| `watr:Error-MeanAbsoluteError` | Mean Absolute Error (MAE) | Average of absolute errors across multiple measurements. |
| `watr:Error-MeanSquaredError` | Mean Squared Error (MSE) | Average of squared errors. |
| `watr:Error-RootMeanSquaredError` | Root Mean Squared Error (RMSE) | Square root of MSE, in the same units as measurements. |
| `watr:Error-MeanAbsolutePercentageError` | Mean Absolute Percentage Error (MAPE) | Average of absolute percentage errors. |
| `watr:Error-Bias` | Bias | Systematic deviation from the true value (a trueness measure). |

### Precision Metrics (`watr:DataProcessing-PrecisionMetrics`)

Quantities that characterize the repeatability and reproducibility of measurements.

| Enumeration Kind | Label | Description |
|---|---|---|
| `watr:Precision-RepeatabilityStdDev` | Repeatability Standard Deviation | Standard deviation under repeatability conditions (same operator, equipment, short time). |
| `watr:Precision-ReproducibilityStdDev` | Reproducibility Standard Deviation | Standard deviation under reproducibility conditions (different operators, equipment, time). |
| `watr:Precision-CoefficientOfVariation` | Coefficient of Variation | Ratio of standard deviation to mean (relative precision). |
| `watr:Precision-ConfidenceInterval` | Confidence Interval | Range within which the true value likely falls at a specified confidence level. |

### Accuracy Metrics (`watr:DataProcessing-AccuracyMetrics`)

Combined accuracy measures that encompass both precision and trueness.

| Enumeration Kind | Label | Description |
|---|---|---|
| `watr:Accuracy-TotalUncertainty` | Total Uncertainty | Combined standard uncertainty from all sources. |
| `watr:Accuracy-ExpandedUncertainty` | Expanded Uncertainty | Total uncertainty multiplied by a coverage factor. |
| `watr:Accuracy-PercentRecovery` | Percent Recovery | Ratio of measured to known value (for spike/recovery tests). |
| `watr:Accuracy-RSquared` | R-Squared | Coefficient of determination for calibration curves. |

## Example

The following Turtle fragment shows a temperature sensor property with data quality metadata. The raw property carries range and drop-rate characterization, and links to a processed (hourly mean) form of the data:

```turtle
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <urn:nawi-water-ontology#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .

# Raw temperature reading from a sensor
:t1_temp a s223:QuantifiableObservableProperty ;
    s223:hasQuantityKind qudt:Temperature ;
    s223:hasUnit unit:DEG_C ;

    # Normal operating range: max 100°C
    watr:hasVariableRange [
        a s223:QuantifiableProperty ;
        s223:hasValue 100 ;
        s223:hasAspect s223:Aspect-Maximum ;
    ] ;

    # Expected data drop rate
    watr:hasDropRate [
        a s223:QuantifiableProperty ;
        s223:hasValue 10 ;
        s223:hasUnit unit:NUM-PER-HR ;
    ] ;

    # Link to a processed (hourly mean) version of the data
    watr:hasProcessedData :t1_temp_mean ;
.

# Hourly mean of the raw temperature data
:t1_temp_mean a s223:QuantifiableProperty ;
    s223:hasAspect watr:Aggregate-Mean ;
    watr:hasTemporalResolution [
        a s223:QuantifiableProperty ;
        s223:hasUnit unit:HR ;
        s223:hasValue 1 ;
    ] ;
.
```

For a hands-on walkthrough using these annotations with SPARQL queries, see the [Data Quality Tutorial](../tutorials/data-quality-tutorial.md).
