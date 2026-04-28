# T6: Newtonian Limit

## What This Theorem Establishes

In the static, source-free exterior weak-field regime, slow massive test bodies follow Newtonian gravitational motion.

Using the positive Newtonian potential magnitude

$$
U(r)=\frac{GM}{r},
$$

with $U\to0$ at infinity, the theorem establishes

$$
\frac{d^2\mathbf{x}}{dt^2}=\nabla U.
$$

For a point mass,

$$
\nabla U=-\frac{GM}{r^2}\hat{\mathbf{r}},
$$

so

$$
\frac{d^2\mathbf{x}}{dt^2}=-\frac{GM}{r^2}\hat{\mathbf{r}}.
$$

Equivalently, if one uses the signed Newtonian potential

$$
\Phi=-U,
$$

then the result is the familiar form

$$
\frac{d^2\mathbf{x}}{dt^2}=-\nabla\Phi.
$$

This theorem shows that the framework's assembled static exterior weak-field metric reproduces the Newtonian limit for slow massive bodies.

---

## Why This Theorem Is Needed

T5 assembles the framework's static exterior weak-field metric. That metric is the gateway to the remaining weak-field tests, but the framework also needs to show that the metric gives the correct motion of ordinary slow bodies.

The Newtonian limit is the minimal dynamical recovery condition. Before deriving perihelion precession or other post-Newtonian corrections, the framework must recover the leading equation of motion:

$$
\mathbf{a}=-\frac{GM}{r^2}\hat{\mathbf{r}}.
$$

This theorem performs that check.

It also fixes a sign convention that matters downstream. T5 uses $U$ as a positive potential magnitude. With that convention, the acceleration is

$$
\mathbf{a}=\nabla U,
$$

because $U=GM/r$ decreases outward and its gradient points inward. In the more common signed-potential convention, where $\Phi=-GM/r$, the same equation is

$$
\mathbf{a}=-\nabla\Phi.
$$

---

## The Setup

Consider a slow massive test body moving in the static, source-free exterior weak-field metric established by T5:

$$
ds^2
-\left(1-\frac{2U}{c^2}+2\frac{U^2}{c^4}\right)c^2dt^2
+
\left(1+2\frac{U}{c^2}\right)d\vec{x}^{,2}
+
O(c^{-6})*{tt}+O(c^{-4})*{ij}.
$$

For the Newtonian limit, only the leading temporal coefficient is needed:

$$
g_{tt}=-\left(1-\frac{2U}{c^2}\right)+O(c^{-4}).
$$

The assumptions are:

1. **Weak field:** $U/c^2\ll1$.
2. **Slow motion:** $v^2/c^2\ll1$.
3. **Static exterior:** the metric coefficients are time-independent.
4. **Test-body limit:** the moving body does not significantly alter the exterior configuration.
5. **Source-free exterior:** the body moves outside the matter source producing the exterior potential.

The theorem uses the geodesic equation in the recovered weak-field metric. This is not an independent adoption of full general relativity as a theory. It is the standard statement that free test bodies follow extremal proper-time paths in the spacetime geometry already assembled by T5.

---

## The Relevant Geodesic Equation

For a massive test body, the geodesic equation is

$$
\frac{d^2x^i}{d\tau^2}
+
\Gamma^i_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau}
=0.
$$

In the slow-motion limit, the dominant velocity component is the time component. Spatial coordinate velocities are small compared with $c$, so terms involving $dx^i/d\tau$ are higher order. Therefore the leading spatial equation is

$$
\frac{d^2x^i}{d\tau^2}
+
\Gamma^i_{tt}\left(\frac{dt}{d\tau}\right)^2
=0.
$$

Dividing by $(dt/d\tau)^2$ gives, to leading order,

$$
\frac{d^2x^i}{dt^2}=-\Gamma^i_{tt}.
$$

Thus the Newtonian limit is determined by the connection coefficient $\Gamma^i_{tt}$.

---

## Computing the Connection

