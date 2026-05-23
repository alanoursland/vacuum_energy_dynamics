# Candidate Projector Structure for Parent Identity

## Canonical Filename

```text
candidate_projector_structure_for_parent_identity.md
```

This document summarizes the output of:

```text
candidate_projector_structure_for_parent_identity.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a parent identity, not a derivation of closure, and not a covariant projector theorem. It does not add a formal commitment to the theory.

Its purpose is to audit the projector structure needed before a parent identity can be meaningful.

The guiding question was:

```text
What projector structure is required for a parent identity?
```

The answer is:

```text
The parent identity needs projectors before it can be meaningful.

Current clearest projectors:
  P_L
  P_T

Current structural projectors:
  P_scalar
  P_TT
  P_trace
  P_relax
  P_boundary

Current unresolved / missing projectors:
  P_recombination
  P_coeff
```

---

## Why This Study Matters

The reduced-implication test suite showed that a parent identity must imply:

```text
A scalar constraint,
transverse W_i sourcing,
TT-only radiation,
kappa trace relaxation,
exterior kappa neutrality,
boundary mass preservation,
recombination without scalar double-counting.
```

Those implications require source and sector projectors.

Without projectors, a parent identity cannot prevent forbidden overlaps.

The key rule is:

```text
projectors are not derivations,
but a parent identity without projectors is not disciplined.
```

---

## Compact Projector Ledger

| Projector | Feeds | Excludes | Status | Missing |
|---|---|---|---|---|
| \(P_{\rm scalar}\) | \(A\)-sector scalar constraint | ordinary scalar radiation \(A_{\rm rad}\) and independent \(\kappa\) charge | STRUCTURAL | parent definition of scalar charge and areal operator |
| \(P_L\) | scalar continuity / density redistribution | transverse \(W_i\) source | DERIVED_REDUCED | covariant or curved-background generalization |
| \(P_T\) | \(W_i\) transverse vector response | scalar continuity source | DERIVED_REDUCED | parent current projection and normalization |
| \(P_{TT}\) | \(h_{ij}^{TT}\) tensor radiation | trace stress, pressure, scalar / \(\kappa\) response | STRUCTURAL | parent TT source identity and tensor coupling \(C_T\) |
| \(P_{\rm trace}\) | \(\kappa_{\min}\) shift | \(A\)-sector \(\rho\) source, \(h_{TT}\), \(\Box\kappa\) radiation | STRUCTURAL | \(S_{\rm trace,effective}\) and \(\chi_\kappa\) |
| \(P_{\rm relax}\) | first-order \(\kappa\) relaxation / vacuum restoration | second-order \(\kappa\) momentum channel | CONSTRAINED | vacuum configuration energy accounting |
| \(P_{\rm boundary}\) | local smoothing or \(\kappa\) boundary condition | change in exterior \(A\) mass flux | CONSTRAINED | boundary mass preservation theorem |
| \(P_{\rm closed}\) | ordinary closed gravity sector | \(\Sigma_{\rm creation}\) | CONSTRAINED | active-regime trigger / exclusion law |
| \(P_{\rm recombination}\) | metric / geometry-like recombination map | scalar double-counting and GR form-copying | UNRESOLVED | covariant or reduced parent recombination identity |
| \(P_{\rm coeff}\) | \(\alpha_W/K_c,\beta_W,C_T,K_T\) | coefficient matching by hand | MISSING | action / stiffness derivation |

---

## Status Counts

The run counted:

```text
CONSTRAINED:      3
DERIVED_REDUCED:  2
MISSING:          1
STRUCTURAL:       3
UNRESOLVED:       1
```

Interpretation:

```text
Reduced current projectors P_L and P_T are the clearest.
Scalar, TT, trace, and relaxation projectors are structural.
Recombination and coefficient projectors remain unresolved / missing.
```

---

## Required Source Decomposition

The parent source decomposition must route:

```text
rho / scalar charge
  -> P_scalar
  -> A

longitudinal current
  -> P_L
  -> scalar continuity

transverse current
  -> P_T
  -> W_i

TT stress
  -> P_TT
  -> h_ij^TT

trace / pressure
  -> P_trace
  -> kappa_min

kappa imbalance
  -> P_relax
  -> first-order relaxation

