# Process Folder Map

## What This Document Is

A navigation map of the process subfolder of `03_gr_weak_field`. The process folder contains the framework's evolving analysis of the Equal-Response derivation problem — the open question of why the weak-field spatial response equals the temporal response ($\gamma_v = 1$) in the framework's vacuum-exchange ontology.

The documents in this folder are not derivations the framework currently endorses. They are working analyses, candidate paths, attempted derivations, and computational investigations. Each document captures a stage of thinking about the problem. This map shows how they relate to one another and where the current frontier sits.

## The Target

The Equal-Response problem is the question:

> Why does the framework's weak-field spatial metric coefficient equal its temporal metric coefficient?

In scale-factor form, $A(r) B(r) = 1$. In mode form, $\kappa = (\ln A + \ln B)/2 = 0$. In observational form, $\gamma_v = 1$ in the PPN expansion.

Closing this question converts `candidate_vacuum_variation_unity.md` from provisional to derived, which makes the framework's reproductions of light deflection, Shapiro delay, and (with the second-order time-metric candidate) perihelion precession unconditional.

## Map
```
EQUAL-RESPONSE PROBLEM
                      (γ_v = 1, A·B = 1)
                            |
                            v
              +---------------------------+
              | candidate_paths_to_       |
              | equal_response.md         |
              | (the path enumeration)    |
              +---------------------------+
                            |
    +-----------------------+-------------------------+
    |                       |                         |
    v                       v                         v
Path 1, 2, 3:           Path 4:                    Path 5:
symmetry,               richer vacuum              exchange-creation
fixed-point,            mathematical               separation
substance               structure
commitment              (open work,
                         not pursued
                         here)
    \                                                /
     \                                              /
      v                                            v
+---------------------+              +-----------------------------+
| candidate_          |              | candidate_                  |
| reciprocal_scale_   |              | exchange_creation_          |
| equal_response.md   |              | separation.md               |
| (reframes target    |              | (proposes new postulate     |
|  as κ = 0 / AB = 1) |              |  to close the problem)      |
+---------------------+              +-----------------------------+
      |                                            |
      |                                            |
      v                                            v
+---------------------+              +-----------------------------+
| candidate_          |              | attempt_deriving_           |
| mismatch_energy_    |              | exchange_creation_          |
| for_equal_          |              | separation_from_            |
| response.md         |              | existing_postulates.md      |
| (energy minimum     |              | (verbal analysis: cannot    |
|  argument; concludes|              |  derive J_κ = 0 from        |
|  J_κ = 0 is wall)   |              |  Postulates 2 and 3 alone)  |
+---------------------+              +-----------------------------+
      |                                            |
      +-------------------+------------------------+
      |
      v
+-------------------------------+
| structure_search_baseline_    |
| results.md                    |
| (2D computational test:       |
|  trace-free exchange is       |
|  non-generic, only            |
|  antisymmetric directions)    |
+-------------------------------+
      |
      v
+-------------------------------+
| structure_search_4d_          |
| extension_results.md          |
| (3+1 computational test:      |
|  trace-free is codimension-1, |
|  reframed as conservation     |
|  law on trace a + b)          |
+-------------------------------+
      |
      v
+-------------------------------+
| candidate_configuration_      |
| exchange_not_substance_       |
| exchange.md                   |
| (physical interpretation:     |
|  if trace conservation,       |
|  exchange is configuration    |
|  not substance)               |
+-------------------------------+
      |
      v
(CURRENT FRONTIER)
      |
      v
Open: derive trace conservation
under static spherical symmetry,
or adopt as structural postulate,
or explore Path 4 (richer vacuum
mathematical structure)

```

## How To Read The Map

The map flows roughly chronologically and from problem-statement to current-frontier. It branches where multiple paths through postulate-space were considered, and merges where computational results forced consolidation.

### Top: Problem Statement

The Equal-Response target sits at the top. Everything below is an attempt to reach it, characterize what reaching it would require, or rule out attempts that don't reach it.

### First Tier: Path Enumeration

`candidate_paths_to_equal_response.md` enumerates five candidate routes for closing the problem. The branches in the map reflect this enumeration:

- Paths 1, 2, 3 (symmetry, fixed-point, substance) feed into the reframing of Equal-Response as the reciprocal-scale condition.
- Path 4 (richer vacuum mathematical structure) is acknowledged but not pursued in detail in this folder.
- Path 5 (exchange-creation separation) is developed in its own branch.

### Second Tier: Two Branches

The left branch focuses on **what closing Equal-Response would mean structurally**. `candidate_reciprocal_scale_equal_response.md` reframes the target from $\gamma_v = 1$ to $AB = 1$ (or $\kappa = 0$). `candidate_mismatch_energy_for_equal_response.md` then asks what would force $\kappa = 0$ at the energy minimum, concluding that the load-bearing assumption is $J_\kappa = 0$ — that exchange does not source the conformal mode.

