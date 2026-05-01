# Candidate Boundary Kappa Relaxation Layer

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or complete boundary-layer model. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_boundary_kappa_relaxation_layer.py
```

The guiding question was:

```text
Can nonzero interior kappa relax to exterior kappa=0 without spoiling
the exact exterior compensated branch?
```

The answer is yes, at the level of reduced toy profiles.

The cleanest profile class is:

```text
kappa nonzero inside,
kappa(R)=0,
kappa'(R)=0,
kappa=0 outside.
```

This allows traceful interior response while preserving source-free exterior compensation.

---

## Background

The exact exterior branch requires:

$$\kappa_{\rm ext}=0.$$

Then:

$$AB=1,$$

and:

$$B=\frac1A.$$

With the areal-flux law for:

$$A=e^s,$$

the exterior solution is:

$$A=1-\frac{2GM}{rc^2},$$

and:

$$B=\frac1{1-2GM/(rc^2)}.$$

However, interior matter may source \(\kappa\). The GR interior diagnostic supports this, since:

$$A_{\rm GR}B_{\rm GR}\neq1$$

inside matter but returns to:

$$A_{\rm GR}B_{\rm GR}=1$$

at the surface.

Thus the boundary/interface problem is:

```text
How can kappa be nonzero inside but zero outside?
```

---

## Case 1: Sharp Cutoff

A sharp cutoff profile is:

```text
kappa = k0 inside
kappa = 0 outside
```

This enforces exterior compensation.

But it creates a jump or derivative singularity at the boundary.

Interpretation:

```text
A sharp cutoff requires interface stress, a boundary condition, or a more
resolved transition layer.
```

This is mathematically simple but physically crude.

---

## Case 2: Smooth Polynomial Interior Profile

The script tested:

$$\kappa_{\rm in}(r)=k_0\left(1-\frac{r^2}{R^2}\right)^2.$$

At the boundary:

$$r=R,$$

this gives:

$$\kappa_{\rm in}(R)=0.$$

The derivative is:

$$\kappa_{\rm in}'(R)=0.$$

At the center:

$$\kappa_{\rm in}'(0)=0.$$

Thus the profile is regular at the center and smoothly dies at the surface.

This is the cleanest reduced profile class.

It shows that nonzero interior \(\kappa\) can coexist with exact exterior \(\kappa=0\) without a derivative jump.

---

## Case 3: Exponential Exterior Relaxation

The script tested an exterior tail:

$$\kappa_{\rm ext}(r)=k_R e^{-(r-R)/L}.$$

At the boundary:

$$\kappa_{\rm ext}(R)=k_R.$$

At infinity:

$$\lim_{r\to\infty}\kappa_{\rm ext}(r)=0.$$

The derivative at the boundary is:

$$\kappa_{\rm ext}'(R)=-\frac{k_R}{L}.$$

This shows that exterior relaxation can suppress \(\kappa\) asymptotically.

But it also creates an exterior \(\kappa\)-leak channel.

Since exterior \(\kappa\)-leak affects weak-field observables, this option is dangerous unless:

```text
k_R is extremely small,
or L is very short,
or the exterior relaxation is otherwise strongly suppressed.
```

For ordinary Schwarzschild exterior recovery, the preferred condition is:

$$k_R=0.$$

---

## Case 4: Massive Kappa Relaxation Outside

A possible exterior relaxation equation is:

$$\kappa''+\frac{2}{r}\kappa'-m^2\kappa=0.$$

The decaying spherical solution behaves like:

$$\kappa_{\rm ext}\sim\frac{C e^{-mr}}{r}.$$

This supports rapid exterior suppression if \(m\) is large.

But it is still a leak channel unless the amplitude or range is strongly constrained.

This gives one possible phenomenological model for deviations:

```text
massive exterior kappa tail.
```

It should be treated as observationally constrained.

---

## Case 5: Energy Penalty Picture

The script used a local energy picture.

Inside matter:

$$E_{\rm inside}=C_\kappa\kappa^2-J_{\rm inside}\kappa.$$

Stationarity gives:

$$\kappa_{\rm inside}=\frac{J_{\rm inside}}{2C_\kappa}.$$

Thus a sourceful interior can prefer nonzero \(\kappa\).

Outside matter:

$$E_{\rm outside}=C_\kappa\kappa^2.$$

Stationarity gives:

$$\kappa_{\rm outside}=0.$$

A small script-assumption issue caused the original SymPy solve to return an empty list when \(\kappa\) was declared positive; the intended math is clear if \(\kappa\) is treated as real.

The interpretation remains:

```text
sourceful interior can prefer nonzero kappa;
source-free exterior prefers kappa=0.
```

---

## Case 6: Exterior Observable Constraint

If persistent exterior \(\kappa\)-leak has the weak-field form:

$$\kappa_{\rm ext}=\lambda_\kappa\epsilon,$$

with:

$$s=-2\epsilon,$$

then:

$$A\approx1+(\lambda_\kappa-2)\epsilon,$$

and:

$$B\approx1+(\lambda_\kappa+2)\epsilon.$$

Also:

$$AB\approx1+2\lambda_\kappa\epsilon.$$

Thus exterior \(\kappa\)-leak changes weak-field metric coefficients.

This remains an observational deviation channel.

Therefore a viable model must ensure:

```text
interior kappa response does not leak appreciably into ordinary weak-field exterior regions.
```

---

## What This Study Established

This study established:

1. Sharp cutoff profiles enforce exterior compensation but need interface handling.
2. Smooth interior profiles can satisfy:
   $$\kappa(R)=0,$$
   and:
   $$\kappa'(R)=0.$$
3. Such profiles are regular at the center.
4. Exponential exterior relaxation can suppress \(\kappa\) at infinity.
5. Massive exterior relaxation gives a decaying Yukawa-like tail.
6. Any exterior \(\kappa\)-tail is an observational deviation channel.
7. A sourceful interior energy can prefer nonzero \(\kappa\).
8. A source-free exterior energy can prefer \(\kappa=0\).

---

## What This Study Did Not Establish

This study did not derive the true \(\kappa\) field equation.

It did not determine the physical source \(J_{\rm inside}\).

It did not model pressure or stress.

It did not construct a full boundary layer from first principles.

It did not derive matching conditions from a covariant action.

It did not estimate observational bounds on exterior \(\kappa\)-tails.

It only showed that boundary relaxation is plausible in reduced toy profiles.

---

## Current Best Interpretation

The current best interpretation is:

```text
Interior matter may source kappa.

The exterior source-free region suppresses kappa.

A viable boundary/interface transition should restore kappa=0 before the
ordinary exterior weak-field region.

The cleanest reduced profile class has kappa(R)=0 and kappa'(R)=0.
```

This supports the larger interior/exterior strategy.

---

## Relationship to GR Interior Residual

The GR residual diagnostic found:

$$\kappa_{\rm GR}\neq0$$

inside matter, but:

$$\kappa_{\rm GR}=0$$

at the boundary.

This boundary-layer study shows that such behavior is structurally possible in the reduced model.

The next step is to derive the profile dynamically rather than choosing it by hand.

---

## Summary

The boundary \(\kappa\)-relaxation study supports the idea that nonzero interior \(\kappa\) can coexist with exact exterior compensation.

The cleanest toy profile satisfies:

$$\kappa(R)=0,$$

$$\kappa'(R)=0,$$

and:

$$\kappa=0$$

outside.

This lets \(\kappa\) carry traceful interior response while preserving the exact compensated exterior branch.

The main warning is that any persistent exterior \(\kappa\)-tail becomes a weak-field deviation channel.
