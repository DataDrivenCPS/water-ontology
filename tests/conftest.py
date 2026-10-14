from contextlib import contextmanager
from pathlib import Path

import pytest
import shifty
from ontoenv import OntoEnv
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import OWL


SH = Namespace("http://www.w3.org/ns/shacl#")
WATR = Namespace("https://watermetadata.org/ontology/watr#")


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"
NONCONFORMING_EXAMPLES_DIR = EXAMPLES_DIR / "nonconforming"
LOCAL_DPR_EXAMPLE = EXAMPLES_DIR / "union-dpr-model.ttl"
WATER_DIR = ROOT / "ontology"
S223_DIR = ROOT / "s223"

CLASS_DEFAULTS_FILE = WATER_DIR / "class-defaults.ttl"
CLASS_DEFAULTS_URI = URIRef("https://watermetadata.org/ontology/modules/class-defaults")


def _ttl_files(directory: Path) -> list[Path]:
    """Return all Turtle files beneath a directory in stable order."""
    return sorted(path for path in directory.rglob("*.ttl") if path.is_file())


def _conforming_example_files() -> list[Path]:
    """Return committed examples expected to pass SHACL validation.

    The local DPR integration model is not part of this example corpus.
    """
    return [
        path
        for path in _ttl_files(EXAMPLES_DIR)
        if NONCONFORMING_EXAMPLES_DIR not in path.parents
        and path != LOCAL_DPR_EXAMPLE
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


def _has_example_result_with_severity(
    data_graph: Graph, report_graph: Graph, severities: set
) -> bool:
    """Return whether example data has a validation result at a given severity."""
    example_nodes = set(data_graph.all_nodes())
    for result in report_graph.subjects(SH.focusNode, None):
        severity = report_graph.value(result, SH.resultSeverity)
        if severity not in severities:
            continue
        if report_graph.value(result, SH.focusNode) in example_nodes:
            return True
    return False


def _has_example_violations(data_graph: Graph, report_graph: Graph) -> bool:
    """Return whether the SHACL report contains a violation on example data."""
    return _has_example_result_with_severity(
        data_graph, report_graph, {SH.Violation}
    )


def _has_example_warnings_or_violations(
    data_graph: Graph, report_graph: Graph
) -> bool:
    """Return whether the report contains a warning or violation on example data."""
    return _has_example_result_with_severity(
        data_graph, report_graph, {SH.Warning, SH.Violation}
    )


@pytest.fixture(scope="session")
def water_graph() -> Graph:
    """Parse the water ontology's own Turtle files, merged, once per session."""
    g = Graph()
    for path in sorted(WATER_DIR.glob("*.ttl")):
        g.parse(path, format="ttl")
    return g


@pytest.fixture(scope="session")
def water_graph_without_class_defaults() -> Graph:
    """The water ontology with the class-defaults rule not imported.

    Built the way the ontology itself would be if it did not ship the rule: the
    file is left unparsed and the owl:imports triple naming it is dropped, so the
    closure resolved from this graph never reaches it. Contrast
    ``water_graph``, which imports it -- see ``ontology/watr.ttl``.
    """
    g = Graph()
    for path in sorted(WATER_DIR.glob("*.ttl")):
        if path == CLASS_DEFAULTS_FILE:
            continue
        g.parse(path, format="ttl")
    g.remove((None, OWL.imports, CLASS_DEFAULTS_URI))
    return g


@contextmanager
def _test_environment(root: Path, temporary_root: Path):
    """Resolve current sources without writing to the development environment.

    Reuse only downloaded vocabulary from its cache. Local models and compiled
    graphs are excluded, and source modules are always indexed afresh.
    """
    cached_graphs = []
    options = {}
    if (root / ".ontoenv").is_dir():
        with OntoEnv.connect(str(root), read_only=True) as existing:
            options = {
                "offline": existing.is_offline(),
                "remote_cache_ttl_secs": existing.remote_cache_ttl_secs(),
            }
            cache = temporary_root / "vocabulary-cache"
            cache.mkdir(parents=True)
            for name in sorted(existing.get_ontology_names()):
                location = str(existing.get_ontology(name).location)
                if not location.startswith(("http://", "https://")):
                    continue
                path = cache / f"{len(cached_graphs)}.ttl"
                existing.copy_graph(name).serialize(path, format="turtle")
                cached_graphs.append((name, path))

    with OntoEnv.create(
        str(temporary_root / "resolver"),
        search_directories=[str(root / "ontology"), str(root / "s223")],
        includes=["*.ttl"],
        **options,
    ) as env:
        for name, path in cached_graphs:
            env.add_no_imports(str(path), rename=name)
        env.update(force=True)
        yield env


@pytest.fixture(scope="session")
def ontoenv(tmp_path_factory):
    """One isolated resolver for the session, with reusable remote vocabulary."""
    with _test_environment(ROOT, tmp_path_factory.mktemp("ontoenv")) as env:
        yield env


@pytest.fixture(scope="session")
def ontology_shapes_graph(water_graph: Graph, ontoenv: OntoEnv) -> Graph:
    """Resolve the water ontology's full import closure once per session."""
    shapes_graph, _imported = ontoenv.get_dependencies(water_graph, fetch_missing=True)
    shapes_graph += water_graph
    return shapes_graph


@pytest.fixture(scope="session")
def shapes_graph_without_class_defaults(
    water_graph_without_class_defaults: Graph, ontoenv: OntoEnv
) -> Graph:
    """The same closure resolved from a graph that does not import the rule."""
    shapes_graph, _imported = ontoenv.get_dependencies(
        water_graph_without_class_defaults, fetch_missing=True
    )
    shapes_graph += water_graph_without_class_defaults
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
        "has_example_warnings_or_violations": _has_example_warnings_or_violations(
            data_graph, report_graph
        ),
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