The Christoffel symbol is

$$
\Gamma^i_{tt}
\frac{1}{2}g^{i\lambda}\left(\partial_t g_{t\lambda}+\partial_t g_{t\lambda}-\partial_\lambda g_{tt}\right).
$$

The metric is static and has no time-space cross terms in this regime, so the time derivatives vanish and the only leading contribution is

$$
\Gamma^i_{tt}
-\frac{1}{2}g^{ij}\partial_j g_{tt}.
$$

To Newtonian order, the inverse spatial metric is

$$
g^{ij}=\delta^{ij}+O(c^{-2}).
$$

Also,

$$
g_{tt}=-\left(1-\frac{2U}{c^2}\right)+O(c^{-4})
=-1+\frac{2U}{c^2}+O(c^{-4}).
$$

Therefore,

$$
\partial_j g_{tt}=\frac{2}{c^2}\partial_j U+O(c^{-4}).
$$

Substituting,

$$
\Gamma^i_{tt}
=-\frac{1}{2}\delta^{ij}\left(\frac{2}{c^2}\partial_j U\right)+O(c^{-4}).
$$

So

$$
\Gamma^i_{tt}
=-\frac{1}{c^2}\partial^i U+O(c^{-4}).
$$

There is a convention issue here: the coordinate $t$ in the metric appears in the interval as $c^2dt^2$. If the time coordinate in the Christoffel calculation is taken as $x^0=ct$, then the corresponding coefficient is

$$
\Gamma^i_{00}=-\frac{1}{c^2}\partial^i U.
$$

The spatial acceleration with respect to $t$ is

$$
\frac{d^2x^i}{dt^2}=-c^2\Gamma^i_{00}.
$$

Therefore,

$$
\frac{d^2x^i}{dt^2}=\partial^i U.
$$

In vector form,

$$
\frac{d^2\mathbf{x}}{dt^2}=\nabla U.
$$

This is the Newtonian limit in the positive-potential convention.

---

## Point-Mass Exterior

For a localized point mass in the weak-field exterior,

$$
U(r)=\frac{GM}{r}.
$$

Its gradient is

$$
\nabla U
\frac{d}{dr}\left(\frac{GM}{r}\right)\hat{\mathbf{r}}
-\frac{GM}{r^2}\hat{\mathbf{r}}.
$$

Therefore,

$$\frac{d^2\mathbf{x}}{dt^2}-\frac{GM}{r^2}\hat{\mathbf{r}}.$$

This is Newton's inverse-square gravitational acceleration.

---

## Relation to P6

P6 already contains the framework's equivalence-principle content. It states that energy in a curvature gradient experiences force uniformly per unit energy. For a slow body whose rest energy is $Mc^2$, the force per unit energy gives

$$
F=Mg,
$$

and therefore

$$
a=g,
$$

independent of the body's mass.

T6 shows that the metric assembled in T5 expresses the same result geometrically. The connection derived from the weak-field temporal metric coefficient gives

$$
\mathbf{a}=\nabla U,
$$

which is the same acceleration field that P6 identifies as the force-per-energy response to the gradient.

Thus the Newtonian limit is recovered in both readings:

* dynamically, through P6's force-per-energy rule;
* geometrically, through the T5 weak-field metric.

This agreement is important. It shows that the framework's force-language and metric-language are consistent in the slow-motion weak-field limit.

---

## What This Theorem Uses and Does Not Use

T6 uses only the leading temporal coefficient of the weak-field metric:

$$
g_{tt}=-1+\frac{2U}{c^2}+O(c^{-4}).
$$

It does not require the second-order temporal coefficient from T4. The $\beta=1$ result becomes important for post-Newtonian orbital corrections, especially perihelion precession, but it is not needed for the Newtonian limit.

It does not require the spatial coefficient $\gamma=1$ from T3 at leading order for slow massive bodies. The spatial metric contributes to higher-order corrections, but the leading Newtonian acceleration is controlled by $g_{tt}$.

