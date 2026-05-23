# Candidate GR Limit Recovery Audit

## Canonical Filename

```text
candidate_gr_limit_recovery_audit.md
```

This document summarizes the output of:

```text
candidate_gr_limit_recovery_audit.py
```

---

## What This Document Is

This document is a development note for the `11_field_equation_closure/` group.

It is not a claim that the theory has fully recovered GR, not a final parent closure, and not a covariant derivation. It does not add a formal commitment to the theory.

Its purpose is to audit the GR-facing recovery status.

The guiding question was:

```text
Which GR-facing results are actually derived, reduced-derived, structural,
matched, constrained, missing, or risky?
```

The answer is:

```text
real reduced reconstruction:
  static spherical exterior

strong reduced / structural support:
  weak scalar limit,
  gamma=1,
  vector shape

structural but not coefficient-derived:
  tensor waves

matched:
  tensor coupling / flux,
  vector normalization

constrained:
  no scalar radiation,
  kappa safety

missing:
  Bianchi-like parent closure,
  covariant recombination
```

---

## Why This Study Matters

Before trying to write a parent identity, the project needs to know what the identity must explain.

A parent identity should not merely be written to reproduce GR.

It should explain which parts have already been reconstructed from the vacuum-curvature ontology and which parts are still only structural or matched.

The audit prevents this failure mode:

```text
target = derivation
```

The audit also preserves this rule:

```text
structural agreement is not coefficient derivation.
```

---

## Compact GR Recovery Ledger

| Result | GR Target | Status | Real | Not Yet Real |
|---|---|---|---|---|
| Static spherical exterior \(A\) | Schwarzschild \(A=1-2GM/(c^2r)\) | DERIVED_REDUCED | Exterior scalar factor is genuinely reconstructed in the reduced static spherical case | Full covariant derivation and nonspherical nonlinear extension |
| Exterior \(B=1/A\) | Schwarzschild radial factor | DERIVED_REDUCED | Reduced exterior reciprocal relation follows once exterior \(\kappa=0\) | Covariant gauge / physical meaning of \(\kappa\) and \(B\) |
| Weak scalar multipoles | Newtonian potential / weak GR scalar limit | DERIVED_REDUCED | Weak scalar / multipole structure follows from scalar constraint analogy | Full nonlinear nonspherical equation and conservation closure |
| PPN \(\gamma=1\) / spatial scalar response | equal weak spatial/lapse scalar response | DERIVED_REDUCED | Weak exterior reciprocal relation supports \(\gamma=1\) in the reduced regime | General PPN derivation with all parameters and gauges |
| Frame-dragging shape | far-field gravitomagnetic dipole proportional to angular momentum \(J\) | DERIVED_REDUCED | Expected far-field vector shape and angular-momentum dependence are supported | Absolute normalization and observable coupling \(\beta_W\) |
| Frame-dragging normalization | Lense-Thirring coefficient | MATCHED | Target normalization is known | Ontology-derived coefficient |
| Tensor wave existence | two transverse-traceless gravitational wave polarizations | STRUCTURAL | TT-only radiation is structurally consistent and scalar/vector radiation hazards are constrained | Action-derived tensor wave equation and coupling |
| Tensor wave coupling | linearized GR coupling to TT stress / quadrupole | MATCHED | Correct target structure is identified | \(C_T\) from vacuum ontology |
| Quadrupole radiation power | GR quadrupole luminosity | MATCHED | Energy-flux form is structurally aligned with TT radiation | Absolute flux coefficient and quadrupole power coefficient |
| No scalar breathing radiation | GR has no scalar breathing mode | CONSTRAINED | Scalar radiation hazards are explicitly controlled by current rules | Parent identity proving absence rather than imposing it |
| \(\kappa\) interior / trace behavior | GR interior pressure/stress effects without exterior scalar radiation | STRUCTURAL | Coherent control model prevents \(\kappa\) from becoming scalar gravity | Source law, coefficients, covariant origin, boundary theorem |
| Near-boundary deviation | possible deviation from naive GR interior/exterior matching | RISK | Deviation diagnostics are defined | Magnitude, observable, weights, transition width, compatibility with tests |
| Conservation / Bianchi compatibility | \(\nabla_\mu G^{\mu\nu}=0\) and \(\nabla_\mu T^{\mu\nu}=0\) compatibility | MISSING | Required identity is named | The identity itself |
| Metric recombination | one coherent metric field | UNFINISHED | Sector map is explicit and no-double-counting rules are known | Covariant recombination map |

