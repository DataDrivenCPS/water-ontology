# Model Relations and Rules

## Class

**Description:** This is a modeling construct. All classes defined in the watr ontology are instances of `watr:Class`.

**Superclasses:** `rdfs:Class`

## Class defaults

**Description:** Materializes watr:hasProcess and watr:hasTreatmentObjective onto an instance from the qualified requirements of its class and that class's ancestors.

## A constituent-removal objective names its constituent

**Description:** Warns when a watr:TreatmentObjective-ConstituentRemoval neither states watr:targetsConstituent nor inherits one.

## Constituent target values are constituents

**Description:** Every object of watr:targetsConstituent must be an s223:Medium-Constituent.

## Defined class

**Description:** A class that exists: it carries at least one rdf:type.

## Process and role constraints reference defined classes

**Description:** Every class named by a watr:hasProcess, watr:hasTreatmentObjective or s223:hasRole constraint must be defined.

## Process bearers are equipment or systems

**Description:** watr:hasProcess and watr:hasTreatmentObjective may only be asserted on an s223:Equipment or an s223:System.

## Objective from process

**Description:** Materializes watr:hasTreatmentObjective onto anything that performs a process which declares watr:achievesTreatmentObjective.

## Process values are water processes

**Description:** Every object of watr:hasProcess must be a watr:Process.

## System process coverage

**Description:** Warns when a system claims a compound process but neither it, a nested member, nor equipment contained within a member performs a constituent process.

## A treatment objective is reached by a process

**Description:** Equipment declaring watr:hasTreatmentObjective must also declare the watr:hasProcess by which it reaches it.

## Treatment objective values are treatment objectives

**Description:** Every object of watr:hasTreatmentObjective must be a watr:TreatmentObjective.

## Unit Process

**Description:** A unit process is a specific type of water treatment process that can be applied to water.

**Superclasses:** `s223:Equipment`

## achieves treatment objective

**Description:** Relates a process type to the treatment objective it achieves wherever it is performed. Used to derive an equipment's treatment objective from its process.

## has accuracy

**Description:** The `hasAccuracy` relation is used to link to a numerical `Property` whose value indicates the maximum expected deviation between the measured value and the true value in engineering units.

## has aggregation

**Description:** The `hasAggregation` relation associates a property with water-specific aggregation semantics such as total, mean, maximum, or minimum.

## has bias

**Description:** The `hasBias` relation is used to link to a numerical `Property` whose value indicates the systematic offset or drift in measurements relative to the true value.

## has calibration curve

**Description:** The `hasCalibrationCurve` relation is used to link to a `Property` that describes the mathematical relationship or lookup table between raw sensor output and calibrated engineering units.

## has drop rate

**Description:** The `hasDropRate` relation is used to link to a `Property` describes the amount of data points lost within a range of time due to latencies or other factors.

## has measurement range

**Description:** The `hasMeasurementRange` relation is used to link to a numerical `Property` whose value indicates the expected range of variation that can physically be measured, e.g. by a sensor.

## has numeric range

**Description:** The `hasNumericRange` relation is used to link to a numerical `Property` whose value indicates the span between the minimum and maximum measurable values in engineering units.

## has numeric resolution

**Description:** The `hasNumericResolution` relation is used to link to a numerical `Property` whose value indicates the smallest distinguishable difference between two measured values in engineering units.

## has precision

**Description:** The `hasPrecision` relation is used to link to a numerical `Property` whose value indicates the repeatability or reproducibility of measurements under identical conditions.

## has process

**Description:** Associates a water treatment process with the entity that performs it: a piece of Equipment, or an s223:System where the process is performed by the collection and by no individual member (backwashing, or a treatment train such as an MLE). See watr:ProcessBearerShape and watr:ProcessValueShape.

## has processed data

**Description:** The `hasProcessedData` relation is used to link to a `Property` that describes any data processing, filtering, or transformation applied to the raw measurement values.

## has response time

**Description:** The `hasResponseTime` relation is used to link to a numerical `Property` whose value indicates the time required for the sensor or measurement system to respond to a step change in the measured variable.

## has temporal range

**Description:** The `hasTemporalRange` relation is used to link to a numerical `Property` whose value indicates the start and end times for which data has been recorded.

## has temporal resolution

**Description:** The `hasTemporalResolution` relation is used to link to a numerical `Property` whose value indicates the minimum time interval between successive measurements or data points.

## has treatment objective

**Description:** Associates a piece of equipment or a system with the treatment objective it is intended to achieve. What it does to achieve that is watr:hasProcess.

## has variable range

**Description:** The `hasVariableRange` relation is used to link to a numerical `Property` whose value indicates the expected range of variation for the measured variable under normal operating conditions.

## includes process

**Description:** Relates a compound process to a constituent process that a system performing it is expected to carry out, typically through a member. Used to check coverage, not validity.

## targets constituent

**Description:** Relates a treatment objective to the constituent it removes, converts or controls. An explicit target takes precedence over ancestor targets; without one, use the nearest declaring ancestor on each inheritance branch. See the constituent query in docs/guides/querying_treatment_function.md.
