# Candidate Volume Creation Frame Field Inventory

## Canonical Filename

```text
candidate_volume_creation_frame_field_inventory.md
```

This document summarizes the output of:

```text
candidate_volume_creation_frame_field_inventory.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a final frame definition, not a completed \(\Sigma_V\) source law, and not a covariant derivation.

Its purpose is to inventory frame choices for:

\[
\Sigma_V=\chi\rho a^\mu\nabla_\mu A.
\]

The guiding question was:

```text
Who gets to say what accelerating across the gradient means?
```

The answer is:

```text
The frame inventory reduces the branch to two clean candidates:

  matter congruence u_m^mu
  vacuum rest frame u_vac^mu

Hybrid projection should wait until both are defined.

Best next test:
  candidate_matter_vs_vacuum_frame_branch_test.py
```

---

## Why This Study Matters

The acceleration-gradient audit found that:

\[
\Sigma_V=\chi\rho a^\mu\nabla_\mu A
\]

is the best postulate-facing source law candidate.

But the bottleneck is no longer the scalar form. The bottleneck is the frame:

```text
what is u^mu,
what is u_vac^mu,
and what projection defines a^mu nabla_mu A?
```

This frame-field inventory prevents the branch from hiding an arbitrary gauge choice inside the word "acceleration."

---

## Compact Frame-Field Ledger

| Entry | Frame Choice | Status | Consequence |
|---|---|---|---|
| FF1: frame-field target | choose physical \(u^\mu/u^\mu_{\rm vac}\) for \(\Sigma_V=\chi\rho a^\mu\nabla_\mu A\) | THEOREM_TARGET | decides whether acceleration-gradient candidate can be covariant |
| FF2: matter congruence frame | \(u^\mu=u_m^\mu\) from matter flow; \(a_m^\mu=u_m^\nu\nabla_\nu u_m^\mu\) | CANDIDATE | works best for fluid / dust sources but may be source-dependent |
| FF3: vacuum rest frame | \(u^\mu=u_{\rm vac}^\mu\) from local rest frame of vacuum substance / \(\zeta\) flow | CANDIDATE | best aligned with vacuum ontology but currently missing |
| FF4: projected matter acceleration | \(\Sigma_V=\chi\rho(P_{\rm vac}a_m)^\mu(P_{\rm vac}\nabla A)_\mu\) | RISK | may express mass accelerating across vacuum gradient, but adds structure |
| FF5: vacuum acceleration of vacuum flow | \(\Sigma_V=\chi\rho a_{\rm vac}^\mu\nabla_\mu A\) | RISK | may shift source law away from matter acceleration |
| FF6: hypersurface normal frame | \(u^\mu=n^\mu\), normal to chosen slicing | CONSTRAINED | likely diagnostic only unless tied to vacuum rest frame |
| FF7: coordinate velocity frame | \(u^\mu\) from coordinate velocity \(v^i\) | REJECTED | prevents \(\rho v\cdot\nabla A\) from becoming field equation |
| FF8: static-source safety | frame choice makes \(\Sigma_V\) static-neutral unless physical acceleration / exchange exists | REQUIRED | kills frame choices that make static matter source scalar volume charge |
| FF9: sign / orientation rule | frame / projection fixes sign of \(a\cdot\nabla A\) as creation / destruction | UNRESOLVED | needed before numerical or recovery claims |
| FF10: \(\chi\)-origin dependency | frame choice does not fix \(\chi\) by recovery; \(\chi\) still needs ontology / source coupling | REQUIRED | frame field alone cannot complete \(\Sigma_V\) derivation |
| FF11: boundary / no-overlap requirements | source-driven \(\zeta\) is boundary-neutral and enters metric only through \(B_s\) | REQUIRED | frame-safe source still fails if accounting fails |
| FF12: recommended next move | test vacuum rest frame vs matter congruence frame before hybrid projection | RECOMMENDED | next script should compare \(u_{\rm matter}\) and \(u_{\rm vac}\) branches directly |

---

## Status Counts

The run counted:

```text
CANDIDATE:       2
CONSTRAINED:     1
RECOMMENDED:     1
REJECTED:        1
REQUIRED:        3
RISK:            2
THEOREM_TARGET:  1
UNRESOLVED:      1
```

Interpretation:

```text
Matter congruence and vacuum rest frame are the two clean branches.
Hybrid projection is possible but risky unless both frames are defined.
Hypersurface normal is diagnostic unless physically tied to vacuum ontology.
Coordinate velocity is rejected as parent frame.
Static neutrality, chi-origin, boundary neutrality, and no-overlap remain mandatory.
```

---

## Frame Decision Tree

### 1. Matter Frame \(u_m^\mu\)

```text
Good for source-local acceleration,
but source-model dependent.
```

### 2. Vacuum Frame \(u_{\rm vac}^\mu\)

```text
Best ontology match,
but currently missing.
```

### 3. Hybrid Projection

```text
Only after u_m and u_vac are both defined.
```

### 4. Hypersurface Normal

```text
Diagnostic unless slicing is physically defined.
```

### 5. Coordinate Velocity

```text
Rejected as parent law.
```

---

## Good Failure / Branch Decision

Good failure:

```text
no matter/vacuum frame can define acceleration-gradient volume creation
while preserving static neutrality, chi-origin, boundary neutrality, and no-overlap.
```

Consequence:

```text
acceleration-gradient source law fails for now.
Return to Sigma_V theorem target or test broader tensor candidates.
```

Bad failure:

```text
choose a convenient frame and proceed as if it were physical.
```

---

## Failure Controls

Frame-field inventory fails if:

1. Coordinate velocity becomes parent frame.
2. Vacuum frame is invented to fit recovery.
3. Hypersurface normal is treated as physical without ontology.
4. Hybrid projection is used before both frames are defined.
5. Static source creates independent exterior \(\zeta\) charge.
6. Frame choice hides \(\chi\) tuning.
7. Boundary neutrality is absent.
8. No-overlap theorem is absent.

---

## What This Study Established

This study established that the frame inventory reduces the branch to two clean candidates:

```text
matter congruence u_m^mu
vacuum rest frame u_vac^mu
```

It also established that hybrid projection should wait until both are defined.

Coordinate velocity is rejected as a parent frame.

The hypersurface normal frame remains diagnostic unless physical slicing is supplied by vacuum ontology.

---

## What This Study Did Not Establish

This study did not choose between \(u_m^\mu\) and \(u_{\rm vac}^\mu\).

It did not define \(u_{\rm vac}^\mu\).

It did not prove static-source safety.

It did not fix the sign / orientation convention.

It did not derive \(\chi\).

It did not prove boundary neutrality or no-overlap.

---

## Current Best Interpretation

The acceleration-gradient branch should now compare:

```text
matter-flow frame
vacuum-flow frame
```

directly.

A hybrid projection may be physically appealing, but using it now would hide the fact that neither branch has yet been tested cleanly.

---

## Next Development Target

The next script should be:

```text
candidate_matter_vs_vacuum_frame_branch_test.py
```

Purpose:

```text
Compare u_matter and u_vac frame branches directly.
```

Reason:

```text
The next bottleneck is choosing between matter-flow and vacuum-flow frames before adding hybrid projections.
```

Expected result:

```text
A matter-vs-vacuum frame branch ledger:
  matter congruence source law,
  vacuum rest-frame source law,
  hybrid projection deferred,
  static-source safety,
  source-model dependence,
  ontology-native frame requirement,
  sign/orientation requirement,
  chi-origin requirement,
  boundary/no-overlap requirements,
  branch-defer if neither frame is physical.
```

---

## Summary

The frame-field result is:

```text
The source law has two candidate clocks.
```

The next goblin gate is:

```text
does matter carry the clock, or does vacuum?
```
