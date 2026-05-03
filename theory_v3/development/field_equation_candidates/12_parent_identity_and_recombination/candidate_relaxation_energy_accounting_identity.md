# Candidate Relaxation Energy Accounting Identity

## Canonical Filename

```text
candidate_relaxation_energy_accounting_identity.md
```

This document summarizes the output of:

```text
candidate_relaxation_energy_accounting_identity.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a parent identity, not a final energy theorem, and not a complete definition of vacuum-substance energy. It does not add a formal commitment to the theory.

Its purpose is to state the energy-accounting requirement for \(\Gamma_{\rm relax}\) and \(\kappa\) relaxation.

The guiding question was:

```text
Where does relaxation energy go?
```

The answer is:

```text
Relaxation energy accounting requires:
  Gamma_relax is exchange / restoration, not destruction,
  E_kappa has a local free-energy form,
  local relaxation is monotonic,
  total ordinary closed-regime accounting is conserved,
  exterior M_ext is preserved,
  Sigma_creation remains zero,
  no kappa momentum / radiation channel appears,
  E_vac_config or equivalent must be defined.
```

---

## Interpretation Update: Vacuum Substance Exchange

A better interpretation is:

```text
curvature relaxation exchanges with vacuum substance.
```

More specifically:

```text
curvature excess relaxes into vacuum-substance configuration,
curvature deficit pulls from vacuum-substance configuration,
and the exchange moves the local curvature / volume state toward its minimum.
```

This means \(\Gamma_{\rm relax}\) should not be read as dissipation out of the system.

It should be read as an internal exchange term between:

```text
curvature / kappa imbalance
```

and:

```text
vacuum-substance configuration energy.
```

A curvature deficit can therefore be modeled as a demand on the vacuum substance:

```text
vacuum configuration energy is converted into curvature / volume restoration,
lowering the deficit.
```

A curvature excess can be modeled as the reverse:

```text
curvature / volume imbalance is converted into vacuum-substance configuration energy.
```

The exchange should be monotonic toward the local minimum, but the total accounting must remain closed in the ordinary regime.

---

## Why This Study Matters

The recombination audit constrained the geometry map.

But it left a hole:

```text
Gamma_relax has no named energy destination.
```

If \(\Gamma_{\rm relax}\) removes energy without a destination, it becomes cosmetic damping.

That would violate the ordinary closed-regime rule:

\[
\Sigma_{\rm creation}=0.
\]

Therefore the relaxation channel must be internal exchange.

---

## Compact Relaxation Energy Ledger

| Requirement | Candidate Form | Forbidden Form | Status | Missing |
|---|---|---|---|---|
| E1: relaxation is exchange, not destruction | \(\Gamma_{\rm relax}\to dE_{\rm vac,config}/d\tau\) | \(\Gamma_{\rm relax}\) removes energy with no destination | REQUIRED | definition of \(E_{\rm vac,config}\) |
| E2: \(\kappa\) relaxation has an energy functional | \(E_\kappa=\frac12K_\kappa(\kappa-\kappa_{\min})^2\) | first-order relaxation without stored / free energy | CANDIDATE | derivation of \(K_\kappa\) and measure / volume element |
| E3: monotonic local relaxation but conserved total accounting | \(dE_\kappa/d\tau\le0\), while \(dE_{\rm total}/d\tau=0\) in ordinary closed regime | local damping interpreted as total energy loss | REQUIRED | destination reservoir and total balance identity |
| E4: exterior mass remains fixed under relaxation | \(\delta M_{\rm ext}|_{\Gamma_{\rm relax}}=0\) for internal trace relaxation | relaxation changes exterior \(1/r\) coefficient without source flux | CONSTRAINED | boundary mass / energy separation theorem |
| E5: ordinary closed regime excludes creation | \(\Sigma_{\rm creation}=0\); \(\Gamma_{\rm relax}\) internal exchange only | \(\Gamma_{\rm relax}\) creates / destroys net vacuum energy in ordinary regime | CONSTRAINED | active / ordinary regime separation |
| E6: trace minimum stores configuration displacement | \(\kappa_{\min}=\chi_\kappa S_{\rm trace,effective}\); \(E_\kappa\) centered at \(\kappa_{\min}\) | trace source pumps \(\Box\kappa\) radiation | STRUCTURAL | source law for \(S_{\rm trace,effective}\) and \(\chi_\kappa\) |
| E7: no \(\kappa\) momentum reservoir | no \(\frac12(u^\mu\nabla_\mu\kappa)^2\) propagating energy term | second-order oscillator / sloshing \(\kappa\) channel | CONSTRAINED | parent reason for non-inertial \(\kappa\) |
| E8: vacuum configuration variable must be named | \(E_{\rm vac,config}[A,\kappa,\text{boundary},q_v]\) or \(q_v/J_v\) balance | unnamed reservoir invoked only when needed | MISSING | definition of \(q_v,E_{\rm vac,config}\), or equivalent |
| E9: recombination must not double-count relaxation energy | \(\rho\to A\) mass flux; trace displacement \(\to E_{\rm vac,config}/\kappa\) sector | same stress energy contributes independently to \(A\) mass and \(\kappa\) stored energy as exterior charge | REQUIRED | parent source decomposition and recombination accounting |
| E10: near-boundary smoothing energy remains diagnostic | \(E_{\rm joint}\) diagnostic with fixed \(M_{\rm ext}\) and no prediction claim | boundary smoothing energy predicts measurable deviation without weights / recombination | CONSTRAINED | weights, \(\sigma\), observable map, closure |

---

## Status Counts

The run counted:

```text
CANDIDATE:    1
CONSTRAINED:  4
MISSING:      1
REQUIRED:     3
STRUCTURAL:   1
```

Interpretation:

```text
A kappa free-energy form is plausible but not derived.
The missing object is the vacuum configuration energy variable / reservoir.
The accounting must preserve exterior mass and ordinary closed-regime conservation.
```

---

## Candidate Local Free-Energy Form

Candidate local free-energy form:

\[
E_\kappa
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Candidate relaxation:

\[
u^\mu\nabla_\mu\kappa
=
-\mu_\kappa
\frac{\partial E_\kappa}{\partial\kappa}.
\]

This gives:

\[
u^\mu\nabla_\mu\kappa
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

Local monotonicity:

\[
\frac{dE_\kappa}{d\tau}
=
-\mu_\kappa
\left(
\frac{\partial E_\kappa}{\partial\kappa}
\right)^2
\le0.
\]

But the lost local free energy must go somewhere:

\[
\frac{dE_{\rm vac,config}}{d\tau}
=
-\frac{dE_\kappa}{d\tau}.
\]

This is candidate accounting, not yet a parent identity.

---

## Deficit / Excess Exchange Reading

Let:

\[
\Delta\kappa=\kappa-\kappa_{\min}.
\]

Then:

```text
Delta kappa > 0:
  curvature / volume state is above its local minimum.
  relaxation transfers excess into vacuum-substance configuration.

