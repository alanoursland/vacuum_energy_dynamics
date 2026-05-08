# Candidate Areal-Gauge Kappa Condition

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full covariant field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_areal_gauge_kappa_condition.py
```

The guiding question was:

```text
Can areal-gauge kappa=0 be re-expressed as a gauge-invariant or
gauge-fixed condition derived from sphere area / radial foliation geometry?
```

The answer is qualified:

Not as an invariant scalar \(\kappa = 0\).

Yes as a gauge-fixed geometric construction: define the areal radius by sphere area, express the metric in areal gauge, then impose \(\kappa_{\rm areal} = \frac12\ln(AB) = 0\).

In arbitrary radial coordinate, the same condition becomes:

$$T(R)Q(R) = [S'(R)]^2.$$

This includes the angular-radius function \(S(R)\) and avoids the naive gauge artifact \(TQ \neq 1\) under radial reparameterization.

---

## Background

The gauge-dependence study showed that under a radial reparameterization \(r = f(R)\), naive reduced modes shift:

$$\kappa \rightarrow \kappa + \ln f'(R),$$

and:

$$s \rightarrow s - \ln f'(R).$$

This means the compensation condition \(\kappa = 0\) is gauge-dependent. After reparameterization, the naive product \(A_{\rm new}B_{\rm new} = [f'(R)]^2 \neq 1\).

The question addressed here is whether the areal radius, defined geometrically by sphere area, can repair this gauge dependence.

---

## General Spherical Metric in Arbitrary Radial Coordinate

A general static spherically symmetric metric in an arbitrary radial coordinate \(R\) is:

$$ds^2 = -T(R)c^2dt^2 + Q(R)dR^2 + S(R)^2 d\Omega^2.$$

Here:

- \(T(R)\) is the temporal coefficient.
- \(Q(R)\) is the radial coefficient.
- \(S(R)\) is the geometric sphere-radius function.

The area of a symmetry sphere at coordinate \(R\) is:

$$\text{Area}(R) = 4\pi S(R)^2.$$

The areal radius is defined as:

$$r_{\rm areal} = \sqrt{\frac{\text{Area}}{4\pi}} = S(R).$$

This is a geometric definition that does not depend on the choice of radial coordinate.

---

## Transform to Areal Radius

Define the areal radius as the radial coordinate:

$$r = S(R).$$

Then:

$$\frac{dr}{dR} = S'(R), \qquad \frac{dR}{dr} = \frac{1}{S'(R)}.$$

In areal gauge, the metric coefficients become:

$$A_{\rm areal} = T(R),$$

and:

$$B_{\rm areal} = \frac{Q(R)}{[S'(R)]^2}.$$

The angular sector is \(r^2 d\Omega^2\) by construction.

---

## Areal-Gauge Kappa from Arbitrary-Coordinate Metric

The naive \(\kappa\) in the arbitrary coordinate \(R\), incorrectly treating \(R\) as the areal radius, would be:

$$\kappa_{\rm naive} = \frac12\ln(T(R)Q(R)).$$

The correct areal-gauge \(\kappa\), constructed after using \(r = S(R)\), is:

$$\kappa_{\rm areal} = \frac12\ln\left(\frac{T(R)Q(R)}{[S'(R)]^2}\right).$$

The difference is:

$$\kappa_{\rm naive} - \kappa_{\rm areal} = \ln S'(R).$$

This is precisely the radial gauge Jacobian identified in the gauge-dependence study.

---

## Areal-Gauge Compensation Condition

The compensation condition in areal gauge is:

$$\kappa_{\rm areal} = 0.$$

This is equivalent to:

$$\frac{T(R)Q(R)}{[S'(R)]^2} = 1.$$

Or:

$$T(R)Q(R) = [S'(R)]^2.$$

In areal gauge itself, where \(R = r\) and \(S(R) = R\), this reduces to:

$$AB = 1.$$

So the familiar areal-gauge reciprocal relation is a special case of the more general condition.

---

## Recovery of Previous Reparameterization Result

Starting from an areal-gauge metric and reparameterizing \(r = f(R)\):

$$T(R) = A(f(R)),$$

$$Q(R) = B(f(R))[f'(R)]^2,$$

$$S(R) = f(R).$$

The areal-gauge \(\kappa\) reconstructed from these is:

$$\kappa_{\rm areal} = \frac12\ln\left(\frac{A(f(R))B(f(R))[f'(R)]^2}{[f'(R)]^2}\right) = \frac12\ln(A(f(R))B(f(R))).$$

The Jacobian factor cancels. This recovers the original areal-gauge \(\kappa\), confirming that the arbitrary-coordinate expression correctly removes the gauge artifact.

---

## Gauge-Fixed Condition as Geometric Construction

The result can be stated as a procedure:

1. Start with a static spherical geometry.
2. Define the areal radius by sphere area: \(r = \sqrt{\text{Area}/4\pi}\).
3. Express the metric in areal-radius form: \(ds^2 = -A(r)c^2dt^2 + B(r)dr^2 + r^2 d\Omega^2\).
4. Define \(\kappa_{\rm areal} = \frac12\ln(AB)\).
5. Exterior reciprocal compensation is \(\kappa_{\rm areal} = 0\), equivalently \(AB = 1\).

This is not a coordinate-invariant scalar equation. It is a condition after geometric gauge fixing by sphere area.

---

## Arbitrary-Coordinate Expression

In a general static spherical metric:

$$ds^2 = -T(R)c^2dt^2 + Q(R)dR^2 + S(R)^2 d\Omega^2,$$

the areal-gauge compensation condition \(\kappa_{\rm areal} = 0\) is equivalent to:

$$T(R)Q(R) = [S'(R)]^2.$$

This expression includes the angular-radius function \(S(R)\). It is the arbitrary-coordinate version of the areal-gauge condition \(AB = 1\).

---

## Failure Control: Ignoring the Angular Sector

If one ignores the angular sector and computes only the naive product \(T(R)Q(R)\), then a pure radial reparameterization of an \(AB = 1\) metric gives:

$$T(R)Q(R) = [f'(R)]^2.$$

This falsely looks like reciprocal compensation failed.

But the angular sector is \(f(R)^2 d\Omega^2\), so the areal radius is \(f(R)\), and \(S'(R) = f'(R)\).

The corrected expression is:

$$\frac{T(R)Q(R)}{[S'(R)]^2} = \frac{[f'(R)]^2}{[f'(R)]^2} = 1.$$

The gauge artifact disappears when the angular-radius function is included.

---

## What This Study Established

This study established:

1. The areal radius is geometrically defined by sphere area.
2. In arbitrary radial coordinate \(R\), the metric has angular radius \(S(R)\).
3. Transforming to areal radius \(r = S(R)\) gives \(B_{\rm areal} = Q(R)/[S'(R)]^2\).
4. Therefore \(\kappa_{\rm areal} = \frac12\ln[T(R)Q(R)/[S'(R)]^2]\).
5. Areal-gauge compensation \(\kappa_{\rm areal} = 0\) becomes \(T(R)Q(R) = [S'(R)]^2\).
6. This is a gauge-fixed geometric condition, not a raw scalar condition.
7. Including the angular-radius function removes the false Jacobian artifact from the gauge-dependence study.

---

## What This Study Did Not Establish

This study did not prove that \(\kappa\) is a coordinate-invariant scalar.

It did not produce a fully covariant field equation.

It did not address time-dependent or non-spherical geometries.

It did not derive the condition from an action principle.

It only showed that \(\kappa = 0\) can be safely phrased as an areal-gauge condition derived from sphere-area radial foliation geometry.

---

## Relationship to the Gauge-Dependence Study

The gauge-dependence study showed that naive \(\kappa\) and \(s\) shift under radial reparameterization. This study shows how to write the compensation condition in a form that includes the angular-radius function \(S(R)\), removing the false Jacobian artifact.

The key repair is replacing:

$$TQ = 1 \quad \text{(naive, fails under reparameterization)}$$

with:

$$TQ = [S']^2 \quad \text{(gauge-aware, includes sphere-area geometry)}.$$

---

## Relationship to the Orbit-Space Modes Study

The orbit-space modes study takes this further by identifying:

$$[S'(R)]^2 / Q(R) = |\nabla R|^2,$$

the orbit-space norm of the areal-radius gradient. This gives the cleaner geometric form:

$$\kappa = \frac12\ln\left(\frac{A}{|\nabla R|^2}\right),$$

and:

$$A = |\nabla R|^2$$

as the compensation condition.

---

## Development Implication

The key implication is:

```text
kappa=0 can be safely phrased as an areal-gauge condition derived
from sphere-area radial foliation geometry.
```

The areal radius provides a geometric gauge-fixing mechanism that makes \(\kappa\) well-defined within the static spherical sector. The arbitrary-coordinate expression \(TQ = [S']^2\) correctly handles the angular sector and avoids false gauge artifacts.

---

## Summary

The areal-gauge kappa condition study bridges from the gauge-dependence result to a more geometric formulation.

The gauge-dependence study showed:

$$\kappa \rightarrow \kappa + \ln f'.$$

This study shows that the compensation condition can be written as:

$$T(R)Q(R) = [S'(R)]^2,$$

which includes the angular-radius function and is valid in any radial coordinate.

In areal gauge, this reduces to \(AB = 1\).

This is not a coordinate-invariant scalar equation. It is a condition after geometric gauge fixing by the area of symmetry spheres.

The orbit-space modes study subsequently reinterprets this in terms of the areal-radius gradient norm \(|\nabla R|^2\).
