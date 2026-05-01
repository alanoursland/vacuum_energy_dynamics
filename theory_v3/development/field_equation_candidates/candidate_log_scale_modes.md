# Candidate: Log-Scale Exterior Modes

## What This Document Is

This document is a speculative development note.

It is not a postulate, theorem, proof, field equation, or empirical consequence. It does not add a new commitment to the framework. Its purpose is to explore a possible mathematical language for developing the future static exterior field equation.

The central idea is that the static exterior temporal and radial metric factors may be easier to reason about in logarithmic scale variables. In those variables, P7 and P8 take especially simple forms:

```text
P7 / exterior compensation:
  temporal log-scale + radial log-scale = 0

P8 / temporal self-coupling:
  temporal log-scale changes add by logarithmic composition
```

This note asks whether a future configuration-energy functional could make those two structures natural, rather than leaving them as independent exterior postulates.

Suggested file location:

```text
04_development/field_equation_candidates/candidate_log_scale_exterior_modes.md
```

This file belongs in development. It should not be placed in the postulate chain or theorem chain.

---

## Motivation

The current framework has a formal weak-field recovery chain.

P7 states that in a static, source-free exterior vacuum configuration, temporal and radial distortions compensate. In spherical symmetry, using metric-coefficient notation,

$$A(r)B(r)=1.$$

T3 then derives reciprocal exterior scaling from P7 and identifies the weak-field spatial-response value

$$\gamma=1.$$

P8 states that in a static, source-free exterior weak field, temporal mappings compose multiplicatively. In temporal scale-factor notation,

$$\alpha(r)=\sqrt{-g_{tt}(r)},$$

P8 gives

$$d\ln\alpha=-\frac{dU}{c^2}+O(c^{-6}).$$

T4 then derives

$$-g_{tt}=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}),$$

and therefore

$$\beta=1.$$

The weak-field theorem chain works. But the future theory still needs a deeper reason why P7 and P8 hold in the static exterior limit.

This note explores one possible path: rewrite the static exterior metric in log-scale variables and treat P7 and P8 as statements about exterior modes.

---

## Static Spherical Exterior Setup

Consider a static, spherically symmetric exterior metric in areal-radius form:

$$ds^2=-A(r)c^2dt^2+B(r)dr^2+r^2d\Omega^2.$$

Here:

- $A(r)$ is the temporal metric coefficient.
- $B(r)$ is the radial spatial metric coefficient.
- $r$ is the areal radius, so spheres at radius $r$ have area $4\pi r^2$.
- The angular sector is fixed by the coordinate convention.
- The source-free exterior freedom lies in the temporal and radial factors.

Asymptotic flatness gives

$$A(r)\to1,$$

and

$$B(r)\to1,$$

as

$$r\to\infty.$$

P7 states that in the static source-free exterior,

$$A(r)B(r)=1.$$

The log-scale language rewrites this relation in a way that may be more natural for field-equation design.

---

## Log-Scale Variables

Define the temporal log-scale variable

$$\psi(r)=\frac{1}{2}\ln A(r).$$

Since

$$\alpha(r)=\sqrt{A(r)}=\sqrt{-g_{tt}(r)},$$

this is also

$$\psi(r)=\ln\alpha(r).$$

Define the radial log-scale variable

$$\chi(r)=\frac{1}{2}\ln B(r).$$

Then

$$A(r)=e^{2\psi(r)},$$

and

$$B(r)=e^{2\chi(r)}.$$

Flat exterior vacuum corresponds to

$$\psi=0,$$

and

$$\chi=0.$$

The metric becomes

$$ds^2=-e^{2\psi(r)}c^2dt^2+e^{2\chi(r)}dr^2+r^2d\Omega^2.$$

This is only a change of variables in the static spherical exterior. It is not a new metric ansatz for the general theory.

---

## P7 in Log-Scale Form

P7 says

$$A(r)B(r)=1.$$

Using

$$A=e^{2\psi},$$

and

$$B=e^{2\chi},$$

we get

$$e^{2\psi}e^{2\chi}=1.$$

Therefore,

$$e^{2(\psi+\chi)}=1.$$

Assuming real exterior scale factors, this gives

$$\psi+\chi=0.$$

So P7 becomes:

