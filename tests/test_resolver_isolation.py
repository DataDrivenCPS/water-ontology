"""Validation must preserve the developer's persistent ontology environment."""

from ontoenv import OntoEnv
from rdflib import Literal, URIRef
from rdflib.namespace import RDFS

from conftest import _test_environment


ONTOLOGY = "urn:resolver-isolation:ontology"


def _source(path, label):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"""
        @prefix owl: <http://www.w3.org/2002/07/owl#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        <{ONTOLOGY}> a owl:Ontology; rdfs:label "{label}" .
    """)


def test_resolver_preserves_configuration_and_reindexes_only_sources(tmp_path):
    root = tmp_path / "project"
    _source(root / "ontology/source.ttl", "Current source")
    _source(root / "models/compiled.ttl", "Unrelated model")
    (root / "s223").mkdir()
    with OntoEnv.create(str(root), search_directories=[str(root / "models")],
                        offline=True, remote_cache_ttl_secs=12345,
                        excludes=["build/*"]) as existing:
        existing.update(force=True)
    config = root / ".ontoenv/ontoenv.json"
    original = config.read_bytes()

    with _test_environment(root, tmp_path / "isolated") as env:
        assert env.is_offline()
        assert env.remote_cache_ttl_secs() == 12345
        graph = env.copy_graph(ONTOLOGY)
        assert graph.value(URIRef(ONTOLOGY), RDFS.label) == Literal("Current source")
        assert config.read_bytes() == original

    assert config.read_bytes() == original
    with OntoEnv.connect(str(root), read_only=True) as existing:
        graph = existing.copy_graph(ONTOLOGY)
        assert graph.value(URIRef(ONTOLOGY), RDFS.label) == Literal("Unrelated model")


def test_resolver_does_not_create_a_development_cache(tmp_path):
    root = tmp_path / "project"
    _source(root / "ontology/source.ttl", "Source")
    (root / "s223").mkdir()
    with _test_environment(root, tmp_path / "isolated") as env:
        assert ONTOLOGY in env.get_ontology_names()
    assert not (root / ".ontoenv").exists()
