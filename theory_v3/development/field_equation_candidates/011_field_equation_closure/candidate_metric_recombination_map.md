# Candidate Metric Recombination Map

## What This Document Is

This document is a development note for the `11_field_equation_closure/` group.

It is not a final covariant metric derivation, not a completed parent geometry, and not a proof that the sector map reconstructs GR. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_metric_recombination_map.py
```

The guiding question was:

```text
How do A, W_i, h_ij^TT, and kappa recombine into one metric-like object?
```

The answer is:

```text
The current recombination map is a reduced bookkeeping ansatz:

  g_tt from A,
  g_0i from W_i,
  g_ij from scalar spatial response, constrained kappa trace role, and h_ij^TT.

It is not yet a covariant parent derivation.
```

The two key risks are:

```text
scalar double-counting,
silent GR import.
```

---

## Why This Study Matters

The field-equation closure inventory showed that the current theory has a disciplined sector split, but not a completed field-equation closure.

Once sectors are identified, the next danger is recombination.

A theory can look successful if each sector is assigned a familiar GR-shaped role. But unless the recombination is controlled, this can become:

```text
GR metric form imported by hand,
with vacuum-language labels attached.
```

This study prevents that by marking each metric piece explicitly.

---

## Reduced Metric Ansatz

The schematic weak/reduced recombination is:

\[
ds^2
=
-Ac^2dt^2
+
2W_i c\,dt\,dx^i
+
\gamma_{ij}dx^idx^j.
\]

with:

\[
\gamma_{ij}
=
\gamma_{ij}^{\rm scalar}(A,\kappa)
+
h_{ij}^{TT}.
\]

Status:

```text
STRUCTURAL — normalizations and signs not final.
```

This is a bookkeeping ansatz.

It is not yet a covariant parent derivation.

---

## Component Ledger

| Component | Schematic Form | Sector Source | Status | Main Risk | Missing |
|---|---|---|---|---|---|
| \(g_{tt}\) | \(-Ac^2\) | \(A\)-sector scalar monopole / lapse response | DERIVED_REDUCED | Overextending static spherical scalar result into all regimes | Full nonlinear nonspherical parent map |
| \(g_{rr}\) / radial scalar piece | \(B=e^{2\kappa}/A\) in reduced areal gauge | \(A\) plus \(\kappa\) diagnostic | DERIVED_REDUCED | Treating areal-gauge relation as fully covariant | Gauge-invariant interpretation of \(\kappa\) and \(B\) |
| \(g_{0i}\) | proportional to \(W_i\) | transverse vector current sector | STRUCTURAL | Normalization and sign imported from GR | Observable coupling and covariant shift-vector map |
| \(g_{ij}\) scalar trace | scalar spatial response tied to \(A\), plus constrained \(\kappa\) trace role | \(A\)-sector spatial response plus \(\kappa\) relaxation | CONSTRAINED | Double-counting scalar trace response or turning \(\kappa\) into scalar gravity | No-double-counting rule and parent decomposition |
| \(g_{ij}^{TT}\) | \(\delta_{ij}+h_{ij}^{TT}\) in weak radiation limit | tensor TT radiation sector | STRUCTURAL | Correct TT form but coupling/source identity not derived | Tensor coupling normalization and action stiffness |
| forbidden scalar radiation | no ordinary long-range \(A_{\rm rad}\) or \(\kappa\) breathing wave | scalar radiation safety constraint | CONSTRAINED | Hidden scalar mode reappears through recombination | Parent mechanism enforcing scalar-radiation absence |

---

## Kappa Recombination Rule

\(\kappa\) may enter recombination through the diagnostic relation:

\[
AB=e^{2\kappa}.
\]

It may also represent constrained trace / volume relaxation.

But \(\kappa\) must not be treated as:

```text
an independent long-range scalar potential,
an ordinary massless breathing-wave field,
a duplicate source of rho.
```

Preferred rule:

```text
kappa modifies trace/volume matching and interior/boundary relaxation,
while exterior kappa -> 0 and F_kappa(R+) = 0.
```

Status:

```text
CONSTRAINED — parent/gauge split missing.
```

This is currently a safety rule, not a covariant derivation.

---

## Recombination No-Double-Counting Rules

The run stated these recombination rules:

1. \(A\) carries the long-range scalar mass response from \(\rho\).
2. \(\kappa\) does not carry an independent long-range \(\rho\)-sourced scalar field.
3. \(W_i\) carries transverse current response; longitudinal current remains scalar continuity.
4. \(h_{ij}^{TT}\) carries trace-free tensor radiation.
5. Trace / pressure may shift \(\kappa_{\min}\), but must not source propagating scalar radiation.
6. Spatial scalar response tied to \(A\) must not be duplicated by \(\kappa\).
7. Near-boundary \(\kappa\) smoothing must not change total exterior mass flux by hand.

Status:

```text
CONSTRAINED
```

These rules should be carried forward into the source-decomposition ledger.

---

## GR Import Risks

High-risk imports:

```text
g_0i normalization from frame dragging,
tensor coupling 16*pi*G/c^4,
radiation energy coefficient c^3/(32*pi*G),
spatial gamma=1 beyond weak scalar derivation,
Bianchi/conservation identity.
```

These are allowed as targets.

They should not be claimed as ontology-derived unless the vacuum-curvature-exchange structure forces them.

Status:

```text
RISK — targets are not derivations.
```

This is one of the most important closure warnings.

---

## Classification

The script produced this classification:

| Component | Status |
|---|---|
| \(g_{tt}\) | DERIVED_REDUCED |
| \(g_{rr}\) / radial scalar piece | DERIVED_REDUCED |
| \(g_{0i}\) | STRUCTURAL |
| \(g_{ij}\) scalar trace | CONSTRAINED |
| \(g_{ij}^{TT}\) | STRUCTURAL |
| forbidden scalar radiation | CONSTRAINED |

Current recombination status:

```text
useful reduced ansatz,
not covariantly derived,
scalar double-counting controlled by rules,
parent map missing.
```

---

## What This Study Established

This study established:

1. The current recombination map is only a reduced bookkeeping ansatz.
2. \(g_{tt}\) from \(A\) is the strongest piece.
3. \(g_{rr}\) through \(B=e^{2\kappa}/A\) is reduced/gauge-conditioned.
4. \(g_{0i}\) from \(W_i\) is structural but normalization is missing.
5. \(g_{ij}^{TT}\) from \(h_{ij}^{TT}\) is structural but coupling is missing.
6. \(\kappa\) must not become a second scalar gravity field.
7. Recombination must be protected against scalar double-counting and silent GR import.

---

## What This Study Did Not Establish

This study did not derive the covariant metric.

It did not derive the shift-vector normalization.

It did not derive the tensor coupling.

It did not derive the parent gauge structure.

It did not derive the no-double-counting rules.

It did not prove GR-equivalence.

It only audited the reduced recombination map.

---

## Current Best Interpretation

The current recombination map is:

```text
g_tt:
  from A

g_0i:
  from W_i

g_ij:
  from scalar spatial response,
  constrained kappa trace role,
  and h_ij^TT
```

It is not yet a covariant parent derivation.

The two key risks are:

```text
scalar double-counting,
silent GR import.
```

---

## Next Development Target

The next script should be:

```text
candidate_source_decomposition_ledger.py
```

Purpose:

```text
Separate rho, j_T, trace, pressure, and TT stress source roles.
```

Reason:

```text
Recombination depends on a clean source split; source roles are the next trap.
```

Expected result:

```text
A source ledger stating exactly which source feeds A, W_i, h_ij^TT, kappa,
and which source assignments are forbidden.
```

---

## Summary

The recombination map is useful but dangerous.

It says:

\[
g_{tt}\leftarrow A,
\]

\[
g_{0i}\leftarrow W_i,
\]

\[
g_{ij}\leftarrow
\text{scalar spatial response}
+
\kappa_{\rm constrained}
+
h_{ij}^{TT}.
\]

But the goblin warning remains:

```text
do not let recombination become GR imported in disguise.
```

The next gate is source decomposition.
