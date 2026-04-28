# T8: Shapiro Delay

## What This Theorem Establishes

In a static, source-free exterior weak field around a localized mass, a light signal passing near the mass takes longer to travel between two distant points than it would in flat space.

For a one-way signal passing a mass $M$ with impact parameter $b$, emitted from radial distance $r_1$ and received at radial distance $r_2$, the leading weak-field Shapiro delay is

$$\Delta t_{\text{one-way}}=\frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right),$$

in the large-distance limit $r_1,r_2\gg b$.

For a round-trip radar signal following the same path outward and back, the delay is twice this:

$$\Delta t_{\text{round-trip}}=\frac{4GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

This is the standard general-relativistic weak-field Shapiro delay.

The framework obtains this result from the static exterior weak-field metric assembled in T5. Like light deflection, the leading Shapiro delay depends on the PPN combination

$$1+\gamma.$$

Since T3 gives

$$\gamma=1,$$

the framework recovers the full general-relativistic delay rather than the half-delay produced by temporal gravity alone.

## The Setup

Consider a light signal passing a localized mass $M$ in the static exterior weak-field region.

Let the unperturbed path run along the $z$ direction, with closest approach distance $b$ in the transverse direction. Along the unperturbed path,

$$r(z)=\sqrt{b^2+z^2}.$$

The positive Newtonian potential magnitude is

$$U(r)=\frac{GM}{r}.$$

Let the emitter be at coordinate position $z=-z_1$ and the receiver at coordinate position $z=z_2$, where $z_1,z_2>0$. Their radial distances from the mass are

$$r_1=\sqrt{b^2+z_1^2},$$

and

$$r_2=\sqrt{b^2+z_2^2}.$$

The assumptions are:

1. **Weak field:** $U/c^2\ll1$ along the path.
2. **Small deflection:** the travel time may be computed along the unperturbed straight path.
3. **Static exterior:** the mass and exterior field are not changing during the light propagation.
4. **Source-free exterior:** the light propagates outside the matter source.
5. **Asymptotic flatness:** far from the mass, the metric approaches Minkowski form.
6. **Large-distance approximation:** the logarithmic form simplifies when $r_1,r_2\gg b$.

The proof uses the leading-order null metric from T5:

$$ds^2=-\left(1-\frac{2U}{c^2}\right)c^2dt^2+\left(1+2\frac{U}{c^2}\right)d\ell^2.$$

The $U^2/c^4$ temporal term is not needed for the leading Shapiro delay.

## Why Only the First-Order Metric Is Needed

Shapiro delay at leading order is an $O(c^{-3})$ travel-time effect produced by the $O(U/c^2)$ correction to the coordinate light-travel time.

Therefore the proof only needs the metric through first order in $U/c^2$:

$$-g_{tt}=1-\frac{2U}{c^2}+O(c^{-4}),$$

and

$$g_{ij}=\left(1+2\frac{U}{c^2}\right)\delta_{ij}+O(c^{-4}).$$

The second-order temporal coefficient from T4, equivalently $\beta=1$, is not needed for the leading Shapiro delay.

The crucial input is the spatial-response coefficient from T3:

$$\gamma=1.$$

Without that spatial response, the delay would contain only the temporal contribution and would be half the general-relativistic value.

## The Null Condition and Effective Optical Index

For light,

$$ds^2=0.$$

Using the leading-order T5 metric,

$$0=-\left(1-\frac{2U}{c^2}\right)c^2dt^2+\left(1+2\frac{U}{c^2}\right)d\ell^2.$$

Solving for the coordinate travel time gives

$$cdt=\sqrt{\frac{1+2U/c^2}{1-2U/c^2}}\,d\ell.$$

Expanding to first order in $U/c^2$,

$$cdt=\left(1+2\frac{U}{c^2}\right)d\ell.$$

This is equivalent to light propagating through an effective optical index

$$n(r)=1+2\frac{U(r)}{c^2}.$$

More generally, if the spatial response is left parameterized by $\gamma$, the effective index is

$$n(r)=1+(1+\gamma)\frac{U(r)}{c^2}.$$

The framework has $\gamma=1$ by T3, so

$$n(r)=1+2\frac{U(r)}{c^2}.$$

The coordinate travel time is therefore

$$t=\frac{1}{c}\int n(r)\,d\ell.$$

The flat-space travel time is

$$t_0=\frac{1}{c}\int d\ell.$$

The excess time delay is

$$\Delta t=\frac{1}{c}\int (n(r)-1)\,d\ell.$$

Substituting the framework's effective index gives

$$\Delta t=\frac{2}{c^3}\int U(r)\,d\ell.$$

For a point mass,

$$U(r)=\frac{GM}{r},$$

so

$$\Delta t=\frac{2GM}{c^3}\int \frac{d\ell}{r}.$$

## Integrating Along the Light Path

To leading order, evaluate the delay along the unperturbed straight path. Then $d\ell=dz$ and

$$r(z)=\sqrt{b^2+z^2}.$$

The one-way delay is

$$\Delta t_{\text{one-way}}=\frac{2GM}{c^3}\int_{-z_1}^{z_2}\frac{dz}{\sqrt{b^2+z^2}}.$$

The integral is

$$\int\frac{dz}{\sqrt{b^2+z^2}}=\operatorname{asinh}\left(\frac{z}{b}\right).$$

Therefore,

$$\Delta t_{\text{one-way}}=\frac{2GM}{c^3}\left[\operatorname{asinh}\left(\frac{z_2}{b}\right)+\operatorname{asinh}\left(\frac{z_1}{b}\right)\right].$$

Using

$$\operatorname{asinh}(x)=\ln\left(x+\sqrt{1+x^2}\right),$$

we get

$$\Delta t_{\text{one-way}}=\frac{2GM}{c^3}\ln\left(\frac{(z_2+r_2)(z_1+r_1)}{b^2}\right).$$

In the large-distance limit $r_1,r_2\gg b$, we have

$$z_1+r_1\approx 2r_1,$$

and

$$z_2+r_2\approx 2r_2.$$

Thus,

$$\Delta t_{\text{one-way}}\approx\frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

For a round-trip signal, the leading delay is twice the one-way delay:

$$\Delta t_{\text{round-trip}}\approx\frac{4GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

This is the standard leading Shapiro radar-delay result in the general-relativistic case.

## PPN Form of the Result

Keeping $\gamma$ symbolic, the effective optical index is

$$n(r)=1+(1+\gamma)\frac{U(r)}{c^2}.$$

The excess one-way delay is then

$$\Delta t_{\text{one-way}}=(1+\gamma)\frac{GM}{c^3}\int_{-z_1}^{z_2}\frac{dz}{\sqrt{b^2+z^2}}.$$

So

$$\Delta t_{\text{one-way}}=(1+\gamma)\frac{GM}{c^3}\ln\left(\frac{(z_2+r_2)(z_1+r_1)}{b^2}\right).$$

In the large-distance limit,

$$\Delta t_{\text{one-way}}\approx(1+\gamma)\frac{GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

By T3,

$$\gamma=1.$$

Therefore,

$$\Delta t_{\text{one-way}}\approx\frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

This makes the role of the spatial response explicit. The Shapiro delay is not produced by temporal redshift alone. It depends on the combined temporal and spatial weak-field structure.

## Physical Interpretation in Framework Terms

In the framework, Shapiro delay is a frame-translation effect produced by the static exterior vacuum configuration.

Locally, light always propagates at $c$. This is required by SR2 and SR9. The light signal is not locally slowing down in an absolute sense.

The delay appears when an asymptotic observer translates local propagation along the path into their coordinate time. Near the mass, the temporal mapping and spatial mapping differ from their asymptotic values. T1 and T2 supply the temporal side of this mapping. T3 supplies the spatial side through reciprocal exterior scaling.

The resulting effective optical index is

$$n(r)=1+2\frac{U(r)}{c^2}.$$

That index is not a material refractive index. It is a compact way of expressing how the asymptotic observer's time coordinate relates to local light propagation through the exterior vacuum configuration.

In framework language, the light traverses a region where vacuum extent is directionally redistributed. The signal remains locally luminal, but the exterior mapping between local proper propagation and distant coordinate time produces an extra travel-time contribution.

## Relationship to Light Deflection

T7 and T8 use the same leading null structure.

T7 uses the transverse gradient of the effective optical index to derive light deflection:

$$\Delta\theta=\frac{4GM}{bc^2}.$$

T8 uses the line integral of the same effective optical index to derive Shapiro delay:

$$\Delta t_{\text{one-way}}\approx\frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

Both results depend on the same PPN combination:

$$1+\gamma.$$

Both therefore depend on T3's result:

$$\gamma=1.$$

The two proofs are companion tests of the framework's spatial weak-field response.

## Relationship to Earlier Framework Results

T8 depends directly on T5, the assembled static exterior weak-field metric.

The leading delay uses only the first-order part of that metric. In terms of earlier results:

- T1 and T2 supply the first-order temporal mapping.
- T3 supplies $\gamma=1$, the spatial-response coefficient.
- T5 packages these into the weak-field metric used here.

T4 and P8 are not required for the leading Shapiro delay coefficient. They are part of the full one-post-Newtonian metric assembly, but Shapiro delay at leading order is controlled by $\gamma$, not by $\beta$.

This dependency structure is parallel to T7. Light deflection and Shapiro delay test the spatial-response side of weak-field recovery. Perihelion precession tests the combination of spatial response and second-order temporal self-coupling.

## What This Theorem Does Not Establish

T8 does not derive the source law $U=GM/r$ from the framework's configuration-energy functional. It uses the Newtonian exterior potential profile in the weak-field point-mass limit.

T8 does not derive the full null geodesic equation in arbitrary fields. It uses the static weak-field optical-index form appropriate to the T5 metric.

T8 does not apply to strong-field time delay, near-horizon propagation, or photon-sphere behavior. Those require strong-field structure that the framework has not yet derived.

T8 does not apply to rotating sources or frame-dragging time delays. Those require off-diagonal metric terms not present in T5.

T8 does not apply automatically to time-dependent gravitational fields or gravitational waves.

T8 does not establish $\gamma=1$ by itself. It depends on T3 for that result.

## Status of the Result

T8 is a theorem downstream of T5.

Given:

- the static exterior weak-field metric assembled in T5,
- the spatial-response result $\gamma=1$ from T3,
- weak fields,
- small deflection,
- source-free exterior propagation,
- and the point-mass exterior potential $U=GM/r$,

then a one-way light signal passing the mass with impact parameter $b$ has the leading excess travel time

$$\Delta t_{\text{one-way}}\approx\frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

For a round-trip radar signal, the leading excess delay is

$$\Delta t_{\text{round-trip}}\approx\frac{4GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

This matches the standard general-relativistic weak-field Shapiro delay.

The theorem is conditional on the framework's exterior weak-field recovery structure. If P7/T3 were removed, the spatial-response coefficient would no longer be fixed and the delay would remain parameterized by $\gamma$.

## Imports and Dependencies

This theorem invokes:

- SR2: Invariance of the Speed of Light, for local light propagation at $c$.
- SR3: Spacetime Interval and Minkowski Structure, for the null condition and flat limit.
- SR9: Local Validity of SR in Inertial Frames, for the interpretation that light is locally measured at $c$ even though coordinate travel time varies.

It depends on:

- P1: Vacuum-Energy Equivalence, as part of the ontology underlying vacuum configuration.
- P2: Vacuum-Spacetime Identity, because light propagates through vacuum/spacetime structure.
- P3a: Spatial Differential is Curvature, for the framework's curvature vocabulary.
- P4: Curvature Contains Energy, for the configuration-energy status of curved vacuum.
- P5: Vacuum Seeks Minimum Energy Configuration, for the static exterior as a constrained minimum configuration.
- P7: Static Exterior Vacuum Compensation, inherited through T3.
- T1: Gravitational Redshift, for the temporal side of the weak-field metric inherited through T5.
- T2: Gravitational Time Dilation, for the clock-rate interpretation inherited through T5.
- T3: Reciprocal Exterior Scaling, for $\gamma=1$.
- T5: Static Exterior Weak-Field Metric, the direct metric input for the proof.

T4 and P8 are part of T5's full one-post-Newtonian assembly, but the leading Shapiro delay coefficient does not require $\beta=1$.

## Summary

T8 derives the weak-field Shapiro delay from the framework's assembled static exterior metric.

From T5, the leading null metric is

$$ds^2=-\left(1-\frac{2U}{c^2}\right)c^2dt^2+\left(1+2\frac{U}{c^2}\right)d\ell^2.$$

Setting $ds^2=0$ gives the effective optical index

$$n(r)=1+2\frac{U(r)}{c^2}.$$

The excess one-way travel time is

$$\Delta t_{\text{one-way}}=\frac{1}{c}\int(n-1)d\ell=\frac{2GM}{c^3}\int_{-z_1}^{z_2}\frac{dz}{\sqrt{b^2+z^2}}.$$

Evaluating the integral gives

$$\Delta t_{\text{one-way}}=\frac{2GM}{c^3}\ln\left(\frac{(z_2+r_2)(z_1+r_1)}{b^2}\right).$$

For $r_1,r_2\gg b$,

$$\Delta t_{\text{one-way}}\approx\frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

The result depends on the spatial-response coefficient $\gamma=1$ supplied by T3. This is the theorem that shows the framework recovers the full weak-field Shapiro delay rather than the half-delay produced by temporal gravity alone.