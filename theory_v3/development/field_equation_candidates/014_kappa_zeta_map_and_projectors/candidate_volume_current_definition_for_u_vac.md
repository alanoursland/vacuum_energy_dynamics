# Candidate Volume Current Definition For u Vac

## Canonical Filename

```text
candidate_volume_current_definition_for_u_vac.md
```

This document summarizes the output of:

```text
candidate_volume_current_definition_for_u_vac.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of `J_V^mu`, not a completed vacuum rest-frame definition, and not a source law.

Its purpose is to test whether a real vacuum-volume current can define:

```text
u_vac^mu = J_V^mu / sqrt(-J_V^2)
```

The guiding question was:

```text
Can J_V be written, or do we close the cave?
```

The answer is:

```text
J_V is the best candidate for defining u_vac, but it is not yet defined.

The strongest possible form is an exchange continuity law:

  nabla_mu J_V^mu = Sigma_V - R_V

But Sigma_V/R_V and flux direction are not yet available.

Best next script:
  candidate_group_14_closure_summary.py
```

---

## Why This Study Matters

The vacuum-frame definition audit found that `u_vac^mu` is not yet defined.

The strongest surviving candidate was:

```text
u_vac^mu = J_V^mu / sqrt(-J_V^2)
```

This only works if `J_V^mu` is a real vacuum-volume current, not a name introduced to keep the acceleration-gradient branch alive.

This script tested whether `J_V^mu` can be written with the current ingredients.

---

## Compact Volume-Current Ledger

| Entry | Current | Status | Consequence |
|---|---|---|---|
| JV1: volume-current theorem target | `J_V^mu` is a real vacuum-volume flux current; `u_vac^mu = J_V^mu / sqrt(-J_V^2)` | THEOREM_TARGET | decides whether `u_vac` can be defined |
| JV2: zeta-gradient current | `J_V^mu = beta_z nabla^mu zeta` | RISK | likely insufficient as general vacuum rest frame |
| JV3: exchange continuity current | `nabla_mu J_V^mu = Sigma_V - R_V` | CANDIDATE | strongest route if volume exchange supplies conservation / balance law |
| JV4: source-driven current | `J_V^mu` sourced by `Sigma_V ~ chi rho a^nu nabla_nu A` | CANDIDATE | needs more than scalar source; requires transport / flux law |
| JV5: equilibrium zero-flux current | `u_vac` is rest frame where spatial `J_V` vanishes locally | SAFE_IF | useful rest-frame definition but not a current origin |
| JV6: density-times-frame circularity | `J_V^mu = n_V u_vac^mu` | REJECTED | cannot define the clock using the clock |
| JV7: decorative current failure | `J_V` is declared as vacuum volume current without flux law | REJECTED | triggers Group 14 closure if no current is written |
| JV8: timelike / nonzero requirement | `J_V^2 < 0` and `J_V != 0` in regimes where `u_vac` is used | REQUIRED | prevents invalid frame definition |
| JV9: static-source neutrality | static equilibrium sources do not produce independent exterior `J_V/zeta` charge | REQUIRED | kills current definitions that create scalar gravity |
| JV10: sign / orientation rule | orientation of `J_V` fixes creation / destruction sign | UNRESOLVED | needed before numerical or recovery claims |
| JV11: boundary / no-overlap requirements | `J_V`-driven zeta is boundary-neutral and metric insertion occurs only through `B_s` | REQUIRED | even a real current fails if accounting fails |
| JV12: recommended closure move | if exchange continuity current cannot be specified, close Group 14 | RECOMMENDED | next artifact should be Group 14 closure unless `J_V` becomes explicit |

---

## Status Counts

```text
CANDIDATE:      2
RECOMMENDED:    1
REJECTED:       2
REQUIRED:       3
RISK:           1
SAFE_IF:        1
THEOREM_TARGET: 1
UNRESOLVED:     1
```

Interpretation:

```text
J_V is not defined by naming it.
zeta-gradient current is risky and probably not general.
exchange continuity current is the strongest candidate but needs Sigma_V and R_V.
source-driven scalar Sigma_V alone does not determine flux direction.
if no exchange/transport law is supplied, Group 14 should close.
```

---

## Volume-Current Decision Tree

1. Can `J_V` be defined by exchange continuity?

```text
Need:
  nabla_mu J_V^mu = Sigma_V - R_V
with:
  Sigma_V and R_V defined.
```

2. Can `J_V` be defined by zeta gradient?

```text
Only if grad zeta is timelike/nonzero in target regimes.
```

3. Can scalar `Sigma_V` define `J_V` direction?

```text
No, not by itself.
A transport / flux law is needed.
```

4. Can `J_V = n_V u_vac` define `u_vac`?

```text
No.
That is circular.
```

5. If no real `J_V`:

```text
close Group 14 with u_vac/J_V as bottleneck.
```

---

## Good Failure / Closure Trigger

Good failure:

```text
no non-circular, timelike, boundary-neutral J_V can be defined from current ingredients.
```

Consequence:

```text
u_vac cannot currently be defined.
Acceleration-gradient volume creation remains a theorem target, not a source law.
Group 14 should close with J_V/u_vac as the surviving bottleneck.
```

Bad failure:

```text
declare J_V and keep going because the next equation needs a clock.
```

---

## Failure Controls

Volume-current definition fails if:

1. `J_V` is named but not defined.
2. `J_V` is defined using `u_vac` circularly.
3. zeta-gradient is used where it is not timelike / nonzero.
4. scalar `Sigma_V` is treated as flux direction.
5. `Sigma_V/R_V` are unnamed in continuity equation.
6. static sources create independent exterior zeta charge.
7. `J_V` creates residual metric trace outside `B_s`.
8. sign / orientation is chosen from recovery.
9. the group continues without defining `J_V`.

---

## What This Study Established

This study established that `J_V^mu` is the best available candidate for defining `u_vac^mu`, but it is not yet defined.

The strongest possible structure is:

```text
nabla_mu J_V^mu = Sigma_V - R_V
```

But this requires:

```text
Sigma_V,
R_V,
boundary conditions,
and flux / transport direction.
```

Those ingredients are not available inside Group 14.

---

## What This Study Did Not Establish

This study did not define `J_V^mu`.

It did not define `Sigma_V` completely.

It did not define `R_V`.

It did not provide a transport / flux direction law.

It did not prove static-source neutrality.

It did not prove boundary neutrality or no-overlap.

It did not resolve sign / orientation.

---

## Current Best Interpretation

Group 14 has reached its useful endpoint.

The group successfully reduced the `A_spatial` / spatial-trace origin problem to a precise bottleneck:

```text
J_V/u_vac definition for vacuum-volume exchange.
```

Without `J_V`, the acceleration-gradient source law cannot be promoted from theorem target to source law.

---

## Next Development Target

The next script should be:

```text
candidate_group_14_closure_summary.py
```

Purpose:

```text
Close Group 14 with J_V/u_vac as surviving bottleneck.
```

Reason:

```text
J_V remains dependent on an exchange continuity law not yet available.
Close Group 14 and promote J_V/u_vac to next-group bottleneck.
```

---

## Summary

The volume-current result is:

```text
No flux law, no vacuum clock.
```

The next goblin gate is not another candidate loop.

It is:

```text
close Group 14.
```
