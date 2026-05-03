# Candidate Source Decomposition Ledger

## What This Document Is

This document is a development note for the `11_field_equation_closure/` group.

It is not a final source law, not a covariant stress-energy decomposition, and not a proof of conservation closure. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_source_decomposition_ledger.py
```

The guiding question was:

```text
Which source feeds which field sector, and which source assignments are forbidden?
```

The answer is:

```text
rho -> A
j_T -> W_i
trace / pressure -> kappa_min shift
TT stress / quadrupole -> h_ij^TT
A_rad ordinary long-range scalar source -> rejected
```

Main risk:

```text
any source doing two independent jobs without a parent identity.
```

---

## Why This Study Matters

The metric recombination map showed that recombination cannot be trusted unless the source roles are clean.

The theory currently has several possible source objects:

```text
rho,
M_enc,
j_i,
j_T,
j_L,
pressure p,
stress trace T,
TT stress S_ij^TT,
quadrupole Q_ij^TT,
A_rad source,
Sigma_creation,
Gamma_relax.
```

If these sources are allowed to feed multiple sectors freely, the theory will double-count matter response and quietly imitate GR.

This source ledger prevents that.

---

## Compact Source Ledger

| Source | Allowed Role | Forbidden Role | Sector | Status |
|---|---|---|---|---|
| \(\rho\) | sources \(A\)-sector scalar monopole / areal flux | must not also source an independent long-range \(\kappa\) scalar | \(A\) | DERIVED_REDUCED |
| \(M_{\rm enc}\) | sets exterior \(A\) flux normalization | must not be altered by \(\kappa\) boundary smoothing | \(A\) exterior | DERIVED_REDUCED |
| \(j_i=\rho v_i\) | matter current; decomposes into transverse and longitudinal parts | must not source \(W_i\) through longitudinal / gauge part | continuity source | CONSTRAINED |
| \(j_T=P_Tj\) | sources transverse vector \(W_i\) | must not feed scalar \(A\) except through consistency / continuity | \(W_i\) | STRUCTURAL |
| \(j_L=P_Lj\) | belongs to scalar continuity / density redistribution | must not create transverse vector curl field | \(A\) / continuity | DERIVED_REDUCED |
| pressure \(p\) | may contribute to trace / minimum shift \(\kappa_{\min}\) | must not source ordinary massless \(\kappa\) Poisson tail or breathing wave | \(\kappa\) | CONSTRAINED |
| stress trace \(T\) | may shift \(\kappa_{\min}\) / trace-volume relaxation | must not duplicate \(A\)-sector \(\rho\) source or TT radiation | \(\kappa\) | STRUCTURAL |
| TT stress \(S_{ij}^{TT}\) | sources \(h_{ij}^{TT}\) tensor radiation | must not be collapsed into scalar trace or \(\kappa\) source | \(h_{ij}^{TT}\) | STRUCTURAL |
| quadrupole \(Q_{ij}^{TT}\) | far-zone tensor radiation shape | must not imply scalar quadrupole radiation in \(A_{\rm rad}\) or \(\kappa\) | \(h_{ij}^{TT}\) far zone | STRUCTURAL |
| \(A_{\rm rad}\) source | none as ordinary long-range scalar radiation | forbidden unless separately derived, massive, constrained, or non-propagating | scalar radiation hazard | REJECTED |
| \(\Sigma_{\rm creation}\) | special active-regime nonconservative source if separately invoked | must not enter ordinary closed gravity field equations by default | active regimes | RISK |
| \(\Gamma_{\rm relax}\) | relaxation toward vacuum minimum / \(\kappa\) non-inertial equilibration | must not destroy energy or damp \(A\)-sector mass field | \(\kappa\) / vacuum balance | STRUCTURAL |

---

## Status Counts

The run counted:

```text
CONSTRAINED:      2
DERIVED_REDUCED:  3
REJECTED:         1
RISK:             1
STRUCTURAL:       5
```

Interpretation:

```text
The source split is useful and disciplined, but not yet covariantly derived.
```

---

## Key No-Double-Counting Rules

The source decomposition produced these rules:

1. \(\rho\) is the \(A\)-sector scalar mass source.
2. \(\kappa\) may respond to trace / pressure only as a local minimum shift.
3. \(\kappa\) must not produce an exterior \(\rho\)-like \(1/r\) scalar field.
4. \(j_T\) sources \(W_i\); \(j_L\) belongs to scalar continuity.
5. TT stress sources \(h_{ij}^{TT}\); trace stress does not source TT radiation.
6. \(A_{\rm rad}\) is not an ordinary active sector.
7. Relaxation may transfer imbalance into vacuum configuration, but must not erase \(A\).

Status:

```text
CONSTRAINED
```

These are not optional bookkeeping preferences. They are safety rules.

---

## Source Role Hierarchy

The source hierarchy is:

```text
conserved mass / energy density
  -> scalar constraint A

