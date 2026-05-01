# Reduced Exterior Mode Program Summary

## What This Document Is

This document summarizes the current reduced exterior mode program.

It is not a postulate, theorem, proof, or field equation. It is a development summary that connects several exploratory studies into one coherent chain.

The program summarized here includes two completed reduced-sector units:

```text
Unit 1: Log-scale modes and kappa suppression
Unit 2: Exterior shear source-law toy
```

Together, these units give a clean reduced path from reciprocal exterior compensation to the weak-field exterior metric.

The summary chain is:

```text
log-scale modes
  -> kappa controls reciprocal scaling
  -> source-free exterior suppresses kappa
  -> compensated shear mode s remains active
  -> shear obeys a candidate Poisson/Laplace source law
  -> weak-field exterior metric is recovered
```

This document also identifies the next target:

```text
derive kappa suppression and the shear source law from a shared reduced exterior action or variational principle.
```

---

## Development Status

The reduced exterior mode program is exploratory.

It is not yet the full theory.

It does not derive the framework's postulates, and it does not replace the formal weak-field theorem chain. Instead, it provides a candidate mathematical bridge between the framework's ontology and the weak-field exterior recovery.

The formal theory currently contains P7 as a postulate:

```text
static source-free exterior curvature is compensated temporal-radial redistribution.
```

The reduced exterior mode program asks:

```text
What mathematical structure could eventually explain P7?
```

The current answer is:

```text
P7 corresponds, in a reduced static exterior sector, to suppression of the kappa mode.
```

---

## Unit 1: Log-Scale Modes

The first unit introduced log-scale variables for the static exterior metric factors.

Let:

$$a=\ln A,$$

and:

$$b=\ln B.$$

Define:

$$\kappa=\frac{a+b}{2},$$

and:

$$s=\frac{a-b}{2}.$$

Equivalently:

$$a=\kappa+s,$$

and:

$$b=\kappa-s.$$

Therefore:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Multiplying gives:

$$AB=e^{2\kappa}.$$

This is the core identity.

It means:

$$\kappa=0 \quad \Longleftrightarrow \quad AB=1.$$

Thus, in the reduced static exterior sector, \(\kappa\) is the reciprocal-scaling control mode.

The compensated/shear mode \(s\) remains active when \(\kappa=0\).

When \(\kappa=0\):

$$A=e^s,$$

and:

$$B=e^{-s}.$$

So:

$$AB=1$$

exactly, while \(s\) can still encode nontrivial exterior distortion.

---

## Interpretation of the Modes

The mode \(\kappa\) is the conformal, uncompensated, or measure-changing mode.

It tracks the failure of temporal and radial distortions to compensate.

The mode \(s\) is the shear, compensated, or reciprocal mode.

It tracks an opposing temporal-radial distortion that preserves:

$$AB=1.$$

In compact language:

```text
kappa = uncompensated exterior distortion
s     = compensated exterior distortion
```

The reduced P7-style exterior condition is:

$$\kappa=0,\qquad s\neq0.$$

This says:

```text
the source-free exterior suppresses uncompensated distortion,
while allowing compensated shear distortion.
```

---

## Unit 1 Result: Kappa Suppression

The \(\kappa\)-suppression studies tested whether toy exterior functionals can relax to:

$$\kappa=0$$

while still allowing:

$$s\neq0.$$

The answer was yes.

Finite-shell and continuum toy models both supported the same structure.

A typical source-free exterior continuum density was:

$$L_{\rm ext}=K_\kappa(\kappa')^2+M_\kappa^2\kappa^2+K_s(s')^2.$$

The \(\kappa\) equation was:

$$-2K_\kappa\kappa''+2M_\kappa^2\kappa=0.$$

With zero \(\kappa\) boundary data, the relaxed exterior solution is:

$$\kappa(r)=0.$$

Meanwhile, the shear mode can remain active through boundary/interface data.

For example:

$$s(r)=S_0\left(1-\frac{r}{R}\right)$$

solves a simple massless shear toy equation on a finite interval.

Therefore the toy exterior can satisfy:

$$\kappa(r)=0,$$

while:

$$s(r)\neq0.$$

