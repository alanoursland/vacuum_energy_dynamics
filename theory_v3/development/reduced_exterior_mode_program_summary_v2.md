# Reduced Exterior Mode Program Summary v2

## What This Document Is

This document is a consolidated status summary for the reduced exterior mode program.

It replaces the earlier reduced exterior summary as the current best map of the static spherical branch.

It is not a postulate, theorem, proof, or complete field equation. It is a development summary.

The major v2 update is:

```text
The previous shear source law ∇²s = 8πGρ/c² is now understood as the
linearized weak-field form.

The stronger exact static spherical candidate is ∇²A = 8πGρ/c²,
with A = exp(s).
```

Equivalently:

$$\nabla^2e^s=\frac{8\pi G}{c^2}\rho.$$

In source-free exterior:

$$\nabla^2e^s=0.$$

In terms of \(s\):

$$\nabla^2s+|\nabla s|^2=0.$$

This exact candidate recovers the Schwarzschild exterior metric factors in areal gauge.

---

## Current Core Chain

The reduced static spherical exterior metric is written in areal gauge as:

$$ds^2=-A(r)c^2dt^2+B(r)dr^2+r^2d\Omega^2.$$

Define log-scale variables:

$$a=\ln A,$$

and:

$$b=\ln B.$$

The reduced modes are:

$$\kappa=\frac{a+b}{2},$$

and:

$$s=\frac{a-b}{2}.$$

Equivalently:

$$a=\kappa+s,$$

and:

$$b=\kappa-s.$$

Thus:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Multiplying:

$$AB=e^{2\kappa}.$$

Therefore:

$$\kappa=0\quad\Longleftrightarrow\quad AB=1.$$

The compensated exterior sector is:

$$\kappa=0,\qquad s\neq0.$$

Then:

$$A=e^s,$$

and:

$$B=e^{-s}.$$

---

## Interpretation of the Modes

The current interpretation is:

```text
kappa:
  reduced imbalance / reciprocal-scaling / trace-like mode

s:
  reduced compensated shear-like mode
```

The static source-free exterior suppresses \(\kappa\), while \(s\) carries the exterior gravitational distortion.

A useful slogan remains:

```text
Gravity is the compensated shear left after the source-free vacuum suppresses imbalance.
```

The formal reduced version is:

```text
In the static spherical exterior, kappa is suppressed and the remaining
field is carried by the compensated shear mode s.
```

---

## Gauge and Orbit-Space Status

The variables \(\kappa\) and \(s\) are not raw invariant scalar fields.

Under a radial reparameterization:

$$r=f(R),$$

the naive modes shift:

$$\kappa\rightarrow\kappa+\ln f'(R),$$

and:

$$s\rightarrow s-\ln f'(R).$$

So the safe statement is:

```text
kappa and s are static-spherical areal-gauge reduced variables,
or gauge-aware spherical-reduction diagnostics.
```

For a general static spherical metric:

$$ds^2=-T(X)c^2dt^2+Q(X)dX^2+S(X)^2d\Omega^2,$$

the areal radius is:

$$R=S(X).$$

The areal-gauge imbalance mode is:

$$\kappa_{\rm areal} =
\frac12\ln\left(\frac{T(X)Q(X)}{[S'(X)]^2}\right).$$

Thus:

$$\kappa_{\rm areal}=0$$

is equivalent to:

$$T(X)Q(X)=[S'(X)]^2.$$

The orbit-space formulation improves this.

Spherically symmetric geometry can be written as:

$$ds^2=h_{AB}(x)dx^A dx^B+R(x)^2d\Omega^2.$$

The areal-radius scalar satisfies:

$$|\nabla R|^2=h^{AB}\partial_A R\partial_B R.$$

In the static diagonal sector:

$$|\nabla R|^2=\frac{[S'(X)]^2}{Q(X)}.$$

Then:

$$\kappa =
\frac12\ln\left(\frac{A}{|\nabla R|^2}\right),$$

and:

$$s =
\frac12\ln\left(A|\nabla R|^2\right).$$

The compensation condition becomes:

$$\kappa=0\quad\Longleftrightarrow\quad A=|\nabla R|^2.$$

In areal gauge:

$$|\nabla R|^2=\frac1B,$$

so this reduces to:

$$AB=1.$$

This is the current best geometric expression of exterior compensation in spherical reduction.

---

## Weak-Field v1 Source Law

The earlier shear source-law candidate used:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

Outside the source:

$$\nabla^2s=0.$$

In spherical symmetry, asymptotic flatness gives:

$$s(r)=\frac{C}{r}.$$

Flux normalization gives:

$$s(r)=-\frac{2GM}{rc^2}.$$

Then:

$$A=e^s=e^{-2GM/(rc^2)},$$

and:

$$B=e^{-s}=e^{2GM/(rc^2)}.$$

Expanding to first order:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

This recovers the weak-field exterior.

But:

$$e^{-2GM/(rc^2)}$$

does not equal the exact Schwarzschild temporal factor:

$$1-\frac{2GM}{rc^2}.$$

Therefore the v1 shear source law is only the linearized weak-field law.

---

## Exact Static Spherical Candidate

The exact static spherical candidate uses:

$$A=e^s$$

as the harmonic/source variable.

The candidate source equation is:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

Equivalently:

$$\nabla^2e^s=\frac{8\pi G}{c^2}\rho.$$

In source-free exterior:

$$\nabla^2A=0.$$

The spherical exterior solution is:

$$A(r)=C_0+\frac{C_1}{r}.$$

Asymptotic flatness gives:

$$C_0=1.$$

The exterior solution is:

$$A(r)=1-\frac{r_s}{r}.$$

Flux normalization gives:

$$4\pi r^2 A'=\frac{8\pi GM}{c^2}.$$

Since:

$$A'=\frac{r_s}{r^2},$$

we get:

$$4\pi r_s=\frac{8\pi GM}{c^2}.$$

Thus:

$$r_s=\frac{2GM}{c^2}.$$

So:

$$A(r)=1-\frac{2GM}{rc^2}.$$

With:

$$\kappa=0,$$

we have:

$$B=e^{-s}=\frac1A.$$

Therefore:

$$B(r)=\frac1{1-2GM/(rc^2)}.$$

This recovers the exact Schwarzschild exterior metric factors in areal gauge.

---

## Nonlinear Equation for s

Since:

$$A=e^s,$$

the exact source-free equation:

$$\nabla^2A=0$$

becomes:

$$\nabla^2e^s=0.$$

Using:

$$\nabla^2e^s=e^s(\nabla^2s+|\nabla s|^2),$$

we get:

$$\nabla^2s+|\nabla s|^2=0.$$

The exact Schwarzschild shear is:

$$s_{\rm exact} =
\ln\left(1-\frac{2GM}{rc^2}\right).$$

It is not harmonic:

$$\nabla^2s_{\rm exact}\neq0.$$

But it satisfies:

$$\nabla^2s_{\rm exact}+|\nabla s_{\rm exact}|^2=0.$$

In weak field, the nonlinear term is second order, so:

$$\nabla^2s\approx0.$$

Thus the older equation:

$$\nabla^2s=0$$

is the linearized source-free form.

---

## Relationship to Schwarzschild

Exact Schwarzschild in areal coordinates has:

$$A=1-\frac{r_s}{r},$$

and:

$$B=\frac1{1-r_s/r}.$$

Therefore:

$$AB=1.$$

So:

$$\kappa=0.$$

Also:

$$A=|\nabla R|^2$$

in the orbit-space formulation.

Thus exact Schwarzschild satisfies the reduced exterior compensation condition:

$$\kappa=0,$$

or equivalently:

$$A=|\nabla R|^2.$$

The exact shear is:

$$s=\ln A=\ln\left(1-\frac{r_s}{r}\right).$$

This is stronger than weak-field recovery.

---

## Relationship to the Reduced Exterior Action

The earlier reduced exterior action was:

$$L =
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s.$$

This action supported the weak-field shear source law.

The exact-recovery result suggests that the \(s\)-sector may need a nonlinear or transformed form where the source variable is:

$$A=e^s.$$

A possible exact-sector replacement is schematically:

$$K_A|\nabla A|^2+\alpha\rho A,$$

or an equivalent nonlinear action in \(s\):

$$K_s e^{2s}|\nabla s|^2+\alpha\rho e^s.$$

This is not yet established. It is a next candidate target.

The key change is:

```text
linearized action in s -> exact candidate action in A=e^s
```

---

## Relationship to Regime Classification

The exchange / creation / relaxation program still fits.

Static exterior gravity remains an exchange/relaxation endpoint:

$$\kappa=0.$$

The field is carried by the compensated mode:

$$s=\ln A.$$

But the exact source variable is:

$$A=e^s.$$

A \(\kappa\)-leak remains a deviation channel:

$$AB=e^{2\kappa}\neq1.$$

Thus the exact recovery does not erase the regime classification. It strengthens the static exterior branch.

---

## Current Stable Results

The current stable reduced results are:

1. Log-scale split:
   $$AB=e^{2\kappa}.$$

2. Compensation:
   $$\kappa=0\Longleftrightarrow AB=1.$$

3. Orbit-space form:
   $$\kappa=\frac12\ln(A/|\nabla R|^2).$$

4. Geometric compensation:
   $$A=|\nabla R|^2.$$

5. Exact static spherical source candidate:
   $$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

6. Exact exterior solution:
   $$A=1-\frac{2GM}{rc^2}.$$

7. Exact compensated radial factor:
   $$B=\frac1{1-2GM/(rc^2)}.$$

8. Exact shear:
   $$s=\ln\left(1-\frac{2GM}{rc^2}\right).$$

9. Nonlinear shear equation:
   $$\nabla^2s+|\nabla s|^2=0$$
   in source-free exterior.

10. Weak-field shear law:
   $$\nabla^2s\approx\frac{8\pi G}{c^2}\rho$$
   as the linearized approximation.

---

## Current Open Questions

### 1. What is the geometric action?

The exact candidate suggests an action in \(A\), \(e^s\), or orbit-space variables.

Open question:

```text
Can we write an action whose variation gives ∇²A = 8πGρ/c²
while preserving kappa suppression?
```

### 2. What is the correct Laplacian?

The current exact recovery uses the flat radial Laplacian in areal coordinates.

Open question:

```text
Is this operator a reduced orbit-space Laplacian, a Euclidean auxiliary operator,
or a consequence of a deeper geometric variational principle?
```

### 3. What about interiors?

The exterior solution works.

Open question:

```text
What interior source model and boundary conditions produce the exact exterior?
```

### 4. What about pressure and relativistic sources?

The current source is mass density \(\rho\).

Open question:

```text
How do pressure, stress, and relativistic energy sources enter?
```

### 5. What about nonspherical, rotating, and time-dependent fields?

Not yet addressed.

---

## Recommended Next Work

The next technical target is:

```text
candidate_orbit_space_action.py
```

Purpose:

```text
Test whether the exact source law can be represented as a variational
principle in A=e^s and then translated into s and orbit-space variables.
```

The script should compare:

```text
weak action in s:
  |∇s|² + rho s

exact candidate action in A:
  |∇A|² + rho A

nonlinear s action:
  e^{2s}|∇s|² + rho e^s
```

and verify that variation gives:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho$$

or equivalently:

$$\nabla^2e^s=\frac{8\pi G}{c^2}\rho.$$

---

## One-Paragraph Current Summary

The reduced exterior mode program now has a stronger exact static spherical branch. The log-scale split identifies \(\kappa\) as the reciprocal-scaling control mode and \(s\) as the compensated shear mode. Gauge and orbit-space studies show that \(\kappa\) is best treated as a spherical-reduction diagnostic, with exterior compensation expressed geometrically as \(A=|\nabla R|^2\). The earlier shear source law \(\nabla^2s=8\pi G\rho/c^2\) is now understood as weak-field linearized. The exact static spherical candidate uses \(A=e^s\) as the source variable: \(\nabla^2A=8\pi G\rho/c^2\). This gives \(A=1-2GM/(rc^2)\), \(B=1/A\), \(r_s=2GM/c^2\), and exact Schwarzschild exterior metric factors in areal gauge. The next problem is to find the action/geometric principle behind this exact reduced law.

---

## Status Snapshot

```text
Most stable identity:
  AB = exp(2 kappa)

Best compensation form:
  A = |∇R|²

Best exact static spherical source variable:
  A = exp(s)

Best exact source-law candidate:
  ∇²A = 8πGρ/c²

Best weak-field approximation:
  ∇²s = 8πGρ/c²

Strongest recovery:
  exact Schwarzschild exterior metric factors in areal gauge

Main caveat:
  still reduced, static, spherical, and not a full covariant field equation

Best next script:
  candidate_orbit_space_action.py
```
