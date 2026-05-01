# Candidate Multipole Areal-Flux Extension

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full nonspherical gravity theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_multipole_areal_flux_extension.py
```

The guiding question was:

```text
Can the areal-flux law survive beyond perfect spherical symmetry, at least
in the weak-field multipole limit?
```

The answer is yes, in a cautious weak-field sense.

The areal-flux law has a natural weak multipole extension if:

$$A=1+\frac{2\Phi}{c^2},$$

where \(\Phi\) is the Newtonian potential.

Then Newtonian Poisson:

$$\nabla^2\Phi=4\pi G\rho$$

becomes:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

In vacuum:

$$\nabla^2A=0.$$

Therefore \(A\) supports the usual harmonic multipole expansion.

This keeps the reduced exterior program compatible with weak nonspherical Newtonian gravity.

However, this does not solve the full nonlinear nonspherical problem. A single scalar \(A\) is not enough to define the full spatial metric in general nonspherical fields.

---

## Background

The strongest static spherical branch uses the exterior areal-flux law:

$$F_A(r)=4\pi r^2A'(r),$$

with:

$$F_A=\frac{8\pi GM}{c^2}.$$

This gives:

$$A=1-\frac{2GM}{rc^2}.$$

With exterior compensation:

$$\kappa=0,$$

we have:

$$B=\frac1A.$$

Thus the exact Schwarzschild exterior metric factors are recovered in areal gauge.

The concern is that this is a spherical result. Real weak gravitational fields can have multipoles.

The present study asks whether the \(A\)-source law at least reproduces weak nonspherical Newtonian behavior.

---

## Spherical Recap

For a spherical mass:

$$A_{\rm sph}=1-\frac{2GM}{c^2r}.$$

Then:

$$A_{\rm sph}'=\frac{2GM}{c^2r^2}.$$

The areal flux is:

$$F_A=4\pi r^2A'=\frac{8\pi GM}{c^2}.$$

The script confirmed that the spherical flux gives the Schwarzschild coefficient.

This is the monopole case.

---

## Weak-Field Identification

In weak field, identify:

$$A=1+\frac{2\Phi}{c^2}.$$

Then:

$$\nabla^2A=\frac{2}{c^2}\nabla^2\Phi.$$

Newtonian gravity gives:

$$\nabla^2\Phi=4\pi G\rho.$$

Therefore:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

So the reduced \(A\)-source law is exactly Newtonian Poisson written in terms of \(A\).

This supports the idea that the spherical areal-flux law is the monopole sector of a weak-field Poisson law for \(A\).

---

## Vacuum Harmonic Multipoles

In vacuum:

$$\rho=0.$$

So:

$$\nabla^2A=0.$$

For separated spherical harmonic modes:

$$A_{\ell m}(r,\theta,\phi)=f_\ell(r)Y_{\ell m}(\theta,\phi),$$

the radial operator is:

$$
\frac1{r^2}\frac{d}{dr}
\left(
r^2\frac{df_\ell}{dr}
\right)
-
\frac{\ell(\ell+1)}{r^2}f_\ell.
$$

The exterior harmonic radial modes are:

$$f_\ell(r)=\frac1{r^{\ell+1}}.$$

The script checked:

```text
ell = 0, 1, 2, 3, 4
```

and confirmed:

$$\nabla^2\left(r^{-(\ell+1)}Y_{\ell m}\right)=0$$

for each tested exterior mode.

Thus the weak exterior \(A\)-field can carry ordinary harmonic multipoles.

---

## Regular Interior Harmonic Modes

The regular interior harmonic radial modes are:

$$f_\ell(r)=r^\ell.$$

The script checked:

```text
ell = 0, 1, 2, 3, 4
```

and confirmed that each is harmonic under the corresponding separated-mode operator.

This shows that the standard regular/harmonic mode structure is available in the weak limit.

This is not a full interior source model. It only confirms that the weak \(A\)-Poisson law has the expected multipole basis.

---

## Surface Flux Selects the Monopole

The script tested a toy axisymmetric field:

$$
A
=
1-\frac{2GM}{c^2r}
+
\frac{Q}{r^3}P_2(\mu),
$$

where:

$$\mu=\cos\theta,$$

and:

$$P_2(\mu)=\frac12(3\mu^2-1).$$

The surface flux is:

$$
\oint r^2\partial_rA\,d\Omega.
$$

The quadrupole term integrates to zero over the sphere.

The script found:

$$
\oint r^2\partial_rA\,d\Omega
=
\frac{8\pi GM}{c^2}.
$$

Thus the total surface flux measures only the monopole mass.

Higher multipoles redistribute the angular field but do not change the net flux.

This is exactly what should happen in the weak Newtonian limit.

---

## Dipole Caution

The script tested a pure dipole mode:

$$A_{\rm dipole}=\frac{D\mu}{r^2}.$$

The surface flux integral is zero:

$$\oint r^2\partial_rA_{\rm dipole}\,d\Omega=0.$$

This confirms that a pure dipole carries no net mass flux.

However, dipole terms require care because they depend on origin choice and center-of-mass frame.

This is a coordinate/gauge warning for any future multipole extension.

---

## Linear Compensated Metric From Multipole A

Let:

$$\psi=\frac{\Phi}{c^2}.$$

Then:

$$A=1+2\psi.$$

If the exterior compensated condition is applied formally:

$$\kappa=0,$$

then:

$$B=\frac1A.$$

Expanding:

$$B=\frac1{1+2\psi}.$$

To second order:

$$B\approx1-2\psi+4\psi^2.$$

To first order:

$$B\approx1-2\psi.$$

For attractive gravity:

$$\Phi<0,$$

so:

$$A<1,$$

and:

$$B>1.$$

This matches the expected weak-field sign behavior.

The script confirmed that reciprocal compensation extends formally to weak nonspherical \(A\).

However, this is only a scalar/diagonal analogy. A full nonspherical metric cannot be determined by a single scalar \(A\) and one reciprocal \(B\).

---

## Nonlinear Nonspherical Caution

The weak multipole extension is natural:

$$A=1+\frac{2\Phi}{c^2},$$

and:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

In vacuum:

$$\nabla^2A=0.$$

But the exact nonlinear spherical branch uses:

$$B=\frac1A,$$

and:

$$\kappa=0.$$

For general nonspherical fields, a single scalar \(A\) is not enough to define the full spatial metric.

There are tensor/shear degrees of freedom that do not appear in the spherical \(A/B\) reciprocal pair.

Therefore:

```text
This study supports weak multipoles.
It does not produce a full nonlinear nonspherical gravity theory.
```

---

## What This Study Established

This study established:

1. The spherical areal-flux law is the monopole sector of a weak \(A\)-Poisson law.
2. The weak-field identification is:
   $$A=1+2\Phi/c^2.$$
3. Newtonian Poisson becomes:
   $$\nabla^2A=8\pi G\rho/c^2.$$
4. Vacuum exterior \(A\) supports harmonic multipoles.
5. Exterior radial modes:
   $$r^{-(\ell+1)}$$
   are harmonic for tested \(\ell\).
6. Regular interior modes:
   $$r^\ell$$
   are harmonic for tested \(\ell\).
7. Total surface flux selects only the monopole mass.
8. Higher multipoles affect angular field distribution but not net flux.
9. Dipole modes carry zero net flux and require origin/center-of-mass care.
10. Formal reciprocal compensation extends at first weak-field order.
11. The full nonlinear nonspherical problem remains open.

---

## What This Study Did Not Establish

This study did not derive a nonlinear nonspherical field equation.

It did not construct a full nonspherical metric.

It did not handle frame dragging.

It did not handle gravitational waves.

It did not handle tensor degrees of freedom.

It did not prove that \(\kappa=0\) is meaningful for arbitrary nonspherical fields.

It did not derive a covariant parent equation.

It only showed that the reduced \(A\)-source law is compatible with weak Newtonian multipoles.

---

## Relationship to the Existing Program

This result connects the static spherical mechanics branch to weak nonspherical Newtonian gravity.

Previously, the main law was:

$$F_A=4\pi r^2A'=\frac{8\pi GM}{c^2}.$$

This is the integrated monopole form.

The multipole extension says the weak local form is:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

The monopole flux law follows by integrating over a sphere.

Higher multipoles have zero net surface flux but still appear in the angular structure of \(A\).

Thus the source map becomes:

```text
monopole mass:
  net A-flux

