# Candidate Correction Tensor Source Separation

## Canonical Filename

```text
candidate_correction_tensor_source_separation.md
```

This document summarizes the output of:

```text
candidate_correction_tensor_source_separation.py
```

## What This Document Is

This document is a Group 19 parent-correction tensor audit artifact.

It is not a source-separation theorem, not a parent field equation, not a projector construction, and not a definition of \(H_{\rm curv}\) or \(H_{\rm exch}\).

Its purpose is to audit whether correction tensors can avoid double-counting ordinary matter and vacuum sources.

The locked-door question was:

```text
Can correction tensors avoid double-counting ordinary matter and vacuum sources?
```

The result is:

```text
Source separation is required but not derived.

Correction tensors cannot double-count:

  ordinary matter
  A-sector mass source
  e_curv accounting
  A_curv diagnostic status
  undefined J_curv
  Sigma/R role labels
  J_V/J_exch role labels
  J_sub/J_exch matter channels
  dark-sector labels
  zeta/B_s residual trace
  boundary failure

Candidate safe routes:

  real projectors
  diagnostic-only H-like objects

Best next script:

  candidate_correction_tensor_boundary_and_mass_neutrality.py
```

## Core Result

Source separation is required but not derived.

A correction tensor cannot safely enter the parent equation if it hides source overlap between:

```text
ordinary matter,
A-sector mass,
curvature accounting,
curvature admissibility,
undefined curvature current,
exchange source/relaxation labels,
vacuum-current role labels,
dark-sector labels,
metric insertion / residual trace,
or boundary failure.
```

The current safest routes are:

```text
real projectors,
diagnostic-only H-like objects.
```

## Compact Source-Separation Ledger

