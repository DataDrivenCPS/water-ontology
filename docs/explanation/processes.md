# Modeling Composition, Topology, and Treatment Function

A WaTr model describes what a unit is made of (composition), how it is piped to
everything else (topology), what flows through it (media), and what it does
(treatment function). This page works through all four with one ultraviolet
disinfection unit:

![](Topology.png)

Every box in the figure is a node in the graph, and every arrow a relation.
The complete model is
{download}`uv-disinfection-system.ttl <../../examples/uv-disinfection-system.ttl>`,
which validates with the other examples.

## Composition

### Modeling

`s223:contains` relates equipment to the equipment inside it. The UV unit
contains a plug flow reactor and two lamps:

```ttl
@prefix : <urn:example/uv-disinfection#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .

:uvSystem a watr:UltravioletLightUnit ;
    s223:contains :reactor, :lamp1, :lamp2 .

:reactor a watr:PlugFlowReactor .

:lamp1 a s223:Equipment ;
    s223:hasProperty :lamp1Wavelength .
:lamp1Wavelength a s223:QuantifiableProperty ;
    qudt:hasQuantityKind quantitykind:Wavelength ;
    qudt:hasUnit unit:NanoM ;
    s223:hasValue 250 .
```

### Rationale

WaTr has no lamp class, so each lamp is generic `s223:Equipment` identified by its
emitted wavelength. The wavelength is a rated characteristic with a fixed value,
so it is a `QuantifiableProperty`. A quantity a sensor reads, such as the lamp
brightness in the figure, would be a `QuantifiableObservableProperty`.

### Validation

S223 checks containment, not WaTr. It warns when equipment contains equipment from
its own class branch, because a query for that class would count both. A
`watr:UnitProcess` containing a `watr:PlugFlowReactor`, itself a `UnitProcess`,
draws that warning. That is why the outer unit is an `UltravioletLightUnit`, which
is not an ancestor of a plug flow reactor. S223 also warns when an
`ObservableProperty` is observed by no sensor, so a rated value typed as observable
draws a warning too. Contained equipment may not connect directly to equipment
outside its container, which is a violation. Its ports map to the container's
instead, as below.

## Topology

### Modeling

