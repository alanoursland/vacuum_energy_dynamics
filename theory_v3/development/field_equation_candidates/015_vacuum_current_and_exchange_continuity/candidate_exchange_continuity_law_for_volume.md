# Candidate Exchange Continuity Law For Volume

## Canonical Filename

```text
candidate_exchange_continuity_law_for_volume.md
```

This document summarizes the output of:

```text
candidate_exchange_continuity_law_for_volume.py
```

## What This Document Is

This document opens the `15_vacuum_current_and_exchange_continuity/` group.

It is not a derivation of \(J_V^\mu\), not a completed continuity law, and not a definition of \(u_{\rm vac}^\mu\).

Its purpose is to test the strongest surviving structure from Group 14:

```text
nabla_mu J_V^mu = Sigma_V - R_V
```

The guiding question was:

```text
Can a real exchange continuity law define J_V?
```

The answer is:

```text
Exchange continuity is the right locked door,
but it is not yet a law.

J_V needs a flux direction,
Sigma_V and R_V must be split,
and recovery checks remain downstream.

Best next test:
  candidate_sigma_R_split_for_volume_exchange.py
```

## Why This Study Matters

Group 14 closed with the bottleneck:

```text
J_V / u_vac
```

The candidate relation was:

```text
u_vac^mu = J_V^mu / sqrt(-J_V^2)
```

but \(J_V^\mu\) was not defined.

This run tests whether an exchange continuity equation can begin to define \(J_V\), while preventing the false move of declaring:

```text
nabla_mu J_V^mu = Sigma_V - R_V
```

as a finished law before \(J_V\), \(\Sigma_V\), \(R_V\), boundary conditions, and flux direction exist.

## Compact Exchange-Continuity Ledger

| Entry | Law | Status | Consequence |
|---|---|---|---|
| EC1: exchange continuity theorem target | \(\nabla_\mu J_V^\mu=\Sigma_V-R_V\) | THEOREM_TARGET | decides whether \(u_{\rm vac}\) can become a real ontology object |
| EC2: \(J_V\) as flux, not density-times-clock | \(J_V^\mu\) must define \(u_{\rm vac}\), not depend on \(u_{\rm vac}\) | REQUIRED | without flux direction, no vacuum clock |
| EC3: \(\Sigma_V\) source term | \(\Sigma_V\) may include source-driven volume creation, e.g. \(\chi\rho a^\mu\nabla_\mu A\) | CANDIDATE | source term remains theorem target until frame and \(\chi\) are fixed |
| EC4: \(R_V\) relaxation / exchange term | \(R_V\) represents relaxation / reconfiguration of vacuum volume | CANDIDATE | could distinguish creation from relaxation, but risks patching |
| EC5: flux direction law | \(J_V\) direction must follow from gradient, transport, or exchange structure | REQUIRED | scalar \(\Sigma_V\) alone cannot define \(J_V\) |
| EC6: timelike / nonzero domain | \(J_V^2<0\), \(J_V\neq0\) where \(u_{\rm vac}=J_V/\sqrt{-J_V^2}\) is used | REQUIRED | defines where vacuum clock exists |
| EC7: static-source neutrality | static equilibrium sources have zero or boundary-neutral independent \(J_V/\zeta\) charge | REQUIRED | kills continuity laws that produce ordinary scalar charge |
| EC8: boundary / no-overlap | \(J_V\)-driven \(\zeta\) is boundary-neutral and enters metric only through \(B_s\), or residual killed | REQUIRED | continuity law fails if accounting fails |
| EC9: sign / orientation | orientation of \(J_V\) and signs of \(\Sigma_V/R_V\) define creation versus destruction | UNRESOLVED | needed before simulations or recovery claims |
| EC10: decorative continuity rejection | \(\nabla_\mu J_V^\mu=\Sigma_V-R_V\) with unnamed terms | REJECTED | prevents Group 15 from becoming another painted tunnel |
| EC11: recovery checks downstream | after \(J_V/\Sigma_V/R_V\) are fixed, test \(\gamma_{\rm like}\) and \(AB\) | RECOVERY_TARGET | keeps recovery from becoming construction |
| EC12: recommended next move | split \(\Sigma_V\) and \(R_V\) definitions before claiming exchange continuity | RECOMMENDED | next script should inventory \(\Sigma_V\) and \(R_V\) roles in the continuity law |

