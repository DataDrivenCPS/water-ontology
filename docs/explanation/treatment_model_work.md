# Treatment model release checks

The treatment vocabulary and inference model are implemented. Main, including
merged PR #46, is incorporated. The
[review disposition](treatment_review.md) records the comments and decisions;
the [model summary](treatment_model_summary.md) documents current behavior.

Source modules live in `ontology/`. The build emits `build/watr.ttl` and a
versioned document. Published term URIs stay unversioned and retired terms carry
`owl:deprecated` and `dcterms:isReplacedBy`.

Reproduce release checks:

```sh
make build-ontology
make test
uv run python scripts/check_watr_terms.py examples
uv run python scripts/generate_reference_docs.py
uv run python scripts/generate-process-objective-map.py
make local-docs
```

Keep generated reference Markdown when vocabulary changes are intentional.
Do not commit compiled build artifacts, HTML output, or OntoEnv caches.

The build checks cover composition constraints, explicit complement-inference
premises, class defaults, process objective inference, system coverage,
equipment-region containment, contaminant targets, port structure, and compiler
prefix metadata.
The documentation queries should parse as SPARQL with the listed prefixes.
