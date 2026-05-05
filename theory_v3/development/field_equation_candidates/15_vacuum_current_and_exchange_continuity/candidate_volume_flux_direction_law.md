# Candidate Volume Flux Direction Law

## Canonical Filename

```text
candidate_volume_flux_direction_law.md
```

This document summarizes the output of:

```text
candidate_volume_flux_direction_law.py
```

## What This Document Is

This document is a development note for the `15_vacuum_current_and_exchange_continuity/` group.

It is not a derivation of \(J_V^\mu\), not a completed transport law, and not a definition of \(u_{\rm vac}^\mu\).

Its purpose is to test what determines the direction of \(J_V\), after the \(\Sigma_V/R_V\) split established that the source side can provide divergence but not a vector current.

The guiding question was:

```text
How does a scalar creation / relaxation balance become a vector current?
```

The answer is:

```text
The source side gives divergence, not direction.

J_V needs an independent flux / transport law.

If a direction candidate survives, the next missing object is:
  timelike / nonzero domain

Best next test:
  candidate_timelike_domain_for_volume_current.py
```

## Why This Study Matters

The exchange-continuity structure:

```text
nabla_mu J_V^mu = Sigma_V - R_V
```

can constrain a current, but it does not define a current.

This run prevents the false move:

```text
Sigma_V - R_V supplies the direction of J_V.
```

It does not. A scalar source term supplies divergence strength. A vector current needs a direction / transport law.

## Compact Flux-Direction Ledger

| Entry | Direction Law | Status | Consequence |
|---|---|---|---|
| FD1: flux-direction target | \(J_V\) must have a direction / transport law in addition to \(\nabla\cdot J_V=\Sigma_V-R_V\) | THEOREM_TARGET | decides whether \(J_V\) can become more than a divergence placeholder |
| FD2: scalar source insufficiency | \(\Sigma_V-R_V\) supplies divergence strength, not vector direction | REQUIRED | prevents scalar source from masquerading as \(J_V\) |
| FD3: zeta-gradient flux | \(J_V^\mu\sim-D_z\nabla^\mu\zeta\) | RISK | tempting but likely not a general \(u_{\rm vac}\)-defining current |
| FD4: exchange-potential flux | \(J_V^\mu\sim-D_V\nabla^\mu\Phi_V\) | CANDIDATE | could define direction if exchange potential becomes real |
| FD5: source-gradient flux | \(J_V^\mu\) follows gradient of \(\Sigma_V\) or source density / support profile | RISK | may localize redistribution but can become repair current |
| FD6: relaxation-gradient flux | \(J_V^\mu\) follows gradient of relaxation target, e.g. \(\nabla(\zeta-\zeta_{\min})\) | RISK | could align flux with \(R_V\), but risks coefficient / boundary patching |
| FD7: causal transport current | \(J_V\) obeys first-order transport with finite characteristic speed | CANDIDATE | stronger than elliptic repair but requires new dynamics |
| FD8: zero-flux local exchange | \(J_V=0\) locally while \(\Sigma_V=R_V\) pointwise | SAFE_IF | protects exterior neutrality but cannot define \(u_{\rm vac}\) from \(J_V\) |
| FD9: compact-support redistribution | \(J_V\) nonzero only inside compact support with zero boundary flux | CANDIDATE | can preserve exterior neutrality but still needs internal direction law |
| FD10: elliptic repair current | choose \(J_V\) by solving \(\nabla\cdot J_V=\Sigma_V-R_V\) after the fact | RISK | may be diagnostic but does not define real flux |
| FD11: acausal repair current | \(J_V\) chosen nonlocally to cancel scalar charge or enforce exterior neutrality | REJECTED | would make exchange continuity a boundary-tuning device |
| FD12: boundary neutrality requirement | any flux law must have zero exterior scalar charge / zero forbidden far-zone flux | REQUIRED | kills flux laws that become scalar gravity |
| FD13: no-overlap requirement | \(J_V\)-driven \(\zeta\) enters metric only through \(B_s\), or residual trace killed / non-metric | REQUIRED | prevents current from reintroducing \(\zeta/\kappa\) scalar duplicate |
| FD14: timelike-domain dependency | after a flux law survives, test \(J_V^2<0\), \(J_V\neq0\) where \(u_{\rm vac}\) is used | REQUIRED | sets next script if a direction candidate survives |
| FD15: recovery downstream | \(\gamma_{\rm like}\) and \(AB\) checked only after flux, \(\Sigma/R\), and domain are defined | RECOVERY_TARGET | keeps recovery from becoming construction |
| FD16: recommended next move | if a direction candidate survives, test timelike / nonzero domain for \(J_V\) | RECOMMENDED | next script should test whether surviving \(J_V\) candidates can define \(u_{\rm vac}\) |

