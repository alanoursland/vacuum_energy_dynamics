# Candidate Recombination Projector For Trace Volume

## Canonical Filename

```text
candidate_recombination_projector_for_trace_volume.md
```

This document summarizes the output of:

```text
candidate_recombination_projector_for_trace_volume.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a covariant recombination law, not a parent metric derivation, and not a final sector assembly rule.

Its purpose is to define what \(P_{\rm recombination}\) must do so that \(A\), \(\zeta\), and \(\kappa\) enter the geometry once, and only once.

The guiding question was:

```text
How do A, zeta, and kappa assemble into the metric once, and only once?
```

The answer is:

```text
P_recombination is the count-once gate:

  g_tt <- A
  g_0i <- W_i
  g_ij <- A_spatial_once + trace_volume_residual_once + h_TT

Main unresolved issue:

  What spatial trace belongs to A,
  and what remains for zeta/kappa?
```

---

## Why This Study Matters

The boundary projector split clarified that \(P_{\rm boundary}\) owns:

```text
exterior zeta/kappa neutrality,
zero boundary flux,
zero volume/kappa charge,
A-sector mass protection,
shell-source avoidance.
```

After that split, the next danger became recombination double-counting.

The theory must not assemble:

```text
A-sector spatial response,
zeta volume response,
and kappa residual response
```

as three independent scalar spatial traces.

That would turn a count-once scalar response into multiple scalar gravities.

---

## Compact \(P_{\rm recombination}\) Ledger

| Entry | Requirement | Status | Missing |
|---|---|---|---|
| R1: \(A\)-sector time response | \(g_{tt}\leftarrow A\) | STRUCTURAL | covariant recombination map |
| R2: \(A\)-sector spatial companion | \(g_{ij}\) may include scalar spatial response required by \(A\)-sector geometry | UNRESOLVED | which spatial trace belongs to \(A\) versus \(\zeta/\kappa\) |
| R3: \(\zeta\) volume response | \(\zeta\) enters as volume-form configuration only once | REQUIRED | metric insertion rule for \(\zeta\) |
| R4: \(\kappa\) residual / diagnostic response | \(\kappa\) enters as projected residual, diagnostic, or relaxation coordinate | REQUIRED | \(\kappa\)-\(\zeta\) map and energy convention |
| R5: count-once trace / volume rule | \({\rm Trace}[g_{ij}\ {\rm scalar\ sector}]\) equals one assembled trace / volume response | REQUIRED | explicit projection formula |
| R6: boundary-neutral input | \(P_{\rm recombination}\) receives \(P_{\rm boundary}P_{\rm trace}\) output | REQUIRED | composition order |
| R7: TT trace-free insertion | \(g_{ij}\leftarrow\ldots+h_{ij}^{TT}\), with \(\gamma^{ij}h_{ij}^{TT}=0\) | STRUCTURAL | nonlinear / covariant TT recombination |
| R8: vector insertion | \(g_{0i}\leftarrow W_i\) | STRUCTURAL | covariant vector recombination and normalization |
| R9: no scalar wave insertion | no \(A_{\rm rad}\), no \(\Box\kappa\), no \(\Box\zeta\) contribution inserted into metric | FORBIDDEN | parent scalar-radiation exclusion |
| R10: \(\epsilon/e_\kappa\) accounting compatibility | metric assembly must match energy accounting convention | REQUIRED | degree-of-freedom accounting |
| R11: areal diagnostic compatibility | \(\kappa=\frac12\ln(AB)\) remains reduced diagnostic unless promoted | CONSTRAINED | areal diagnostic versus physical variable split |
| R12: recommended provisional recombination rule | \(g_{tt}\leftarrow A\), \(g_{0i}\leftarrow W_i\), \(g_{ij}\leftarrow A_{\rm spatial,once}+\) boundary-neutral trace / volume residual once \(+h_{TT}\) | RECOMMENDED | explicit covariant parent recombination |

---

## Status Counts

The run counted:

```text
CONSTRAINED:  1
FORBIDDEN:    1
RECOMMENDED:  1
REQUIRED:     5
STRUCTURAL:   3
UNRESOLVED:   1
```

Interpretation:

```text
P_recombination is the count-once gate.
The major unresolved issue is A_spatial versus zeta/kappa trace volume response.
Recombination must match energy accounting or the theory double-counts even if projectors look clean.
```

---

## Minimal \(P_{\rm recombination}\) Requirement Bundle

Current provisional bundle:

```text
g_tt <- A
g_0i <- W_i
g_ij <- A_spatial_once + trace_volume_residual_once + h_TT
```

where:

```text
trace_volume_residual_once <- P_boundary P_trace
```

or:

```text
trace_volume_residual_once <- P_boundary P_relax P_trace
```

and:

```text
h_TT is trace-free,
W_i is transverse,
no A_rad / Box kappa / Box zeta is inserted.
```

Status:

```text
RECOMMENDED / PROVISIONAL
```

This is recombination bookkeeping, not a derived covariant metric law.

---

## Main Unresolved Issue

The main unresolved issue is:

```text
What spatial trace belongs to A,
and what remains for zeta/kappa?
```

This is now the bottleneck because \(A\) already carries the exterior mass response.

If the \(A\)-sector already forces the scalar spatial trace required for exterior recovery, then \(\zeta/\kappa\) cannot add an independent scalar spatial trace without double-counting.

If the \(A\)-sector only accounts for the mass-sector spatial response, then \(\zeta/\kappa\) may survive as a boundary-neutral residual.

This must be tested directly.

---

## Failure Controls

\(P_{\rm recombination}\) fails if:

1. \(A\) spatial response, \(\zeta\), and \(\kappa\) all add the same trace.
2. \(\kappa\) becomes an independent exterior scalar gravity.
3. \(\zeta\) creates exterior scalar charge.
4. \(h_{TT}\) contributes trace volume.
5. \(W_i\) receives longitudinal / scalar current.
6. A scalar breathing mode is inserted.
7. Boundary neutrality is undone during metric assembly.
8. Metric count-once rule conflicts with \(\epsilon/e_\kappa\) energy accounting.
9. Reduced areal \(\kappa\) diagnostic is treated as covariant physical scalar without derivation.

---

## What This Study Established

This study established \(P_{\rm recombination}\) as the count-once gate.

The provisional recombination bundle is:

```text
g_tt <- A
g_0i <- W_i
g_ij <- A_spatial_once + trace_volume_residual_once + h_TT
```

It also established that the major unresolved recombination bottleneck is:

```text
A_spatial versus zeta/kappa trace volume response.
```

---

## What This Study Did Not Establish

This study did not derive \(P_{\rm recombination}\).

It did not derive the \(A\)-sector spatial companion.

It did not derive the metric insertion rule for \(\zeta\).

It did not decide whether \(\kappa\) is diagnostic, residual, energetic, or physical.

It did not derive the composition order:

```text
P_boundary P_trace
```

versus:

```text
P_boundary P_relax P_trace.
```

It did not prove that the recombination map is covariant.

---

## Current Best Interpretation

\(P_{\rm recombination}\) should currently be treated as:

```text
a count-once recombination requirement,
not a derived metric law.
```

It receives boundary-neutral trace / volume input and assembles it with \(A\), \(W_i\), and \(h_{TT}\) without duplicate scalar trace.

The biggest unsolved counting question is:

```text
Does A_spatial already consume the scalar spatial trace,
or is there a genuine boundary-neutral zeta/kappa residual left to recombine?
```

---

## Next Development Target

The next script should be:

```text
candidate_A_spatial_vs_zeta_trace_counting.py
```

Purpose:

```text
Focus on whether A spatial curvature and zeta volume configuration overlap.
```

Reason:

```text
The unresolved recombination bottleneck is whether A_spatial and zeta/kappa trace-volume response overlap.
```

Expected result:

```text
A counting ledger:
  A_spatial consumes all scalar spatial trace,
  A_spatial consumes only mass-sector trace,
  zeta/kappa survives as boundary-neutral residual,
  kappa becomes diagnostic only,
  epsilon/e_kappa accounting compatibility,
  forbidden duplicate scalar spatial trace.
```

---

## Summary

The recombination result is:

```text
P_recombination is the count-once gate.
```

The next goblin gate is:

```text
what scalar spatial trace is already consumed by A?
```
