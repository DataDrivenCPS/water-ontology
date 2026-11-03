"""Focused tests for the A2/O treatment-train example.

The generic ``test_examples`` suite only checks that the example produces no
SHACL warning or violation on an example node. The A2/O brief asks for more:
class-default inference must be visible, the compound process must sit on the
system rather than a tank, every constituent step of ``watr:Process-A2O`` must
have a witness in the train, and the recycle loops must be modeled as
assemblies. These tests pin those properties.
"""

from pathlib import Path

import shifty
from rdflib import Graph, Namespace

WATR = Namespace("https://watermetadata.org/ontology/watr#")
S223 = Namespace("http://data.ashrae.org/standard223#")
EX = Namespace("https://watermetadata.org/ontology/modules/examples/a2o-train#")

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "a2o-train.ttl"


def _inferred(ontology_shapes_graph):
    data = Graph().parse(EXAMPLE)
    return shifty.infer(data, shapes_graph=ontology_shapes_graph).graph()


def test_compound_process_is_on_the_system_not_a_tank(ontology_shapes_graph):
    inf = _inferred(ontology_shapes_graph)
    # Process-A2O is asserted on the train system.
    assert (EX.a2oTrain, WATR.hasProcess, WATR["Process-A2O"]) in inf
    # ... and not on any of the tanks.
    for tank in ("anaerobicZone", "anoxicZone", "aerobicZone", "clarifier"):
        assert (EX[tank], WATR.hasProcess, WATR["Process-A2O"]) not in inf


def test_class_defaults_are_materialized(ontology_shapes_graph):
    """The clarifier omits its fixed process and objective; both appear
    after SHACL-AF inference. Zones declare complete process overrides."""
    inf = _inferred(ontology_shapes_graph)
    defaults = [
        (EX.clarifier, WATR.hasProcess, WATR["Process-Settling"]),
        (EX.clarifier, WATR.hasTreatmentObjective, WATR["TreatmentObjective-Clarification"]),
    ]
    missing = [(s, p, o) for s, p, o in defaults if (s, p, o) not in inf]
    assert not missing, f"class-default inference missed: {missing}"


def test_installation_specific_processes_are_stated_not_inferred(ontology_shapes_graph):
    """EBPR, denitrification and nitrification are installation-specific, so they
    are in the source file as well as in the inferred graph."""
    data = Graph().parse(EXAMPLE)
    stated = [
        (EX.anaerobicZone, WATR.hasProcess, WATR["Process-Mixing"]),
        (EX.anoxicZone, WATR.hasProcess, WATR["Process-Mixing"]),
        (EX.aerobicZone, WATR.hasProcess, WATR["Process-Aeration"]),
        (EX.anaerobicZone, WATR.hasProcess, WATR["Process-EnhancedBiologicalPhosphorusRemoval"]),
        (EX.anoxicZone, WATR.hasProcess, WATR["Process-Denitrification"]),
        (EX.aerobicZone, WATR.hasProcess, WATR["Process-Nitrification"]),
    ]
    for triple in stated:
        assert triple in data, f"expected {triple} to be stated in the example"


def test_every_constituent_step_has_a_witness(ontology_shapes_graph):
    """All six steps of Process-A2O (its own four plus aeration and solid-liquid
    separation inherited from Process-ActivatedSludge) must be performed by the
    train, a member, or a member of a nested subsystem."""
    inf = _inferred(ontology_shapes_graph)
    query = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX s223: <http://data.ashrae.org/standard223#>
        PREFIX watr: <https://watermetadata.org/ontology/watr#>
        SELECT ?system ?missing WHERE {
          ?system watr:hasProcess ?compound .
          ?compound rdfs:subClassOf*/watr:includesProcess ?missing .
          FILTER NOT EXISTS {
            ?system s223:hasMember* ?performer .
            ?performer watr:hasProcess ?actual .
            ?actual rdfs:subClassOf* ?missing .
          }
        }
    """
    # The inferred model contains instance statements; process definitions and
    # their hierarchy remain in the ontology. Query both so coverage cannot
    # pass simply because includesProcess statements are absent.
    query_graph = ontology_shapes_graph + inf
    required = set(query_graph.objects(WATR["Process-A2O"], WATR.includesProcess))
    assert required, "A2/O must declare constituent steps before checking coverage"
    missing = list(query_graph.query(query))
    assert not missing, f"uncovered A2O steps: {missing}"


def test_recycle_loops_are_assemblies_with_recirculation(ontology_shapes_graph):
    """Recirculation is performed by nested systems, not by pumps alone, and the
    pumps/valves are members of those systems."""
    data = Graph().parse(EXAMPLE)
    for system, members in (
        (EX.internalRecycleSystem, (EX.internalRecycleValve, EX.internalRecyclePump)),
        (EX.rasSystem, (EX.rasValve, EX.rasPump)),
    ):
        assert (system, WATR.hasProcess, WATR["Process-Recirculation"]) in data
        for member in members:
            assert (system, S223.hasMember, member) in data


def test_roles_are_on_zones_and_clarifier(ontology_shapes_graph):
    data = Graph().parse(EXAMPLE)
    roles = [
        (EX.anaerobicZone, WATR["Role-Anaerobic"]),
        (EX.anoxicZone, WATR["Role-Anoxic"]),
        (EX.aerobicZone, WATR["Role-Aerobic"]),
        # watr:Role-Secondary (the wastewater stage), not s223:Role-Secondary (a loop).
        (EX.clarifier, WATR["Role-Secondary"]),
    ]
    for equip, role in roles:
        assert (equip, S223.hasRole, role) in data, f"missing role {role} on {equip}"


def test_recycle_pump_ports_retain_the_actual_process_medium(ontology_shapes_graph):
    """A pump must not relabel sludge as generic water merely to meet its shape."""
    data = Graph().parse(EXAMPLE)
    media = {
        EX.irPumpInlet: WATR["Sludge-MixedLiquor"],
        EX.irPumpOutlet: WATR["Sludge-MixedLiquor"],
        EX.rasPumpInlet: WATR["Fluid-Sludge"],
        EX.rasPumpOutlet: WATR["Fluid-Sludge"],
    }
    for connection_point, medium in media.items():
        assert (connection_point, S223.hasMedium, medium) in data


def test_system_outcomes_include_inherited_organics_removal(ontology_shapes_graph):
    """Process-A2O inherits Process-ActivatedSludge, which achieves
    TreatmentObjective-OrganicsRemoval, so the train has it whether it says so or
    not -- watr:ProcessObjectiveRule follows the subclass chain."""
    data = Graph().parse(EXAMPLE)
    for outcome in (
        WATR["TreatmentObjective-NitrogenRemoval"],
        WATR["TreatmentObjective-PhosphorusRemoval"],
        WATR["TreatmentObjective-OrganicsRemoval"],
    ):
        assert (EX.a2oTrain, WATR.hasTreatmentObjective, outcome) in data
