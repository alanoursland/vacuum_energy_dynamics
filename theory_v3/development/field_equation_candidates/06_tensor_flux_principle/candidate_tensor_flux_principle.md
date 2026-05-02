# Candidate Tensor Flux Principle

## What This Document Is

This document is a principle-level development note for the tensor-flux program.

It is not a full gravitational theory, not a derivation of general relativity, and not a covariant action. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_tensor_flux_principle.py
```

The guiding question was:

```text
Can the scalar A-flux result and the tensor TT wave result be organized into
one multi-sector vacuum-response principle?
```

The answer is yes, at the structural level.

The principle is:

```text
A-flux is the scalar monopole vacuum-response channel.
h_ij^TT is the tensor quadrupole radiative channel.
```

This does not derive GR. It organizes the theory so that the scalar successes and the tensor-wave requirement belong to different but compatible sectors.

The most important guardrail is:

```text
Do not force waves into A.
Do not treat scalar flux as a complete gravity theory.
Build a multi-sector vacuum-response theory.
```

---

## Background

The scalar branch established:

$$A=1+\frac{2\Phi}{c^2},$$

and:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

In spherical exterior form:

$$F_A=4\pi r^2A'=\frac{8\pi GM}{c^2}.$$

This is the scalar monopole channel.

The scalar no-wave failure control established that scalar \(A\) cannot produce tensor gravitational waves.

The scalar spatial perturbation:

$$h_{ij}^{\rm scalar}=-2\psi\delta_{ij}$$

is pure trace. Its trace-free projection is zero.

The tensor branch then introduced a transverse-traceless tensor:

$$h_{ij}^{TT}.$$

For propagation along \(z\):

$$
h_{ij}^{TT}
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

This supplies the two tensor polarizations needed for gravitational radiation.

---

## Scalar Monopole Channel

The scalar \(A\)-flux channel is:

```text
M -> F_A
```

with:

$$F_A=\frac{8\pi GM}{c^2}.$$

This is the monopole mass channel.

Interpretation:

```text
monopole mass controls scalar A-flux.
```

This channel is responsible for:

```text
Newtonian potential,
static spherical exterior,
weak scalar multipoles,
monopole vacuum response.
```

It is not responsible for tensor waves.

---

## Scalar No-Wave Guardrail

The scalar spatial perturbation is:

$$
h_{ij}^{\rm scalar}
=
\begin{pmatrix}
-2\psi & 0 & 0 \\
0 & -2\psi & 0 \\
0 & 0 & -2\psi
\end{pmatrix}.
$$

The trace is:

$$\mathrm{Tr}(h^{\rm scalar})=-6\psi.$$

The trace-free projection is:

$$0.$$

Thus the scalar mode is pure trace and has no transverse-traceless tensor content.

The script confirmed:

```text
scalar mode is pure trace;
scalar mode has zero trace-free tensor content.
```

This is the key reason scalar \(A\)-flux cannot be a complete gravity theory.

---

## Tensor TT Channel

The tensor TT channel is built from:

$$e_+,$$

and:

$$e_\times.$$

For \(z\)-propagation:

$$
e_+
=
\begin{pmatrix}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 0
\end{pmatrix},
$$

and:

$$
e_\times
=
\begin{pmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

A general TT wave is:

$$H_{TT}=h_+e_+ + h_\times e_\times.$$

In matrix form:

$$
H_{TT}
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

Its trace is zero:

$$\mathrm{Tr}(H_{TT})=0.$$

This channel has two polarizations:

```text
h_plus
h_cross
```

The script confirmed that this is the required TT tensor channel.

---

## Tensor Wave Propagation

The tensor amplitude can support a wave equation.

For a plane wave:

$$h=H\cos(kz-\omega t),$$

the wave operator gives:

$$
\Box h
=
\frac{H}{c^2}
(c^2k^2-\omega^2)
\cos(kz-\omega t).
$$

Dividing by \(h\):

$$\frac{\Box h}{h}=k^2-\frac{\omega^2}{c^2}.$$

The wave condition is:

$$\omega^2=c^2k^2.$$

Thus the TT amplitude supports the standard wave dispersion relation.

This is the propagation side of the tensor channel.

---

## Quadrupole Source Projection

The source-side tensor object is the trace-free quadrupole:

$$Q_{ij}^{TF}=Q_{ij}-\frac13\mathrm{Tr}(Q)\delta_{ij}.$$

For a general symmetric quadrupole:

$$
Q
=
\begin{pmatrix}
Q_{xx} & Q_{xy} & Q_{xz} \\
Q_{xy} & Q_{yy} & Q_{yz} \\
Q_{xz} & Q_{yz} & Q_{zz}
\end{pmatrix},
$$

the trace-free form is:

$$
Q_{ij}^{TF}
=
\begin{pmatrix}
\frac{2Q_{xx}-Q_{yy}-Q_{zz}}{3} & Q_{xy} & Q_{xz} \\
Q_{xy} & \frac{-Q_{xx}+2Q_{yy}-Q_{zz}}{3} & Q_{yz} \\
Q_{xz} & Q_{yz} & \frac{-Q_{xx}-Q_{yy}+2Q_{zz}}{3}
\end{pmatrix}.
$$

For \(z\)-propagation, the plus and cross projections are:

$$Q_+=\frac{Q_{xx}-Q_{yy}}{2},$$

and:

$$Q_\times=Q_{xy}.$$

The script confirmed that the quadrupole projects into both plus and cross channels.

This is the source-side half of the tensor-flux principle.

---

## Time-Derivative Distinction

The script used a rotating quadrupole proxy:

$$Q_+=Q_0\cos(2\Omega t),$$

and:

$$Q_\times=Q_0\sin(2\Omega t).$$

The second-derivative amplitude proxy is:

$$\ddot Q_+^2+\ddot Q_\times^2=16\Omega^4Q_0^2.$$

The third-derivative power proxy is:

$$\dddot Q_+^2+\dddot Q_\times^2=64\Omega^6Q_0^2.$$

This preserves the important distinction:

```text
wave amplitude proxy uses second derivatives;
radiated-power proxy uses third derivatives.
```

This will matter for future coupling-normalization and radiation-flux studies.

---

## Multi-Channel Vacuum-Response Map

The tensor-flux principle sits inside a broader multi-channel architecture:

| Channel | Variable | Source object | Role |
|---|---|---|---|
| scalar monopole | \(A\) | \(M/\rho\) | Newtonian potential, static flux |
| trace interior | \(\kappa\) | pressure / trace candidate | matter response |
| vector current | \(W_i\) | mass current / angular momentum | frame dragging |
| tensor quadrupole | \(h_{ij}^{TT}\) | \(Q_{ij}^{TF}\) derivatives | radiation |

This is the current best sector map.

The tensor-flux principle is not scalar-only.

It is a multi-sector principle.

---

## What This Study Established

This study established:

1. Scalar \(A\)-flux is the monopole channel.
2. Scalar \(A\) has no TT wave content.
3. The TT tensor basis supplies plus/cross polarizations.
4. TT amplitudes support wave propagation.
5. Trace-free quadrupole structure projects onto plus/cross channels.
6. Changing quadrupole structure is the source-side tensor object.
7. Tensor-flux principle should be multi-sector, not scalar-only.

---

## What This Study Did Not Establish

This study did not derive general relativity.

It did not derive a covariant action.

It did not normalize the tensor coupling.

It did not derive the exact far-zone wave amplitude.

It did not derive the gravitational-wave power formula.

It did not prove that tensor flux emerges from vacuum microphysics.

It only established the structural principle:

```text
scalar monopole channel plus tensor quadrupole channel.
```

---

## Current Best Interpretation

The current best interpretation is:

```text
A-flux is the scalar monopole vacuum-response channel.

