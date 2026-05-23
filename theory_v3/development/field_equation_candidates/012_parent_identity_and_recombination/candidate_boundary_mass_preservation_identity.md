# Candidate Boundary Mass Preservation Identity

## Canonical Filename

```text
candidate_boundary_mass_preservation_identity.md
```

This document summarizes the output of:

```text
candidate_boundary_mass_preservation_identity.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a proof of boundary matching, not a parent identity, and not a final interface theorem. It does not add a formal commitment to the theory.

Its purpose is to formalize the requirement that \(\kappa\) / boundary relaxation cannot change exterior mass.

The guiding question was:

```text
Can kappa / boundary relaxation occur without changing exterior mass?
```

The answer is:

```text
Boundary / kappa relaxation can remain safe only if:
  exterior mass is A-sector flux,
  delta M_ext from kappa relaxation is zero,
  Q_kappa is zero,
  F_kappa(R+) is zero,
  exterior kappa relaxes to zero,
  recombination preserves exterior Schwarzschild,
  relaxation energy is accounted.
```

---

## Why This Study Matters

The \(\kappa\) covariant-relaxation audit found that first-order \(\kappa\) relaxation is safe only if it cannot leak into exterior scalar charge or alter the exterior mass.

The key danger is:

```text
boundary smoothing tunes measured gravity.
```

This study sharpens the required identity:

\[
\delta M_{\rm ext}\big|_{\kappa{\rm\ relaxation}}=0.
\]

and:

\[
F_\kappa(R+)=0.
\]

---

## Compact Boundary Ledger

| Requirement | Candidate Form | Forbidden Form | Status | Missing |
|---|---|---|---|---|
| B1: exterior mass is \(A\)-sector flux | \(A_{\rm ext}=1-2GM_{\rm ext}/(c^2r)\) | \(M_{\rm ext}\) adjusted by \(\kappa\) boundary smoothing | DERIVED_REDUCED | parent flux-charge definition |
| B2: \(\kappa\) boundary relaxation preserves \(M_{\rm ext}\) | \(\delta M_{\rm ext}|_{\kappa{\rm\ relaxation}}=0\) | \(\delta M_{\rm ext}\ne0\) from smoothing or \(\kappa\) interface adjustment | REQUIRED | boundary mass preservation theorem |
| B3: exterior \(\kappa\) charge vanishes | \(Q_\kappa=\int S_\kappa d^3x=0\) | \(\kappa_{\rm ext}\sim q_\kappa/r\) | CONSTRAINED | projection or boundary cancellation identity |
| B4: exterior \(\kappa\) flux vanishes | \(F_\kappa(R+)=4\pi R^2\kappa'(R+)=0\) | \(F_\kappa(R+)\ne0\) | CONSTRAINED | interface law enforcing zero flux |
| B5: exterior vacuum fixed point | \(S_{\rm trace,effective}=0\Rightarrow\kappa_{\min}=0\Rightarrow\kappa\to0\) | nonzero exterior \(\kappa\) attractor | CONSTRAINED | exterior vacuum relaxation proof |
| B6: \(A\) flux and \(\kappa\) flux are independent charges | \(\delta\int\nabla A\cdot dS|_\kappa=0\) | \(\kappa\) boundary condition changes \(\int\nabla A\cdot dS\) | REQUIRED | parent separation of \(A\) flux and \(\kappa\) boundary condition |
| B7: joint-minimum smoothing is diagnostic only | \(f_{\rm joint}\) diagnostics with fixed exterior \(M_{\rm ext}\) | joint-minimum fit changes exterior mass coefficient | CONSTRAINED | weights, \(\sigma\), recombination, observable map |
| B8: source compactness condition | support\((S_{\kappa{\rm eff}})\) compact and/or \(\int S_{\kappa{\rm eff}}d^3x=0\) | uncompensated trace source leaking into exterior | STRUCTURAL | definition of \(S_{\kappa{\rm eff}}\) and compensation law |
| B9: recombination preserves exterior Schwarzschild | \(\kappa_{\rm ext}=0\Rightarrow\) recombination gives exterior Schwarzschild reduced form | recombination reintroduces scalar trace outside | REQUIRED | \(P_{\rm recombination}\) identity |
| B10: relaxation energy does not alter \(M_{\rm ext}\) by disappearance | \(\Delta E_{\rm relax}\to\Delta E_{\rm vac,config}\) with total exterior charge preserved | energy damping changes mass without source accounting | MISSING | vacuum configuration energy balance |

---

## Status Counts

The run counted:

```text
CONSTRAINED:      4
DERIVED_REDUCED:  1
MISSING:          1
REQUIRED:         3
STRUCTURAL:       1
```

Interpretation:

```text
Exterior A mass is reduced-derived.
Boundary preservation is required but not proven.
Relaxation energy accounting remains missing.
```

---

## Candidate Boundary Identity

The candidate boundary preservation identity is:

\[
\delta M_{\rm ext}\big|_{\kappa{\rm\ relaxation}}=0.
\]

with:

\[
M_{\rm ext}
\propto
\text{exterior }A\text{ flux},
\]

\[
F_\kappa(R+)=0,
\]

\[
Q_\kappa=0,
\]

and:

\[
\kappa_{\rm ext}\to0.
\]

Equivalent reduced reading:

```text
kappa can smooth / relax local trace-volume matching,
but it cannot change the coefficient of 1/r in A_ext.
```

Status:

```text
REQUIRED / NOT YET THEOREM
```

---

## Failure Controls

Boundary mass preservation fails if:

1. \(\kappa\) smoothing changes \(M_{\rm ext}\).
2. \(F_\kappa(R+)\) is nonzero.
3. \(Q_\kappa\) is nonzero.
4. Exterior \(\kappa\) has a nonzero attractor.
5. \(A\) flux and \(\kappa\) flux mix without parent identity.
6. Near-boundary diagnostics are advertised as measured predictions.
7. Relaxation energy disappears or changes exterior mass without accounting.

---

## What This Study Established

This study established that \(\kappa\) / boundary relaxation can remain safe only if:

```text
exterior mass is A-sector flux,
delta M_ext from kappa relaxation is zero,
Q_kappa is zero,
F_kappa(R+) is zero,
exterior kappa relaxes to zero,
recombination preserves exterior Schwarzschild,
relaxation energy is accounted.
```

The strongest piece is:

```text
exterior mass as A-sector flux.
```

The weakest pieces are:

```text
boundary mass preservation theorem,
relaxation energy accounting,
P_recombination identity.
```

---

## What This Study Did Not Establish

This study did not derive the boundary theorem.

It did not derive the parent separation of \(A\)-flux and \(\kappa\)-flux.

It did not derive \(Q_\kappa=0\).

It did not derive \(F_\kappa(R+)=0\).

It did not derive relaxation energy accounting.

It did not derive recombination.

It only formalized the boundary mass preservation requirements.

---

## Current Best Interpretation

Boundary / \(\kappa\) relaxation can remain safe only if:

\[
\delta M_{\rm ext}\big|_{\kappa{\rm\ relaxation}}=0,
\]

\[
Q_\kappa=0,
\]

\[
F_\kappa(R+)=0,
\]

and:

\[
\kappa_{\rm ext}\to0.
\]

This is a requirement, not a theorem.

---

## Next Development Target

The next script should be:

```text
candidate_recombination_without_double_counting.py
```

Purpose:

```text
Try a disciplined recombination map.
```

Reason:

```text
Boundary mass is protected by requirements;
now recombination must avoid reintroducing scalar double-counting.
```

Expected result:

```text
A recombination ledger:
  g_tt receives A,
  g_0i receives W_i,
  g_ij receives scalar spatial response, constrained kappa, and h_TT,
  exterior kappa=0 preserves Schwarzschild,
  scalar response is counted exactly once,
  kappa does not carry exterior mass,
  h_TT is trace-free,
  W_i is transverse.
```

---

## Summary

The boundary result says:

```text
kappa may smooth trace / volume matching,
but it cannot change exterior mass.
```

The next goblin gate is recombination.
