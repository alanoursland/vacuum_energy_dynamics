# Process Folder Map

## What This Document Is

A navigation map of the process subfolder of `03_gr_weak_field`. The process folder contains the framework's evolving analysis of the Equal-Response derivation problem — formerly the open question of why the weak-field spatial response equals the temporal response ($\gamma_v = 1$) in the framework's vacuum-exchange ontology, now closed at first order via the forward-simulation result.

The documents in this folder are working analyses, candidate paths, attempted derivations, and computational investigations. Each document captures a stage of thinking about the problem. This map shows how they relate to one another and what the current status is.

## The Target

The Equal-Response problem is the question:

> Why does the framework's weak-field spatial metric coefficient equal its temporal metric coefficient?

In scale-factor form, $A(r) B(r) = 1$. In mode form, $\kappa = (\ln A + \ln B)/2 = 0$. In observational form, $\gamma_v = 1$ in the PPN expansion.

Closing this question converts `candidate_vacuum_variation_unity.md` from provisional to derived, which makes the framework's reproductions of light deflection, Shapiro delay, and (with the second-order time-metric candidate) perihelion precession unconditional.

**Status: closed at first order.** The forward simulation in `structure_search_local_exchange.md` established that Postulates 1-5 plus the metric ansatz plus Postulate 5's energy minimization plus the empirical fixing of $\gamma_v = 1$ force $J_\kappa = 0$ for local exchange. Trace conservation is no longer an open question; it is a derived consequence of the framework's existing commitments combined with observation. The Configuration Exchange interpretation upgrades from candidate to consequence; the Vacuum Variation Unity assumption upgrades from provisional to derived.

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
commitment              (later ruled
                         out as rescue
                         route)
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
              +-------------------------------+
              | structure_search_local_       |
              | exchange.md                   |
              | (forward simulation closes    |
              |  the question: postulates +   |
              |  observation force J_κ = 0;   |
              |  Path 4 ruled out as rescue)  |
              +-------------------------------+
                          |
                          v
                   (CLOSED AT FIRST ORDER)
                          |
                          v
   Outstanding: second-order time-metric candidate
   (independent question; perihelion precession
   inherits its provisional status until that
   derivation closes separately)
```

## How To Read The Map

The map flows roughly chronologically and from problem-statement to current closure. It branches where multiple paths through postulate-space were considered, merges where computational results forced consolidation, and terminates where the forward simulation closed the question.

### Top: Problem Statement

The Equal-Response target sits at the top. Everything below is an attempt to reach it, characterize what reaching it would require, or rule out attempts that don't reach it.

### First Tier: Path Enumeration

`candidate_paths_to_equal_response.md` enumerates five candidate routes for closing the problem. The branches in the map reflect this enumeration:

- Paths 1, 2, 3 (symmetry, fixed-point, substance) feed into the reframing of Equal-Response as the reciprocal-scale condition.
- Path 4 (richer vacuum mathematical structure) was acknowledged as a possible rescue route. The forward simulation later ruled it out: any version of Path 4 that preserves the framework's other commitments cannot rescue substance exchange.
- Path 5 (exchange-creation separation) is developed in its own branch.

### Second Tier: Two Branches

The left branch focuses on **what closing Equal-Response would mean structurally**. `candidate_reciprocal_scale_equal_response.md` reframes the target from $\gamma_v = 1$ to $AB = 1$ (or $\kappa = 0$). `candidate_mismatch_energy_for_equal_response.md` then asks what would force $\kappa = 0$ at the energy minimum, concluding that the load-bearing assumption is $J_\kappa = 0$ — that exchange does not source the conformal mode.

The right branch focuses on **what new structural commitment would close the problem**. `candidate_exchange_creation_separation.md` proposes the Exchange-Creation Separation principle as a candidate postulate: local exchange is trace-free, vacuum creation is traceful. `attempt_deriving_exchange_creation_separation_from_existing_postulates.md` then tests whether this principle follows from Postulates 1-3 as currently written, concluding it does not.

The two branches converge at the same point. The left branch identifies $J_\kappa = 0$ as the wall. The right branch identifies the same condition as the candidate Exchange-Creation Separation postulate. Both branches concluded — at the time they were written — that the existing postulates do not force this condition. The forward simulation later refined this: the existing postulates *plus the metric ansatz plus observation* do force the condition. The verbal analysis was correct in proof-system isolation but missed the empirical input that closes the chain.

### Third Tier: Computational Investigation

`structure_search_baseline_results.md` is the first computational attack on the wall. Using VacuumForge, it tests whether trace-free exchange falls out of natural candidate structures. Result: in 2D, it doesn't — trace-free exchange occurs only along the antisymmetric directions and is non-generic. The wall is real.

`structure_search_4d_extension_results.md` extends the investigation to 3+1. Result: the trace-free condition is codimension-1 in any dimension. The 2D "rare special direction" framing was an artifact; the constraint is a single conservation law (preservation of $a + b$) rather than a directional fine-tuning. The wall is *reshaped* — clearer in shape, structurally simpler — but at this stage not yet crossed.

### Fourth Tier: Physical Interpretation

`candidate_configuration_exchange_not_substance_exchange.md` interprets the trace-conservation result physically. It argues that under trace conservation, ordinary local gravitational exchange must operate on configuration energy alone, not on the substance content of the vacuum. Cosmic expansion, by contrast, is reserved as the framework's mechanism for substance creation. This document distinguishes two readings of the framework's earlier "vacuum consumption" language and identifies which framework content is affected by the choice.

At the time this document was written, the configuration-exchange interpretation was conditional on adopting trace conservation. With the forward simulation's result, the conditional collapses: trace conservation is forced, so the configuration interpretation is forced as well.

### Fifth Tier: Forward Simulation and Closure

`structure_search_local_exchange.md` runs the framework forward under each $J_\kappa$ value (Fork TC: $J_\kappa = 0$; Fork SE: $J_\kappa \neq 0$) and compares the resulting derivation chains. Result: Fork TC derives $\gamma_v = 1$ as a theorem; Fork SE leaves $\gamma_v$ as a free parameter dependent on source-strength ratios the framework does not specify. The framework's predictive content for $\gamma_v$ exists only under trace conservation. Observation has fixed $\gamma_v = 1$ to parts in $10^5$ via Cassini, which combined with the framework's existing machinery forces $J_\kappa = 0$.

This closes the question at first order. The implication chain is:

```
metric ansatz + Postulate 5 + observation (γ_v = 1)
  => J_κ = 0 (trace conservation forced)
    => κ = 0 at equilibrium
      => AB = 1
        => γ_v = 1 (now derivable rather than assumed)