transverse current
  -> vector response W_i

trace-free quadrupole / shear
  -> tensor radiation h_ij^TT

trace / pressure / volume imbalance
  -> constrained kappa_min shift

scalar radiative residue
  -> rejected or non-propagating
```

This keeps each source from doing too many jobs.

---

## Failure Controls

Source decomposition fails if:

1. \(\rho\) sources both \(A\) and a long-range \(\kappa\) field.
2. Pressure trace creates a massless exterior \(\kappa\) tail.
3. Trace response becomes breathing radiation.
4. Vector longitudinal current is treated as frame dragging.
5. TT stress coupling is matched while claimed derived.
6. \(\Sigma_{\rm creation}\) enters ordinary gravity closure without active-regime conditions.
7. \(\Gamma_{\rm relax}\) hides energy nonconservation.
8. Source decomposition is chosen to imitate GR rather than forced by ontology.

---

## What This Study Established

This study established:

1. \(\rho\) belongs to the \(A\)-sector mass response.
2. \(j_T\) belongs to the vector response.
3. \(j_L\) belongs to continuity / scalar redistribution.
4. Pressure and stress trace may shift \(\kappa_{\min}\), but may not source scalar radiation.
5. TT stress and quadrupole structure belong to tensor radiation.
6. \(A_{\rm rad}\) remains rejected as an ordinary long-range scalar radiation sector.
7. \(\Sigma_{\rm creation}\) is not part of ordinary closed gravity unless an active regime is separately invoked.
8. \(\Gamma_{\rm relax}\) must not destroy energy or damp the \(A\)-sector mass field.

---

## What This Study Did Not Establish

This study did not derive the covariant stress-energy decomposition.

It did not derive the parent conservation identity.

It did not derive vector normalization.

It did not derive tensor coupling.

It did not derive \(S_{\rm trace,effective}\).

It did not derive \(\Gamma_{\rm relax}\)'s vacuum energy destination.

It only formalized the current source ledger.

---

## Current Best Interpretation

Current source decomposition:

```text
rho:
  A-sector scalar mass source

j_T:
  W_i vector source

trace / pressure:
  kappa_min shift source

TT stress / quadrupole:
  h_ij^TT source

ordinary long-range scalar radiation source:
  rejected
```

Main risk:

```text
any source doing two independent jobs without a parent identity.
```

---

## Next Development Target

The next script should be:

```text
candidate_no_double_counting_constraints.py
```

Purpose:

```text
Turn source ledger into explicit algebraic / sector constraints.
```

Reason:

```text
The ledger identifies forbidden overlaps; the next check should formalize them.
```

Expected result:

```text
A constraint ledger stating which source-sector overlaps are allowed,
which must vanish,
and which require parent identity support.
```

---

## Summary

The source ledger says:

```text
One source may participate in total stress-energy,
but it may not become multiple independent gravity sources unless a parent
identity forces the split.
```

That is the next goblin law to formalize.