h_ij^TT is the tensor quadrupole radiative channel.

These are different but compatible sectors of a multi-sector vacuum-response
theory.
```

This is the first coherent answer to the scalar-gravity failure:

```text
Scalar gravity is not enough.
Scalar flux survives as the monopole channel.
Tensor flux begins as the quadrupole radiative channel.
```

---

## Next Development Targets

### 1. Quadrupole Coupling Normalization

A direct next script:

```text
candidate_quadrupole_coupling_normalization.py
```

Purpose:

```text
Ask what coefficient would map quadrupole derivatives to far-zone h_ij^TT
amplitude and how that compares with expected GR-like scaling.
```

### 2. Tensor Radiation Energy Flux

A later script:

```text
candidate_tensor_radiation_energy_flux.py
```

Purpose:

```text
Develop a tensor radiation energy-flux proxy and compare it to the quadratic
plus/cross structure.
```

### 3. No Unwanted Scalar Radiation

A later script:

```text
candidate_no_unwanted_scalar_radiation.py
```

Purpose:

```text
Ensure the scalar A channel does not produce large forbidden scalar radiation
from binaries.
```

---

## Summary

The tensor-flux-principle study organizes the theory into a multi-sector vacuum-response architecture.

Scalar \(A\)-flux carries the monopole channel:

$$M\rightarrow F_A.$$

Tensor \(h_{ij}^{TT}\) carries the quadrupole radiative channel:

$$Q_{ij}^{TF}\rightarrow h_{ij}^{TT}.$$

The scalar no-wave guardrail remains essential:

```text
Do not force waves into A.
```

The tensor-flux principle is:

```text
A-flux is scalar monopole flow.
h_ij^TT is tensor quadrupole radiative flow.
```

This does not yet derive GR, but it gives the next mathematically coherent architecture.
