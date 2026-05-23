# Candidate Volume Form Configuration Variable

## Canonical Filename

```text
candidate_volume_form_configuration_variable.md
```

This document summarizes the output of:

```text
candidate_volume_form_configuration_variable.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a covariant theory of vacuum configuration, not a parent identity, and not a proof of TT-only radiation. It does not add a formal commitment to the theory.

Its purpose is to test whether vacuum-spacetime configuration can be represented by a volume-form variable.

The guiding question was:

```text
Can vacuum-spacetime configuration be represented by a volume-form variable?
```

The answer is:

```text
The best current geometric candidate is:
  zeta = ln sqrt(gamma)

with:
  dV_phys = sqrt(gamma) d^3x
  delta zeta = 1/2 gamma^ij delta gamma_ij
  delta zeta|TT = 0

Interpretation:
  trace / volume modes change vacuum-spacetime amount,
  TT modes are volume-preserving shear.
```

---

## Why This Study Matters

The group-13 inventory found that \(E_{\rm vac,config}\) must be geometric or tightly constrained bookkeeping.

The best immediate geometric candidates were:

\[
\sqrt{\gamma}
\]

and:

\[
\ln\sqrt{\gamma}.
\]

This study tests those candidates.

The key result is not full covariance.

The key result is the linear structural observation:

```text
TT modes are trace-free,
therefore TT modes preserve volume at linear order.
```

That makes \(\zeta=\ln\sqrt{\gamma}\) a promising candidate for the scalar / trace conversion variable.

---

## Compact Volume-Form Ledger

| Candidate | Role | Status | Forbidden Use | Missing |
|---|---|---|---|---|
| \(dV_{\rm phys}=\sqrt{\gamma}\,d^3x\) | geometric expression of local vacuum / spacetime amount in a chosen slice | CANDIDATE | treated as gauge-invariant observable without slicing / frame definition | choice of spatial metric \(\gamma_{ij}\) and foliation / frame |
| \(\zeta=\ln\sqrt{\gamma}\) | additive local trace / volume configuration variable | CANDIDATE | duplicate \(A\)-sector mass response or exterior scalar charge | reference volume / background subtraction and relation to \(\kappa\) |
| \(\delta\zeta=\frac12\gamma^{ij}\delta\gamma_{ij}\) | shows that volume change is trace part of spatial metric perturbation | STRUCTURAL | allowing trace to source \(h_{TT}\) or scalar radiation | parent projector \(P_{\rm trace}\) |
| \(\gamma^{ij}h_{ij}^{TT}=0\Rightarrow \delta\zeta|_{TT}=0\) | candidate reason TT modes propagate without vacuum creation / destruction | CANDIDATE | claiming theorem before parent projector derivation | full nonlinear / covariant statement and TT source identity |
| \(ds=e^\phi dx\), so \(\zeta_{1D}=\phi\) | concrete analog: local expansion field multiplies physical length | STRUCTURAL | importing the toy's irreversible reservoir \(R\) as theory | higher-dimensional generalization and conservative exchange law |
| \(\kappa\sim\zeta-\zeta_{\min}\) or \(\kappa=\frac12\ln(AB)\) in reduced areal gauge | relates \(\kappa\) to volume / trace mismatch rather than independent scalar field | CANDIDATE | \(\kappa\) as \(\rho\)-sourced exterior scalar charge | precise map between \(\kappa\) and volume-form strain |
| \(\epsilon_{\rm vac,config}=F(\zeta,\zeta_{\min},\nabla\zeta,\ldots)\) | geometric local configuration density built from volume strain | CANDIDATE | bottomless reservoir or coefficient tuning functional | functional form \(F\) and stiffness coefficients |
| \(M_{\rm ext}\) determined by \(A_{\rm flux}\), not \(\int\zeta\) | protects exterior mass from volume-form relaxation | CONSTRAINED | using volume strain integral to alter exterior mass | boundary volume mode no exterior charge theorem |
| \(\zeta_{\rm ext}\to0,\;\kappa_{\rm ext}\to0,\;Q_{\rm volume}=0\) | prevents volume-form scalar tail outside ordinary matter | CONSTRAINED | \(\zeta_{\rm ext}\sim1/r\) scalar charge | projection / boundary theorem |
| \(\zeta=\ln\sqrt{\gamma}\) depends on spatial decomposition | flags that volume-form accounting needs a frame / foliation or covariant replacement | UNRESOLVED | pretending \(\zeta\) is fully covariant without extra structure | frame \(u^\mu\), foliation, or covariant volume current |

---

## Status Counts

The run counted:

```text
CANDIDATE:    5
CONSTRAINED:  2
STRUCTURAL:   2
UNRESOLVED:   1
```

Interpretation:

```text
The volume-form candidate is promising but not covariant yet.
The key structural fact is that TT perturbations are trace-free, hence volume-preserving at linear order.
The key risk is duplicating A-sector scalar mass response.
```

---

## Minimal Candidate Definition

Minimal candidate:

\[
\zeta=\ln\sqrt{\gamma}.
\]

Physical volume element:

\[
dV_{\rm phys}
=
\sqrt{\gamma}\,d^3x.
\]

Perturbative variation:

\[
\delta\zeta
=
\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

TT perturbation:

\[
\gamma^{ij}h_{ij}^{TT}=0.
\]

Therefore:

\[
\delta\zeta\big|_{TT}=0.
\]

Interpretation:

```text
trace / volume modes change vacuum-spacetime amount,
TT modes are volume-preserving shear.
```

Status:

```text
LINEAR STRUCTURAL OBSERVATION / NOT FULL THEOREM
```

---

## Relation To The 1D Toy Model

The 1D toy has:

\[
ds=e^\phi dx.
\]

Therefore:

\[
\phi=\ln(ds/dx).
\]

This is the 1D analog of:

\[
\zeta=\ln\sqrt{\gamma}.
\]

Useful extraction:

```text
physical length / volume is coordinate measure multiplied by a vacuum-configuration factor.
```

Rejected extraction:

```text
a one-way thermodynamic reservoir R as final theory.
```

Reinterpreted extraction:

```text
scalar / trace conversion changes the geometry / volume-form variable itself.
```

---

## Failure Controls

The volume-form candidate fails if:

1. \(\zeta\) duplicates \(A\)-sector exterior mass.
2. \(\zeta\) produces an exterior \(1/r\) scalar tail.
3. \(\zeta\) is treated as gauge-invariant without frame / foliation.
4. \(\kappa\) and \(\zeta\) become independent scalar charges.
5. TT modes accidentally change volume.
6. Scalar conversion becomes far-zone scalar radiation.
7. \(\epsilon_{\rm vac,config}\) becomes a coefficient tuning reservoir.

---

## What This Study Established

This study established the best current geometric candidate:

\[
\zeta=\ln\sqrt{\gamma}.
\]

It also established the core linear split:

\[
\delta\zeta
=
\frac12\gamma^{ij}\delta\gamma_{ij},
\]

and:

\[
\delta\zeta\big|_{TT}=0.
\]

This makes \(\zeta\) a promising candidate for the scalar / trace conversion variable and makes TT modes promising candidates for volume-preserving shear.

---

## What This Study Did Not Establish

This study did not derive a covariant volume variable.

It did not define the frame / foliation.

It did not prove the nonlinear TT-only radiation theorem.

It did not derive the parent projectors.

It did not relate \(\kappa\) exactly to \(\zeta\).

It did not prove exterior volume-mode neutrality.

It only identified a strong geometric candidate.

---

## Current Best Interpretation

The best current geometric candidate is:

```text
zeta = ln sqrt(gamma)
```

with:

```text
dV_phys = sqrt(gamma) d^3x,
delta zeta = 1/2 gamma^ij delta gamma_ij,
delta zeta|TT = 0.
```

Interpretation:

```text
trace / volume modes change vacuum-spacetime amount,
TT modes are volume-preserving shear.
```

---

## Next Development Target

The next script should be:

```text
candidate_trace_vs_tt_geometric_split.py
```

Purpose:

```text
Formalize why trace / volume modes convert while TT modes propagate.
```

Reason:

```text
The volume-form candidate points directly to the trace / TT split as the possible TT-only radiation theorem.
```

Expected result:

```text
A trace-vs-TT ledger:
  trace perturbations change zeta,
  TT perturbations preserve zeta at linear order,
  scalar/trace modes are candidates for vacuum-spacetime conversion,
  TT modes are candidates for propagating shear,
  limitations from slicing/frame and nonlinear corrections are marked.
```

---

## Summary

The volume-form candidate is the first strong geometric handle on \(E_{\rm vac,config}\).

The next goblin gate is:

```text
Can the trace / TT split explain scalar conversion and TT-only radiation?
```