$$\chi=-\psi.$$

In log-scale language, static exterior compensation says that the radial log-scale mode cancels the temporal log-scale mode.

This is suggestive. Instead of treating P7 only as a product rule, we can treat it as a statement that a particular exterior mode vanishes:

$$\sigma(r)=\psi(r)+\chi(r)=0.$$

Call this the uncompensated exterior measure mode.

Then P7 says:

```text
In a static, source-free exterior with no net vacuum substance exchange, the uncompensated measure mode vanishes.
```

The remaining exterior distortion is then the compensated mode.

---

## Compensated and Uncompensated Modes

The variables

$$\psi$$

and

$$\chi$$

can be recombined into two mode variables.

Define the uncompensated mode:

$$\sigma=\psi+\chi.$$

Define the compensated mode:

$$\eta=\psi-\chi.$$

Then

$$\psi=\frac{1}{2}(\sigma+\eta),$$

and

$$\chi=\frac{1}{2}(\sigma-\eta).$$

P7 sets

$$\sigma=0$$

in the static source-free exterior.

When

$$\sigma=0,$$

we have

$$\psi=\frac{\eta}{2},$$

and

$$\chi=-\frac{\eta}{2}.$$

Equivalently,

$$\chi=-\psi.$$

This decomposition may be useful because the two modes have different physical interpretations.

The uncompensated mode $\sigma$ changes the temporal-radial product. It represents a failure of temporal and radial distortions to compensate.

The compensated mode $\eta$ changes temporal and radial scales oppositely. It represents exterior curvature as redistribution rather than net substance exchange.

In framework language:

```text
sigma ≠ 0:
  possible substance-regime or source/interior behavior

sigma = 0:
  source-free exterior configuration-regime compensation

eta:
  remaining compensated exterior curvature mode
```

This is speculative, but it gives a clean candidate mathematical meaning to P7.

---

## P8 in Log-Scale Form

P8 is already naturally logarithmic.

The temporal scale factor is

$$\alpha=\sqrt{-g_{tt}}=\sqrt{A}=e^\psi.$$

Therefore,

$$\ln\alpha=\psi.$$

P8 states that in a static, source-free exterior weak field,

$$d\ln\alpha=-\frac{dU}{c^2}+O(c^{-6}).$$

In the present notation, this is simply

$$d\psi=-\frac{dU}{c^2}+O(c^{-6}).$$

With asymptotic flatness,

$$\psi(\infty)=0,$$

and

$$U(\infty)=0.$$

So integration gives

$$\psi(r)=-\frac{U(r)}{c^2}+O(c^{-6}).$$

Then

$$A(r)=e^{2\psi(r)}=e^{-2U/c^2+O(c^{-6})}.$$

Expanding through second order,

$$A(r)=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}).$$

Since

$$A=-g_{tt},$$

this is the T4 temporal result.

Thus P8 is not merely compatible with log-scale variables; it is almost written in them already.

---

## Why Logarithms Are Natural Here

Logarithms appear naturally when local scale factors compose multiplicatively.

If two neighboring exterior shells contribute temporal scale factors

$$\alpha_1$$

and

$$\alpha_2,$$

then the total temporal scale factor is

$$\alpha_{\text{total}}=\alpha_1\alpha_2.$$

Taking the logarithm gives

$$\ln\alpha_{\text{total}}=\ln\alpha_1+\ln\alpha_2.$$

So multiplicative composition becomes additive in log-scale variables.

This is exactly the structure P8 uses. Temporal distortion is not an additive offset against an undistorted background. It is a scale factor that compounds through the exterior configuration.

The log variable

$$\psi=\ln\alpha$$

is therefore the natural variable for temporal self-coupling.

The same reasoning may apply to radial scaling. The radial scale factor is

$$\sqrt{B}=e^\chi.$$

So radial scale distortions also compose naturally through

$$\chi=\ln\sqrt{B}.$$

This suggests that the static exterior configuration may be better represented by log-scale modes than by raw metric coefficients.

---

## Relation to Vacuum Amount

P3 says that vacuum energy density is finite and locally constant. P3a says curvature is differential vacuum amount, not variation in density. P7 says that in static source-free exteriors, curvature is compensated directional redistribution rather than net substance exchange.

In log-scale language, the temporal-radial product

