---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Data Quality Model Exploration

```{note}
The purpose of this tutorial is to explore a wastewater treatment system model with data quality annotations by learning the following:
1. Parsing (loading) an existing model with data quality metadata
2. Querying data quality properties in the model
3. Understanding temporal resolution and data processing aspects
```

For this tutorial, we'll use a wastewater treatment system model that includes temperature sensors with data quality annotations using the WATR ontology. This demonstrates how to capture metadata about sensor data quality, including variable ranges, drop rates, temporal resolution, and data processing methods.

## Model Parsing

First, we'll create a new empty graph then parse (load) an existing graph into it using the Python RDFLib library. We'll also load the necessary ontology namespaces to make querying easier down the line.

```{code-cell}
from rdflib import Graph, Namespace

# Create a Graph
g = Graph()

# Define namespaces
S223 = Namespace("http://data.ashrae.org/standard223#")
WATR = Namespace("http://data.ashrae.org/watr#")
QUDT = Namespace("http://qudt.org/schema/qudt/")
UNIT = Namespace("http://qudt.org/vocab/unit/")

# Bind namespaces for cleaner output
g.bind("s223", S223)
g.bind("watr", WATR)
g.bind("qudt", QUDT)
g.bind("unit", UNIT)

# Parse in an RDF file (replace with actual model file path)
# g.parse("wastewater-treatment-model.ttl", format="ttl")

# For this tutorial, we'll create a sample model inline
sample_model = """
@prefix : <http://example.org/wastewater#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <http://data.ashrae.org/watr#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

# This node represents the reading from a temperature sensor
:t1_temp a s223:QuantifiableObservableProperty ;
    s223:hasQuantityKind qudt:Temperature ;
    s223:hasUnit unit:DEG_C ;

    # This temperature sensor has various properties defining its expected range during operation
    watr:hasVariableRange :t1_temp_range ;
    # Its drop rate, meaning how often it is expected to be missing data
    watr:hasDropRate :t1_temp_droprate ;
    # and other processed quantities based on the data stream
    watr:hasProcessedData :t1_temp_mean, :t1_temp_interpolated ;
.

# it's expected to never go above 100C
:t1_temp_range a s223:QuantifiableProperty ;
    s223:hasValue 100 ;
    s223:hasAspect s223:Aspect-Maximum ;
.

# It has a mean quantified value 
:t1_temp_mean a s223:QuantifiableProperty ;
    s223:hasAspect watr:Aggregate-Mean ;

    # the temporal resolution of the mean is 1 hour, meaning it represents the average of 1 hour of data
    watr:hasTemporalResolution [
        a s223:QuantifiableProperty ;
        s223:hasUnit unit:HR ;
        s223:hasValue 1 ;
    ] ;
.

# the temperature measurement also has an expected data drop rate of 10 logs per hour 
:t1_temp_droprate a s223:QuantifiableProperty ;
    s223:hasValue 10 ;
    s223:hasUnit unit:NUM-PER-HR ;
.

# Because there is data loss, we also generate an interpolated version of the data
:t1_temp_interpolated a s223:QuantifiableProperty ;
    s223:hasAspect watr:Interpolation-Linear ;
    # This external reference may link this property to a database where the timeseries data is stored
    s223:hasExternalReference :t1_temp_1min ;  
    # This interpolated data is calculated every minute
    watr:hasTemporalResolution [
        a s223:QuantifiableProperty ;
        s223:hasUnit unit:MIN ;
        s223:hasValue 1 ;
    ] ;
.
"""

g.parse(data=sample_model, format="turtle")
```


Finally, let's look at our model to make sure it loaded correctly.


```{code-cell}
# Print out the entire Graph in the RDF Turtle format
print(g.serialize(format="turtle"))
```

## Understanding Data Quality Aspects

Theis tutorial uses a few of the data quality and processing elements of the WATR ontology:

1. **watr:hasVariableRange** - Defines the expected range of values for a sensor
2. **watr:hasProcessedData** - Links to processed versions of the raw data
3. **watr:hasTemporalResolution** - Specifies the time interval for aggregated or interpolated data
4. **watr:hasDropRate** - Indicates the rate at which data points are missing
5. **s223:hasAspect** - Describes additional informatino about properties, in this case, the type of processing (e.g., Mean aggregation, Linear interpolation)

These annotations enable better understanding of data quality, processing methods, and potential issues in wastewater treatment system monitoring.

## Working with Sensor Data

Now let's explore how to use these data quality properties in practice. We'll add some dummy sensor readings and demonstrate how to validate data against expected ranges and compare different data processing methods.

This processing would most often be done in python, however, we will accomplish simple examples of filtering and querying using SPARQL. 


```{note}
In production systems, sensor data is typically stored in time-series/relational databases and linked to the ontology model via external references. For this tutorial, we'll include sample data directly in the graph for demonstration purposes.
```

### Adding Sample Sensor Data

Let's extend our model with actual temperature readings:

