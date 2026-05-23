# Candidate Kappa Near-Boundary Deviation Diagnostic

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a prediction, not an observational claim, and not a completed comparison with GR. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_near_boundary_deviation_diagnostic.py
```

The guiding question was:

```text
If the joint-minimum model deviates from GR near a material boundary, what
exactly would deviate?
```

The answer is:

```text
Near-boundary deviation should be discussed only through diagnostics:
  delta_f,
  delta_g,
  delta_curv,
  delta_redshift.

No magnitude claim is justified until:
  weights are derived,
  transition width is derived,
  recombination map is fixed,
  observable is selected.
```

This is diagnostic discipline before prediction.

---

## Why This Study Matters

The joint-minimum energy-functional study suggested that the largest deviation from naive GR/Newtonian interior matching may occur near a material boundary.

But that does not yet mean the theory has a prediction.

A prediction needs:

```text
a reference profile,
a joint-minimum profile,
a map to observables,
a transition width,
a magnitude estimate,
and a check against existing constraints.
```

This study defines the diagnostics first.

---

## Reference and Joint Profiles

The reference profile is:

\[
f_{\rm GR,ref}(r).
\]

The joint-minimum profile is:

\[
f_{\rm joint}(r).
\]

The profile deviation is:

\[
\delta_f(r)
=
f_{\rm joint}(r)-f_{\rm GR,ref}(r).
\]

Status:

```text
CONSTRAINED_BY_IDENTITY — reference profile must be specified.
```

This is the most basic deviation diagnostic.

It is not yet an observable by itself.

---

## Acceleration Diagnostic

If \(f\) behaves like a potential or lapse-like scalar, the local radial acceleration deviation is proportional to:

\[
\delta_g(r)
=
-\frac{d\delta_f}{dr}.
\]

Equivalently:

\[
\delta_g
=
\frac{df_{\rm GR,ref}}{dr}
-
\frac{df_{\rm joint}}{dr}.
\]

This would likely peak where the transition layer bends fastest.

Status:

```text
CONSTRAINED_BY_IDENTITY — normalization / recombination missing.
```

This is a candidate diagnostic, not a final acceleration prediction.

---

## Curvature Diagnostic

The second-derivative curvature-like deviation is:

\[
\delta_{\rm curv}(r)
=
\frac{d^2\delta_f}{dr^2}.
\]

That is:

\[
\delta_{\rm curv}
=
-f_{\rm GR,ref}''(r)
+
f_{\rm joint}''(r).
\]

The areal Laplacian-like deviation is:

\[
\delta_{\rm lap}
=
\delta_f''
+
\frac{2}{r}\delta_f'.
\]

Status:

```text
CONSTRAINED_BY_IDENTITY — metric mapping still needed.
```

This is likely the most sensitive diagnostic for sharp transition layers.

---

## Redshift / Lapse Diagnostic

If the deviation enters a lapse-like factor \(A\):

\[
A_{\rm joint}
=
A_{\rm ref}
+
\delta_A,
\]

then the fractional clock/redshift deviation is:

\[
\sqrt{\frac{A_{\rm joint}}{A_{\rm ref}}}-1.
\]

Exactly:

\[
-1+\frac{\sqrt{A_{\rm ref}+\delta_A}}{\sqrt{A_{\rm ref}}}.
\]

For small \(\delta_A\):

\[
\frac{\delta_A}{2A_{\rm ref}}.
\]

Status:

```text
CONSTRAINED_BY_IDENTITY — requires recombination map.
```

This diagnostic cannot become a prediction until the theory says how the joint-minimum variable enters the metric.

---

## Transition Width Scaling

Let \(\epsilon\) be a characteristic profile deviation amplitude and \(\sigma\) the transition width.

Scaling estimates:

\[
\delta_f\sim\epsilon,
\]

\[
\delta_g\sim\frac{\epsilon}{\sigma},
\]

\[
\delta_{\rm curv}\sim\frac{\epsilon}{\sigma^2}.
\]

Thus curvature-like deviations are most sensitive to narrow transition layers.

Status:

```text
PLAUSIBLE — epsilon and sigma not derived.
```

This scaling is useful, but it is not yet a magnitude estimate.

---

## Region Hierarchy

The script produced this hierarchy:

| Region | Diagnostic expectation |
|---|---|
| deep interior | \(\delta\) may be small if quadratic tendency dominates |
| inner transition side | \(\delta_g\) and \(\delta_{\rm curv}\) may grow |
| material boundary | likely largest curvature-like diagnostic |
| near exterior | possible small relaxation back to \(1/r\) |
| far exterior | \(\delta\) should decay / vanish |

Status:

```text
PLAUSIBLE — magnitude unknown.
```

This keeps the expected deviation localized.

---

## Possible Observable Channels

Candidate observable channels:

1. Local acceleration near a dense body's surface.
2. Clock/redshift gradient near a surface.
3. Pressure/interior-equilibrium inference in compact objects.
4. Thin-shell laboratory density-interface tests.
5. Astrophysical surface matching effects.

Status:

```text
PLAUSIBLE — inventory only.
```

No channel is claimed viable yet.

These are only diagnostic buckets.

---

## Measurement Caution

This may be unmeasured or hard to measure because:

```text
interior curvature is not directly accessible in ordinary bodies,
near-surface Newtonian backgrounds dominate,
material systematics may swamp tiny deviations,
exterior far field must agree with GR,
compact-object interiors are model-dependent.
```

Therefore:

```text
possible deviation != practical test yet.
```

Status:

```text
CONSTRAINED_BY_IDENTITY — avoid overclaim.
```

---

## Failure Controls

The deviation diagnostic program fails if:

1. \(f_{\rm joint}\) and \(f_{\rm ref}\) are not mapped to observables.
2. \(\delta\) is nonzero only by arbitrary spline choice.
3. Far exterior \(\delta\) does not vanish.
4. Predicted acceleration/redshift deviation is already excluded.
5. \(\kappa\)-sector deviation is confused with \(A\)-sector mass flux.
6. Magnitude is claimed before \(\sigma\) and weights are derived.

---

## Classification

The script produced this classification:

| Diagnostic | Status |
|---|---|
| profile deviation \(\delta_f\) | CONSTRAINED_BY_IDENTITY |
| acceleration deviation \(\delta_g\) | CONSTRAINED_BY_IDENTITY |
| curvature deviation \(\delta_{\rm curv}\) | CONSTRAINED_BY_IDENTITY |
| redshift / lapse deviation | CONSTRAINED_BY_IDENTITY |
| transition width scaling | PLAUSIBLE |
| observable channels | PLAUSIBLE inventory only |
| magnitude prediction | MISSING |
| measurement claim | NOT MADE |

---

## What This Study Established

This study established:

1. Near-boundary deviations must be stated as diagnostics first.
2. The basic profile diagnostic is:
   \[
   \delta_f=f_{\rm joint}-f_{\rm GR,ref}.
   \]
3. The acceleration-like diagnostic is:
   \[
   \delta_g=-\delta_f'.
   \]
4. The curvature-like diagnostic is:
   \[
   \delta_{\rm curv}=\delta_f''.
   \]
5. The lapse/redshift diagnostic is linearized as:
   \[
   \frac{\delta_A}{2A_{\rm ref}}.
   \]
6. Transition width controls scaling.
7. No magnitude or measurement claim is justified yet.

---

## What This Study Did Not Establish

This study did not define \(f_{\rm GR,ref}\).

It did not solve for \(f_{\rm joint}\).

It did not derive the transition width \(\sigma\).

It did not derive the deviation amplitude \(\epsilon\).

It did not select an observable.

It did not estimate magnitude.

It did not prove measurability.

It only defined the diagnostic categories.

---

## Current Best Interpretation

Near-boundary deviation should be discussed only through diagnostics:

```text
delta_f,
delta_g,
delta_curv,
delta_redshift.
```

No magnitude claim is justified until:

```text
weights are derived,
transition width is derived,
recombination map is fixed,
observable is selected.
```

---

## Next Development Target

The output recommended:

```text
candidate_kappa_trace_response_status_summary.md
```

Purpose:

```text
Summarize group 10 current state.
```

Reason:

```text
Group 10 has reached a natural boundary: kappa status is now clear enough to
summarize before pushing numerical or observational speculation.
```

---

## Summary

This study gives the rule for near-boundary deviations:

```text
diagnostic before prediction.
```

The theory may imply a near-boundary deviation from GR, but the responsible next step is not a magnitude claim.

It is a status summary for the \(\kappa\) trace-response sector.
