# Candidate Recombination Without Double-Counting

## Canonical Filename

```text
candidate_recombination_without_double_counting.md
```

This document summarizes the output of:

```text
candidate_recombination_without_double_counting.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a covariant metric derivation, not a parent identity, and not proof of GR recovery. It does not add a formal commitment to the theory.

Its purpose is to state a disciplined reduced recombination map and its no-double-counting checks.

The guiding question was:

```text
How can A, W_i, h_TT, and kappa recombine without scalar double-counting?
```

The answer is:

```text
A disciplined recombination map is possible only if:
  A carries exterior mass,
  W_i carries transverse vector response,
  h_TT carries trace-free radiation,
  kappa is limited to trace / volume matching,
  scalar response is counted once,
  exterior kappa=0 preserves Schwarzschild,
  scalar radiation stays rejected,
  boundary smoothing preserves M_ext,
  coefficients remain labeled until derived.
```

---

## Why This Study Matters

The boundary mass preservation audit protected the exterior \(A\)-sector mass:

\[
\delta M_{\rm ext}\big|_{\kappa{\rm\ relaxation}}=0,
\]

\[
Q_\kappa=0,
\]

\[
F_\kappa(R+)=0,
\]

\[
\kappa_{\rm ext}\to0.
\]

But recombination can undo that protection if it reintroduces the same scalar response through the metric map.

This study prevents:

```text
A and kappa both carrying rho,
trace stress contaminating h_TT,
longitudinal current entering W_i,
scalar radiation reappearing after metric assembly,
or GR coefficients being imported as derivations.
```

---

## Compact Recombination Ledger

| Recombination Piece | Component | Candidate Form | Status | Missing |
|---|---|---|---|---|
| R1: lapse / time scalar from \(A\) | \(g_{tt}\)-like component | \(g_{tt}\sim-Ac^2\) in reduced / static weak map | DERIVED_REDUCED | covariant parent lapse / recombination map |
| R2: exterior radial reciprocal from \(A\) and \(\kappa\) | \(g_{rr}\)-like radial scalar piece | \(\kappa_{\rm ext}=0\Rightarrow B=1/A\) | DERIVED_REDUCED | gauge / physical split for \(B\) and \(\kappa\) |
| R3: vector shift from \(W_i\) | \(g_{0i}\)-like component | \(g_{0i}\sim\) coefficient \(\times W_i\) | STRUCTURAL | \(\beta_W\), normalization, parent shift map |
| R4: tensor radiation from \(h_{TT}\) | trace-free spatial tensor | \(g_{ij}\) contains \(h_{ij}^{TT}\) as trace-free radiative part | STRUCTURAL | \(C_T,K_T\), tensor action stiffness |
| R5: \(\kappa\) limited to trace / volume matching | scalar spatial / \(AB\) diagnostic role | \(\kappa\) enters \(AB=e^{2\kappa}\) or local trace / volume matching only | CONSTRAINED | \(P_{\rm recombination}\) role of \(\kappa\) |
| R6: scalar response counted once | scalar part of recombined geometry | \(\rho\to A\), trace \(\to\kappa_{\min}\), no duplicate scalar mass channel | REQUIRED | explicit scalar accounting rule in recombination map |
| R7: exterior Schwarzschild preservation | exterior recombined geometry | outside ordinary matter: \(\kappa=0,\;A=1-2GM/(c^2r),\;B=1/A\) | REQUIRED | \(P_{\rm recombination}\) proof |
| R8: scalar radiation excluded after recombination | radiative content | ordinary radiation projector selects \(h_{ij}^{TT}\) only | CONSTRAINED | parent radiation projector |
| R9: boundary smoothing remains local / diagnostic | near-boundary geometry | near-boundary adjustments preserve \(A_{\rm ext}\) coefficient | CONSTRAINED | boundary mass theorem and observable map |
| R10: coefficient map remains labeled | observable coefficients | \(\alpha_W/K_c,\beta_W,C_T,K_T\) remain UNKNOWN / MATCHED until derived | MISSING | \(P_{\rm coeff}\) / action stiffness derivation |

---

## Status Counts

The run counted:

```text
CONSTRAINED:      3
DERIVED_REDUCED:  2
MISSING:          1
REQUIRED:         2
STRUCTURAL:       2
```

Interpretation:

```text
Exterior scalar pieces are reduced-derived.
Vector / tensor / kappa recombination is structural or constrained.
Coefficient mapping remains missing.
```

---

## Candidate Reduced Recombination Map

Candidate reduced map:

```text
g_tt  <- A
g_0i  <- W_i
g_ij  <- scalar_spatial_response(A) + kappa_trace_matching + h_ij^TT
```

with constraints:

```text
rho -> A only
trace / pressure -> kappa_min only
kappa_ext = 0
h_ij^TT trace-free
W_i transverse
source(A_rad ordinary massless)=0
delta M_ext|kappa_relaxation = 0
```

Status:

```text
CANDIDATE / REDUCED MAP
```

This is not a covariant derivation.

---

## No-Double-Counting Checks

Recombination checks:

1. Does \(\rho\) appear anywhere except \(A\)-sector mass response?
2. Does \(\kappa\) produce an exterior \(1/r\) field?
3. Does trace stress enter \(h_{TT}\)?
4. Does \(P_Lj\) enter \(W_i\)?
5. Does boundary smoothing change \(M_{\rm ext}\)?
6. Does \(A_{\rm rad}\) reappear after recombination?
7. Are vector / tensor coefficients labeled rather than imported?
8. Does exterior \(\kappa=0\) preserve \(B=1/A\)?
9. Is scalar spatial response counted exactly once?
10. Is near-boundary deviation still diagnostic-only?

---

## Failure Controls

Recombination fails if:

1. It copies GR metric components and calls them derived.
2. \(A\) and \(\kappa\) both carry the same \(\rho\) scalar response.
3. \(\kappa\) reintroduces exterior scalar charge.
4. \(h_{TT}\) receives trace stress.
5. \(W_i\) receives longitudinal current.
6. Boundary smoothing changes the exterior \(1/r\) coefficient.
7. Scalar radiation appears as \(A_{\rm rad}\) or \(\Box\kappa\).
8. Coefficients are matched but claimed derived.

---

## What This Study Established

This study established that a disciplined reduced recombination map is possible only if:

```text
A carries exterior mass,
W_i carries transverse vector response,
h_TT carries trace-free radiation,
kappa is limited to trace / volume matching,
scalar response is counted once,
exterior kappa=0 preserves Schwarzschild,
scalar radiation stays rejected,
boundary smoothing preserves M_ext,
coefficients remain labeled until derived.
```

It also established that coefficient mapping remains explicitly missing.

---

## What This Study Did Not Establish

This study did not derive covariant recombination.

It did not derive \(P_{\rm recombination}\).

It did not derive \(P_{\rm coeff}\).

It did not derive vector normalization.

It did not derive tensor coupling.

It did not derive tensor flux coefficient.

It did not derive the boundary mass theorem.

It only constrained the recombination map.

---

## Current Best Interpretation

Reduced recombination is allowed only as a disciplined bookkeeping map:

```text
g_tt  <- A,
g_0i  <- W_i,
g_ij  <- scalar_spatial_response(A) + kappa_trace_matching + h_ij^TT.
```

But:

```text
A carries mass,
kappa carries trace / volume matching,
h_TT carries trace-free radiation,
W_i carries transverse current response.
```

The scalar response must be counted exactly once.

---

## Next Development Target

The next script should be:

```text
candidate_relaxation_energy_accounting_identity.py
```

Purpose:

```text
Define the energy destination for Gamma_relax.
```

Reason:

```text
Recombination can be constrained,
but relaxation energy remains explicitly missing.
```

Expected result:

```text
A relaxation-energy ledger:
  Gamma_relax cannot be energy destruction,
  kappa relaxation moves imbalance into vacuum configuration energy,
  exterior M_ext remains fixed under local relaxation,
  ordinary closed-regime total accounting is preserved,
  missing variables are named.
```

---

## Summary

Recombination is not closure.

It is a constrained map.

The next goblin hole is:

```text
Where does relaxation energy go?
```