```{code-cell}
# Add sample sensor data to the graph
sample_data = """
@prefix : <http://example.org/wastewater#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# Raw sensor readings (5-minute intervals)
:reading_1 a s223:ObservationEvent ;
    s223:observes :t1_temp ;
    s223:hasValue 72.5 ;
    s223:hasTimestamp "2024-01-15T10:00:00"^^xsd:dateTime ;
.

:reading_2 a s223:ObservationEvent ;
    s223:observes :t1_temp ;
    s223:hasValue 73.2 ;
    s223:hasTimestamp "2024-01-15T10:05:00"^^xsd:dateTime ;
.

:reading_3 a s223:ObservationEvent ;
    s223:observes :t1_temp ;
    s223:hasValue 74.1 ;
    s223:hasTimestamp "2024-01-15T10:10:00"^^xsd:dateTime ;
.

:reading_4 a s223:ObservationEvent ;
    s223:observes :t1_temp ;
    s223:hasValue 150.0 ;  # Outlier - outside expected range!
    s223:hasTimestamp "2024-01-15T10:15:00"^^xsd:dateTime ;
.

:reading_5 a s223:ObservationEvent ;
    s223:observes :t1_temp ;
    s223:hasValue 73.8 ;
    s223:hasTimestamp "2024-01-15T10:20:00"^^xsd:dateTime ;
.

# Hourly mean (aggregated from raw data)
:hourly_mean_1 a s223:ObservationEvent ;
    s223:observes :t1_temp_mean ;
    s223:hasValue 73.4 ;  # Mean of valid readings
    s223:hasTimestamp "2024-01-15T10:00:00"^^xsd:dateTime ;
.

# Resampled data (1-minute intervals via linear interpolation)
:resampled_1 a s223:ObservationEvent ;
    s223:observes :t1_temp_interpolated ;
    s223:hasValue 72.64 ;
    s223:hasTimestamp "2024-01-15T10:01:00"^^xsd:dateTime ;
.

:resampled_2 a s223:ObservationEvent ;
    s223:observes :t1_temp_interpolated ;
    s223:hasValue 72.78 ;
    s223:hasTimestamp "2024-01-15T10:02:00"^^xsd:dateTime ;
.
"""

g.parse(data=sample_data, format="turtle")
print(f"Graph now has {len(g)} statements after adding sensor data.")
```

### Validating Data Against Expected Ranges

Let's query for readings that fall outside the expected variable range:

```{code-cell}
# Query to find outliers based on variable range
q_outliers = """
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX watr: <http://data.ashrae.org/watr#>

SELECT ?reading ?value ?timestamp ?minRange ?maxRange WHERE {
  # Get the sensor and its range
  ?sensor watr:hasVariableRange ?range .
  ?range s223:hasValue ?rangeValue .
  
  # Get readings for this sensor
  ?reading s223:observes ?sensor ;
           s223:hasValue ?value ;
           s223:hasTimestamp ?timestamp .
  
  # Bind range value
  BIND(?rangeValue AS ?maxRange)
  
  # Filter for values outside the range
  FILTER(?value > 100)
}
ORDER BY ?timestamp
"""

print("Outlier Detection - Readings Outside Expected Range:")
print("=" * 60)
for r in g.query(q_outliers):
    print(f"Reading: {r.reading}")
    print(f"Value: {r.value}°C (Expected < 100°C)")
    print(f"Timestamp: {r.timestamp}")
    print()
```

### Comparing Raw, Aggregated, and Resampled Data

Now let's compare the different data representations:

```{code-cell}
# Query to get all three types of data
q_compare = """
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX watr: <http://data.ashrae.org/watr#>

SELECT ?dataType ?value ?timestamp WHERE {
  {
    # Raw sensor data
    ?reading s223:observes :t1_temp ;
             s223:hasValue ?value ;
             s223:hasTimestamp ?timestamp .
    BIND("Raw" AS ?dataType)
  }
  UNION
  {
    # Hourly mean
    ?reading s223:observes :t1_temp_mean ;
             s223:hasValue ?value ;
             s223:hasTimestamp ?timestamp .
    BIND("Hourly Mean" AS ?dataType)
  }
  UNION
  {
    # Resampled (interpolated)
    ?reading s223:observes :t1_temp_interpolated ;
             s223:hasValue ?value ;
             s223:hasTimestamp ?timestamp .
    BIND("Resampled (1-min)" AS ?dataType)
  }
}
ORDER BY ?timestamp ?dataType
"""

print("Comparison of Data Processing Methods:")
print("=" * 60)
for r in g.query(q_compare):
    print(f"{r.timestamp} | {r.dataType:20s} | {r.value}°C")
```

## Summary

In this tutorial, we:
- Loaded a wastewater treatment system model with data quality annotations
- Queried for observable properties (measured data) and their metadata
- Extracted variable ranges, processed data configurations, and drop rates
- Learned about the WATR ontology's data quality properties
- Added sample sensor data and validated it against expected ranges
- Compared raw, aggregated, and resampled data representations

This approach can be extended to more complex wastewater treatment systems with multiple sensors, actuators, and data processing pipelines. In production wastewater treatment systems, these data quality annotations enable:
- Automated anomaly detection
- Data validation pipelines
- Informed selection of appropriate data resolution for analysis
- Tracking of data processing provenance
