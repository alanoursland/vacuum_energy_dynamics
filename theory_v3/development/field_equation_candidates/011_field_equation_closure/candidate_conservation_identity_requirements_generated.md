# Candidate Conservation Identity Requirements

## Canonical Filename

```text
candidate_conservation_identity_requirements.md
```

This document summarizes the output of:

```text
candidate_conservation_identity_requirements.py
```

or a generated equivalent.

---

## What This Document Is

This document is a development note for the `11_field_equation_closure/` group.

It is not a parent identity, not a proof of Bianchi-compatible closure, and not a completed conservation derivation. It does not add a formal commitment to the theory.

Its purpose is to make explicit which parent identities would be required to justify the current constraint / evolution split.

The guiding question was:

```text
What parent identities are required to justify the constraint/evolution split?
```

The answer is:

```text
The sector split is disciplined but not closed.

Closure requires a parent identity that explains:
  constraint propagation,
  source conservation,
  TT-only radiation,
  non-radiative kappa trace relaxation,
  mass preservation,
  ordinary exclusion of Sigma_creation.
```

---

## Why This Study Matters

The previous studies produced a disciplined sector map:

```text
A:
  scalar constraint

B:
  reduced gauge-conditioned companion

W_i:
  transverse vector response

h_ij^TT:
  propagating tensor radiation

kappa:
  non-inertial trace relaxation

A_rad:
  rejected scalar radiation
```

But a disciplined sector map is not closure.

Closure requires an identity that forces the split rather than merely assuming it.

The key warning is:

```text
do not claim closure just because the sector split is organized.
```

---

## Identity Requirement Ledger

| Identity | Required Identity | Enforces | Status | Failure If Missing |
|---|---|---|---|---|
| I1: scalar constraint propagation | time evolution of \(A\) constraint is compatible with continuity of \(\rho\) | \(A\) remains a constraint rather than scalar radiation | UNFINISHED | \(A\) may need a wave equation or violate source conservation |
| I2: mass flux preservation | exterior \(A\) flux / \(M_{\rm ext}\) is invariant under \(\kappa\) boundary relaxation | \(\kappa\) smoothing cannot change measured exterior mass | CONSTRAINED | boundary smoothing tunes gravity by hand |
| I3: current decomposition identity | \(j=P_Tj+P_Lj\), with \(W_i\) sourced only by \(P_Tj\) | transverse current sources \(W_i\); longitudinal current remains scalar continuity | STRUCTURAL | vector and scalar sectors double-count current |
| I4: TT source conservation | TT projection of stress source is compatible with conserved total stress-energy | \(h_{ij}^{TT}\) carries tensor radiation without trace contamination | STRUCTURAL | tensor radiation source may be imported from GR or double-count trace |
| I5: \(\kappa\) non-radiative trace identity | trace / pressure shifts \(\kappa_{\min}\) but does not source \(\Box\kappa\) | \(\kappa\) relaxes locally and does not radiate breathing modes | CONSTRAINED | scalar breathing radiation or hidden \(\kappa\) wave |
| I6: scalar radiation exclusion | source\((A_{\rm rad}\ {\rm ordinary\ massless})=0\) in ordinary closed regime | ordinary long-range radiation is TT-only | CONSTRAINED | unwanted scalar radiation channel |
| I7: ordinary closure excludes creation | \(\Sigma_{\rm creation}=0\) outside active creation / exchange regimes | ordinary gravity remains conservative / closed | CONSTRAINED | nonconservative field equations |
| I8: relaxation energy accounting | \(\Gamma_{\rm relax}\) transfers imbalance into vacuum configuration, not energy loss | \(\kappa\) relaxation is exchange / restoration, not dissipation from total system | STRUCTURAL | cosmetic damping or energy disappearance |
| I9: metric recombination compatibility | sector recombination preserves source split and avoids duplicate scalar response | \(A,W_i,h_{TT},\kappa\) combine without double-counting | UNFINISHED | GR metric imported by hand or scalar trace duplicated |
| I10: Bianchi-like closure target | parent divergence identity implies source conservation and sector constraints | full field system is compatible with conservation | MISSING | theory remains a sector ledger, not a closed field-equation system |

---

## Status Counts

The run counted:

```text
CONSTRAINED: 4
MISSING:     1
STRUCTURAL:  3
UNFINISHED:  2
```

Interpretation:

```text
Most identities are constrained or structural requirements.
The Bianchi-like closure identity remains missing.
```

This means the project has a disciplined requirements list, not a final identity.

---

## Minimal Parent Identity Template

A minimal parent identity must look something like:

```text
divergence(parent field equation) = source balance identity
```

In reduced sector language, it must imply:

```text
A constraint propagation,
W_i transverse current sourcing,
h_ij^TT TT radiation sourcing,
kappa trace relaxation without scalar radiation,
exterior mass preservation,
ordinary Sigma_creation = 0.
```

Status:

```text
UNFINISHED
```

This is a requirement template, not a derivation.

---

## Hardest Requirements

The hardest requirements are:

1. Bianchi-like closure target.
2. Metric recombination compatibility.
3. \(\kappa\) non-radiative trace identity.
4. Tensor coupling / source conservation.
5. Boundary mass preservation.

These are where the reconstruction can still fail.

---

## What This Study Established

This study established:

1. The sector split is disciplined but not closed.
2. \(A\)-constraint propagation must be compatible with source continuity.
3. \(\kappa\) boundary relaxation must preserve exterior mass.
4. Current decomposition must protect the vector sector from scalar-current contamination.
5. TT source conservation must prevent trace contamination of tensor radiation.
6. \(\kappa\) must remain non-radiative even when trace / pressure shifts its local minimum.
7. Ordinary scalar radiation remains excluded.
8. Ordinary gravity must exclude \(\Sigma_{\rm creation}\).
9. Relaxation must be energy-accounted as vacuum exchange / restoration.
10. Metric recombination and Bianchi-like closure remain unfinished.

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not prove Bianchi-compatible closure.

It did not derive source conservation.

It did not derive tensor coupling.

It did not derive \(\kappa\)'s non-radiative identity.

It did not prove boundary mass preservation.

It only listed the identities required before closure can be claimed.

---

## Current Best Interpretation

The project currently has:

```text
a disciplined reduced sector split,
a clear no-double-counting source ledger,
a clear constraint/evolution classification,
and a missing parent conservation identity.
```

That is a good position.

It means the project knows what must be derived next.

But it also means:

```text
field-equation closure is not yet achieved.
```

---

## Next Development Target

The next script should be:

```text
candidate_gr_limit_recovery_audit.py
```

Purpose:

```text
Audit where GR recovery is derived versus matched.
```

Reason:

```text
Before inventing the parent identity, audit which GR limits are actually derived.
```

Expected result:

```text
A table classifying each GR-facing result:
  derived,
  reduced-derived,
  structural,
  matched,
  constrained,
  missing,
  or rejected.
```

---

## Summary

The conservation-identity requirements study gives the group-11 warning:

```text
The sector split is disciplined but not closed.
```

Closure requires the missing parent identity.

Before attempting that identity, the next goblin audit is:

```text
Which GR limits have we really recovered,
and which have we only matched or structured?
```