The right branch focuses on **what new structural commitment would close the problem**. `candidate_exchange_creation_separation.md` proposes the Exchange-Creation Separation principle as a candidate postulate: local exchange is trace-free, vacuum creation is traceful. `attempt_deriving_exchange_creation_separation_from_existing_postulates.md` then tests whether this principle follows from Postulates 1-3 as currently written, concluding it does not.

The two branches converge at the same point. The left branch identifies $J_\kappa = 0$ as the wall. The right branch identifies the same condition as the candidate Exchange-Creation Separation postulate. Both branches conclude that the existing postulates do not force this condition; either it must be derived from richer structure or adopted as a new commitment.

### Third Tier: Computational Investigation

`structure_search_baseline_results.md` is the first computational attack on the wall. Using VacuumForge, it tests whether trace-free exchange falls out of natural candidate structures. Result: in 2D, it doesn't — trace-free exchange occurs only along the antisymmetric directions and is non-generic. The wall is real.

`structure_search_4d_extension_results.md` extends the investigation to 3+1. Result: the trace-free condition is codimension-1 in any dimension. The 2D "rare special direction" framing was an artifact; the constraint is a single conservation law (preservation of $a + b$) rather than a directional fine-tuning. The wall is *reshaped* — clearer in shape, structurally simpler — but not crossed.

### Fourth Tier: Physical Interpretation

`candidate_configuration_exchange_not_substance_exchange.md` interprets the trace-conservation result physically. It argues that under trace conservation, ordinary local gravitational exchange must operate on configuration energy alone, not on the substance content of the vacuum. Cosmic expansion, by contrast, is reserved as the framework's mechanism for substance creation. This document distinguishes two readings of the framework's earlier "vacuum consumption" language and identifies which framework content is affected by the choice.

### Bottom: Current Frontier

The frontier is at the trace-conservation question. Three options remain:

1. Derive trace conservation under static spherical symmetry from existing postulates (the next-investigation target named in the 4D extension).
2. Develop Path 4 — the vacuum's richer mathematical structure — and check whether trace conservation falls out as a consequence.
3. Adopt trace conservation as a new structural postulate (with the Configuration Exchange interpretation as its physical content).

## Status of Each Document

- `candidate_paths_to_equal_response.md` — candidate path enumeration; framing document, not a derivation.
- `candidate_reciprocal_scale_equal_response.md` — reframing of the target; mathematical equivalence, not new content.
- `candidate_mismatch_energy_for_equal_response.md` — energy-minimum argument identifying $J_\kappa = 0$ as the wall; conditional on assumptions noted in the document.
- `candidate_exchange_creation_separation.md` — proposed candidate postulate; not adopted, not derived.
- `attempt_deriving_exchange_creation_separation_from_existing_postulates.md` — verbal analysis concluding the candidate postulate is not a consequence of existing postulates.
- `structure_search_baseline_results.md` — 2D computational result; superseded in interpretation by the 4D extension but retained as the first establishing pass.
- `structure_search_4d_extension_results.md` — 3+1 computational result; current best statement of what the structure search has shown.
- `candidate_configuration_exchange_not_substance_exchange.md` — physical interpretation conditional on trace conservation; not yet load-bearing in the framework.

None of these documents are framework commitments. They are the working notes of an open derivation. When the derivation closes — by deriving trace conservation, by adopting it as a postulate, or by replacing it with a different route to Equal-Response — the relevant documents will move out of `process/` and into the framework proper, with appropriate revisions.

## Reading Order

For someone new to the Equal-Response problem, the documents should be read roughly in the order they appear in the map, top to bottom:

1. `candidate_paths_to_equal_response.md` (the landscape)
2. `candidate_reciprocal_scale_equal_response.md` (target reframing)
3. `candidate_mismatch_energy_for_equal_response.md` (energy argument identifying the wall)
4. `candidate_exchange_creation_separation.md` (proposed postulate)
5. `attempt_deriving_exchange_creation_separation_from_existing_postulates.md` (why the postulate doesn't fall out of existing commitments)
6. `structure_search_baseline_results.md` (first computational test)
7. `structure_search_4d_extension_results.md` (corrected and generalized computational test)
8. `candidate_configuration_exchange_not_substance_exchange.md` (physical interpretation of the trace-conservation result)

Reading in this order, the problem develops from a vague "we need to derive $\gamma_v = 1$" into a sharply specified "we need to derive trace conservation under static spherical symmetry," with the framework's options for how to do so explicitly laid out.
