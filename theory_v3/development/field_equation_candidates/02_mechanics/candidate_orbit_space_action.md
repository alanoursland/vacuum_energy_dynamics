# Candidate Orbit-Space Action

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full covariant action. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_orbit_space_action.py
```

The guiding question was:

```text
Can the exact static spherical source law be represented by a reduced
variational principle?
```

The answer is yes, in a reduced static spherical sense.

The exact-recovery study suggested that the correct exact source variable is:

$$A=e^s,$$

not \(s\) itself.

The candidate exact reduced source law is:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

This action study shows that this equation follows from a simple reduced action:

$$E_A=\int\left[K_A|\nabla A|^2+\beta\rho A\right]d^3x,$$

with:

$$\beta=\frac{16\pi G K_A}{c^2}.$$

Under:

$$A=e^s,$$

this becomes a nonlinear action in \(s\):

$$E_s=\int\left[K_Ae^{2s}|\nabla s|^2+\beta\rho e^s\right]d^3x.$$

In source-free exterior, it gives:

$$\nabla^2A=0,$$

or equivalently:

$$\nabla^2s+|\nabla s|^2=0.$$

This is the exact static spherical refinement of the earlier weak-field \(s\)-action.

---

## Background

The reduced exterior program uses:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Thus:

$$AB=e^{2\kappa}.$$

The compensated exterior condition is:

$$\kappa=0.$$

Then:

$$A=e^s,$$

and:

$$B=e^{-s}.$$

The exact static spherical recovery study found that Schwarzschild exterior is recovered by:

$$A=1-\frac{r_s}{r},$$

with:

$$r_s=\frac{2GM}{c^2}.$$

Then:

$$s=\ln A=\ln\left(1-\frac{r_s}{r}\right),$$

and:

$$B=\frac1A.$$

This gives:

$$AB=1.$$

The earlier weak-field source law:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho$$

is now understood as linearized.

The exact candidate is:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho,$$

with:

$$A=e^s.$$

---

## Case 0: Exact Source Variable Recap

The exact source variable is:

$$A=e^s.$$

For the exact Schwarzschild exterior:

$$A=1-\frac{r_s}{r}.$$

Then:

$$s=\ln\left(1-\frac{r_s}{r}\right).$$

The source-free exterior equation is:

$$\nabla^2A=0.$$

Since:

$$A=e^s,$$

we have:

$$\nabla^2e^s=e^s(\nabla^2s+|\nabla s|^2).$$

Thus source-free exterior also gives:

$$\nabla^2s+|\nabla s|^2=0.$$

The script confirmed:

```text
A is harmonic outside source.
s satisfies the nonlinear source-free equation.
kappa=0 gives AB=1.
```

---

## Case 1: Weak-Field Linear s-Action

The earlier weak-field action was:

$$E_s=\int\left[K_s|\nabla s|^2+\alpha\rho s\right]d^3x.$$

In one coordinate, the density is:

$$L_s=K_s(s')^2+\alpha\rho s.$$

The Euler-Lagrange equation is:

$$-2K_s s''+\alpha\rho=0.$$

Thus:

$$s''=\frac{\alpha}{2K_s}\rho.$$

In three-dimensional spherical form, this corresponds to:

$$\nabla^2s=\frac{\alpha}{2K_s}\rho.$$

Choosing:

$$\alpha=\frac{16\pi G K_s}{c^2}$$

gives:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

This is now classified as the weak-field linearized action.

---

## Case 2: Exact Candidate A-Action

The exact candidate action is:

$$E_A=\int\left[K_A|\nabla A|^2+\beta\rho A\right]d^3x.$$

In one coordinate, the density is:

$$L_A=K_A(A')^2+\beta\rho A.$$

The Euler-Lagrange equation is:

$$-2K_AA''+\beta\rho=0.$$

Thus:

$$A''=\frac{\beta}{2K_A}\rho.$$

In three-dimensional form, the candidate is:

$$\nabla^2A=\frac{\beta}{2K_A}\rho.$$

To match the exact static spherical source law:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho,$$

choose:

$$\frac{\beta}{2K_A}=\frac{8\pi G}{c^2}.$$

Therefore:

$$\beta=\frac{16\pi G K_A}{c^2}.$$

The script confirmed that the \(A\)-action gives the desired Poisson equation for \(A\).

---

## Case 3: Nonlinear s-Action Induced by A = exp(s)

Because:

$$A=e^s,$$

we have:

$$A'=e^s s'.$$

Therefore:

$$|A'|^2=e^{2s}|s'|^2.$$

Substituting into the \(A\)-action gives:

$$E_s^{\rm exact}
=
\int\left[K_Ae^{2s}|\nabla s|^2+\beta\rho e^s\right]d^3x.$$

This is the exact nonlinear \(s\)-action induced by the linear \(A\)-action.

The script confirmed that varying this nonlinear \(s\)-action is equivalent to varying the \(A\)-action and then applying:

$$A=e^s.$$

In one coordinate, the Euler-Lagrange equation becomes proportional to:

$$\beta\rho-2K_AA''=0.$$

In source-free exterior:

$$\rho=0,$$

so:

$$A''=0$$

in one dimension, or:

$$\nabla^2A=0$$

in the radial three-dimensional version.

In terms of \(s\), this becomes:

$$\nabla^2s+|\nabla s|^2=0.$$

---

## Case 4: Radial Source-Free A Equation

For:

$$A=1-\frac{r_s}{r},$$

the radial Laplacian is:

$$\nabla^2A=0$$

outside the source.

With:

$$s=\ln A,$$

the script confirmed:

$$\nabla^2s+|\nabla s|^2=0.$$

This verifies that the exact Schwarzschild exterior temporal factor is a source-free solution of the \(A\)-equation.

---

## Case 5: Radial A-Action with Spherical Measure

The three-dimensional spherical action reduces to a one-dimensional radial integral with measure:

$$r^2dr.$$

Ignoring the constant \(4\pi\), the radial density is:

$$L_{\rm radial}
=
r^2\left[K_A(A')^2+\beta\rho A\right].$$

The Euler-Lagrange equation is:

$$r^2\beta\rho-2K_A(r^2A')'=0.$$

Rearranging:

$$\frac1{r^2}(r^2A')'
=
\frac{\beta}{2K_A}\rho.$$

Thus:

$$\nabla^2A=\frac{\beta}{2K_A}\rho.$$

This confirms that the \(A\)-action gives the spherical Poisson equation when the radial measure is included.

---

## Case 6: Flux Normalization

For the exterior solution:

$$A=1-\frac{r_s}{r},$$

we have:

$$A'=\frac{r_s}{r^2}.$$

The flux is:

$$4\pi r^2A'=4\pi r_s.$$

Set the source flux to:

$$\frac{8\pi GM}{c^2}.$$

Then:

$$4\pi r_s=\frac{8\pi GM}{c^2}.$$

Therefore:

$$r_s=\frac{2GM}{c^2}.$$

So the action-normalized \(A\)-source law recovers the Schwarzschild radius relation.

---

## Case 7: Combining A-Action with Kappa Suppression

The exact-sector toy action can be combined with \(\kappa\)-suppression:

$$E=
\int
\left[
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_A|\nabla A|^2
+
\beta\rho A
\right]d^3x.$$

The \(\kappa\) equation is:

$$-2K_\kappa\nabla^2\kappa+2M_\kappa^2\kappa=0.$$

In a source-free exterior, the relaxed solution is:

$$\kappa=0.$$

The \(A\) equation is:

$$\nabla^2A=\frac{\beta}{2K_A}\rho.$$

With:

$$\beta=\frac{16\pi G K_A}{c^2},$$

this gives:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

Thus the combined reduced exact-sector toy is:

```text
kappa is suppressed;
A=e^s is sourced;
when kappa=0, B=1/A.
```

This produces exact Schwarzschild exterior metric factors in the static spherical exterior.

---

## Case 8: Orbit-Space Compensation Reminder

The orbit-space formulation writes the static spherical metric as:

$$ds^2=-T(X)c^2dt^2+Q(X)dX^2+S(X)^2d\Omega^2.$$

The areal-radius scalar is:

$$R=S(X).$$

The orbit-space gradient norm is:

$$|\nabla R|^2=\frac{[S'(X)]^2}{Q(X)}.$$

The gauge-aware reduced imbalance is:

$$\kappa=
\frac12\ln\left(\frac{A}{|\nabla R|^2}\right).$$

Compensation:

$$\kappa=0$$

gives:

$$A=|\nabla R|^2.$$

In arbitrary radial coordinate:

$$T(X)Q(X)=[S'(X)]^2.$$

In areal gauge:

$$|\nabla R|^2=\frac1B,$$

so:

$$A=\frac1B,$$

and:

$$AB=1.$$

Exact Schwarzschild satisfies this with:

$$A=1-\frac{r_s}{r}.$$

This connects the action variable \(A\) to the orbit-space compensation condition.

---

## Main Result

The action probe supports the exact-recovery refinement.

The weak-field theory can be represented by an action in \(s\):

$$E_s=\int\left[K_s|\nabla s|^2+\alpha\rho s\right]d^3x.$$

The exact static spherical candidate is cleaner in \(A=e^s\):

$$E_A=\int\left[K_A|\nabla A|^2+\beta\rho A\right]d^3x.$$

With:

$$\beta=\frac{16\pi G K_A}{c^2},$$

this gives:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

Under:

$$A=e^s,$$

this becomes the nonlinear \(s\)-action:

$$E_s^{\rm exact}
=
\int
\left[
K_Ae^{2s}|\nabla s|^2
+
\beta\rho e^s
\right]d^3x.$$

In source-free exterior, this yields:

$$\nabla^2s+|\nabla s|^2=0.$$

---

## Relationship to Exact Schwarzschild Recovery

The exact Schwarzschild exterior in areal gauge is:

$$A=1-\frac{2GM}{rc^2},$$

and:

$$B=\frac1{1-2GM/(rc^2)}.$$

The \(A\)-action gives the exterior equation:

$$\nabla^2A=0.$$

The flux normalization gives:

$$r_s=\frac{2GM}{c^2}.$$

With \(\kappa=0\):

$$B=\frac1A.$$

Thus the combined reduced exact-sector action recovers the exact Schwarzschild exterior metric factors.

---

## Relationship to the Earlier Reduced Action

The earlier reduced exterior action was:

$$E=
\int
\left[
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s
\right]d^3x.$$

That action is now best interpreted as the weak-field linearized form.

The exact-sector replacement is:

$$E=
\int
\left[
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_A|\nabla A|^2
+
\beta\rho A
\right]d^3x.$$

with:

$$A=e^s.$$

This preserves the structure:

```text
kappa suppression + sourced exterior field
```

but upgrades the sourced field from \(s\) to \(A=e^s\).

---

## What This Study Established

This study established:

1. The weak-field \(s\)-action gives a Poisson equation for \(s\).
2. The exact \(A\)-action gives a Poisson equation for \(A\).
3. Choosing \(\beta=16\pi G K_A/c^2\) gives:
   $$\nabla^2A=8\pi G\rho/c^2.$$
4. Under \(A=e^s\), the \(A\)-action becomes nonlinear in \(s\).
5. The nonlinear \(s\)-action is variationally equivalent to the \(A\)-action.
6. In source-free exterior:
   $$\nabla^2A=0.$$
7. In source-free exterior, equivalently:
   $$\nabla^2s+|\nabla s|^2=0.$$
8. The radial action with spherical measure gives the spherical Poisson equation.
9. Flux normalization recovers:
   $$r_s=2GM/c^2.$$
10. Combining \(A\)-sourcing with \(\kappa\)-suppression gives a reduced exact-sector toy.

---

## What This Study Did Not Establish

This study did not produce a full covariant action.

It did not prove that \(A\) is the correct fundamental field.

It did not derive the spherical radial Laplacian from a deeper geometric principle.

It did not address time dependence.

It did not address nonspherical fields.

It did not include pressure or relativistic stress sources.

It did not derive Einstein's equations.

It did not handle horizons or interiors beyond exterior boundary behavior.

It only provides a reduced static spherical variational toy.

---

## Current Best Interpretation

The current best interpretation is:

```text
The weak-field exterior action is naturally linear in s.