boundary data
  -> P_boundary
  -> M_ext preservation and kappa exterior safety

active-regime terms
  -> P_closed
  -> Sigma_creation=0 in ordinary regime

sector fields
  -> P_recombination
  -> geometry without double-counting
```

Status:

```text
CONSTRAINED
```

---

## Projector Consistency Tests

The projector tests are:

1. \(P_{\rm scalar}\rho\) must not feed \(A_{\rm rad}\).
2. \(P_{\rm scalar}\rho\) must not feed long-range \(\kappa\).
3. \(P_Tj\) must be divergence-free / transverse.
4. \(P_Lj\) must not feed \(\nabla\times W\).
5. \(P_{TT}S\) must be trace-free.
6. \(P_{\rm trace}T\) must not feed \(h_{TT}\).
7. \(P_{\rm trace}T\) must not create \(\Box\kappa\).
8. \(P_{\rm boundary}\) must preserve \(M_{\rm ext}\).
9. \(P_{\rm closed}\) must set \(\Sigma_{\rm creation}=0\) in ordinary gravity.
10. \(P_{\rm recombination}\) must count scalar response exactly once.

---

## Hardest Projectors

### 1. \(P_{\rm scalar}\)

This must explain:

```text
A as constraint rather than scalar radiation.
```

Failure mode:

```text
Box A ordinary scalar radiation.
```

This is the hardest immediate gate.

---

### 2. \(P_{\rm trace}\) / \(P_{\rm relax}\)

These must explain:

```text
kappa relaxation rather than Box kappa.
```

Failure mode:

```text
hidden breathing wave or kappa repair knob.
```

---

### 3. \(P_{\rm boundary}\)

This must explain:

```text
exterior mass preservation under boundary smoothing.
```

Failure mode:

```text
boundary smoothing tunes measured mass.
```

---

### 4. \(P_{\rm recombination}\)

This must explain:

```text
geometry without silent GR import.
```

Failure mode:

```text
copying GR metric form by hand.
```

---

### 5. \(P_{\rm coeff}\)

This must explain:

```text
vector / tensor coefficients rather than matching them.
```

Failure mode:

```text
GR coefficients inserted as derivation.
```

---

## What This Study Established

This study established that the parent identity requires explicit projectors.

It also established that the clearest current projectors are the reduced current projectors:

\[
P_Lj=\nabla\Delta^{-1}\nabla\cdot j,
\]

and:

\[
P_T=I-\frac{kk^T}{k^2}.
\]

These are still reduced / flat-background projectors, not a final covariant parent structure.

The structural projectors are:

```text
P_scalar,
P_TT,
P_trace,
P_relax,
P_boundary.
```

The unresolved or missing projectors are:

```text
P_recombination,
P_coeff.
```

---

## What This Study Did Not Establish

This study did not derive the covariant parent identity.

It did not derive \(P_{\rm scalar}\).

It did not derive \(P_{TT}\) from vacuum shear/stress.

It did not derive \(P_{\rm trace}\) or \(S_{\rm trace,effective}\).

It did not derive \(P_{\rm boundary}\).

It did not derive \(P_{\rm recombination}\).

It did not derive \(P_{\rm coeff}\).

It only stated the projector requirements.

---

## Current Best Interpretation

The parent identity needs projectors before it can be meaningful.

Current clearest projectors:

```text
P_L,
P_T.
```

Current structural projectors:

```text
P_scalar,
P_TT,
P_trace,
P_relax,
P_boundary.
```

Current unresolved / missing projectors:

```text
P_recombination,
P_coeff.
```

---

## Next Development Target

The next script should be:

```text
candidate_scalar_constraint_not_radiation_identity.py
```

Purpose:

```text
Focus on why A constrains rather than radiates.
```

Reason:

```text
P_scalar is the hardest immediate gate:
the parent must explain scalar constraint, not scalar radiation.
```

Expected result:

```text
A test of whether scalar non-radiation can be made structural:
  A is constraint,
  A_rad is rejected,
  scalar constraint propagation follows continuity,
  rho does not source kappa,
  trace does not create scalar radiation.
```

---

## Summary

The next parent-identity problem is not the whole identity.

It is the scalar projector:

```text
Why does the scalar source produce A as a constraint,
rather than A_rad as radiation?
```

That is the next goblin gate.
