# Candidate Static-Source Neutrality For J_V

## Canonical Filename

```text
candidate_static_source_neutrality_for_J_V.md
```

This document summarizes the output of:

```text
candidate_static_source_neutrality_for_J_V.py
```

## What This Document Is

This document is a development note for the `15_vacuum_current_and_exchange_continuity/` group.

It is not a derivation of \(J_V^\mu\), not a proof of static neutrality, and not a completed ordinary-sector current law.

Its purpose is to test whether a candidate \(J_V/\Sigma_V/R_V\) structure creates an independent exterior scalar charge around ordinary static sources.

The guiding question was:

```text
Does the proposed J_V / Sigma_V / R_V structure create exterior scalar charge around static sources?
```

The answer is:

```text
Static-source neutrality is mandatory for ordinary gravity.

Best current interpretation:
  static zero-current or compact/balanced exchange may be safe,
  but any exterior scalar charge kills the current family.

Best next test:
  candidate_boundary_no_overlap_for_volume_current.py
```

## Why This Study Matters

The timelike-domain run found that \(J_V\) can define \(u_{\rm vac}\) only on a timelike / nonzero domain. It also found that zero-current equilibrium may protect neutrality but cannot define \(u_{\rm vac}\) from \(J_V\).

This run applies the ordinary-sector safety test:

```text
ordinary static mass must not create independent exterior zeta/kappa/J_V charge.
```

A static current family that creates an exterior scalar tail is not a harmless variant. It is killed for ordinary gravity.

## Compact Static-Neutrality Ledger

| Entry | Neutrality Test | Status | Consequence |
|---|---|---|---|
| SN1: static-source neutrality target | ordinary static sources create no independent exterior \(J_V/\zeta/\kappa\) scalar charge | THEOREM_TARGET | decides whether \(J_V/\Sigma/R\) can survive ordinary static gravity |
| SN2: static zero-current equilibrium | \(J_V=0\) in static equilibrium with no exterior flux | SAFE_IF | protects neutrality but does not define current-based \(u_{\rm vac}\) |
| SN3: pointwise Sigma/R balance | \(\Sigma_V=R_V\) pointwise in static equilibrium | CANDIDATE | can prevent static volume charge if not decorative |
| SN4: compact-support current | \(J_V\) nonzero only inside source / interior, with zero boundary flux | CANDIDATE | may allow internal exchange without exterior scalar charge |
| SN5: zeta-gradient static risk | \(J_V\sim-D_z\nabla\zeta\) around static source | RISK | likely rejects unrestricted zeta-gradient current in ordinary static gravity |
| SN6: source-gradient static risk | \(J_V\) follows source / support gradient near static matter boundary | RISK | can become boundary repair or shell source if uncontrolled |
| SN7: acceleration-gradient static safety | \(\Sigma_V\sim\chi\rho a^\mu\nabla_\mu A\) is zero or neutral for static equilibrium | RISK | may kill acceleration-gradient source in ordinary static branch if unsafe |
| SN8: exterior scalar charge rejection | \(Q_V=\int_{\rm static}(\Sigma_V-R_V)\) with boundary terms gives no exterior scalar charge | REQUIRED | kills any static law that makes independent scalar gravity |
| SN9: no far-zone scalar flux | \(F_{\rm scalar,far}[J_V,\zeta,\kappa]=0\) for ordinary static sources | REQUIRED | prevents \(J_V\) from becoming observable scalar field |
| SN10: no exterior mass shift | \(\delta M_{\rm ext}|_{\rm volume}=0\) for static volume exchange | REQUIRED | kills current laws that alter A-sector mass |
| SN11: no-overlap / residual-kill | static \(J_V\)-driven \(\zeta\) enters metric only through \(B_s\), or residual trace killed / non-metric | REQUIRED | prevents static current from reviving \(\zeta/\kappa\) scalar duplicate |
| SN12: \(R_V\) cancellation patch rejection | \(R_V\) tuned to cancel static exterior charge | REJECTED | prevents relaxation from becoming scalar-charge eraser |
| SN13: recovery downstream | \(\gamma_{\rm like}\) and \(AB\) checked only after static neutrality is structural | RECOVERY_TARGET | keeps recovery from selecting neutrality mechanism |
| SN14: static neutrality failure | candidate \(J_V/\Sigma/R\) produces exterior scalar charge around static sources | BRANCH_KILLED | unsafe current family cannot support ordinary gravity |
| SN15: recommended next move | if static neutrality survives, test boundary / no-overlap for volume current | RECOMMENDED | next script should test whether the current double-counts \(B_s\)/residual trace or leaks through boundary |

