# Candidate Exterior Shear Source Law

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or field equation. It does not add a formal commitment to the theory.

Its purpose is to record a candidate reduced source-law structure for the exterior compensated/shear mode \(s(r)\), after the log-scale and \(\kappa\)-suppression studies established the reduced exterior compensation condition:

$$\kappa=0.$$

Suggested file location:

```text
04_development/field_equation_candidates/candidate_exterior_shear_source_law.md
```

This note belongs to the shear/source-law development unit.

---

## Background

The log-scale exterior-mode studies introduced:

$$a=\ln A,$$

$$b=\ln B,$$

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

Multiplying the two metric factors gives:

$$AB=e^{2\kappa}.$$

Thus:

$$\kappa=0 \quad \Longleftrightarrow \quad AB=1.$$

The \(\kappa\)-suppression studies then showed, in reduced toy form, that a source-free exterior functional can suppress \(\kappa\) while allowing the compensated/shear mode \(s\) to remain active.

So the reduced P7-style exterior structure is:

$$\kappa=0,$$

with:

$$s\neq0.$$

This note asks the next question:

```text
Given kappa = 0 in the source-free exterior, what determines s(r)?
```

---

## The Reduced Exterior Target

When:

$$\kappa=0,$$

the metric factors reduce to:

$$A=e^s,$$

and:

$$B=e^{-s}.$$

The reciprocal product is then exact:

$$AB=1.$$

The weak-field exterior target is:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

Since:

$$A=e^s,$$

we need:

$$s(r)\approx-\frac{2GM}{rc^2}.$$

The target shear profile is therefore:

$$s(r)=-\frac{2GM}{rc^2}$$

in the weak-field exterior.

This note explores the simplest reduced source law that produces this profile.

---

## Candidate Source-Free Exterior Equation

The candidate source-free exterior equation is:

$$\nabla^2s=0.$$

In spherical symmetry, this becomes:

$$\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{ds}{dr}\right)=0.$$

The general solution is:

$$s(r)=C_0+\frac{C_1}{r}.$$

Asymptotic flatness requires:

$$s(r)\to0$$

as:

$$r\to\infty.$$

Therefore:

$$C_0=0.$$

So the exterior solution becomes:

$$s(r)=\frac{C_1}{r}.$$

This gives the correct \(1/r\) shape. The remaining problem is to fix the coefficient \(C_1\) in terms of the source mass.

---

## Candidate Mass/Interface Flux Condition

The candidate mass/interface condition is a flux condition for the shear mode:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

For:

$$s(r)=\frac{C_1}{r},$$

we have:

$$s'(r)=-\frac{C_1}{r^2}.$$

Therefore:

$$4\pi r^2s'(r)=-4\pi C_1.$$

Imposing the flux condition gives:

$$-4\pi C_1=\frac{8\pi GM}{c^2}.$$

So:

$$C_1=-\frac{2GM}{c^2}.$$

Thus:

$$s(r)=-\frac{2GM}{rc^2}.$$

This is the desired weak-field exterior shear profile.

---

## Equivalent Poisson Form

The flux condition corresponds to the reduced Poisson equation:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

For a point mass:

$$\rho=M\delta^3(\mathbf r).$$

Using:

$$\nabla^2\left(\frac{1}{r}\right)=-4\pi\delta^3(\mathbf r),$$

we get:

$$\nabla^2\left(-\frac{2GM}{c^2r}\right)=\frac{8\pi GM}{c^2}\delta^3(\mathbf r).$$

Thus:

$$s(r)=-\frac{2GM}{rc^2}$$

is the exterior solution of the candidate reduced source law.

Outside the source:

$$\rho=0,$$

so:

$$\nabla^2s=0.$$

---

## Weak-Field Metric Recovery

With:

$$s(r)=-\frac{2GM}{rc^2},$$

and:

$$\kappa=0,$$

we have:

$$A=e^s=e^{-2GM/(rc^2)},$$

and:

$$B=e^{-s}=e^{2GM/(rc^2)}.$$

Let:

$$\epsilon=\frac{GM}{rc^2}.$$

Then:

$$A=e^{-2\epsilon},$$

and:

$$B=e^{2\epsilon}.$$

Expanding in weak field:

$$A=1-2\epsilon+2\epsilon^2+O(\epsilon^3),$$

and:

$$B=1+2\epsilon+2\epsilon^2+O(\epsilon^3).$$

To first order:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

Also:

$$AB=1$$

exactly in this reduced compensated sector.

So this candidate shear source law reproduces the desired weak-field exterior behavior while preserving reciprocal scaling.

---

## Relationship to the Previous Unit

The log-scale and \(\kappa\)-suppression unit established:

```text
kappa controls reciprocal scaling.
source-free exterior compensation means kappa = 0.
the exterior field can still be carried by s.
```

This note begins the next unit by proposing:

```text
the source-free exterior shear mode s is harmonic.
mass/interface data fix the shear flux.
```

