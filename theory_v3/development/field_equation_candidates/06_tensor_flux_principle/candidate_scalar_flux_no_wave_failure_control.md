# Candidate Scalar-Flux No-Wave Failure Control

## What This Document Is

This document is a failure-control note for the tensor-flux development group.

It is not a postulate, theorem, or complete radiation theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_scalar_flux_no_wave_failure_control.py
```

The guiding question was:

```text
Can the scalar A-flux law secretly contain gravitational waves?
```

The answer is no.

The scalar \(A\)-flux law can carry the monopole/Newtonian/scalar channel:

$$A=1+\frac{2\Phi}{c^2}.$$

But gravitational waves require a transverse-traceless spatial tensor:

$$h_{ij}^{TT}.$$

The scalar spatial perturbation is pure trace/conformal and has no nontrivial transverse-traceless content.

This is an important guardrail:

```text
A-flux is not the wave sector.
A-flux is the scalar/monopole channel.
Tensor radiation requires a separate h_ij^TT sector or a deeper mechanism
that produces one.
```

---

## Background

The previous nonspherical-sector studies showed that the scalar \(A\)-branch works as the weak Newtonian scalar sector:

$$A=1+\frac{2\Phi}{c^2}.$$

Reciprocal compensation gives the weak scalar spatial factor:

$$B=\frac1A\approx1-\frac{2\Phi}{c^2}.$$

This reproduces the first-order \(\gamma=1\) scalar spatial metric factor.

However, gravitational waves are not scalar conformal perturbations.

In linearized gravity, the radiative wave sector is described by a transverse-traceless tensor:

$$h_{ij}^{TT}.$$

For a wave propagating along the \(z\)-direction, the standard TT form is:

$$
h_{ij}^{TT}
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

It has two polarizations:

```text
h_plus
h_cross
```

The question was whether scalar \(A\) could somehow reproduce that structure.

It cannot.

---

## Scalar Spatial Perturbation Is Not Trace-Free

The scalar spatial perturbation is:

$$h_{ij}^{\rm scalar}=-2\psi\delta_{ij},$$

where:

$$\psi=\frac{\Phi}{c^2}.$$

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

$$\mathrm{Tr}(h^{\rm scalar})=-6\psi.$$

A TT gravitational wave must be trace-free.

Therefore the scalar conformal perturbation is not a TT wave unless:

$$\psi=0.$$

The script confirmed this directly.

---

## Trace-Free Projection of the Scalar Mode Vanishes

The trace-free projection is:

$$
h_{ij}^{TF}
=
h_{ij}
-
\frac13\mathrm{Tr}(h)\delta_{ij}.
$$

For the scalar conformal perturbation:

$$h_{ij}^{\rm scalar}=-2\psi\delta_{ij},$$

the trace-free projection is:

$$h_{ij}^{TF}=0.$$

Thus the scalar spatial mode has no TT content after removing the trace.

This is one of the cleanest algebraic statements in the whole batch:

```text
The scalar A mode has zero trace-free tensor content.
```

---

## Scalar Breathing Mode Versus TT Plus/Cross

A scalar transverse breathing-like mode for propagation along \(z\) can be represented as:

$$
h_{ij}^{\rm breathing}
=
\begin{pmatrix}
\psi & 0 & 0 \\
0 & \psi & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

Its trace is:

$$2\psi.$$

A tensor TT mode is:

$$
h_{ij}^{TT}
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

Its trace is:

$$0.$$

So a scalar breathing mode is not the same as a tensor wave.

The script confirmed:

```text
breathing mode is not trace-free unless trivial;
TT plus/cross mode is trace-free.
```

This matters because a scalar wave equation could produce scalar radiation, but that would not be the observed two-polarization tensor wave sector.

---

## No Scalar Psi Reproduces Nontrivial TT Modes

The script solved the equation:

$$H_{\rm scalar}=H_{TT}.$$

The only solution was:

$$\psi=0,$$

$$h_+=0,$$

$$h_\times=0.$$

Therefore a scalar conformal perturbation cannot generate nonzero plus/cross modes.

This proves:

```text
There is no nontrivial scalar=TT identification.
```

The scalar channel and the tensor channel are algebraically distinct.

---

## Transversality Alone Is Not Enough

The script also checked a transverse scalar breathing mode.

For propagation along \(z\), a breathing mode can satisfy:

$$k^ih_{ij}=0.$$

But it still has nonzero trace:

$$\mathrm{Tr}(h)=2\psi.$$

Therefore transversality alone does not make a mode a GR tensor wave.

A TT wave must be both:

```text
transverse
and
traceless.
```

The scalar breathing mode fails the traceless condition.

---

## Scalar Wave Equation Would Be Scalar Radiation

Suppose scalar \(\psi\) obeys a wave equation:

$$\Box\psi=0.$$

A plane-wave scalar solution can be written:

$$\psi=H\cos(kz-\omega t).$$

The scalar wave equation gives the dispersion relation:

$$\omega^2=c^2k^2.$$

So a scalar field could propagate.

But this would be scalar radiation, not TT tensor gravitational radiation.

The script confirmed:

```text
scalar wave equation is not a tensor wave equation.
```

This is an important distinction.

The problem is not merely propagation. The problem is polarization and tensor structure.

---

## Required Tensor Sector

A gravitational wave sector requires a tensor of the form:

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
two tensor polarizations,
zero trace,
transverse spatial structure.
```