## Status Counts

```text
CANDIDATE:       3
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        4
RISK:            4
SAFE_IF:         1
THEOREM_TARGET:  1
```

Interpretation:

```text
Scalar Sigma_V - R_V does not determine J_V direction.
Zeta-gradient, source-gradient, and relaxation-gradient fluxes are risky.
Exchange-potential and causal-transport currents are candidates if their mechanisms are defined.
Zero-flux local exchange is safe for neutrality but cannot define u_vac from J_V.
If a current survives, the next bottleneck is timelike / nonzero domain.
```

## Direction Decision Tree

```text
1. Zeta-gradient flux:
   tempting minimal law, but likely domain-limited and scalar-flux risky.

2. Exchange-potential flux:
   candidate only if Phi_V is independently defined.

3. Source-gradient / relaxation-gradient flux:
   may localize flow, but risks patching boundary behavior.

4. Causal transport:
   strongest physical current if derived, but introduces new dynamics.

5. Zero-flux local exchange:
   safe but cannot define u_vac by normalized J_V.

6. Acausal repair current:
   rejected.
```

## Good Failure / Branch Decision

Good failure:

```text
no flux direction can be specified without acausal repair,
recovery tuning, exterior scalar charge, or residual trace overlap.
```

Consequence:

```text
J_V remains a theorem target.
Exchange continuity cannot yet define u_vac.
```

Bad failure:

```text
solve div J_V = Sigma_V - R_V after the fact
and call that the current law.
```

## Failure Controls

Flux-direction law fails if:

1. Scalar \(\Sigma_V-R_V\) is treated as vector direction.
2. Direction is chosen from \(\gamma_{\rm like}\) or \(AB\).
3. Direction is chosen to cancel exterior scalar charge.
4. Zeta-gradient flux creates far-zone scalar flux.
5. Elliptic repair is promoted to physical transport.
6. Causal transport becomes \(\Box\zeta\) or scalar radiation.
7. \(J_V\) creates residual metric trace outside \(B_s\).
8. Boundary neutrality is absent.
9. Timelike / nonzero domain is skipped.

## What This Study Established

This study established that:

```text
Sigma_V - R_V gives divergence, not direction.
```

A viable \(J_V\) needs an independent flux / transport law.

## What This Study Did Not Establish

This study did not define \(J_V^\mu\).

It did not derive a flux direction.

It did not define \(\Phi_V\).

It did not define causal transport.

It did not prove boundary neutrality.

It did not prove no-overlap.

It did not test timelike / nonzero domain.

## Current Best Interpretation

```text
J_V remains a theorem target until a candidate direction also has a valid domain.
```

The next local test is:

```text
candidate_timelike_domain_for_volume_current.py
```

## Next Development Target

The next script should be:

```text
candidate_timelike_domain_for_volume_current.py
```

Purpose:

```text
Test J_V^2 < 0 and J_V != 0 for surviving current candidates.
```

Reason:

```text
If the flux-direction inventory leaves candidate currents alive,
the next gate is whether any can define u_vac through a timelike / nonzero domain.
```

Expected result:

```text
A timelike-domain ledger:
  zeta-gradient current domain,
  exchange-potential current domain,
  causal transport current domain,
  compact-support redistribution domain,
  zero-current equilibrium domain,
  spacelike/null/zero current failure,
  domain-limited u_vac,
  equilibrium-frame fallback,
  boundary/no-overlap requirements,
  next static-source neutrality test if a domain survives.
```

## Summary

The flux-direction result is:

```text
The source side gives divergence, not direction.
```

The next goblin gate is:

```text
if a current points somewhere,
can it actually carry a vacuum clock?
```
