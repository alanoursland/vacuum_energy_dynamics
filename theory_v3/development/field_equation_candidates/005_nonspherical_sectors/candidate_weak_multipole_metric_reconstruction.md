# Candidate Weak Multipole Metric Reconstruction

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full nonspherical gravitational theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_weak_multipole_metric_reconstruction.py
```

The guiding question was:

```text
Can the weak A-multipole sector reconstruct the standard weak scalar metric,
and what metric degrees of freedom remain missing?
```

The answer is:

```text
Yes, the weak scalar sector works.

A=1+2Phi/c² reconstructs the weak temporal scalar metric, and reciprocal
compensation gives the scalar spatial factor 1-2Phi/c² at first order.

But this is not a full nonspherical gravity theory. Spatial shear,
vector/frame-dragging modes, tensor/wave modes, and nonlinear closure remain
missing.
```

---

## Background

The previous multipole extension showed that the reduced \(A\)-source law has a natural weak-field form:

$$A=1+\frac{2\Phi}{c^2},$$

where \(\Phi\) is the Newtonian potential.

Then Newtonian Poisson,

$$\nabla^2\Phi=4\pi G\rho,$$

becomes:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

In vacuum:

$$\nabla^2A=0.$$

Thus \(A\) can carry ordinary weak harmonic multipoles.

The present reconstruction study asks whether this \(A\)-sector also gives the expected weak metric factors.

---

## Weak Metric Target

Let:

$$\psi=\frac{\Phi}{c^2}.$$

The standard weak scalar metric has temporal factor:

$$A=1+2\psi,$$

and scalar spatial conformal factor:

$$1-2\psi.$$

Equivalently:

$$g_{tt}\sim-(1+2\psi)c^2,$$

and:

$$g_{ij}\sim(1-2\psi)\delta_{ij}.$$

The script used this as the target scalar sector.

---

## Reciprocal Compensation at Weak Order

In the reduced compensated exterior branch:

$$\kappa=0.$$

In spherical form this gives:

$$AB=1,$$

so:

$$B=\frac1A.$$

For the weak scalar sector, take:

$$A=1+2\psi.$$

Then:

$$B_{\rm recip}=\frac1{1+2\psi}.$$

Expanding:

$$B_{\rm recip}=1-2\psi+4\psi^2-8\psi^3+\cdots.$$

To first order:

$$B_{\rm recip}\approx1-2\psi.$$

This matches the standard weak scalar spatial factor.

The script confirmed:

```text
reciprocal compensation matches scalar spatial factor at first order.
```

---

## Gamma Proxy

A PPN-like scalar spatial factor can be written:

$$1-2\gamma\psi.$$

Reciprocal compensation gives:

$$1-2\psi.$$

Matching gives:

$$\gamma=1.$$

Thus, in the weak scalar sector, reciprocal compensation reproduces the \(\gamma=1\) spatial curvature factor.

This is important because \(\gamma=1\) is the GR value for the standard weak-field scalar sector.

Caution:

```text
This is only a scalar-sector proxy.
It is not a full PPN derivation.
```

---

## Multipole Scalar Potential Reconstruction

The script used a weak multipole potential of the form:

$$
\psi
=
-\frac{\bar M}{r}
+
\frac{Q}{r^3}P_2(\mu),
$$

where:

$$\mu=\cos\theta,$$

and:

$$P_2(\mu)=\frac12(3\mu^2-1).$$

Then:

$$A=1+2\psi,$$

and the scalar spatial factor is:

$$1-2\psi.$$

Thus the same weak multipole potential controls both:

```text
the temporal scalar factor,
and the scalar conformal spatial factor.
```

This is the expected weak scalar metric structure with \(\gamma=1\).

---

## Vacuum Harmonic Modes

The script confirmed that the scalar multipole modes remain harmonic in vacuum.

For separated modes:

$$f_\ell(r)Y_{\ell m}(\theta,\phi),$$

the exterior harmonic radial functions are:

$$f_\ell(r)=\frac1{r^{\ell+1}}.$$

The script checked:

```text
ell = 0, 1, 2, 3, 4
```

and confirmed that each mode is harmonic.

These are scalar \(A/\psi\) multipoles.

They are not the full tensor metric content.

---

## Anisotropic Spatial Shear Is Missing

The scalar conformal spatial perturbation has the form:

$$h_{ij}^{\rm scalar}=-2\psi\delta_{ij}.$$

In matrix form:

$$
h_{ij}^{\rm scalar}
=
\begin{pmatrix}
-2\psi & 0 & 0 \\
0 & -2\psi & 0 \\
0 & 0 & -2\psi
\end{pmatrix}.
$$

Its trace is:

$$-6\psi.$$

Its trace-free part is zero.

A general diagonal spatial perturbation is:

$$
h_{ij}^{\rm diag}
=
\begin{pmatrix}
h_{xx} & 0 & 0 \\
0 & h_{yy} & 0 \\
0 & 0 & h_{zz}
\end{pmatrix}.
$$

The trace-free diagonal shear part is:

$$
\begin{pmatrix}
\frac{2h_{xx}-h_{yy}-h_{zz}}{3} & 0 & 0 \\
0 & \frac{-h_{xx}+2h_{yy}-h_{zz}}{3} & 0 \\
0 & 0 & \frac{-h_{xx}-h_{yy}+2h_{zz}}{3}
\end{pmatrix}.
$$

A single scalar \(\psi\) fixes only the conformal/trace spatial piece.

It cannot represent arbitrary trace-free spatial shear.

Therefore a nonspherical theory needs additional spatial shear degrees of freedom.

---

## Vector / Frame-Dragging Sector Is Missing

Weak stationary rotating sources introduce off-diagonal components:

$$g_{ti}\neq0.$$

These are vector, gravitomagnetic, or frame-dragging degrees of freedom.

The scalar \(A\)-field and reciprocal scalar spatial factor do not produce \(g_{ti}\) components.

Therefore any theory that aims to reproduce rotation and frame dragging needs a vector sector beyond scalar \(A\).

---

## Tensor / Wave Sector Is Missing

Linearized gravitational waves require transverse-traceless spatial metric perturbations:

$$h_{ij}^{\rm TT}.$$

These are not captured by a scalar field:

$$A=1+2\psi.$$

Therefore the weak scalar multipole extension is not a wave-sector theory.

A viable full theory must eventually account for tensor/radiative degrees of freedom.

---

## Nonlinear Nonspherical Closure

The exact spherical branch has:

$$A=1-\frac{2GM}{rc^2},$$

$$\kappa=0,$$

and:

$$B=\frac1A.$$

The weak nonspherical scalar branch has:

$$A=1+\frac{2\Phi}{c^2},$$

and scalar spatial factor:

$$1-\frac{2\Phi}{c^2}.$$

The open nonlinear question is:

```text
How should full spatial geometry be reconstructed when Phi is nonspherical
and nonlinear effects matter?
```

The likely required sectors are:

```text
scalar A / Newtonian potential,
kappa / trace response,
spatial shear,
vector frame-dragging,
tensor waves.
```

The script explicitly marks nonlinear nonspherical closure as still open.

---

## What This Study Established

This study established:

1. \(A=1+2\Phi/c^2\) reconstructs the weak temporal scalar metric.
2. Reciprocal compensation gives:
   $$B=1/A\approx1-2\Phi/c^2.$$
3. This matches the standard scalar spatial factor at first order.
4. The scalar sector gives a \(\gamma=1\) proxy.
5. Weak scalar multipoles are compatible with the \(A\)-source law.
6. Vacuum harmonic scalar modes remain valid.
7. A single scalar cannot represent arbitrary trace-free spatial shear.
8. A single scalar cannot represent frame dragging.
9. A single scalar cannot represent tensor gravitational waves.
10. The nonlinear nonspherical closure remains open.

---

## What This Study Did Not Establish

This study did not derive full nonspherical field equations.

It did not construct the full spatial metric.

It did not include vector modes.

It did not include tensor waves.

It did not solve frame dragging.

It did not solve nonlinear nonspherical gravity.

It did not derive a covariant parent.

It only showed that the weak scalar multipole sector is compatible with the expected weak scalar metric form.

---

## Relationship to the Multipole Areal-Flux Extension

The previous multipole areal-flux study showed:

$$A=1+\frac{2\Phi}{c^2},$$

and:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

This study adds that the same \(A\) also reconstructs the weak scalar metric factors:

$$g_{tt}\sim-(1+2\Phi/c^2)c^2,$$

and:

$$g_{ij}\sim(1-2\Phi/c^2)\delta_{ij}.$$

Thus the weak scalar sector is internally consistent.

But both studies agree that scalar \(A\) is not enough for full nonspherical gravity.

---

## Current Best Interpretation

The current best interpretation is:

```text
The theory has a credible weak scalar sector.