WaTr takes its topology from [ASHRAE 223](https://docs.open223.info/explanation/223_overview.html).
Connectable things, which are equipment, junctions and domain spaces, carry
connection points. An `InletConnectionPoint`, `OutletConnectionPoint` or
`BidirectionalConnectionPoint` gives the direction of flow, and `s223:hasMedium`
what flows. A `Connection`, such as a pipe or a channel, joins two connection
points and conveys a medium between them. `s223:cnx` links the parts; S223
inference derives the more specific relations from it.

The UV unit has an inlet and an outlet. The reactor inside has its own, and
`s223:mapsTo` maps each of them to the unit's matching port:

```ttl
:uvSystem s223:cnx :systemInlet, :systemOutlet .
:systemInlet a s223:InletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water .
:systemOutlet a s223:OutletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water .

:reactor s223:cnx :reactorInlet, :reactorOutlet .
:reactorInlet a s223:InletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water ;
    s223:mapsTo :systemInlet .
:reactorOutlet a s223:OutletConnectionPoint ;
    s223:hasMedium s223:Fluid-Water ;
    s223:mapsTo :systemOutlet .
```

### Rationale

Mapping keeps both views of the unit. Upstream piping connects to the UV unit as
one piece of equipment, and a model that looks inside still sees that the water
passes through the reactor.

### Validation

S223 reports an `sh:Info` for a connection point with no connection, unless it is
mapped or marked as a boundary or optional point. The UV unit's own inlet and outlet
draw this in the example file, since nothing upstream is modeled; the example
tests allow Info findings. Connection points joined through a connection must
carry compatible media (see below), or S223 reports a violation.

WaTr adds port requirements per equipment class. `watr:PlugFlowReactor` and every
`watr:Reactor` need a fluid inlet and a fluid outlet, which the reactor's two
mapped ports satisfy. See [equipment classes](treatment_model_summary.md#tanks-reactors-and-separation-tanks)
for the rest.

## Media and constituents

### Definitions

A `ConnectionPoint` or `Connection` carries a *medium*, the substance flowing
through it (water, a chemical, air). S223 decides whether two media are
*compatible* by comparing the constituents they are `s223:composedOf`. Two pure
media are compatible only if one is a subclass of the other. Two mixture media are
compatible when they share at least one constituent, either the same one or one
that is a subclass of the other.

WaTr defines several aqueous media as subclasses of `s223:Fluid-Water`:
`Water-Seawater`, `Water-Brackish`, `Water-Freshwater` and `Water-Brine`. Each
declares `s223:composedOf` its constituents, sharing `s223:Constituent-H2O` with
`s223:Fluid-Water` itself:

```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix s223: <http://data.ashrae.org/standard223#> .
@prefix watr: <https://watermetadata.org/ontology/watr#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

watr:Water-Seawater
    rdfs:subClassOf s223:Fluid-Water ;
    s223:composedOf [
        a s223:QuantifiableProperty ;
        s223:ofConstituent s223:Constituent-H2O ;
        qudt:hasQuantityKind quantitykind:MassFraction ;
        qudt:hasUnit unit:PERCENT ;
    ] ;
    s223:composedOf [
        a s223:QuantifiableProperty ;
        s223:ofConstituent watr:Salt-NaCl ;
        qudt:hasQuantityKind quantitykind:MassFraction ;
        qudt:hasUnit unit:PERCENT ;
    ] .
```

`Water-Freshwater` declares only `Constituent-H2O`; the saline media also declare
`watr:Salt-NaCl`.

`watr:Fluid-Sludge` is a semi-solid slurry, a subclass of `s223:Mix-Fluid` composed
of `s223:Constituent-H2O`, `watr:Constituent-OrganicSolids` and
`watr:Constituent-InorganicSolids`. It is not a `Fluid-Water`.

A flowing medium differs from a filter medium. Water, brine or sludge flows
through the equipment; sand, carbon, resin or a membrane is the material that
does the separating, and is never the `hasMedium` of a pipe.

WaTr follows S223's self-enumerated medium pattern: a reusable medium designation
is both a class and an instance of itself, and is used directly as the value of
`s223:hasMedium`. For a reusable salinity such as 15-percent brine, mint a more
specific medium class, type it as itself, subclass it from `Water-Brine` and assert
its composition directly. See {download}`brine-composition.ttl <../../examples/brine-composition.ttl>`.

Composition is not inherited through `rdfs:subClassOf`. A specialized medium does
not acquire the `s223:composedOf` statements of `Water-Brine`; it repeats every
constituent it needs. The superclass organizes the vocabulary and takes part in
class compatibility, but it is not a template.

### Rationale

Because seawater, brackish water, brine and freshwater all declare
`s223:Constituent-H2O`, S223 treats them as mutually compatible. One piece of
equipment can accept a seawater feed and emit freshwater and brine streams without
the validator flagging the media. See
{download}`ro-mixture-test.ttl <../../examples/ro-mixture-test.ttl>`.

Sludge shares `Constituent-H2O`, so the same rules accept water in and sludge out
of a clarifier, sludge in and supernatant out of a thickener, and a sludge pipe
joined to either kind of connection point. See
{download}`clarifier-sludge-compatibility.ttl <../../examples/clarifier-sludge-compatibility.ttl>`,
which validates both directions. Sludge is a mixture rather than a kind of water,
so a sludge port never stands in for a water port, and S223's pump shape does not
accept it; see [pumps](treatment_model_summary.md#pumps).

A shared constituent establishes topology compatibility and nothing more. It does
not claim equivalent composition, a material balance, membrane selectivity, or
that a pump suits a sludge.

### Validation

**S223 compatibility.** Connection points and connections must carry compatible
media, by the constituent rule above. An incompatible pair is a violation.

**`watr:CompositionFractionBoundsShape`** and **`watr:CompositionIntervalShape`.**
Each constituent percentage must lie between 0 and 100, and one constituent may
not have conflicting exact values or bounds, such as a lower bound above its upper
bound. Both are violations.

**`watr:CompositionPercentageShape`.** For any node with `s223:composedOf`
fractions in `unit:PERCENT`, the percentages on each common mass or volume basis
may not exceed 100%: "The constituent percentages of {$this} add up to {?total}%,
which exceeds 100%." For a constituent given as a range with
`s223:Aspect-LowLimit` and `s223:Aspect-HighLimit`, only the greatest declared
lower bound counts, since upper bounds need not hold at once. `Brine-5to10Percent`
(5-10% salt, 90-95% water) conforms because its lower bounds sum to 95%. A
partial composition that names only some constituents stays valid. See
{download}`composition-exceeds-100-percent.ttl <../../examples/nonconforming/composition-exceeds-100-percent.ttl>`.

**`watr:CompleteCompositionShape`.** When `watr:hasCompleteComposition true` is
asserted, the common-basis fractions must be able to total 100%. Exact fractions
totaling 90% fail, as do ranges whose tightest upper bounds total 90%. A missing
value or a lower-only bound can still reach 100% and does not by itself establish
a deficit. Mixed units or bases establish no common total. See
{download}`complete-composition-ranges.ttl <../../examples/complete-composition-ranges.ttl>`
and the rejected
{download}`complete-composition-below-100-percent.ttl <../../examples/nonconforming/complete-composition-below-100-percent.ttl>`.

**`watr:CompositionComplementRule`** (SHACL-AF). Fills in a percentage you did
not state. It applies when the medium declares `watr:hasCompleteComposition true`,
the fractions share a basis and percent units, and exactly one carries no
`s223:hasValue`. That fraction becomes the remainder of the others: 12% salt
with an empty water fraction yields 88%, and 20% salt with 10% solids leaves 70%
for water. The completed fraction can be an inline blank node or a named one;
name it when something else must refer to the inferred value. See
{download}`brine-inferred-complement.ttl <../../examples/brine-inferred-complement.ttl>`.
The rule stays silent when more than one fraction is unquantified, when none is
quantified (so a medium naming only `Constituent-H2O` is not claimed to be 100%
water), when a quantified fraction is a low-limit or high-limit range, when a
constituent is declared twice, or when the remainder would be negative. The
negative case is the over-100% error that `CompositionPercentageShape` reports.

## Treatment function

### Modeling

What a unit does is separate from how it is built. The UV unit performs
ultraviolet irradiation for the objective of disinfection. Another UV unit with a
different reactor or more lamps does the same, and a query for disinfection
finds both. Here the class says it all: `UltravioletLightUnit` requires
`Process-UVIrradiation` and inherits `TreatmentObjective-Disinfection` from
`DisinfectionUnit`, so inference supplies both. The reactor states the irradiation
it hosts:

```ttl
:reactor watr:hasProcess watr:Process-UVIrradiation .
```

### Rationale

Containment does not copy a parent's process onto its components, or a component's
onto its parent. Each piece of equipment states, or inherits from its class, what
it does itself.

### Validation

The process and objective shapes and the class-default rules are explained in
[Equipment Type, Treatment Objective, Process, and Role](equipment_function.md).
Processes performed by a group of equipment, such as a treatment train, are in
[Processes Performed by Systems](system_processes.md).
