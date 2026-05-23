# Candidate Areal-Flux Principle

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full covariant field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_areal_flux_principle.py
```

The guiding question was:

```text
Can the exact static spherical source law be stated more safely as a
Gauss-law-like areal-flux principle, instead of pretending that A is harmonic
under the curved spatial Laplacian?
```

The answer is yes.

The current safest mechanics statement is:

```text
Mass sources the areal flux of A=e^s.
```

The areal flux is:

$$F_A(r)=4\pi r^2A'(r).$$

The candidate flux law is:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

Outside the source:

$$M_{\rm enc}(r)=M,$$

so:

$$F_A(r)=\frac{8\pi GM}{c^2}.$$

This implies:

$$A(r)=1-\frac{2GM}{rc^2}.$$

With exterior compensation:

$$\kappa=0,$$

we have:

$$B=\frac1A.$$

Thus:

$$B(r)=\frac1{1-2GM/(rc^2)}.$$

This recovers the exact Schwarzschild exterior metric factors in areal gauge.

The open problem remains:

```text
Why should mass source areal flux of A=e^s?
```

That is now the central mechanics question.

---

## Background

The reduced exterior mode program uses:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Therefore:

$$AB=e^{2\kappa}.$$

The compensated exterior condition is:

$$\kappa=0.$$

Then:

$$A=e^s,$$

and:

$$B=e^{-s}=\frac1A.$$

The exact static spherical recovery study showed that the Schwarzschild exterior is recovered if:

$$A=1-\frac{r_s}{r},$$

with:

$$r_s=\frac{2GM}{c^2}.$$

The exact source law was first written as:

$$\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho,$$

where:

$$\Delta_{\rm areal}A =
\frac1{r^2}\frac{d}{dr}(r^2A').$$

The geometry check then showed that this operator should not be confused with the ordinary curved spatial Laplacian.

The successful operator is better interpreted as an areal-flux law.

---

## Areal-Flux Form of the Source Law

Define:

$$F_A(r)=4\pi r^2A'(r).$$

The areal source law is:

$$\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho.$$

Substitute the radial operator:

$$\frac1{r^2}\frac{d}{dr}(r^2A') =
\frac{8\pi G}{c^2}\rho.$$

Multiply by:

$$4\pi r^2.$$

Then:

$$4\pi\frac{d}{dr}(r^2A') =
4\pi r^2\frac{8\pi G}{c^2}\rho.$$

Since:

$$F_A=4\pi r^2A',$$

we get:

$$F_A'(r) =
\frac{32\pi^2G}{c^2}r^2\rho(r).$$

Now define the enclosed mass:

$$M_{\rm enc}'(r)=4\pi r^2\rho(r).$$

Then:

$$F_A'(r) =
\frac{8\pi G}{c^2}M_{\rm enc}'(r).$$

Integrating:

$$F_A(r) =
\frac{8\pi G}{c^2}M_{\rm enc}(r)+C.$$

For regular interior conditions with zero flux at zero enclosed mass, set:

$$C=0.$$

Thus:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

This is the Gauss-law form of the exact reduced source law.

---

## Source-Free Exterior

Outside the source:

$$\rho=0.$$

Therefore:

$$M_{\rm enc}(r)=M.$$

So:

$$F_A(r)=\frac{8\pi GM}{c^2}.$$

Since:

$$F_A=4\pi r^2A',$$

we have:

$$4\pi r^2A'=\frac{8\pi GM}{c^2}.$$

Therefore:

$$A'=\frac{2GM}{c^2r^2}.$$

Integrate:

$$A(r)=C_0-\frac{2GM}{c^2r}.$$

Asymptotic flatness requires:

$$A(\infty)=1.$$

So:

$$C_0=1.$$

Thus:

$$A(r)=1-\frac{2GM}{rc^2}.$$

This is the exact Schwarzschild temporal factor in areal gauge.

---

## Metric Recovery

With exterior compensation:

$$\kappa=0,$$

we have:

$$AB=1.$$

Thus:

$$B=\frac1A.$$

Using:

$$A=1-\frac{2GM}{rc^2},$$

we get:

$$B=\frac1{1-2GM/(rc^2)}.$$

So the exterior metric factors are:

$$A=1-\frac{2GM}{rc^2},$$

and:

$$B=\frac1{1-2GM/(rc^2)}.$$

These are the exact Schwarzschild exterior metric factors in areal gauge.

Thus the reduced compensated exterior plus the areal-flux law recovers the exact Schwarzschild exterior.

---

## Thin Shell / Jump Form

For a thin shell of mass:

$$M_{\rm shell},$$

the flux jump is:

$$F_A({\rm outside})-F_A({\rm inside}) =
\frac{8\pi G}{c^2}M_{\rm shell}.$$

If the inside flux is zero, then:

$$F_A({\rm outside}) =
\frac{8\pi G}{c^2}M_{\rm shell}.$$

This emphasizes the boundary interpretation:

```text
Mass changes the areal flux of A across the source.
```

This may become useful for source/interface modeling.

---

## Boundary / Gauss-Law Form

For a shell region:

$$r_1<r<r_2,$$

the integrated source law is:

$$F_A(r_2)-F_A(r_1) =
\frac{8\pi G}{c^2}M_{\rm between}.$$

where:

$$M_{\rm between}=\int_{r_1}^{r_2}4\pi r^2\rho(r)\,dr.$$

This is the cleanest current interpretation of the exact source law.

It says:

```text
Mass controls the jump or value of areal flux of A.
```

This is safer than saying:

```text
A is harmonic under the curved spatial Laplacian.
```

because that statement is false for the Schwarzschild exterior.

---

## Relation to the Nonlinear s Equation

Since:

$$A=e^s,$$

we have:

$$A'=e^s s'.$$

The areal flux is:

$$F_A=4\pi r^2e^s s'.$$

In source-free exterior:

$$F_A=\text{constant}.$$

The areal Laplacian relation is:

$$\Delta_{\rm areal}A =
e^s\left(\Delta_{\rm areal}s+|\nabla s|^2\right).$$

Thus source-free exterior gives:

$$\Delta_{\rm areal}s+|\nabla s|^2=0.$$

For:

$$A=1-\frac{r_s}{r},$$

we have:

$$s=\ln\left(1-\frac{r_s}{r}\right).$$

The script confirmed:

$$\Delta_{\rm areal}s+|\nabla s|^2=0.$$

So the areal-flux law for \(A\) is equivalent to a nonlinear source-free equation for \(s\).

In weak field, the nonlinear term is second order, so this reduces to:

$$\Delta_{\rm areal}s\approx0.$$

Thus the earlier shear Laplace law remains as the weak-field approximation.

---

## Difference from Curved Spatial Laplacian

The geometry check and the areal-flux script both confirm that the working operator is not the curved spatial scalar Laplacian.

The curved spatial metric is:

$$dl^2=B(r)dr^2+r^2d\Omega^2.$$

The scalar Laplacian on this curved spatial slice gives, for Schwarzschild \(A=1-r_s/r\):

$$\Delta_{\rm spatial}A=\frac{r_s^2}{2r^4}.$$

This is not zero.

Therefore the flux principle must not be described as ordinary scalar harmonicity on the curved spatial slice.

The correct current language is:

```text
A obeys a reduced areal-flux law.
```

not:

```text
A is a standard curved-space harmonic scalar.
```

---

## Relationship to the A-Action

The exact reduced action candidate was:

$$E_A=\int\left[K_A|\nabla A|^2+\beta\rho A\right]d^3x.$$

With:

$$\beta=\frac{16\pi G K_A}{c^2},$$

variation gives:

$$\Delta A=\frac{8\pi G}{c^2}\rho.$$

After the geometry check, the correct interpretation is:

```text
The gradient and measure in this reduced action are areal / flat-radial,
not the curved spatial metric gradient and measure.
```

Thus the action is successful as a reduced static spherical action toy, but it is not yet a full geometric/covariant action.

The areal-flux principle sharpens what the action is doing:

```text
It enforces mass-sourced areal flux of A.
```

---

## Relationship to Orbit-Space Compensation

The orbit-space foundation showed:

$$\kappa=\frac12\ln\left(\frac{A}{|\nabla R|^2}\right).$$

Therefore:

$$\kappa=0$$

is equivalent to:

$$A=|\nabla R|^2.$$

In areal gauge:

$$|\nabla R|^2=\frac1B.$$

So:

$$A=\frac1B,$$

and:

$$AB=1.$$

The areal-flux principle supplies the source law for \(A\).

The orbit-space compensation condition supplies the relation between \(A\) and \(B\).

Together:

```text
areal flux law determines A;
compensation determines B.
```

For a spherical mass:

$$A=1-\frac{2GM}{rc^2},$$

and:

$$B=\frac1A.$$

---

## What This Study Established

This study established:

1. The exact source law can be written as areal flux:
   $$F_A=4\pi r^2A'.$$

2. The enclosed-mass form is:
   $$F_A(r)=8\pi GM_{\rm enc}(r)/c^2.$$

3. Source-free exterior gives constant \(F_A\).

4. Constant exterior flux implies:
   $$A=C_0+C_1/r.$$

5. Asymptotic flatness gives:
   $$C_0=1.$$

6. Mass flux gives:
   $$C_1=-2GM/c^2.$$

7. Therefore:
   $$A=1-2GM/(rc^2).$$

8. With \(\kappa=0\):
   $$B=1/A.$$

9. The exact Schwarzschild exterior metric factors are recovered.

10. The operator is areal-flux / flat-radial, not curved-spatial.

---

## What This Study Did Not Establish

This study did not derive the areal-flux law from a covariant principle.

It did not show why mass should source \(F_A\).

It did not prove that the areal-flux law is fundamental.

It did not handle pressure or relativistic stress.

It did not solve the interior problem.

It did not handle nonspherical, rotating, or time-dependent systems.

It did not derive Einstein's equations.

It only reframed the exact static spherical source law as a Gauss-law-like areal-flux principle.

---

## Current Best Interpretation

The current best mechanics interpretation is:

```text
Mass sources areal flux of A=e^s.

