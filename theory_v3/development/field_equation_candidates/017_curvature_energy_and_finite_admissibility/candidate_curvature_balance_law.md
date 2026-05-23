# Candidate Curvature Balance Law

## Canonical Filename

```text
candidate_curvature_balance_law.md
```

This document summarizes the output of:

```text
candidate_curvature_balance_law.py
```

## What This Document Is

This document is a Group 17 curvature-energy / finite-admissibility artifact.

It is not a curvature current derivation, not a curvature balance law, not an anti-singularity theorem, and not a parent correction tensor.

Its purpose is to test whether curvature admissibility can be expressed as a balance law without becoming decorative continuity language.

The locked-door question was:

```text
Can curvature admissibility be expressed as a balance law
without becoming decorative?
```

The result is:

```text
Curvature balance remains a theorem target, not a law.

Strongest possible form:

  nabla_mu J_curv^mu = Sigma_curv - R_curv

But this is not usable until J_curv, Sigma_curv, R_curv, domain, and measure are defined.

Safe fallback:

  curvature admissibility remains diagnostic / branch-filter only.

Best next script:

  candidate_curvature_boundary_and_mass_neutrality.py
```

## Core Result

Curvature balance can currently be stated only as a theorem target.

The strongest candidate form is:

```text
nabla_mu J_curv^mu = Sigma_curv - R_curv
```

but that equation is not usable as a law because the current and both source sides are not yet defined.

The safe fallback remains:

```text
finite admissibility as diagnostic / branch-filter only.
```

## Compact Curvature Balance Ledger

| Entry | Balance Form | Status | Consequence |
|---|---|---|---|
| CB1: curvature balance target | curvature admissibility balance with defined current/source/relaxation/domain | THEOREM_TARGET | decides whether curvature admissibility can become dynamical structure |
| CB2: divergence balance candidate | \(\nabla_\mu J_{\rm curv}^\mu=\Sigma_{\rm curv}-R_{\rm curv}\) | THEOREM_TARGET | strongest balance form if source sides become real |
| CB3: inequality balance candidate | \(\nabla_\mu J_{\rm curv}^\mu \le {\rm admissibility\_bound}\) | CANDIDATE | could express finite admissibility without exact conservation |
| CB4: boundary flux balance candidate | \(\int_{\partial D}J_{\rm curv}\cdot d\Sigma\) controls \(\int_D I_{\rm curv}dV\) | CANDIDATE | could link finite integral to boundary safety if not patch |
| CB5: curvature-volume exchange candidate | curvature admissibility exchange tied to \(\zeta\)/volume response | RISK | promising but dangerous until Group 16 bottlenecks are solved |
| CB6: diagnostic-only branch | no balance law; finite admissibility remains diagnostic / branch-filter | SAFE_IF | keeps anti-singularity claims limited but honest |
| CB7: source side requirement | \(\Sigma_{\rm curv}\) must be defined before appearing in balance | REQUIRED | prevents source term from being repair label |
| CB8: relaxation side requirement | \(R_{\rm curv}\) must be defined before appearing in balance | REQUIRED | prevents \(R_{\rm curv}\) from becoming cancellation knob |
| CB9: admissibility-bound requirement | admissibility bound must be defined before balance test | REQUIRED | prevents inequality from being solution-tailored |
| CB10: domain and measure requirement | balance law uses fixed \(D_{\rm curv}\), \(dV_{\rm phys}\), and boundary measure | REQUIRED | prevents fake finite balance |
| CB11: boundary neutrality requirement | curvature balance has no boundary repair flux, exterior scalar charge, or \(M_{\rm ext}\) shift | REQUIRED | protects exterior sector |
| CB12: matter separation requirement | curvature balance does not double-count \(T_{\mu\nu}\) or alter ordinary matter coupling | REQUIRED | prevents matter repair behavior |
| CB13: \(e_{\rm curv}\) separation | \(e_{\rm curv}\) remains diagnostic/accounting unless source law is later derived | REQUIRED | preserves curvature-energy fence |
| CB14: \(H_{\rm curv}\) deferred | \(H_{\rm curv}\) is not introduced as balance closure in Group 17 | DEFER | prevents premature correction tensor |
| CB15: decorative continuity rejection | \(\nabla_\mu J_{\rm curv}^\mu=\Sigma_{\rm curv}-R_{\rm curv}\) written with all symbols undefined | REJECTED | prevents painted conservation law |
| CB16: repair balance rejection | balance law chosen to cancel singularity, divergence, or boundary leakage | REJECTED | prevents singularity-avoidance by cancellation label |
| CB17: recovery-tuned balance rejection | curvature balance chosen to pass \(\gamma_{\rm like}\), \(AB\), or exterior matching | REJECTED | keeps recovery downstream |
| CB18: anti-singularity claim guard | balance candidate does not license bounce / regular core without dynamics and solutions | REQUIRED | keeps anti-singularity claims honest |
| CB19: balance failure | no non-decorative balance can be written with current objects | BRANCH_KILLED | \(J_{\rm curv}\) balance cannot be used; continue diagnostic-only |
| CB20: recommended next move | if balance remains theorem target, audit curvature boundary and mass neutrality next | RECOMMENDED | next script should be `candidate_curvature_boundary_and_mass_neutrality.py` |