The exact static spherical exterior action is naturally linear in A=e^s.

When rewritten in s, the exact action becomes nonlinear.

Kappa suppression supplies reciprocal compensation.

A-sourcing supplies the exact Schwarzschild temporal factor.

Together they recover exact Schwarzschild exterior metric factors in areal gauge.
```

This makes the reduced exterior branch more coherent.

---

## Next Development Targets

### 1. Candidate Orbit-Space Action v2

The next version should ask:

```text
Can the A-action be written directly in orbit-space geometric variables,
using h_AB, R, A, and |∇R|²?
```

The current action still uses an effectively Euclidean radial measure.

### 2. Interior Source Model

The exterior solution is clean.

The next source question is:

```text
What interior equation and boundary conditions produce the same exterior A?
```

### 3. Pressure / Stress Coupling

The current source is mass density \(\rho\).

A relativistic theory must eventually decide how pressure and stress source the fields.

### 4. Time-Dependent Generalization

The exact static spherical action does not yet describe waves or dynamical fields.

---

## Summary

The orbit-space action probe supports the exact static spherical refinement.

The exact reduced action sector is:

$$E_A=\int\left[K_A|\nabla A|^2+\beta\rho A\right]d^3x,$$

with:

$$A=e^s,$$

and:

$$\beta=\frac{16\pi G K_A}{c^2}.$$

Variation gives:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

In source-free exterior:

$$\nabla^2A=0.$$

For spherical mass:

$$A=1-\frac{2GM}{rc^2}.$$

With:

$$\kappa=0,$$

we get:

$$B=\frac1A.$$

Thus:

$$A=1-\frac{2GM}{rc^2},$$

and:

$$B=\frac1{1-2GM/(rc^2)}.$$

This recovers the exact Schwarzschild exterior metric factors in areal gauge.

The main caveat remains: this is a reduced static spherical action candidate, not a full covariant action.
