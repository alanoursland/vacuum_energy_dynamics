# Summary: Weak-Field GR Recovery

## What This Document Is

This document summarizes how the framework recovers the standard weak-field tests of general relativity in the static, source-free exterior regime.

It is not a theorem and does not introduce new commitments. It is an organizational summary of the postulates and theorems that together establish weak-field recovery.

The recovery is conditional on the current exterior structural postulates:

- P7: Static Exterior Vacuum Compensation
- P8: Static Exterior Temporal Self-Coupling

The framework's position is that P7 and P8 are localized exterior recovery constraints. They are not full field equations. A future configuration-energy functional or field equation should derive them rather than merely assume them.

---

## Recovery Scope

The recovery described here applies to static, source-free exterior weak fields around localized mass constraints.

The assumptions are:

1. The source is localized.
2. The region considered is outside the matter source.
3. The exterior field is static.
4. The field is weak, so $U/c^2 \ll 1$.
5. The metric is asymptotically flat.
6. The exterior Newtonian potential magnitude is used in the weak-field limit.

For a point mass,

$$U(r)=\frac{GM}{r}.$$

This recovery does not apply automatically to strong fields, interiors, rotating sources, radiating systems, nonspherical dynamical fields, or cosmology.

---

## Core Conceptual Structure

The weak-field recovery rests on two layers.

The first layer is the foundational ontology and dynamics:

- P1 identifies vacuum with energy.
- P2 identifies vacuum with spacetime.
- P3 makes vacuum energy density finite and locally constant.
- P3a identifies curvature with differential vacuum extent.
- P4 says curvature/configuration carries energy.
- P5 says vacuum seeks constrained minimum-energy configurations.
- P6 says energy in curvature gradients experiences force uniformly per unit energy, with kinetic changes sourced or sunk by vacuum exchange.

This layer gives the framework its physical interpretation of gravity: gravitational phenomena are vacuum-configuration phenomena.

The second layer is the static exterior recovery structure:

- P7 states that static source-free exterior curvature is compensated temporal-radial redistribution rather than net vacuum substance exchange.
- P8 states that static source-free exterior temporal distortion self-couples by multiplicative composition.

This second layer supplies the currently adopted exterior constraints needed to recover the weak-field metric.

---

## The Theorem Chain

### T1: Gravitational Redshift

T1 derives the weak-field gravitational redshift formula:

$$\frac{\Delta E}{E}\approx-\frac{gh}{c^2}.$$

Framework interpretation: a photon climbing through a curvature gradient loses energy, and the lost energy is matched by vacuum creation. A photon descending through the gradient gains energy, sourced by vacuum destruction.

T1 establishes the first-order temporal energy-shift side of weak-field gravity.

---

### T2: Gravitational Time Dilation

T2 derives gravitational time dilation from T1:

$$\tau_A^{(B)}\approx\tau\left(1+\frac{gh}{c^2}\right).$$

Framework interpretation: clock-rate differences are observer-to-observer mappings produced by the vacuum configuration between the clocks. Local clocks do not locally run slow; the mapping between local rates differs across the curvature gradient.

T2 establishes the first-order temporal clock-rate side of weak-field gravity.

---

### T3: Reciprocal Exterior Scaling

T3 derives reciprocal temporal-radial scaling from P7:

$$A(r)B(r)=1.$$

In weak-field PPN language, this gives

$$\gamma=1.$$

Framework interpretation: in a static source-free exterior, curvature is compensated redistribution of vacuum extent, not net vacuum substance exchange. Temporal and radial distortions compensate.

T3 supplies the spatial-response side of weak-field recovery.

---

### T4: Second-Order Temporal Self-Coupling

T4 derives the second-order temporal coefficient from P8.

Writing

$$\alpha(r)=\sqrt{-g_{tt}(r)},$$

P8 gives

$$d\ln\alpha=-\frac{dU}{c^2}+O(c^{-6}).$$

With asymptotic flatness, T4 derives

$$-g_{tt}=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}).$$

Comparing with the PPN form,

$$-g_{tt}=1-\frac{2U}{c^2}+2\beta\frac{U^2}{c^4}+O(c^{-6}),$$

gives

$$\beta=1.$$