This means the Newtonian limit is more robust than the full one-post-Newtonian recovery. Even before the framework closes the spatial-response and second-order temporal-response conditions, the leading slow-body acceleration follows from the first-order temporal metric structure.

However, T6 is placed downstream of T5 because T5 is the framework's assembled exterior metric theorem. Later weak-field proofs can depend on T5 and T6 in a clean order.

---

## Scope and Limitations

T6 applies only in the slow-motion weak-field limit.

It does not derive post-Newtonian corrections. Those require keeping terms of order $v^2/c^2$, $U/c^2$, and $U^2/c^4$ beyond the leading Newtonian acceleration.

It does not derive light propagation. Photons require the null condition and depend on both temporal and spatial metric coefficients. Light deflection and Shapiro delay are separate downstream theorems.

It does not derive perihelion precession. Perihelion precession requires one-post-Newtonian orbital dynamics and depends on both $\gamma$ and $\beta$.

It does not derive the source law $U=GM/r$ from the framework's configuration-energy functional. It uses the exterior Newtonian potential profile in the weak-field limit.

It does not apply inside matter, to cosmology, or to time-dependent, rotating, radiating, or strong-field configurations.

---

## Status of the Result

T6 is a theorem downstream of T5.

Given:

* the static exterior weak-field metric assembled in T5,
* slow test-body motion,
* weak fields,
* asymptotic flatness,
* and the exterior Newtonian potential profile $U$,

then the leading equation of motion is

$$
\frac{d^2\mathbf{x}}{dt^2}=\nabla U.
$$

For a point mass, this becomes

$$
\frac{d^2\mathbf{x}}{dt^2}=-\frac{GM}{r^2}\hat{\mathbf{r}}.
$$

So the framework recovers Newton's inverse-square gravitational acceleration for slow bodies in a static source-free exterior weak field.

---

## Imports and Dependencies

This theorem invokes:

* SR3: Spacetime Interval and Minkowski Structure, for the metric form and flat limit.
* SR9: Local Validity of SR in Inertial Frames, for the interpretation of local free motion.

It depends on:

* P1: Vacuum-Energy Equivalence, as part of the ontology behind the exterior vacuum configuration.
* P2: Vacuum-Spacetime Identity, because the metric is interpreted as vacuum/spacetime structure.
* P3a: Spatial Differential is Curvature, as part of the framework's curvature vocabulary.
* P4: Curvature Contains Energy, as part of the configuration-energy status of curved vacuum.
* P5: Vacuum Seeks Minimum Energy Configuration, for the static exterior as a constrained minimum configuration.
* P6: Vacuum Exchange in Gradients, for the equivalent force-per-energy interpretation of the Newtonian acceleration.
* T5: Static Exterior Weak-Field Metric, the direct metric input for the proof.

T5's dependency chain includes T1, T2, T3, T4, P7, and P8. T6 inherits those dependencies through T5, although the leading Newtonian acceleration itself uses only the first-order temporal coefficient.

---

## Summary

T6 establishes the Newtonian limit of the framework's static exterior weak-field metric.

From T5, the leading temporal metric coefficient is

$$
g_{tt}=-1+\frac{2U}{c^2}+O(c^{-4}).
$$

The slow-motion geodesic equation gives

$$
\frac{d^2x^i}{dt^2}=-c^2\Gamma^i_{00}.
$$

Computing the connection from the weak-field metric gives

$$
\Gamma^i_{00}=-\frac{1}{c^2}\partial^iU,
$$

so

$$
\frac{d^2x^i}{dt^2}=\partial^iU.
$$

For $U=GM/r$,

$$
\nabla U=-\frac{GM}{r^2}\hat{\mathbf{r}},
$$

therefore

$$
\frac{d^2\mathbf{x}}{dt^2}=-\frac{GM}{r^2}\hat{\mathbf{r}}.
$$

The framework therefore recovers Newtonian gravitational acceleration for slow test bodies in the static source-free exterior weak-field regime.
