# Candidate Compare GR Interior Schwarzschild

## What This Document Is

This document is a diagnostic comparison note.

It is not a derivation of GR, not a proof of the reduced theory, and not a formal commitment to match the GR interior solution.

Its purpose is to summarize the result of:

```text
candidate_compare_gr_interior_schwarzschild.py
```

The guiding question was:

```text
How does the reduced constant-density interior A model compare to the exact
GR interior Schwarzschild solution?
```

The result is:

```text
The reduced interior A model agrees with GR at the surface and at first
weak-field order, but differs at higher order inside matter.

The largest structural difference is that forcing kappa=0 inside gives B=1/A,
whereas the GR interior Schwarzschild solution generally has AB != 1 inside.
```

This supports the interpretation that:

```text
kappa=0 should be treated as a source-free exterior condition, not necessarily
an interior matter condition.
```

---

## Dimensionless Setup

Use the dimensionless variables:

$$x=\frac{r}{R},$$

and:

$$u=\frac{r_s}{R}=\frac{2GM}{c^2R}.$$

Here \(R\) is the source radius and \(u\) is the compactness.

The reduced interior \(A\)-model for a uniform-density sphere is:

$$A_{\rm red}(x)=1-\frac{3u}{2}+\frac{u x^2}{2}.$$

The exact GR interior Schwarzschild lapse factor is:

$$A_{\rm GR}(x)
=
\frac14
\left(
3\sqrt{1-u}
-
\sqrt{1-ux^2}
\right)^2.
$$

At the boundary:

$$x=1,$$

both should match the exterior Schwarzschild value:

$$A_{\rm boundary}=1-u.$$

The script confirmed:

$$A_{\rm red}(1)=A_{\rm GR}(1)=1-u.$$

---

## Boundary Derivative Comparison

The reduced derivative is:

$$\frac{dA_{\rm red}}{dx}=ux.$$

At the boundary:

$$\frac{dA_{\rm red}}{dx}\bigg|_{x=1}=u.$$

The GR derivative also gives:

$$\frac{dA_{\rm GR}}{dx}\bigg|_{x=1}=u.$$