| Entry | Rule | Status | Consequence |
|---|---|---|---|
| SS1: source-separation target | correction tensors must not double-count ordinary matter, curvature accounting, exchange sources, metric insertion, residual trace, dark sector, or boundary sources | THEOREM_TARGET | decides whether correction tensors can enter parent equation without double-counting |
| SS2: ordinary matter routing | ordinary \(T_{\mu\nu}\) / \(\rho\) / scalar charge remains routed through established ordinary source side | REQUIRED | protects ordinary matter coupling and A-sector mass result |
| SS3: A-sector mass protection | A-sector mass result is not modified by correction tensor source accounting | REQUIRED | protects strongest reduced reconstruction result |
| SS4: \(e_{\rm curv}\) not source reservoir | \(e_{\rm curv}\) remains diagnostic/accounting and is not placed inside \(H_{\rm curv}\) as stress/source reservoir | REQUIRED | preserves Group 17 closure |
| SS5: \(A_{\rm curv}\) diagnostic limit | \(A_{\rm curv}\) remains diagnostic/branch-filter unless dynamics are derived | REQUIRED | prevents anti-singularity source smuggling |
| SS6: \(J_{\rm curv}\) absence | \(J_{\rm curv}\) is not defined and cannot be counted as source/current for \(H_{\rm curv}\) | REQUIRED | preserves curvature-current unresolved status |
| SS7: \(\Sigma/R\) not tuning knobs | \(\Sigma/R\) are not coefficients, cancellation knobs, or hidden tuning terms inside \(H_{\rm exch}\) | REQUIRED | prevents exchange source double-counting |
| SS8: \(J_V/J_{\rm exch}\) unresolved guard | \(J_V\) and \(J_{\rm exch}\) are not defined enough to source \(H_{\rm exch}\) | REQUIRED | preserves Group 18 role-level split |
| SS9: \(J_{\rm sub}/J_{\rm exch}\) not ordinary matter channels | \(J_{\rm sub}\) and \(J_{\rm exch}\) do not become ordinary matter coupling channels through correction tensors | REQUIRED | prevents current split from becoming source overlap |
| SS10: dark sector not ordinary relabel | dark-sector source is absent/deferred and cannot relabel ordinary matter or ordinary exchange failure | REQUIRED | preserves no-dark-patch rule |
| SS11: \(\zeta/B_s\) insertion not reopened | correction tensors do not reopen \(B_s/F_\zeta\) insertion or residual metric trace | REQUIRED | preserves Group 16 guardrails |
| SS12: residual killed/non-metric unless \(O\) derived | residual \(\zeta/\kappa\) trace remains killed or non-metric unless no-overlap operator is derived | REQUIRED | prevents hidden scalar source restoration |
| SS13: boundary source not counted as tensor correction | boundary leakage, shell source, scalar tail, or mass shift cannot be reclassified as \(H\) source | REQUIRED | prevents boundary repair as source separation |
| SS14: coefficient source separation | correction tensor coefficients are not fitted from overlapping source sectors | REQUIRED | prevents coefficient-level double-counting |
| SS15: projected source separation candidate | defined projectors separate ordinary, curvature, exchange, residual, and dark sectors | CANDIDATE | possible future no-double-counting route |
| SS16: diagnostic-only separation fallback | \(H\)-like objects remain diagnostic-only and therefore do not source or double-count | SAFE_IF | allows source audits without source overlap |
| SS17: ordinary \(T\) inside \(H_{\rm exch}\) by fiat rejection | ordinary \(T_{\mu\nu}\) appears inside \(H_{\rm exch}\) as exchange source by convenience | REJECTED | prevents ordinary matter double-counting |
| SS18: \(e_{\rm curv}\) inside \(H_{\rm curv}\) source reservoir rejection | \(e_{\rm curv}\) is inserted into \(H_{\rm curv}\) as source reservoir | REJECTED | prevents curvature energy reservoir |
| SS19: \(\Sigma/R\) inside \(H_{\rm exch}\) coefficient knobs rejection | \(\Sigma/R\) are hidden inside \(H_{\rm exch}\) as adjustable coefficient knobs | REJECTED | prevents source/relaxation double-counting |
| SS20: residual restored through tensor correction rejection | \(B_s/F_\zeta\) residual trace is restored through correction tensor after being killed/non-metric | REJECTED | prevents scalar trace resurrection |
| SS21: dark sector relabels ordinary matter rejection | dark-sector source is ordinary matter or ordinary exchange failure under a new name | REJECTED | prevents dark patch |
| SS22: boundary source counted as tensor correction rejection | boundary leakage/shell/scalar tail is counted as correction tensor source | REJECTED | prevents boundary repair tensor |
| SS23: source-separation failure | correction tensors cannot avoid ordinary/vacuum/source overlap | BRANCH_KILLED | correction tensors cannot be inserted |
| SS24: recommended next move | after source separation, audit boundary and mass neutrality | RECOMMENDED | next script should be `candidate_correction_tensor_boundary_and_mass_neutrality.py` |

## Status Counts

```text
BRANCH_KILLED: 1
CANDIDATE:     1
RECOMMENDED:   1
REJECTED:      6
REQUIRED:      13
SAFE_IF:       1
THEOREM_TARGET:1
```

Interpretation:

```text
Source separation is required but not derived.

Ordinary matter must stay in ordinary source routing
and A-sector mass accounting must remain protected.

e_curv cannot become H_curv source reservoir.

Sigma/R cannot become H_exch tuning knobs.

J_sub/J_exch cannot become ordinary matter channels.

Dark sector cannot relabel ordinary matter or ordinary exchange failure.

zeta/B_s insertion and residual trace cannot be reopened by correction tensor.

Boundary failure cannot be reclassified as correction tensor source.

Projected source separation is a candidate only if projectors are real.

Diagnostic-only remains the safest fallback.

Next gate is boundary and mass neutrality.
```

## Required Separations

```text
1. ordinary matter vs correction tensors
2. A-sector mass source vs H sources
3. e_curv accounting vs H_curv source
4. A_curv diagnostic vs H_curv dynamics
5. J_curv absence vs H_curv current
6. Sigma/R role labels vs H_exch source/relaxation operators
7. J_V/J_exch role labels vs H_exch current
8. J_sub/J_exch vs ordinary matter channels
9. dark sector vs ordinary matter relabel
10. zeta/B_s insertion vs residual trace restoration
11. boundary source vs tensor correction
```

