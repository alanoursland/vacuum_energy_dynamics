# Lab Report: P3 Volume Preservation Test

## Experiment

**Script:** `candidate_p3_volume_preservation_test.py`
**Experiment type:** Postulate-derivation analysis (negative result)
**Status:** Exploratory / pedagogical, not formal theory
**Related prior work:**

```text
structure_search_baseline_results.md
structure_search_4d_extension_results.md
log_scale_modes_lab_report.md
log_scale_modes_v2_lab_report.md
kappa_suppression_lab_report.md
```

## Purpose

The purpose of this experiment was to test whether P3's commitment to constant local vacuum energy density forces local exchange operators to preserve volume on configuration space.

The structure search baseline established that volume-preserving exchange operators automatically lie in the trace kernel of the projection map, which produces $J_\kappa = 0$, which produces reciprocal scaling $AB = 1$, which produces $\gamma_v = 1$ in the static spherical exterior weak-field regime. The remaining link in the chain is the connection from existing postulates to the volume-preservation property.

If P3 forces volume preservation, then the trace-kernel constraint on local exchange is a derived consequence of existing framework commitments rather than a separate postulate, and the equal-response problem closes at the postulate level.

The experiment was designed to either confirm this derivation or to identify what is missing.

## Hypothesis

The hypothesis under test was:

```text
P3 (constant local vacuum energy density) forces local exchange operators
to preserve volume on configuration space.
```

The reasoning behind the hypothesis was that P3 says $\rho_v$ is locally constant. If exchange between matter and vacuum changes the configuration but does not change the local density, then the local volume of vacuum exchanged must equal the local volume of vacuum displaced. Volume preservation would follow as a consequence of density constancy.

The intended test was to construct candidate exchange operators, evaluate whether they preserve volume, and identify any operators that violate volume preservation while still satisfying P3's density constancy. If such operators exist, P3 alone does not force volume preservation. If no such operators exist, P3 forces it.

## Setup

The script used SymPy directly rather than VacuumForge's structure search subsystem. The reason for this choice is that the experiment as initially conceived did not require the full structure-search machinery; it required only a symbolic check on the relationship between density constancy and volume preservation.

The script defined pre-mode configuration variables for static spherical 3+1:

$$q_t,\quad q_r,\quad q_\theta,\quad q_\phi.$$

Constant-direction exchange operators were specified by direction coefficients:

$$\delta q_i = e_i \cdot S,$$

with $S$ as the exchange amplitude.

A volume-preservation test was defined in terms of the divergence of the exchange direction field, which vanishes trivially for constant-direction operators. A density-preservation test was defined in terms of the change in $\rho_v$ before and after exchange.

## Results

The script ran to completion and produced a diagnostic output rather than a test result.

The diagnostic output stated that the experiment as conceived collapses for a structural reason that became visible during script construction: P1 and P3 together identify vacuum volume with vacuum energy.

P1 says vacuum is energy. P3 says $\rho_v$ is constant. The combination implies that vacuum energy and vacuum volume are the same quantity, related by the fixed constant $\rho_v$:

$$E_{\text{vacuum}} = \rho_v \cdot V_{\text{vacuum}}.$$

Under this identity, "exchange that preserves volume" and "exchange that preserves local energy" are not two separate conditions to compare. They are the same condition expressed in different units.

The hypothesis "P3 forces volume preservation" therefore does not have a meaningful failure mode within the framework's existing ontology. There is no degree of freedom for an exchange that "doesn't preserve volume" while still being consistent with P1 and P3, because volume *is* energy under the identity. Any exchange that preserves local energy preserves volume by construction; any exchange that does not preserve local energy is not within the regime P1 and P3 describe.

The experiment therefore did not test what it was designed to test. It revealed that the question, as posed, was not well-formed within the framework's commitments.

## Interpretation

The collapse of the question reveals that the actual gap is located one level higher than the experiment was probing.

The structure search baseline established that volume-preserving exchange produces trace-free behavior. The current experiment shows that P1 and P3 together make volume preservation equivalent to local energy conservation. So the chain of logic is:

```text
local exchange that preserves local energy
  → preserves volume (by P1+P3 identity)
  → lies in trace kernel (by structure search baseline)
  → produces J_kappa = 0
  → produces AB = 1
  → produces gamma_v = 1
```

The first link in this chain is the open question. The chain closes if "local exchange" means "interaction that preserves local energy." It does not close if "local exchange" includes interactions that change local energy at the matter location.

The framework's existing postulates do not currently distinguish these two possibilities. P6 commits to vacuum exchange in gradients but does not pin down whether the exchange is local-energy-conserving or whether it can involve net local energy injection or extraction. The substance-regime aspect of P6 explicitly allows kinetic energy changes to be sourced and sunk by vacuum exchange, which involves real energy redistribution between the falling body and the vacuum, but it does not specify whether this redistribution is local-energy-conserving in the sense required for volume preservation at each point.

The actual missing structural commitment is therefore:

```text
Local matter-vacuum exchange in static configurations preserves local energy.
Net local energy change at a point constitutes creation or destruction,
not exchange.
```

This commitment, if added, would close the chain. Without it, P1 through P5 do not force the trace-kernel direction on local exchange operators, and the equal-response result remains conditional on the exterior recovery postulates P7 and P8.

## Why the Experiment Was Not a Forge Experiment

