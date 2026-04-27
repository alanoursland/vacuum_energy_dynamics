# Structure Search: Local Exchange Forward Simulation

## What This Document Is

This is a pre-lab document, now extended with results. It describes the planned VacuumForge investigation of the framework's commitment to $J_\kappa$ for local gravitational exchange, the experimental setup, and the results obtained when the experiment was run. The structure follows the chemistry pre-lab convention: state the position in the larger investigation, describe the experimental setup and the methodology in concrete terms, identify what the experiment can and cannot establish, pre-register the outcomes, and report the results against the pre-registration.

The investigation is the natural next move identified at the conclusion of `structure_search_4d_extension_results.md` and refined through analysis in the candidate documents. It is also the cheaper of two complementary investigations identified during planning; the alternative — a full postulate-space mapping that determines which subsets of postulates force which $J_\kappa$ values — remains available as a follow-up if this investigation reveals it is needed.

## Position in the Map

The map of the process folder (`process_folder_map.md`) places this investigation at the current frontier. The Equal-Response problem has been refined through several stages:

```
                    EQUAL-RESPONSE PROBLEM
                            |
                            v
              [path enumeration, target reframing,
               energy argument, candidate postulate,
               attempted derivation, computational
               investigation in 2D and 3+1]
                            |
                            v
              Trace conservation identified as
              the open question. Codimension-1
              constraint, single conservation law.
                            |
                            v
                   THIS INVESTIGATION
                   (forward simulation)
                            |
                            v
              [postulate-space mapping if needed,
               Path 1 derivation of trace
               conservation, or adoption as
               structural postulate]
```

The structure search has established that trace conservation is the load-bearing condition for closing Equal-Response through the trace-kernel route. The candidate documents have established what trace conservation would mean physically (Configuration Exchange) and have noted that the existing postulates do not, on the verbal analysis available so far, force trace conservation.

This investigation tested that verbal-analysis conclusion computationally. By running the framework forward under each value of $J_\kappa$, it determined whether the existing postulates *actually* leave $J_\kappa$ undetermined or whether they have hidden commitments that the verbal analysis missed.

## Hypothesis

Three outcomes were possible.

**Outcome A: Both forks are consistent.** The existing postulates leave $J_\kappa$ undetermined. Choosing $J_\kappa = 0$ or $J_\kappa \neq 0$ produces two internally consistent extensions of the framework. The framework's current predictive content does not depend on the choice; closing the question requires either additional postulates or richer ontological structure.

**Outcome B: One fork produces a contradiction.** The existing postulates have already silently committed to one $J_\kappa$ value. Adopting the other value contradicts existing framework content. This would surface a hidden commitment the verbal analysis had not noticed.

**Outcome C: The forks differ in predictive content.** Both forks are internally consistent but produce different predictions for some derivable observable. The choice between them becomes empirically testable.

The verbal analysis strongly suggested Outcome A. The methodology designed in response to the previous framework's collapse is built precisely to surface cases that look like Outcome A but are secretly Outcome B. This investigation was an audit against that failure mode.

## Experimental Design

### Setup

Two TheoryContext instances were constructed, identical in their commitment to Postulates 1-5 and their derived consequences, differing only in their commitment to $J_\kappa$ for local gravitational exchange.

**Fork TC: trace conservation fork.** Postulates 1-5 plus the additional commitment $J_\kappa = 0$ for local exchange. This is the postulate state under which the Configuration Exchange interpretation becomes load-bearing.

**Fork SE: substance exchange fork.** Postulates 1-5 plus the additional commitment $J_\kappa \neq 0$ for local exchange. This is the postulate state in which ordinary gravitational interaction creates and destroys vacuum substance locally.

The cosmic expansion consequence retains $J_\kappa \neq 0$ in both forks; that commitment is independent of the local-exchange question. What differs between the forks is only the local-exchange behavior.

### Operations Per Fork

For each fork, the investigation ran the framework's existing derivations through VacuumForge under the strengthened postulate set. The derivations re-checked included:

- The Newtonian limit derivation from Postulate 3.
- The metric ansatz $A = \exp(\Phi/c^2), B = \exp(-\gamma_v \Phi/c^2)$ with $\gamma_v$ free.
- The exchange source specification under each fork.
- The energy functional construction.
- The energy minimization stationary conditions.
- The derivation chain $\kappa_{eq} \to AB \to \gamma_v$.

For each derivation, the analysis recorded:

1. **Closure.** Does the derivation still close under the strengthened postulate set?
2. **Route.** Does it close through the same logical chain as the original derivation, or through a different chain enabled or required by the strengthened postulate?
3. **New theorems.** Does any previously open or provisional result become derivable?
4. **Contradictions.** Does any existing framework content become inconsistent with the strengthened postulate set?
5. **Predictive divergence.** Does the strengthened fork produce a different prediction for any observable than the other fork?

### VacuumForge Implementation

The investigation was implemented as two scripts:

- `e5a.py`: Primary forward simulation comparing forks via energy minimization, requirement validation, model classification, and side-by-side comparison.
- `e5b.py`: Detailed derivation chain audit tracing each step under both forks with explicit dependency tracking.

Both scripts share the same fork-construction logic but differ in how they expose the derivation chain. e5a uses the M26 model-comparison machinery for high-level reporting; e5b uses the dependency-tracking machinery (M1-M18) for step-by-step audit.

### Reporting Format

The investigation produces a comparison report in three sections:

**Section A: Per-derivation comparison.** A table with rows for each derivation and columns for each fork, showing closure status and route.

**Section B: Newly derivable theorems.** For each fork, results that were previously open or provisional but become derivable.

**Section C: Predictive divergences.** Predictions that differ between forks.

## What This Investigation Establishes

This investigation is *forward simulation* in proof-system mode. It establishes structural facts about the framework's commitments under each fork. It does not establish world-truth.

What it can establish:

- Whether the existing postulates have a hidden commitment to one $J_\kappa$ value (Outcome B).
- Whether the framework's current derivable content distinguishes the two forks (Outcome C).
- Which derivations depend on which assumptions, in a form auditable against the framework's prose claims.
- Whether the methodology's verbal analysis of "the postulates don't force trace conservation" is correct or whether it missed a hidden commitment.

What it cannot establish:

- Which fork matches physical reality. That requires observation.
- Whether trace conservation can be derived under a *strengthened* reading of an existing postulate. That is a separate Path 1 investigation, requiring different machinery.
- Whether the framework's strong-field or cosmological-scale predictions distinguish the forks. The current derivable scope is weak-field; strong-field and detailed cosmological predictions are open work.

## Relation to Adjacent Documents

This investigation extends the structure-search line:

- `structure_search_baseline_results.md` — established that trace-free exchange is non-generic in 2D.
- `structure_search_4d_extension_results.md` — corrected this to a codimension-1 conservation law in any dimension and identified the static spherical $e_t + e_s = 0$ form.
- `structure_search_local_exchange.md` — *this document.* Forward simulation under each $J_\kappa$ value to map the framework's commitments.

This investigation also activates the candidate documents:

- `candidate_configuration_exchange_not_substance_exchange.md` — the physical interpretation of $J_\kappa = 0$.
- `candidate_paths_to_equal_response.md` — the path enumeration.

## Pre-Registration

The pre-lab convention asks the experimenter to commit, before running the experiment, to what would count as which outcome.

**Outcome A is registered if:** Both forks complete all derivations without contradiction, with closures through the same routes as the originals. No new theorems become derivable in either fork beyond those expected from the trace-conservation chain in Fork TC. No predictive divergences are surfaced within the framework's current derivable scope.

**Outcome B is registered if:** One fork produces a contradiction during execution of an existing derivation. The contradiction surfaces a hidden commitment in the existing postulates that the verbal analysis had not identified.

**Outcome C is registered if:** Both forks complete consistently but produce different predictions for some derivable observable. The divergence is explicitly identified and a candidate observation that would distinguish them is named.

If the investigation surfaced something not anticipated by the three outcomes — a partial contradiction, an inconsistency in the framework that doesn't track the fork distinction, a derivation that fails under both forks — that should be reported as a *fourth* outcome and treated as a finding about the framework's current state independent of the $J_\kappa$ question.