Framework interpretation: temporal distortion is part of the exterior vacuum configuration and composes multiplicatively. The second-order temporal term comes from self-coupling of the first-order temporal distortion, not from a universal scalar metric ansatz.

T4 supplies the nonlinear temporal side of weak-field recovery.

---

### T5: Static Exterior Weak-Field Metric

T5 assembles T1 through T4 into the static exterior weak-field metric.

In PPN-compatible weak-field coordinates,

$$ds^2=-\left(1-\frac{2U}{c^2}+2\frac{U^2}{c^4}\right)c^2dt^2+\left(1+2\frac{U}{c^2}\right)d\vec{x}^{\,2}+O(c^{-6})_{tt}+O(c^{-4})_{ij}.$$

Equivalently,

$$-g_{tt}=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}),$$

and

$$g_{ij}=\left(1+2\frac{U}{c^2}\right)\delta_{ij}+O(c^{-4}).$$

T5 is the bridge theorem. It packages the recovered static exterior weak-field geometry so downstream proofs do not re-import a metric assumption independently.

---

### T6: Newtonian Limit

T6 shows that slow massive test bodies in the T5 metric obey Newtonian gravitational acceleration.

Using the positive potential magnitude $U=GM/r$,

$$\frac{d^2\mathbf{x}}{dt^2}=\nabla U.$$

For a point mass,

$$\nabla U=-\frac{GM}{r^2}\hat{\mathbf{r}},$$

so

$$\frac{d^2\mathbf{x}}{dt^2}=-\frac{GM}{r^2}\hat{\mathbf{r}}.$$

This recovers Newton's inverse-square gravitational acceleration.

T6 also shows consistency between the framework's force-language in P6 and the metric-language assembled in T5.

---

### T7: Light Deflection

T7 derives the leading weak-field light-deflection angle:

$$\Delta\theta=\frac{4GM}{bc^2}.$$

In PPN form,

$$\Delta\theta=(1+\gamma)\frac{2GM}{bc^2}.$$

Since T3 gives $\gamma=1$,

$$\Delta\theta=\frac{4GM}{bc^2}.$$

Light deflection is primarily a test of the spatial-response side of the framework. Without T3/P7, the framework would recover only the temporal half of the deflection.

---

### T8: Shapiro Delay

T8 derives the leading weak-field Shapiro delay.

For a one-way signal passing the mass with impact parameter $b$, emitted from radial distance $r_1$ and received at radial distance $r_2$,

$$\Delta t_{\text{one-way}}\approx\frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

For a round-trip radar signal,

