# Candidate Exact Source-Law Geometry Check

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full covariant field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_exact_source_law_geometry_check.py
```

The guiding question was:

```text
The exact static spherical recovery used ∇²A = 8πGρ/c².
But what geometry does that ∇² belong to?
```

The result is important.

The exact Schwarzschild recovery survives, but the source operator is currently best understood as an **areal-flux / flat-radial reduced operator**, not as the ordinary scalar Laplacian of the curved spatial slice and not as the scalar operator of the two-dimensional orbit-space metric.

This is not fatal. It is a precision gain.

It tells us exactly what the future covariant or geometric parent must explain.

---

## Background

The reduced exact static spherical branch uses:

$$A=e^s,$$

and the candidate exact source law:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

In source-free exterior:

$$\nabla^2A=0.$$

For spherical mass, the desired exterior solution is:

$$A=1-\frac{r_s}{r},$$

with:

$$r_s=\frac{2GM}{c^2}.$$

Under exterior compensation:

$$\kappa=0,$$

so:

$$B=\frac1A.$$

Thus:

$$B=\frac1{1-r_s/r},$$

and:

$$AB=1.$$

This recovers the Schwarzschild exterior metric factors in areal gauge.

The geometry-check script asked whether the operator \(\nabla^2\) in the source law is:

```text
1. the flat areal radial Laplacian,
2. the curved spatial Laplacian,
3. the two-dimensional orbit-space scalar operator,
4. or simply an areal-flux conservation law.
```

---

## Test Metric

The test case was the exact Schwarzschild exterior in areal gauge:

$$A=1-\frac{r_s}{r},$$

and:

$$B=\frac1A=\frac{r}{r-r_s}.$$

Then:

$$AB=1.$$

The derivative is:

$$A'=\frac{r_s}{r^2}.$$

The script confirmed:

```text
Schwarzschild areal exterior has AB=1.
```

---

## Operator 1: Flat Areal Radial Laplacian

The flat areal radial Laplacian is:

$$\Delta_{\rm flat}A =
\frac1{r^2}\frac{d}{dr}\left(r^2A'\right).$$

For:

$$A=1-\frac{r_s}{r},$$

we have:

$$A'=\frac{r_s}{r^2}.$$

Thus:

$$r^2A'=r_s.$$

So:

$$\frac{d}{dr}(r^2A')=0.$$

Therefore:

$$\Delta_{\rm flat}A=0.$$

The script confirmed:

```text
A=1-r_s/r is flat-harmonic for r>0.
```

The corresponding areal flux is:

$$F_A=4\pi r^2A'.$$

For Schwarzschild:

$$F_A=4\pi r_s.$$

This is constant.

So the exact source law used so far is equivalent to conserved areal flux of \(A\) through coordinate spheres.

---

## Operator 2: Curved Spatial Laplacian

The curved spatial metric on a static time slice is:

$$dl^2=B(r)dr^2+r^2d\Omega^2.$$

For a radial scalar \(A(r)\), the scalar Laplacian on this curved spatial metric is:

$$\Delta_{\rm spatial}A =
\frac{1}{r^2\sqrt{B}}
\frac{d}{dr}
\left(
\frac{r^2}{\sqrt{B}}A'
\right).
$$

For the Schwarzschild exterior with:

$$B=\frac1A,$$

the script found:

$$\Delta_{\rm spatial}A =
\frac{r_s^2}{2r^4}.
$$

Thus:

$$\Delta_{\rm spatial}A\neq0.$$

So \(A\) is not harmonic under the ordinary curved spatial scalar Laplacian.

This means the exact reduced \(A\)-action is not simply a standard curved-space scalar-field energy on the \(t=\text{constant}\) spatial slice.

---

## Operator 3: Orbit-Space Scalar Operator

The two-dimensional orbit-space metric is:

$$h_{AB}dx^A dx^B=-A(r)c^2dt^2+B(r)dr^2.$$

For a static radial scalar, the corresponding orbit-space scalar operator is:

$$\Box_h A =
\frac1{\sqrt{|h|}}
\frac{d}{dr}
\left(
\sqrt{|h|}h^{rr}A'
\right).
$$

Ignoring the constant \(c\), we have:

$$\sqrt{|h|}=\sqrt{AB},$$

and:

$$h^{rr}=\frac1B.$$

In the compensated exterior:

$$AB=1,$$

so:

$$\sqrt{|h|}=1.$$

Also:

$$\frac1B=A.$$

Thus:

$$\Box_h A=\frac{d}{dr}(AA').$$

For:

$$A=1-\frac{r_s}{r},$$

the script found:

$$\Box_h A =
\frac{r_s(-2r+3r_s)}{r^4}.
$$

Thus:

$$\Box_h A\neq0.$$

So the exact source law is also not simply the scalar wave/Laplace operator of the two-dimensional orbit-space metric.

---

## Operator Comparison

The script compared all operators directly:

$$\Delta_{\rm flat}A=0,$$

$$\Delta_{\rm spatial}A=\frac{r_s^2}{2r^4},$$

and:

$$\Box_hA=\frac{r_s(-2r+3r_s)}{r^4}.$$

The areal flux is:

$$4\pi r^2A'=4\pi r_s.$$

Its derivative is:

$$\frac{d}{dr}(4\pi r^2A')=0.$$

Classification:

```text
flat areal radial operator: passes
conserved areal flux: passes
curved spatial Laplacian: fails
2D orbit-space scalar operator: fails
```

Therefore the exact source law is specifically an areal-flux / flat-radial reduced law in its current form.

---

## General Conserved Areal Flux Solution

The conserved areal flux condition is:

$$\frac{d}{dr}(r^2A')=0.$$

Equivalently:

$$r^2A''+2rA'=0.$$

The general solution is:

$$A(r)=C_1+\frac{C_2}{r}.$$

Asymptotic flatness sets:

$$C_1=1.$$

Mass flux sets:

$$C_2=-r_s.$$

Thus:

$$A(r)=1-\frac{r_s}{r}.$$

This is why conserved areal flux naturally gives the Schwarzschild temporal factor.

---

## Curved-Spatial Harmonicity Is a Different Branch

The script also checked what would happen if one imposed curved-spatial harmonicity instead.

With:

$$B=\frac1A,$$

the curved spatial Laplacian equation becomes nonlinear:

$$\Delta_{\rm spatial}A=0.$$

The operator expression is:

$$
\frac{
\left[
\frac{r}{2}(A')^2+
(rA''+2A')A
\right]
}{r}.
$$

This is not generally solved by:

$$A=1-\frac{r_s}{r}.$$

Therefore curved-spatial harmonicity would define a different theory branch.

The current exact recovery is not based on curved-spatial harmonicity of \(A\).

---

## Interpretation of the Working Operator

The operator that works is:

$$\Delta_{\rm areal}A =
\frac1{r^2}\frac{d}{dr}(r^2A').$$

This is equivalent to conserved flux through areal spheres:

$$F_A=4\pi r^2A'.$$

It is not the ordinary scalar Laplacian of the curved spatial slice.

It is not the ordinary scalar operator of the two-dimensional orbit-space metric.

Possible interpretations are:

```text
1. The reduced exact law is an areal-flux law.
2. The action uses an auxiliary Euclidean radial measure.
3. The true covariant parent is not a standard scalar-field action.
4. A deeper variational principle may reduce to areal-flux conservation.
```

This is now a central open problem.

---

## Implications for the A-Action

The current exact reduced action is:

$$E_A=\int\left[K_A|\nabla A|^2+\beta\rho A\right]d^3x.$$

This action should be read carefully.

The \(\nabla\) and \(d^3x\) in this expression currently behave like flat areal-coordinate operators, not curved spatial metric operators.

Therefore:

```text
The action is a successful reduced static spherical action toy.
It is not yet a geometric or covariant action.
```

The next theory task is to explain why the areal-flux operator, rather than the curved spatial scalar Laplacian, is the right reduced operator.

---

## What This Study Established

This study established:

1. \(A=1-r_s/r\) is harmonic under the flat areal radial operator.
2. \(A=1-r_s/r\) has conserved areal flux:
   $$4\pi r^2A'=4\pi r_s.$$
3. The conserved areal flux law gives the general exterior form:
   $$A=C_1+C_2/r.$$
4. With asymptotic flatness and mass flux, this gives:
   $$A=1-r_s/r.$$
5. \(A\) is not harmonic under the curved spatial Laplacian.
6. \(A\) is not harmonic under the two-dimensional orbit-space scalar operator.
7. The current exact source law is best described as an areal-flux / flat-radial reduced law.
8. The exact exterior recovery survives.
9. The geometric origin of the successful operator remains open.

---

## What This Study Did Not Establish

This study did not derive the areal-flux operator from a covariant principle.

It did not show that the flat areal radial operator is fundamental.

It did not produce a full action for arbitrary spacetime.

It did not address time dependence.

It did not handle nonspherical fields.

It did not address rotation.

It did not include pressure or relativistic stress.

It did not prove that the exact source law is physically correct.

It only identified which reduced operator is actually doing the work in the exact Schwarzschild recovery.

---

## Relationship to Exact Static Spherical Recovery

The exact static spherical recovery result remains valid:

$$A=1-\frac{r_s}{r},$$

$$r_s=\frac{2GM}{c^2},$$

$$B=\frac1A,$$

and:

$$AB=1.$$

But the geometry check changes the interpretation of the source law.

The safe wording is now:

```text
The reduced exact exterior model recovers Schwarzschild by an areal-flux law
for A=e^s, not by a standard curved-space scalar Laplacian.
```

This is more precise than saying simply:

```text
A is harmonic.
```

A is harmonic under the flat areal radial operator, not under the curved spatial or orbit-space scalar operators tested here.

---

## Relationship to Orbit-Space Compensation

The orbit-space compensation condition remains useful:

$$\kappa=0
\quad\Longleftrightarrow\quad
A=|\nabla R|^2.$$

In areal gauge:

$$|\nabla R|^2=\frac1B,$$

so:

$$A=\frac1B.$$

This gives:

$$AB=1.$$

The geometry check does not change this condition.

Instead, it clarifies that the source law for \(A\) is not simply the scalar Laplacian associated with the same orbit-space metric.

Thus two pieces currently have different statuses:

```text
compensation condition:
  geometrically improved through orbit-space / areal-radius scalar

