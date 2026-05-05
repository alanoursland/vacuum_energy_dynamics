# Candidate Vacuum Rest Frame Definition

## Canonical Filename

```text
candidate_vacuum_rest_frame_definition.md
```

This document summarizes the output of:

```text
candidate_vacuum_rest_frame_definition.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of \(u^\mu_{\rm vac}\), not a final source law, and not a completed volume-current theory.

Its purpose is to test whether the vacuum rest frame can be defined from \(\zeta\), vacuum substance, volume configuration, volume flow, or equilibrium structure.

The guiding question was:

```text
Is u_vac a real ontology object, or just a clock drawn on the cave wall?
```

The answer is:

```text
u_vac is not yet defined.

Best surviving candidate:
  u_vac^mu = J_V^mu / sqrt(-J_V^2)

But this only works if J_V is a real vacuum-volume current.

Best next test:
  candidate_volume_current_definition_for_u_vac.py

Group closure note:
  If J_V cannot be defined, close Group 14 with u_vac/J_V as the surviving bottleneck.
```

---

## Why This Study Matters

The matter-versus-vacuum frame branch test found that \(u^\mu_{\rm vac}\) is the ontology-native frame, but it must be defined or killed.

The acceleration-gradient source law:

\[
\Sigma_V=\chi\rho a^\mu\nabla_\mu A
\]

cannot proceed unless \(a^\mu\) is tied to a physical frame.

This study tested candidate definitions of \(u^\mu_{\rm vac}\).

---

## Compact Vacuum-Frame Ledger

| Entry | Definition | Status | Consequence |
|---|---|---|---|
| VF1: vacuum frame theorem target | \(u^\mu_{\rm vac}\) is derived from vacuum substance / \(\zeta\) / volume configuration | THEOREM_TARGET | decides whether acceleration-gradient source law can proceed |
| VF2: \(\zeta\)-gradient normal candidate | \(u^\mu_{\rm vac}\) parallel to normalized timelike gradient of \(\zeta\), if \(\nabla\zeta\) is timelike | RISK | may fail in static or equilibrium regions where \(\zeta\) has no usable time gradient |
| VF3: vacuum volume current candidate | \(u^\mu_{\rm vac}=J_V^\mu/\sqrt{-J_V^2}\), with \(J_V\) a vacuum-volume flux current | CANDIDATE | strongest route if volume exchange supplies a real current |
| VF4: local equilibrium frame candidate | \(u_{\rm vac}\) is frame in which local vacuum volume flux vanishes / \(\zeta\) configuration is at rest | CANDIDATE | may define \(u_{\rm vac}\) in static regions without scalar time gradient |
| VF5: hypersurface-normal diagnostic | \(u^\mu_{\rm vac}=n^\mu\), normal to preferred \(\zeta\) / vacuum-volume foliation | CONSTRAINED | diagnostic only unless vacuum ontology picks the slices |
| VF6: matter-comoving fallback | \(u^\mu_{\rm vac}=u^\mu_m\) in tightly coupled matter / vacuum equilibrium | RISK | may collapse back to matter-frame source-model dependence |
| VF7: arbitrary preferred frame | \(u_{\rm vac}\) chosen as convenient background rest frame | REJECTED | would introduce an unsupported preferred frame |
| VF8: static-source neutrality requirement | \(u_{\rm vac}\) definition yields \(\Sigma_V\) static-neutral or boundary-neutral around equilibrium sources | REQUIRED | kills \(u_{\rm vac}\) definitions that create ordinary scalar gravity |
| VF9: sign / orientation rule | \(u_{\rm vac}\) and projection fix sign of \(a_{\rm vac}\cdot\nabla A\) as creation / destruction | UNRESOLVED | needed before numerical or recovery claims |
| VF10: \(\chi\)-origin dependency | \(u_{\rm vac}\) definition does not determine \(\chi\) by recovery fitting | REQUIRED | \(u_{\rm vac}\) alone does not complete \(\Sigma_V\) |
| VF11: boundary / no-overlap requirements | source-driven \(\zeta\) is boundary-neutral and enters metric only through \(B_s\) | REQUIRED | even a defined \(u_{\rm vac}\) fails if accounting fails |
| VF12: recommended next move | try volume-current \(J_V\) definition first; otherwise closure summary | RECOMMENDED | next script should either define \(J_V\), or close Group 14 with \(u_{\rm vac}\) as bottleneck |

---

## Status Counts

The run counted:

```text
CANDIDATE:      2
CONSTRAINED:    1
RECOMMENDED:    1
REJECTED:       1
REQUIRED:       3
RISK:           2
THEOREM_TARGET: 1
UNRESOLVED:     1
```

Interpretation:

```text
u_vac cannot be an arbitrary preferred frame.
zeta-gradient normal is risky because zeta may not provide a timelike clock.
volume-current J_V is the strongest candidate if the exchange law supplies it.
equilibrium-frame definition may work in static regions if defined invariantly.
if neither J_V nor equilibrium frame can be defined, Group 14 should close with u_vac as the bottleneck.
```

---

## Vacuum-Frame Definition Decision Tree

1. Does volume exchange define a current \(J_V\)?

```text
If yes:
  define u_vac = normalized J_V.
