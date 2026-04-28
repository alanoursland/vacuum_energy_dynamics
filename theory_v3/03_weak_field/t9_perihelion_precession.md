# T9: Perihelion Precession

## What This Theorem Establishes

In a static, source-free exterior weak field around a localized mass, a bound test-body orbit advances by

$$\Delta\varpi=\frac{6\pi GM}{a(1-e^2)c^2}$$

per orbit, where $a$ is the orbit's semi-major axis and $e$ is its eccentricity.

This is the standard weak-field perihelion-precession result of general relativity.

In PPN language, the leading perihelion advance is

$$\Delta\varpi=(2+2\gamma-\beta)\frac{2\pi GM}{a(1-e^2)c^2}.$$

By T3, the framework has

$$\gamma=1.$$

By T4, the framework has

$$\beta=1.$$

Therefore,

$$2+2\gamma-\beta=3,$$

and so

$$\Delta\varpi=3\frac{2\pi GM}{a(1-e^2)c^2}=\frac{6\pi GM}{a(1-e^2)c^2}.$$

This theorem is the weak-field orbital payoff of having both exterior spatial response and second-order temporal self-coupling.

## Why This Theorem Is Needed

Light deflection and Shapiro delay primarily test the first-order spatial-response coefficient $\gamma$. Perihelion precession tests a different combination of weak-field structure. It depends on both the spatial-response coefficient $\gamma$ and the nonlinear temporal coefficient $\beta$.

That makes perihelion precession a stronger recovery test than redshift, time dilation, light deflection, or Shapiro delay alone.

The framework's recovery chain is:

T3 gives the spatial-response result

$$\gamma=1.$$

T4 gives the temporal nonlinear result

$$\beta=1.$$

T5 assembles these into the static exterior weak-field metric.

T9 uses that metric to derive the perihelion advance.

Without T4/P8, this theorem would remain incomplete. The precession formula would still contain an undetermined $\beta$. With T4 in place, the framework recovers the standard result.

## The Setup

Consider a test body of negligible mass orbiting a central localized mass $M$ in the static exterior weak-field region.

Let

$$U(r)=\frac{GM}{r}$$

be the positive Newtonian potential magnitude.

Let the orbit have semi-major axis $a$, eccentricity $e$, and semi-latus rectum

$$p=a(1-e^2).$$

Use the reciprocal radius variable

$$u=\frac{1}{r}.$$

The assumptions are:

1. **Weak field:** $GM/(rc^2)\ll1$ throughout the orbit.
2. **Slow orbital motion:** $v^2/c^2\ll1$.
3. **Bound orbit:** the Newtonian orbit is approximately elliptical.
4. **Test-body limit:** the orbiting body does not significantly alter the exterior configuration.
5. **Static exterior:** the central source and exterior field are time-independent.
6. **Source-free exterior:** the test body moves outside the matter source.
7. **One-post-Newtonian order:** terms are kept through the order needed for the leading relativistic perihelion advance.

The proof uses the static exterior weak-field metric assembled in T5.

## Metric Input

T5 gives the PPN-compatible static exterior weak-field metric:

$$ds^2=-\left(1-\frac{2U}{c^2}+2\beta\frac{U^2}{c^4}\right)c^2dt^2+\left(1+2\gamma\frac{U}{c^2}\right)d\vec{x}^{\,2}.$$

For the framework,

$$\gamma=1,$$

and

$$\beta=1.$$

For the derivation, keep $\gamma$ and $\beta$ symbolic until the final substitution. This makes clear which part of the framework supplies which part of the result.

The metric is static and spherically symmetric to the order used here, so the orbit may be taken to lie in a plane. Use polar coordinates in that plane:

$$d\vec{x}^{\,2}=dr^2+r^2d\phi^2.$$

## Post-Newtonian Orbital Equation

Expanding the geodesic equation for a slow test body in the static weak-field PPN metric gives the one-post-Newtonian orbital equation

$$\frac{d^2u}{d\phi^2}+u=\frac{GM}{h^2}+(2+2\gamma-\beta)\frac{GM}{c^2}u^2.$$

Here $h$ is the Newtonian angular momentum per unit mass. At leading Newtonian order,

$$h^2=GMp.$$

The first term on the right-hand side gives the ordinary Newtonian ellipse. The second term is the leading relativistic correction. Its coefficient contains the PPN combination

$$2+2\gamma-\beta.$$

This is the key structural point. Perihelion precession is not controlled by $\gamma$ alone or by $\beta$ alone. It is controlled by their combination.

For the framework, T3 supplies $\gamma=1$ and T4 supplies $\beta=1$, so this correction becomes

$$3\frac{GM}{c^2}u^2.$$

That is the same correction term obtained from the Schwarzschild weak-field limit.

## Perturbative Solution

The Newtonian orbit satisfies