source law for A:
  still an areal-flux / flat-radial reduced law needing deeper explanation
```

---

## Relationship to the Action Program

The exact-sector action candidate was:

$$E_A=\int\left[K_A|\nabla A|^2+\beta\rho A\right]d^3x.$$

The geometry check says:

```text
This action works if ∇ and d³x are interpreted as flat areal-coordinate
operators/measures.
```

It does not yet work as a standard curved spatial scalar action.

Therefore the action program must either:

```text
1. justify the flat areal measure as fundamental in the reduced sector,
2. derive it from a deeper boundary/flux principle,
3. replace it with a more geometric action that reduces to the same areal-flux law,
4. or revise the source law.
```

---

## Current Best Interpretation

The current best interpretation is:

```text
The exact static spherical exterior source law is an areal-flux law for A=e^s.

It is not yet a standard geometric Laplacian law.

The exact Schwarzschild recovery is real inside the reduced model, but the
operator responsible for it still needs a covariant or geometric parent.
```

This is a sharper and safer position than before the geometry check.

---

## Next Development Targets

### 1. Arel-Flux Principle

A possible next artifact:

```text
candidate_areal_flux_principle.md
```

Purpose:

```text
Ask whether conserved areal flux of A can be justified as a boundary or
Gauss-law principle for vacuum response.
```

### 2. Geometric Parent Search

A possible next script:

```text
candidate_geometric_parent_areal_flux.py
```

Purpose:

```text
Search for geometric quantities whose static spherical reduction gives
d/dr(r²A') = source.
```

### 3. Boundary Action

A possible next script:

```text
candidate_boundary_flux_action.py
```

Purpose:

```text
Test whether the areal-flux law can arise from a boundary/area variation
rather than a bulk curved-spatial scalar action.
```

### 4. Interior Source Model

A possible next script:

```text
candidate_interior_A_source_model.py
```

Purpose:

```text
Study interior density profiles and matching conditions for A.
```

---

## Summary

The exact source-law geometry check sharpened the theory.

The exact exterior recovery uses:

$$A=1-\frac{r_s}{r},$$

with:

$$r_s=\frac{2GM}{c^2}.$$

This \(A\) satisfies:

$$\frac1{r^2}\frac{d}{dr}(r^2A')=0,$$

and has conserved areal flux:

$$4\pi r^2A'=4\pi r_s.$$

But it does not satisfy:

```text
the curved spatial scalar Laplacian equation,
or the two-dimensional orbit-space scalar equation.
```

Therefore the exact source law is currently best described as:

```text
an areal-flux / flat-radial reduced law for A=e^s.
```

The exact Schwarzschild recovery survives.

The open problem is now precise:

```text
Why is the areal-flux operator the correct reduced source operator,
and what covariant/geometric principle produces it?
```
