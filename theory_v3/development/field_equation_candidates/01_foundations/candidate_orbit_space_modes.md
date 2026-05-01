# Candidate Orbit-Space Modes

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full covariant field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_orbit_space_modes.py
```

The guiding question was:

```text
Can the reduced areal-gauge modes kappa and s be expressed in a more geometric
spherical-reduction language, rather than only as raw metric coefficients A and B?
```

The answer is yes, in a qualified way.

The reduced variables can be rewritten using the two-dimensional orbit-space metric and the areal-radius scalar.

The key result is:

$$\kappa
=
\frac12\ln\left(\frac{A}{|\nabla R|^2}\right),$$

and:

$$s
=
\frac12\ln\left(A|\nabla R|^2\right).$$

The compensation condition:

$$\kappa=0$$

then becomes:

$$A=|\nabla R|^2.$$

In areal gauge:

$$|\nabla R|^2=\frac1B,$$

so this reduces to:

$$AB=1.$$

This is a significant improvement over the raw areal-gauge expression, because it shows how the reduced condition is tied to the orbit-space geometry and the areal-radius scalar.

It still does not make \(\kappa\) or \(s\) full spacetime scalar fields.

---

## Background

The reduced exterior program originally used the static spherical areal-gauge metric:

$$ds^2=-A(r)c^2dt^2+B(r)dr^2+r^2d\Omega^2.$$

The log-scale variables were:

$$a=\ln A,$$

and:

$$b=\ln B.$$

Then:

$$\kappa=\frac{a+b}{2},$$

and:

$$s=\frac{a-b}{2}.$$

Equivalently:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Multiplying gives:

$$AB=e^{2\kappa}.$$

Thus, in areal gauge:

$$\kappa=0
\quad\Longleftrightarrow\quad
AB=1.$$

This was useful, but gauge-dependent. A later gauge study showed that under radial reparameterization:

$$r=f(R),$$

the naive reduced modes shift as:

$$\kappa\rightarrow\kappa+\ln f'(R),$$

and:

$$s\rightarrow s-\ln f'(R).$$

Therefore \(\kappa\) and \(s\) are not raw coordinate-invariant scalar fields.

The areal-gauge study repaired this by defining areal radius geometrically from sphere area. The orbit-space study goes one step further.

---

## Spherical Orbit-Space Decomposition

A general spherically symmetric geometry can be written as:

$$ds^2=h_{AB}(x)dx^A dx^B+R(x)^2d\Omega^2.$$

Here:

- \(h_{AB}\) is the two-dimensional orbit-space metric.
- \(x^A\) are coordinates on the orbit space.
- \(R(x)\) is the areal-radius scalar.
- The area of a symmetry sphere is:

$$\text{Area}=4\pi R(x)^2.$$

This separates the two-dimensional temporal-radial geometry from the angular sphere geometry.

This is more geometric than choosing a raw radial coordinate.

The reduced variables \(\kappa\) and \(s\) should be understood as shadows of structures in \(h_{AB}\) together with \(R(x)\).

---

## Static Diagonal Reduction

In static diagonal form with arbitrary radial coordinate \(X\), write:

$$ds^2=-T(X)c^2dt^2+Q(X)dX^2+S(X)^2d\Omega^2.$$

The orbit-space metric is:

$$h_{AB}dx^A dx^B=-T(X)c^2dt^2+Q(X)dX^2.$$

The areal-radius scalar is:

$$R(X)=S(X).$$

Areal gauge is obtained by using:

$$R=S(X)$$

as the radial coordinate.

Since:

$$dR=S'(X)dX,$$

we have:

$$dX=\frac{dR}{S'(X)}.$$

Thus the radial coefficient in areal gauge is:

$$B_{\rm areal}=\frac{Q(X)}{[S'(X)]^2}.$$

The temporal coefficient is:

$$A_{\rm areal}=T(X).$$

Therefore:

$$\kappa_{\rm areal}
=
\frac12\ln(A_{\rm areal}B_{\rm areal})
=
\frac12\ln\left(\frac{T(X)Q(X)}{[S'(X)]^2}\right).$$

Similarly:

$$s_{\rm areal}
=
\frac12\ln\left(\frac{A_{\rm areal}}{B_{\rm areal}}\right)
=
\frac12\ln\left(\frac{T(X)[S'(X)]^2}{Q(X)}\right).$$

This recovers the earlier areal-gauge result, but now framed through the orbit-space metric and areal-radius scalar.

---

## Orbit-Space Determinant Interpretation

The orbit-space metric in the static diagonal arbitrary coordinate \(X\) has determinant:

$$\det(h)=-c^2T(X)Q(X).$$

After transforming to areal radius \(R=S(X)\), the orbit-space determinant becomes:

$$\det(h_{\rm areal})
=
-\frac{c^2T(X)Q(X)}{[S'(X)]^2}.$$

Its magnitude is:

$$|\det(h_{\rm areal})|
=
\frac{c^2T(X)Q(X)}{[S'(X)]^2}.$$

Removing the constant factor \(c^2\), we get:

$$\frac{|\det(h_{\rm areal})|}{c^2}
=
\frac{T(X)Q(X)}{[S'(X)]^2}.$$

Therefore:

$$\kappa_{\rm areal}
=
\frac12\ln\left(\frac{|\det(h_{\rm areal})|}{c^2}\right).$$

This means that in static spherical areal gauge, \(\kappa\) is the half-log orbit-space determinant factor.

In interpretation:

```text
kappa is a reduced orbit-space volume / determinant diagnostic.
```

This is not a four-dimensional scalar field. It is a spherical-reduction quantity derived from the two-dimensional temporal-radial geometry.

---

## Areal-Radius Gradient Norm

The orbit-space norm of the areal-radius gradient is:

$$|\nabla R|^2
=
h^{AB}\partial_A R\partial_B R.$$

In the static diagonal metric:

$$R(X)=S(X).$$

Since \(R\) depends only on \(X\),

$$\partial_X R=S'(X).$$

The inverse radial component is:

$$h^{XX}=\frac1{Q(X)}.$$

Thus:

$$|\nabla R|^2=\frac{[S'(X)]^2}{Q(X)}.$$

But:

$$B_{\rm areal}=\frac{Q(X)}{[S'(X)]^2}.$$

So:

$$|\nabla R|^2=\frac1{B_{\rm areal}}.$$

This lets us rewrite \(\kappa\) and \(s\) without raw \(B\).

Since:

$$A_{\rm areal}=T(X),$$

we have:

$$\kappa
=
\frac12\ln(A_{\rm areal}B_{\rm areal})
=
\frac12\ln\left(\frac{A}{|\nabla R|^2}\right).$$

Also:

$$s
=
\frac12\ln\left(\frac{A_{\rm areal}}{B_{\rm areal}}\right)
=
\frac12\ln\left(A|\nabla R|^2\right).$$

These are the key orbit-space expressions.

---

## Compensation Condition in Orbit-Space Form

The reduced compensation condition is:

$$\kappa=0.$$

Using:

$$\kappa
=
\frac12\ln\left(\frac{A}{|\nabla R|^2}\right),$$

we get:

$$\frac{A}{|\nabla R|^2}=1.$$

Therefore:

$$A=|\nabla R|^2.$$

This may be the cleanest spherical-reduction statement of exterior compensation.

In arbitrary radial coordinate \(X\), this is:

$$T(X)=\frac{[S'(X)]^2}{Q(X)}.$$

Equivalently:

$$T(X)Q(X)=[S'(X)]^2.$$

In areal gauge, \(R=r\), so:

$$|\nabla R|^2=\frac1B.$$

Then:

$$A=|\nabla R|^2$$

becomes:

$$A=\frac1B.$$

Thus:

$$AB=1.$$

So the old areal-gauge relation is recovered as a special case.

---

## Schwarzschild Exterior Check

For the Schwarzschild exterior in areal coordinates:

$$A=1-\frac{2GM}{rc^2},$$

and:

$$B=\frac1A.$$

Thus:

$$AB=1.$$

So:

$$\kappa=0.$$

Also, in areal gauge:

$$|\nabla R|^2=\frac1B.$$

Since:

$$B=\frac1A,$$

we have:

$$|\nabla R|^2=A.$$

Therefore Schwarzschild satisfies the orbit-space compensation condition:

$$A=|\nabla R|^2.$$

This is important because it is not merely a weak-field statement. It matches the exact Schwarzschild exterior reciprocal relation in areal coordinates.

This does not prove the full theory, but it shows that the reduced compensation condition is aligned with the exact static spherical GR exterior.

---

## Failure Control: Ignoring the Areal Scalar

The script also checked a failure mode.

Start with an areal-gauge metric satisfying:

$$AB=1.$$

Now make a radial reparameterization:

$$r=f(X).$$

Then:

$$T(X)=A(f(X)),$$

$$Q(X)=B(f(X))[f'(X)]^2,$$

and:

$$S(X)=f(X).$$

The naive product is:

$$T(X)Q(X)
=
A(f(X))B(f(X))[f'(X)]^2.$$

Since:

$$A(f(X))B(f(X))=1,$$

the naive product becomes:

$$T(X)Q(X)=[f'(X)]^2.$$

If one ignores the angular sector, this falsely looks like reciprocal compensation failed.

But the areal scalar is:

$$S(X)=f(X),$$

so:

$$S'(X)=f'(X).$$

The corrected expression is:

$$\frac{T(X)Q(X)}{[S'(X)]^2}
=
A(f(X))B(f(X)).
$$

Thus the radial Jacobian cancels.

This confirms that the areal-radius scalar is essential for a gauge-aware formulation.

---

## What This Study Established

This study established:

1. Spherical symmetry admits a two-dimensional orbit-space metric \(h_{AB}\) plus an areal-radius scalar \(R(x)\).
2. The static diagonal metric is a special case of this orbit-space decomposition.
3. The areal-gauge radial coefficient is:
   $$B_{\rm areal}=Q/[S']^2.$$
4. The areal-gauge imbalance mode is:
   $$\kappa=\frac12\ln(TQ/[S']^2).$$
5. The areal-gauge shear mode is:
   $$s=\frac12\ln(T[S']^2/Q).$$
6. The areal-radius gradient norm satisfies:
   $$|\nabla R|^2=[S']^2/Q=1/B_{\rm areal}.$$
7. Therefore:
   $$\kappa=\frac12\ln(A/|\nabla R|^2).$$
8. And:
   $$s=\frac12\ln(A|\nabla R|^2).$$
9. Compensation becomes:
   $$A=|\nabla R|^2.$$
10. In areal gauge, this reduces to:
   $$AB=1.$$
11. Schwarzschild exterior satisfies this condition exactly.
12. Including \(R(x)\) removes the radial-coordinate Jacobian artifact.

---

## What This Study Did Not Establish

This study did not produce a full covariant field equation.

It did not show how to define \(A\) in arbitrary dynamical spacetime without a static time direction or observer normalization.

It did not generalize to nonspherical geometries.

It did not handle rotation.

It did not handle gravitational waves or general time dependence.

It did not prove that \(\kappa\) and \(s\) are fundamental fields.

It did not derive the reduced exterior action.

It only improved the geometric status of \(\kappa\) and \(s\) inside spherical reduction.

---

## Relationship to the Scalar-Theory Question

This study helps answer the concern:

```text
Are we accidentally building a scalar gravitation theory?
```

The answer remains:

```text
No, not necessarily.
```

The variables \(\kappa\) and \(s\) look scalar in static spherical reduction because symmetry has collapsed the geometry to radial mode amplitudes.

The orbit-space study shows that they are better interpreted as diagnostics built from:

```text
the two-dimensional orbit-space metric h_AB,
the areal-radius scalar R,
and the static temporal coefficient A.
```

In particular:

$$|\nabla R|^2=h^{AB}\partial_A R\partial_B R$$

is a geometric spherical-reduction object.

Thus \(\kappa\) and \(s\) are not arbitrary scalar gravitational fields. They are scalar amplitudes of reduced geometric structure.

A full theory may still need tensorial or covariant parent modes.

---

## Relationship to the Reduced Exterior Action

The reduced exterior action used:

$$L
=
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s.$$

This should now be understood as a reduced spherical action involving the orbit-space diagnostics:

$$\kappa=\frac12\ln(A/|\nabla R|^2),$$

and:

$$s=\frac12\ln(A|\nabla R|^2).$$

That is more geometrically meaningful than treating \(\kappa\) and \(s\) as arbitrary scalar fields.

A future action should probably be written directly in terms of \(h_{AB}\), \(R\), and matter/source data, with \(\kappa\) and \(s\) appearing only after reduction.

---

## Relationship to the Gauge Notes

The gauge-dependence notes showed that naive \(\kappa\) and \(s\) shift under radial reparameterization.

The areal-gauge condition note showed that:

$$\kappa_{\rm areal}
=
\frac12\ln(TQ/[S']^2).$$

This orbit-space note explains why:

$$[S']^2/Q$$

is not an arbitrary correction. It is:

$$|\nabla R|^2.$$

So the corrected expression is:

$$\kappa=\frac12\ln(A/|\nabla R|^2).$$

This is the gauge-aware spherical-reduction form.

---

## Current Best Interpretation

The best current interpretation is:

```text
kappa is the spherical-reduction imbalance between the static temporal coefficient
and the orbit-space norm of the areal-radius gradient.

