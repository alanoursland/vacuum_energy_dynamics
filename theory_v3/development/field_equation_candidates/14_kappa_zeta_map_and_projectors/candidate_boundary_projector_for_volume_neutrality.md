# Candidate Boundary Projector For Volume Neutrality

## Canonical Filename

```text
candidate_boundary_projector_for_volume_neutrality.md
```

This document summarizes the output of:

```text
candidate_boundary_projector_for_volume_neutrality.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of \(P_{\rm boundary}\), not a boundary mass theorem, and not a final interface law.

Its purpose is to split boundary / exterior-neutrality duties away from \(P_{\rm trace}\).

The guiding question was:

```text
What exactly belongs to P_boundary for zeta/kappa exterior neutrality?
```

The answer is:

```text
P_boundary is responsible for:
  exterior zeta/kappa neutrality,
  zero boundary flux,
  zero volume/kappa charge,
  A-sector mass protection,
  shell-source avoidance.

It should compose with P_trace:

  P_boundary P_trace.
```

---

## Why This Study Matters

The trace-projector audit found that \(P_{\rm trace}\) had become a requirement bundle:

```text
trace extraction,
A-sector exclusion,
compensation / zero monopole,
TT annihilation,
boundary cooperation.
```

This was too broad. Boundary neutrality is mechanism-distinct from trace extraction.

Therefore this study splits out \(P_{\rm boundary}\).

---

## Compact \(P_{\rm boundary}\) Ledger

| Entry | Requirement | Status | Missing |
|---|---|---|---|
| B1: exterior \(\zeta\) neutrality | \(\zeta_{\rm ext}\to0\) | REQUIRED | exterior stability theorem |
| B2: exterior \(\kappa\) neutrality | \(\kappa_{\rm ext}\to0\) | REQUIRED | \(\kappa\)-\(\zeta\) boundary relation |
| B3: zero \(\zeta\) boundary flux | \(F_\zeta(R+)=0\) | REQUIRED | interface law |
| B4: zero \(\kappa\) boundary flux | \(F_\kappa(R+)=0\) | REQUIRED | interface law |
| B5: zero volume charge | \(Q_{\rm volume}=0\) | REQUIRED | \(S_{\rm volume}\) definition and compensation origin |
| B6: zero \(\kappa\) charge | \(Q_\kappa=0\) | REQUIRED | \(Q_\kappa\) definition and relation to \(Q_{\rm volume}\) |
| B7: \(A\)-sector mass protection | \(\delta M_{\rm ext}|_{\rm boundary\ zeta/\kappa}=0\) | REQUIRED | boundary mass preservation theorem |
| B8: compact-support profile compatibility | \(\zeta(R)=\zeta'(R)=0\) and/or \(\kappa(R)=\kappa'(R)=0\) | STRUCTURAL | physical interface law |
| B9: shell-source avoidance | sufficient smoothness at boundary, possibly \(C^2\) or distribution-safe matching | CANDIDATE | required differentiability from action / field equations |
| B10: cooperation with \(P_{\rm trace}\) | \(P_{\rm boundary}P_{\rm trace}\) maps trace / volume residual to exterior-neutral support | RECOMMENDED | composition law \(P_{\rm boundary}P_{\rm trace}\) |
| B11: cooperation with \(P_{\rm recombination}\) | boundary-neutral \(\zeta/\kappa\) inserted into \(g_{ij}\) once | REQUIRED | \(P_{\rm recombination}\) definition |
| B12: no scalar radiation at boundary | boundary projector is not a radiative outgoing condition for scalar mode | FORBIDDEN | parent scalar-radiation exclusion |

---

## Status Counts

The run counted:

```text
CANDIDATE:    1
FORBIDDEN:    1
RECOMMENDED:  1
REQUIRED:     8
STRUCTURAL:   1
```

Interpretation:

```text
P_boundary has a clearer job than P_trace:
  enforce exterior neutrality, zero flux, zero charge, and mass preservation.