---

## Status Counts

The run counted:

```text
CONSTRAINED:      1
DERIVED_REDUCED:  5
MATCHED:          3
MISSING:          1
RISK:             1
STRUCTURAL:       2
UNFINISHED:       1
```

Interpretation:

```text
The strongest results are reduced scalar / exterior results.
Vector shape is reduced-derived but normalization is matched / missing.
Tensor radiation is structurally correct but coupling and flux are matched.
Conservation / Bianchi closure is missing.
```

---

## Strongest Current GR-Facing Recoveries

The strongest current GR-facing recoveries are:

1. Static spherical exterior \(A\).
2. Exterior \(B=1/A\) once \(\kappa=0\).
3. Weak scalar multipole / Newtonian limit.
4. \(\gamma=1\) in the reduced exterior weak limit.
5. Frame-dragging far-field shape proportional to \(J\).

These are real reduced / structural wins.

But they are limited.

Status:

```text
DERIVED_REDUCED
```

---

## Weakest or Most Matched Pieces

The weakest or most matched GR-facing pieces are:

1. Frame-dragging normalization.
2. Tensor coupling \(C_T\).
3. Tensor radiation energy flux coefficient.
4. Bianchi / conservation closure.
5. Covariant metric recombination.

These must not be advertised as derived.

Status:

```text
RISK
```

---

## Reconstruction Scorecard

```text
Reduced scalar exterior:
  real reconstruction

Weak scalar / multipole:
  reduced / structural success

Vector sector:
  shape success,
  normalization missing

Tensor radiation:
  structural TT success,
  coupling / flux matched

Kappa:
  safety / control success,
  not covariant derivation

Conservation / closure:
  missing
```

---

## What This Study Established

This study established:

1. Static spherical exterior recovery is the strongest real reconstruction.
2. Exterior \(B=1/A\) is reduced-derived once exterior \(\kappa=0\).
3. Weak scalar / multipole behavior is strong but still reduced.
4. PPN \(\gamma=1\) is supported in the reduced weak exterior, but this is not a full PPN audit.
5. Frame-dragging shape is supported by the vector-current structure.
6. Frame-dragging normalization remains matched / missing.
7. Tensor waves are structurally correct as TT radiation.
8. Tensor coupling and radiation flux coefficients remain matched.
9. No scalar breathing radiation is constrained, not parent-derived.
10. \(\kappa\) is a safety/control success, not a covariant derivation.
11. Conservation / Bianchi compatibility remains missing.
12. Metric recombination remains unfinished.

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not derive covariant recombination.

It did not derive tensor coupling.

It did not derive tensor radiation flux coefficient.

It did not derive vector normalization.

It did not derive full PPN recovery.

It did not derive \(\kappa\)'s covariant source law.

It only audited the recovery status.

---

## Current Best Interpretation

Honest GR recovery status:

```text
real reduced reconstruction:
  static spherical exterior

strong reduced / structural support:
  weak scalar limit,
  gamma=1,
  vector shape

structural but not coefficient-derived:
  tensor waves

matched:
  tensor coupling / flux,
  vector normalization

constrained:
  no scalar radiation,
  kappa safety

missing:
  Bianchi-like parent closure,
  covariant recombination
```

---

## Next Development Target

The next script should be:

```text
candidate_parent_identity_template.py
```

Purpose:

```text
Try to write an explicit candidate parent identity.
```

Reason:

```text
The GR audit has separated real wins from matched gaps; now try the parent identity.
```

Expected result:

```text
A proposed divergence / balance template that does not claim derivation,
but tests whether one identity can support:
  scalar constraint propagation,
  source conservation,
  TT-only radiation,
  kappa non-radiative trace relaxation,
  boundary mass preservation,
  ordinary exclusion of Sigma_creation.
```

---

## Summary

The audit says:

```text
The theory has real reduced wins.
The theory does not yet have closure.
```

The next goblin door is parent identity.