```

2. If no \(J_V\), does \(\zeta\) define a timelike gradient?

```text
If yes:
  zeta-gradient normal may define local vacuum clock.
```

3. If no \(\zeta\) clock, does vacuum equilibrium define a rest frame?

```text
If yes:
  use invariant zero-flux/equilibrium frame.
```

4. If only arbitrary slicing remains:

```text
reject u_vac as parent frame.
```

5. If \(u_{\rm vac}\) cannot be defined:

```text
close Group 14 with u_vac as surviving bottleneck.
```

---

## Good Failure / Group Closure Trigger

Good failure:

```text
no J_V, zeta-clock, or invariant equilibrium criterion defines u_vac.
```

Consequence:

```text
acceleration-gradient volume creation cannot currently be promoted.
Group 14 should close with u_vac / volume-current definition as the surviving bottleneck.
```

Bad failure:

```text
choose a convenient preferred frame and continue as if u_vac were derived.
```

---

## Failure Controls

Vacuum-frame definition fails if:

1. \(u_{\rm vac}\) is arbitrary preferred frame.
2. \(u_{\rm vac}\) is chosen from \(\gamma_{\rm like}\) or \(AB\).
3. \(\zeta\)-gradient is used where not timelike / nonzero.
4. Hypersurface normal is arbitrary gauge slicing.
5. \(J_V\) is named but not defined.
6. Equilibrium frame is coordinate rest frame.
7. Static source creates independent exterior \(\zeta\) charge.
8. Boundary neutrality or no-overlap is dropped.
9. \(\chi\) tuning is hidden in normalization.

---

## What This Study Established

This study established that \(u^\mu_{\rm vac}\) is not yet defined.

The best surviving candidate is:

\[
u^\mu_{\rm vac}
=
\frac{J_V^\mu}{\sqrt{-J_V^2}}.
\]

But this only works if \(J_V^\mu\) is a real vacuum-volume current.

The \(\zeta\)-gradient normal is risky because \(\zeta\) may not provide a timelike, nonzero clock in static or equilibrium regions.

An arbitrary preferred frame is rejected.

---

## What This Study Did Not Establish

This study did not define \(J_V^\mu\).

It did not derive \(u^\mu_{\rm vac}\).

It did not derive the sign / orientation of volume creation.

It did not derive \(\chi\).

It did not prove static-source neutrality.

It did not prove boundary neutrality or no-overlap.

---

## Current Best Interpretation

Group 14 is now at its intended endpoint unless a real volume current can be written.

The final live test is:

```text
candidate_volume_current_definition_for_u_vac.py
```

If that script cannot define \(J_V^\mu\), then the group should close with:

```text
u_vac / J_V definition is the surviving bottleneck.
```

---

## Next Development Target

The next script should be:

```text
candidate_volume_current_definition_for_u_vac.py
```

Purpose:

```text
Try to define J_V and u_vac = normalized J_V.
```

Reason:

```text
J_V is the strongest non-arbitrary u_vac candidate.
Test it once, then close the group if it remains unnamed.
```

Expected result:

```text
A volume-current ledger:
  J_V as volume flux current,
  J_V from zeta derivative,
  J_V from source-driven volume creation,
  J_V from exchange continuity equation,
  static-source neutrality,
  sign/orientation,
  chi-origin dependency,
  boundary/no-overlap,
  rejection of decorative J_V,
  group-closure trigger if J_V remains undefined.
```

---

## Summary

The vacuum-frame result is:

```text
No current, no clock.
```

The next goblin gate is:

```text
can J_V be written, or do we close the cave?
```
