# Data Quality Metadata

A sensor reading is only as useful as what is known about it: how precise the
sensor is, what range it can measure, how often it reports, and whether the value
you are looking at is the raw reading or an hourly average of it. WaTr records this
with `watr:` relations on `s223:QuantifiableProperty` (and, for some, directly on
`s223:Sensor`). The metadata serves two purposes that work together. It
characterizes the raw measurement, and it links a raw property to processed forms
of itself and says how each was produced.

## Characterizing a measurement

### Requirements

Each characterization relation points from a `QuantifiableProperty` to another
`QuantifiableProperty` whose value and unit carry the metadata quantity.

- *Measurement:* `watr:hasTemporalResolution` is the minimum interval between
  successive data points, `watr:hasNumericResolution` the smallest distinguishable
  difference between values, `watr:hasResponseTime` the time to respond to a step
  change, and `watr:hasCalibrationCurve` the relationship between raw output and
  calibrated engineering units.
- *Range:* `watr:hasTemporalRange` is the start and end of the recorded data,
  `watr:hasNumericRange` the span between minimum and maximum measured values,
  `watr:hasVariableRange` the expected maximum or minimum during normal operation,
  and `watr:hasMeasurementRange` the maximum or minimum that can physically be
  measured. The last also applies directly to an `s223:Sensor`.
- *Error and uncertainty:* `watr:hasAccuracy` is the maximum expected deviation
  from the true value, `watr:hasPrecision` the repeatability or reproducibility
  under identical conditions, and `watr:hasBias` a systematic offset or drift.
- *Availability:* `watr:hasDropRate` is the number of data points lost per unit
  time to latency or other causes.

### Rationale

Each quantity is itself a property, with its own value, quantity kind and unit,
rather than a bare number on the reading. A sensor's drop rate or upper limit is
then queried and unit-converted like any other measurement. The relations stay
separate because they answer different questions: the measurement range says what
the hardware can see, the variable range says what the process normally does, and
accuracy and precision say how far to trust either.

### Validation

A shape on `s223:QuantifiableProperty` in `watr.ttl` requires the value of each of
these relations to be a `QuantifiableProperty`; anything else is a violation.
Nothing checks that units agree or that the numbers are consistent with each
other. Those are modeling conventions.

## Processed data and processing methods

### Definitions

`watr:hasProcessedData` links a raw property to a `QuantifiableProperty` that is a
processed, filtered or transformed form of it. The processed property says how it
was made with an `s223:hasAspect` triple whose object is a
`watr:EnumerationKind-DataProcessing` value. These values form families beneath
that class, which is itself a subclass of `s223:EnumerationKind`:

- **Aggregation** (`watr:DataProcessing-Aggregate`) combines many points into one:
  `Aggregate-Mean`, `-Median`, `-Max`, `-Min`, `-Sum`, `-Count`, `-StdDev`,
  `-Variance`, `-Range` (maximum minus minimum) and `-Mode`.
- **Interpolation** (`DataProcessing-Interpolation`) estimates values between or in
  place of missing points: `Interpolation-Linear`, `-Spline` (cubic), `-Polynomial`,
  `-NearestNeighbor`, `-ForwardFill` (carry the last valid value forward) and
  `-BackwardFill`.
- **Normalization** (`DataProcessing-Normalization`) scales data to a standard
  range or distribution: `Normalization-MinMax` (to [0, 1]), `-ZScore` (mean 0,
  standard deviation 1) and `-Decimal` (decimal scaling).
- **Synchronization** (`DataProcessing-Synchronization`) aligns data from several
  sources to common time intervals: `Synchronization-Resampling`, `-Upsampling`,
  `-Downsampling` and `-TimeAlignment`.
- **Filtering** (`DataProcessing-Filter`) is a parent for methods that remove
  outliers or unwanted points. It has no members; model authors define the specific
  filters they need beneath it.
- **Error metrics** (`DataProcessing-ErrorMetrics`) characterize the error of
  measurements: `Error-AbsoluteError`, `-RelativeError`, `-MeanAbsoluteError`,
  `-MeanSquaredError`, `-RootMeanSquaredError`, `-MeanAbsolutePercentageError` and
  `-Bias` (a trueness measure).
