---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Exploring Data Quality Metadata

WaTr describes measurement limits, sampling intervals, processing methods, and
links to processed data. This tutorial loads temperature metadata, uses its
configured limit to find an outlier, and compares raw and processed samples.

Run these cells in order. The sample rows use a local application vocabulary;
production systems usually keep time-series values in a historian and link
properties to that storage using `s223:hasExternalReference`.

## Load the metadata

```{code-cell} python
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, XSD

EX = Namespace("urn:example/data-quality#")
g = Graph()
model = """
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
"""
g.parse(data=model, format="turtle")
print(f"Loaded {len(g)} metadata statements.")
```

The temperature limit uses `s223:Aspect-HighLimit`. Quantity kinds and units use
`qudt:hasQuantityKind` and `qudt:hasUnit`. The hourly mean records both its
processing method and aggregation semantics; the one-hour and one-minute
properties describe output intervals. These annotations do not perform the
aggregation or interpolation.

## Add illustrative samples

The samples below represent data already returned by a historian or processing
pipeline. The local `:Reading`, `:forProperty`, `:value`, and `:timestamp` terms
identify rows for this demonstration.

```{code-cell} python
samples = [
    ("raw1", EX.t1_temp, 72.5, "2024-01-15T10:00:00"),
    ("raw2", EX.t1_temp, 73.2, "2024-01-15T10:05:00"),
    ("raw3", EX.t1_temp, 74.1, "2024-01-15T10:10:00"),
    ("raw4", EX.t1_temp, 150.0, "2024-01-15T10:15:00"),
    ("raw5", EX.t1_temp, 73.8, "2024-01-15T10:20:00"),
    ("mean1", EX.hourlyMean, 73.4, "2024-01-15T10:00:00"),
    ("interpolated1", EX.interpolated, 72.64, "2024-01-15T10:01:00"),
    ("interpolated2", EX.interpolated, 72.78, "2024-01-15T10:02:00"),
]
for name, property_node, value, timestamp in samples:
    reading = EX[name]
    g.add((reading, RDF.type, EX.Reading))
    g.add((reading, EX.forProperty, property_node))
    g.add((reading, EX.value, Literal(value)))
    g.add((reading, EX.timestamp, Literal(timestamp, datatype=XSD.dateTime)))
```

## Query the configured operating limit

The query reads the limit from the metadata. It returns the 150°C sample because
it exceeds the configured upper limit of 100°C.

```{code-cell} python
outliers = list(g.query("""
PREFIX : <urn:example/data-quality#>
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX watr: <https://watermetadata.org/ontology/watr#>
SELECT ?reading ?value ?timestamp ?upper WHERE {
  ?property watr:hasVariableRange ?limit .
  ?limit s223:hasAspect s223:Aspect-HighLimit; s223:hasValue ?upper .
  ?reading :forProperty ?property; :value ?value; :timestamp ?timestamp .
  FILTER (?value > ?upper)
}
ORDER BY ?timestamp
"""))
assert len(outliers) == 1 and outliers[0].reading == EX.raw4
for row in outliers:
    print(f"{row.timestamp}: {row.value}°C exceeds {row.upper}°C")
```

This query compares samples with an operating limit. SHACL validation of the
metadata graph is a separate check, and WaTr does not infer permit compliance
from these annotations.

## Compare raw and processed samples

```{code-cell} python
comparison = list(g.query("""
PREFIX : <urn:example/data-quality#>
SELECT ?kind ?value ?timestamp WHERE {
  VALUES (?property ?kind) {
    (:t1_temp "Raw")
    (:hourlyMean "Hourly mean")
    (:interpolated "Interpolated")
  }
  ?reading :forProperty ?property; :value ?value; :timestamp ?timestamp .
}
ORDER BY ?timestamp ?kind
"""))
assert len(comparison) == len(samples)
for row in comparison:
    print(f"{row.timestamp} | {row.kind}: {row.value}°C")
```

See [Data Quality Metadata](../explanation/data_quality.md) for the relations and
processing vocabulary, and [Creating a Model](creating-models.md) for SHACL
validation and inference.
