# Notes for coding agents

## Writing explanation pages (`docs/explanation/`)

An explanation page describes how a part of the ontology is modeled and checked.
Root it in the SHACL shapes, not in prose about the domain.

For each topic, use these three subsections, in order:

1. **What the shapes require** (or **What the ontology defines** for pure
   vocabulary, **What the model states** for modeler-facing relations).
   Summarize the shape: which class, which property, how many of what type. Use
   a table when several classes are compared, and include a "Subclass of" column
   so inheritance is explicit. Read the shape in `ontology/` rather than
   describing it from memory.
2. **Why.** The modeling reason the requirement exists, in domain terms. Do not
   explain SHACL mechanics here, such as "one port cannot fill both slots".
3. **How it is validated.** Every validation rule behind it: the shape name,
   its severity, what it checks and what it deliberately does not. Name any
   SHACL-AF rule, inference step or workaround that applies, and what it does.
   If nothing is validated, say so in one line.

Keep it terse and direct. Link the conforming and nonconforming examples. Quote
the shape's own `sh:message` wording where it helps. Do not state anything the
shapes do not enforce as if they did.

After editing the ontology, regenerate the reference docs with
`make reference-docs`, and update any explanation page that describes the changed
shape.
