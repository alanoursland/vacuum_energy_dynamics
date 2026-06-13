# Summary: Weak-Field GR Recovery

## What This Document Is

This document summarizes how the framework recovers the standard
weak-field tests of general relativity in the static, source-free
exterior regime.

It is not a theorem and does not introduce new commitments. It records
the current dependency chain after the field-equation closure:

- P7 is no longer a standalone recovery postulate; its $AB=1$ content is
  the metric shadow of adopted P7'.
- The former P8 temporal-composition rule is no longer a standalone
  recovery postulate; it is a theorem under P9 plus the C2 static
  bootstrap.
- The weak-field recoveries are also corollaries of the full field
  equations in `04_field_equations/`.

## Recovery Scope

The recovery described here applies to static, source-free exterior weak
fields around localized mass constraints. It assumes weak field,
asymptotic flatness, and the exterior Newtonian potential magnitude

$$U(r)=\frac{GM}{r}.$$

It does not apply by itself to strong fields, interiors, rotating
sources, radiating systems, nonspherical dynamical fields, or cosmology.

## Core Chain

P1-P6 provide the ontology and interaction rules:

- vacuum is energy;
- vacuum configuration is spacetime;
- vacuum density is locally constant;
- curvature is spatial differential vacuum extent;
- curvature configurations carry energy;
- energy in gradients exchanges with the vacuum.

The static exterior weak-field recovery then uses two derived exterior
results:

- **T3:** P7' gives the static frame-indifference shadow $AB=1$, which
  supplies $\gamma=1$.
- **T4:** P9 plus the C2 bootstrap gives multiplicative temporal
  composition, which supplies $\beta=1$.

The compact dependency structure is

$$P7' \rightarrow T3 \rightarrow \gamma=1,$$

and

$$P9 + C2 \rightarrow T4 \rightarrow \beta=1.$$

Then

$$T3+T4\rightarrow T5,$$

and

$$T5\rightarrow T6,T7,T8,T9.$$

## Theorem Chain

### T1: Gravitational Redshift

T1 derives the weak-field gravitational redshift formula

$$\frac{\Delta E}{E}\approx-\frac{gh}{c^2}.$$

### T2: Gravitational Time Dilation

T2 derives observer-level gravitational time dilation from T1.

### T3: Reciprocal Exterior Scaling

T3 derives

$$A(r)B(r)=1,$$

from P7' through its static exterior metric shadow. In weak-field PPN
language this gives

$$\gamma=1.$$

### T4: Second-Order Temporal Self-Coupling

T4 derives the second-order temporal coefficient from the P9+C2
temporal-composition theorem:

$$d\ln\alpha=-\frac{dU}{c^2}+O(c^{-6}).$$

With asymptotic flatness,

$$-g_{tt}=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}),$$

so

$$\beta=1.$$

### T5: Static Exterior Weak-Field Metric

T5 assembles T1 through T4 into the static exterior weak-field metric:

$$ds^2=-\left(1-\frac{2U}{c^2}+2\frac{U^2}{c^4}\right)c^2dt^2+\left(1+2\frac{U}{c^2}\right)d\vec{x}^{\,2}+O(c^{-6})_{tt}+O(c^{-4})_{ij}.$$

### T6: Newtonian Limit

T6 shows that slow massive test bodies in the T5 metric obey

$$\frac{d^2\mathbf{x}}{dt^2}=\nabla U,$$

which gives Newton's inverse-square acceleration for $U=GM/r$.

### T7: Light Deflection

T7 derives

$$\Delta\theta=\frac{4GM}{bc^2}.$$

The leading coefficient depends on $1+\gamma$, with $\gamma=1$ supplied
by T3.

### T8: Shapiro Delay

T8 derives the leading one-way Shapiro delay

$$\Delta t_{\text{one-way}}\approx\frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

Like light deflection, the leading delay depends on $1+\gamma$.

### T9: Perihelion Precession

T9 derives

$$\Delta\varpi=\frac{6\pi GM}{a(1-e^2)c^2}.$$

In PPN form,

$$\Delta\varpi=(2+2\gamma-\beta)\frac{2\pi GM}{a(1-e^2)c^2}.$$

Using T3 and T4 gives $\gamma=1$ and $\beta=1$, hence the standard
weak-field result.

## Recovered Results

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

## Status

The framework recovers the standard static exterior weak-field tests
through one post-Newtonian order from the modern dependency chain:

```text
P7' -> T3 -> gamma = 1
P9 + C2 -> T4 -> beta = 1
T3 + T4 -> T5 -> T6-T9
```

The older statement "conditional on P7 and P8" is retired. The current
reading is "conditional on P7' and P9+C2," with the full
field-equation derivation making these weak-field results corollaries
of the closed response law.
