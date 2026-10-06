# Contributing to the NAWI Water Ontology

This guide covers how the repository is laid out, the URI and naming rules that govern every term, and how to get a change built, tested, and merged.

- [Reporting bugs and issues](#reporting-bugs-and-issues)
- [Proposing changes](#proposing-changes)
- [Development setup](#development-setup)
- [Repository layout](#repository-layout)
- [Building the ontology](#building-the-ontology)
- [URIs, namespacing, and versioning](#uris-namespacing-and-versioning)
- [Adding and changing terms](#adding-and-changing-terms)
- [Deprecating terms](#deprecating-terms)
- [Templates](#templates)
- [Testing](#testing)
- [Submitting pull requests](#submitting-pull-requests)
- [Cutting a release](#cutting-a-release)

## Reporting bugs and issues

Open an issue on the [issue tracker](https://github.com/DataDrivenCPS/water-ontology/issues),
or start a thread on the [discussion board](https://github.com/DataDrivenCPS/water-ontology/discussions)
if you are unsure whether something is a bug.

Search first, as someone may have already reported it. A good report includes:

- A clear, descriptive title.
- The Turtle snippet, SPARQL query, or model that triggers the problem.
- What you expected, and what actually happened (paste the SHACL report if
  validation is involved).
- Whether you are on the latest `main`.

## Proposing changes

Modeling changes are discussed before they are implemented. Open an issue that
covers:

- **Motivation**: the real system or dataset you cannot currently describe.
- **Scope**: which classes, processes, or relationships are affected.
- **Sketch**: the terms you propose, their parents, and an example instance.

Modeling decisions ripple into everyone's data, so it is much cheaper to settle
the shape of a change in an issue instead of in a pull request review.
Once the design is agreed upon, implement it in a branch and open a PR.

## Development setup

The project uses [`uv`](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
and requires Python 3.11 or newer.

```bash
git clone https://github.com/DataDrivenCPS/water-ontology
cd water-ontology
uv sync
```

`uv sync` installs OntoEnv 0.6+ for both the Python API and the CLI; run it as
`uv run ontoenv`. No separate CLI install is needed. `pyproject.toml` is the
single source of truth for dependencies. If you add one, specify a version
range, re-run `uv sync`, and mention it in your PR.

To refresh the vendored copy of 223P, run `./download-s223.sh`. This only works
if you already have access to that repository.

## Repository layout

| Path | Contents |
| --- | --- |
| `ontology/` | **The ontology source. Edit these files.** |
| `build/` | Compiled ontology documents. Generated, git-ignored. Never edit or commit these! |
| `libraries/` | BuildingMOTIF templates (`templates/`, `nrel-223p-templates/`) and the vendored `223p.ttl` |
| `s223/` | Vendored ASHRAE 223P ontology files. |
| `examples/` | Example models that must pass validation; `examples/nonconforming/` holds models that must *fail*. |
| `scripts/` | Compile, validation, and documentation utilities. |
| `tests/` | pytest suite. |
| `docs/` | Jupyter Book documentation. |

`ontology/` holds five development modules:

| File | Ontology IRI |
| --- | --- |
| `watr.ttl` | `https://watermetadata.org/ontology/watr` |
| `equipment.ttl` | `https://watermetadata.org/ontology/modules/equipment` |
| `processtypes.ttl` | `https://watermetadata.org/ontology/modules/processtypes` |
| `substances.ttl` | `https://watermetadata.org/ontology/modules/substances` |
| `enumerationkinds.ttl` | `https://watermetadata.org/ontology/modules/enumerationkinds` |

The split is an authoring convenience to keep related concepts together. The
module IRIs are **not published**; the compile strips them and merges everything
into one document.

**`owl:imports` decides what gets included in the watr.ttl build.** The
compile starts at `ontology/watr.ttl` and walks the import closure, keeping
every graph whose IRI is under `https://watermetadata.org/ontology/`.

To add a module:

1. Give it an `owl:Ontology` declaration with an IRI under
   `/ontology/modules/<name>`.
2. Add `owl:imports <that IRI>` to `ontology/watr.ttl`, or to a module already
   in the closure.

Dropping a file into `ontology/` without step 2 does nothing: it will not be
merged, and its terms will not appear in the published ontology. This is
deliberate — it keeps work-in-progress and experiments out of a release, and
makes the module structure something you declare rather than something the
filesystem decides.

## Building the ontology

```bash
make build-ontology   # compile both published documents
make test             # compile, then run the test suite
make clean            # remove build/ and the OntoEnv cache
```

There is no separate setup step. The OntoEnv environment in `.ontoenv/` is
created on first use, and `make build-ontology` refreshes it (`ontoenv update`,
which is incremental) before every compile. It resolves both the external
dependencies (223P, QUDT, SHACL) and the internal module imports the compile
walks, so a newly added or re-pointed module is picked up automatically.

If you run `scripts/compile-water-ontology.py` directly rather than through
`make`, refresh it yourself first with `uv run ontoenv update`. Otherwise, the
closure wil lbe resolved against a stale index.

One compile emits two documents:

- `build/watr.ttl`: unversioned "latest" copy.
- `build/watr-<version>.ttl`: immutable versioned snapshot

They contain identical term definitions and differ only in their ontology IRI,
`owl:versionIRI`, and the `rdfs:isDefinedBy` on each term.

Only the modules under `ontology/` are merged. External dependencies stay as
`owl:imports` rather than being copied in, which keeps the published document
around 3k triples instead of 116k, and lets consumers resolve 223P and QUDT at
whatever version they already have. The consequence is that `build/watr.ttl`
is **not self-contained** — loading it requires an import resolver (OntoEnv, or
BuildingMOTIF with `libraries/223p.ttl` loaded alongside).

> **Never commit `build/`.** It is git-ignored, and OntoEnv is configured to
> exclude it. Both matter: a compiled artifact declares the same ontology IRI as
> `ontology/watr.ttl`, so if OntoEnv indexes it, a previous build shadows the
> real sources and folds the entire external closure back into the next one.

## URIs, namespacing, and versioning

**Every term lives in one permanently unversioned namespace:**

```
https://watermetadata.org/ontology/watr#Pump
```

bound to the prefix `watr:`.

**A version identifies a document, never a term.** This is the convention QUDT,
Brick, and 223P all converge on. `watr:Pump` means the same thing in every
release, so upgrading never requires rewriting existing models.

| Role | IRI |
| --- | --- |
| Term namespace (`watr:`) | `https://watermetadata.org/ontology/watr#` |
| Published document, latest | `https://watermetadata.org/ontology/watr` |
| Published document, versioned | `https://watermetadata.org/ontology/0.2/watr` |
| Development modules (not published) | `https://watermetadata.org/ontology/modules/<name>` |

Rules that follow from this:

- **Never put a version in a term URI.** A versioned term namespace makes
  `watr:Pump` from a 1.0 model a different resource from `watr:Pump` in a 1.1
  model, with nothing relating them.
- **Never rename or re-namespace a term.** Renaming breaks every model that
  already uses it. Deprecate instead (see below).
- **Never hand-write a versioned IRI in a source file.** The compile derives
  both documents from the same sources.

The published documents get `owl:versionIRI`, `owl:versionInfo`, and an
`rdfs:isDefinedBy` on every term pointing at the document that defines it. The
compile adds all of these -- do not write them by hand.

## Adding and changing terms

Add terms to the module that fits: equipment to `equipment.ttl`, processes to
`processtypes.ttl`, media and constituents to `substances.ttl`, enumerations to
`enumerationkinds.ttl`. Keep related definitions near each other so diffs stay
readable.

**Naming.** Class names are `CamelCase` (`watr:RapidSandFilter`,
`watr:GravityThickener`). Properties are `lowerCamelCase` and read as a phrase
(`watr:hasProcess`, `watr:hasTemporalResolution`). Individuals and
sub-vocabularies use a `Category-Specific` prefix, which keeps families
alphabetically adjacent:

- `watr:Process-Filtration`, `watr:Process-MediaFiltration`
- `watr:Constituent-NaCl`, `watr:Constituent-Organics`
- `watr:Coagulant-Alum`, `watr:Disinfectant-Ozone`, `watr:Water-Brine`

**Every term needs a label and a definition — both are enforced.** The
`watr:Class` shape requires an `rdfs:label` and an `rdfs:comment`. Both are
violations, so a term missing either will fail `make test`.

Use `rdfs:comment` for the definition. Say what the term means and, where useful, how it differs from its siblings.

`watr:Class` is a **metaclass**, following `s223:Class`: terms are instances of
it (`a watr:Class`), never subclasses of it. Keep it that way. SHACL gives a
shape that is also an `rdfs:Class` an implicit target of every instance of
itself *and of its subclasses*, so a single `rdfs:subClassOf watr:Class`
anywhere in the hierarchy would silently extend these documentation rules to
every instance in every user model (so a pump instance in a plant model would be asked for
a definition). Water classes descend from the s223 hierarchy
(`s223:Equipment`, `s223:Substance`, and so on), which is where they belong.

A typical equipment class:

```turtle
watr:GravityThickener
    a sh:NodeShape ;
    a watr:Class ;
    rdfs:label "Gravity Thickener" ;
    rdfs:comment "A thickener that uses gravity settling to concentrate solids." ;
    rdfs:subClassOf watr:Thickener ;
    sh:property [
        sh:path watr:hasProcess ;
        sh:hasValue watr:Process-Sedimentation ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:message "Instances of GravityThickener must have the Sedimentation process." ;
    ] .
```

**Equipment classes must stay consistent with the processes they inherit.** A
subclass may only *refine* an ancestor's `watr:hasProcess` constraint, never
contradict it: at least one of its required processes must be the same as, or a
transitive subclass of, each process an ancestor requires. Adding a new
equipment class often means adding a matching process to `processtypes.ttl`
first. `tests/test_processtype_consistency.py` enforces this and names the
offending class when it fails.

Add an example under `examples/` demonstrating any substantive new term. If the
change makes a previously valid pattern invalid, add a case to
`examples/nonconforming/`.

The reference pages under `docs/reference/` are generated from the modules. Run
`make reference-docs` and commit the result, so the published documentation
lists the term.

## Deprecating terms

Terms are retired, never deleted or renamed:

```turtle
watr:OldTerm
    owl:deprecated true ;
    rdfs:comment "Deprecated in 0.3. Use watr:NewTerm instead." ;
    dcterms:isReplacedBy watr:NewTerm .
```

Keep the original definition in place so existing models still resolve.

## [Testing](Testing.md)

```bash
make test
```

The suite covers four things:

| Test | Checks |
| --- | --- |
| `test_examples.py` | Every model in `examples/` passes SHACL validation. |
| `test_nonconforming_examples.py` | Every model in `examples/nonconforming/` fails, as intended. |
| `test_validation.py` | The ontology validates against its own shapes. |
| `test_processtype_consistency.py` | Equipment process constraints refine, never contradict, their ancestors. |

To check that a directory of models only uses terms the
ontology actually defines, which catches typos and stale copy-paste:

```bash
uv run python scripts/check_watr_terms.py examples
```

Run the full suite before opening a PR, and add tests or examples alongside
ontology changes.

## Submitting pull requests

Fork, branch, and open a PR against `main`.

- **Keep PRs focused.** One modeling concern per PR; separate mechanical
  renames from substantive changes.
- **Do not commit generated files** — `build/`, `docs/_build/`, `.ontoenv/`.
  Check `git status` before committing.
- **Make sure `make test` passes.**
- **Write a useful description**: what changed, why, any new SHACL shapes or
  templates, and the impact on downstream models. Call out anything that
  invalidates existing data.

## Preparing a release

1. Bump `ONTOLOGY_VERSION` in `scripts/compile-water-ontology.py`.
2. Run `make clean && make test`.
3. Re-run the watermetadata.org repository to update the submodule and publish the new version. The ontology is published
   behind `watermetadata.org` as `/ontology/watr` and `/ontology/<version>/watr`.

Note that GitHub Pages serves an extensionless file as
`application/octet-stream`, so consumers may need to name the format
explicitly: `Graph().parse(url, format="turtle")`.

## Need help?

Open a [discussion](https://github.com/DataDrivenCPS/water-ontology/discussions),
or open a draft PR early if you would like feedback before the change is
finished.