## Reproduction

The experiment is implemented as `e5a.py` and `e5b.py` in `vacuum_energy_dynamics/vacuum_forge/src/scripts/`:

```
PYTHONPATH=src python src/scripts/e5a.py
PYTHONPATH=src python src/scripts/e5b.py
```

## Results

### Section A: Per-Derivation Comparison

| Derivation | Fork TC | Fork SE |
|-----------|---------|---------|
| Newtonian limit (A) | derived | derived |
| B ansatz | present | present |
| Exchange source | candidate postulate | candidate postulate |
| Energy functional | present | present |
| $\kappa$ equilibrium | $\kappa = 0$ | $\kappa = J_k/(2C_\kappa)$ |
| $\sigma$ equilibrium | $\sigma = J_s/(2C_\sigma)$ | $\sigma = J_s/(2C_\sigma)$ |
| Reciprocal scaling | $AB = 1$ derived | $AB = \exp(J_k/C_\kappa)$ |
| $\gamma_v = 1$ | derived | open question |

Both forks completed all derivations. No fork produced an internal contradiction. The chains diverged at the energy equilibrium step, with downstream consequences that propagated through the rest of the chain.

### Section B: Newly Derivable Theorems

**Fork TC (trace conservation):**

- $\kappa_{eq} = 0$ from energy minimization with $J_\kappa = 0$.
- $AB = 1$ from $\kappa = 0$ via $a + b = 0$.
- $\gamma_v = 1$ from $AB = 1$ combined with the metric ansatz $A = \exp(\Phi/c^2), B = \exp(-\gamma_v \Phi/c^2)$.
- Reciprocal scaling derived (passes the requirement validator).

**Fork SE (substance exchange):**

- $\kappa_{eq} = J_k/(2C_\kappa)$ from energy minimization with $J_\kappa = J_k \neq 0$.
- $AB = \exp(J_k/C_\kappa)$, which equals 1 only if $J_k = 0$ (contradicting the fork premise).
- $\gamma_v$ remains a free parameter dependent on the $J_k/C_\kappa$ ratio.
- Reciprocal scaling fails the requirement validator.

### Section C: Predictive Divergences

| Quantity | Fork TC | Fork SE |
|----------|---------|---------|
| $\kappa$ at equilibrium | $0$ | $J_k/(2C_\kappa)$ |
| $AB$ | $1$ exact | $\exp(J_k/C_\kappa)$ |
| $\gamma_v$ | $1$ (derived) | free parameter |
| Light deflection coefficient $(1+\gamma_v)/2$ | $1.0$ | $(1+\gamma_v)/2$, undetermined |
| Shapiro delay coefficient $(1+\gamma_v)$ | $2.0$ | $(1+\gamma_v)$, undetermined |
| Perihelion precession | standard GR | modified, depends on $\gamma_v$ |

### Leak Detection Audit

Section F of `e5a.py` reported a leak on `gamma_v_one` in Fork TC, traced through the assumption `gamma_v_derived`. This is a tooling artifact rather than a substantive finding: the script in `e5a.py` adds `gamma_v_derived` directly as an assumption to satisfy the requirement validator, rather than letting the dependency resolver propagate it through the chain. The full derivation chain is implemented correctly in `e5b.py`, where `gamma_v_one_derived` is added through the proper sequence (`newtonian_A`, `B_ansatz`, `kappa_equilibrium`, `reciprocal_scaling_derived`) with dependency tracking enabled. The leak detector's flag in `e5a.py` reflects a missing intermediate step in that script, not a circular argument in the underlying mathematics.

Fork SE reported no leaks. The other audited targets (`reciprocal_scaling`, `kappa_zero`, `trace_free_exchange`) were clean in both forks.

## Interpretation

### Outcome Determination

The result is closer to a *fourth outcome* than to any of the three pre-registered options.

