# Candidate Kappa Boundary Layer Source Compatibility

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final source law, not a derived interface theory, and not a completed interior/exterior curvature model. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_boundary_layer_source_compatibility.py
```

The guiding question was:

```text
Can the smooth C2 compact kappa profile be produced by plausible
trace/pressure/minimum-shift physics?
```

The answer is:

```text
The C2 compact profile is not naturally produced by raw pressure as an elliptic
Poisson source.

Its Delta-kappa source is compensated/sign-changing.

However, in the non-inertial relaxation picture, matter trace does not need to
equal Delta kappa.

Instead it can shift the local minimum:

  kappa_min = chi_k S_trace_effective

Then a smooth compact kappa_min can produce a smooth compact kappa without
treating trace as a radiative scalar charge.
```

This favors the non-inertial minimum-shift picture.

---

## Why This Study Matters

The previous second-derivative boundary-stress study found that the smoother C2 profile:

\[
\kappa(r)=\kappa_0\left(1-\frac{r^2}{R^2}\right)^3
\]

can match exterior \(\kappa=0\) through second derivative.

It has:

\[
\kappa(R)=0,
\]

\[
\kappa'(R)=0,
\]

\[
\kappa''(R)=0,
\]

zero boundary flux, and zero net effective source.

But that only proves mathematical smoothness.

This study asks whether the source required by that profile is physically plausible.

---

## C2 Effective Source

For the C2 profile:

\[
\kappa
=
\kappa_0\left(1-\frac{r^2}{R^2}\right)^3,
\]

the elliptic effective source is:

\[
S_{\rm eff}
\sim
\Delta\kappa.
\]

The script found:

\[
S_{\rm eff}
=
-\frac{6\kappa_0(-R+r)(R+r)(-3R^2+7r^2)}{R^6}.
\]

The integrated effective source is:

\[
Q_{\rm eff}=0.
\]

Status:

```text
DERIVED_REDUCED — source interpretation pending.
```

---

## Sign Structure

The effective source has an internal zero at:

\[
r=\sqrt{\frac{3}{7}}R.
\]

So \(S_{\rm eff}\) changes sign inside the matter support.

Status:

```text
CONSTRAINED_BY_IDENTITY — raw pressure trace cannot directly produce it.
```

This is important.

A raw positive pressure source cannot be the whole explanation.

---

## Raw Pressure Trace Comparison

The toy raw pressure trace was:

\[
S_{\rm raw}=3p_0\left(1-\frac{r^2}{R^2}\right).
\]

For:

\[
p_0>0,
\qquad
0\le r\le R,
\]

we have:

\[
S_{\rm raw}\ge0.
\]

But the C2 effective source changes sign.

Therefore raw pressure trace alone is incompatible with the C2 effective source if \(\kappa\) is treated as a Poisson/elliptic field sourced by \(\Delta\kappa\).

Status:

```text
REJECTED — unless projected or combined with compensation.
```

---

## Compensated Trace Comparison

The compensated pressure trace is:

\[
S_{\rm comp}
=
-\frac{3p_0(-3R^2+5r^2)}{5R^2}.
\]

The C2 effective source is:

\[
S_{\rm eff}
=
-\frac{6\kappa_0(-R+r)(R+r)(-3R^2+7r^2)}{R^6}.
\]

Both have:

```text
zero net integral,
sign-changing structure.
```

They are not identical shapes.

But they are in the same compensated-source family.

Status:

```text
PLAUSIBLE — exact source law not derived.
```

This keeps the compensated-source option alive, but it still needs a parent identity.

---

## Shifted Local Minimum Interpretation

If non-inertial relaxation reaches local equilibrium:

\[
\kappa=\kappa_{\min},
\]

and:

\[
\kappa_{\min}=\chi_\kappa S_{\rm trace,effective},
\]

then the required effective trace source is:

\[
S_{\rm trace,effective}
=
\frac{\kappa_0(R^2-r^2)^3}{R^6\chi_\kappa}.
\]

This source is:

```text
compact,
positive for kappa_0 / chi_k > 0,
smoothly zero at R.
```

This is different from the elliptic effective source \(\Delta\kappa\).

In the non-inertial model, trace shifts the minimum rather than acting as a Poisson charge.

Status:

```text
PLAUSIBLE — chi_k and source law not derived.
```

This is the most important result of the run.

---

## Operator-Dependence Warning

Source compatibility depends on which equation \(\kappa\) obeys.

If \(\kappa\) is elliptic:

```text
source ~ Delta kappa,
C2 implies compensated/sign-changing source.
```

If \(\kappa\) is non-inertial relaxation:

```text
source shifts kappa_min,
C2 can come from a compact positive shifted minimum.
```

Therefore the non-inertial model is more compatible with ordinary interior trace response than a Poisson-source \(\kappa\) model.

Status:

```text
CONSTRAINED_BY_IDENTITY — supports non-inertial minimum-shift picture.
```

---

## Boundary / Interface Interpretation

The smooth compact C2 profile may reflect:

```text
matter trace source in the interior,
plus vacuum-interface restoration near the boundary.
```

rather than raw pressure source alone.

This suggests a two-part minimum:

\[
\kappa_{\min}(r)
=
\text{interior trace shift}
\times
\text{boundary cutoff}.
\]

The boundary cutoff enforces:

\[
\kappa_{\min}(R)=0,
\]

\[
\kappa_{\min}'(R)=0,
\]

\[
\kappa_{\min}''(R)=0.
\]

Status:

```text
PLAUSIBLE — interface law missing.
```

---

## Relation to Interior / Exterior Curvature

This study suggests the interior curvature should not be assumed to be exactly the Newtonian quadratic profile.

A mass source may impose a roughly quadratic interior tendency, while the exterior vacuum minimum prefers a reciprocal \(1/r\)-type configuration.

The actual minimum configuration may be a smooth joint solution of the two tendencies:

```text
interior regularity / approximate quadratic behavior,
exterior reciprocal vacuum falloff,
boundary smoothness,
zero kappa flux,
no breathing propagation.
```

This means the interior curve may bend away from the naive parabola near the surface so that the interior and exterior form one smooth minimum-energy configuration.

This is theoretical.

It may be difficult or impossible to measure directly as interior curvature.

But it is a useful modeling direction.

---

## Failure Controls

Source compatibility fails if:

1. Raw pressure is claimed to produce sign-changing \(\Delta\kappa\) directly.
2. Compensation is inserted with no parent identity.
3. Boundary cutoff is chosen only to hide exterior \(\kappa\).
4. Shifted-minimum source is not connected to trace/volume physics.
5. Interface restoration conflicts with \(A\)-sector mass flux.
6. \(\kappa\) dynamics are mixed inconsistently between Poisson and relaxation pictures.

---

## Classification

The script produced this classification:

| Interpretation | Status |
|---|---|
| raw pressure trace as elliptic source | REJECTED as sole source |
| compensated trace as elliptic source | PLAUSIBLE / needs parent identity |
| C2 source as \(\Delta\kappa\) | DERIVED_REDUCED shape, source law missing |
| shifted local minimum \(\kappa_{\min}\) | PLAUSIBLE |
| boundary cutoff / interface restoration | PLAUSIBLE |
| hand-chosen smoothing | RISK |
| final source compatibility | UNFINISHED |

---

## What This Study Established

This study established:

1. The C2 profile is not naturally produced by raw pressure as an elliptic Poisson source.
2. The C2 \(\Delta\kappa\) source changes sign.
3. The C2 source resembles a compensated trace family.
4. The non-inertial shifted-minimum interpretation is more natural.
5. Matter trace can shift \(\kappa_{\min}\) without becoming a radiative scalar charge.
6. Boundary/interface restoration likely matters.
7. Source compatibility is still unfinished.

---

## What This Study Did Not Establish

This study did not derive \(\chi_\kappa\).

It did not derive \(S_{\rm trace,effective}\).

It did not derive the boundary cutoff.

It did not prove the spline/joint-minimum picture.

It did not solve the full interior/exterior curvature profile.

It only clarified which source interpretation is most plausible.

---

## Current Best Interpretation

The C2 compact profile is not naturally produced by raw pressure as an elliptic Poisson source.

Its \(\Delta\kappa\) source is compensated/sign-changing.

However, in the non-inertial relaxation picture, matter trace does not need to equal \(\Delta\kappa\).

Instead it can shift the local minimum:

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace,effective}.
\]

Then a smooth compact \(\kappa_{\min}\) can produce a smooth compact \(\kappa\) without treating trace as a radiative scalar charge.

---

## Next Development Target

The output recommended:

```text
candidate_kappa_minimum_shift_source_model.py
```

But the current discussion sharpens that target.

The better next script is:

```text
candidate_kappa_joint_minimum_spline_model.py
```

Purpose:

```text
Model the interior quadratic tendency and exterior reciprocal tendency as a
single smooth minimum-energy curve.
```

Reason:

```text
The source compatibility issue now points to joint interior/exterior smoothing,
not only a local cutoff.
```

Expected result:

```text
Construct toy spline profiles that can support interior x^2-like behavior,
exterior 1/x-like behavior, boundary smoothness, and controlled deviation near
the surface.
```

---

## Summary

The source-compatibility study says the goblin thing plainly:

```text
Do not treat kappa as a raw Poisson field sourced by pressure.
```

The better picture is:

```text
matter shifts a local vacuum-curvature minimum;
the exterior vacuum minimum participates;
the actual curve is a smooth joint configuration.
```

The next model should use splines or matched basis functions that can support both:

\[
r^2
\]

and:

\[
\frac{1}{r}.
\]