## Status Counts

```text
CANDIDATE:       2
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        5
THEOREM_TARGET:  1
UNRESOLVED:      1
```

Interpretation:

```text
Exchange continuity is the right next locked door, but not yet a law.
J_V needs a flux direction, not only a divergence equation.
Sigma_V and R_V must be defined separately.
Static neutrality, boundary neutrality, and no-overlap remain mandatory.
```

## Minimal Law Requirements

A real exchange continuity law must provide:

```text
1. J_V flux direction / transport law
2. Sigma_V source creation law
3. R_V relaxation / exchange law
4. timelike / nonzero domain for J_V
5. static-source neutrality
6. boundary neutrality
7. no-overlap / residual-kill theorem
8. sign / orientation convention
9. recovery checks downstream
```

Missing these turns continuity into decoration.

## Good Failure / Branch Decision

Good failure:

```text
exchange continuity cannot be defined without unnamed Sigma_V/R_V
or arbitrary flux direction.
```

Consequence:

```text
J_V/u_vac remains a theorem target.
Return to postulate-level derivation of vacuum exchange
rather than writing field equations.
```

Bad failure:

```text
write nabla_mu J_V^mu = Sigma_V - R_V
and pretend the current has been defined.
```

## Failure Controls

Exchange continuity law fails if:

1. \(J_V\) has no flux direction.
2. \(J_V\) is defined as \(n_Vu_{\rm vac}\) before \(u_{\rm vac}\) exists.
3. \(\Sigma_V\) is unnamed or recovery-tuned.
4. \(R_V\) is unnamed or used as scalar-charge patch.
5. Static sources create exterior volume charge.
6. \(J_V\) creates residual metric trace outside \(B_s\).
7. Sign / orientation is chosen from \(\gamma/AB\).
8. Continuity is used as decorative conservation language.

## What This Study Established

This study established that:

```text
nabla_mu J_V^mu = Sigma_V - R_V
```

is the correct first locked door for Group 15.

It also established that the equation is not enough by itself. A divergence equation can constrain a current, but it does not by itself define a flux direction.

## What This Study Did Not Establish

This study did not define \(J_V^\mu\).

It did not define \(\Sigma_V\).

It did not define \(R_V\).

It did not define a flux direction.

It did not prove timelike / nonzero domain.

It did not prove static-source neutrality.

It did not prove boundary neutrality or no-overlap.

It did not fix sign / orientation.

## Current Best Interpretation

```text
Exchange continuity is the right structure,
but source and relaxation must be split before the current can be defined.
```

The next local test is:

```text
candidate_sigma_R_split_for_volume_exchange.py
```

## Next Development Target

The next script should be:

```text
candidate_sigma_R_split_for_volume_exchange.py
```

Purpose:

```text
Split Sigma_V and R_V roles before defining J_V.
```

Reason:

```text
The continuity equation cannot define J_V until the source and relaxation / exchange terms are split and named.
```

Expected result:

```text
A Sigma/R split ledger:
  Sigma_V as source-driven creation/destruction,
  Sigma_V as acceleration-gradient source,
  Sigma_V as trace/volume conversion source,
  R_V as local equilibrium restoration,
  R_V as zeta_min relaxation,
  R_V as kappa-linked relaxation,
  R_V as boundary-neutral reconfiguration,
  Sigma/R double-counting risk,
  sign convention,
  ordinary closed-regime constraints.
```

## Summary

The exchange-continuity result is:

```text
The river equation is drawn,
but source, drain, and flow direction are not yet real.
```

The next goblin gate is:

```text
separate spring from return flow before naming the river current.
```
