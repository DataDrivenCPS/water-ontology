# Pending Ontology Features

This page tracks potential additions to WaTr for future design and discussion.
The entries are proposals, not implemented capabilities or release commitments.
Add new entries with their motivation, current support, open questions, and a
link to the originating discussion when available.

## Chemical conversions

**Status:** Proposed; deferred from PR #39.

Represent how a treatment process transforms constituents, such as oxidation
changing one chemical species into another. This could help explain changes
between incoming and outgoing streams and eventually support validation of
declared transformations.

WaTr currently describes treatment mechanisms and objectives, along with stream
constituents and composition. It does not encode reaction-specific conversion
rules or validate reaction stoichiometry and material balances. An objective
does not establish that a measured conversion occurred.

Questions to resolve:

- How should reactants, products, and chemical species be identified?
- How should conversions depend on reagents and operating conditions?
- What information is needed for qualitative inference versus quantitative
  material-balance validation?
- How should incomplete stream composition affect validation findings?

Origin: [Fletcher's chemical-conversion question on PR #39](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3814151705).

## Recirculation inferred from topology

**Status:** Proposed; deferred from PR #39.

Recognize and distinguish recycle streams from their connections and their
position within a treatment system. For example, mixed-liquor recycle between
biological treatment zones may have a different function from a recycle confined
to one unit.

WaTr currently supports explicit recirculation processes and S223
connection-point roles. It does not infer recirculation or its treatment purpose
from topology alone.

Questions to resolve:

- What topology and flow-direction evidence identifies a recycle stream?
- How should system boundaries distinguish internal and external recycles?
- Which operating-state information is needed for reversible or valved paths?
- Which process classifications can safely follow from a recycle's location?
- How should inferred information interact with explicit modeler annotations?

Origin: [Daly's recirculation question on PR #39](https://github.com/DataDrivenCPS/water-ontology/pull/39#discussion_r3806523244).

## Equipment/process plausibility checks

**Status:** Deferred; removed from PR #39 during review preparation.

Optionally flag unusual combinations of equipment types and declared processes.
WaTr currently permits modelers to state additional processes while validating
their types and preserving equipment-class requirements. No permission list or
plausibility-warning shape is used. Cleaning processes still imply the
equipment-cleaning objective when explicitly declared.

Questions to resolve:

- Is there enough practical benefit to justify maintaining expected combinations?
- How should multifunction equipment, retrofits, and equipment regions be handled?
- Should checks be an optional application profile rather than core ontology rules?
- How can incomplete permission lists avoid warnings on legitimate plant models?

The earlier `mayAlsoPerform` property and `ProcessPlausibilityShape` are removed
from the release preparation. Revisit their design only if a concrete modeling
or application need emerges.