Thus both \(A\) and \(A'\) match at the boundary.

This is important because the reduced flux model is consistent with the exterior matching behavior.

---

## Weak-Field Compactness Series

The reduced interior expression is:

$$A_{\rm red}=1+\frac{u}{2}(x^2-3).$$

The GR interior expression expands as:

$$A_{\rm GR}
=
1+\frac{u}{2}(x^2-3)
+
\frac{u^2}{16}
\left[
2x^4+(x^2-3)^2-6
\right]
+\cdots.
$$

Therefore:

$$A_{\rm GR}-A_{\rm red}
=
\frac{3u^2}{16}(x^4-2x^2+1)+O(u^3).
$$

Since:

$$x^4-2x^2+1=(1-x^2)^2,$$

the leading residual is:

$$A_{\rm GR}-A_{\rm red}
=
\frac{3u^2}{16}(1-x^2)^2+O(u^3).
$$

Thus the models agree through first order in compactness but differ at second order inside the source.

At the boundary \(x=1\), this residual vanishes.

---

## Center Lapse Comparison

At the center:

$$x=0.$$

The reduced model gives:

$$A_{\rm red}(0)=1-\frac{3u}{2}.$$

The GR interior gives:

$$A_{\rm GR}(0)
=
\frac14(3\sqrt{1-u}-1)^2.
$$

Expanding:

$$A_{\rm GR}(0)
=
1-\frac{3u}{2}
+
\frac{3u^2}{16}
+
\frac{3u^3}{32}
+\cdots.
$$

The center difference is:

$$A_{\rm GR}(0)-A_{\rm red}(0)
=
\frac{3u^2}{16}
+
\frac{3u^3}{32}
+\cdots.
$$

So the center values agree at first order but differ beyond first order.

This is consistent with the reduced model reproducing Newtonian weak-field behavior but not the full relativistic interior.

---

## Radial Metric Comparison

If the reduced model forces:

$$\kappa=0$$

inside, then:

$$AB=1.$$

So:

$$B_{\rm red}=\frac1{A_{\rm red}}.$$

The GR constant-density interior radial metric is:

$$B_{\rm GR}=\frac1{1-ux^2}.$$

These are not equal generically.

The script confirmed that \(B_{\rm red}\) and \(B_{\rm GR}\) differ already at first order for generic interior radius.

This is the strongest structural clue in the comparison.

It says:

```text
Forcing reciprocal scaling inside matter is probably not correct.
```

---

## GR Interior Kappa Diagnostic

Define the reduced diagnostic:

$$\kappa=\frac12\ln(AB).$$

For the GR interior Schwarzschild solution:

$$A_{\rm GR}B_{\rm GR}\neq1$$

generically inside the source.

But at the boundary:

$$A_{\rm GR}B_{\rm GR}\big|_{x=1}=1.$$

Thus:

$$\kappa_{\rm GR}\neq0$$

inside matter, but:

$$\kappa_{\rm GR}=0$$

at the exterior boundary.

This supports the interior/exterior interpretation:

```text
kappa=0 is natural in the source-free exterior;
inside matter, traceful response can appear.
```

---

## What This Study Established

This study established:

1. \(A_{\rm red}\) and \(A_{\rm GR}\) match at the surface.
2. Their derivatives match at the surface.
3. \(A_{\rm red}\) and \(A_{\rm GR}\) agree through first weak-field order.
4. They differ at second order inside matter.
5. The leading residual is proportional to:
   $$u^2(1-x^2)^2.$$
6. The reduced model center lapse differs from GR beyond first order.
7. If \(\kappa=0\) is forced inside, then:
   $$B_{\rm red}=1/A_{\rm red}.$$
8. GR interior has:
   $$B_{\rm GR}=1/(1-ux^2).$$
9. GR interior generally has:
   $$A_{\rm GR}B_{\rm GR}\neq1.$$
10. At the boundary, GR recovers:
   $$A_{\rm GR}B_{\rm GR}=1.$$

---

## What This Study Did Not Establish

This study did not derive the GR interior solution.

It did not prove the reduced model must match GR interior exactly.

It did not identify the full source terms responsible for the residual.

It did not include pressure or stress in the reduced model.

It did not solve for an interior \(\kappa\)-field dynamically.

It did not derive a relativistic matter coupling.

It only located where the reduced constant-density interior differs from the GR interior Schwarzschild solution.

---

## Interpretation of the Residual

The difference between the reduced interior and the GR interior begins at second order in compactness:

$$A_{\rm GR}-A_{\rm red}
=
\frac{3u^2}{16}(1-x^2)^2+O(u^3).
$$

The shape:

$$ (1-x^2)^2 $$

vanishes at the boundary and is largest at the center.

This resembles an interior self-field, pressure, or trace-response correction rather than an exterior mass-flux correction.

The comparison suggests that the missing physics likely lives inside matter and does not affect the exterior Schwarzschild matching.

Possible interpretations:

```text
pressure/stress source terms;
interior kappa response;
nonlinear matter self-coupling;
boundary/interface relaxation;
relativistic correction to A sourcing.
```

---

## Relationship to Interior Kappa Response

The interior \(\kappa\)-response study showed that nonzero interior \(\kappa\) can vanish at the boundary and therefore coexist with exterior \(\kappa=0\).

The GR interior comparison makes this more plausible.

GR itself has an effective nonzero interior \(\kappa\) diagnostic:

$$\kappa_{\rm GR}
=
\frac12\ln(A_{\rm GR}B_{\rm GR}),
$$

while still matching to exterior reciprocal scaling at the boundary.

Therefore:

```text
interior kappa response is not an arbitrary complication;
it may be the missing channel required for relativistic interior behavior.
```

---

## Current Best Interpretation

The current best interpretation is:

```text
The reduced areal-flux model correctly captures exterior mass flux and
first-order interior Newtonian behavior.

It does not capture full relativistic interior structure.

The missing structure probably involves pressure/stress and/or nonzero
interior kappa.

Exterior kappa suppression remains viable because GR itself restores AB=1
at the exterior boundary.
```

This is a strong refinement of the reduced program.

It prevents overclaiming and identifies where the next source-model work belongs.

---

## Next Development Targets

### 1. Interior Kappa Residual Model

A possible script:

```text
candidate_gr_residual_as_kappa_response.py
```

Purpose:

```text
Ask whether the GR interior AB deviation can be modeled as an interior
kappa profile that vanishes at the boundary.
```

### 2. Pressure / Stress Source Extension

A possible note:

```text
candidate_pressure_stress_source_extension.md
```

Purpose:

```text
Identify how pressure and stress might source interior kappa or modify A flux.
```

### 3. Boundary Kappa Relaxation

A possible script:

```text
candidate_boundary_kappa_relaxation_layer.py
```

Purpose:

```text
Model transition from traceful interior response to compensated exterior.
```

---

## Summary

The reduced constant-density interior \(A\)-model agrees with the GR interior Schwarzschild lapse at the boundary and through first weak-field order.

It differs at second order inside matter.

The major structural difference is that the reduced model, if forced to \(\kappa=0\) inside, has:

$$B=1/A.$$

The GR interior does not generally satisfy:

$$AB=1$$

inside matter.

However, GR restores:

$$AB=1$$

at the exterior boundary.

Therefore the comparison supports the interpretation that \(\kappa=0\) is an exterior/source-free condition, while matter interiors may carry traceful \(\kappa\)-response.

The next target is to identify whether the GR interior residual corresponds to pressure, stress, interior \(\kappa\), or some combination.