$$A B=e^{2(\psi+\chi)}=e^{2\sigma}$$

is a simple proxy for temporal-radial measure change in the exterior spherical sector.

If

$$\sigma=0,$$

then the temporal-radial product is preserved.

This gives a possible formal reading of exterior compensation:

```text
Static source-free exterior curvature carries compensated directional distortion.
The compensated mode changes temporal and radial scales oppositely.
The uncompensated mode is suppressed or absent outside sources.
```

This may be the seed of a future field-equation condition.

But caution is required. The full vacuum measure in a Lorentzian spacetime involves the determinant of the metric, coordinate conventions, and the angular sector. In areal-radius coordinates, the angular part has already been fixed. Therefore $\sigma$ should not be overinterpreted as a full invariant volume mode.

The safer statement is:

```text
In the restricted static spherical exterior sector, psi + chi captures the temporal-radial compensation condition expressed by P7.
```

---

## Candidate Configuration-Energy Interpretation

A future configuration-energy functional might assign a high cost to uncompensated exterior distortion in source-free regions.

In log-scale variables, a toy exterior penalty could take the form

$$E_{\sigma}\sim\int w(r)\left[\sigma(r)\right]^2dr,$$

or

$$E_{\nabla\sigma}\sim\int w(r)\left[\frac{d\sigma}{dr}\right]^2dr.$$

Here $w(r)$ is a positive weight determined by the proper radial measure, angular area, and whatever density factors the final theory requires.

If the source-free exterior minimization drives

$$\sigma\to0,$$

then P7 would arise as an exterior minimum-energy condition.

This is only a toy. It is not a proposed field equation.

But it suggests a route:

```text
P7 may follow if source-free exterior vacuum strongly suppresses uncompensated temporal-radial measure distortion.
```

The compensated mode $\eta$ would remain available to encode the actual exterior gravitational field.

---

## Candidate Exterior Mode Functional

One can imagine a reduced static spherical exterior energy of the schematic form

