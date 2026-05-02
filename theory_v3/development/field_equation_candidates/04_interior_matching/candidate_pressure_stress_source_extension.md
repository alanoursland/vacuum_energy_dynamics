# Candidate Pressure / Stress Source Extension

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or complete matter-coupling law. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_pressure_stress_source_extension.py
```

The guiding question was:

```text
Should pressure and stress source A-flux directly, source interior kappa,
or appear as boundary-smooth second-order corrections?
```

The current answer is:

```text
Pressure/stress most likely belongs to the interior problem, not the ordinary
exterior mass-flux law.
```

The cleanest current hypothesis is:

```text
density / total mass fixes exterior A-flux;
pressure and stress source interior kappa and/or boundary-smooth second-order
A corrections;
source-free exterior suppresses kappa and conserves A-flux.
```

---

## Background

The current reduced exterior law is:

$$F_A(r)=4\pi r^2A'(r),$$

with:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

Outside the source:

$$M_{\rm enc}(r)=M,$$

so:

$$F_A=\frac{8\pi GM}{c^2}.$$

This gives:

$$A=1-\frac{2GM}{rc^2}.$$

With exterior compensation:

$$\kappa=0,$$

we have:

$$B=\frac1A.$$

This recovers the exact Schwarzschild exterior metric factors in the reduced static spherical sector.

However, comparison with the GR interior Schwarzschild solution showed that the reduced density-only interior is incomplete at second order inside matter.

The missing structure is likely related to:

```text
pressure,
stress,
interior kappa,
or nonlinear interior self-field corrections.
```

---

## GR Constant-Density Pressure Profile

For the GR constant-density interior, use:

$$x=\frac{r}{R},$$

and:

$$u=\frac{r_s}{R}=\frac{2GM}{c^2R}.$$

The dimensionless pressure profile is:

$$
\frac{p}{\rho c^2}
=
\frac{\sqrt{1-ux^2}-\sqrt{1-u}}
{3\sqrt{1-u}-\sqrt{1-ux^2}}.
$$

The script expanded this as:

$$
\frac{p}{\rho c^2}
=
\frac{u}{4}(1-x^2)
+
\frac{u^2}{4}(1-x^2)
+
O(u^3)
$$

in the displayed series form:

$$
\frac{p}{\rho c^2}
=
\frac{u(-ux^2+u-x^2+1)}{4}
+
O(u^3).
$$

The leading shape is:

$$
\frac{p}{\rho c^2}
\approx
\frac{u}{4}(1-x^2).
$$

This begins at order \(u\) and vanishes at the boundary:

$$p(R)=0.$$

That boundary behavior is important because it allows pressure corrections to be interior-contained.

---

## A Residual Versus Pressure-Like Shape

The reduced interior \(A\)-model is:

$$A_{\rm red}=1-\frac{3u}{2}+\frac{ux^2}{2}.$$

The GR interior Schwarzschild lapse is:

$$
A_{\rm GR}
=
\frac14
\left(
3\sqrt{1-u}
-
\sqrt{1-ux^2}
\right)^2.
$$

The leading residual is:

$$
A_{\rm GR}-A_{\rm red}
=
\frac{3u^2}{16}(x^4-2x^2+1)
+
O(u^3).
$$

Since:

$$x^4-2x^2+1=(1-x^2)^2,$$

this is:

$$
A_{\rm GR}-A_{\rm red}
=
\frac{3u^2}{16}(1-x^2)^2
+
O(u^3).
$$

The leading pressure shape is:

$$
P_{\rm lead}
=
\frac{u}{4}(1-x^2).
$$

Then:

$$
3P_{\rm lead}^2
=
\frac{3u^2}{16}(1-x^2)^2.
$$

So:

$$
A_{\rm GR}-A_{\rm red}
=
3P_{\rm lead}^2
+
O(u^3).
$$

The script confirmed this exact leading-shape match.

Interpretation:

```text
The missing A-lapse structure is second-order, interior-supported, and
pressure/self-field-like.
```

This does not prove pressure is the source, but it strongly suggests that the missing correction belongs to the interior relativistic matter problem.

---

## Hypothesis H1: Pressure as Direct A-Flux Source

The first hypothesis tested was:

$$
\Delta_{\rm areal}A
=
\frac{8\pi G}{c^2}
\left(
\rho+\chi\frac{p}{c^2}
\right).
$$

This would mean pressure directly changes the \(A\)-flux source.

Consequences:

```text
pressure contributes to A-flux;
the exterior flux may depend on integrated pressure as well as mass;
if pressure vanishes at the boundary, exterior matching can still be boundary-clean;
but total exterior mass normalization may need reinterpretation.
```

This hypothesis is possible, but dangerous: if pressure contributes directly to exterior flux, the theory must explain how this relates to observed gravitational mass.

---

## Hypothesis H2: Pressure / Stress as Kappa Source

The second hypothesis was that pressure and stress source interior \(\kappa\).

Use a toy trace-like source:

$$J_\kappa=a\rho c^2+bp.$$

With local energy:

$$E=C_\kappa\kappa^2-J_\kappa\kappa,$$

stationarity gives:

$$2C_\kappa\kappa-J_\kappa=0.$$

Therefore:

$$
\kappa_{\rm eq}
=
\frac{a\rho c^2+bp}{2C_\kappa}.
$$

If the source vanishes in the exterior, then exterior \(\kappa\) relaxes to zero.

This fits the current interior/exterior interpretation:

```text
pressure/stress may excite traceful kappa inside matter;
source-free exterior suppresses kappa.
```

---

## Boundary Preservation Conditions

The script compared three leading interior shapes.

Pressure leading shape:

$$
P_{\rm lead}
=
\frac{u}{4}(1-x^2).
$$

Kappa diagnostic leading shape from the GR interior comparison:

$$
\kappa_{\rm lead}
=
-\frac{3u}{4}(1-x^2).
$$

A residual leading shape:

$$
\Delta A_{\rm lead}
=
\frac{3u^2}{16}(1-x^2)^2.
$$

At the boundary \(x=1\):

$$P_{\rm lead}=0,$$

$$\kappa_{\rm lead}=0,$$

and:

$$\Delta A_{\rm lead}=0.$$

Also:

$$\frac{d}{dx}\Delta A_{\rm lead}\bigg|_{x=1}=0.$$

Thus these corrections are boundary-contained.

Interpretation:

```text
Interior pressure/stress corrections can vanish smoothly at the boundary,
letting the exterior A-flux law and exterior kappa=0 remain intact.
```

---

## Source-Channel Classification

The current best channel map is:

### 1. Density / Total Mass to A-Flux

Density determines enclosed mass:

$$M_{\rm enc}(r)=\int_0^r4\pi \bar r^2\rho(\bar r)d\bar r.$$

Then:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

This controls the exterior mass field.

### 2. Pressure / Stress to Interior Kappa

Pressure and stress may source:

$$\kappa_{\rm interior}\neq0.$$

This carries traceful matter response and should vanish or relax at the boundary.

### 3. Pressure / Self-Field to Second-Order A Residual

The GR interior lapse residual begins at order \(u^2\) and has a pressure-squared-like boundary shape:

$$\frac{3u^2}{16}(1-x^2)^2.$$

This suggests second-order interior corrections to \(A\), not changes to the exterior flux law.

### 4. Source-Free Exterior

Outside matter:

$$\kappa\to0,$$

$$F_A=\text{constant},$$

and:

$$B=\frac1A.$$

---

## What This Study Established

This study established:

1. GR interior pressure begins at order \(u\).
2. The leading pressure profile vanishes at the surface.
3. The GR \(A\)-residual relative to the reduced model begins at order \(u^2\).
4. The leading \(A\)-residual shape is:
   $$\frac{3u^2}{16}(1-x^2)^2.$$
5. This is exactly:
   $$3P_{\rm lead}^2.$$
6. Pressure can be formulated as a direct \(A\)-flux source.
7. Pressure/stress can be formulated as an interior \(\kappa\)-source.
8. Boundary behavior favors interior-contained corrections.
9. The cleanest current channel map keeps exterior mass flux separate from pressure/stress interior response.

---

## What This Study Did Not Establish

This study did not derive a pressure/stress source law.

It did not prove pressure sources \(\kappa\).

It did not prove pressure modifies \(A\)-flux.

It did not derive the TOV equation.

It did not produce a full relativistic matter coupling.

It did not prove equivalence to the GR interior Schwarzschild solution.

It only identified plausible pressure/stress channels and their boundary behavior.

---

## Current Best Interpretation

The current best interpretation is:

```text
Density / total mass fixes exterior A-flux.

