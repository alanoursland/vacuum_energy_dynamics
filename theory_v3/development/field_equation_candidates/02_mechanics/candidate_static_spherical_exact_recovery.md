# Candidate Static Spherical Exact Recovery

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full derivation of Einstein's equations. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_static_spherical_exact_recovery.py
```

The guiding question was:

```text
Can the reduced static spherical exterior program recover the exact
Schwarzschild exterior metric factors, not merely the weak-field limit?
```

The answer is yes, in a reduced areal-gauge sense.

The key refinement is:

```text
The earlier shear Laplace law ∇²s = 0 is the weak-field linearization.

The exact static spherical source-free variable appears to be A = exp(s),
not s itself.
```

The candidate exact exterior equation is:

$$\nabla^2 A=0,$$

with:

$$A=e^s.$$

Equivalently:

$$\nabla^2 e^s=0.$$

In terms of \(s\), this becomes:

$$\nabla^2s+|\nabla s|^2=0.$$

This nonlinear equation reduces to:

$$\nabla^2s=0$$

in weak field.

---

## Background

The reduced exterior mode program uses:

$$a=\ln A,$$

and:

$$b=\ln B.$$

The modes are:

$$\kappa=\frac{a+b}{2},$$

and:

$$s=\frac{a-b}{2}.$$

Equivalently:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Multiplying:

$$AB=e^{2\kappa}.$$

The compensated exterior condition is:

$$\kappa=0.$$

Then:

$$A=e^s,$$

and:

$$B=e^{-s}.$$

Therefore:

$$AB=1.$$

Previous weak-field work used:

$$s_{\rm weak}(r)=-\frac{r_s}{r},$$

where:

$$r_s=\frac{2GM}{c^2}.$$

This gives:

$$A=e^{s_{\rm weak}}=e^{-r_s/r}.$$

Expanding:

$$A=1-\frac{r_s}{r}+\frac{r_s^2}{2r^2}+\cdots.$$

This matches the Schwarzschild exterior only to first order.

Exact Schwarzschild in areal gauge has:

$$A_{\rm exact}=1-\frac{r_s}{r},$$

and:

$$B_{\rm exact}=\frac{1}{1-r_s/r}.$$

Thus exact recovery requires:

$$s_{\rm exact}=\ln\left(1-\frac{r_s}{r}\right).$$

---

## Exact Schwarzschild Compensated Exterior

In areal gauge, the Schwarzschild exterior metric factors are:

$$A=1-\frac{r_s}{r},$$

and:

$$B=\frac{1}{1-r_s/r}.$$

Therefore:

$$AB=1.$$

So:

$$\kappa=\frac12\ln(AB)=0.$$

Since:

$$B=\frac1A,$$

the shear mode is:

$$s=\frac12\ln\left(\frac{A}{B}\right).$$

Substituting \(B=1/A\):

$$s=\frac12\ln(A^2).$$

For the exterior region:

$$r>r_s,$$

we have \(A>0\), so:

$$s=\ln A.$$

Thus:

$$s_{\rm exact}=\ln\left(1-\frac{r_s}{r}\right).$$

Then:

$$A=e^s=1-\frac{r_s}{r},$$

and:

$$B=e^{-s}=\frac1{1-r_s/r}.$$

So:

$$AB=1$$

exactly.

This shows that the \(\kappa=0\) compensated sector can reproduce the exact Schwarzschild exterior metric factors if \(s\) takes the logarithmic form.

---

## Weak Shear Versus Exact Shear

The weak-field shear profile was:

$$s_{\rm weak}=-\frac{r_s}{r}.$$

This gives:

$$A_{\rm weak}=e^{-r_s/r}.$$

The large-radius expansion is:

$$A_{\rm weak} =
1-\frac{r_s}{r}
+
\frac{r_s^2}{2r^2}
-
\frac{r_s^3}{6r^3}
+\cdots.$$

The exact Schwarzschild temporal factor is:

$$A_{\rm exact}=1-\frac{r_s}{r}.$$

Thus \(A_{\rm weak}\) and \(A_{\rm exact}\) agree only at first order.

The exact shear is:

$$s_{\rm exact}=\ln\left(1-\frac{r_s}{r}\right).$$

Its large-radius expansion is:

$$s_{\rm exact} =
-\frac{r_s}{r}
-
\frac{r_s^2}{2r^2}
-
\frac{r_s^3}{3r^3}
+\cdots.$$

So:

$$s_{\rm exact}=s_{\rm weak}+O(r_s^2/r^2).$$

The weak shear profile is therefore the first-order approximation to the exact shear profile.

---

## Harmonic Tests

The script tested the flat radial Laplacian for spherical functions:

$$\nabla^2 f =
\frac1{r^2}\frac{d}{dr}\left(r^2\frac{df}{dr}\right).$$

For:

$$s_{\rm weak}=-\frac{r_s}{r},$$

the source-free exterior result is:

$$\nabla^2s_{\rm weak}=0.$$

So the weak shear is harmonic outside the source.

For:

$$s_{\rm exact}=\ln\left(1-\frac{r_s}{r}\right),$$

the script found:

$$\nabla^2s_{\rm exact} =
-\frac{r_s^2}{r^2(r-r_s)^2}.$$

Thus:

$$\nabla^2s_{\rm exact}\neq0.$$

So exact Schwarzschild shear is not harmonic as a function \(s\).

However, the exact temporal factor:

$$A_{\rm exact}=1-\frac{r_s}{r}$$

satisfies:

$$\nabla^2A_{\rm exact}=0$$

outside the source.

This is the key discovery of the experiment.

---

## Nonlinear Equation for s

Since:

$$A=e^s,$$

we can compute:

$$\nabla^2e^s =
e^s\left(\nabla^2s+|\nabla s|^2\right).$$

Therefore, if:

$$\nabla^2A=0,$$

then:

$$\nabla^2e^s=0.$$

Since \(e^s\neq0\), this is equivalent to:

$$\nabla^2s+|\nabla s|^2=0.$$

The script checked this for:

$$s_{\rm exact}=\ln\left(1-\frac{r_s}{r}\right).$$

It found:

$$\nabla^2s =
-\frac{r_s^2}{r^2(r-r_s)^2},$$

and:

$$|\nabla s|^2 =
\frac{r_s^2}{r^2(r-r_s)^2}.$$

Thus:

$$\nabla^2s+|\nabla s|^2=0.$$

So the exact Schwarzschild shear satisfies the nonlinear source-free equation.

---

## Linearization

Let:

$$s=\epsilon u(r),$$

where \(\epsilon\) is a small bookkeeping parameter.

Then:

$$\nabla^2s+|\nabla s|^2 =
\epsilon\nabla^2u+\epsilon^2|\nabla u|^2.$$

To first order:

$$\nabla^2s+|\nabla s|^2=0$$

becomes:

$$\nabla^2u=0.$$

Thus the earlier weak-field shear Laplace equation:

$$\nabla^2s=0$$

is the linearized approximation to the nonlinear exact equation:

$$\nabla^2s+|\nabla s|^2=0.$$

This clarifies the status of the earlier shear source-law study.

That earlier result remains valid as weak-field theory, but it should not be treated as the exact static exterior equation for \(s\).

---

## Flux Normalization for A

The candidate exact harmonic variable is:

$$A=1-\frac{r_s}{r}.$$

Then:

$$A'=\frac{r_s}{r^2}.$$

The flux is:

$$4\pi r^2 A'=4\pi r_s.$$

Set the target mass flux to:

$$\frac{8\pi GM}{c^2}.$$

Then:

$$4\pi r_s=\frac{8\pi GM}{c^2}.$$

Therefore:

$$r_s=\frac{2GM}{c^2}.$$

This recovers the Schwarzschild radius.

This parallels the earlier weak-field \(s\)-flux normalization, but the exact harmonic variable is \(A=e^s\), not \(s\).

---

## Candidate Exact Reduced Source Law

The candidate exact reduced static spherical source law is:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

Since:

$$A=e^s,$$

this can be written as:

$$\nabla^2e^s=\frac{8\pi G}{c^2}\rho.$$

In the source-free exterior:

$$\rho=0,$$

so:

$$\nabla^2e^s=0.$$

Equivalently:

$$\nabla^2s+|\nabla s|^2=0.$$

In weak field, the nonlinear term is second order, so the equation reduces to:

$$\nabla^2s\approx0.$$

This supports the interpretation that the weak-field shear source law was a linearized version of a nonlinear exact law.

---

## Exact Metric Recovery

Using the exact candidate:

$$A=1-\frac{r_s}{r},$$

and:

$$s=\ln A,$$

with:

$$\kappa=0,$$

we get:

$$B=e^{-s}.$$

Therefore:

$$B=\frac1A.$$

So:

$$B=\frac1{1-r_s/r}.$$

The product is:

$$AB=1.$$

Thus the reduced compensated sector recovers exact Schwarzschild exterior metric factors:

$$A=1-\frac{r_s}{r},$$

and:

$$B=\frac1{1-r_s/r}.$$

This is an exact areal-gauge static exterior recovery, not merely a weak-field recovery.

---

## Relationship to Orbit-Space Condition

The orbit-space study found that exterior compensation can be written as:

$$A=|\nabla R|^2,$$

where \(R\) is the areal-radius scalar and:

$$|\nabla R|^2=h^{AB}\partial_A R\partial_B R.$$

In areal gauge:

$$|\nabla R|^2=\frac1B.$$

Thus:

$$A=|\nabla R|^2$$

becomes:

$$A=\frac1B.$$

Therefore:

$$AB=1.$$

For exact Schwarzschild:

$$A=1-\frac{r_s}{r},$$

and:

$$|\nabla R|^2=A.$$

So exact Schwarzschild satisfies the orbit-space compensation condition.

This ties the exact recovery result back to the more geometric spherical-reduction formulation.

---

## Relationship to Previous Shear Source-Law Work

The previous shear profile source-law study established:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho$$

as a weak-field source-law toy.

That study produced:

$$s=-\frac{2GM}{rc^2}.$$

This correctly recovers the first-order weak-field exterior.

The exact recovery study refines that result.

The better exact reduced candidate is:

$$\nabla^2e^s=\frac{8\pi G}{c^2}\rho.$$

In weak field:

$$e^s\approx1+s.$$

Therefore:

$$\nabla^2e^s\approx\nabla^2s.$$

So the older source-law study is recovered as the linearized approximation.

Recommended wording going forward:

```text
The shear source law ∇²s = 8πGρ/c² is the linearized weak-field form.
The exact static spherical candidate is ∇²e^s = 8πGρ/c².
```

---

## What This Study Established

This study established:

1. Exact Schwarzschild exterior has \(AB=1\) in areal gauge.
2. Exact Schwarzschild exterior has \(\kappa=0\).
3. Exact Schwarzschild shear is:
   $$s=\ln(1-r_s/r).$$
4. The weak shear \(s=-r_s/r\) matches only to first order.
5. \(s_{\rm exact}\) is not harmonic under the flat radial Laplacian.
6. \(A_{\rm exact}=e^s\) is harmonic outside the source.
7. \(s_{\rm exact}\) satisfies:
   $$\nabla^2s+|\nabla s|^2=0.$$
8. This nonlinear equation linearizes to:
   $$\nabla^2s=0.$$
9. Flux normalization of \(A\) gives:
   $$r_s=2GM/c^2.$$
10. \(\kappa=0\), \(s=\ln(1-r_s/r)\) recovers exact Schwarzschild metric factors.

---

## What This Study Did Not Establish

This study did not derive Einstein's equations.

It did not prove that the full theory must use \(\nabla^2A=8\pi G\rho/c^2\).

It did not handle interior solutions.

It did not address pressure, stress, or relativistic matter sources.

It did not address rotation.

It did not address time dependence.

It did not address gravitational waves.

It did not prove that the flat radial Laplacian is the correct operator in the full theory.

It did not produce a covariant action.

It only shows that a reduced exact static spherical candidate can recover Schwarzschild exterior metric factors.

---

## Why This Matters

This result is important because it upgrades the reduced exterior program.

Previously, the program recovered only the weak-field exterior:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

Now the reduced compensated sector can recover exact Schwarzschild exterior metric factors:

$$A=1-\frac{2GM}{rc^2},$$

and:

$$B=\frac1{1-2GM/(rc^2)}.$$

The key was changing the exact harmonic variable from \(s\) to:

$$A=e^s.$$

This gives a plausible nonlinear completion of the weak-field shear law.

---

## Next Development Targets

### 1. Update Reduced Exterior Program Summary

The older reduced exterior summary should be updated to distinguish:

```text
linearized weak-field shear law:
  ∇²s = 8πGρ/c²