Delta kappa < 0:
  curvature / volume state is below its local minimum.
  vacuum-substance configuration supplies the deficit,
  pulling the system toward the minimum.
```

In both cases:

\[
\Delta\kappa\to0.
\]

No momentum channel is introduced.

There is no sloshing.

There is no breathing wave.

There is only first-order exchange toward the local minimum.

---

## Required Total Balance

Ordinary closed-regime target:

\[
\frac{d}{d\tau}
\left(
E_{\rm matter}
+
E_A
+
E_W
+
E_{TT}
+
E_\kappa
+
E_{\rm vac,config}
\right)
=
0.
\]

with:

\[
\Sigma_{\rm creation}=0,
\]

\[
\delta M_{\rm ext}\big|_{\Gamma_{\rm relax}}=0
\]

for internal relaxation,

\[
A_{\rm rad}=0,
\]

and no:

\[
\Box\kappa.
\]

This is a requirement, not a derivation.

---

## Failure Controls

Relaxation energy accounting fails if:

1. \(\Gamma_{\rm relax}\) removes energy with no destination.
2. \(E_{\rm vac,config}\) is unnamed or only invoked as a repair reservoir.
3. Relaxation changes exterior \(M_{\rm ext}\).
4. \(\Gamma_{\rm relax}\) acts like \(\Sigma_{\rm creation}\) in ordinary gravity.
5. \(\kappa\) gains a kinetic / momentum channel and becomes radiative.
6. Trace minimum energy is counted again as \(A\)-sector exterior mass.
7. Boundary smoothing energy is advertised as prediction before closure.

---

## What This Study Established

This study established that \(\Gamma_{\rm relax}\) must be internal exchange.

It also established that the natural exchange destination is:

```text
vacuum-substance configuration energy.
```

A useful candidate is:

\[
E_\kappa=\frac12K_\kappa(\kappa-\kappa_{\min})^2,
\]

with first-order gradient relaxation and compensating change in \(E_{\rm vac,config}\).

The physical interpretation is:

```text
curvature excess relaxes into vacuum substance,
curvature deficit pulls from vacuum substance,
and both move toward the local minimum without sloshing.
```

---

## What This Study Did Not Establish

This study did not define \(E_{\rm vac,config}\).

It did not define \(q_v\) or \(J_v\).

It did not derive \(K_\kappa\).

It did not derive the measure / volume element.

It did not derive total energy conservation.

It did not derive the parent identity.

It only stated the accounting requirements.

---

## Current Best Interpretation

Relaxation energy accounting requires:

```text
Gamma_relax is exchange / restoration, not destruction.
E_kappa has a local free-energy form.
Local relaxation is monotonic.
Total ordinary closed-regime accounting is conserved.
Exterior M_ext is preserved.
Sigma_creation remains zero.
No kappa momentum / radiation channel appears.
E_vac_config or equivalent must be defined.
```

Your phrasing is probably the right ontology-native interpretation:

```text
curvature relaxation goes into vacuum substance;
curvature deficit pulls from vacuum substance to reduce the deficit.
```

---

## Next Development Target

The next script should be:

```text
candidate_parent_identity_template_v2.py
```

Purpose:

```text
Attempt a tighter parent identity scaffold using exclusions, projectors,
recombination, and relaxation-energy accounting.
```

Reason:

```text
The missing energy variable is named;
now update the parent scaffold with all group-12 constraints.
```

Expected result:

```text
A second parent-identity scaffold that includes:
  forbidden-parent exclusions,
  reduced-sector implications,
  projector routing,
  scalar non-radiation,
  kappa first-order relaxation,
  boundary mass preservation,
  recombination no-double-counting,
  relaxation energy exchange with vacuum substance.
```

---

## Summary

The relaxation channel should be interpreted as vacuum-substance exchange.

It is not energy deletion.

It is not scalar radiation.

It is not a momentum channel.

It is first-order restoration toward a local minimum, with the imbalance exchanged against vacuum-substance configuration.
