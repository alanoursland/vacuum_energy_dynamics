# Candidate Matter Versus Vacuum Frame Branch Test

## Canonical Filename

```text
candidate_matter_vs_vacuum_frame_branch_test.md
```

This document summarizes the output of:

```text
candidate_matter_vs_vacuum_frame_branch_test.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a final frame choice, not a completed source law, and not a derivation of \(u^\mu_{\rm vac}\).

Its purpose is to compare the two clean frame branches for the acceleration-gradient source law:

\[
\Sigma_V=\chi\rho a^\mu\nabla_\mu A.
\]

The guiding question was:

```text
Does matter carry the clock, or does vacuum?
```

The answer is:

```text
The branch comparison does not choose matter frame by convenience.

Best next test:
  candidate_vacuum_rest_frame_definition.py

Reason:
  u_vac is the ontology-native frame, but it must be defined or killed.
```

---

## Why This Study Matters

The volume-creation frame-field inventory found two clean candidates:

```text
matter congruence u_m^mu
vacuum rest frame u_vac^mu
```

Hybrid projection remains deferred until both are independently defined.

This branch test prevents the project from choosing the matter frame merely because it is easier, or inventing a vacuum frame merely because the theory needs one.

---

## Compact Matter-Vacuum Frame Ledger

| Entry | Branch | Status | Consequence |
|---|---|---|---|
| MV1: branch comparison target | choose whether \(\Sigma_V\) uses matter frame \(u_m\) or vacuum frame \(u_{\rm vac}\) | THEOREM_TARGET | decides whether acceleration-gradient branch can proceed |
| MV2: matter congruence branch | \(\Sigma_V=\chi\rho a_m^\mu\nabla_\mu A\), \(a_m^\mu=u_m^\nu\nabla_\nu u_m^\mu\) | CANDIDATE | physically local but source-model dependent |
| MV3: vacuum rest-frame branch | \(\Sigma_V=\chi\rho a_{\rm vac}^\mu\nabla_\mu A\), \(a_{\rm vac}^\mu=u_{\rm vac}^\nu\nabla_\nu u_{\rm vac}^\mu\) | CANDIDATE | best ontology match but currently missing its core object |
| MV4: hybrid projection deferred | \(\Sigma_V=\chi\rho(P_{\rm vac}a_m)^\mu(P_{\rm vac}\nabla A)_\mu\) | DEFER | hybrid projection waits; goblin not allowed to glue clocks together yet |
| MV5: static-source safety for matter frame | matter-frame \(\Sigma_V\) vanishes or is boundary-neutral for static equilibrium sources | REQUIRED | major risk for matter congruence branch |
| MV6: static-source safety for vacuum frame | vacuum-frame \(\Sigma_V\) is neutral for static vacuum / source equilibrium | REQUIRED | major risk for vacuum rest-frame branch |
| MV7: source-model dependence | matter branch depends on dust / fluid / stress model | RISK | may make matter branch too narrow for parent law |
| MV8: ontology-native vacuum frame requirement | \(u_{\rm vac}\) must arise from vacuum substance, \(\zeta\) flow, or volume configuration | REQUIRED | vacuum branch cannot proceed without defining vacuum rest frame |
| MV9: sign / orientation rule | branch choice fixes creation / destruction sign of \(a\cdot\nabla A\) | UNRESOLVED | required before numerical or recovery claims |
| MV10: \(\chi\)-origin dependency | neither matter nor vacuum frame may hide \(\chi\) tuning | REQUIRED | frame branch decision does not complete \(\Sigma_V\) derivation alone |
| MV11: boundary / no-overlap requirements | source-driven \(\zeta\) is boundary-neutral and metric insertion occurs only through \(B_s\) | REQUIRED | even a physical frame fails if accounting fails |
| MV12: recommended next move | try defining \(u_{\rm vac}\) from \(\zeta\) / vacuum substance before adopting matter-frame branch | RECOMMENDED | next script should attempt \(u_{\rm vac}\) definition directly |

---

## Status Counts

The run counted:

```text
CANDIDATE:      2
DEFER:          1
RECOMMENDED:    1
REQUIRED:       5
RISK:           1
THEOREM_TARGET: 1
UNRESOLVED:     1
```

Interpretation:

```text
Matter frame is concrete but source-model dependent and static-source risky.
Vacuum frame is ontologically preferred but missing its definition.
Hybrid projection remains deferred.
The next constructive step is to attempt u_vac definition from zeta/vacuum substance.
```

---

## Branch Decision

Matter frame:

```text
Pros:
  concrete for fluids/dust;
  source-local.

Risks:
  source-model dependence;
  static pressure/support artifacts.
```

Vacuum frame:

```text
Pros:
  ontology-native;
  natural for vacuum substance and zeta.

Risks:
  currently undefined;
  can become arbitrary preferred frame.
```

Hybrid projection:

```text
Pros:
  may express matter acceleration relative to vacuum.

Risks:
  only valid after both frames are independently defined.
```

Decision:

```text
Try to define u_vac before adopting matter frame as parent law.
```

---

## Good Failure / Branch Decision

Good failure:

```text
u_vac cannot be defined from vacuum substance/zeta,
and matter frame is too source-model-dependent or static-source unsafe.
```

Consequence:

```text
acceleration-gradient source law fails for now.
Return Sigma_V to theorem target status or test broader tensor candidate.
```

Bad failure:

```text
choose matter frame because it is easy,
or invent vacuum frame because it is needed.
```

---

## Failure Controls

Matter / vacuum frame branch test fails if:

1. Frame is selected from \(\gamma_{\rm like}\) or \(AB\).
2. Coordinate velocity enters parent law.
3. \(u_{\rm vac}\) is arbitrary gauge / slicing.
4. Hybrid projection is used before both frames are defined.
5. Matter-frame branch creates static scalar charge.
6. Vacuum-frame branch invents preferred frame.
7. \(\chi\)-origin is hidden in frame choice.
8. Boundary neutrality or no-overlap is dropped.

---

## What This Study Established

This study established that the branch comparison does not choose matter frame by convenience.

The vacuum frame is ontologically preferred because the active ontology is vacuum substance / spacetime volume.

But the vacuum frame is not yet defined.

Therefore the next step is:

```text
define or kill u_vac.
```

---

## What This Study Did Not Establish

This study did not define \(u_{\rm vac}^\mu\).

It did not prove the matter frame is unsafe.

It did not prove static-source neutrality.

It did not fix the sign / orientation of creation versus destruction.

It did not derive \(\chi\).

It did not prove boundary neutrality or no-overlap.

---

## Current Best Interpretation

Group 14 is near closure.

The surviving live branch is:

```text
source-driven volume creation
  -> acceleration-gradient source law
  -> vacuum rest frame definition
```

If \(u_{\rm vac}^\mu\) cannot be defined from \(\zeta\), vacuum substance, or volume configuration, the acceleration-gradient route should be deferred or killed for this group.

---

## Next Development Target

The next script should be:

```text
candidate_vacuum_rest_frame_definition.py
```

Purpose:

```text
Try to define u_vac from zeta/vacuum substance ontology.
```

Reason:

```text
u_vac is the ontology-native frame, but it must be defined or killed.
```

---

## Summary

The matter-vacuum frame result is:

```text
Do not pick the easy clock.
Try to define the vacuum clock.
```

The next goblin gate is:

```text
is u_vac a real ontology object, or just a clock drawn on the cave wall?
```
