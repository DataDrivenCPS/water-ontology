# Offline QUDT test vocabulary

`qudt-3.3.0.ttl` contains upstream descriptions of the units and quantity kinds
referenced by `ontology/`, `examples/`, the bundled `s223/` graphs, and the YAML
templates in `libraries/templates/`, plus schema definitions and
the quantity kinds associated with those units. Blank-node descriptions are
included; other linked resources are not expanded. This is a subset for
testing, not a replacement for the complete published QUDT ontologies.

Sources: [QUDT 3.3.0 units](https://qudt.org/3.3.0/vocab/unit),
[QUDT 3.3.0 quantity kinds](https://qudt.org/3.3.0/vocab/quantitykind), and the
[QUDT 3.3.0 schema](https://qudt.org/3.3.0/schema/qudt).
Attribution: QUDT.org, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The extraction preserves the selected RDF descriptions without modifying them.

To regenerate after adding references to external vocabulary:

```sh
curl -L --fail -H 'Accept: text/turtle' https://qudt.org/3.3.0/vocab/unit -o /tmp/watr-qudt-units.ttl
curl -L --fail -H 'Accept: text/turtle' https://qudt.org/3.3.0/vocab/quantitykind -o /tmp/watr-qudt-quantitykinds.ttl
curl -L --fail -H 'Accept: text/turtle' https://qudt.org/3.3.0/schema/qudt -o /tmp/watr-qudt-schema.ttl
uv run python scripts/extract_test_qudt.py /tmp/watr-qudt-units.ttl /tmp/watr-qudt-quantitykinds.ttl /tmp/watr-qudt-schema.ttl
uv run pytest tests
```

The coverage test fails if a referenced unit or quantity kind is missing from
the snapshot. The duration inference test also checks that unit metadata
supports inferring `quantitykind:Time` from `unit:HR`.