Compact profiles are useful diagnostics but not derivations.
P_boundary must cooperate with P_trace and P_recombination.
```

---

## Minimal \(P_{\rm boundary}\) Requirement Bundle

Current operational bundle:

```text
P_boundary =
  exterior zeta/kappa neutrality
  + zero boundary flux
  + zero volume/kappa charge
  + A-sector mass protection
  + shell-source avoidance
```

Composition target:

\[
P_{\rm boundary}P_{\rm trace}.
\]

Meaning:

```text
trace / volume residual is projected into a boundary-neutral sector.
```

---

## Toy Boundary Diagnostics

Compact-support profile compatibility is currently structural, not a physical mechanism.

Examples:

\[
\zeta(R)=\zeta'(R)=0,
\]

and:

\[
\kappa(R)=\kappa'(R)=0.
\]

These are useful because they diagnose:

```text
zero boundary flux,
no exterior tail,
and possible shell-source avoidance.
```

But they do not yet explain why the theory should produce such profiles.

Therefore:

```text
compact profiles are tests,
not laws.
```

---

## Failure Controls

\(P_{\rm boundary}\) fails if:

1. \(\zeta_{\rm ext}\) has a \(1/r\) tail.
2. \(\kappa_{\rm ext}\) has a \(1/r\) tail.
3. \(F_\zeta(R+)\) or \(F_\kappa(R+)\) is nonzero.
4. \(Q_{\rm volume}\) or \(Q_\kappa\) is nonzero.
5. \(\delta M_{\rm ext}\) changes.
6. A hidden shell source appears.
7. Compact profile tests are mistaken for derivation.
8. Boundary neutralization becomes scalar radiation.
9. \(P_{\rm boundary}\) and \(P_{\rm recombination}\) both add trace corrections.

---

## What This Study Established

This study established that \(P_{\rm boundary}\) owns the boundary / exterior-neutrality burden:

```text
exterior zeta/kappa neutrality,
zero boundary flux,
zero volume/kappa charge,
A-sector mass protection,
shell-source avoidance.
```

It also established the key composition:

\[
P_{\rm boundary}P_{\rm trace}.
\]

This composition means:

```text
trace / volume residual is projected into a boundary-neutral sector.
```

---

## What This Study Did Not Establish

This study did not derive \(P_{\rm boundary}\).

It did not derive the exterior stability theorem.

It did not derive the interface law.

It did not prove the boundary mass preservation theorem.

It did not define \(Q_\kappa\), \(Q_{\rm volume}\), or \(S_{\rm volume}\).

It did not define \(P_{\rm recombination}\).

It did not prove scalar-radiation exclusion.

---

## Current Best Interpretation

\(P_{\rm boundary}\) is now cleaner than \(P_{\rm trace}\).

It should own:

```text
exterior neutrality,
zero flux,
zero charge,
mass protection,
shell-source avoidance.
```

It should not own the whole scalar-radiation theorem.

It must not become an outgoing scalar-radiation boundary condition.

---

## Next Development Target

The next script should be:

```text
candidate_recombination_projector_for_trace_volume.py
```

Purpose:

```text
Define how A, zeta, and kappa assemble without double-counting.
```

Reason:

```text
P_boundary is now separated.
The next risk is recombination double-counting of A, zeta, and kappa.
```

Expected result:

```text
A recombination-projector ledger:
  A-sector mass/spatial response,
  zeta volume response,
  kappa residual/diagnostic response,
  h_TT trace-free addition,
  W_i vector addition,
  boundary-neutral inputs,
  count-once trace/volume assembly,
  forbidden duplicate scalar spatial response.
```

---

## Summary

The boundary-projector result is:

```text
P_boundary is not the whole scalar-safety theorem.
It is the exterior-neutrality and boundary-interface gate.
```

The next goblin gate is:

```text
how do A, zeta, and kappa enter the metric once, and only once?
```
