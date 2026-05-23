# Candidate Trace Projector Definition

## Canonical Filename

```text
candidate_trace_projector_definition.md
```

This document summarizes the output of:

```text
candidate_trace_projector_definition.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of \(P_{\rm trace}\), not a parent projector theorem, and not a final \(\kappa\)-\(\zeta\) map.

Its purpose is to define the required roles of \(P_{\rm trace}\) without pretending the parent projector is derived.

The guiding question was:

```text
What must P_trace do for projected kappa to be safe?
```

The answer is:

```text
P_trace is currently best understood as a requirement bundle:

  trace extraction,
  A-sector exclusion,
  compensation / zero monopole,
  TT annihilation,
  boundary cooperation.

It is not yet a derived operator.
```

---

## Why This Study Matters

The projected \(\kappa\)-\(\zeta\) map:

\[
\kappa=P_{\rm trace}(\zeta-\zeta_{\min})
\]

is only meaningful if \(P_{\rm trace}\) is real enough to prevent scalar double-counting, scalar radiation, and exterior scalar charge.

The safer projected relation:

\[
\kappa=P_{\rm relax}P_{\rm trace}(\zeta-\zeta_{\min})
\]

also depends on \(P_{\rm trace}\) being non-radiative and compatible with first-order relaxation.

This study concludes that \(P_{\rm trace}\) is not yet a single clean operator. It is a bundle of required jobs.

---

## Compact \(P_{\rm trace}\) Ledger

| Entry | Requirement | Status | Missing |
|---|---|---|---|
| T1: linear metric trace extraction | \(P_{\rm trace}h_{ij}=\frac13\gamma_{ij}\gamma^{ab}h_{ab}\) | STRUCTURAL | nonlinear / covariant extension |
| T2: \(\zeta\) variation relation | \(\delta\zeta=\frac12\gamma^{ij}\delta\gamma_{ij}\) | STRUCTURAL | frame or covariant volume variable |
| T3: TT annihilation | \(P_{\rm trace}h_{TT}=0\) and \(P_{TT}P_{\rm trace}=0\) | REQUIRED | nonlinear / covariant projector proof |
| T4: \(A\)-sector mass exclusion | \(P_{\rm trace}\) excludes \(A_{\rm flux}\) / \(\rho\) exterior mass charge | REQUIRED | scalar constraint propagation and source routing identity |
| T5: compensation / zero monopole | \(\int P_{\rm trace}S_{\rm volume}\,d^3x=0\) or \(Q_\kappa=Q_{\rm volume}=0\) | REQUIRED | parent origin of compensation |
| T6: boundary cooperation | \(P_{\rm boundary}P_{\rm trace}\) enforces \(F_\zeta(R+)=F_\kappa(R+)=0\) | REQUIRED | \(P_{\rm boundary}\) definition |
| T7: no wave operator | \(P_{\rm trace}\) is not \(\Box\), not hyperbolic propagation | FORBIDDEN | parent proof of no scalar inertia |
| T8: relaxation compatibility | \(P_{\rm relax}P_{\rm trace}\) may feed first-order \(\kappa\) relaxation | CANDIDATE | \(P_{\rm relax}\) and \(\Gamma_{\rm relax}\) relation |
| T9: diagnostic versus energetic status | \(P_{\rm trace}\) output must be labeled diagnostic, constraint, or energetic | UNRESOLVED | degree-of-freedom and energy-accounting rule |
| T10: recombination compatibility | \(P_{\rm recombination}\) counts \(A/\zeta/\kappa\) trace response once | REQUIRED | \(P_{\rm recombination}\) definition |
| T11: raw pressure / trace source rejection | \(P_{\rm trace}[T]\) is not raw \(T\), raw \(p\), or \(\Delta\kappa=\alpha T\) | REJECTED | not pursued as raw source |
| T12: recommended provisional \(P_{\rm trace}\) definition | trace extraction + \(A\)-sector exclusion + compensation + TT annihilation, with boundary cooperation | RECOMMENDED | actual parent-derived mathematical operator |

---

## Status Counts

The run counted:

```text
CANDIDATE:    1
FORBIDDEN:    1
RECOMMENDED:  1
REJECTED:     1
REQUIRED:     5
STRUCTURAL:   2
UNRESOLVED:   1
```

Interpretation:

```text
P_trace is not a single simple operation yet.
It is currently a requirement bundle:
  trace extraction,
  A-exclusion,
  compensation,
  TT annihilation,
  boundary cooperation.
The next likely split is P_trace versus P_boundary versus P_recombination.
```

---

## Minimal \(P_{\rm trace}\) Requirement Bundle

Current operational bundle:

```text
P_trace =
  trace extraction
  + A-sector mass exclusion
  + compensation / zero monopole
  + TT annihilation
  + boundary cooperation
```

Not yet decided:

```text
which pieces belong to P_trace itself,
which belong to P_boundary,
which belong to P_recombination,
which belong to P_relax.
```

Therefore:

```text
P_trace is a requirement bundle, not a derived operator.
```

---

## Failure Controls

\(P_{\rm trace}\) fails if:

1. It is raw pressure / trace source.
2. It duplicates \(A\)-sector mass.
3. It allows \(\kappa/\zeta\) exterior \(1/r\) charge.
4. It contaminates TT radiation.
5. It becomes \(\Box\kappa\) or \(\Box\zeta\).
6. It hides boundary conditions.
7. It creates \(e_\kappa/\epsilon_\zeta\) double-counting.
8. It is treated as parent-derived before derivation.

---

## What This Study Established

This study established that \(P_{\rm trace}\) is currently a requirement bundle, not a derived operator.

Its minimal burden is:

```text
trace extraction,
A-sector exclusion,
compensation / zero monopole,
TT annihilation,
boundary cooperation.
```

It also established that boundary neutrality should probably be split out next.

---

## What This Study Did Not Establish

This study did not derive \(P_{\rm trace}\).

It did not derive the covariant trace projector.

It did not define \(P_{\rm boundary}\).

It did not define \(P_{\rm recombination}\).

It did not define \(P_{\rm relax}\).

It did not resolve whether the \(P_{\rm trace}\) output is diagnostic, energetic, or constraint-defining.

---

## Current Best Interpretation

The current best operational definition is:

```text
P_trace = trace extraction + A-sector exclusion + compensation + TT annihilation,
with boundary cooperation.
```

But this is not a final operator.

The next step is to split off the boundary duties.

---

## Next Development Target

The next script should be:

```text
candidate_boundary_projector_for_volume_neutrality.py
```

Purpose:

```text
Split off boundary / exterior neutrality duties.
```

Reason:

```text
P_trace currently carries boundary neutrality duties.
Those should be isolated as P_boundary requirements.
```

Expected result:

```text
A boundary-projector ledger:
  zero exterior zeta/kappa,
  zero boundary flux,
  zero volume/kappa charge,
  protected A-sector mass,
  compact support / compensation,
  shell-source avoidance,
  relation to P_trace and P_recombination.
```

---

## Summary

The trace-projector result is:

```text
P_trace is not one magic operator.
It is a requirement bundle that must now be decomposed.
```

The next goblin gate is:

```text
what exactly belongs to P_boundary?
```