Pressure and stress likely belong to the interior correction problem.

Those corrections may source kappa and/or produce boundary-smooth second-order
A-lapse residuals.

The source-free exterior remains compensated:
  kappa=0,
  F_A=constant,
  B=1/A.
```

This preserves the exact exterior branch while opening a path toward richer matter interiors.

---

## Next Development Targets

### 1. Pressure-to-Kappa Source Model

A possible script:

```text
candidate_pressure_kappa_source_model.py
```

Purpose:

```text
Build a reduced field equation where pressure/stress sources interior kappa
and test whether it reproduces the leading GR kappa diagnostic.
```

### 2. A Residual Source Reconstruction

A possible script:

```text
candidate_A_residual_source_reconstruction.py
```

Purpose:

```text
Compute what effective source would produce the GR A residual under the
areal-flux operator.
```

### 3. Pressure / Boundary Matching

A possible script:

```text
candidate_pressure_boundary_matching.py
```

Purpose:

```text
Test whether pressure corrections vanish smoothly enough to preserve exterior
Schwarzschild matching.
```

---

## Summary

The pressure/stress extension study suggests that the exterior source law should remain mass-flux based:

$$F_A=\frac{8\pi GM}{c^2}.$$

Pressure/stress appears to be an interior correction channel.

The leading GR pressure shape is:

$$\frac{p}{\rho c^2}\approx\frac{u}{4}(1-x^2).$$

The leading GR \(A\)-residual is:

$$A_{\rm GR}-A_{\rm red}
=
\frac{3u^2}{16}(1-x^2)^2.
$$

This equals three times the square of the leading pressure shape.

Thus the missing interior structure is naturally pressure/self-field-like and boundary-contained.

The next target is to determine whether pressure/stress sources \(\kappa\), \(A\), or both.
