# Work needed on the branch

This is the implementation checklist for the design in
[treatment_model_summary.md](treatment_model_summary.md).
That document describes the target model. This one lists what has to change
on the `gtf-watr-constituent-mixtures` branch to match it.

Each item says where the design document describes the end state. Items marked *not in the design document* are implementation details with no design content.

1. Restructure the objective hierarchy. Add `Constituent Removal`, `Dissolved Solids Removal`, `Volume Reduction`, `pH Control`, and `Resource Recovery` as parents. Move the existing objectives under them. Keep `Clarification`. Described in section 7, objectives tree.
2. Add `watr:targetsConstituent` on constituent-removal objectives, and allow a modeler to create a local objective typed `watr:TreatmentObjective-ConstituentRemoval` that points at a constituent. Described in section 1a, treatment objective, and section 7, constituents.
3. Extend the constituent vocabulary in `water/substances.ttl` to the list in section 7. New terms: `DissolvedSolids`, `Hardness`, `Silica`, `Sulfate`, `VolatileOrganicCompounds`, `PFAS`, `Nitrogen`, `OrganicNitrogen`, `Phosphorus`, `Phosphate`, `Pathogens`, `Viruses`, `Protozoa`, `ChlorineResidual`. Re-parent `Salt` and `Metals` under `DissolvedSolids`, `Ammonia`, `Nitrate`, and `Nitrite` under `Nitrogen`, and `Bacteria` under `Pathogens`. Declare `watr:targetsConstituent` on every named constituent-removal objective and on Disinfection.
4. Make `Land Application` and `Landfill` processes that achieve `Biosolids Disposal`. Described in sections 4 and 7.
5. Remove the clarification default from `watr:SedimentationTank`. Add `watr:Clarifier` as a subclass carrying clarification. Apply the rule that a class carries a design objective only when every unit of the class is built for the same result, and audit the other equipment classes against it. Described in sections 1a, 2, and 6.
6. Rename `Process-ChlorineDosing` to `Process-Chlorination`. Add `Process-SulfiteDosing`, achieving chlorine residual removal. Rename `Dechlorination` to `Chlorine Residual Removal` and keep the old name as an alternate label. Described in sections 4 and 7.
7. Drop the desalination default on `ReverseOsmosisMembrane`. Described in sections 2, 4, and 6. Open question, *not in the design document*: whether `ElectrodialysisUnit` keeps its desalination default. The team decides whether electrodialysis is desalination-specific.
8. Add the system-membership query for "everything involved in an objective" to `docs/guides/querying_treatment_function.md`, and fix that file's variable names, which contain a space (`?treatment objective`) after an earlier rename. Described in section 10.
9. Add an inference rule that copies `watr:achievesTreatmentObjective` from a process onto every unit and system that performs it, next to the class-defaults rule. Remove the warning that currently fires when the objective is missing. Described in sections 1a, 1b, and 5, which already treat the objective as inherited.
10. Document the repurposing rule: an unchanged vessel gains a role; a rebuilt vessel gets a new type. Described in section 6, repurposed unit.
11. Mechanical fixes, *not in the design document*: rename the outcomes files and the process-outcome map to say "objective"; fix the GAC duplicate in the generated docs and rename it GAC Filtration; label the root process "Water Treatment Process"; prefix `MakeUp` with `Role-` in the docs; de-duplicate the aeration basin description; explain `rdfs:comment` versus `skos:definition`; link the shifty severity levels.
