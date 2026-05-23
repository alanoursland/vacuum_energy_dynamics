# Candidate A Spatials Versus Zeta Trace Counting

## Canonical Filename

```text
candidate_A_spatial_vs_zeta_trace_counting.md
```

This document summarizes the output of:

```text
candidate_A_spatial_vs_zeta_trace_counting.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of the \(A\)-sector spatial response, not a covariant recombination theorem, and not a final \(\zeta/\kappa\) insertion rule.

Its purpose is to classify trace-counting branches without assuming GR spatial recombination.

The guiding question was:

```text
What spatial trace is already consumed by A,
and what remains for zeta/kappa?
```

The answer is:

```text
The safest current recombination counting rule is:

  scalar trace in g_ij = A_spatial_once + boundary-neutral trace_volume_residual_once

with:
  no overlap,
  no exterior scalar charge,
  no GR spatial metric import,
  no kappa diagnostic promotion.
```

---

## Why This Study Matters

The recombination projector audit established:

```text
P_recombination is the count-once gate.
```

with provisional bundle:

```text
g_tt <- A
g_0i <- W_i
g_ij <- A_spatial_once + trace_volume_residual_once + h_TT
```

The unresolved bottleneck was whether \(A_{\rm spatial}\) and \(\zeta/\kappa\) represent overlapping scalar spatial trace.

This study turns that bottleneck into explicit branch tests.

---

## Compact Trace-Counting Ledger

| Entry | Branch | Status | Consequence |
|---|---|---|---|
| C1: \(A_{\rm spatial}\) consumes all scalar spatial trace | \(g_{ij}\) scalar trace is fully fixed by \(A\)-sector recovery | SAFE_IF | \(\kappa\) likely diagnostic / residual only; \(\zeta\) volume energy cannot be inserted as independent metric trace |
| C2: \(A_{\rm spatial}\) consumes only mass-sector trace | \(A_{\rm spatial}\) accounts for exterior mass geometry, leaving compensated residual trace / volume freedom | CANDIDATE | \(P_{\rm boundary}P_{\rm trace}\) residual can enter recombination once |
| C3: \(A_{\rm spatial}\) and \(\zeta\) are the same trace variable | \(\zeta\) is the volume expression of the \(A\)-sector spatial response | RISK | \(\zeta\) may become diagnostic / energy bookkeeping for \(A_{\rm spatial}\); \(\kappa\) remains separate or diagnostic |
| C4: \(\kappa\) is only residual after \(A_{\rm spatial}\) and \(\zeta\) | \(A_{\rm spatial}\) and \(\zeta\) define volume geometry; \(\kappa\) tracks mismatch / relaxation only | CANDIDATE | supports \(\kappa\) diagnostic / first-order residual role |
| C5: \(\zeta/\kappa\) boundary residual only | \(\zeta/\kappa\) enter only through compact or boundary-neutral residual correction | CANDIDATE | preserves group-13 volume accounting while minimizing GR-smuggling risk |
| C6: no independent \(A_{\rm spatial}\) derivation | \(A_{\rm spatial}\) is currently recovery bookkeeping, not derived | UNRESOLVED | recombination remains bookkeeping until \(A_{\rm spatial}\) is derived |
| C7: duplicate scalar spatial trace | \(g_{ij}\) includes \(A_{\rm spatial}+\zeta+\kappa\) as independent trace terms | FORBIDDEN | kills the branch unless projection removes two of the three contributions |
| C8: exterior scalar tail from residual | trace-volume residual produces \(\zeta_{\rm ext}\) or \(\kappa_{\rm ext}\sim1/r\) | FORBIDDEN | requires \(P_{\rm boundary}\) or branch rejection |
| C9: energy accounting mismatch | metric count-once but \(\epsilon/e_\kappa\) count twice, or metric double-counts while energy counts once | REQUIRED | forces either \(\kappa\) diagnostic status or absorbed / unified energy convention |
| C10: areal diagnostic caution | \(\kappa=\frac12\ln(AB)\) used as reduced diagnostic only | CONSTRAINED | suggests a later diagnostic-vs-physical \(\kappa\) script remains useful |
| C11: best provisional counting convention | \(A_{\rm spatial,once}+\) boundary-neutral trace-volume residual once | RECOMMENDED | use as working recombination convention until \(A_{\rm spatial}\) theorem is derived |
| C12: theorem target | \({\rm Trace}[g_{ij}^{\rm scalar}]={\rm Trace}_{A,{\rm mass}}+{\rm Trace}_{\rm residual,neutral}\), with no overlap | THEOREM_TARGET | defines the central future recombination theorem |

---

## Status Counts

The run counted:

```text
CANDIDATE:      3
CONSTRAINED:    1
FORBIDDEN:      2
RECOMMENDED:    1
REQUIRED:       1
RISK:           1
SAFE_IF:        1
THEOREM_TARGET: 1
UNRESOLVED:     1
```

Interpretation:

```text
The recombination search now turns on A_spatial.
If A_spatial consumes all scalar spatial trace, zeta/kappa must become diagnostic or residual only.
If A_spatial consumes only mass-sector trace, a boundary-neutral zeta/kappa residual may survive.
Triple scalar trace insertion is forbidden.
```

---

## Provisional Count-Once Rule

Recommended provisional rule:

\[
{\rm Trace}[g_{ij}^{\rm scalar}]
=
A_{\rm spatial,once}
+
{\rm trace\_volume\_residual}_{\rm once}.
\]

where:

```text
A_spatial_once = mass-sector spatial trace required by A-sector recovery.
```

and:

```text
trace_volume_residual_once = boundary-neutral zeta/kappa residual, if any.
```

The overlap condition is:

\[
{\rm overlap}
(
A_{\rm spatial,once},
{\rm trace\_volume\_residual}_{\rm once}
)
=
0.
\]

Status:

```text
THEOREM TARGET / NOT DERIVED RECOMBINATION LAW
```

---

## Failure Controls

Trace counting fails if:

1. \(A_{\rm spatial}\), \(\zeta\), and \(\kappa\) are all inserted as independent scalar traces.
2. \(\zeta/\kappa\) residual has exterior \(1/r\) charge.
3. \(A_{\rm spatial}\) is copied from GR and called derived.
4. \(\kappa=\frac12\ln(AB)\) is promoted from diagnostic without proof.
5. Metric recombination and \(\epsilon/e_\kappa\) accounting disagree.
6. Boundary-neutral residual changes \(M_{\rm ext}\).
7. Overlap between \(A_{\rm spatial}\) and residual trace remains nonzero.

---

## What This Study Established

This study established that the recombination branch has narrowed to one central count-once theorem target:

\[
{\rm Trace}[g_{ij}^{\rm scalar}]
=
{\rm Trace}_{A,{\rm mass}}
+
{\rm Trace}_{\rm residual,neutral},
\]

with:

\[
{\rm overlap}=0.
\]

It also established that triple scalar trace insertion is forbidden:

```text
A_spatial + zeta + kappa
```

cannot be inserted as three independent trace contributions.

---

## What This Study Did Not Establish

This study did not derive \(A_{\rm spatial}\).

It did not derive the residual trace projector.

It did not prove the overlap condition.

It did not prove boundary mass preservation.

It did not decide whether \(\zeta\) is independent, residual, diagnostic, or energy bookkeeping for \(A_{\rm spatial}\).

It did not decide whether \(\kappa\) is physical, residual, or diagnostic.

---

## Current Best Interpretation

The safest current recombination counting rule is:

```text
scalar trace in g_ij = A_spatial_once + boundary-neutral trace_volume_residual_once
```

with:

```text
no overlap,
no exterior scalar charge,
no GR spatial metric import,
no kappa diagnostic promotion.
```

This is a theorem target and working convention, not a derived metric law.

---

## Next Development Target

The next script should be:

```text
candidate_areal_kappa_diagnostic_vs_physical_variable.py
```

Purpose:

```text
Separate kappa = 1/2 ln(AB) diagnostic from physical kappa/zeta response.
```

Reason:

```text
The current counting problem depends on not silently promoting kappa = 1/2 ln(AB)
from reduced diagnostic to physical scalar.
```

Expected result:

```text
A diagnostic-vs-physical ledger:
  areal kappa as reduced diagnostic,
  areal kappa as exterior recovery check,
  areal kappa as physical trace variable risk,
  areal kappa as proxy for zeta,
  residual/relaxation kappa,
  e_kappa consequence,
  forbidden silent covariant promotion,
  recovery constraint versus construction.
```

---

## Summary

The trace-counting result is:

```text
A_spatial and zeta/kappa cannot overlap as scalar spatial trace.
```

The next goblin gate is:

```text
keep areal kappa useful without letting it become a smuggled physical scalar.
```
