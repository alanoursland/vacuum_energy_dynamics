# Candidate Quadrupole Tensor Flux

## What This Document Is

This document is a development note for the tensor-flux program.

It is not a full radiation theory, not a postulate, and not a covariant derivation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_quadrupole_tensor_flux.py
```

The guiding question was:

```text
If scalar A-flux is the monopole channel, what is the source-side structure
for the tensor radiative channel?
```

The answer is:

```text
The natural source-side object is the trace-free quadrupole tensor Q_ij^TF.
Its transverse-traceless projection feeds the plus/cross tensor wave channels.
```

The resulting channel map is:

```text
monopole mass M -> scalar A-flux
trace-free quadrupole Q_ij^TF -> tensor h_ij^TT radiation
```

This is the first source-side structure for the tensor-flux program.

---

## Background

The scalar-flux no-wave failure control established that scalar \(A\)-flux cannot be the gravitational-wave sector.

The tensor-flux basis study defined the TT basis:

$$e_+,$$

and:

$$e_\times.$$

The tensor wave equation study showed that:

$$h_{ij}^{TT}=h_+e_+ + h_\times e_\times$$

can satisfy:

$$\Box h_{ij}^{TT}=0$$

in vacuum, with dispersion:

$$\omega^2=c^2k^2.$$

The present study asks what kind of source structure should feed that tensor channel.

---

## Scalar Channel Versus Tensor Channel

The scalar channel is:

```text
monopole mass -> A-flux
```

with:

$$F_A=\frac{8\pi GM}{c^2}.$$

The tensor channel target is:

```text
trace-free quadrupole source -> h_ij^TT radiation
```

This distinction is essential.

The scalar channel is not supposed to radiate tensor waves.

The tensor channel should carry the quadrupole radiative sector.

---

## Trace-Free Quadrupole Tensor

Start with a general symmetric quadrupole tensor:

$$
Q_{ij}
=
\begin{pmatrix}
Q_{xx} & Q_{xy} & Q_{xz} \\
Q_{xy} & Q_{yy} & Q_{yz} \\
Q_{xz} & Q_{yz} & Q_{zz}
\end{pmatrix}.
$$

Its trace is:

$$\mathrm{Tr}(Q)=Q_{xx}+Q_{yy}+Q_{zz}.$$

Define the trace-free quadrupole:

$$Q_{ij}^{TF}=Q_{ij}-\frac13\mathrm{Tr}(Q)\delta_{ij}.$$

Explicitly:

$$
Q_{ij}^{TF}
=
\begin{pmatrix}
\frac{2Q_{xx}-Q_{yy}-Q_{zz}}{3} & Q_{xy} & Q_{xz} \\
Q_{xy} & \frac{-Q_{xx}+2Q_{yy}-Q_{zz}}{3} & Q_{yz} \\
Q_{xz} & Q_{yz} & \frac{-Q_{xx}-Q_{yy}+2Q_{zz}}{3}
\end{pmatrix}.
$$

The script confirmed:

$$\mathrm{Tr}(Q^{TF})=0.$$

Thus \(Q_{ij}^{TF}\) is the correct trace-free tensor source object.

---

## Monopole and Dipole Are Not TT Radiation Channels

The monopole \(M\) is a scalar.

It sources scalar \(A\)-flux:

$$M\rightarrow F_A.$$

It does not source TT tensor radiation directly.

The dipole is a vector:

$$\vec D=(D_x,D_y,D_z).$$

For isolated systems, ordinary mass dipole radiation is removed by center-of-mass and momentum conservation.

Therefore tensor gravitational radiation begins at the trace-free quadrupole order.

This matches the intended sector architecture:

```text
monopole -> scalar channel
dipole/current -> vector channel
quadrupole -> tensor radiative channel
```

---

## Projection Onto Plus/Cross Channels

For propagation along the \(z\)-direction, the plus and cross basis tensors are:

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

Using the inner product:

$$\langle A,B\rangle=\sum_{ij}A_{ij}B_{ij},$$

and noting:

$$\langle e_+,e_+\rangle=2,$$

$$\langle e_\times,e_\times\rangle=2,$$

the plus and cross quadrupole projections are:

$$Q_+=\frac12\langle Q^{TF},e_+\rangle,$$

and:

$$Q_\times=\frac12\langle Q^{TF},e_\times\rangle.$$

The script found:

$$Q_+=\frac{Q_{xx}-Q_{yy}}{2},$$

and:

$$Q_\times=Q_{xy}.$$

Thus the plus channel sees the difference between \(x\) and \(y\) quadrupole moments, while the cross channel sees the \(xy\) quadrupole moment.

This is exactly the expected source-side structure for a wave propagating along \(z\).

---

## Time-Dependent Quadrupole Source Proxy

The script used a simple rotating quadrupole proxy:

$$Q_+(t)=Q_0\cos(2\Omega t),$$

and:

$$Q_\times(t)=Q_0\sin(2\Omega t).$$

Then:

$$\ddot Q_+=-4\Omega^2Q_0\cos(2\Omega t),$$

and:

$$\ddot Q_\times=-4\Omega^2Q_0\sin(2\Omega t).$$

The second-derivative amplitude proxy is:

$$\ddot Q_+^2+\ddot Q_\times^2=16\Omega^4Q_0^2.$$

The third derivatives are:

$$\dddot Q_+=8\Omega^3Q_0\sin(2\Omega t),$$

and:

$$\dddot Q_\times=-8\Omega^3Q_0\cos(2\Omega t).$$

The power proxy is:

$$\dddot Q_+^2+\dddot Q_\times^2=64\Omega^6Q_0^2.$$

The important distinction is:

```text
far-zone wave amplitude source ~ second time derivative of quadrupole
radiated-power proxy ~ third time derivative squared
```

This distinction must be preserved in future tensor-flux studies.

---

## Static Quadrupole Does Not Radiate

The script tested a static quadrupole:

$$Q_{\rm static}=Q_0.$$

Then:

$$\ddot Q_{\rm static}=0,$$

and:

$$\dddot Q_{\rm static}=0.$$

Therefore a static quadrupole has no wave-amplitude source and no radiation-power proxy.

This is important because the tensor channel is radiative only when the quadrupole changes.

A static nonspherical source may produce a static tensor/spatial deformation, but not outgoing radiation.

---

## Tensor-Flux Analogy

The study states the central analogy:

```text
Scalar monopole channel:
  M -> A-flux
  F_A = 8*pi*G*M/c^2

