# Vacuum-Consumption Gravity

## Reader's Guide and Development Plan

---

## Overview

This project develops a speculative framework for gravity based on a simple intuition: gravitational potential energy is not bookkeeping but something physical, and that something is the vacuum itself. When a mass falls through a gravitational gradient, it consumes vacuum and converts it into kinetic energy. When energy climbs out of a gravitational well, it regenerates vacuum and loses its own energy in proportion. What we call spacetime is not a stage on which physics happens; it is the vacuum substance whose function is to constrain how information can propagate.

The framework is being developed in dialogue, one postulate and one derivation at a time. Each substantive claim is captured in its own document so that it can be revised independently as the framework matures.

The structure below serves two purposes. For a reader new to the project, it is a reading order: follow the documents from top to bottom and the framework will unfold in dependency order. For the development effort itself, it is a plan: it shows what has been written, what is planned, and how the pieces are expected to relate to one another.

---

## Status Legend

- **[done]** — document written and current
- **[skeleton]** — document exists but is incomplete or a placeholder
- **[planned]** — document intended but not yet started
- **[open]** — work item, not yet assigned to a document

---

## The Tree

### Foundational Layer

- **[done] `overview.md`** — the supposition and its motivation. Establishes the "what if" at the root of the project, the relationship to special relativity (adopted) and general relativity (bracketed), and the methodology of provisional supposition.

- **[done] `postulate_vacuum_energy_density.md`** — Postulate 1. The vacuum possesses a finite energy density $\rho_v$ that is locally constant: every observer, in their own frame, measures the same finite value at every location. This is the foundational claim that everything else builds on. Rules out accounts of gravity or cosmology based on spatial or temporal variation in vacuum density, and commits the framework to locating geometric variation in the amount of vacuum present rather than in its density.

- **[done] `postulate_vacuum_exchange_in_gradients.md`** — Postulate 2. Any energy in a region of curvature gradient experiences a force directed along the gradient, applied uniformly to every quantum of energy. When energy moves along the gradient toward greater curvature, its momentum along the gradient increases and vacuum is consumed; when it moves against the gradient, momentum along the gradient decreases and vacuum is regenerated. Combines what were originally separate postulates for descent and ascent. Explicitly does not propose a mechanism for the force — this is a real gap the framework has not yet filled.

- **[done] `consequence_curvature_as_spatial_differential.md`** — works out what the existing postulates commit us to about curvature. Under Postulate 1 (constant density) and the identity postulate (vacuum is spacetime), the only way spacetime can vary geometrically is through variation in the amount of vacuum per span of space. Curvature is the spatial-volume differential between neighboring spans. Consumption increases local curvature; regeneration decreases it.

- **[done] `postulate_mass_energy_equivalence.md`** — Postulate 3. All forms of energy participate in vacuum exchanges equivalently, via mass-energy equivalence. A photon of energy $E$ behaves, for purposes of vacuum exchange, as if it possessed mass $E/c^2$. This follows from special relativity but is stated explicitly because of the work it does in derivations.

  - **[done] `proof_gravitational_redshift.md`** — derivation of the gravitational redshift formula from the core postulates, without importing General Relativity. Recovers the Pound-Rebka result in the weak-field limit. Distinctively, identifies a physical source and sink for the energy change (vacuum regeneration on ascent, consumption on descent) that standard physics leaves as unexplained bookkeeping. Depends on all three core postulates plus special relativity.

### Ontological Layer

- **[done] `postulate_vacuum_spacetime_identity.md`** — the postulate that the vacuum is identical to spacetime (the structure that constrains information propagation), from which it follows that spacetime is energy. Lays out four options for how vacuum and spacetime could be related and argues for identity as the choice that fits the framework's prior commitments while removing free parameters. Depends on the core postulates.

  - **[done] `consequence_cosmic_expansion.md`** — works out what the identity postulate forces us to say about the observed expansion of the universe. If space is vacuum is energy, then expansion creates energy. Notes the alignment with dark energy's observed constant density and flags the connection to Noether's theorem and the known failure of global energy conservation in expanding spacetimes.

  The following candidates are discussions or partial derivations that become possible once the vacuum-spacetime identity is adopted. Each is an independent line of inquiry; they do not depend on one another, only on the parent postulate.

  - **[planned] `candidate_equivalence_principle.md`** — argument that the equivalence of gravitational and inertial mass follows from the framework rather than being an independent postulate. Both quantities reduce to vacuum consumed in forming a given body. This is the candidate most likely to yield a real reduction in independent assumptions.

  - **[planned] `candidate_black_hole_entropy.md`** — discussion of whether the area-scaling of black hole entropy admits a natural interpretation in the framework, where the horizon is the boundary across which the information-propagation substrate transitions from normal to depleted.

  - **[planned] `candidate_time_dilation_mechanism.md`** — derivation path for gravitational time dilation as a direct mechanistic consequence of vacuum depletion slowing local signal propagation. Aims to check whether the framework's prediction matches GR's $\sqrt{1 - 2GM/rc^2}$ factor or diverges.

  - **[planned] `candidate_universal_speed_limit.md`** — discussion of why $c$ appears universally across special relativity, electromagnetism, and gravity. Under the framework, $c$ is the natural speed of the substrate, and its universal appearance reflects that all these phenomena involve the same substrate.

  - **[planned] `candidate_finite_speed_propagation.md`** — the claim that disturbances in the vacuum propagate at exactly $c$. Previously treated as a consequence of the identity postulate, but flagged as using ingredients (what counts as a propagating substrate change, what detectability means) that have not been rigorously defined within the framework. Candidate theorem pending those definitions.

