# Sensor, Property, Quantity Kind, and Unit Model

This note describes how sensor context is represented in the DPR combined water treatment system knowledge graph in `dpr-combined-model 1.ttl`, using the WaTr ontology, ASHRAE 223, QUDT, and the local `acq:` historian-reference vocabulary.

## Core Pattern

The graph separates four concerns that are often collapsed into a single SCADA point name:

```text
physical sensor or virtual measurement source
  s223:observes
property representing the measured or commanded signal
  qudt:hasQuantityKind
kind of quantity being measured
  qudt:hasUnit
engineering unit for values
```

The property is also attached to the part of the treatment system that it characterizes:

```text
equipment, connection, or connection point
  s223:hasProperty
property
```

For the DPR model, properties commonly link to a PostgreSQL/TimescaleDB source through `acq:hasExternalReference`. That reference records the table, time column, value column, and point filter needed to retrieve the actual time series. The RDF graph does not store the time series values themselves.

## Sensors

A sensor is modeled as an instance of `s223:Sensor` or a more specific WaTr sensor class. The ontology defines water-domain sensor classes such as `watr:FlowSensor`, `watr:PressureSensor`, `watr:TemperatureSensor`, `watr:ConcentrationSensor`, `watr:pHSensor`, `watr:TurbidityMeter`, and `watr:TotalOrganicCompoundConcentrationSensor`.

In `dpr-combined-model 1.ttl`, there are seven explicit `s223:Sensor` instances. All seven are located at the connection `wbs:conn-baf-4-outlet-junction-to-mb1-valve` using `s223:hasObservationLocation`. Each one observes one water-quality property on that same connection:

| Sensor | Observed property | Quantity kind | Unit | Historian point filter |
|---|---|---|---|---|
| `wbs:conn-baf-4-outlet-junction-to-mb1-valve-dissolved-o2-sensor` | `wbs:conn-baf-4-outlet-junction-to-mb1-valve-dissolved-o2` | `qudtqk:Concentration` | `unit:MilliGM-PER-L` | `BAF-Dissolved Oxygen (mg/L)` |
| `wbs:conn-baf-4-outlet-junction-to-mb1-valve-nh4-mgL-sensor` | `wbs:conn-baf-4-outlet-junction-to-mb1-valve-nh4-mgL` | `qudtqk:Concentration` | `unit:MilliGM-PER-L` | `BAF-Ammonia (mg/L)` |
| `wbs:conn-baf-4-outlet-junction-to-mb1-valve-no2-mgL-sensor` | `wbs:conn-baf-4-outlet-junction-to-mb1-valve-no2-mgL` | `qudtqk:Concentration` | `unit:MilliGM-PER-L` | `BAF-Nitrite (mg/L)` |
| `wbs:conn-baf-4-outlet-junction-to-mb1-valve-no3-mgL-sensor` | `wbs:conn-baf-4-outlet-junction-to-mb1-valve-no3-mgL` | `qudtqk:Concentration` | `unit:MilliGM-PER-L` | `BAF-Nitrate (mg/L)` |
| `wbs:conn-baf-4-outlet-junction-to-mb1-valve-ph-sensor` | `wbs:conn-baf-4-outlet-junction-to-mb1-valve-ph` | `qudtqk:Acidity` | `unit:PH` | `BAF-pH` |
| `wbs:conn-baf-4-outlet-junction-to-mb1-valve-toc-ppm-sensor` | `wbs:conn-baf-4-outlet-junction-to-mb1-valve-toc-ppm` | `qudtqk:Concentration` | `unit:PPM` | `BAF-TOC (ppm)` |
| `wbs:conn-baf-4-outlet-junction-to-mb1-valve-turbidity-sensor` | `wbs:conn-baf-4-outlet-junction-to-mb1-valve-turbidity` | `qudtqk:Turbidity` | `unit:NTU` | `BAF-Turbidity [2] (NTU)` |

## Properties

A property is the graph node that carries the semantic meaning of a point. In this model, measured values are usually instances of `s223:QuantifiableObservableProperty`, while writable or commanded values are instances of `s223:QuantifiableActuatableProperty`.

For example, a dissolved oxygen property is represented as:

```turtle
wbs:conn-baf-4-outlet-junction-to-mb1-valve-dissolved-o2
    a s223:QuantifiableObservableProperty ;
    s223:ofMedium s223:Fluid-Water ;
    s223:ofSubstance nawi:Oxygen ;
    qudt:hasQuantityKind qudtqk:Concentration ;
    qudt:hasUnit unit:MilliGM-PER-L ;
    acq:hasExternalReference wbs:conn-baf-4-outlet-junction-to-mb1-valve-dissolved-o2_pg_ref .
```