- **Precision metrics** (`DataProcessing-PrecisionMetrics`) characterize
  repeatability and reproducibility: `Precision-RepeatabilityStdDev` (same operator,
  equipment and short time), `-ReproducibilityStdDev` (different operators,
  equipment and time), `-CoefficientOfVariation` and `-ConfidenceInterval`.
- **Accuracy metrics** (`DataProcessing-AccuracyMetrics`) combine precision and
  trueness: `Accuracy-TotalUncertainty`, `-ExpandedUncertainty` (total uncertainty
  times a coverage factor), `-PercentRecovery` (for spike and recovery tests) and
  `-RSquared` (for calibration curves).

### Rationale

A raw reading and its hourly mean are different quantities with different
uncertainty, and a model needs to say which one a value is. Giving the processed
form its own property keeps the raw stream intact and lets each processed stream
carry its own resolution, range and quality metadata. The processing method is
an enumeration value, not free text, so queries can find every mean or every
interpolated series.

`s223:hasAspect` records the method, such as `Aggregate-Mean`. `watr:hasAggregation`
separately records the aggregation semantics, such as `Aggregation-Mean`, which is
what a downstream reader uses to interpret the value.

### Validation

`watr:hasProcessedData` takes a `QuantifiableProperty`, and a `watr:hasAggregation`
value must be a `watr:EnumerationKind-Aggregation`; anything else is a violation.
Nothing checks that the aspect agrees with the aggregation, or that a processed
property was actually derived from its raw one.

## Example

The following Turtle fragment shows a temperature sensor property with data quality metadata. The raw property carries range and drop-rate characterization, and links to a processed (hourly mean) form of the data:

```turtle
@prefix : <urn:example/data-quality#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:t1_temp a s223:QuantifiableObservableProperty ;
    rdfs:label "Raw temperature" ;
    qudt:hasQuantityKind quantitykind:Temperature ;
    qudt:hasUnit unit:DEG_C ;
    watr:hasVariableRange :upperLimit ;
    watr:hasDropRate :dropRate ;
    watr:hasProcessedData :hourlyMean, :interpolated .
:upperLimit a s223:QuantifiableProperty ;
    rdfs:label "Normal operating upper limit" ;
    qudt:hasQuantityKind quantitykind:Temperature ;
    qudt:hasUnit unit:DEG_C ;
    s223:hasAspect s223:Aspect-HighLimit ;
    s223:hasValue 100 .
:dropRate a s223:QuantifiableProperty ;
    rdfs:label "Expected missing samples per hour" ;
    qudt:hasQuantityKind quantitykind:Frequency ;
    qudt:hasUnit unit:NUM-PER-HR ;
    s223:hasValue 10 .
:hourlyMean a s223:QuantifiableProperty ;
    rdfs:label "Hourly mean temperature" ;
    qudt:hasQuantityKind quantitykind:Temperature ;
    qudt:hasUnit unit:DEG_C ;
    s223:hasAspect watr:Aggregate-Mean ;
    watr:hasAggregation watr:Aggregation-Mean ;
    watr:hasTemporalResolution :oneHour .
:oneHour a s223:QuantifiableProperty ;
    rdfs:label "Hourly output interval" ;
    qudt:hasQuantityKind quantitykind:Time ;
    qudt:hasUnit unit:HR ;
    s223:hasValue 1 .
:interpolated a s223:QuantifiableProperty ;
    rdfs:label "Interpolated temperature" ;
    qudt:hasQuantityKind quantitykind:Temperature ;
    qudt:hasUnit unit:DEG_C ;
    s223:hasAspect watr:Interpolation-Linear ;
    watr:hasTemporalResolution :oneMinute .
:oneMinute a s223:QuantifiableProperty ;
    rdfs:label "One-minute output interval" ;
    qudt:hasQuantityKind quantitykind:Time ;
    qudt:hasUnit unit:MIN ;
    s223:hasValue 1 .
```

The complete fragment is also available as
{download}`data-quality-temperature.ttl <../../examples/data-quality-temperature.ttl>`.

For a hands-on walkthrough using these annotations with SPARQL queries, see the [Data Quality Tutorial](../tutorials/data-quality-tutorial.md).
