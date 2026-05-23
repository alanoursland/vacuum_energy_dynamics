# Candidate Timelike Domain For Volume Current

## Canonical Filename

```text
candidate_timelike_domain_for_volume_current.md
```

This document summarizes the output of:

```text
candidate_timelike_domain_for_volume_current.py
```

## What This Document Is

This document is a development note for the `15_vacuum_current_and_exchange_continuity/` group.

It is not a derivation of \(J_V^\mu\), not a proof of a global vacuum rest frame, and not a completed exchange-continuity law.

Its purpose is to ask a narrower domain question:

```text
Where, if anywhere, can a surviving J_V candidate define u_vac?
```

The guiding condition was:

```text
J_V^2 < 0
J_V != 0
```

wherever:

```text
u_vac = J_V / sqrt(-J_V^2)
```

is used.

The answer is:

```text
J_V defines u_vac only on a timelike / nonzero domain.

Best current interpretation:
  u_vac is domain-limited unless a separate equilibrium-frame rule is derived.

Best next test:
  candidate_static_source_neutrality_for_J_V.py
```

## Why This Study Matters

The flux-direction inventory established that \(\Sigma_V-R_V\) supplies divergence strength, not vector direction.

This run adds the next viability gate: even a direction candidate is not enough. To define a vacuum rest frame by normalization, the current must be timelike and nonzero in the region where the frame is used.

This prevents the false move:

```text
normalize J_V everywhere,
even where J_V is spacelike, null, or zero.
```

## Compact Timelike-Domain Ledger

| Entry | Domain Test | Status | Consequence |
|---|---|---|---|
| TD1: timelike-domain target | \(J_V^2<0\), \(J_V\neq0\) where \(u_{\rm vac}=J_V/\sqrt{-J_V^2}\) is used | THEOREM_TARGET | decides whether \(J_V\) can define \(u_{\rm vac}\) anywhere useful |
| TD2: zeta-gradient current domain | \(J_V^\mu\sim-D_z\nabla^\mu\zeta\) requires \((\nabla\zeta)^2<0\), \(\nabla\zeta\neq0\) | RISK | likely domain-limited, not a general vacuum clock |
| TD3: exchange-potential current domain | \(J_V^\mu\sim-D_V\nabla^\mu\Phi_V\) requires \((\nabla\Phi_V)^2<0\) and \(\Phi_V\) defined | CANDIDATE | could define \(u_{\rm vac}\) only if exchange potential has clock-like gradient |
| TD4: causal transport current domain | transport \(J_V\) has causal / timelike current with finite characteristic speed | CANDIDATE | strong candidate if it avoids scalar wave behavior |
| TD5: compact-support redistribution domain | \(J_V\) timelike / nonzero only inside compact active region; zero boundary flux | SAFE_IF | may define local \(u_{\rm vac}\), but not a global vacuum clock |
| TD6: zero-flux local equilibrium | \(J_V=0\) in static / local equilibrium while \(\Sigma_V=R_V\) pointwise | SAFE_IF | protects neutrality but forces \(u_{\rm vac}\) fallback outside current definition |
| TD7: spacelike redistribution current | \(J_V^2>0\) in spatial redistribution regimes | CONSTRAINED | \(J_V\) may exist as redistribution current without defining \(u_{\rm vac}\) |
| TD8: null transition current | \(J_V^2=0\) at transition or boundary surfaces | RISK | creates boundaries where vacuum clock is undefined |
| TD9: vanishing-current nodes | \(J_V=0\) at equilibrium nodes, centers, or exterior | REQUIRED | prevents false global vacuum rest frame |
| TD10: domain-limited \(u_{\rm vac}\) | \(u_{\rm vac}\) exists only on \(D_V=\{J_V^2<0,\;J_V\neq0\}\) | CANDIDATE | may save \(J_V\) definition by limiting where clock is used |
| TD11: equilibrium-frame fallback | where \(J_V=0\), define vacuum frame by equilibrium/minimization rather than current | DEFER | may be needed if static regions require \(u_{\rm vac}\) but have \(J_V=0\) |
| TD12: boundary neutrality requirement | candidate domain must not create exterior scalar charge or forbidden far-zone flux | REQUIRED | kills timelike domains that become scalar gravity |
| TD13: no-overlap requirement | \(J_V\)-driven \(\zeta\) enters metric only through \(B_s\), or residual killed / non-metric | REQUIRED | prevents current-defined frame from reviving scalar duplicate |
| TD14: recovery downstream | \(\gamma_{\rm like}\) and \(AB\) checked only after direction and domain are fixed | RECOVERY_TARGET | keeps recovery from choosing the current domain |
| TD15: recommended next move | if domain survives, test static-source neutrality for \(J_V/\Sigma/R\) | RECOMMENDED | next script should test whether the candidate current produces exterior scalar charge around static sources |