s is the corresponding compensated shear-like combination.
```

More compactly:

$$\kappa=\frac12\ln\left(\frac{A}{|\nabla R|^2}\right),$$

and:

$$s=\frac12\ln\left(A|\nabla R|^2\right).$$

Exterior compensation is:

$$A=|\nabla R|^2.$$

This is stronger and cleaner than saying only:

$$AB=1.$$

The \(AB=1\) expression is the areal-gauge form of the orbit-space condition.

---

## Next Development Target

The next target is to decide how far this orbit-space formulation can be pushed.

Possible next artifacts:

```text
candidate_orbit_space_action.md
candidate_orbit_space_action.py
```

Purpose:

```text
Rewrite the reduced exterior action in terms of h_AB, R, A, and |∇R|²,
instead of treating kappa and s as independent scalar fields.
```

Another possible target:

```text
candidate_static_spherical_exact_recovery.md
```

Purpose:

```text
Study whether the condition A=|∇R|² plus an appropriate source law
can recover exact Schwarzschild exterior, not just weak-field behavior.
```

Another possible target:

```text
candidate_time_dependent_orbit_space_modes.md
```

Purpose:

```text
Explore what survives when the static assumption is relaxed.
```

The recommended next step is probably:

```text
candidate_static_spherical_exact_recovery.py
```

because the Schwarzschild check suggests the exact exterior may be closer than expected.

---

## Summary

The orbit-space mode study improves the reduced exterior program.

The raw areal-gauge formulas:

$$\kappa=\frac12\ln(AB),$$

and:

$$s=\frac12\ln(A/B)$$

can be rewritten using the two-dimensional orbit-space geometry and the areal-radius scalar:

$$|\nabla R|^2=h^{AB}\partial_A R\partial_B R.$$

In the static diagonal spherical sector:

$$\kappa=\frac12\ln\left(\frac{A}{|\nabla R|^2}\right),$$

and:

$$s=\frac12\ln\left(A|\nabla R|^2\right).$$

The compensation condition becomes:

$$\kappa=0
\quad\Longleftrightarrow\quad
A=|\nabla R|^2.$$

In areal gauge, this reduces to:

$$AB=1.$$

Schwarzschild exterior satisfies the condition exactly.

This does not make \(\kappa\) a full spacetime scalar field. It makes \(\kappa\) a gauge-aware spherical-reduction diagnostic built from orbit-space geometry and the areal-radius scalar.

That is the current best bridge from the reduced scalar-looking mode program toward a geometric parent structure.
