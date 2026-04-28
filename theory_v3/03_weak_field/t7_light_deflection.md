# T7: Light Deflection

## What This Theorem Establishes

In a static, source-free exterior weak field around a localized mass, light passing the mass at impact parameter $b$ is deflected by

$$
\Delta\theta=\frac{4GM}{bc^2}.
$$

This is the standard weak-field light-deflection result of general relativity.

The framework obtains this result from the static exterior weak-field metric assembled in T5. The leading deflection depends on the first-order temporal and spatial metric coefficients. In PPN language, the result depends on the combination

$$
1+\gamma.
$$

Since T3 gives the framework's spatial-response value

$$
\gamma=1,
$$

the deflection becomes

$$
\Delta\theta=(1+\gamma)\frac{2GM}{bc^2}=\frac{4GM}{bc^2}.
$$

This theorem is therefore one of the direct observational payoffs of P7/T3. Without the spatial response supplied by reciprocal exterior scaling, the framework would recover only the temporal half of the deflection.

---

## The Setup

Consider a light ray passing a localized mass $M$ in the static exterior weak-field region. Let the ray's unperturbed path run along the $z$ direction, with closest approach distance $b$ in the transverse direction. Along the unperturbed path,

$$
r=\sqrt{b^2+z^2}.
$$

The positive Newtonian potential magnitude is

$$
U(r)=\frac{GM}{r}.
$$

The assumptions are:

1. **Weak field:** $U/c^2\ll1$ along the path.
2. **Small deflection:** the actual path can be evaluated to leading order along the unperturbed straight line.
3. **Static exterior:** the mass is not changing during the light passage.
4. **Source-free exterior:** the ray propagates outside the matter source.
5. **Asymptotic flatness:** far from the mass, the metric approaches Minkowski form.
6. **Impact parameter:** $b$ is large compared with the source radius, so the exterior weak-field metric applies throughout the relevant path.

The proof uses the weak-field metric from T5:

$$
ds^2
-\left(1-\frac{2U}{c^2}\right)c^2dt^2
+
\left(1+2\frac{U}{c^2}\right)d\ell^2
+
O(c^{-4})
$$

for the leading light-deflection calculation. The $U^2/c^4$ temporal term is not needed at leading order.

---

## Why Only the First-Order Metric Is Needed

Light deflection at leading order is an $O(c^{-2})$ effect. Therefore, the proof only needs the metric through first order in $U/c^2$:

$$
-g_{tt}=1-\frac{2U}{c^2}+O(c^{-4}),
$$

and

$$
g_{ij}=\left(1+2\frac{U}{c^2}\right)\delta_{ij}+O(c^{-4}).
$$

The second-order temporal coefficient from T4, equivalently $\beta=1$, is not needed for the leading deflection result. It becomes important for one-post-Newtonian orbital dynamics, especially perihelion precession.

For light deflection, the crucial input beyond the temporal redshift/time-dilation side is the spatial coefficient. T3 supplies that coefficient by giving

$$
\gamma=1.
$$

---

## The Null Condition and Effective Optical Index

For light,

$$
ds^2=0.
$$

Using the leading-order T5 metric,

$$
0
-\left(1-\frac{2U}{c^2}\right)c^2dt^2
+
\left(1+2\frac{U}{c^2}\right)d\ell^2.
$$

Solve for the coordinate travel time:

$$
c^2dt^2
\frac{1+2U/c^2}{1-2U/c^2}d\ell^2.
$$

Taking the square root and expanding to first order,

$$
cdt
\sqrt{\frac{1+2U/c^2}{1-2U/c^2}}d\ell
\approx
\left(1+2\frac{U}{c^2}\right)d\ell.
$$

This has the form of light propagation through an effective refractive index $n(r)$:

$$
cdt=n(r)d\ell,
$$

with

$$
n(r)=1+2\frac{U(r)}{c^2}.
$$

More generally, if the spatial response were parameterized by $\gamma$, the effective index would be

$$
n(r)=1+(1+\gamma)\frac{U(r)}{c^2}.
$$