```

Path 4 was checked as a possible rescue route for substance exchange. The chain that forces $J_\kappa = 0$ runs through the metric ansatz, the energy functional, Postulate 5, and observation; breaking any of these is revision of existing content rather than enrichment of the vacuum's mathematical structure. Path 4 in its enrichment-only form cannot rescue substance exchange.

### Bottom: Closure and Outstanding Work

The Equal-Response problem is closed at first order in $\Phi/c^2$. Trace conservation is a derived consequence of the framework's existing commitments plus observation. Configuration Exchange becomes the established physical interpretation of how local gravity operates: configuration deformation, not substance creation.

The remaining outstanding work in the broader weak-field program is the second-order time-metric candidate (`candidate_second_order_time_metric_from_redshift.md`), which is independent of the local-exchange question. The perihelion precession proof inherits its provisional status until that derivation closes separately.

## Status of Each Document

- `candidate_paths_to_equal_response.md` — candidate path enumeration; framing document. Path 4 is now noted as ruled out for the substance-exchange rescue route.
- `candidate_reciprocal_scale_equal_response.md` — reframing of the target; mathematical equivalence. Content unchanged; status as a reframing tool stands.
- `candidate_mismatch_energy_for_equal_response.md` — energy-minimum argument identifying $J_\kappa = 0$ as the wall. The energy-minimum argument is now part of the closed chain rather than identifying an open question.
- `candidate_exchange_creation_separation.md` — proposed candidate postulate. Now structurally entailed by the framework plus observation rather than free-standing.
- `attempt_deriving_exchange_creation_separation_from_existing_postulates.md` — verbal analysis concluding the candidate postulate is not a consequence of the postulates *alone*. The conclusion is correct in proof-system isolation; the forward simulation completes the picture by adding the metric ansatz and the empirical input.
- `structure_search_baseline_results.md` — 2D computational result; superseded in interpretation by the 4D extension but retained as the first establishing pass.
- `structure_search_4d_extension_results.md` — 3+1 computational result; established the codimension-1 conservation-law shape of the constraint.
- `candidate_configuration_exchange_not_substance_exchange.md` — physical interpretation. Now structurally entailed (upgrade from candidate to consequence pending document revision).
- `structure_search_local_exchange.md` — forward simulation; closes the question at first order. The current best statement of what the framework commits to about local exchange.

The candidate documents in the framework proper — `candidate_vacuum_variation_unity.md` and `candidate_second_order_time_metric_from_redshift.md` — are affected differently:

- `candidate_vacuum_variation_unity.md`: upgrades from provisional to derived (with respect to first-order content).
- `candidate_second_order_time_metric_from_redshift.md`: unaffected. Remains the framework's outstanding open derivation for second-order content.

## Reading Order

For someone new to the Equal-Response problem, the documents should be read roughly in the order they appear in the map, top to bottom:

1. `candidate_paths_to_equal_response.md` (the landscape)
2. `candidate_reciprocal_scale_equal_response.md` (target reframing)
3. `candidate_mismatch_energy_for_equal_response.md` (energy argument identifying the wall)
4. `candidate_exchange_creation_separation.md` (proposed postulate)
5. `attempt_deriving_exchange_creation_separation_from_existing_postulates.md` (why the postulate doesn't fall out of postulates alone)
6. `structure_search_baseline_results.md` (first computational test)
7. `structure_search_4d_extension_results.md` (corrected and generalized computational test)
8. `candidate_configuration_exchange_not_substance_exchange.md` (physical interpretation of the trace-conservation result)
9. `structure_search_local_exchange.md` (forward simulation; closes the question at first order)

Reading in this order, the problem develops from a vague "we need to derive $\gamma_v = 1$" through a sharply specified "we need to derive trace conservation" to "trace conservation is forced by the framework plus observation, and the Configuration Exchange interpretation is the physical content of that closure."

## Migration Notes

When the relevant candidate documents are revised to reflect the closure (re-tagging Configuration Exchange from candidate to consequence; upgrading Vacuum Variation Unity from provisional to derived; updating the static-gravity proofs' provisional sections), several of these process documents will become historical records of the derivation rather than active working notes. The methodology supports keeping them in the process folder as audit trail, with the closure documents (`structure_search_local_exchange.md` and the revised candidate documents) becoming the primary references.

The discipline of keeping the process folder intact rather than collapsing it into the closure is what makes the framework's reasoning auditable. A future reader who wants to understand *how* the framework arrived at trace conservation as a derived consequence will be able to trace the documents in reading order and see the chain of analysis that produced the closure. That auditability is part of what the methodology was designed to preserve.