Tensor quadrupole channel:
  Q_ij^TF -> h_ij^TT
  changing quadrupole -> outgoing tensor radiation
```

In the language of the vacuum-response program:

```text
A-flux is monopole scalar vacuum flow.
Tensor flux is quadrupole TT radiative vacuum flow.
```

This is the conceptual bridge to a tensor-flux principle.

---

## What This Study Established

This study established:

1. \(Q_{ij}^{TF}\) is the natural tensor source object.
2. \(Q_{ij}^{TF}\) is trace-free.
3. Monopole mass belongs to the scalar \(A\)-flux channel.
4. Dipole is not the leading isolated tensor radiation channel.
5. \(Q_{ij}^{TF}\) projects onto plus/cross TT polarizations.
6. For \(z\)-propagation:
   $$Q_+=\frac{Q_{xx}-Q_{yy}}{2},$$
   and:
   $$Q_\times=Q_{xy}.$$
7. Wave-amplitude source is associated with second derivatives.
8. Radiated-power proxy is associated with third derivatives squared.
9. Static quadrupoles do not radiate.

---

## What This Study Did Not Establish

This study did not normalize the quadrupole coupling.

It did not derive the far-zone wave amplitude.

It did not derive the gravitational-wave power formula.

It did not derive tensor energy flux.

It did not produce a covariant action.

It did not connect to binary inspiral observations.

It only establishes the source-side structure needed for the tensor-flux program.

---

## Current Best Interpretation

The current best interpretation is:

```text
A-flux is the scalar monopole channel.
h_ij^TT is the tensor quadrupole radiative channel.
The source for h_ij^TT is the time-changing trace-free quadrupole.
```

The next step is to formulate the tensor-flux principle itself.

That principle should say, cautiously:

```text
The vacuum response appears to have multiple flux channels:
  scalar monopole flow carried by A,
  tensor quadrupole radiative flow carried by h_ij^TT.
```

---

## Next Development Targets

### 1. Tensor Flux Principle

A direct next script:

```text
candidate_tensor_flux_principle.py
```

Purpose:

```text
Collect scalar monopole flux, TT tensor basis, tensor wave propagation,
and quadrupole source structure into one principle-level diagnostic.
```

### 2. Quadrupole Coupling Normalization

A later script:

```text
candidate_quadrupole_coupling_normalization.py
```

Purpose:

```text
Match the tensor wave amplitude scaling to the expected far-zone quadrupole
structure.
```

### 3. Tensor Radiation Energy Flux

A later script:

```text
candidate_tensor_radiation_energy_flux.py
```

Purpose:

```text
Develop a tensor radiation energy-flux proxy and compare with plus/cross
quadratic structure.
```

---

## Summary

The quadrupole tensor-flux study provides the first source-side result for the tensor branch.

The scalar channel uses monopole mass:

$$M\rightarrow A\text{-flux}.$$

The tensor channel uses trace-free quadrupole structure:

$$Q_{ij}^{TF}\rightarrow h_{ij}^{TT}.$$

For a wave propagating along \(z\), the source projections are:

$$Q_+=\frac{Q_{xx}-Q_{yy}}{2},$$

and:

$$Q_\times=Q_{xy}.$$

Time-varying quadrupole structure feeds tensor waves.

The source-side distinction is:

```text
second derivatives -> wave amplitude proxy
third derivatives squared -> radiated-power proxy
```

This sets up the tensor-flux principle.
