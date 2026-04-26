# Structure Search: Local Exchange Forward Simulation

## What This Document Is

This is a pre-lab document. It describes a planned VacuumForge investigation of the framework's commitment to $J_\kappa$ for local gravitational exchange, before the experiment is run. The structure of the document follows the chemistry pre-lab convention: state the position in the larger investigation, describe the experimental setup and the methodology in concrete terms, identify what the experiment can and cannot establish, and reserve placeholders for results that will be filled in once the experiment is conducted.

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

This investigation tests that verbal-analysis conclusion computationally. By running the framework forward under each value of $J_\kappa$, it determines whether the existing postulates *actually* leave $J_\kappa$ undetermined or whether they have hidden commitments that the verbal analysis missed.

## Hypothesis

Three outcomes are possible.

**Outcome A: Both forks are consistent.** The existing postulates leave $J_\kappa$ undetermined. Choosing $J_\kappa = 0$ or $J_\kappa \neq 0$ produces two internally consistent extensions of the framework. The framework's current predictive content does not depend on the choice; closing the question requires either additional postulates or richer ontological structure.

**Outcome B: One fork produces a contradiction.** The existing postulates have already silently committed to one $J_\kappa$ value. Adopting the other value contradicts existing framework content. This would surface a hidden commitment the verbal analysis had not noticed.

**Outcome C: The forks differ in predictive content.** Both forks are internally consistent but produce different predictions for some derivable observable. The choice between them becomes empirically testable.

The verbal analysis strongly suggests Outcome A. The methodology designed in response to the previous framework's collapse is built precisely to surface cases that look like Outcome A but are secretly Outcome B. This investigation is an audit against that failure mode.

## Experimental Design

### Setup

Two TheoryContext instances are constructed, identical in their commitment to Postulates 1-5 and their derived consequences, differing only in their commitment to $J_\kappa$ for local gravitational exchange.

**Fork TC: trace conservation fork.** Postulates 1-5 plus the additional commitment $J_\kappa = 0$ for local exchange. This is the postulate state under which the Configuration Exchange interpretation becomes load-bearing.

**Fork SE: substance exchange fork.** Postulates 1-5 plus the additional commitment $J_\kappa \neq 0$ for local exchange. This is the postulate state in which ordinary gravitational interaction creates and destroys vacuum substance locally.

The cosmic expansion consequence retains $J_\kappa \neq 0$ in both forks; that commitment is independent of the local-exchange question. What differs between the forks is only the local-exchange behavior.

### Operations Per Fork

For each fork, the investigation runs the framework's existing derivations through VacuumForge under the strengthened postulate set. The derivations to be re-checked include, at minimum:

- The Newtonian limit derivation from Postulate 3.
- The gravitational redshift derivation.
- The gravitational time dilation derivation.
- The weak-field metric construction.
- The light deflection derivation.
- The Shapiro delay derivation.
- The weak-field equations of motion.
- The perihelion precession derivation.
- The cosmic expansion consequence.

For each derivation, the analysis records:

1. **Closure.** Does the derivation still close under the strengthened postulate set?
2. **Route.** Does it close through the same logical chain as the original derivation, or through a different chain enabled or required by the strengthened postulate?
3. **New theorems.** Does any previously open or provisional result become derivable?
4. **Contradictions.** Does any existing framework content become inconsistent with the strengthened postulate set?
5. **Predictive divergence.** Does the strengthened fork produce a different prediction for any observable than the other fork?

The output is a comparison table: for each derivation and each fork, the status of items 1-4. Item 5 is reported separately as a list of distinguishing predictions, if any.

### VacuumForge Implementation Notes

The investigation should be implemented as a single experiment script (suggested filename `e5.py`) following the pattern established by `e1.py` through `e4c.py`.

The TheoryContext API supports adding derived assumptions to a context. The two forks are constructed by:

```python
ctx_tc = TheoryContext("trace_conservation_fork")
ctx_tc.define_equal_response_algebraic_symbols()
ctx_tc.assume("J_kappa_local = 0", justification="forked postulate")

ctx_se = TheoryContext("substance_exchange_fork")
ctx_se.define_equal_response_algebraic_symbols()
ctx_se.assume("J_kappa_local != 0", justification="forked postulate")
```

The exact API for asserting the forked postulate may differ; the implementer should consult the M35 theorem-candidate system and the M26 model-comparison capabilities, both of which are listed in the VacuumForge feature set as supporting this kind of operation.

The derivations to be re-run are encoded in the framework's existing proof scripts. The investigation should call them under each TheoryContext and capture the dependency tracker's output, the requirement-validation output, and any contradictions surfaced during execution.

The structure search analyzer is *not* the primary tool for this investigation. The structure search asks whether a specific structure produces trace-free exchange. This investigation asks what the framework's existing derivations look like under each fork, which is a different question. The dependency-tracking and requirement-validation machinery (M1-M18) are the load-bearing components.

### Reporting Format

The investigation produces a comparison report in three sections:

**Section A: Per-derivation comparison.** A table with rows for each derivation and columns for each fork, showing closure status and route. Cells should distinguish:

- *closes-original*: derivation closes through its original chain.
- *closes-new*: derivation closes through a different chain enabled by the fork.
- *fails*: derivation does not close under this fork.
- *contradicts*: a contradiction is surfaced during the derivation under this fork.

**Section B: Newly derivable theorems.** For each fork, results that were previously open or provisional but become derivable. Specifically, this should report whether $\gamma_v = 1$ becomes derivable in Fork TC (it should, by the conditional chain), and whether any other provisional commitment is closed.

**Section C: Predictive divergences.** Predictions that differ between forks. The most likely candidate is gravitational wave polarization (scalar mode admissibility), but other possibilities include strong-field corrections to the Schwarzschild form, cosmological accumulation rates, and behavior at the boundary between local-gravity and cosmic-expansion regimes.

If no predictive divergences are found within the framework's current derivable scope, this should be reported explicitly as a finding: the framework's predictive content does not currently distinguish the forks.

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

The investigation's output sharpens the framework's self-knowledge but does not resolve the open question. Resolution requires either additional postulates, richer ontological structure (Path 2 / Path 4), or empirical input distinguishing the forks predictively.

## Relation to Adjacent Documents

This investigation extends the structure-search line:

- `structure_search_baseline_results.md` — established that trace-free exchange is non-generic in 2D.
- `structure_search_4d_extension_results.md` — corrected this to a codimension-1 conservation law in any dimension and identified the static spherical $e_t + e_s = 0$ form.
- `structure_search_local_exchange.md` — *this document.* Forward simulation under each $J_\kappa$ value to map the framework's commitments.

This investigation also activates the candidate documents:

- `candidate_configuration_exchange_not_substance_exchange.md` — the physical interpretation of $J_\kappa = 0$. If Fork TC produces no contradictions and yields $\gamma_v = 1$ as derivable, the Configuration Exchange interpretation becomes load-bearing whenever the framework adopts trace conservation.
- `candidate_paths_to_equal_response.md` — the path enumeration. The current investigation is technically not Path 1 (which would derive trace conservation from existing postulates), nor Path 3 (which would adopt it as a postulate). It is *prerequisite* to choosing among paths: it determines whether the existing postulates already settle the question.

## Pre-Registration

The pre-lab convention asks the experimenter to commit, before running the experiment, to what would count as which outcome. This serves two purposes: it prevents post-hoc reinterpretation of the results, and it forces explicit articulation of what the experiment is actually testing.

For this investigation, the pre-registration is:

**Outcome A is registered if:** Both forks complete all derivations without contradiction, with closures through the same routes as the originals. No new theorems become derivable in either fork beyond those expected from the trace-conservation chain in Fork TC. No predictive divergences are surfaced within the framework's current derivable scope.

**Outcome B is registered if:** One fork produces a contradiction during execution of an existing derivation. The contradiction surfaces a hidden commitment in the existing postulates that the verbal analysis had not identified.

**Outcome C is registered if:** Both forks complete consistently but produce different predictions for some derivable observable. The divergence is explicitly identified and a candidate observation that would distinguish them is named.

If the investigation surfaces something not anticipated by the three outcomes — a partial contradiction, an inconsistency in the framework that doesn't track the fork distinction, a derivation that fails under both forks — that should be reported as a *fourth* outcome and treated as a finding about the framework's current state independent of the $J_\kappa$ question.

## Reproduction

The experiment will be implemented as `e5.py` in `vacuum_energy_dynamics/vacuum_forge/src/scripts/`. Reproduction:

```
PYTHONPATH=src python src/scripts/e5.py
```

The script's output should be machine-readable enough to be incorporated into the results section of this document directly, with human interpretation added.

## Results

*To be filled in after the experiment is run. The structure of this section will mirror the experimental design's reporting format: Section A (per-derivation comparison table), Section B (newly derivable theorems), Section C (predictive divergences).*

### Section A: Per-Derivation Comparison

*Placeholder for comparison table.*

### Section B: Newly Derivable Theorems

*Placeholder for newly derivable results in each fork.*

### Section C: Predictive Divergences

*Placeholder for distinguishing predictions, if any.*

## Interpretation

*To be filled in after results are available. The interpretation should explicitly address which of the pre-registered outcomes was observed and what that outcome implies for the framework's next move.*

## Status

*To be filled in after the experiment is run. The conditional chain to Equal-Response and the framework's options for closing it should be updated based on what the investigation establishes.*

## Next Investigation

*To be determined based on results. Likely candidates include:*

- *If Outcome A: postulate-space mapping (the larger investigation deferred during planning), or pursuit of Path 2 (richer vacuum mathematical structure), or pursuit of Path 1 in its strengthened-postulate form (test whether candidate structural assumptions force trace conservation).*
- *If Outcome B: revision of the postulate set to remove the hidden commitment, or acknowledgment that the framework has already settled the question and the candidate documents need to be aligned accordingly.*
- *If Outcome C: identification of an experimental test that would distinguish the forks observationally.*
