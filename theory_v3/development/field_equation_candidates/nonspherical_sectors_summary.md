# Nonspherical Sectors Summary

## Purpose

This document summarizes the `05_nonspherical_sectors/` development group.

This group marks the end of the first nonspherical-sector inventory. It does not construct the full vector or tensor theory yet. Instead, it establishes what the scalar \(A\)-flux branch can do, where it fails, and what must be added next.

The most important conclusion is:

```text
Scalar gravity is ruled out as a complete theory.
```

More precisely:

```text
The scalar A-flux law survives as the weak Newtonian / monopole / scalar
multipole sector, but it cannot reproduce the full degree content of gravity.
It cannot produce frame dragging, trace-free spatial shear, or tensor
gravitational waves.
```

This is not a failure of the scalar branch. It is a boundary result.

The scalar branch remains valuable, but only as one sector of a larger theory.

---

## Directory Scope

This group contains studies beyond static spherical scalar mechanics.

It asks:

```text
Can the areal A-flux law extend beyond spherical symmetry?
If yes, how far?
Where does it fail?
What additional sectors are required?
```

The files in this group are:

```text
candidate_multipole_areal_flux_extension.py
candidate_multipole_areal_flux_extension.md

candidate_weak_multipole_metric_reconstruction.py
candidate_weak_multipole_metric_reconstruction.md

candidate_nonspherical_degree_inventory.py
candidate_nonspherical_degree_inventory.md

candidate_vector_sector_frame_dragging.py
candidate_vector_sector_frame_dragging.md

candidate_wave_sector_linearized_modes.py
candidate_wave_sector_linearized_modes.md
```

This group should be read as a sector-boundary map.

The next group should begin the tensor-flux/radiation program.

---

## Main Result

The main result is a split conclusion.

### Positive Result

The scalar \(A\)-flux law has a natural weak nonspherical extension.

Use:

$$A=1+\frac{2\Phi}{c^2}.$$

Then Newtonian Poisson:

$$\nabla^2\Phi=4\pi G\rho$$

becomes:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

In vacuum:

$$\nabla^2A=0.$$

Thus \(A\) carries ordinary weak harmonic multipoles.

This means the scalar branch is not trapped in spherical symmetry at weak order.

### Negative Result

The scalar branch is not a complete gravity theory.

A scalar field cannot represent:

```text
trace-free spatial shear,
frame dragging / gravitomagnetic vector modes,
transverse-traceless gravitational waves,
full nonlinear nonspherical metric reconstruction.
```

Therefore:

```text
The theory cannot be only scalar A-flux.
```

The scalar flux law is the scalar/monopole channel, not the whole theory.

---

## Study 1: Multipole Areal-Flux Extension

Files:

```text
candidate_multipole_areal_flux_extension.py
candidate_multipole_areal_flux_extension.md
```

This study asked whether the spherical areal-flux law can be interpreted as the monopole sector of a weak nonspherical field law.

The key identification was:

$$A=1+\frac{2\Phi}{c^2}.$$

Then:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

This is exactly Newtonian Poisson rewritten in terms of \(A\).

In vacuum:

$$\nabla^2A=0.$$

The study checked exterior harmonic multipole radial modes:

$$f_\ell(r)=\frac1{r^{\ell+1}}.$$

These are harmonic for the tested modes.

It also checked regular interior harmonic modes:

$$f_\ell(r)=r^\ell.$$

The key flux result was that total surface flux selects only the monopole:

$$\oint r^2\partial_r A\,d\Omega
=
\frac{8\pi GM}{c^2}.
$$

Higher multipoles affect angular structure but integrate to zero net mass flux.

This result means:

```text
The spherical A-flux law is the monopole/Gauss-law form of a weak scalar
A-Poisson equation.
```

This is a real extension beyond spherical symmetry, but only in the weak scalar sector.

---

## Study 2: Weak Multipole Metric Reconstruction

Files:

```text
candidate_weak_multipole_metric_reconstruction.py
candidate_weak_multipole_metric_reconstruction.md
```

This study asked whether the weak scalar \(A\)-multipole field reconstructs the expected weak metric factors.

Let:

$$\psi=\frac{\Phi}{c^2}.$$

Then:

$$A=1+2\psi.$$

Reciprocal compensation gives:

$$B=\frac1A.$$

Expanding:

$$B=\frac1{1+2\psi}
=
1-2\psi+4\psi^2-\cdots.
$$