$$E_{\text{ext}}[\sigma,\eta]
=
\int dr\,w(r)
\left[
K_\sigma(\sigma')^2
+
M_\sigma^2\sigma^2
+
K_\eta(\eta')^2
+
V_\eta(\eta)
+
C(\sigma,\eta)
\right].
$$

Here:

- $\sigma=\psi+\chi$ is the uncompensated mode.
- $\eta=\psi-\chi$ is the compensated mode.
- $K_\sigma$ and $K_\eta$ are stiffness-like coefficients.
- $M_\sigma^2$ represents a cost for uncompensated exterior distortion.
- $V_\eta$ represents the allowed exterior gravitational configuration.
- $C(\sigma,\eta)$ represents possible coupling between the modes.

If the source-free exterior equations force

$$\sigma=0,$$

then the exterior solution obeys P7.

The remaining equation for $\eta$ would determine the exterior potential profile.

In the weak-field point-mass limit, that profile must reduce to

$$U(r)=\frac{GM}{r}.$$

This toy suggests a possible separation of tasks:

```text
sigma equation:
  derive exterior compensation / P7

eta equation:
  derive source profile / Newtonian potential

temporal composition rule:
  derive P8 / temporal self-coupling
```

The challenge is to produce these from a covariant Lorentzian field equation rather than a coordinate-specific toy functional.

---

## Relation to the Source Law

The current weak-field theorem chain uses the Newtonian exterior potential

$$U(r)=\frac{GM}{r}.$$

The framework has not yet derived this source law from mass-as-constraint dynamics.

In the log-scale exterior language, the source-law problem becomes:

```text
What boundary or constraint condition imposed by mass produces the exterior compensated mode eta(r) corresponding to U(r)=GM/r?
```

Since

$$\psi=-\frac{U}{c^2}$$

and, under P7,

$$\chi=\frac{U}{c^2},$$

we have

$$\eta=\psi-\chi=-2\frac{U}{c^2}.$$

For a point-mass weak field,

$$\eta(r)=-\frac{2GM}{rc^2}.$$

So the source-law target can be written as:

$$\eta(r)\propto-\frac{1}{r}.$$

That suggests a Laplace-like exterior equation:

$$\nabla^2\eta=0$$

outside the source, with a source/boundary condition at the mass.

This is unsurprising, but useful. It separates two questions:

1. Why does the exterior compensated mode obey a harmonic equation in the weak-field limit?
2. What mass constraint fixes the coefficient as $GM/c^2$?

A future field equation must answer both.

---

## Relation to Vacuum Burden Reduction

The burden-reduction idea says that mass imposes a cost on the vacuum, and that gravitational attraction may arise because systems evolve toward lower total vacuum burden.

In log-scale exterior variables, burden might be expressible as the cost of sustaining exterior modes and source-interface conditions.

Schematic burden functional:

$$E_{\text{burden}}=E_{\text{interface}}+E_{\sigma}+E_{\eta}+E_{\text{substance}}+\cdots.$$

For a single isolated mass, the exterior burden includes the cost of sustaining the compensated mode

$$\eta(r)\sim-\frac{2GM}{rc^2}.$$

For multiple masses, the combined exterior mode is not simply two isolated burdens pasted together. The total configuration may relax into a lower-burden arrangement.

This gives a possible mathematical version of the burden-reduction mechanism:

```text
Matter imposes boundary/interface conditions.
The exterior vacuum solves a minimum-burden mode equation.
Motion occurs because changing matter separation changes the minimum exterior burden.
The force is the gradient of that minimized burden with respect to matter configuration.
```

In schematic form,

$$F_R=-\frac{dE_{\text{burden,min}}(R)}{dR}.$$

This remains speculative. The immediate value is that log-scale variables may provide a compact way to express what burden is in the static exterior sector.

---

## Relationship to the Graph Model

The informal graph model pictures vacuum as a relational structure.

In that picture:

- substance energy belongs to vacuum amount itself,
- configuration energy belongs to arrangement,
- curvature is directional variation in arrangement,
- flat vacuum is relaxed minimum configuration,
- and mass imposes constraints that disturb the relaxed configuration.

The log-scale exterior variables are the smooth-manifold version of a very small piece of that picture.

The temporal log-scale $\psi$ and radial log-scale $\chi$ are not graph quantities. But they play a similar conceptual role: they track how local relations are stretched or compressed in different directions.

The compensated mode $\eta$ resembles an arrangement distortion that preserves a local exterior measure.

The uncompensated mode $\sigma$ resembles a net measure distortion that may be forbidden or suppressed in source-free exterior configuration-regime behavior.

This connection should remain heuristic. The graph model is not part of the formal theory.

---

## Relationship to Lorentzian Manifold Language

The smooth Lorentzian manifold is the intended formal home for future development.

In that language, the metric $g_{\mu\nu}$ is the vacuum configuration. The log-scale variables $\psi$ and $\chi$ are not fundamental fields. They are symmetry-reduced variables extracted from $g_{\mu\nu}$ in a static spherical exterior.

Therefore this document should not be read as proposing a general two-scalar theory.

The correct hierarchy is:

```text
General theory:
  Lorentzian metric g_{\mu\nu}, possibly with additional substance/exchange variables.

Static spherical exterior reduction:
  metric coefficients A(r), B(r).

Log-scale exterior variables:
  psi = 1/2 ln A,
  chi = 1/2 ln B.

Mode decomposition:
  sigma = psi + chi,
  eta = psi - chi.
```

This hierarchy protects the framework from scalar-metric collapse.

---

## Avoiding the Scalar-Metric Trap

There is a dangerous shortcut.

Since P8 gives

$$\psi=-\frac{U}{c^2},$$

and P7 gives

$$\chi=\frac{U}{c^2},$$

one might write

$$A=e^{-2U/c^2},$$

and

$$B=e^{2U/c^2},$$

then declare a universal scalar exponential metric.

That would be a mistake.

The current framework does not say that every metric component in every physical regime is generated by one scalar potential. It only says that in a static source-free exterior weak field, the temporal self-coupling and reciprocal compensation conditions recover the needed coefficients.

The scalar exponential form is, at most, a restricted exterior weak-field guide. It should not be promoted into a global metric ansatz.

Why not?

Because P3a and P4 require directional/tensor-like structure. General curvature cannot be represented by one scalar value at each point. Rotating sources, gravitational waves, nonspherical fields, shear modes, frame dragging, and cosmology all require structure beyond a single scalar exterior potential.

Therefore:

```text
Use log-scale variables as a reduced-sector tool.
Do not turn them into a universal scalar theory.
```

---

## Relationship to P7 and P8

This document does not replace P7 or P8.

P7 and P8 are current postulates of the framework. They are part of the formal theory.

This document asks how those postulates might eventually become consequences of a deeper field equation.

Possible future derivation targets:

```text
Derive P7:
  Show that source-free exterior minimization suppresses sigma = psi + chi,
  leaving AB = 1.

Derive P8:
  Show that temporal scale distortions compose in log-scale form,
  giving d psi = -dU/c^2 through one-post-Newtonian order.

Derive source law:
  Show that mass constraints generate eta(r) ∝ -1/r in the weak-field exterior.
```

If all three targets were achieved, the static exterior weak-field recovery spine would become much deeper:

```text
configuration-energy functional
  -> exterior mode equations
  -> P7/P8 behavior
  -> T3/T4
  -> T5
  -> T6-T9
```

---

## Candidate Field-Equation Questions

This log-scale exploration suggests several concrete questions.

### 1. What is the covariant parent of sigma?

In the static spherical exterior,

$$\sigma=\psi+\chi.$$

But a general theory cannot depend on this coordinate-specific variable.

Question:

```text
What covariant or gauge-controlled geometric quantity reduces to psi + chi in the static spherical exterior?
```

Possibilities include:

- determinant-related modes of the metric,
- trace modes of spatial-temporal deformation,
- lapse-radial combinations in a chosen exterior gauge,
- constrained measure modes,
- or some decomposition of metric perturbations into trace and transverse parts.

### 2. What is the covariant parent of eta?

In the static spherical exterior,

$$\eta=\psi-\chi.$$

Question:

```text
What general geometric structure reduces to the compensated exterior gravitational mode eta?
```

Possibilities include:

- trace-free radial-temporal distortion,
- Weyl-like exterior curvature content,
- tidal/distortion modes,
- or the scalar potential mode that appears only after imposing high symmetry.

### 3. Why should sigma vanish outside sources?

P7 says the static source-free exterior has

$$\sigma=0.$$

Question:

```text
Is sigma forbidden by constant-density exterior compensation,
dynamically suppressed by a high energy cost,
eliminated by a constraint equation,
or removable by gauge after physical conditions are imposed?
```

These are different possibilities. They should not be conflated.

### 4. Why should psi obey logarithmic potential response?

P8 says

$$d\psi=-\frac{dU}{c^2}+O(c^{-6}).$$

Question:

```text
Does this follow from multiplicative temporal scale composition alone,
from a temporal configuration-energy term,
from local SR plus redshift,
or from a deeper stationarity condition?
```

### 5. What fixes the exterior 1/r profile?

In weak-field point-mass form,

$$\eta(r)=-\frac{2GM}{rc^2}.$$

Question:

```text
Does eta obey a Laplace equation outside sources?
If so, what source constraint fixes the coefficient?
```

### 6. How does burden reduction appear in mode language?

Question:

```text
Can E_burden be written in terms of sigma, eta, interface terms, and substance exchange?
Can attraction be derived as motion toward lower minimized burden?
```

### 7. What changes in nonspherical or rotating cases?

Question:

```text
What replaces psi, chi, sigma, and eta when the exterior is not static and spherical?
Which additional tensor modes appear?
How does the framework avoid losing gravitational-wave and frame-dragging content?
```

---

## A Minimal Toy Program

A minimal toy development program could proceed as follows.

### Step 1: Work in static spherical symmetry

Use

$$ds^2=-e^{2\psi(r)}c^2dt^2+e^{2\chi(r)}dr^2+r^2d\Omega^2.$$

Define

$$\sigma=\psi+\chi,$$

and

$$\eta=\psi-\chi.$$

### Step 2: Impose source-free exterior compensation as a target

Require that the exterior equations drive or constrain

$$\sigma=0.$$

This reproduces P7.

### Step 3: Derive or model the weak-field exterior mode

Assume or derive a weak-field exterior equation

$$\nabla^2\eta=0$$

outside the source.

For a localized mass, choose boundary conditions giving

$$\eta=-\frac{2GM}{rc^2}.$$

Then

$$\psi=-\frac{GM}{rc^2},$$

and

$$\chi=\frac{GM}{rc^2}.$$

This recovers the first-order exterior metric.

### Step 4: Build temporal self-coupling into the log variable

Let the temporal scale compose through

$$\psi=\ln\alpha.$$

Then the second-order temporal coefficient follows from exponentiating

$$\alpha=e^\psi.$$

If

$$\psi=-\frac{U}{c^2},$$

then

$$-g_{tt}=A=e^{2\psi}=e^{-2U/c^2}.$$

Through second order,

$$-g_{tt}=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}).$$