### Open Work

The following are questions the framework needs to address but which do not yet have documents assigned to them. Resolving any of these will produce new documents to be inserted into the tree at the appropriate places.

- **[open]** Mechanism for the gravitational force. Postulate 2 commits to the observable phenomenon (force directed along a curvature gradient, acting on every quantum of energy) but does not propose a microscopic mechanism. An early candidate (asymmetric vacuum exchange across the mass) had a scaling problem — it predicted decreasing force in regions of reduced space, which does not match observation. A working mechanism is the central gap in the framework's account of gravity.

- **[open]** Mathematical structure of the vacuum — is $\rho_v$ a scalar, a tensor, or something richer? The functional argument suggests the vacuum must carry enough structure to implement a full metric, which likely exceeds what a simple scalar density can provide. An additional constraint: whatever structure the vacuum has, it must support independent extensive variation (amount of vacuum per span, which produces curvature) and intensive variation (energy density, which Postulate 1 fixes as constant). A single scalar field whose value is the density cannot support this independence. Resolving the structure question unlocks several downstream derivations.

- **[open]** Relationship between vacuum density and total vacuum energy in a region. The framework implicitly assumes something like $E_v \sim \rho_v V$ but has not formally committed to this. Quantitative work on cosmic expansion and elsewhere will require pinning this down.

- **[open]** Spatial profile of $\rho_v$ around a spherically symmetric mass, derived from symmetry plus the vacuum-spacetime identity, without importing the Schwarzschild solution. The key test of whether the framework can reproduce (or correct) Newtonian gravity from first principles.

- **[open]** Equation of motion for a test body in a vacuum-density gradient. Currently the framework asserts that masses fall but does not derive the trajectory they follow.

- **[open]** Mode structure of gravitational radiation in the framework. Does it predict pure transverse modes (matching GR), pure breathing modes (likely ruled out by Hulse-Taylor), or a mixture? This is where the framework is most likely to make a falsifiable prediction distinct from GR.

- **[open]** Connection between the framework and existing scalar-tensor gravity theories. If the framework turns out to be isomorphic to Brans-Dicke or a similar theory once its mathematical structure is pinned down, that is useful to know explicitly.

- **[open]** The cosmological constant problem — does the framework offer any principled account of why $\Lambda$ has its specific small value, beyond the qualitative alignment noted in the cosmic expansion consequence document?

- **[open]** Mass formation. The framework describes exchanges between vacuum and kinetic energy but does not say how masses come to exist in the first place. Pair production, gravitational collapse, and the early universe all touch this gap.

- **[open]** Quantum formulation. The framework is currently classical. How vacuum consumption looks at the quantum level is not addressed and may eventually require substantial new machinery.

---

## Notes on Organization

Documents in this project follow a few conventions worth stating explicitly.

Filenames use lowercase words connected by underscores. The prefix indicates the document's role:

- `postulate_` — documents whose primary content is a postulate adopted by the framework
- `proof_` — documents containing a derivation from postulates to a specific result
- `candidate_` — documents exploring possible derivations or consequences that are not yet fully established
- `consequence_` — documents tracing what the framework's postulates commit us to say about a specific phenomenon, without introducing new postulates or deriving new theorems

Documents without a prefix (like `overview.md` and `README.md`) are framework-level rather than content-level documents.

Documents do not link to one another. Cross-references are given by document name in prose. This keeps documents portable and avoids broken links during reorganization.

When a document's status changes — from skeleton to done, or from planned to skeleton — the entry in this tree should be updated. When new open questions emerge, they are added under Open Work. When open questions are resolved and acquire their own documents, they move from Open Work into the tree at the appropriate position.

This README is itself a living document. It will be revised as the framework develops.

---

## Current Reading Order

For someone encountering this project for the first time, the correct reading order is:

1. This README, for orientation.
2. `overview.md`, for the supposition at the root of the project.
3. `postulate_vacuum_energy_density.md`, for Postulate 1 (foundational).
4. `postulate_vacuum_exchange_in_gradients.md`, for Postulate 2 (force and exchange in gradients).
5. `postulate_vacuum_spacetime_identity.md`, for the ontological postulate.
6. `consequence_curvature_as_spatial_differential.md`, for what curvature is under the existing postulates.
7. `consequence_cosmic_expansion.md`, for what the identity forces us to say about expansion.
8. `postulate_mass_energy_equivalence.md`, for Postulate 3.
9. `proof_gravitational_redshift.md`, for the first derivation from the core postulates.
10. Any of the candidate documents, in any order, according to interest.

Documents marked `[planned]` do not yet exist. Readers encountering a gap in the sequence have reached the current frontier of the work.