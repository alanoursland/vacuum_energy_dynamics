# Candidate Acceleration-Gradient Volume Creation

## Canonical Filename

```text
candidate_acceleration_gradient_volume_creation.md
```

This document summarizes the output of:

```text
candidate_acceleration_gradient_volume_creation.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a final source law, not a frame-field definition, and not a completed \(\Sigma_V\) derivation.

Its purpose is to test the source-driven volume creation candidate:

\[
\Sigma_V=\chi\rho a^\mu\nabla_\mu A.
\]

The guiding question was:

```text
Can acceleration across gradient be made covariant,
or is it only a good cave-picture?
```

The answer is:

```text
Acceleration-gradient volume creation is the best postulate-facing source law candidate.

But the current bottleneck is not the scalar form; it is the frame:

  what is u^mu, and what projection defines a^mu nabla_mu A?

Best next test:
  candidate_volume_creation_frame_field_inventory.py
```

---

## Why This Study Matters

The source-driven volume creation audit identified one best candidate:

\[
\Sigma_V\sim\chi\rho a^\mu\nabla_\mu A.
\]

It is closest to the postulate-facing idea:

```text
mass/source response across an A-gradient creates or destroys vacuum volume.
```

But the candidate only becomes meaningful once acceleration, frame/projection, \(\chi\)-origin, static-source safety, boundary neutrality, and no-overlap are defined.

---

## Compact Acceleration-Gradient Ledger

| Entry | Form | Status | Consequence |
|---|---|---|---|
| AG1: acceleration-gradient target | \(\Sigma_V=\chi\rho a^\mu\nabla_\mu A\) | THEOREM_TARGET | decides whether source-driven companion branch has a real source law |
| AG2: covariant acceleration definition | \(a^\mu=u^\nu\nabla_\nu u^\mu\) | CANDIDATE | candidate becomes meaningful only after frame field is specified |
| AG3: vacuum rest-frame projection | \(a_\perp^\mu=P^\mu{}_\nu(u_{\rm vac})a^\nu,\;\nabla_\perp A=P\nabla A\) | RISK | ties directly to earlier missing vacuum frame field |
| AG4: matter-flow projection | \(\rho a_m^\mu\nabla_\mu A\), using matter congruence \(u_m^\mu\) | CANDIDATE | may be local but source-model dependent |
| AG5: static-source safety | \(\Sigma_V=0\), or boundary-neutral, for static equilibrium sources unless real acceleration exists | REQUIRED | ordinary-sector viability depends on this |
| AG6: sign / orientation ambiguity | \(a^\mu\nabla_\mu A\) may create or destroy volume depending on sign convention | UNRESOLVED | must be resolved before numerical or recovery claims |
| AG7: \(\chi\)-origin requirement | \(\chi\) fixed by ontology / source coupling before \(\gamma/AB\) checks | REQUIRED | \(\Sigma_V\) remains candidate only while \(\chi\) is not recovery-fit |
| AG8: coordinate velocity toy rejection | \(\rho v^i\partial_i A\) is diagnostic only | REJECTED | forces covariant / frame-safe expression |
| AG9: residual-kill / no-overlap | source-driven \(\zeta\) enters metric only through \(B_s\), or residual trace killed / non-metric | REQUIRED | prevents \(\zeta\) from doing both jobs |
| AG10: boundary neutrality | \(Q_{\rm ext}[\Sigma_V\;{\rm independent\;zeta}]=0\), or contribution absorbed into \(B_s\) | REQUIRED | prevents acceleration-gradient branch from becoming scalar gravity |
| AG11: recovery checks downstream | after \(\Sigma_V/F_\zeta\) fixed, test \(\gamma_{\rm like}=1\) and \(AB\to1\) | RECOVERY_TARGET | tests but does not define acceleration-gradient law |
| AG12: recommended next move | define the frame field \(u^\mu/u^\mu_{\rm vac}\) before refining \(\Sigma_V\) | RECOMMENDED | next script should inventory frame-field choices for \(a^\mu\) and projection |

---

## Status Counts

The run counted:

```text
CANDIDATE:       2
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        4
RISK:            1
THEOREM_TARGET:  1
UNRESOLVED:      1
```

Interpretation:

```text
The acceleration-gradient candidate is live but depends on frame definition.
u^mu or u_vac^mu is now the bottleneck.
Static-source safety, chi-origin, no-overlap, and boundary neutrality are mandatory.
Coordinate velocity remains rejected as a parent law.
```

---

## Minimal Candidate Form

Candidate:

\[
\Sigma_V=\chi\rho a^\mu\nabla_\mu A.
\]

with:

\[
a^\mu=u^\nu\nabla_\nu u^\mu.
\]

Open choices:

```text
1. Is u^mu matter flow or vacuum rest frame?
2. Is the contraction fully spacetime or spatially projected?
3. What fixes chi?
4. What makes static sources neutral?
5. How does zeta enter B_s without residual trace overlap?
```

---

## Good Failure / Branch Decision

Good failure:

```text
Sigma_V = chi rho a^mu nabla_mu A cannot be made frame-defined,
coefficient-fixed, static-neutral, and no-overlap compatible.
```

Consequence:

```text
acceleration-gradient branch fails for now.
Return to source-driven map as theorem target,
or test broader tensor candidates.
```

Bad failure:

```text
keep using acceleration-gradient language while u^mu and chi remain undefined.
```

---

## Failure Controls

Acceleration-gradient branch fails if:

1. \(u^\mu\) is not defined.
2. Vacuum frame is invented to fit recovery.
3. \(\chi\) is chosen from \(\gamma_{\rm like}\).
4. \(AB\) diagnostic chooses sign or coefficient.
5. Coordinate velocity replaces covariant acceleration.
6. Static density produces independent exterior scalar charge.
7. \(\zeta\) residual trace remains metric-active.
8. Boundary neutrality is absent.
9. No-overlap theorem is absent.

---

## What This Study Established

This study established that acceleration-gradient volume creation is the best postulate-facing source law candidate:

\[
\Sigma_V=\chi\rho a^\mu\nabla_\mu A.
\]

It also established that the bottleneck is no longer the scalar form.

The bottleneck is:

```text
the frame.
```

Specifically:

```text
what is u^mu,
what is u_vac^mu,
and what projection defines a^mu nabla_mu A?
```

---

## What This Study Did Not Establish

This study did not define \(u^\mu\).

It did not define \(u^\mu_{\rm vac}\).

It did not choose matter-frame versus vacuum-frame projection.

It did not define \(\chi\).

It did not prove static-source safety.

It did not prove boundary neutrality.

It did not define no-overlap.

---

## Current Best Interpretation

The acceleration-gradient branch should not be refined further until the frame field is inventoried.

Trying broader tensor candidates too early risks skipping the central missing object:

```text
the local rest frame of vacuum substance / source flow.
```

---

## Next Development Target

The next script should be:

```text
candidate_volume_creation_frame_field_inventory.py
```

Purpose:

```text
Inventory matter-flow, vacuum-flow, and projected-frame choices for a^mu nabla_mu A.
```

Reason:

```text
The acceleration-gradient branch cannot proceed until u^mu/u_vac^mu and projection are defined.
```

Expected result:

```text
A frame-field ledger:
  matter congruence u_m^mu,
  vacuum rest frame u_vac^mu,
  hybrid/projection choices,
  static-source safety,
  coordinate-gauge rejection,
  sign/orientation consequence,
  chi-origin dependency,
  boundary neutrality,
  no-overlap,
  branch-defer if no physical frame exists.
```

---

## Summary

The acceleration-gradient result is:

```text
The source law has a shape.
The frame is missing.
```

The next goblin gate is:

```text
who gets to say what “accelerating across the gradient” means?
```