higher moments:
  angular distribution of A

source-free exterior:
  harmonic A field

nonlinear completion:
  still open
```

---

## Current Best Interpretation

The current best interpretation is:

```text
The areal-flux law is not restricted to spherical symmetry at weak order.
It is the monopole flux form of the weak A-Poisson equation.

Weak nonspherical fields can be represented by harmonic multipoles of A.

However, the exact nonlinear nonspherical theory requires additional
geometric degrees of freedom beyond scalar A.
```

This is a positive but limited result.

It keeps the theory from being immediately trapped in spherical symmetry, while clearly identifying the next major gap.

---

## Next Development Targets

### 1. Weak Multipole Metric Reconstruction

A possible next script:

```text
candidate_weak_multipole_metric_reconstruction.py
```

Purpose:

```text
Compare weak multipole A fields to standard weak-field metric perturbations
and identify which spatial components are missing from scalar reciprocal
compensation.
```

### 2. Tensor / Shear Degree Inventory

A possible note:

```text
candidate_nonspherical_degree_inventory.md
```

Purpose:

```text
List the additional degrees of freedom required beyond spherical A and B.
```

### 3. Frame-Dragging / Vector Sector

A later script:

```text
candidate_vector_sector_frame_dragging.py
```

Purpose:

```text
Ask what mode would reproduce weak gravitomagnetic/frame-dragging effects.
```

### 4. Wave Sector

A later script:

```text
candidate_wave_sector_linearized_modes.py
```

Purpose:

```text
Identify whether the theory has propagating tensor modes or only scalar modes.
```

---

## Summary

The multipole areal-flux extension passed as a weak-field diagnostic.

Using:

$$A=1+\frac{2\Phi}{c^2},$$

Newtonian Poisson becomes:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

In vacuum:

$$\nabla^2A=0,$$

so \(A\) carries the usual harmonic multipoles.

The total surface flux:

$$\oint r^2\partial_rA\,d\Omega$$

selects only the monopole mass:

$$\frac{8\pi GM}{c^2}.$$

Higher multipoles affect angular structure but not net flux.

This keeps the reduced exterior program compatible with weak nonspherical Newtonian gravity.

The full nonlinear nonspherical theory remains open.
