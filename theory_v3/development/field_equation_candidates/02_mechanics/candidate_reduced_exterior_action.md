# Candidate Reduced Exterior Action

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full field equation. It does not add a formal commitment to the theory.

Its purpose is to record a candidate reduced variational structure that unifies two previously separate reduced mechanisms:

```text
kappa suppression
```

and:

```text
shear source law
```

The candidate was tested in:

```text
candidate_reduced_exterior_action.py
```

and passed the reduced symbolic checks.

Suggested file location:

```text
04_development/field_equation_candidates/candidate_reduced_exterior_action.md
```

---

## Background

The reduced exterior mode program introduced log-scale variables:

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

Therefore:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Multiplying:

$$AB=e^{2\kappa}.$$

Thus:

$$\kappa=0 \quad \Longleftrightarrow \quad AB=1.$$

The \(\kappa\)-suppression studies showed that source-free exterior toy functionals can relax to:

$$\kappa=0$$

while allowing:

$$s\neq0.$$

The shear/source-law study then showed that if the compensated shear mode obeys:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho,$$

then a spherical source of mass \(M\) gives:

$$s(r)=-\frac{2GM}{rc^2}.$$

With \(\kappa=0\), this gives:

$$A=e^s,$$

$$B=e^{-s},$$

and:

$$AB=1.$$

In weak field:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

This note records a reduced action that produces both pieces in one toy variational structure.

---

## Candidate Reduced Action

The candidate reduced exterior energy/action density is:

$$L
=
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s.$$

Here:

- \(\kappa\) is the uncompensated or conformal exterior mode.
- \(s\) is the compensated/shear exterior mode.
- \(K_\kappa\) is the stiffness coefficient for gradients of \(\kappa\).
- \(M_\kappa^2\) is the suppression coefficient for \(\kappa\).
- \(K_s\) is the stiffness coefficient for gradients of \(s\).
- \(\rho\) is the mass density source.
- \(\alpha\) is the coupling coefficient between mass density and shear.

This is a reduced, non-covariant toy. It is written only to test whether one simple variational structure can produce both reduced exterior mechanisms.

---

## Variation with Respect to Kappa

Varying with respect to \(\kappa\) gives:

$$-2K_\kappa\nabla^2\kappa+2M_\kappa^2\kappa=0.$$

In a source-free exterior with zero \(\kappa\) boundary data, the relaxed solution is:

$$\kappa=0.$$

This immediately gives:

$$AB=e^{2\kappa}=1.$$

So the \(\kappa\) part of the action supplies the reduced exterior compensation mechanism.

In interpretation:

```text
the source-free exterior suppresses uncompensated distortion.
```

---

## Variation with Respect to Shear

Varying with respect to \(s\) gives:

$$-2K_s\nabla^2s+\alpha\rho=0.$$

Therefore:

$$\nabla^2s=\frac{\alpha}{2K_s}\rho.$$

The desired reduced shear source law is:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

Thus the coupling must satisfy:

$$\frac{\alpha}{2K_s}=\frac{8\pi G}{c^2}.$$

So:

$$\alpha=\frac{16\pi G K_s}{c^2}.$$

With this normalization, the reduced action yields:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

---

## Spherical Exterior Solution

Outside the source:

$$\rho=0.$$

Therefore:

$$\nabla^2s=0.$$

In spherical symmetry:

$$\nabla^2s=\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{ds}{dr}\right).$$

The exterior solution is:

$$s(r)=C_0+\frac{C_1}{r}.$$

Asymptotic flatness requires:

$$C_0=0.$$

The mass/interface flux condition is:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

For:

$$s(r)=\frac{C_1}{r},$$

we have:

$$s'(r)=-\frac{C_1}{r^2}.$$

So:

$$4\pi r^2s'(r)=-4\pi C_1.$$

Setting this equal to the mass flux gives:

$$-4\pi C_1=\frac{8\pi GM}{c^2}.$$

Therefore:

$$C_1=-\frac{2GM}{c^2}.$$

So:

$$s(r)=-\frac{2GM}{rc^2}.$$

---

## Metric Recovery

With:

$$\kappa=0,$$

we have:

$$A=e^s,$$

and:

$$B=e^{-s}.$$

Using:

$$s(r)=-\frac{2GM}{rc^2},$$

we get:

$$A=e^{-2GM/(rc^2)},$$

and:

$$B=e^{2GM/(rc^2)}.$$

Let:

$$\epsilon=\frac{GM}{rc^2}.$$

Then:

$$A=e^{-2\epsilon},$$

and:

$$B=e^{2\epsilon}.$$

Expanding:

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

Thus the reduced action recovers the desired weak-field exterior behavior.

---

## Failure Control: Direct Kappa Source

The forge script also tested the failure mode where \(\kappa\) is directly sourced.

Consider:

$$L_\kappa
=
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
-
J_\kappa\kappa.$$

For a constant equilibrium:

$$-J_\kappa+2M_\kappa^2\kappa=0.$$

So:

$$\kappa=\frac{J_\kappa}{2M_\kappa^2}.$$

Then:

$$AB=e^{2\kappa}=e^{J_\kappa/M_\kappa^2}.$$

This is not generally equal to 1.

Therefore, direct exterior \(\kappa\)-sourcing breaks reciprocal scaling.

This confirms the key structural requirement:

```text
mass may source shear s,
but the source-free exterior must not source kappa.
```

---

## Failure Control: Wrong Shear Coefficient

