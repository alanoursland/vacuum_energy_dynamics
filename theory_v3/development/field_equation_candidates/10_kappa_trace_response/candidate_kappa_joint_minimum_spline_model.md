# Candidate Kappa Joint Minimum Spline Model

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final variational theory, not a claim of a measured deviation from GR, and not a completed interior/exterior matching model. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_joint_minimum_spline_model.py
```

The guiding question was:

```text
Can interior quadratic tendency and exterior reciprocal tendency be represented
as one smooth vacuum-curvature minimum curve?
```

The answer is:

```text
Yes, as a toy modeling basis.

A joint-minimum spline model can represent:
  interior quadratic tendency,
  exterior reciprocal 1/r tendency,
  smooth near-surface compromise.

This supports the idea that interior curvature need not be exactly
Newtonian/parabolic near the surface.

The real version should be variational:
  minimize a combined interior/exterior/smoothness energy.
```

Important interpretation:

```text
The near-boundary gravity prediction may deviate from GR.
```

But this should be treated carefully:

```text
the deviation is theoretical at this stage,
it is likely near-surface/interior dominated,
and it may be very difficult to measure directly.
```

---

## Why This Study Matters

The previous \(\kappa\) studies suggested that an interior trace/volume response cannot simply be a raw Poisson field sourced by pressure.

The better picture is:

```text
matter shifts a local vacuum-curvature minimum,
the exterior vacuum configuration also participates,
and the realized profile is a smooth joint minimum.
```

That means the interior may not be exactly the naive Newtonian parabola.

A mass source may create a quadratic interior tendency, while the exterior vacuum prefers a reciprocal \(1/r\)-type configuration.

The boundary region then has to reconcile both.

---

## Interior and Exterior Tendencies

The toy interior regular quadratic tendency is:

\[
f_{\rm int}(r)=a_0+a_2r^2.
\]

The toy exterior reciprocal tendency is:

\[
f_{\rm ext}(r)=1-\frac{M}{r}.
\]

These are not asserted as final metric functions in this script.

They are basis tendencies for a joint minimum model.

Status:

```text
PLAUSIBLE — coefficients/source relation not derived.
```

---

## Hermite Transition Layer

The script first listed a cubic Hermite basis on:

\[
x\in[0,1].
\]

The basis functions are:

\[
H_{00}=2x^3-3x^2+1,
\]

\[
H_{10}=x^3-2x^2+x,
\]

\[
H_{01}=-2x^3+3x^2,
\]

\[
H_{11}=x^3-x^2.
\]

This can match value and first derivative across a transition layer.

Status:

```text
PLAUSIBLE — C1 smooth; C2 requires quintic or higher.
```

Since earlier boundary checks showed second-derivative jumps can matter, cubic Hermite is probably not smooth enough for the final \(\kappa\) interface.

---

## Quintic Smoothstep for C2 Matching

The quintic smoothstep is:

\[
s(x)=6x^5-15x^4+10x^3.
\]

It satisfies:

\[
s'(0)=0,
\]

\[
s'(1)=0,
\]

\[
s''(0)=0,
\]

\[
s''(1)=0.
\]

Status:

```text
DERIVED_REDUCED
```

This basis can splice tendencies without value, slope, or curvature jumps.

It is a better toy basis for the boundary region.

---

## Blended Joint Minimum

The transition coordinate is:

\[
x=\frac{r-(R-w)}{w}.
\]

The smooth blend is:

\[
f_{\rm joint}
=
(1-s)f_{\rm int}+sf_{\rm ext}.
\]

where:

\[
f_{\rm int}=a_0+a_2r^2,
\]

and:

\[
f_{\rm ext}=1-\frac{M}{r}.
\]

Interpretation:

```text
near the inner side, interior tendency dominates;
near the outer side, exterior reciprocal tendency dominates;
the transition region modifies the naive interior parabola near the surface.
```

Status:

```text
PLAUSIBLE — energy functional not derived.
```

This is a modeling device, not yet a physical minimizer.

---

## Direct Boundary Matching

If directly matching at \(R\) without a transition layer, C1 matching gives:

\[
a_2R^2+a_0
=
1-\frac{M}{R},
\]

and:

\[
2Ra_2
=
\frac{M}{R^2}.
\]

Solving gives:

\[
a_0=\frac{-3M+2R}{2R},
\]

\[
a_2=\frac{M}{2R^3}.
\]

Status:

```text
DERIVED_REDUCED — toy coefficient relation only.
```

This shows exterior \(1/r\) boundary conditions can determine the best quadratic interior coefficients if direct matching is imposed.

With a transition layer, the interior can remain more Newtonian in the bulk while the boundary region absorbs the smoothing.

---

## Curvature Deviation Near the Surface

The spline model implies:

```text
the interior bulk may look approximately quadratic;
near the surface, the exterior reciprocal minimum pulls the curve away from the
naive parabola;
the transition layer distributes that correction smoothly.
```

Therefore:

```text
internal curvature is not exactly the Newtonian parabolic prediction;
exterior may also be slightly adjusted near the surface in a full joint-minimum
model;
exterior far field should still recover reciprocal 1/r behavior.
```

Status:

```text
PLAUSIBLE — observable consequences not assessed.
```

This is where a possible deviation from GR enters.

But it is not yet quantified.

---

## Possible Near-Boundary Deviation From GR

If this picture is right, the most likely deviation is not a large far-field effect.

It would be concentrated near the matter/vacuum interface.

Possible locations:

```text
inside the body near the surface,
in a thin exterior transition region,
or in how interior curvature matches to exterior curvature.
```

This could imply that the near-boundary gravity prediction differs slightly from the GR interior/exterior matching prediction.

But this is not yet a prediction until the model provides:

```text
a definite variational energy,
a definite transition width,
a definite coupling strength,
a definite exterior recovery scale,
and a definite observable.
```

It is also plausible that no one has directly measured this kind of interior/near-surface curvature effect with the needed precision, especially inside matter.

For now, this should be classified as:

```text
possible theoretical deviation,
not established observable prediction.
```

---

## Energy Functional Placeholder

The script sketched a real joint-minimum model as an energy functional:

\[
E[f]
=
\int
\left[
W_{\rm int}(r)(f-f_{\rm int})^2
+
W_{\rm ext}(r)(f-f_{\rm ext})^2
+
\lambda_1(f')^2
+
\lambda_2(f'')^2
\right]dr.
\]

The minimizer would naturally compromise between interior and exterior tendencies while penalizing sharp boundary curvature.

Status:

```text
PLAUSIBLE — weights and variational derivation missing.
```

This is the more principled version of spline blending.

---

## Relation to Kappa

The spline variable may represent one of:

```text
A-like scalar response,
kappa_min,
an effective curvature/volume profile.
```

For \(\kappa\) specifically:

```text
matter trace shifts kappa_min in the interior,
exterior vacuum requires kappa_min -> 0,
boundary smoothing gives compact kappa response.
```

This supports non-propagating trace relaxation rather than breathing waves.

Status:

```text
CONSTRAINED_BY_IDENTITY — variable identification must be fixed.
```

---

## Failure Controls

The spline / joint-minimum model fails if:

1. The spline is used only as curve-fitting with no energy principle.
2. Exterior \(1/r\) far field is spoiled.
3. The transition creates hidden shell stress.
4. Interior deviation conflicts with known matching constraints.
5. \(\kappa\) and \(A\) profiles are mixed inconsistently.
6. Smoothing hides rather than explains scalar confinement.
7. A claimed near-boundary deviation is presented without a definite observable.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| interior quadratic tendency | PLAUSIBLE basis |
| exterior reciprocal tendency | PLAUSIBLE / required far field |
| Hermite C1 splice | PLAUSIBLE |
| quintic C2 smoothstep | DERIVED_REDUCED smoothness |
| direct C1 coefficient matching | DERIVED_REDUCED toy relation |
| near-surface interior deviation | PLAUSIBLE |
| joint energy functional | PLAUSIBLE / missing derivation |
| final physical spline model | UNFINISHED |

---

## What This Study Established

This study established:

1. A spline model can combine \(r^2\)-like interior behavior with \(1/r\)-like exterior behavior.
2. Quintic smoothstep supports C2 boundary smoothness.
3. Direct matching relates interior quadratic coefficients to exterior reciprocal behavior.
4. A transition layer can move deviation into the near-boundary region.
5. The model suggests interior curvature need not be exactly Newtonian/parabolic near the surface.
6. A real version must be variational.

---

## What This Study Did Not Establish

This study did not derive the energy functional.

It did not derive \(W_{\rm int}\), \(W_{\rm ext}\), \(\lambda_1\), or \(\lambda_2\).

It did not identify the spline variable definitively.

It did not quantify the deviation from GR.

It did not prove observability.

It did not check whether such a deviation is already constrained.

It only established a plausible modeling framework.

---

## Current Best Interpretation

A joint-minimum spline model can represent:

```text
interior quadratic tendency,
exterior reciprocal 1/r tendency,
smooth near-surface compromise.
```

This supports the idea that interior curvature need not be exactly Newtonian/parabolic near the surface.

The real version should be variational:

```text
minimize a combined interior/exterior/smoothness energy.
```

---

## Next Development Target

The next script should be:

```text
candidate_kappa_joint_minimum_energy_functional.py
```

Purpose:

```text
Make the spline model variational instead of hand-blended.
```

Reason:

```text
Near-boundary deviation becomes meaningful only if the joint curve comes from an
energy minimization rather than chosen smoothing.
```

Expected result:

```text
Construct a toy energy functional whose Euler-Lagrange equation shows how
interior tendency, exterior tendency, and smoothness penalty compete.
```

Also include:

```text
a symbolic deviation diagnostic from naive GR/Newtonian matching near the boundary.
```

---

## Summary

The joint-minimum spline model says:

```text
the boundary is not just a seam;
it may be where interior and exterior vacuum-curvature tendencies negotiate a
smooth minimum.
```

That may imply a near-boundary deviation from GR.

But for now, that is only a theoretical possibility.

The next step is to make the smoothing variational.
