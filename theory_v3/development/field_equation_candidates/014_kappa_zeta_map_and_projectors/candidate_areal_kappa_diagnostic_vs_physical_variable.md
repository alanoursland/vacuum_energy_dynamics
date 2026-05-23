# Candidate Areal Kappa Diagnostic Versus Physical Variable

## Canonical Filename

```text
candidate_areal_kappa_diagnostic_vs_physical_variable.md
```

This document summarizes the output of:

```text
candidate_areal_kappa_diagnostic_vs_physical_variable.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of physical \(\kappa\), not a covariant map from \(\kappa\) to \(\zeta\), and not a parent field-equation construction.

Its purpose is to separate reduced areal diagnostic \(\kappa\) from any physical / residual \(\kappa\).

The guiding question was:

```text
How do we keep kappa = 1/2 ln(A B) useful without letting it become a smuggled physical scalar?
```

The answer is:

```text
Areal kappa is useful but dangerous:

  kappa_areal = 1/2 ln(A B)

Use it as:
  reduced diagnostic,
  exterior recovery check,
  A/B mismatch test instrument.

Do not use it as:
  covariant physical scalar,
  independent trace insertion,
  physical e_kappa basis,
  parent field-equation building block.
```

---

## Why This Study Matters

The previous trace-counting result established the active theorem target:

\[
{\rm Trace}[g_{ij}^{\rm scalar}]
=
{\rm Trace}_{A,{\rm mass}}
+
{\rm Trace}_{\rm residual,neutral},
\]

with no overlap.

The areal relation:

\[
\kappa_{\rm areal}
=
\frac12\ln(AB)
\]

is powerful in static spherical areal reduction, because:

\[
\kappa_{\rm areal}\to0
\]

corresponds to:

\[
AB\to1.
\]

But that relation is also dangerous. If silently promoted, it can smuggle reduced spherical metric structure into the parent theory.

---

## Compact Areal-Kappa Ledger

| Entry | Branch | Status | Consequence |
|---|---|---|---|
| K1: areal kappa as reduced diagnostic only | \(\kappa_{\rm areal}=\frac12\ln(AB)\) | RECOMMENDED | safe to use as test instrument, not as field-equation building block |
| K2: exterior recovery diagnostic | \(\kappa_{\rm areal}\to0\) corresponds to \(AB\to1\) in recovered exterior | SAFE_IF | \(AB=1\) remains target / diagnostic, not derivation |
| K3: areal kappa as physical trace variable | \(\kappa_{\rm phys}:=\frac12\ln(AB)\) | RISK | unsafe until derived; risks GR smuggling and scalar double-counting |
| K4: areal kappa as proxy for \(\zeta-\zeta_{\min}\) | \(\kappa_{\rm areal}\sim\zeta-\zeta_{\min}\) in spherical reduction | CANDIDATE | may guide \(\kappa\)-\(\zeta\) map but cannot define it yet |
| K5: residual / relaxation kappa distinct from areal diagnostic | \(\kappa_{\rm residual}\ne\kappa_{\rm areal}\) unless mapped | CANDIDATE | allows \(e_\kappa\) to remain provisional if residual variable survives |
| K6: silent covariant promotion | use \(\kappa=\frac12\ln(AB)\) as general scalar in parent equation | FORBIDDEN | would smuggle reduced spherical metric structure into the parent theory |
| K7: \(e_\kappa\) if kappa is diagnostic only | \(e_\kappa=\frac12K_\kappa(\kappa-\kappa_{\min})^2\) with diagnostic \(\kappa\) | UNRESOLVED | \(e_\kappa\) may need retirement, reinterpretation, or residual-variable relabeling |
| K8: recombination use of areal kappa | \(\kappa_{\rm areal}\) used in recombination diagnostics | CONSTRAINED | can test recombination but not define physical trace insertion |
| K9: \(A_{\rm spatial}\) recovery dependency | \(A_{\rm spatial}\) recovery uses \(\kappa_{\rm areal}\) to diagnose \(AB\) mismatch | SAFE_IF | fencing areal kappa now makes \(A_{\rm spatial}\) recovery safer next |
| K10: count-once theorem preservation | \({\rm Trace}[g_{ij}^{\rm scalar}]={\rm Trace}_{A,{\rm mass}}+{\rm Trace}_{\rm residual,neutral}\) with no overlap | REQUIRED | preserves previous trace-counting theorem target |
| K11: diagnostic failure outcome | no clean map from \(\kappa_{\rm areal}\) to \(\zeta\) without gauge / slicing assumptions | SAFE_IF | forces physical \(\kappa\), if any, to be separately defined |
| K12: recommended convention | areal kappa is reduced diagnostic; physical / residual \(\kappa\) remains unresolved | RECOMMENDED | use \(\kappa_{\rm areal}\) as test instrument, not building block |

---

## Status Counts

```text
CANDIDATE:    2
CONSTRAINED:  1
FORBIDDEN:    1
RECOMMENDED:  2
REQUIRED:     1
RISK:         1
SAFE_IF:      3
UNRESOLVED:   1
```

Interpretation:

```text
Areal kappa is valuable as a reduced diagnostic.
Silent promotion to a physical / covariant scalar is forbidden.
Physical or residual kappa remains unresolved and must be separately defined.
e_kappa remains provisional until residual kappa survives as more than a diagnostic.
```

---

## Recommended Convention

Recommended for now:

\[
\kappa_{\rm areal}
=
\frac12\ln(AB).
\]

This is:

```text
a reduced spherical areal-gauge diagnostic,
an exterior recovery check,
a test instrument for A/B mismatch.
```

It is not:

```text
a covariant physical scalar,
an independent spatial trace insertion,
a sufficient basis for physical e_kappa,
a parent field-equation building block.
```

Physical / residual \(\kappa\) remains unresolved.

---

## \(AB=1\): Recovery, Not Construction

Safe phrasing:

```text
In the recovered static spherical exterior, kappa_areal -> 0 corresponds to A B -> 1.
This is a diagnostic of exterior recovery.
It is not a derivation of the parent metric structure.
```

Unsafe phrasing:

```text
Set kappa = 0, therefore A B = 1, therefore the exterior metric is fixed.
```

Rule:

```text
AB=1 is a recovery target / check, not a construction principle.
```

---

## Good Failure Outcome

A useful negative result would be:

```text
no clean map from kappa_areal to zeta without gauge / slicing assumptions.
```

This does not kill all \(\kappa\)-language.

It means:

```text
kappa_areal stays diagnostic-only,
and physical kappa, if any, must be separately defined.
```

---

## What This Study Established

This study established that areal \(\kappa\) is allowed as:

```text
reduced diagnostic,
exterior recovery check,
A/B mismatch test instrument.
```

It is not allowed as:

```text
covariant physical scalar,
independent trace insertion,
physical e_kappa basis,
parent field-equation building block.
```

The study also preserved the count-once theorem target:

\[
{\rm Trace}[g_{ij}^{\rm scalar}]
=
{\rm Trace}_{A,{\rm mass}}
+
{\rm Trace}_{\rm residual,neutral},
\]

with no overlap.

---

## What This Study Did Not Establish

This study did not derive a physical \(\kappa\).

It did not derive a covariant map from \(\kappa_{\rm areal}\) to \(\zeta\).

It did not decide whether \(e_\kappa\) survives.

It did not derive \(A_{\rm spatial}\).

It did not prove the parent exterior recovery theorem.

---

## Current Best Interpretation

\[
\kappa_{\rm areal}
=
\frac12\ln(AB)
\]

is a useful reduced diagnostic.

It should be kept in a labeled box:

```text
test instrument,
not building block.
```

Physical / residual \(\kappa\) remains unresolved.

---

## Next Development Target

The next script should be:

```text
candidate_A_spatial_recovery_constraint.py
```

Purpose:

```text
Identify what A_spatial is required to recover without importing GR.
```

Reason:

```text
Areal kappa is now fenced as diagnostic.
Next identify A_spatial recovery requirements without using kappa as hidden physical scalar.
```

---

## Summary

The areal-\(\kappa\) result is:

```text
Use kappa_areal as a reduced diagnostic.
Do not let it become a smuggled physical scalar.
```

The next goblin gate is:

```text
what must A_spatial recover, without copying GR?
```