Therefore the theory needs:

```text
an independent h_ij^TT sector,
or a deeper vacuum mechanism that produces h_ij^TT.
```

Scalar \(A\)-flux cannot do it.

---

## What This Study Established

This study established:

1. The scalar spatial perturbation is pure trace/conformal.
2. Its trace is:
   $$-6\psi.$$
3. Its trace-free projection is zero.
4. Scalar breathing modes are not TT modes.
5. No nonzero scalar \(\psi\) reproduces \(h_+\) or \(h_\times\).
6. A scalar wave equation would produce scalar radiation, not GR tensor waves.
7. Gravitational waves require an independent \(h_{ij}^{TT}\) sector.

---

## What This Study Did Not Establish

This study did not build the tensor sector.

It did not derive gravitational-wave equations.

It did not derive quadrupole radiation.

It did not derive a tensor-flux principle.

It did not decide whether \(h_{ij}^{TT}\) is fundamental or emergent.

It only proves that the scalar flux law cannot be the wave sector.

---

## Why This Matters

This is an important failure control.

Without it, one might overclaim:

```text
A-flux explains gravity, so maybe it also explains waves.
```

That is false.

The correct statement is:

```text
A-flux explains the scalar/monopole/Newtonian channel.
Tensor radiation requires a separate quadrupole/TT channel.
```

This supports the move from scalar flux to tensor flux.

---

## Current Best Interpretation

The current best interpretation is:

```text
A-flux is the monopole scalar vacuum-response channel.

Tensor flux should be the quadrupole transverse-traceless radiative channel.

The scalar law does not contain the tensor law.
```

Thus the next development group should not try to force waves into \(A\).

It should build the TT tensor sector directly.

---

## Next Development Targets

### 1. Tensor Flux Basis

A direct next script:

```text
candidate_tensor_flux_basis.py
```

Purpose:

```text
Define TT basis tensors, plus/cross polarizations, trace-free and transverse
conditions, and prepare the tensor-flux channel.
```

### 2. Tensor Wave Equation

A later script:

```text
candidate_tensor_wave_equation.py
```

Purpose:

```text
Test plane-wave solutions and propagation speed for h_ij^TT.
```

### 3. Quadrupole Tensor Flux

A later script:

```text
candidate_quadrupole_tensor_flux.py
```

Purpose:

```text
Connect TT radiation to changing quadrupole source structure.
```

---

## Summary

The scalar-flux no-wave failure control proves that the scalar \(A\)-flux law is not secretly a gravitational-wave theory.

The scalar spatial perturbation:

$$h_{ij}^{\rm scalar}=-2\psi\delta_{ij}$$

is pure trace.

Its trace-free projection vanishes.

A scalar breathing mode is not a TT tensor wave.

No nonzero scalar \(\psi\) reproduces \(h_+\) or \(h_\times\).

Therefore:

```text
A-flux remains the monopole/scalar/Newtonian channel.
Gravitational radiation requires h_ij^TT.
```

The next step is to build the tensor-flux basis.