## Status Counts

```text
CANDIDATE:       3
CONSTRAINED:     1
DEFER:           1
RECOMMENDED:     1
RECOVERY_TARGET: 1
REQUIRED:        3
RISK:            2
SAFE_IF:         2
THEOREM_TARGET:  1
```

Interpretation:

```text
J_V can define u_vac only where J_V is timelike and nonzero.
Zeta-gradient and null/transition domains are risky.
Compact-support domains may be safe but only define local u_vac.
Zero-flux equilibrium protects neutrality but cannot define u_vac from J_V.
If a domain survives, static-source neutrality is the next bottleneck.
```

## Domain Decision Tree

```text
1. Timelike / nonzero current:
   u_vac can be defined on that active domain.

2. Spacelike current:
   may be a spatial redistribution flux, not a vacuum clock.

3. Null current:
   transition / boundary zone; u_vac undefined unless separate limit rule exists.

4. Zero current:
   equilibrium / no-flux zone; u_vac cannot be normalized from J_V.

5. Domain-limited u_vac:
   acceptable only if equations do not need u_vac outside domain.

6. Equilibrium-frame fallback:
   deferred unless static regions require a frame.
```

## Good Failure / Branch Decision

Good failure:

```text
surviving J_V candidates are spacelike, null, or zero in the regimes
where u_vac is needed.
```

Consequence:

```text
J_V cannot define u_vac there.
Exchange continuity remains a theorem target
or requires equilibrium-frame fallback.
```

Bad failure:

```text
normalize J_V anyway and pretend the vacuum clock exists globally.
```

## Failure Controls

Timelike-domain test fails if:

1. \(J_V\) is normalized where \(J_V^2\ge0\).
2. \(J_V\) is normalized where \(J_V=0\).
3. Zeta-gradient current is used outside timelike / nonzero domain.
4. Global \(u_{\rm vac}\) is claimed from compact / local current.
5. Equilibrium regions require \(u_{\rm vac}\) but have no fallback.
6. Boundary neutrality is absent.
7. No-overlap is absent.
8. Recovery checks choose the current domain.

## What This Study Established

This study established that:

```text
u_vac is domain-limited unless a separate equilibrium-frame rule is derived.
```

It also established that zero-current equilibrium is not a failure of neutrality, but it is a failure of current-normalized frame definition.

## What This Study Did Not Establish

This study did not define \(J_V^\mu\).

It did not prove any candidate current is timelike.

It did not define an equilibrium-frame fallback.

It did not prove boundary neutrality.

It did not prove no-overlap.

It did not test static-source scalar charge.

## Current Best Interpretation

```text
J_V may define u_vac only in active timelike/nonzero exchange domains.
```

For ordinary static equilibrium, the current may vanish. That protects neutrality but may require a separate frame rule if a frame is still needed.

## Next Development Target

The next script should be:

```text
candidate_static_source_neutrality_for_J_V.py
```

Purpose:

```text
Test whether candidate J_V/Sigma/R structures create exterior scalar charge around static sources.
```

Reason:

```text
If a timelike/nonzero domain can be stated,
the next ordinary-sector gate is static-source neutrality.
```

Expected result:

```text
A static-source neutrality ledger:
  static zero-current equilibrium,
  pointwise Sigma_V = R_V balance,
  compact-support J_V with zero boundary flux,
  source-gradient danger,
  zeta-gradient danger,
  exterior scalar charge rejection,
  no M_ext shift,
  no far-zone scalar flux,
  boundary/no-overlap requirements,
  next boundary/no-overlap script if neutrality survives.
```

## Summary

The timelike-domain result is:

```text
No timelike nonzero current, no current-defined vacuum clock.
```

The next goblin gate is:

```text
does the candidate current stay quiet around ordinary static mass?
```
