# Candidate Wave Sector Linearized Modes

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or derived gravitational-wave theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_wave_sector_linearized_modes.py
```

The guiding question was:

```text
Do the current scalar A, kappa, and vector W_i sectors contain gravitational
waves, or does the theory require an independent tensor wave sector?
```

The answer is:

```text
The current reduced program does not yet contain gravitational waves.

Scalar A handles Newtonian/mass-flux physics.
Vector W_i is the natural home for frame dragging.
Radiative gravity requires a separate transverse-traceless tensor sector
h_ij^TT, or a deeper mechanism that produces one.
```

This is not a failure of the scalar branch.

It is a degree-inventory result.

---

## Current Sector Map

The current reduced program has several candidate sectors:

```text
scalar A -> Newtonian potential / mass flux
kappa -> trace/interior response candidate
vector W_i -> frame-dragging candidate
```

The missing sector is:

```text
tensor transverse-traceless wave sector h_ij^TT
```

A full relativistic gravity theory must address propagating waves.

The script isolated this as an explicit open problem.

---

## Scalar Spatial Mode Is Not Transverse-Traceless

The scalar spatial perturbation has the form:

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

$$\mathrm{Tr}(h^{\rm scalar})=-6\psi.$$

A transverse-traceless tensor must be trace-free.

Therefore the scalar conformal perturbation is not a tensor wave mode unless:

$$\psi=0.$$

The script confirmed:

```text
scalar mode is not TT.
```

Interpretation:

```text
The scalar A branch cannot itself be the gravitational wave sector.
```

---

## Vector Mode Is Not a TT Spatial Tensor

The vector sector is represented by:

$$W_i=(W_x,W_y,W_z).$$

This sector lives in off-diagonal components:

$$g_{ti}.$$

It is the natural home for frame dragging and gravitomagnetic effects.

But tensor waves live in symmetric spatial perturbations:

$$h_{ij}^{TT}.$$

Therefore \(W_i\) is not a transverse-traceless spatial tensor.

The script confirmed:

```text
vector sector is distinct from tensor wave sector.
```

Interpretation:

```text
Adding W_i may help with rotation and frame dragging,
but it does not solve gravitational radiation.
```

---

## TT Tensor Polarizations

For a wave propagating in the \(z\)-direction, a transverse-traceless spatial perturbation can be written:

$$
h_{ij}^{TT}
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

The trace is:

$$h_+ - h_+ + 0 = 0.$$

The two independent polarizations are:

```text
h_plus
h_cross
```

The script confirmed:

```text
TT tensor has two polarizations.
```

This is the structure expected for linearized gravitational waves.

---

## Transversality Check

For a wave vector along the \(z\)-axis:

$$k^i=(0,0,k),$$

transversality requires:

$$k^i h_{ij}=0.$$

Using the TT matrix above:

$$k^i h_{ij}^{TT}=(0,0,0).$$

The script confirmed:

```text
TT mode is transverse for propagation along z.
```

Thus the candidate tensor wave sector must be spatial, trace-free, and transverse.

Scalar \(A\) and vector \(W_i\) do not satisfy this role.

---

## Candidate Wave Equation Placeholder

A tensor wave sector would need a field equation of schematic form:

$$\Box h_{ij}^{TT}=S_{ij}^{TT}.$$

In vacuum:

$$\Box h_{ij}^{TT}=0.$$

The script emphasized that this is not supplied by scalar \(A\) or vector \(W_i\).

Therefore the theory needs one of the following:

```text
an independent tensor sector,
or a deeper vacuum mechanism that produces an effective tensor sector,
or else the theory fails to reproduce gravitational radiation.
```

This is now a major open requirement.

---

## Scalar-Vector-Tensor Sector Separation

The linearized sector map is currently:

| Sector | Candidate variable | Source | Status |
|---|---|---|---|
| scalar | \(A/\Phi\) | density / mass | present weakly |
| trace | \(\kappa\) | pressure / trace candidate | reduced candidate |
| vector | \(W_i\) | mass current / angular momentum | needed, not derived |
| tensor | \(h_{ij}^{TT}\) | quadrupole radiation / TT stress | missing |

This is one of the most important outputs of the nonspherical studies.

It prevents the scalar \(A\)-sector from being overextended into roles it cannot fill.

---

## Wave-Sector Success Criteria

A viable wave sector should eventually show:

1. existence of two transverse-traceless propagating polarizations,
2. propagation at the observed wave speed,
3. coupling to changing quadrupole-like sources,
4. compatibility with scalar \(A\) and vector \(W_i\) sectors,
5. no extra unwanted scalar radiation in regimes where constrained,
6. energy flux and radiation-reaction accounting.

These are future tests.

The present script only inventories the required structure.

---

## What This Study Established

This study established:

1. Scalar \(A\) is not a transverse-traceless tensor mode.
2. Vector \(W_i\) is not a transverse-traceless tensor mode.
3. TT waves require a symmetric trace-free transverse spatial tensor.
4. A \(z\)-propagating TT mode has two polarizations:
   $$h_+,$$
   and:
   $$h_\times.$$
5. A wave equation for \(h_{ij}^{TT}\) is currently missing.
6. A full gravity theory needs this sector.

---

## What This Study Did Not Establish

This study did not derive gravitational waves.

It did not derive a tensor wave equation.

It did not identify the source term \(S_{ij}^{TT}\).

It did not show wave propagation speed.

It did not compute radiation power.

It did not connect to binary inspiral observations.

It did not provide a covariant parent for tensor modes.

It only showed that a tensor wave sector is necessary and currently absent.

---

## Current Best Interpretation

The current best interpretation is:

```text
The reduced program has a credible scalar sector and a candidate vector sector.