The framework has $\gamma=1$ by T3, so

$$
n(r)=1+2\frac{U(r)}{c^2}.
$$

This is the step where the spatial contribution enters. The temporal coefficient alone would give only

$$
n(r)=1+\frac{U(r)}{c^2},
$$

and therefore only half the observed deflection.

---

## Deflection from the Transverse Gradient

In a weakly varying optical medium, the small deflection angle is obtained by integrating the transverse gradient of the refractive index along the unperturbed path:

$$
\Delta\boldsymbol{\theta}
\int_{-\infty}^{\infty}\nabla_\perp n,dz.
$$

With

$$
n(r)=1+2\frac{U(r)}{c^2},
$$

we have

$$
\nabla_\perp n
\frac{2}{c^2}\nabla_\perp U.
$$

For the unperturbed path, take the transverse coordinate to be $b$. Then

$$
U=\frac{GM}{\sqrt{b^2+z^2}}.
$$

The transverse derivative is

$$
\frac{\partial U}{\partial b}
-\frac{GMb}{(b^2+z^2)^{3/2}}.
$$

The negative sign means the deflection points inward, toward the mass. The magnitude is

$$
|\Delta\theta|
\frac{2}{c^2}\int_{-\infty}^{\infty}\frac{GMb}{(b^2+z^2)^{3/2}}dz.
$$

The integral is standard:

$$
\int_{-\infty}^{\infty}\frac{b,dz}{(b^2+z^2)^{3/2}}
\frac{2}{b}.
$$

Therefore,

$$
|\Delta\theta|
\frac{2GM}{c^2}\cdot\frac{2}{b}.
$$

So

$$
\Delta\theta=\frac{4GM}{bc^2}.
$$

This is the standard weak-field light-deflection result.

---

## PPN Form of the Result

Keeping the spatial-response parameter $\gamma$ symbolic, the effective refractive index is

$$
n(r)=1+(1+\gamma)\frac{U(r)}{c^2}.
$$

The same integration gives

$$
\Delta\theta
(1+\gamma)\frac{2GM}{bc^2}.
$$

T3 gives

$$
\gamma=1,
$$

so

$$
\Delta\theta
2\frac{2GM}{bc^2}
\frac{4GM}{bc^2}.
$$

This makes the role of T3 explicit. The temporal part gives one contribution. The spatial part, fixed by reciprocal exterior scaling, gives the second equal contribution. Together they produce the observed value.

---

## Physical Interpretation in Framework Terms

In standard weak-field language, light deflection comes from null propagation through the curved exterior metric. The framework gives that statement a vacuum-configuration interpretation.

T1 and T2 establish the temporal side: photons climbing or descending through a curvature gradient shift energy, and clock-rate mappings differ between locations in the gradient.

T3 establishes the spatial side: in a static source-free exterior, temporal and radial spatial mappings are reciprocally related. Exterior curvature is compensated directional redistribution of vacuum extent rather than net vacuum substance exchange.

Light propagating through this exterior does not merely experience a temporal redshift effect. It also traverses a spatial geometry whose proper-distance mapping differs from the asymptotic coordinate mapping. The effective optical index

$$
n(r)=1+2\frac{U}{c^2}
$$

contains both parts.

Thus light deflection is a direct test that the framework has not stopped at temporal gravity alone. A theory with only the T1/T2 temporal mapping and no spatial response would predict half the deflection. The framework reaches the full result because P7/T3 supplies the reciprocal spatial response.

---

## Relationship to Earlier Framework Results

T7 depends directly on T5, the assembled static exterior weak-field metric.

The leading deflection uses only the first-order part of that metric. In terms of earlier results:

* T1 and T2 supply the first-order temporal mapping.
* T3 supplies $\gamma=1$, the spatial-response coefficient.
* T5 packages these into the weak-field metric used here.

T4 and P8 are not required for the leading light-deflection coefficient. They are part of the assembled one-post-Newtonian recovery structure, but the leading light-deflection proof is controlled by $\gamma$, not by $\beta$.