## Status Counts

```text
BRANCH_KILLED:   1
CANDIDATE:       2
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        4
RISK:            3
SAFE_IF:         1
THEOREM_TARGET:  1
```

Interpretation:

```text
Static zero-current equilibrium is safe if u_vac is not required from J_V there.
Pointwise Sigma/R balance and compact-support current are candidate safety routes.
Zeta-gradient, source-gradient, and acceleration-gradient branches are risky in static ordinary gravity.
No exterior scalar charge, no far-zone scalar flux, no M_ext shift, and no-overlap are mandatory.
If static neutrality survives, boundary/no-overlap becomes the next gate.
```

## Static-Neutrality Decision Tree

```text
1. Static zero-current equilibrium:
   safest for exterior neutrality,
   but cannot define u_vac from J_V.

2. Pointwise Sigma/R balance:
   candidate if balance follows from equilibrium law, not tuning.

3. Compact-support current:
   candidate if boundary flux is structurally zero.

4. Gradient currents around static sources:
   risky because exterior gradients can create scalar tails.

5. R_V cancellation:
   rejected if used to erase scalar charge after the fact.

6. If exterior scalar charge appears:
   branch killed for ordinary static gravity.
```

## Good Failure / Branch Decision

Good failure:

```text
a candidate J_V / Sigma_V / R_V family produces exterior scalar charge
around ordinary static sources.
```

Consequence:

```text
reject that current family for ordinary gravity.
Do not patch with R_V tuning or boundary repair.
```

Bad failure:

```text
allow static scalar charge and hope recovery checks hide it.
```

## Failure Controls

Static-source neutrality fails if:

1. Static mass creates independent \(\zeta/\kappa\) exterior charge.
2. \(R_V\) is tuned to cancel that charge.
3. Source-gradient creates shell scalar charge at boundary.
4. Zeta-gradient current produces far-zone scalar tail.
5. Acceleration-gradient source treats static support as scalar source without neutrality theorem.
6. \(J_V\) changes \(M_{\rm ext}\) independently of A-sector.
7. Static current creates residual metric trace outside \(B_s\).
8. \(\gamma_{\rm like}\) or \(AB\) is used to select neutrality mechanism.

## What This Study Established

This study established that static-source neutrality is not optional.

The only safe-looking ordinary static branches are:

```text
static zero-current equilibrium,
pointwise Sigma/R balance,
compact-support current with zero boundary flux.
```

Each remains conditional.

## What This Study Did Not Establish

This study did not derive static neutrality.

It did not prove pointwise \(\Sigma_V=R_V\).

It did not prove compact support.

It did not prove boundary flux cancellation.

It did not prove no-overlap or residual-kill.

It did not define an equilibrium frame for \(J_V=0\).

## Current Best Interpretation

```text
Static zero-current or compact/balanced exchange may be safe,
but any exterior scalar charge kills the current family.
```

The next local test is:

```text
candidate_boundary_no_overlap_for_volume_current.py
```

## Next Development Target

The next script should be:

```text
candidate_boundary_no_overlap_for_volume_current.py
```

Purpose:

```text
Test whether surviving volume-current families leak through the boundary
or double-count B_s / residual trace.
```

Reason:

```text
If ordinary static neutrality survives,
the next gate is whether J_V-driven zeta leaks through the boundary
or double-counts B_s / residual trace.
```

Expected result:

```text
A boundary/no-overlap ledger:
  zero exterior J_V flux,
  zero exterior zeta/kappa charge,
  no far-zone scalar flux,
  no M_ext shift,
  B_s-only metric insertion,
  residual zeta/kappa killed or non-metric,
  compact-support current,
  boundary shell-source risk,
  no-overlap operator theorem target,
  branch kill if boundary leakage or trace overlap appears.
```

## Summary

The static-neutrality result is:

```text
static mass must not awaken a scalar volume tail.
```

The next goblin gate is:

```text
even if the current stays quiet outside,
does it double-count the trace inside?
```