It does not yet contain radiative tensor gravity.

A full theory must add or derive h_ij^TT.
```

This creates a sharp decision point.

Either:

```text
tensor modes are fundamental additional degrees of freedom,
```

or:

```text
tensor modes emerge from deeper vacuum variables,
```

or:

```text
the theory is not viable as a complete replacement for relativistic gravity.
```

---

## Relationship to Prior Studies

The prior scalar and multipole studies showed:

$$A=1+\frac{2\Phi}{c^2},$$

and:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

They also showed that reciprocal compensation gives the scalar spatial factor:

$$1-\frac{2\Phi}{c^2}.$$

The vector-sector study showed that rotating sources require:

$$g_{ti}\neq0,$$

and therefore a vector sector \(W_i\).

The wave-sector study now shows that even scalar plus vector sectors are insufficient.

Radiative gravity requires:

$$h_{ij}^{TT}.$$

Thus the sector architecture becomes:

```text
A:
  scalar mass/Newtonian potential

kappa:
  trace/interior matter response

W_i:
  vector angular momentum/frame dragging

h_ij^TT:
  tensor waves/radiation
```

---

## Next Development Targets

### 1. Tensor Sector Placeholder

A possible next script:

```text
candidate_tensor_sector_placeholder_action.py
```

Purpose:

```text
Introduce a minimal tensor sector with h_ij^TT and test trace-free,
transverse, and wave-equation properties.
```

### 2. Wave-Speed and Polarization Test

A possible script:

```text
candidate_wave_speed_polarization_test.py
```

Purpose:

```text
Check whether a proposed tensor wave equation has two polarizations and
propagates at the desired speed.
```

### 3. Quadrupole Source Coupling

A possible script:

```text
candidate_quadrupole_radiation_source.py
```

Purpose:

```text
Ask what source term should couple to h_ij^TT and whether it resembles
time-varying quadrupole stress.
```

### 4. Sector Architecture Summary

A possible note:

```text
candidate_linearized_sector_architecture.md
```

Purpose:

```text
Summarize scalar, trace, vector, and tensor sectors after this batch.
```

---

## Summary

The wave-sector linearized-mode study is a necessary negative result.

It shows:

```text
Scalar A is not a gravitational wave mode.
Vector W_i is not a gravitational wave mode.
A full theory needs a transverse-traceless tensor sector h_ij^TT.
```

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

This has two polarizations and is transverse and trace-free.

The current reduced program does not yet derive this sector.

The next theoretical question is whether \(h_{ij}^{TT}\) should be added as a fundamental sector, derived from deeper vacuum variables, or whether its absence is fatal.