## Status Counts

```text
BRANCH_KILLED: 1
CANDIDATE:     2
DEFER:         1
RECOMMENDED:   1
REJECTED:      3
REQUIRED:      8
RISK:          1
SAFE_IF:       1
THEOREM_TARGET:2
```

Interpretation:

```text
Curvature balance can be stated only as theorem target unless J_curv and source sides are defined.

Exact divergence balance is strongest but currently underdefined.

Inequality and boundary flux balances are candidates if bounds/measures are structural.

Diagnostic-only branch remains the safe fallback.

H_curv remains deferred.

Next gate is boundary and mass neutrality.
```

## Candidate Balance Forms

```text
1. exact divergence balance:
   nabla_mu J_curv^mu = Sigma_curv - R_curv

2. inequality balance:
   nabla_mu J_curv^mu <= admissibility_bound

3. boundary flux balance:
   boundary flux controls finite curvature integral

4. curvature-volume exchange:
   curvature admissibility tied to zeta / volume response

5. diagnostic-only branch:
   no balance law yet
```

## Curvature Balance Decision Tree

```text
1. J_curv + Sigma_curv + R_curv defined:
   exact divergence balance may proceed.

2. J_curv undefined but admissibility bound defined:
   inequality remains theorem target, not law.

3. Boundary flux defined structurally:
   boundary balance candidate may proceed to neutrality audit.

4. Zeta-volume coupling appears:
   high risk; must not reopen Group 16 bottlenecks.

5. All source sides undefined:
   diagnostic-only branch.

6. Balance cancels failure:
   rejected as repair.
```

## Good Failure / Branch Decision

Good failure:

```text
No non-decorative balance law can be written because J_curv,
Sigma_curv, R_curv, bounds, or measures are not defined.
```

Consequence:

```text
curvature admissibility remains diagnostic / branch-filter only.
do not write balance law with placeholder symbols.
```

Bad failure:

```text
write nabla_mu J_curv^mu = Sigma_curv - R_curv
and call it closure.
```

## Failure Controls

Curvature balance law fails if:

1. \(J_{\rm curv}\) is undefined.
2. \(\Sigma_{\rm curv}\) is undefined.
3. \(R_{\rm curv}\) is undefined.
4. admissibility bound is solution-tailored.
5. domain/measure hide divergence.
6. boundary flux repairs singularity or mass shift.
7. matter source is double-counted or rerouted.
8. \(e_{\rm curv}\) becomes source reservoir.
9. \(H_{\rm curv}\) is introduced as closure.
10. \(\gamma_{\rm like}\) / \(AB\) / recovery chooses the balance.
11. bounce or regular core is claimed.

## What This Study Established

This study established that curvature balance remains a theorem target, not a law.

The strongest possible expression is:

```text
nabla_mu J_curv^mu = Sigma_curv - R_curv
```

but it is not yet usable because \(J_{\rm curv}\), \(\Sigma_{\rm curv}\), \(R_{\rm curv}\), the domain, and the measure are not defined.

## What This Study Did Not Establish

This study did not define \(J_{\rm curv}\).

It did not define \(\Sigma_{\rm curv}\).

It did not define \(R_{\rm curv}\).

It did not define an admissibility bound.

It did not prove boundary neutrality.

It did not prove mass neutrality.

It did not license a bounce, regular core, or dynamical avoidance claim.

## Current Best Interpretation

```text
Curvature balance is a theorem target.

Finite admissibility remains diagnostic / branch-filter
unless a real current, source sides, domain, and measure are defined.
```

## Next Development Target

The next script should be:

```text
candidate_curvature_boundary_and_mass_neutrality.py
```

Purpose:

```text
Test whether curvature admissibility or J_curv alters exterior mass,
creates boundary repair behavior,
or leaks an ordinary-sector scalar charge.
```

Reason:

```text
Even if curvature balance remains theorem-targeted,
its safety burden is boundary/mass neutrality.
```

Expected result:

```text
A curvature boundary/mass neutrality ledger:
  no M_ext shift,
  no boundary repair current,
  no exterior scalar charge,
  no recovery-tuned smoothing,
  no hidden matter coupling,
  no singularity avoidance by boundary counterterm,
  interior-only admissibility,
  compact curvature support,
  boundary flux diagnostic only,
  J_curv exterior-neutral.
```

## Summary

The curvature-balance result is:

```text
The balance form is allowed as a target.
It is not allowed as a painted law.
```

Tiny goblin plaque:

```text
A divergence with empty pockets buys no theorem.