Candidate safe routes:

```text
1. real projectors
2. diagnostic-only H-like objects
```

## Source-Separation Decision Tree

```text
1. Source sectors have real projectors / routing:
   projected source-separation candidate survives.

2. H-like object is diagnostic-only:
   safe if never inserted.

3. H_curv uses e_curv, A_curv, or J_curv as source without derivation:
   rejected or deferred.

4. H_exch uses Sigma/R or J_exch as source without derivation:
   rejected or deferred.

5. H reroutes ordinary matter, dark sector, residual trace, or boundary leakage:
   rejected.

6. Source separation cannot be proven:
   keep correction tensors deferred.
```

## Good Failure / Branch Decision

Good failure:

```text
correction tensors cannot avoid source overlap because source routing,
projectors, current objects, or boundary neutrality are missing.
```

Consequence:

```text
keep H_curv/H_exch deferred or diagnostic-only.
do not insert correction tensors into parent equation.
```

Bad failure:

```text
hide source overlap inside H_curv/H_exch coefficients or projector labels.
```

## Failure Controls

Source separation fails if:

1. ordinary matter appears inside \(H_{\rm curv}/H_{\rm exch}\).
2. A-sector mass accounting is changed.
3. \(e_{\rm curv}\) becomes source reservoir.
4. \(A_{\rm curv}\) diagnostic becomes dynamics.
5. \(J_{\rm curv}\) is used by name.
6. \(\Sigma/R\) become tuning knobs.
7. \(J_V/J_{\rm exch}\) role labels become source currents.
8. \(J_{\rm sub}/J_{\rm exch}\) become matter channels.
9. dark sector relabels ordinary matter.
10. \(\zeta/B_s\) insertion is reopened.
11. residual trace is restored.
12. boundary failure becomes source.
13. projectors are invented after overlap.
14. coefficients absorb overlap.

## What This Study Established

This study established that source separation is required but not derived.

It also established that correction tensors cannot be used to hide source overlap.

## What This Study Did Not Establish

This study did not prove source separation.

It did not define projectors.

It did not define \(H_{\rm curv}\).

It did not define \(H_{\rm exch}\).

It did not derive source routing.

It did not prove ordinary matter separation.

It did not prove mass neutrality.

It did not prove scalar-trace neutrality.

It did not prove boundary neutrality.

It did not justify insertion into a parent field equation.

## Current Best Interpretation

```text
Correction tensors may not touch source sectors yet.

They remain deferred or diagnostic-only unless real projectors
or source-routing theorems prevent overlap.
```

## Next Development Target

The next script should be:

```text
candidate_correction_tensor_boundary_and_mass_neutrality.py
```

Purpose:

```text
Audit whether H_curv/H_exch avoid boundary repair and exterior mass shift.
```

Reason:

```text
Source separation is not enough if the tensor repairs boundary behavior
or shifts exterior mass.

The next gate is boundary/mass neutrality.
```

Expected result:

```text
A correction tensor boundary/mass neutrality ledger:
  no M_ext shift independent of A,
  no boundary counterterm,
  no exterior scalar charge,
  no far-zone hidden flux,
  no shell source by support,
  no recovery-tuned boundary smoothing,
  no dark boundary patch,
  no anti-singularity by boundary tensor,
  diagnostic-only correction tensor,
  interior-only branch filter,
  compact support with structural zero-flux,
  identically divergence-free interior tensor,
  source-balanced tensor with neutral boundary.
```

## Summary

The source-separation result is:

```text
No double-counting coins.
No hidden matter in the tensor sack.
No boundary leak renamed as source.
```

Tiny goblin plaque:

```text
Keep the coin piles separate.
A painted sack is not a new treasury.