$$\frac{d^2u_0}{d\phi^2}+u_0=\frac{GM}{h^2}.$$

Its solution is

$$u_0=\frac{1}{p}(1+e\cos\phi),$$

where

$$p=\frac{h^2}{GM}=a(1-e^2).$$

Now treat the post-Newtonian term as a small perturbation. Substitute the Newtonian solution into the correction term:

$$u_0^2=\frac{1}{p^2}(1+2e\cos\phi+e^2\cos^2\phi).$$

The term that produces secular precession is the resonant term proportional to $\cos\phi$:

$$2e\frac{1}{p^2}\cos\phi.$$

Therefore the resonant part of the perturbation equation is

$$\frac{d^2\delta u}{d\phi^2}+\delta u=(2+2\gamma-\beta)\frac{GM}{c^2}\frac{2e}{p^2}\cos\phi.$$

For an equation of the form

$$y''+y=A\cos\phi,$$

a resonant particular solution is

$$y_{\text{res}}=\frac{A}{2}\phi\sin\phi.$$

Thus,

$$\delta u_{\text{res}}=(2+2\gamma-\beta)\frac{GM e}{c^2p^2}\phi\sin\phi.$$

This secular term is the mathematical signature of orbital precession.

## Extracting the Precession

A slowly precessing ellipse can be written as

$$u=\frac{1}{p}\left[1+e\cos((1-\delta)\phi)\right],$$

where $\delta\ll1$ is the fractional angular advance per radian.

Expand the cosine to first order in $\delta$:

$$\cos((1-\delta)\phi)\approx\cos\phi+\delta\phi\sin\phi.$$

Then the orbit becomes

$$u\approx\frac{1}{p}\left[1+e\cos\phi+e\delta\phi\sin\phi\right].$$

The secular precession term is therefore

$$\frac{e\delta}{p}\phi\sin\phi.$$

Compare this with the perturbative secular term:

$$\delta u_{\text{res}}=(2+2\gamma-\beta)\frac{GM e}{c^2p^2}\phi\sin\phi.$$

Equating coefficients gives

$$\frac{e\delta}{p}=(2+2\gamma-\beta)\frac{GM e}{c^2p^2}.$$

Canceling $e$ and solving for $\delta$,

$$\delta=(2+2\gamma-\beta)\frac{GM}{c^2p}.$$

The perihelion advance per orbit is the excess angle accumulated over $2\pi$ radians:

$$\Delta\varpi=2\pi\delta.$$

Therefore,

$$\Delta\varpi=(2+2\gamma-\beta)\frac{2\pi GM}{c^2p}.$$

Since

$$p=a(1-e^2),$$

we get

$$\Delta\varpi=(2+2\gamma-\beta)\frac{2\pi GM}{a(1-e^2)c^2}.$$

## Substituting the Framework Values

By T3,

$$\gamma=1.$$

By T4,

$$\beta=1.$$

Therefore,

$$2+2\gamma-\beta=2+2(1)-1=3.$$

Substituting,

$$\Delta\varpi=3\frac{2\pi GM}{a(1-e^2)c^2}.$$

So,

$$\Delta\varpi=\frac{6\pi GM}{a(1-e^2)c^2}.$$

This is the standard general-relativistic weak-field perihelion advance.

## Physical Interpretation in Framework Terms

In the framework, perihelion precession is not caused by one isolated effect. It is produced by the combined temporal and spatial structure of the static exterior vacuum configuration.

The Newtonian part of the orbit comes from the leading temporal gradient. T6 shows that the weak-field metric recovers the Newtonian acceleration for slow bodies.

The relativistic precession comes from the next-order structure. Two pieces matter:

First, the spatial mapping of the exterior vacuum is not flat. P7/T3 supplies the reciprocal exterior spatial response, giving

$$\gamma=1.$$

Second, the temporal mapping is nonlinear. P8/T4 supplies temporal self-coupling, giving

$$\beta=1.$$

The orbit precesses because the actual exterior vacuum configuration differs from the Newtonian inverse-square system in both ways. The spatial geometry and the temporal self-coupling together modify the radial orbital equation by the term

$$3\frac{GM}{c^2}u^2.$$

That term is what advances the perihelion.

This makes perihelion precession the cleanest weak-field test of the framework's full static exterior recovery structure. Redshift and time dilation test the first-order temporal side. Light deflection and Shapiro delay test the spatial-response side. Perihelion precession tests the combination of spatial response and second-order temporal self-coupling.

## Relationship to T5 and T6

T5 assembles the static exterior weak-field metric. T9 uses that metric through one-post-Newtonian order.

T6 establishes the Newtonian limit:

$$\frac{d^2\mathbf{x}}{dt^2}=\nabla U.$$

That result corresponds to the leading Newtonian orbital equation

$$\frac{d^2u}{d\phi^2}+u=\frac{GM}{h^2}.$$