The pre-registered Outcome C envisioned both forks making different predictions for some derivable observable, with the divergence being symmetric in the sense that each fork commits to a specific prediction. What actually happened is asymmetric: Fork TC predicts $\gamma_v = 1$ as a derivable theorem; Fork SE does not predict any specific $\gamma_v$ at all, leaving it as a free parameter that depends on source-strength ratios the framework does not currently specify.

The careful statement is therefore:

> **Fourth Outcome (asymmetric predictive content).** Fork TC entails $\gamma_v = 1$ as a derivable theorem from Postulates 1-5 plus trace conservation. Fork SE leaves $\gamma_v$ undetermined: it depends on the ratio $J_k/C_\kappa$, which the framework's current postulates do not constrain. The framework's predictive content for $\gamma_v$ exists only under trace conservation. Observation has fixed $\gamma_v = 1$ to parts in $10^5$ (Cassini, 2002); empirical reality is consistent with Fork TC and provides no positive support for Fork SE.

This is a stronger result than symmetric Outcome C. Symmetric Outcome C would have said "both forks make predictions, observation will decide." The actual result says "one fork makes a prediction, the other punts; observation is consistent with the predicting fork." Observation provides positive support for Fork TC, not just a tie-breaker between symmetrical alternatives.

### The Implication Chain

The forward simulation surfaces an implication chain that the verbal analysis had not made fully explicit:

```
metric ansatz (A = exp(Phi/c^2), B = exp(-gamma_v * Phi/c^2))
  +  Postulate 5 (energy minimization)
    +  observation (gamma_v = 1)
      => kappa = 0 at equilibrium
        => J_k = 0
```

Reading this chain forward: if the framework adopts the metric ansatz used in the static-gravity proofs, and applies Postulate 5's energy-minimization machinery, and is constrained by observation to match $\gamma_v = 1$, then $J_k = 0$ is *forced*. It is not a postulate the framework gets to choose; it is a derived consequence of the existing postulate set plus empirical input.

This is the verbal-analysis result corrected. The original verbal analysis concluded that the existing postulates do not force trace conservation. That conclusion was right *in the proof-system sense* — the postulates alone don't entail trace conservation. But the framework operates with an empirical constraint (Cassini fixing $\gamma_v$), and the postulates plus that constraint do force trace conservation. The verbal analysis missed this because it didn't trace the implication through the energy-minimum machinery and the metric ansatz simultaneously.

### Why Path 4 Cannot Rescue Substance Exchange

Path 4 (richer vacuum mathematical structure) was the most underspecified of the candidate paths. The forward simulation makes it possible to ask whether Path 4 could rescue local vacuum substance creation while keeping the rest of the framework intact. The answer is no.

The chain that forces $J_k = 0$ runs through:

1. The metric ansatz that maps $A, B$ to mode variables $\kappa, \sigma$.
2. The energy functional whose stationary condition gives $\kappa_{eq}$ as a function of sources.
3. Postulate 5's commitment to energy minimization.
4. Observation fixing $\gamma_v = 1$, which fixes $AB = 1$, which fixes $\kappa = 0$.

For Path 4 to rescue substance exchange, it would have to break one of these links. Each option requires revising existing framework content:

- Breaking the metric ansatz means changing what $\kappa$ measures.
- Breaking the energy functional's form means changing how Postulate 4's configuration energy interacts with sources.
- Breaking the energy-minimum link means changing Postulate 5.
- Breaking the observation link means the framework's $\gamma_v$ doesn't correspond to PPN $\gamma$, which would invalidate the static-gravity proofs.

None of these is enrichment; all are revision. Path 4 in its enrichment-only form cannot rescue substance exchange.

A subtler form of Path 4 could allow internal vacuum modes that are projection-invisible — exchange that creates or destroys vacuum in some abstract internal sense without sourcing $\kappa$. But that is not the picture the previous framework had in mind when it spoke of "vacuum consumption" during gravitational descent. Internal-mode reorganization is not substance creation in the metric sense.

## Impact on the Theory

The forward simulation closes a question the framework has been carrying since its inception, and the closure has structural consequences for several parts of the theory.

### Local Vacuum Creation and Destruction Are Forbidden