A carries the Newtonian potential and weak scalar multipoles.

Reciprocal compensation gives the correct first-order scalar spatial factor.

But a full nonspherical theory needs additional sectors:
  trace-free spatial shear,
  vector/frame-dragging,
  tensor/wave modes,
  nonlinear closure.
```

This is a good result because it avoids an immediate spherical-symmetry trap while preventing overclaiming.

---

## Next Development Targets

### 1. Nonspherical Degree Inventory

A direct next artifact:

```text
candidate_nonspherical_degree_inventory.md
```

Purpose:

```text
Inventory which degrees of freedom are present, candidate, or missing.
```

### 2. Vector / Frame-Dragging Sector

A possible script:

```text
candidate_vector_sector_frame_dragging.py
```

Purpose:

```text
Ask what additional mode would be required to reproduce weak gravitomagnetic
effects.
```

### 3. Tensor / Wave Sector

A possible script:

```text
candidate_wave_sector_linearized_modes.py
```

Purpose:

```text
Ask whether the theory can support transverse-traceless propagating tensor modes.
```

### 4. Spatial Shear Parent

A possible script:

```text
candidate_spatial_shear_mode_extension.py
```

Purpose:

```text
Explore whether the reduced shear concept can generalize to trace-free
spatial metric perturbations.
```

---

## Summary

The weak multipole metric reconstruction passed for the scalar sector.

With:

$$A=1+\frac{2\Phi}{c^2},$$

reciprocal compensation gives:

$$B=\frac1A\approx1-\frac{2\Phi}{c^2}.$$

This reproduces the standard weak scalar metric structure and a \(\gamma=1\) proxy at first order.

However, this is not a full nonspherical theory.

The missing sectors are:

```text
trace-free spatial shear,
vector/frame-dragging,
tensor/wave modes,
nonlinear nonspherical closure.
```

The next development direction is to inventory and then build those missing sectors.