exact static spherical candidate:
  ∇²e^s = 8πGρ/c²
```

### 2. Candidate Exact Source-Law Lab Report

A possible lab report:

```text
static_spherical_exact_recovery_lab_report.md
```

would record this experiment as evidence.

### 3. Candidate Orbit-Space Action

A deeper next target:

```text
candidate_orbit_space_action.py
```

or:

```text
candidate_orbit_space_action.md
```

would try to express the exact candidate in terms of orbit-space variables:

$$h_{AB},\quad R,\quad A,\quad |\nabla R|^2.$$

### 4. Interior Source Model

The exact exterior source law suggests a future source problem:

```text
What interior equation and boundary conditions produce A=1-r_s/r outside?
```

This is not yet solved.

---

## Summary

The static spherical exact recovery study found that the earlier weak-field shear law should be understood as linearized.

The exact reduced candidate is:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho,$$

with:

$$A=e^s.$$

Equivalently:

$$\nabla^2e^s=\frac{8\pi G}{c^2}\rho.$$

In source-free exterior:

$$\nabla^2e^s=0.$$

In terms of \(s\):

$$\nabla^2s+|\nabla s|^2=0.$$

The exact exterior solution is:

$$A=1-\frac{r_s}{r},$$

with:

$$r_s=\frac{2GM}{c^2}.$$

Then:

$$s=\ln\left(1-\frac{r_s}{r}\right),$$

$$B=e^{-s}=\frac1{1-r_s/r},$$

and:

$$AB=1.$$

Thus the reduced compensated sector recovers exact Schwarzschild exterior metric factors in areal gauge.

This is still not a full theory, but it is the strongest static spherical exterior result so far.
