from pathlib import Path

import pytest
from brick_tq_shacl import validate
from ontoenv import OntoEnv
from rdflib import Graph, Namespace


SH = Namespace("http://www.w3.org/ns/shacl#")
WATR = Namespace("urn:nawi-water-ontology#")


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"
NONCONFORMING_EXAMPLES_DIR = EXAMPLES_DIR / "nonconforming"
WATER_DIR = ROOT / "water"


def _ttl_files(directory: Path) -> list[Path]:
    """Return all Turtle files beneath a directory in stable order."""
    return sorted(path for path in directory.rglob("*.ttl") if path.is_file())


def _conforming_example_files() -> list[Path]:
    """Return example files that are expected to pass SHACL validation."""
    return [
        path
        for path in _ttl_files(EXAMPLES_DIR)
        if NONCONFORMING_EXAMPLES_DIR not in path.parents
    ]


def _example_id(path: Path) -> str:
    """Build a readable pytest parameter id relative to the repo root."""
    return str(path.relative_to(ROOT))


@pytest.fixture(params=_conforming_example_files(), ids=_example_id)
def example_file(request: pytest.FixtureRequest) -> Path:
    """Provide each conforming example file as a test parameter."""
    return request.param


@pytest.fixture(params=_ttl_files(NONCONFORMING_EXAMPLES_DIR), ids=_example_id)
def nonconforming_example_file(request: pytest.FixtureRequest) -> Path:
    """Provide each intentionally invalid example file as a test parameter."""
    return request.param


def _has_example_violations(data_graph: Graph, report_graph: Graph) -> bool:
    """Return whether the SHACL report contains a violation on an example node."""
    example_nodes = set(data_graph.all_nodes())
    for result in report_graph.subjects(SH.focusNode, None):
        if report_graph.value(result, SH.resultSeverity) != SH.Violation:
            continue
        if report_graph.value(result, SH.focusNode) in example_nodes:
            return True
    return False


def _ontology_closure_for_example(example_graph: Graph) -> tuple[Graph, list[str]]:
    """Resolve an example graph's imports into a dedicated closure graph."""
    env = OntoEnv(
        path=ROOT,
        recreate=True,
        search_directories=[str(WATER_DIR)],
        includes=["*.ttl"],
    )
    env.update(all=True)
    return env.get_dependencies(example_graph, fetch_missing=True)


def _validation_result(example_file: Path) -> dict:
    """Validate one example graph and return the SHACL result payload."""
    data_graph = Graph().parse(example_file)
    ontology_shapes_graph, imported = _ontology_closure_for_example(data_graph)
    valid, report_graph, report_string = validate(
        data_graph,
        shape_graphs=ontology_shapes_graph,
        min_iterations=5,
    )
    return {
        "valid": valid,
        "report_graph": report_graph,
        "report_string": report_string,
        "data_graph": data_graph,
        "imported_ontologies": imported,
        "has_example_violations": _has_example_violations(data_graph, report_graph),
    }


@pytest.fixture
def example_validation_result(example_file: Path) -> dict:
    """Return the SHACL validation result for a conforming example."""
    return _validation_result(example_file)


@pytest.fixture
def nonconforming_example_validation_result(
    nonconforming_example_file: Path,
) -> dict:
    """Return the SHACL validation result for a nonconforming example."""
    return _validation_result(nonconforming_example_file)