Outside the source, that flux is conserved.

Conserved areal flux gives the 1/r exterior form.

Mass normalization fixes the coefficient.

Kappa compensation then gives B=1/A.

Together these recover exact Schwarzschild exterior metric factors.
```

This is the strongest current static spherical reduced mechanism.

The central unresolved question is:

```text
Why does mass source areal flux of A=e^s?
```

---

## Next Development Targets

### 1. Arel-Flux Parent Principle

A possible next document:

```text
candidate_areal_flux_parent_principle.md
```

Purpose:

```text
Explore possible ontology or variational reasons why mass sources areal flux
of A rather than curved-space scalar harmonicity.
```

### 2. Boundary / Interface Source Model

A possible next script:

```text
candidate_boundary_flux_action.py
```

Purpose:

```text
Test whether areal flux arises from a boundary/interface variation.
```

### 3. Interior Source Model

A possible next script:

```text
candidate_interior_A_source_model.py
```

Purpose:

```text
Given a density profile rho(r), solve the areal-flux law inside and match to
the exterior Schwarzschild factor.
```

### 4. Stress / Pressure Extension

A possible future note:

```text
candidate_pressure_source_extension.md
```

Purpose:

```text
Ask how pressure and relativistic stress should enter the source flux.
```

---

## Summary

The areal-flux principle reframes the exact source law.

Instead of saying:

$$A \text{ is harmonic under a curved spatial Laplacian},$$

which is false, the correct reduced statement is:

$$F_A(r)=4\pi r^2A'(r)$$

and:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

Outside the source:

$$F_A=\frac{8\pi GM}{c^2}.$$

Therefore:

$$A=1-\frac{2GM}{rc^2}.$$

With:

$$\kappa=0,$$

we get:

$$B=\frac1A.$$

Thus:

$$A=1-\frac{2GM}{rc^2},$$

and:

$$B=\frac1{1-2GM/(rc^2)}.$$

The exact Schwarzschild exterior metric factors are recovered in the reduced static spherical areal-gauge sector.

The open problem is now precise:

```text
Explain why mass sources areal flux of A=e^s.
```