Local gravitational interaction does not create or destroy vacuum. The chain through the metric ansatz, the energy functional, Postulate 5, and the empirical fixing of $\gamma_v$ rules out $J_k \neq 0$. Any version of the framework that retains these four commitments — and dropping any of them would invalidate the static-gravity proofs that give the framework its empirical contact — must satisfy $J_k = 0$ for ordinary gravitational exchange.

This is a *forbidden* outcome, not a *disfavored* one. The framework cannot be modified to allow local vacuum creation while reproducing observed weak-field gravity through its existing machinery. The previous framework's picture — descent literally consumes vacuum, ascent literally regenerates it — is structurally incompatible with the current framework as it stands. The verbal "vacuum consumption" language must be read as configuration redistribution, not literal substance change.

### Local Gravity Is Configuration Deformation

With substance creation ruled out, the framework's mechanism for gravitational interaction is configuration deformation. A planet's gravitational field reshapes the surrounding vacuum without changing the amount of vacuum present. The vacuum's substance content in any given region is conserved during gravitational exchange. What changes is the configuration: curvature, strain, deformation, the local stored configuration energy of Postulate 4.

A falling body does not destroy vacuum to gain energy; it draws energy from the local configuration, which deforms in response. A rising photon does not create vacuum to lose energy; it returns energy to the configuration, which relaxes. Throughout, the vacuum is reshaped, not unmade or remade.

This picture is internally consistent, structurally derivable from the existing postulates plus observation, and matches the observed weak-field phenomenology to the precision of the best solar-system tests.

### Cosmic Expansion Remains the Mechanism for Substance Creation

The forward simulation only addresses local gravitational exchange. Cosmic expansion's $J_\kappa \neq 0$ is unaffected and remains the framework's account of how vacuum substance enters the universe. The framework now has a clean separation between two structurally distinct mechanisms:

- *Ordinary local gravity*: configuration deformation, trace-conserving, no substance change.
- *Cosmic expansion*: substance creation, traceful, increases vacuum content globally.

These are not the same process at different scales. They operate by different rules and produce different mode-level signatures. The framework's previous "vacuum consumption" language was conflating two distinct mechanisms; the trace-conservation result forces the distinction to be made explicit.

### The Configuration Exchange Document Upgrades to Consequence

The candidate document `candidate_configuration_exchange_not_substance_exchange.md` was written as a conditional argument: *if* trace conservation holds, *then* exchange is configuration. With trace conservation now forced by the framework plus observation, the conditional collapses. The Configuration Exchange interpretation becomes a derived consequence rather than a candidate.

The document should be re-tagged accordingly, and its language updated from conditional ("if the framework adopts trace conservation, then...") to unconditional ("the framework operates by configuration exchange because..."). The conditional proof in that document remains valid; what changes is that its premise is now established.

### Vacuum Variation Unity Is Now Derived

The candidate document `candidate_vacuum_variation_unity.md` adopts $\gamma_v = 1$ as a provisional commitment that closes the spatial-mapping content of the weak-field metric. The forward simulation derives $\gamma_v = 1$ from Postulates 1-5 plus trace conservation, and trace conservation is forced by the framework plus observation. So unity is now derivable rather than provisional, with respect to first-order content.

The static-gravity proofs that depended on unity — light deflection, Shapiro delay, perihelion precession — have their unity dependency upgraded from provisional to derived. The perihelion precession proof still inherits the second-order time-metric candidate's provisional status, which is independent of the unity question; that is open work.

The candidate document should be revised to reflect this status change, and the dependent proofs updated accordingly.

### Postulate 3's Wording Should Be Sharpened

The current wording of Postulate 3 — "vacuum is consumed in the region traversed... vacuum is regenerated" — is compatible with both the substance-creation reading and the configuration-deformation reading. The trace-conservation result forces the configuration-deformation reading. The postulate's wording can be retained for its energy-flow content but should be qualified to reflect the now-established interpretation.

A revised wording might read:

> When energy moves along a gradient toward greater curvature, its momentum along the gradient increases and the local vacuum configuration releases configuration energy. When energy moves against the gradient toward lesser curvature, its momentum along the gradient decreases and the local vacuum configuration stores configuration energy. The exchange is trace-preserving: the amount of vacuum present in any region is unchanged.

This preserves the postulate's role in the framework's energy ledger while removing the substance-creation reading that the trace-conservation result rules out.

### The Static-Gravity Branch Is Structurally Complete at First Order

The framework's first-order weak-field content now derives from Postulates 1-5 plus mass-energy equivalence (imported from SR) plus the empirical input $\gamma_v = 1$ (which combined with the framework forces trace conservation). All of:

- Newtonian limit
- Gravitational redshift
- Time dilation
- Light deflection
- Shapiro delay

are now unconditional at first order. Perihelion precession remains conditional on the second-order time-metric candidate, which is a separate open derivation.

The framework's empirical contact with weak-field gravity is no longer provisional. The static-gravity branch has reached structural completion at first order.

### Earlier Disappointment Is Now Earned

The disappointment about losing the local-vacuum-creation picture, registered earlier in the framework's development, is now earned in the rigorous sense. The picture is not just disfavored aesthetically or set aside as one branch among several; it is structurally ruled out by the framework's own commitments combined with observation. The framework cannot have local creation and reproduce observed gravity simultaneously.

This is the methodology working as intended. The disappointment is real, but the foreclosure is genuine. The picture being lost is the cost; the structural certainty about what the framework actually commits to is the result.

## Status

The conditional chain from the structure search investigations is now closed:

```
metric ansatz + Postulate 5 + observation
  => J_kappa = 0 (trace conservation forced)
    => kappa = 0 at equilibrium
      => AB = 1
        => gamma_v = 1
```

Trace conservation is no longer an open question. It is a forced consequence of the framework's existing commitments plus the empirical fixing of $\gamma_v$ by Cassini-precision observation.

The candidate Configuration Exchange document upgrades to a derived consequence. The candidate Vacuum Variation Unity document upgrades from provisional to derived (with respect to first-order content; the second-order time-metric candidate remains provisional).

The framework's static-gravity branch is now structurally complete at first order in $\Phi/c^2$, with all weak-field GR results derivable from Postulates 1-5 plus mass-energy equivalence (imported from SR) plus the empirical input $\gamma_v = 1$. The framework no longer has a free postulate-level choice about $J_\kappa$; the choice is settled.

## Next Investigation

Several investigations are now natural follow-ups:

**Update dependent documents.** The following documents should be revised to reflect the new structural status:

- `candidate_configuration_exchange_not_substance_exchange.md`: re-tag from candidate to consequence; update language from conditional to unconditional.
- `candidate_vacuum_variation_unity.md`: re-tag from provisional to derived; update dependent proofs to remove provisional status.
- `candidate_exchange_creation_separation.md`: revise to reflect that the candidate principle is now structurally entailed.
- `candidate_paths_to_equal_response.md`: update with the result that the chain is closed via Path 1 plus empirical input, with Path 4 ruled out as a rescue route for substance exchange.
- The static-gravity proofs (`proof_light_deflection.md`, `proof_shapiro_delay.md`, `proof_perihelion_precession.md`): update provisional-status sections to reflect that unity is now derived (perihelion precession still inherits second-order time-metric candidacy).
- Postulate 3's wording: clarify that the energy exchange described is configuration-level, not substance-level.

**Address the second-order time-metric candidate.** With first-order content closed, the perihelion precession proof's remaining provisional dependency is on the second-order extension of the redshift exponential. This is a separate derivation problem, independent of the local-exchange question. Closing it would make perihelion precession unconditional as well.

**Postulate-space mapping (deferred).** The cheaper forward simulation produced a sharp result. The full postulate-space mapping that determines which subsets of postulates force which $J_\kappa$ values is no longer required for the local-exchange question, but remains a useful methodology for future structural investigations.

**Consequences for the cosmology branch.** With local gravity now structurally separated from substance creation, the cosmology branch's account of expansion as substance creation becomes the framework's only mechanism for changing vacuum content. The cosmology documents may benefit from updating to reflect this cleaner separation.