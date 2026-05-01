# Candidate GR Residual as Kappa Response

## What This Document Is

This document is a diagnostic development note.

It is not a derivation of general relativity, not a proof of the reduced theory, and not a formal commitment that the reduced theory must exactly reproduce the GR interior Schwarzschild solution.

Its purpose is to summarize the result of:

```text
candidate_gr_residual_as_kappa_response.py
```

The guiding question was:

```text
Can the difference between the reduced interior model and the GR interior
Schwarzschild solution be interpreted as an effective interior kappa response?
```

The answer is yes, in a useful diagnostic sense.

The GR interior Schwarzschild solution has:

$$A_{\rm GR}B_{\rm GR}\neq1$$

inside matter, while:

$$A_{\rm GR}B_{\rm GR}=1$$

at the exterior boundary.

Therefore the diagnostic:

$$\kappa_{\rm GR}=\frac12\ln(A_{\rm GR}B_{\rm GR})$$

is generally nonzero inside matter, but returns to zero at the boundary.

This strongly supports the current interpretation:

```text
kappa=0 is safest as a source-free exterior compensation condition,
not an everywhere-inside-matter condition.
```

---

## Dimensionless Setup

Use:

$$x=\frac{r}{R},$$

where \(R\) is the source radius, and:

$$u=\frac{r_s}{R}=\frac{2GM}{c^2R},$$

where \(u\) is the compactness.

The GR interior Schwarzschild temporal factor is:

$$A_{\rm GR}
=
\frac14
\left(
3\sqrt{1-u}
-
\sqrt{1-ux^2}
\right)^2.
$$

The GR interior radial factor is:

$$B_{\rm GR}
=
\frac1{1-ux^2}.
$$

The diagnostic product is:

$$A_{\rm GR}B_{\rm GR}.$$

Define:

$$\kappa_{\rm GR}
=
\frac12\ln(A_{\rm GR}B_{\rm GR}).
$$

This is not claiming that GR literally uses the reduced model’s \(\kappa\) field. It is a diagnostic projection into the reduced variables.

---

## Boundary Behavior

At the boundary:

$$x=1.$$

The script found:

$$A_{\rm GR}B_{\rm GR}\big|_{x=1}=1.$$

Therefore:

$$\kappa_{\rm GR}(1)=0.$$

This means GR restores reciprocal exterior scaling at the boundary.

However, the derivative is generally nonzero:

$$\kappa_{\rm GR}'(1)\neq0.$$

The script found:

$$\kappa_{\rm GR}'(1)
=
-\frac{3u}{2u-2}.
$$

This suggests that while the value of \(\kappa\) returns to zero at the boundary, the derivative can carry interface or matter-structure information.

Interpretation:

```text
GR-like interior behavior can have nonzero interior kappa while still
matching to exterior kappa=0.
```

---

## Weak-Field Kappa Shape

The script expanded \(A_{\rm GR}B_{\rm GR}\) and \(\kappa_{\rm GR}\) in compactness \(u\).

The leading weak-field shape is:

$$\kappa_{\rm GR}
=
\frac{3u}{4}(x^2-1)+O(u^2).
$$

This is nonzero inside the source for \(0\le x<1\), and vanishes at the surface:

$$\kappa_{\rm GR}(1)=0.$$

At the center:

$$x=0,$$

the leading value is:

$$\kappa_{\rm GR}(0)
=
-\frac{3u}{4}+O(u^2).
$$

This is regular and finite.

Thus the leading diagnostic interior \(\kappa\)-profile is simple:

```text
negative at the center,
monotonic toward zero,
zero at the boundary.
```

The script also showed that a toy profile proportional to:

$$1-x^2$$

captures the leading behavior exactly:

$$\kappa_{\rm GR}^{(1)}
=
-\frac{3u}{4}(1-x^2).
$$

This is useful because it gives a compact toy model for interior trace response.

---

## Center Behavior

At the center:

$$x=0,$$

the exact diagnostic is:

$$\kappa_{\rm GR}(0)
=
\frac12\ln\left(\frac{(3\sqrt{1-u}-1)^2}{4}\right).
$$

The script found:

$$\kappa_{\rm GR}'(0)=0.$$

So the diagnostic profile is regular at the center.

Its compactness expansion begins:

$$\kappa_{\rm GR}(0)
=
-\frac{3u}{4}
-\frac{15u^2}{32}
-\frac{3u^3}{8}
+\cdots.
$$

This again supports interpreting the interior deviation as a regular matter-supported response rather than an exterior pathology.

---

## A-Lapse Residual

The reduced constant-density interior \(A\)-model is:

