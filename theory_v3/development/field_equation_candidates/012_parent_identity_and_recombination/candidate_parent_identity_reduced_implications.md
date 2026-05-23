# Candidate Parent Identity Reduced Implications

## Canonical Filename

```text
candidate_parent_identity_reduced_implications.md
```

This document summarizes the output of:

```text
candidate_parent_identity_reduced_implications.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a parent identity, not a derivation of closure, and not a covariant field equation. It does not add a formal commitment to the theory.

Its purpose is to define the reduced-sector test suite that any surviving parent identity must pass.

The guiding question was:

```text
What must any surviving parent identity imply in each reduced sector?
```

The answer is:

```text
Any surviving parent identity must pass a reduced-sector test suite.

The clearest tests are:
  A constraint,
  exterior Schwarzschild,
  B=1/A when kappa=0,
  transverse W_i,
  TT-only radiation,
  kappa relaxation rather than Box kappa,
  exterior kappa neutrality,
  boundary mass preservation,
  ordinary Sigma_creation=0,
  recombination without double-counting.
```

---

## Why This Study Matters

The previous study ruled out false parent identities.

This study gives the positive companion:

```text
If a parent identity survives the exclusions, what must it imply?
```

The important discipline is:

```text
reduced targets are tests, not derivations.
```

A parent identity must force the sector ledger.

It is not enough for it to coexist with the sector ledger.

---

## Compact Reduced Implication Ledger

| Implication | Sector | Reduced Target | Status | Missing Derivation |
|---|---|---|---|---|
| R1: Static spherical \(A\) constraint | \(A\) scalar / static spherical | \(\Delta_{\rm areal}A=8\pi G\rho/c^2\) | DERIVED_REDUCED_TARGET | Parent projection yielding the areal operator and coefficient |
| R2: Exterior Schwarzschild \(A\) | \(A\) exterior | \(A_{\rm ext}(r)=1-2GM/(c^2r)\) | DERIVED_REDUCED_TARGET | Parent exterior vacuum reduction and mass-flux charge law |
| R3: Exterior \(B\) reciprocal when \(\kappa\) vanishes | \(B/\kappa\) exterior | \(AB=e^{2\kappa}\), \(\kappa_{\rm ext}=0\Rightarrow B=1/A\) | DERIVED_REDUCED_TARGET | Covariant / gauge interpretation of \(AB=e^{2\kappa}\) |
| R4: Weak scalar / Newtonian limit | weak scalar | \(A\simeq1+2\Phi/c^2\), \(\nabla^2\Phi=4\pi G\rho\) | DERIVED_REDUCED_TARGET | Weak-field parent expansion |
| R5: Scalar constraint propagation | scalar dynamics | \(\partial_tC_A[A,\rho]\) follows from continuity\((\rho,j_L)\) | MISSING | Continuity-compatible constraint propagation law |
| R6: Transverse vector source | \(W_i\) vector | \(\nabla\times\nabla\times W=-(\alpha_W/(2K_c))j_T,\;\nabla\cdot W=0\) | STRUCTURAL_TARGET | Parent current projection and normalization \(\alpha_W/K_c\) |
| R7: Angular momentum far-field shape | \(W_i\) far field | \(\nabla\times W\sim J/r^3\) | DERIVED_REDUCED_TARGET | \(\beta_W\) and absolute normalization from parent identity / action |
| R8: TT tensor radiation only | \(h_{ij}^{TT}\) | \(\Box h_{ij}^{TT}=-C_TS_{ij}^{TT}\) | STRUCTURAL_TARGET | Tensor action stiffness, \(C_T\), TT source identity |
| R9: TT source trace exclusion | \(h_{ij}^{TT}\) source | source\((h_{TT})=P_{TT}S_{ij}\), trace excluded | CONSTRAINED_TARGET | Parent projector identity for TT stress |
| R10: \(\kappa\) trace-minimum relaxation | \(\kappa\) trace response | \(\dot\kappa=-\mu_\kappa K_\kappa(\kappa-\kappa_{\min})\) | STRUCTURAL_TARGET | \(K_\kappa,\mu_\kappa,\chi_\kappa,S_{\rm trace,effective}\) from parent vacuum minimum |
| R11: Exterior \(\kappa\) neutrality | \(\kappa\) exterior | \(Q_\kappa=0,\;\kappa\to0,\;F_\kappa(R+)=0\) | CONSTRAINED_TARGET | Parent projection / boundary cancellation law |
| R12: Boundary mass preservation | boundary / interface | \(\delta M_{\rm ext}|_{\kappa{\rm\ relaxation}}=0\) | CONSTRAINED_TARGET | Boundary mass preservation theorem |
| R13: Ordinary closed regime | active regimes | \(\Sigma_{\rm creation}=0\) | CONSTRAINED_TARGET | Active-regime trigger and exclusion law |
| R14: Relaxation energy accounting | vacuum relaxation | \(\Gamma_{\rm relax}\rightarrow\) vacuum configuration restoration / accounting | STRUCTURAL_TARGET | Vacuum configuration energy variable and balance law |
| R15: Recombination without double-counting | metric / geometry recombination | \(g_{tt}\leftarrow A,\;g_{0i}\leftarrow W_i,\;g_{ij}\leftarrow\) scalar response + constrained \(\kappa\) + \(h_{TT}\) | UNRESOLVED | Covariant or reduced parent recombination map |

---

## Status Counts

The run counted:

```text
CONSTRAINED_TARGET:      4
DERIVED_REDUCED_TARGET:  5
MISSING:                 1
STRUCTURAL_TARGET:       4
UNRESOLVED:              1
```

Interpretation:

```text
The parent identity has many clear reduced targets.
Most are not derived from a parent identity yet.
Scalar constraint propagation and recombination remain especially unresolved.
```

---

## Parent Identity Test Suite

A candidate parent identity passes only if it implies:

1. Static spherical \(A\) constraint.
2. Exterior Schwarzschild \(A\).
3. Exterior \(B=1/A\) when \(\kappa=0\).
4. Weak scalar Newtonian limit.
5. Scalar constraint propagation from continuity.
6. Transverse \(W_i\) sourcing.
7. Angular momentum far-field vector shape.
8. TT-only ordinary radiation.
9. Trace exclusion from TT source.
10. \(\kappa\) first-order trace relaxation.
11. Exterior \(\kappa\) neutrality.
12. Boundary mass preservation.
13. \(\Sigma_{\rm creation}=0\) in ordinary closed gravity.
14. Relaxation energy accounting.
15. Recombination without scalar double-counting.

Status:

```text
REQUIRED
```

---

## Hardest Reduced Implications

### 1. Scalar Constraint Propagation

The parent must show:

```text
A evolves consistently with continuity without Box A.
```

This is one of the hardest remaining requirements.

The forbidden alternative is:

\[
\Box A=S.
\]

The desired structure is closer to:

```text
time evolution of the scalar constraint is implied by source continuity.
```

---

### 2. Kappa Trace Relaxation

The parent must show:

```text
trace shifts kappa_min without Box kappa.
```

The forbidden alternative is:

\[
\Box\kappa=\alpha S.
\]

The desired structure is:

\[
\dot\kappa
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}),
\]

with \(\kappa_{\min}\) sourced by an effective trace / pressure / volume condition.

---

### 3. Boundary Mass Preservation

The parent must show:

```text
kappa / boundary relaxation cannot tune M_ext.
```

Required condition:

\[
\delta M_{\rm ext}\big|_{\kappa{\rm\ relaxation}}=0.
\]

Without this, boundary smoothing becomes an illicit mass-adjustment mechanism.

---

### 4. Tensor / Vector Coefficient Derivation

The parent must eventually fix:

```text
C_T,
K_T,
alpha_W / K_c,
beta_W.
```

Until then, vector normalization and tensor coupling / flux remain matched or structurally targeted, not derived.

---

### 5. Recombination

The parent must map sectors into geometry without copying GR by form.

Current reduced target:

```text
g_tt  <- A
g_0i  <- W_i
g_ij  <- scalar response + constrained kappa + h_TT
```

Status:

```text
UNRESOLVED
```

---

## What This Study Established

This study established the reduced-sector test suite for any future parent identity.

The parent identity must not merely exist symbolically.

It must imply:

```text
the A-sector exterior reconstruction,
the scalar constraint structure,
the transverse vector sector,
the TT radiation sector,
the non-radiative kappa trace sector,
the exterior kappa neutrality condition,
the boundary mass preservation condition,
the ordinary closed-regime condition,
and recombination without scalar double-counting.
```

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not derive the projectors.

It did not derive scalar constraint propagation.

It did not derive tensor/vector coefficients.

It did not derive \(\kappa\)'s source law.

It did not derive boundary mass preservation.

It did not derive recombination.

It only stated the tests.

---

## Current Best Interpretation

Any surviving parent identity must pass a reduced-sector test suite.

The clearest tests are:

```text
A constraint,
exterior Schwarzschild,
B=1/A when kappa=0,
transverse W_i,
TT-only radiation,
kappa relaxation rather than Box kappa,
exterior kappa neutrality,
boundary mass preservation,
ordinary Sigma_creation=0,
recombination without double-counting.
```

---

## Next Development Target

The next script should be:

```text
candidate_projector_structure_for_parent_identity.py
```

Purpose:

```text
Work out scalar / vector / TT / trace projectors.
```

Reason:

```text
The reduced implications require projectors.
Projector structure is the next gate.
```

Expected result:

```text
A projector ledger showing:
  which source components feed A,
  which source components feed W_i,
  which source components feed h_TT,
  which source components shift kappa_min,
  which components are forbidden from each sector,
  and which projectors are still only formal.
```

---

## Summary

The parent identity cannot be evaluated as one grand equation yet.

It must first be tested through reduced-sector implications.

Those implications now point to the next goblin gate:

```text
projector structure.
```