T9 goes beyond T6 by keeping the leading post-Newtonian correction to the orbital equation:

$$\frac{d^2u}{d\phi^2}+u=\frac{GM}{h^2}+(2+2\gamma-\beta)\frac{GM}{c^2}u^2.$$

So T6 proves the baseline inverse-square motion. T9 proves the first relativistic correction to bound orbits.

## Relationship to Light Deflection and Shapiro Delay

Light deflection and Shapiro delay depend at leading order on

$$1+\gamma.$$

They are therefore primarily tests of the framework's spatial response.

Perihelion precession depends on

$$2+2\gamma-\beta.$$

It is therefore a combined test of spatial response and temporal nonlinearity.

This is why T9 belongs after T4 and T5. The framework cannot honestly claim to recover perihelion precession unless it has both

$$\gamma=1$$

and

$$\beta=1.$$

With T3 and T4 in place, the perihelion result follows.

## What This Theorem Does Not Establish

T9 does not derive the source law $U=GM/r$ from the framework's configuration-energy functional. It uses the Newtonian exterior potential profile in the weak-field point-mass limit.

T9 does not derive the full strong-field orbital structure. It is a one-post-Newtonian weak-field theorem.

T9 does not apply to orbits near black-hole horizons, innermost stable circular orbits, or other strong-field regimes.

T9 does not include spin, frame dragging, quadrupole moments, or multipole corrections. Rotating or nonspherical sources require additional metric structure not present in T5.

T9 does not apply inside matter. It assumes a source-free exterior.

T9 does not establish $\gamma=1$ or $\beta=1$ by itself. It depends on T3 and T4 for those values.

T9 does not derive P7 or P8. It is conditional on the exterior structural postulates through the earlier theorem chain.

## Status of the Result

T9 is a theorem downstream of T5.

Given:

- the static exterior weak-field metric assembled in T5,
- the spatial-response result $\gamma=1$ from T3,
- the temporal nonlinear result $\beta=1$ from T4,
- weak fields,
- slow bound orbital motion,
- the test-body limit,
- and the point-mass exterior potential $U=GM/r$,

then the perihelion advance per orbit is

$$\Delta\varpi=\frac{6\pi GM}{a(1-e^2)c^2}.$$

This matches the standard weak-field general-relativistic perihelion-precession result.

The theorem is conditional on the framework's exterior weak-field recovery structure. If P7/T3 were removed, the result would remain parameterized by $\gamma$. If P8/T4 were removed, the result would remain parameterized by $\beta$.

## Imports and Dependencies

This theorem invokes:

- SR3: Spacetime Interval and Minkowski Structure, for the metric form and flat limit.
- SR9: Local Validity of SR in Inertial Frames, for the interpretation of local free motion.

It depends on:

- P1: Vacuum-Energy Equivalence, as part of the ontology underlying vacuum configuration.
- P2: Vacuum-Spacetime Identity, because the metric is interpreted as vacuum/spacetime structure.
- P3a: Spatial Differential is Curvature, for the framework's curvature vocabulary.
- P4: Curvature Contains Energy, for the configuration-energy status of curved vacuum.
- P5: Vacuum Seeks Minimum Energy Configuration, for the static exterior as a constrained minimum configuration.
- P7: Static Exterior Vacuum Compensation, inherited through T3.
- P8: Static Exterior Temporal Self-Coupling, inherited through T4.
- T3: Reciprocal Exterior Scaling, for $\gamma=1$.
- T4: Second-Order Temporal Self-Coupling, for $\beta=1$.
- T5: Static Exterior Weak-Field Metric, the direct metric input for the proof.
- T6: Newtonian Limit, for the leading Newtonian orbital baseline.

T1 and T2 are inherited through T5 as part of the first-order temporal recovery chain.

## Summary

T9 derives the weak-field perihelion-precession formula from the framework's assembled static exterior metric.

The one-post-Newtonian orbital equation is

$$\frac{d^2u}{d\phi^2}+u=\frac{GM}{h^2}+(2+2\gamma-\beta)\frac{GM}{c^2}u^2.$$

The Newtonian orbit is

$$u_0=\frac{1}{p}(1+e\cos\phi),$$

with

$$p=a(1-e^2).$$

The post-Newtonian correction produces a secular precession

$$\Delta\varpi=(2+2\gamma-\beta)\frac{2\pi GM}{pc^2}.$$

Using T3 and T4,

$$\gamma=1,$$

and

$$\beta=1.$$

Therefore,

$$\Delta\varpi=\frac{6\pi GM}{a(1-e^2)c^2}.$$

This theorem shows that the framework recovers the standard weak-field perihelion advance once both exterior recovery conditions are in place: reciprocal exterior scaling for $\gamma=1$ and temporal self-coupling for $\beta=1$.