This dependency distinction matters. Light deflection is a test of the framework's spatial response. Perihelion precession will test the combination of spatial response and second-order temporal response.

---

## What This Theorem Does Not Establish

T7 does not derive the source law $U=GM/r$ from the framework's configuration-energy functional. It uses the Newtonian exterior potential profile in the weak-field point-mass limit.

T7 does not derive the full null geodesic equation in arbitrary fields. It uses the static weak-field optical-index form appropriate to the T5 metric.

T7 does not apply to strong lensing, multiple-image regimes, photon spheres, or near-horizon behavior. Those require strong-field structure that the framework has not yet derived.

T7 does not apply to rotating lenses or frame-dragging effects. Those require off-diagonal metric terms not present in T5.

T7 does not apply automatically to time-dependent gravitational fields or gravitational waves.

T7 does not establish $\gamma=1$ by itself. It depends on T3 for that result.

---

## Status of the Result

T7 is a theorem downstream of T5.

Given:

* the static exterior weak-field metric assembled in T5,
* the spatial-response result $\gamma=1$ from T3,
* weak fields,
* small deflection,
* source-free exterior propagation,
* and the point-mass exterior potential $U=GM/r$,

then a light ray passing the mass with impact parameter $b$ is deflected by

$$
\Delta\theta=\frac{4GM}{bc^2}.
$$

This matches the standard general-relativistic weak-field prediction and the observed solar-system light-deflection result.

The theorem is conditional on the framework's exterior weak-field recovery structure. If P7/T3 were removed, the spatial-response coefficient would no longer be fixed and the deflection would remain parameterized by $\gamma$.

---

## Imports and Dependencies

This theorem invokes:

* SR2: Invariance of the Speed of Light, for local light propagation at $c$.
* SR3: Spacetime Interval and Minkowski Structure, for the null condition and flat limit.
* SR9: Local Validity of SR in Inertial Frames, for the interpretation that light is locally measured at $c$ even though coordinate propagation varies.

It depends on:

* P1: Vacuum-Energy Equivalence, as part of the ontology underlying vacuum configuration.
* P2: Vacuum-Spacetime Identity, because light propagates through vacuum/spacetime structure.
* P3a: Spatial Differential is Curvature, for the framework's curvature vocabulary.
* P4: Curvature Contains Energy, for the configuration-energy status of curved vacuum.
* P5: Vacuum Seeks Minimum Energy Configuration, for the static exterior as a constrained minimum configuration.
* P7: Static Exterior Vacuum Compensation, inherited through T3.
* T1: Gravitational Redshift, for the temporal side of the weak-field metric inherited through T5.
* T2: Gravitational Time Dilation, for the clock-rate interpretation inherited through T5.
* T3: Reciprocal Exterior Scaling, for $\gamma=1$.
* T5: Static Exterior Weak-Field Metric, the direct metric input for the proof.

T4 and P8 are part of T5's full one-post-Newtonian assembly, but the leading light-deflection coefficient does not require $\beta=1$.

---

## Summary

T7 derives weak-field light deflection from the framework's assembled static exterior metric.

From T5, the leading null metric is

$$
ds^2
-\left(1-\frac{2U}{c^2}\right)c^2dt^2
+
\left(1+2\frac{U}{c^2}\right)d\ell^2.
$$

Setting $ds^2=0$ gives the effective optical index

$$
n(r)=1+2\frac{U(r)}{c^2}.
$$

For

$$
U(r)=\frac{GM}{\sqrt{b^2+z^2}},
$$

the transverse-gradient integral gives

$$
\Delta\theta
\frac{2}{c^2}\int_{-\infty}^{\infty}\frac{GMb}{(b^2+z^2)^{3/2}}dz
\frac{4GM}{bc^2}.
$$

The result depends on the spatial-response coefficient $\gamma=1$ supplied by T3. This is the theorem that shows the framework recovers the full weak-field light-deflection result rather than the half-deflection produced by temporal gravity alone.
