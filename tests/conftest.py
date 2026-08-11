from pathlib import Path

import pytest
import shifty
from ontoenv import OntoEnv
from rdflib import Graph, Namespace


SH = Namespace("http://www.w3.org/ns/shacl#")
WATR = Namespace("urn:nawi-water-ontology#")


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"
NONCONFORMING_EXAMPLES_DIR = EXAMPLES_DIR / "nonconforming"
WATER_DIR = ROOT / "water"
S223_DIR = ROOT / "s223"


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


@pytest.fixture(scope="session")
def water_graph() -> Graph:
    """Parse the water ontology's own Turtle files, merged, once per session."""
    g = Graph()
    for path in sorted(WATER_DIR.glob("*.ttl")):
        g.parse(path, format="ttl")
    return g


@pytest.fixture(scope="session")
def ontology_shapes_graph(water_graph: Graph) -> Graph:
    """Resolve the water ontology's full import closure once per session."""
    env = OntoEnv.connect(ROOT, read_only=True)
    shapes_graph, _imported = env.get_dependencies(water_graph, fetch_missing=True)
    shapes_graph += water_graph
    return shapes_graph


def _validation_result(example_file: Path, ontology_shapes_graph: Graph) -> dict:
    """Validate one example graph and return the SHACL result payload."""
    data_graph = Graph().parse(example_file)
    valid, report_graph, report_string = shifty.validate(
        data_graph,
        shacl_graph=ontology_shapes_graph,
    )
    return {
        "valid": valid,
        "report_graph": report_graph,
        "report_string": report_string,
        "data_graph": data_graph,
        "has_example_violations": _has_example_violations(data_graph, report_graph),
    }


@pytest.fixture
def example_validation_result(
    example_file: Path, ontology_shapes_graph: Graph
) -> dict:
    """Return the SHACL validation result for a conforming example."""
    return _validation_result(example_file, ontology_shapes_graph)


@pytest.fixture
def nonconforming_example_validation_result(
    nonconforming_example_file: Path, ontology_shapes_graph: Graph
) -> dict:
    """Return the SHACL validation result for a nonconforming example."""
    return _validation_result(nonconforming_example_file, ontology_shapes_graph)