The script also tested the coefficient of the shear profile.

If:

$$s=-\lambda\epsilon,$$

where:

$$\epsilon=\frac{GM}{rc^2},$$

then:

$$A=e^{-\lambda\epsilon}\approx1-\lambda\epsilon.$$

The weak-field temporal coefficient requires:

$$\lambda=2.$$

Thus the shear source normalization must produce:

$$s=-2\frac{GM}{rc^2}.$$

This is why the source-law coefficient is fixed as:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

---

## Conceptual Interpretation

This reduced action gives mathematical form to the slogan:

```text
Gravity is the compensated shear left after the source-free vacuum suppresses imbalance.
```

More precisely:

```text
In the reduced exterior model, the vacuum suppresses the uncompensated mode kappa,
while mass sources the compensated shear mode s.
```

The \(\kappa\) sector enforces balance:

$$\kappa=0.$$

The \(s\) sector carries the exterior gravitational distortion:

$$s(r)=-\frac{2GM}{rc^2}.$$

Together:

$$A=e^s,$$

$$B=e^{-s},$$

and:

$$AB=1.$$

---

## What This Candidate Establishes

At the reduced toy level, this candidate establishes:

1. A single variational structure can produce \(\kappa\)-suppression and the shear source law.
2. The \(\kappa\) equation relaxes to \(\kappa=0\) in the source-free exterior.
3. The \(s\) equation gives a Poisson-type source law.
4. The coefficient \(\alpha=16\pi G K_s/c^2\) gives the desired normalization.
5. The spherical exterior solution is \(s(r)=-2GM/(rc^2)\).
6. The weak-field metric factors are recovered.
7. Direct \(\kappa\)-sourcing breaks reciprocal scaling.
8. The shear coefficient is fixed by the weak-field temporal response.

This is the strongest reduced exterior result so far.

---

## What This Candidate Does Not Establish

This candidate does not provide a covariant field equation.

It does not prove that the true vacuum action has this form.

It does not derive \(K_\kappa\), \(M_\kappa\), \(K_s\), or \(\alpha\) from deeper principles.

It does not explain why mass couples specifically to \(s\) and not to \(\kappa\).

It does not derive the source/interface coupling from vacuum burden, substance exchange, or mass-as-constraint.

It does not generalize to nonspherical, rotating, time-dependent, strong-field, or cosmological situations.

It does not derive exact Schwarzschild behavior.

It does not address gravitational waves, frame dragging, or interior solutions.

It is a reduced exterior variational toy.

---

## Relationship to the Framework

The formal theory currently postulates P7 as the static source-free exterior compensation condition.

This reduced action suggests one possible future route for deriving P7.

In the reduced sector:

$$P7 \quad \leftrightarrow \quad \kappa=0.$$

The action gives:

$$-2K_\kappa\nabla^2\kappa+2M_\kappa^2\kappa=0.$$

With exterior boundary conditions, this relaxes to:

$$\kappa=0.$$

So P7-like compensation may eventually arise as an exterior equilibrium condition rather than a primitive postulate.

The action also supplies the reduced shear source law:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

Together, these yield the weak-field exterior metric.

---

## Next Development Questions

The next questions are:

1. What is the covariant parent of \(\kappa\) and \(s\)?
2. Can this reduced action be obtained from a geometric invariant or constrained variational principle?
3. Why does mass couple to \(s\) with coefficient \(16\pi G K_s/c^2\)?
4. Why does mass not source exterior \(\kappa\)?
5. Is \(M_\kappa^2\kappa^2\) a real physical suppression term, a constraint artifact, or a reduced expression of a deeper geometric condition?
6. What happens in nonspherical or rotating cases?
7. Can the reduced action recover exact Schwarzschild, or only the weak-field exterior?
8. Does the theory predict deviations from GR when \(\kappa\) suppression is imperfect?
9. Can this action be connected to vacuum burden reduction?
10. Can the same variational principle handle gravitational waves or time-dependent fields?

---

## Suggested Next Forge Work

The next script should likely test one of two directions.

### Option A: Covariant-Parent Search

A script or symbolic note that asks:

```text
What geometric quantities reduce to kappa and s in static spherical symmetry?
```

This would begin the transition from reduced variables to metric/tensor language.

Possible file:

```text
candidate_covariant_parent_modes.py
```

or:

```text
candidate_covariant_parent_modes.md
```

### Option B: Imperfect Kappa Suppression

A script that explores deviations when \(\kappa\) is small but nonzero:

$$\kappa=\varepsilon_\kappa(r).$$

Then:

$$AB=e^{2\varepsilon_\kappa}.$$

This could test possible deviations from GR-like reciprocal scaling.

Possible file:

```text
candidate_kappa_leak_deviation.py
```

This may be useful later for novel predictions.

---

## Summary

The candidate reduced exterior action is:

$$L
=
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s.$$

With:

$$\alpha=\frac{16\pi G K_s}{c^2},$$

variation gives:

$$-2K_\kappa\nabla^2\kappa+2M_\kappa^2\kappa=0,$$

and:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

In the static source-free exterior:

$$\kappa=0.$$

For a spherical mass \(M\):

$$s(r)=-\frac{2GM}{rc^2}.$$

Therefore:

$$A=e^s,$$

$$B=e^{-s},$$

and:

$$AB=1.$$

In weak field:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

This candidate unifies the reduced exterior compensation and shear source-law mechanisms in one toy variational structure.

It is not yet the full theory, but it is the clearest reduced action candidate so far.