$$A_{\rm red}
=
1-\frac{3u}{2}
+
\frac{ux^2}{2}.
$$

The GR interior lapse is:

$$A_{\rm GR}
=
\frac14
\left(
3\sqrt{1-u}
-
\sqrt{1-ux^2}
\right)^2.
$$

The residual is:

$$A_{\rm GR}-A_{\rm red}.$$

The leading residual is:

$$A_{\rm GR}-A_{\rm red}
=
\frac{3u^2}{16}(1-x^2)^2+O(u^3).
$$

The script found:

$$A_{\rm GR}-A_{\rm red}=0$$

at the boundary, and:

$$\frac{d}{dx}(A_{\rm GR}-A_{\rm red})=0$$

at the boundary.

Thus the \(A\)-lapse residual is interior-supported and boundary-smooth.

Interpretation:

```text
The missing relativistic interior physics does not disturb the exterior
mass-flux matching at the boundary.
```

This supports the idea that the exterior law can remain exact while the interior gets additional trace/stress corrections.

---

## Toy Effective Kappa Fit

The leading \(\kappa_{\rm GR}\) shape is:

$$\kappa_{\rm GR}^{(1)}
=
\frac{3u}{4}(x^2-1).
$$

The script fit it to a simple toy form:

$$\kappa_{\rm toy}=\eta u(1-x^2).$$

Matching at the center gives:

$$\eta=-\frac34.$$

Therefore:

$$\kappa_{\rm toy}
=
-\frac{3u}{4}(1-x^2)
=
\frac{3u}{4}(x^2-1).
$$

This exactly matches the leading GR diagnostic profile.

This gives a compact candidate shape for future interior \(\kappa\)-response models.

---

## What This Study Established

This study established:

1. GR interior Schwarzschild has:
   $$A_{\rm GR}B_{\rm GR}\neq1$$
   inside matter.

2. Therefore:
   $$\kappa_{\rm GR}\neq0$$
   inside matter.

3. At the boundary:
   $$A_{\rm GR}B_{\rm GR}=1.$$

4. Therefore:
   $$\kappa_{\rm GR}(1)=0.$$

5. The boundary derivative:
   $$\kappa_{\rm GR}'(1)$$
   is generally nonzero.

6. The leading weak-field shape is:
   $$\kappa_{\rm GR}=\frac{3u}{4}(x^2-1)+O(u^2).$$

7. The leading shape is regular at the center and vanishes at the boundary.

8. The \(A\)-lapse residual is interior-supported and boundary-smooth.

9. A simple toy \((1-x^2)\) profile captures the leading \(\kappa\)-response.

---

## What This Study Did Not Establish

This study did not derive the GR interior Schwarzschild solution.

It did not prove the reduced theory must reproduce GR interiors exactly.

It did not derive a dynamical \(\kappa\) equation.

It did not include pressure or stress explicitly in the reduced model.

It did not determine the true physical source of \(\kappa\).

It only showed that the GR interior residual is naturally expressible as a nonzero interior \(\kappa\)-diagnostic that vanishes at the boundary.

---

## Interpretation

The result strongly supports the current interior/exterior split:

```text
Exterior source-free vacuum:
  kappa = 0

Interior matter:
  kappa may be nonzero

Boundary/interface:
  kappa returns to zero so exterior compensation is restored
```

This gives a clean way to preserve the exact exterior Schwarzschild recovery while allowing richer interior structure.

The theory should no longer assume:

```text
kappa=0 everywhere.
```

The safer statement is:

```text
kappa=0 in the relaxed source-free exterior.
```

---

## Relationship to Boundary Kappa Relaxation

The boundary relaxation study tests whether nonzero interior \(\kappa\) can smoothly vanish at the boundary.

The GR diagnostic supports that target because:

$$\kappa_{\rm GR}(1)=0.$$

But since:

$$\kappa_{\rm GR}'(1)\neq0,$$

there may still be boundary/interface derivative information.

A future model must decide whether:

```text
the derivative jump is physical,
a boundary layer smooths it,
or pressure/stress terms carry it.
```

---

## Summary

The GR residual-as-\(\kappa\) diagnostic passed.

The GR interior Schwarzschild solution has an effective reduced diagnostic:

$$\kappa_{\rm GR}=\frac12\ln(A_{\rm GR}B_{\rm GR}).$$

This is generally nonzero inside matter, but returns to zero at the surface.

The leading weak-field shape is:

$$\kappa_{\rm GR}
=
-\frac{3u}{4}(1-x^2).
$$

This supports the current picture:

```text
A-flux carries the exterior mass field.
Kappa may carry traceful interior response.
The boundary/interface restores compensated exterior geometry.
```