This preserves:

$$AB=1$$

while allowing exterior distortion.

---

## Unit 1 Failure Mode

The \(\kappa\)-suppression studies also established a failure mode.

If the exterior has a bulk or boundary source for \(\kappa\), then reciprocal scaling fails generically.

For example, a simple \(\kappa\)-sourced equilibrium gives:

$$\kappa=\frac{J_k}{2M_\kappa^2}.$$

Then:

$$AB=e^{J_k/M_\kappa^2}.$$

This is not generally equal to 1.

Therefore, not every exterior deformation works.

The exterior deformation must live in the compensated/shear sector \(s\), not in the uncompensated \(\kappa\) sector.

This was the key refinement over the older trace-free-exchange picture.

The better reduced statement is not:

```text
all exchange is trace-free everywhere.
```

The better statement is:

```text
source/interface physics may seed compensated shear,
while the static source-free exterior suppresses kappa.
```

---

## Unit 2: Exterior Shear Source Law

Once \(\kappa=0\) is secured, the exterior metric factors are:

$$A=e^s,$$

and:

$$B=e^{-s}.$$

The remaining problem is to determine \(s(r)\).

The shear/source-law unit tested the simplest reduced candidate:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

Outside the source:

$$\rho=0,$$

so:

$$\nabla^2s=0.$$

In spherical symmetry:

$$\nabla^2s=\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{ds}{dr}\right).$$

The source-free exterior solution is:

$$s(r)=C_0+\frac{C_1}{r}.$$

Asymptotic flatness requires:

$$C_0=0.$$

The candidate mass/interface flux condition is:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

For:

$$s(r)=\frac{C_1}{r},$$

this fixes:

$$C_1=-\frac{2GM}{c^2}.$$

Thus:

$$s(r)=-\frac{2GM}{rc^2}.$$

---

## Unit 2 Result: Weak-Field Exterior Metric

With:

$$s(r)=-\frac{2GM}{rc^2},$$

and:

$$\kappa=0,$$

we get:

$$A=e^s=e^{-2GM/(rc^2)},$$

and:

$$B=e^{-s}=e^{2GM/(rc^2)}.$$

Let:

$$\epsilon=\frac{GM}{rc^2}.$$

Then:

$$A=e^{-2\epsilon}=1-2\epsilon+2\epsilon^2+O(\epsilon^3),$$

and:

$$B=e^{2\epsilon}=1+2\epsilon+2\epsilon^2+O(\epsilon^3).$$

To first order:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

Also:

$$AB=1$$

exactly in this reduced compensated sector.

Thus the shear source-law toy recovers the desired weak-field exterior metric behavior.

---

## Combined Reduced Chain

The reduced exterior mode program currently gives this chain:

$$\kappa=\frac{\ln A+\ln B}{2},$$

$$s=\frac{\ln A-\ln B}{2}.$$

Then:

$$AB=e^{2\kappa}.$$

The source-free exterior compensation target is:

$$\kappa=0.$$

Therefore:

$$A=e^s,$$

$$B=e^{-s},$$

and:

$$AB=1.$$

The candidate exterior shear source law is:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

Outside the source:

$$\nabla^2s=0.$$

For a spherical source of mass \(M\):

$$s(r)=-\frac{2GM}{rc^2}.$$

Therefore:

$$A=e^{-2GM/(rc^2)},$$

$$B=e^{2GM/(rc^2)},$$

and:

$$AB=1.$$

In weak field:

$$A\approx1-\frac{2GM}{rc^2},$$

$$B\approx1+\frac{2GM}{rc^2}.$$

This is the reduced exterior bridge from mode decomposition to weak-field metric recovery.

---

## What This Program Has Established

The reduced exterior mode program has established the following at the toy/reduced level:

1. Log-scale modes cleanly separate reciprocal and compensated behavior.
2. \(\kappa\) controls reciprocal scaling.
3. \(\kappa=0\) is equivalent to \(AB=1\).
4. \(s\) can remain nonzero while \(\kappa=0\).
5. Toy exterior functionals can suppress \(\kappa\) without suppressing \(s\).
6. Direct exterior \(\kappa\)-sourcing breaks reciprocal scaling.
7. A Laplace/Poisson law for \(s\) gives the correct \(1/r\) weak-field profile.
8. The mass/interface flux normalization fixes the coefficient as \(-2GM/c^2\).
9. The reduced metric factors recover the expected weak-field exterior form.
10. The old trace-free-exchange idea is better reframed as exterior \(\kappa\)-suppression plus shear sourcing.

---

## What This Program Has Not Established

This program has not established a full field equation.

It has not derived P7 from the deeper postulates.

It has not derived:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho$$

from a vacuum configuration-energy functional.

It has not derived the mass/interface flux condition:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

It has not identified the covariant parent of \(\kappa\) and \(s\).

It has not shown how the reduced variables generalize to nonspherical, rotating, time-dependent, strong-field, or cosmological situations.

It has not derived exact Schwarzschild behavior.

It has not addressed gravitational waves or frame dragging.

It has not yet connected this reduced program to the full substance/configuration energy bookkeeping.

These remain future work.

---

## Why This Summary Matters

Before these studies, the key open question was vague:

```text
How might P7 eventually be derived?
```

The reduced exterior mode program sharpens that question.

The new target is:

```text
Find a variational principle or field equation that suppresses kappa in the static source-free exterior
and gives a Poisson/Laplace source law for the compensated shear mode s.
```

That is a much more precise development target.

Instead of trying to derive all weak-field gravity at once, the reduced program splits the job into two mechanisms:

```text
Mechanism 1:
  exterior kappa suppression -> reciprocal scaling

Mechanism 2:
  shear source law -> 1/r weak-field profile
```

The next step is to unify these mechanisms.

---

## Next Target: Reduced Exterior Action

The next development target should be a candidate reduced exterior action or energy functional.

A schematic candidate is:

$$E_{\rm red}[\kappa,s]
=
\int d^3x
\left[
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
-
\frac{8\pi G}{c^2}\rho s
\right].$$

This is not yet proposed as the true action. It is the simplest reduced object that might yield both desired equations.

Varying with respect to \(\kappa\) should give a source-free suppression equation:

$$-K_\kappa\nabla^2\kappa+M_\kappa^2\kappa=0,$$

or equivalent.

With appropriate exterior boundary conditions, this gives:

$$\kappa=0.$$

Varying with respect to \(s\) should give a source equation of the form:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho,$$

up to sign and normalization conventions.

This would unify the two reduced mechanisms in one candidate variational structure.

---

## Next Forge Script

The next script should be:

```text
candidate_reduced_exterior_action.py
```

Its purpose should be to test whether a reduced action can produce both:

$$\kappa=0$$

in the source-free exterior and:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

The script should test:

1. Euler-Lagrange equation for \(\kappa\).
2. Euler-Lagrange equation for \(s\).
3. Source-free exterior limit.
4. Spherical exterior solution.
5. Flux normalization.
6. Weak-field metric recovery.
7. Failure control with direct \(\kappa\)-source.
8. Failure control with wrong \(s\)-source coefficient.

If successful, the reduced action would become the next candidate development note.

---

## Suggested Next Development Note

After the forge script, write:

```text
candidate_reduced_exterior_action.md
```

This note should explain whether the reduced action successfully unifies:

```text
kappa suppression
```

and:

```text
shear source law
```

in one variational toy.

It should also state clearly what remains missing:

```text
covariant generalization,
source/interface derivation,
strong-field behavior,
and connection to the full vacuum-energy ontology.
```

---

## Final Summary

The reduced exterior mode program has reached a stable intermediate result.

The compact chain is:

$$\kappa=0
\Rightarrow
A=e^s,\quad B=e^{-s},\quad AB=1.$$

Then:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho$$

gives, for a spherical mass:

$$s(r)=-\frac{2GM}{rc^2}.$$

Therefore:

$$A=e^{-2GM/(rc^2)},$$

$$B=e^{2GM/(rc^2)},$$

and:

$$AB=1.$$

In weak field:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

The reduced program is not the full theory, but it gives a clear next target:

```text
build a reduced exterior action that derives both kappa suppression and the shear source law.
```