This reproduces P8/T4 behavior in the weak-field exterior.

### Step 5: Do not overclaim

This toy program would not yet derive the full theory.

It would not solve:

- covariant generalization,
- source law from mass-as-constraint,
- strong-field behavior,
- rotating sources,
- gravitational waves,
- cosmology,
- vacuum substance exchange,
- or the full configuration-energy functional.

It would only sharpen the static spherical exterior target.

---

## Potential Failure Modes

### 1. Coordinate Artifact

The variables $\psi$ and $\chi$ depend on the chosen static spherical coordinate form. If the future theory treats them as fundamental, it risks mistaking a coordinate reduction for physical ontology.

Mitigation:

```text
Treat psi and chi as reduced variables extracted from the metric in a chosen exterior gauge.
Search for covariant parent quantities before promoting anything.
```

### 2. Scalar Collapse

The exterior weak field can be written using one potential $U$. This might tempt one to define the whole theory by a scalar potential.

Mitigation:

```text
Keep the log-scale model explicitly restricted to static spherical exteriors.
Preserve tensorial/directional structure in the general theory.
```

### 3. Re-importing GR

If the configuration-energy functional is simply chosen to be the Einstein-Hilbert action without explanation, the framework risks becoming GR with altered vocabulary.

Mitigation:

```text
Use GR as a comparison target, not as an unexplained primitive.
Ask which vacuum-energy principles select a GR-like functional or where they predict deviations.
```