$$\Delta t_{\text{round-trip}}\approx\frac{4GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

In PPN language, Shapiro delay depends on $1+\gamma$. Since T3 gives $\gamma=1$, the framework recovers the full general-relativistic weak-field delay.

Like light deflection, Shapiro delay tests the spatial-response side of the framework.

---

### T9: Perihelion Precession

T9 derives the weak-field perihelion advance:

$$\Delta\varpi=\frac{6\pi GM}{a(1-e^2)c^2}.$$

In PPN form,

$$\Delta\varpi=(2+2\gamma-\beta)\frac{2\pi GM}{a(1-e^2)c^2}.$$

Using T3 and T4,

$$\gamma=1,$$

and

$$\beta=1.$$

Therefore,

$$2+2\gamma-\beta=3,$$

so

$$\Delta\varpi=\frac{6\pi GM}{a(1-e^2)c^2}.$$

Perihelion precession is the combined weak-field test. It depends on both the spatial-response condition from P7/T3 and the temporal self-coupling condition from P8/T4.

---

## Summary of Recovered Results

The framework recovers the following weak-field results in the static source-free exterior regime:

| Result | Framework theorem | Key recovered structure |
|---|---:|---|
| Gravitational redshift | T1 | First-order temporal energy shift |
| Gravitational time dilation | T2 | First-order temporal clock-rate mapping |
| Reciprocal exterior scaling | T3 | $\gamma=1$ |
| Second-order temporal coefficient | T4 | $\beta=1$ |
| Static exterior weak-field metric | T5 | Assembled PPN-compatible metric |
| Newtonian acceleration | T6 | $\mathbf{a}=\nabla U$ |
| Light deflection | T7 | $\Delta\theta=4GM/(bc^2)$ |
| Shapiro delay | T8 | Standard leading logarithmic delay |
| Perihelion precession | T9 | $\Delta\varpi=6\pi GM/[a(1-e^2)c^2]$ |

---

## What Depends on What

The dependency structure is:

P1 through P6 provide the core ontology and interaction rules.

P7 supplies the exterior compensation principle.

T3 derives reciprocal exterior scaling and $\gamma=1$ from P7.

P8 supplies the exterior temporal self-coupling principle.

T4 derives $\beta=1$ from P8.

T5 assembles the static exterior weak-field metric from T1, T2, T3, and T4.

T6 through T9 derive the standard weak-field tests from T5.

More compactly:

$$P7\rightarrow T3\rightarrow \gamma=1,$$

and

$$P8\rightarrow T4\rightarrow \beta=1.$$

Then

$$T3+T4\rightarrow T5,$$

and

$$T5\rightarrow T6,T7,T8,T9.$$

---

## Why P7 and P8 Are Kept Separate

P7 and P8 should not be collapsed into a single scalar metric ansatz.

P7 concerns the relation between temporal and radial spatial mappings in a static source-free exterior. It gives the reciprocal compensation condition that produces $\gamma=1$.

P8 concerns temporal self-coupling in a static source-free exterior. It gives the second-order temporal coefficient that produces $\beta=1$.

These are different recovery conditions. Combining them into a single all-orders scalar exponential metric would repeat a failure mode of the previous version of the framework. A scalar ansatz can reproduce the desired weak-field coefficients algebraically, but it risks erasing the directional and tensor-like structure required by P3a and P4.

The current version keeps the structure factored:

- P7/T3 handles spatial response.
- P8/T4 handles temporal nonlinearity.
- T5 assembles the weak-field metric only after those pieces are independently stated.

This keeps the epistemic structure honest.

---

## What Has Been Recovered

The framework has recovered the standard static exterior weak-field metric through one-post-Newtonian order, conditional on P7 and P8.

In particular, it recovers

$$\gamma=1,$$

and

$$\beta=1.$$

That is enough to reproduce the standard leading weak-field solar-system tests:

- gravitational redshift,
- gravitational time dilation,
- Newtonian acceleration,
- light deflection,
- Shapiro delay,
- perihelion precession.

This gives the framework weak-field empirical viability in the static source-free exterior regime.

---

## What Has Not Been Recovered

This weak-field recovery does not amount to a full derivation of general relativity.

The framework has not yet derived the full field equation.

It has not derived P7 or P8 from a deeper configuration-energy functional.

It has not derived the exact Schwarzschild solution.

It has not derived the strong-field metric.

It has not derived interior solutions.

It has not derived the source law from first principles.

It has not derived rotating solutions or frame dragging.

It has not derived gravitational-wave dynamics.

It has not derived cosmology.

It has not shown that the same recovery structure applies to arbitrary nonspherical or time-dependent configurations.

The recovery is therefore real but scoped.

---

## Field-Equation Design Constraints

P7 and P8 should be understood as design constraints for the future field equation.

A successful future field equation should reproduce P7 in the static source-free exterior limit:

$$A(r)B(r)=1.$$

It should also reproduce P8 in the static source-free exterior weak-field temporal sector:

$$d\ln\alpha=-\frac{dU}{c^2}+O(c^{-6}).$$

Together, these imply

$$\gamma=1,$$

and

$$\beta=1.$$

If the future field equation derives these results, then P7 and P8 can be demoted from postulates to derived exterior consequences. Until then, they remain localized structural commitments.

---

## Status

The framework's weak-field recovery status is:

**Recovered conditionally:** standard static exterior weak-field GR tests through one-post-Newtonian order.

**Conditional on:** P7 and P8.

**Not yet achieved:** derivation of P7 and P8 from the deeper vacuum configuration-energy functional.

The current architecture is therefore best understood as a scaffold.

P1 through P6 define the vacuum ontology and local interaction rules. P7 and P8 state restricted exterior recovery principles. T1 through T9 show that, given those principles, the framework reproduces the standard weak-field exterior tests of general relativity.

The future field equation must explain why P7 and P8 hold.