This experiment did not use VacuumForge's structure-search subsystem because the question it was designed to answer turned out to be a definitional question rather than a structural one.

The structure search excels at testing whether candidate operator structures satisfy specified properties under specified projections. It catches tautological commitments, identifies measure-zero constraints, and characterizes the space of derivable consequences from a candidate setup.

The structure search does not directly test definitional collapses. The collapse of "P3 forces volume preservation" happens at the level of what the framework's symbols mean rather than at the level of what operators can do within the framework. P1 and P3 together identify two quantities; no operator-level analysis is needed to see that the identification makes the original hypothesis vacuous.

A forge experiment for the actual remaining gap would need to encode the candidate distinction between exchange and creation as separate operator types, specify what makes each type local-energy-conserving or not, and test whether existing postulates force one type to be trace-free. That would be a genuine structure-search experiment. The current script is a precursor to such an experiment, identifying that the candidate distinction is the right thing to test.

## What Was Established

The experiment established several useful results despite not testing what it was designed to test:

The hypothesis "P3 forces volume preservation" is not well-formed within the framework's existing ontology. P1+P3 identify volume with energy, making volume preservation and energy preservation the same condition.

The trace-kernel constraint on local exchange does not follow from P1 through P5 as currently stated. The structure search baseline showed volume preservation suffices for the trace-kernel constraint, and the current experiment shows that P1+P3 make volume preservation a consequence of local-energy preservation, but no current postulate forces local exchange to be local-energy-preserving.

The actual missing commitment is operational: the framework needs a definition of "local exchange" that distinguishes it from "local creation/destruction." Without this distinction at the postulate level, exchange operators are not constrained to the local-energy-conserving subset, and the trace-kernel constraint does not follow.

The candidate Exchange-Creation Separation principle, identified in earlier process documents, is the natural place where this missing commitment would live. The current experiment supports that principle's status as a candidate by showing that no other current postulate produces the same content.

## What Was Not Established

The experiment did not derive the trace-kernel constraint from existing postulates.

It did not produce a forge-validated structural result; it produced a diagnostic that the question requires reframing.

It did not test candidate definitions of exchange-vs-creation; it identified that such candidate definitions are what the next experiment should test.

It did not close the equal-response gap; it relocated the gap from "P3 → volume preservation → trace-kernel" to "P? → exchange-vs-creation distinction → local-energy-conservation in exchange → volume-preservation → trace-kernel."

## Status of the Experiment

The experiment is closed as a negative result. The hypothesis was not refuted; it was found to be vacuous within the framework's existing commitments. The script's diagnostic output is the appropriate result for this kind of vacuous-question discovery.

The experiment's value lies not in the result it produced but in the reframing it forced. The actual remaining gap is now located more precisely than it was before. Whether this reframing leads to a productive next experiment depends on whether candidate definitions of exchange-vs-creation can be formulated specifically enough to test in the structure search.

## Recommended Next Step

The next experiment should test candidate definitions of the exchange-creation distinction at the operator level.

A possible script:

```text
candidate_exchange_creation_distinction_test.py
```

Suggested approach:

1. Encode P5 in its current form and in candidate strengthenings that distinguish relaxation operators from excitation operators.

2. For each version of P5, ask the structure search whether local exchange (defined via the relaxation classification) is forced to be local-energy-conserving.

3. If any candidate strengthening produces this force, examine whether the strengthening can be motivated from existing framework commitments or whether it must be adopted as a new postulate.

4. If no candidate strengthening produces this force from P1-P5 alone, then the exchange-creation distinction must be adopted as a new structural postulate, and the framework's open postulate list grows by one.

A complication identified after the script ran: the formalization of exchange-vs-creation may depend on the formalization of mass-as-constraint, which is currently conceptual rather than mathematical in the framework. If "exchange" is defined as "operator that relaxes the configuration toward its minimum-energy state given prevailing constraints," then the meaning of "exchange" depends on what the constraints are, which depends on how mass imposes constraints. Without mass-as-constraint formalized, exchange-vs-creation may not be sharply definable.

This complication suggests that the next productive experiment may not be the exchange-creation test directly but rather a precursor: a substance-regime experiment in regions away from mass, where mass-as-constraint is not needed because no mass is present. Gravitational wave propagation in empty regions is a candidate. If substance-regime dynamics can be developed in empty regions first, the resulting structure may constrain how mass-as-constraint should be formalized when it is added.

## Reproduction

In `vacuum_energy_dynamics/vacuum_forge/src`:

```
python scripts_v3/candidate_p3_volume_preservation_test.py
```

The script prints a diagnostic explaining why the question reformulates rather than testing the original hypothesis. No external dependencies beyond SymPy.

## Connection to Existing Process Documents

This experiment confirms a structural feature already present in the candidate Exchange-Creation Separation work but not previously connected to the volume-preservation route from the structure search baseline.

The baseline report's "What the Structure Search Does Not Show" section listed three possible directions for the remaining question, including "the trace-kernel direction may correspond to *energy-bookkept exchange* in a specific sense." The current experiment identifies that this direction is not one possible interpretation among several, but the only interpretation consistent with P1+P3. Volume preservation, conformal-content preservation, and local-energy-conservation are the same property under the framework's existing identifications, all expressing the trace-kernel constraint in different language.

This unifies several previously distinct candidate principles into one underlying structural commitment. Whether that commitment can be derived from the existing postulates or must be adopted as a new postulate is the open question this experiment leaves to the next stage.