### 4. No Source Law

Even if sigma = 0 is derived, the exterior field profile still needs a source law.

Mitigation:

```text
Develop mass-as-constraint boundary/interface conditions alongside exterior mode equations.
```

### 5. Misreading P8 as Exact Exponential Metric

P8 fixes the temporal weak-field behavior through the needed order. It does not assert an exact all-orders expression.

Mitigation:

```text
Use exponential/log language as a composition tool, not as an all-orders strong-field claim.
```

---

## What Would Count as Progress?

This development direction would make progress if it produced any of the following.

### Weak progress

A clearer reduced-variable language for P7 and P8:

$$\sigma=0,$$

and

$$d\psi=-\frac{dU}{c^2}+O(c^{-6}).$$

### Medium progress

A toy exterior energy functional whose minimum gives

$$\sigma=0,$$

and whose weak-field compensated mode obeys a Laplace-like equation outside sources.

### Strong progress

A covariant configuration-energy functional whose static source-free exterior reduction yields P7 and P8.

### Very strong progress

A complete field equation that:

- derives P7 and P8 in their appropriate limits,
- derives the weak-field source law,
- recovers T5 through T9,
- predicts strong-field behavior,
- handles rotating and dynamical configurations,
- and accounts for substance-regime exchange.

---

## Summary

This note explores log-scale variables for the static spherical exterior:

$$\psi=\frac{1}{2}\ln A,$$

and

$$\chi=\frac{1}{2}\ln B.$$

In these variables, P7 becomes

$$\psi+\chi=0,$$

and P8 becomes

$$d\psi=-\frac{dU}{c^2}+O(c^{-6}).$$

This suggests a mode decomposition:

$$\sigma=\psi+\chi,$$

and

$$\eta=\psi-\chi.$$

The uncompensated mode $\sigma$ may represent source/interior/substance-regime distortion or exterior measure imbalance. Static source-free exterior compensation suppresses it.

The compensated mode $\eta$ carries the exterior gravitational distortion. In the weak-field point-mass limit,

$$\eta=-\frac{2GM}{rc^2}.$$

The speculative research target is to find a configuration-energy functional or field equation in which these structures emerge naturally.

This document does not solve that problem. It sharpens it.