Together, the reduced chain is:

$$\kappa=0,$$

then:

$$A=e^s,\qquad B=e^{-s},\qquad AB=1,$$

then:

$$\nabla^2s=0$$

outside the source,

then:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2},$$

which gives:

$$s(r)=-\frac{2GM}{rc^2}.$$

This produces the weak-field exterior metric factors.

---

## What This Candidate Explains

This candidate source-law structure explains, at the reduced toy level, how the exterior shear mode can acquire the weak-field \(1/r\) profile.

It shows that if:

1. reciprocal exterior compensation holds, so \(\kappa=0\);
2. the source-free exterior shear is harmonic, so \(\nabla^2s=0\);
3. the source/interface flux is fixed by mass as \(8\pi GM/c^2\);

then the exterior shear profile is:

$$s(r)=-\frac{2GM}{rc^2}.$$

This is enough to recover:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

---

## What This Candidate Does Not Yet Explain

This note does not derive the shear equation from the deeper vacuum framework.

It does not explain why the source-free exterior should obey:

$$\nabla^2s=0.$$

It does not derive the mass/interface flux condition:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

It does not explain why the normalization is:

$$\frac{8\pi G}{c^2}.$$

It does not derive the source law from mass-as-constraint, vacuum burden, interface smoothing, or configuration-energy minimization.

It does not identify the covariant parent of \(s\).

It does not generalize to nonspherical, rotating, time-dependent, strong-field, or cosmological settings.

So this note is not the final field equation. It is a reduced-sector candidate source law.

---

## Interpretation in Framework Language

The candidate source law can be read as follows.

The source-free exterior does not create uncompensated vacuum distortion. That is the \(\kappa=0\) result from the previous unit.

The source/interface does, however, impose a compensated shear burden on the exterior vacuum. That burden appears as a flux of the shear mode \(s\).

The exterior then relaxes harmonically:

$$\nabla^2s=0,$$

while the total flux through a surrounding sphere is fixed by the source mass:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

Thus the exterior vacuum carries a compensated distortion with a \(1/r\) profile, while maintaining reciprocal temporal-radial scaling.

In compact language:

```text
mass fixes the shear flux;
the source-free exterior propagates that shear harmonically;
kappa remains suppressed;
reciprocal scaling survives.
```

---

## Failure Modes

This candidate also clarifies the failure modes.

### Failure Mode 1: Nonzero Asymptotic Constant

If:

$$s(r)=C_0+\frac{C_1}{r},$$

with:

$$C_0\neq0,$$

then the exterior does not become flat at infinity.

So asymptotic flatness requires:

$$C_0=0.$$

### Failure Mode 2: Wrong Coefficient

If:

$$s=-\lambda\frac{GM}{rc^2},$$

then:

$$A=e^s\approx1-\lambda\frac{GM}{rc^2}.$$

The weak-field temporal coefficient requires:

$$\lambda=2.$$

So the source/interface normalization must fix:

$$C_1=-\frac{2GM}{c^2}.$$

### Failure Mode 3: Kappa Sourcing

If the exterior also sources \(\kappa\), then:

$$AB=e^{2\kappa}\neq1$$

generically.

This would break reciprocal scaling.

So the source law for \(s\) must remain compatible with exterior \(\kappa\)-suppression.

---

## Development Status

This candidate has passed the first reduced forge check in:

```text
candidate_shear_profile_source_law.py
```

The script verified:

1. the log-scale convention;
2. the radial Laplace solution;
3. the mass/interface flux coefficient;
4. the weak-field metric expansion;
5. the Poisson sign convention;
6. the asymptotic-flatness and coefficient failure controls.

The result is stable enough to use as a development note.

It should still be treated as a candidate, not as a theorem.

---

## Next Development Questions

The next questions are:

1. What configuration-energy functional gives \(\nabla^2s=0\) in the static source-free exterior?
2. What source/interface condition fixes the shear flux as \(8\pi GM/c^2\)?
3. Can this be derived from mass-as-constraint or vacuum burden reduction?
4. What is the covariant parent of the reduced shear mode \(s\)?
5. How does this generalize beyond spherical static exteriors?
6. Does the same structure predict strong-field deviations or exact Schwarzschild behavior?
7. Can the \(\kappa=0\) condition and shear source law be derived from one shared variational principle?

---

## Summary

The candidate exterior shear source law is:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

In the source-free exterior:

$$\nabla^2s=0.$$

For a spherical source of mass \(M\), asymptotic flatness and the flux condition give:

$$s(r)=-\frac{2GM}{rc^2}.$$

With:

$$\kappa=0,$$

this gives:

$$A=e^s,$$

$$B=e^{-s},$$

and:

$$AB=1.$$

The weak-field metric factors are:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

This note therefore supplies a clean reduced source-law candidate for the shear mode \(s\), while leaving the deeper derivation of that law as the next research target.