To first order:

$$B\approx1-2\psi.$$

This matches the standard weak scalar spatial factor:

$$g_{ij}\sim(1-2\psi)\delta_{ij}.$$

The study also compared to a PPN-like spatial factor:

$$1-2\gamma\psi.$$

Matching gives:

$$\gamma=1.$$

Therefore:

```text
The scalar branch reproduces the standard gamma=1 weak scalar metric structure
at first order.
```

This is another positive result.

But the same study also showed what scalar \(A\) cannot do. A scalar conformal spatial factor is pure trace. It cannot represent arbitrary trace-free spatial shear, vector/frame-dragging components, or tensor waves.

---

## Study 3: Nonspherical Degree Inventory

Files:

```text
candidate_nonspherical_degree_inventory.py
candidate_nonspherical_degree_inventory.md
```

This study made the claim boundary explicit.

A symmetric four-dimensional metric has:

```text
g_tt: 1 component
g_ti: 3 components
g_ij: 6 symmetric spatial components
```

The current scalar \(A\)-sector covers only the weak temporal scalar/Newtonian part.

The inventory identified the current sectors:

| Sector | Status | Role |
|---|---|---|
| scalar \(A/\Phi\) | present | Newtonian potential, weak multipoles |
| scalar spatial conformal | present at first order | \(\gamma=1\) scalar spatial metric |
| \(\kappa\) trace response | reduced/interior candidate | matter trace/interior deviation |
| trace-free spatial shear | missing | anisotropic spatial geometry |
| vector \(g_{ti}\) | missing | frame dragging / rotation |
| tensor TT | missing | gravitational waves |
| nonlinear closure | missing | strong nonspherical gravity |

The key inventory result was:

```text
The current theory has a credible weak scalar sector, but not a full
nonspherical gravity sector.
```

This is where scalar gravity is effectively disproved as a complete theory.

The scalar branch works as a sector. It fails as the whole theory.

---

## Study 4: Vector Sector / Frame Dragging

Files:

```text
candidate_vector_sector_frame_dragging.py
candidate_vector_sector_frame_dragging.md
```

This study asked whether scalar \(A\) or \(\kappa\) can reproduce frame dragging.

The answer was no.

Frame dragging requires off-diagonal metric components:

$$g_{ti}\neq0.$$

The scalar branch has:

$$h_{ti}=0.$$

Therefore scalar \(A\) cannot produce frame dragging.

The study introduced a candidate vector sector:

$$W_i=(W_x,W_y,W_z).$$

The source-channel split became:

```text
density / mass -> scalar A
mass current / spin -> vector W_i
```

For angular momentum along \(z\):

$$\vec J=J\hat z,$$

the study tested a dipole-like exterior vector potential:

$$\vec W\sim\frac{\vec J\times\vec r}{r^3}.$$

This has nonzero curl and is structurally appropriate for frame-dragging-like behavior.

The result was not a derivation of frame dragging. It was a necessity proof:

```text
Frame dragging requires an independent vector sector.
```

This further rules out scalar-only gravity.

---

## Study 5: Wave Sector / Linearized Modes

Files:

```text
candidate_wave_sector_linearized_modes.py
candidate_wave_sector_linearized_modes.md
```

This study asked whether the current scalar \(A\), \(\kappa\), or vector \(W_i\) sectors contain gravitational waves.

The answer was no.

A gravitational wave in the linearized tensor sector is represented by a transverse-traceless spatial perturbation:

$$h_{ij}^{TT}.$$

For a wave propagating in the \(z\)-direction:

$$
h_{ij}^{TT}
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

This has:

```text
two polarizations,
zero trace,
transversality.
```

The scalar spatial perturbation is:

$$h_{ij}^{\rm scalar}=-2\psi\delta_{ij}.$$

Its trace is:

$$-6\psi.$$

So it is not transverse-traceless.

The vector sector \(W_i\) lives in \(g_{ti}\)-type components, not in \(h_{ij}^{TT}\).

Therefore:

```text
Scalar A is not a gravitational wave mode.
Vector W_i is not a gravitational wave mode.
A full theory needs a tensor h_ij^TT sector.
```

This is the strongest failure control in the group.

It proves that scalar flux law alone cannot allow gravitational waves.

---

## Scalar Gravity Is Disproved as a Complete Theory

This group gives a clean answer to the scalar-gravity question.

If by scalar gravity we mean:

```text
all gravitational phenomena are carried by scalar A-flux alone,
```

then that theory is disproved by the degree inventory.

Scalar \(A\) can carry:

```text
mass monopole,
Newtonian potential,
weak scalar multipoles,
first-order gamma=1 scalar spatial response.
```

Scalar \(A\) cannot carry:

```text
frame dragging,
tensor gravitational waves,
trace-free spatial shear,
full nonlinear nonspherical geometry.
```

Therefore:

```text
scalar A-flux is necessary but not sufficient.
```

The correct interpretation is:

```text
A-flux is the scalar/monopole channel of a larger vacuum response theory.
```

This motivates a multipole-sector architecture.

---

## Current Sector Architecture

The current architecture is:

### Scalar / Monopole Channel

Variable:

$$A.$$

Source:

```text
density / mass.
```

Role:

```text
Newtonian potential,
mass flux,
weak scalar multipoles,
static spherical exterior.
```

Flux law:

$$F_A=4\pi r^2A'=\frac{8\pi GM}{c^2}.$$

Weak local law:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

### Trace / Interior Channel

Variable:

$$\kappa.$$

Source candidate:

```text
pressure,
stress,
traceful matter response.
```

Role:

```text
interior deviation,
matter response,
exterior suppression.
```

Exterior condition:

$$\kappa=0.$$

### Vector / Current Channel

Variable:

$$W_i.$$

Source candidate:

```text
mass current,
angular momentum,
spin.
```

Role:

```text
frame dragging,
gravitomagnetic effects.
```

Status:

```text
identified as necessary,
not yet normalized or derived.
```

### Tensor / Quadrupole Wave Channel

Variable:

$$h_{ij}^{TT}.$$

Source candidate:

```text
changing quadrupole / TT stress.
```

Role:

```text
gravitational waves,
radiation,
two tensor polarizations.
```

Status:

```text
missing,
must be added or derived.
```

---

## What We Are Going To Do About It

The scalar-only version is not enough. The next stage should not try to force waves into \(A\). That would be the wrong move.

Instead, the next development group should build the tensor-flux/radiation sector.

The conceptual upgrade is:

```text
A-flux is the monopole/scalar flux channel.
Gravitational waves should be treated as a quadrupole/tensor flux channel.
```

The next folder should likely be:

```text
06_tensor_flux_principle/
```

or:

```text
06_tensor_flux_and_radiation/
```

The goal of that group should be:

```text
Develop a tensor-flux principle in which h_ij^TT carries quadrupole
radiative vacuum flow, analogous to A carrying monopole scalar flow.
```

The first studies should probably be:

```text
candidate_scalar_flux_no_wave_failure_control.py
candidate_tensor_flux_principle.py
candidate_tensor_sector_placeholder_action.py
candidate_quadrupole_radiation_source.py
candidate_wave_speed_polarization_test.py
```

The first one is important because it should record the failure control:

```text
The scalar flux law cannot produce gravitational waves.
```

That is a guardrail for the rest of the program.

---

## Current Best Claim

The strongest safe claim after this group is:

```text
The scalar A-flux law extends naturally to weak nonspherical scalar multipoles
and reproduces the first-order gamma=1 scalar metric structure.

However, scalar A-flux is not a complete theory of gravity. It lacks
trace-free spatial shear, vector frame-dragging modes, and tensor
gravitational waves.

Therefore the theory must become a multi-sector vacuum response theory.
```

In short:

```text
Scalar gravity is dead as the whole theory.
Scalar flux survives as the monopole channel.
```

---

## Closing Summary

The `05_nonspherical_sectors/` group ends with a useful boundary.

It showed that the scalar \(A\)-branch is stronger than a purely spherical trick:

$$A=1+\frac{2\Phi}{c^2}$$

works for weak scalar multipoles, and reciprocal compensation gives:

$$B=\frac1A\approx1-\frac{2\Phi}{c^2}.$$

So the scalar branch reproduces the weak scalar metric sector.

But it also showed that scalar \(A\) cannot produce the full gravitational field.

Frame dragging requires a vector sector:

$$W_i.$$

Gravitational waves require a tensor sector:

$$h_{ij}^{TT}.$$

Trace-free spatial shear requires additional spatial degrees of freedom.

Thus this directory group closes with a decision:

```text
Do not continue as scalar gravity.
Promote the theory to a multi-sector vacuum response model.
Build tensor-flux/radiation next.
```