The connection being observed also references that property:

```turtle
wbs:conn-baf-4-outlet-junction-to-mb1-valve
    a s223:Connection, s223:Pipe ;
    s223:hasProperty
        wbs:conn-baf-4-outlet-junction-to-mb1-valve-dissolved-o2,
        wbs:conn-baf-4-outlet-junction-to-mb1-valve-nh4-mgL,
        wbs:conn-baf-4-outlet-junction-to-mb1-valve-no2-mgL,
        wbs:conn-baf-4-outlet-junction-to-mb1-valve-no3-mgL,
        wbs:conn-baf-4-outlet-junction-to-mb1-valve-ph,
        wbs:conn-baf-4-outlet-junction-to-mb1-valve-toc-ppm,
        wbs:conn-baf-4-outlet-junction-to-mb1-valve-turbidity .
```

Not every property with a historian reference has an explicit sensor node in the DPR graph. Many equipment and connection properties are modeled directly as properties with `s223:hasProperty` and `acq:hasExternalReference`. In those cases, the property is still the semantic point, but the physical sensor identity has not been separately represented.

## Quantity Kinds

Quantity kinds identify what kind of measurable quantity the property value represents. They are QUDT resources linked with `qudt:hasQuantityKind`.

The DPR model uses quantity kinds including:

| Quantity kind | Typical meaning in this graph |
|---|---|
| `qudtqk:Concentration` | Chemical concentration, including dissolved oxygen, ammonia, nitrite, nitrate, ozone, TOC, and TIC. |
| `qudtqk:VolumeFlowRate` | Flow through pumps, connections, and process paths. |
| `qudtqk:Pressure` | Water pressure at filters, permeate lines, and reject lines. |
| `qudtqk:Acidity` | pH readings. |
| `qudtqk:Turbidity` | Turbidity readings. |
| `qudtqk:Volume` | Tank volume readings. |
| `qudtqk:ElectricCurrent` | Electrical current readings for equipment. |
| `qudtqk:Temperature` | Temperature readings. |
| `qudtqk:OpeningRatio` | Valve opening position. |
| `qudtqk:SpeedRatio` | Pump or generator speed command. |

For concentration properties, the quantity kind alone is not enough to identify what is being measured. The model uses `s223:ofSubstance` to distinguish substances such as `nawi:Oxygen`, `nawi:Ammonia`, `nawi:Nitrite`, `nawi:Nitrate`, and `nawi:Constituent-Organics`. It may also use `s223:ofMedium` or `s223:hasMedium` to place the property in water, air, or another medium.

## Units

Units identify how numeric values are encoded. They are QUDT unit resources linked with `qudt:hasUnit`.

The DPR graph uses these quantity-kind/unit pairings:

| Quantity kind or enumeration kind | Unit | Count |
|---|---:|---:|
| `s223:EnumerationKind-Status` | none | 47 |
| `qudtqk:Concentration` | `unit:MilliGM-PER-L` | 10 |
| `qudtqk:OpeningRatio` | none | 9 |
| `qudtqk:Concentration` | `unit:PPM` | 8 |
| `qudtqk:VolumeFlowRate` | none | 8 |
| `qudtqk:SpeedRatio` | `unit:PERCENT` | 6 |
| `qudtqk:Pressure` | `unit:PSI` | 5 |
| `qudtqk:Turbidity` | `unit:NTU` | 4 |
| `qudtqk:VolumeFlowRate` | `unit:MilliL-PER-MIN` | 4 |
| `qudtqk:Acidity` | `unit:PH` | 4 |
| `qudtqk:Volume` | `unit:GAL_US` | 2 |
| `qudtqk:VolumeFlowRate` | `unit:GAL_US-PER-MIN` | 2 |
| `qudtqk:ElectricCurrent` | `unit:A` | 2 |
| `qudtqk:Temperature` | `unit:DEG_C` | 1 |
| `qudtqk:Concentration` | `unit:PPB` | 1 |

Some quantifiable properties have a quantity kind but no unit in the current DPR file. The most common examples are `qudtqk:OpeningRatio` and some `qudtqk:VolumeFlowRate` properties. That reflects the graph as it exists today; applications that need unit conversion or numeric validation should treat those as under-specified.

Status points are modeled with `qudt:hasEnumerationKind s223:EnumerationKind-Status` rather than a numeric quantity kind/unit pair.

## Historian References

Time series lookup metadata is modeled separately from the property semantics:

```turtle
wbs:conn-baf-4-outlet-junction-to-mb1-valve-dissolved-o2
    acq:hasExternalReference
        wbs:conn-baf-4-outlet-junction-to-mb1-valve-dissolved-o2_pg_ref .

wbs:conn-baf-4-outlet-junction-to-mb1-valve-dissolved-o2_pg_ref
    a acq:PGReference ;
    acq:PG_Table "dpr" ;
    acq:PG_TimeColumn "time" ;
    acq:PG_ValueColumn "value" ;
    acq:PG_PointFilter "BAF-Dissolved Oxygen (mg/L)" .
```

The reference says where to fetch values. The property says what those values mean. The unit and quantity kind say how to interpret the numeric values once fetched.

## Data Quality and Processed Data

The WaTr ontology also allows measurement metadata to be attached to quantifiable properties or, in selected cases, directly to sensors. These metadata relations include:

| Relation | Meaning |
|---|---|
| `watr:hasTemporalResolution` | Minimum interval between samples. |
| `watr:hasNumericResolution` | Smallest distinguishable numeric difference. |
| `watr:hasTemporalRange` | Time span covered by recorded data. |
| `watr:hasNumericRange` | Observed or configured numeric span. |
| `watr:hasVariableRange` | Expected operating range of the variable. |
| `watr:hasMeasurementRange` | Physical measurement range of the sensor or measurement system. |
| `watr:hasAccuracy` | Expected deviation from the true value. |
| `watr:hasPrecision` | Repeatability or reproducibility. |
| `watr:hasBias` | Systematic offset or drift. |
| `watr:hasResponseTime` | Response time to a step change. |
| `watr:hasCalibrationCurve` | Calibration relationship from raw output to engineering values. |
| `watr:hasDropRate` | Lost samples per time range. |
| `watr:hasProcessedData` | Link from raw property to a processed property. |
| `watr:hasAggregation` | Aggregation semantics such as maximum, minimum, mean, total, or percentile. |

These relations are defined in the ontology, but they are not the primary pattern used in `dpr-combined-model 1.ttl`. That DPR graph mostly captures point semantics, location, units, quantity kinds, substances, status enumeration kinds, and historian references.

## Inventory of the DPR Graph

Parsing `dpr-combined-model 1.ttl` gives the following point-model inventory:

| Item | Count |
|---|---:|
| RDF triples | 5,898 |
| Explicit `s223:Sensor` instances | 7 |
| `s223:QuantifiableObservableProperty` instances | 106 |
| `s223:QuantifiableActuatableProperty` instances | 7 |
| `s223:observes` links | 7 |
| `s223:hasObservationLocation` links from sensors | 7 |
| `s223:hasProperty` links from modeled assets | 113 |
| Properties with `qudt:hasQuantityKind` | 66 |
| Properties with `qudt:hasUnit` | 49 |
| Properties with `qudt:hasEnumerationKind` | 47 |
| Properties with `acq:hasExternalReference` | 112 |

Every quantifiable observable or actuatable property in the parsed DPR graph has either a QUDT quantity kind or an enumeration kind. Unit coverage is partial, so consumers should not assume every quantifiable property has `qudt:hasUnit`.

## Query Patterns

To find explicit sensors and their observed quantity semantics:

```sparql
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX qudt: <http://qudt.org/schema/qudt/>

SELECT ?sensor ?location ?property ?quantityKind ?unit WHERE {
  ?sensor a s223:Sensor ;
          s223:hasObservationLocation ?location ;
          s223:observes ?property .
  OPTIONAL { ?property qudt:hasQuantityKind ?quantityKind . }
  OPTIONAL { ?property qudt:hasUnit ?unit . }
}
```

To find all semantic points on modeled assets, including properties without explicit sensor nodes:

```sparql
PREFIX s223: <http://data.ashrae.org/standard223#>
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX acq: <urn:acquirium#>

SELECT ?asset ?property ?quantityKind ?unit ?enumerationKind ?reference WHERE {
  ?asset s223:hasProperty ?property .
  OPTIONAL { ?property qudt:hasQuantityKind ?quantityKind . }
  OPTIONAL { ?property qudt:hasUnit ?unit . }
  OPTIONAL { ?property qudt:hasEnumerationKind ?enumerationKind . }
  OPTIONAL { ?property acq:hasExternalReference ?reference . }
}
```

## Practical Interpretation

Use `s223:Sensor` when the identity or location of a measurement device matters. Use `s223:hasProperty` to discover what qualities are modeled on a piece of equipment, connection, or connection point. Use `qudt:hasQuantityKind` to determine the kind of value, `qudt:hasUnit` to interpret numeric scale, `qudt:hasEnumerationKind` for status-like values, and `acq:hasExternalReference` to retrieve the corresponding time series.

