# Candidate Tensor Flux Basis

## What This Document Is

This document is a development note for the tensor-flux program.

It is not a full gravitational-wave theory, not a postulate, and not a covariant derivation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_tensor_flux_basis.py
```

The guiding question was:

```text
If scalar A-flux cannot be the wave sector, what is the minimal tensor object
needed for gravitational radiation?
```

The answer is:

```text
A transverse-traceless spatial tensor h_ij^TT with two independent
polarizations.
```

For propagation along the \(z\)-axis, the two basis tensors are:

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

A general TT wave in this basis is:

$$
h_{ij}^{TT}
=
h_+e_+
+
h_\times e_\times
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

This is the minimal tensor channel needed after proving that scalar \(A\)-flux cannot produce waves.

---

## Background

The scalar-flux no-wave failure control established:

```text
A-flux is not secretly a gravitational-wave theory.
```

The scalar spatial perturbation:

$$h_{ij}^{\rm scalar}=-2\psi\delta_{ij}$$

is pure trace/conformal.

Its trace-free projection vanishes.

A scalar breathing mode is not transverse-traceless.

No nonzero scalar \(\psi\) can reproduce \(h_+\) or \(h_\times\).

Therefore gravitational radiation requires a separate tensor sector:

$$h_{ij}^{TT}.$$

This study begins that tensor sector by defining the basis.

---

## Plus and Cross Basis Tensors

For a wave propagating along \(z\), the plus basis is:

$$
e_+
=
\begin{pmatrix}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

The cross basis is:

$$
e_\times
=
\begin{pmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

The script confirmed both basis tensors are defined and independent.

These are the two tensor polarizations expected for a linearized transverse-traceless wave.

---

## Trace-Free Checks

The trace of the plus basis is:

$$\mathrm{Tr}(e_+)=1-1+0=0.$$

The trace of the cross basis is:

$$\mathrm{Tr}(e_\times)=0.$$

The script confirmed:

```text
plus basis is trace-free;
cross basis is trace-free.
```

This is necessary because tensor gravitational waves are trace-free.

---

## Transversality Checks

For propagation along the \(z\)-axis, the wave vector is:

$$k^i=(0,0,k).$$

Transversality requires:

$$k^ie_{ij}=0.$$

The script checked:

$$k^ie^+_{ij}=0,$$

and:

$$k^ie^\times_{ij}=0.$$

Thus both basis tensors are transverse for propagation along \(z\).

This establishes the basic TT conditions:

```text
trace-free,
transverse.
```

---

## Basis Inner Products

The script used the Frobenius inner product:

$$
\langle A,B\rangle
=
\sum_{ij}A_{ij}B_{ij}.
$$

It found:

$$\langle e_+,e_+\rangle=2,$$

$$\langle e_\times,e_\times\rangle=2,$$

and:

$$\langle e_+,e_\times\rangle=0.$$

Thus plus and cross are nonzero and orthogonal.

This confirms that the two polarization channels are linearly independent.

---

## General TT Wave

A general TT wave in this basis is:

$$
H_{TT}
=
h_+e_+
+
h_\times e_\times.
$$

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

The trace is:

$$h_+-h_++0=0.$$

The script confirmed that a general plus/cross combination remains trace-free and has two amplitudes.

This is the first constructive tensor object in the tensor-flux program.

---

## Scalar Breathing Mode Is Distinct

The scalar breathing-like mode is:

$$
H_{\rm breathing}
=
\begin{pmatrix}
b & 0 & 0 \\
0 & b & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

Its trace is:

$$2b.$$

Thus it is not traceless unless \(b=0\).

The script also checked that the breathing mode is orthogonal to both TT basis tensors:

$$\langle H_{\rm breathing},e_+\rangle=0,$$

and:

$$\langle H_{\rm breathing},e_\times\rangle=0.$$

This reinforces the scalar failure-control result:

```text
Scalar breathing is not a tensor gravitational wave.
```

It is a distinct possible scalar mode, not the GR TT wave sector.

---

## TT Projection for z Propagation

The script also showed how to extract the \(z\)-propagating TT part from a general symmetric spatial tensor:

$$
H
=
\begin{pmatrix}
h_{xx} & h_{xy} & h_{xz} \\
h_{xy} & h_{yy} & h_{yz} \\
h_{xz} & h_{yz} & h_{zz}
\end{pmatrix}.
$$

For propagation along \(z\), the transverse \(x/y\) block is:

$$
\begin{pmatrix}
h_{xx} & h_{xy} & 0 \\
h_{xy} & h_{yy} & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

Removing the trace in the transverse plane gives:

$$
H_{TT}^{(z)}
=
\begin{pmatrix}
\frac{h_{xx}-h_{yy}}{2} & h_{xy} & 0 \\
h_{xy} & \frac{-h_{xx}+h_{yy}}{2} & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

This tensor has:

$$\mathrm{Tr}(H_{TT}^{(z)})=0,$$

and:

$$k^iH_{ij}^{TT}=0.$$

The script confirmed both conditions.

This gives a concrete projection recipe for the simplest propagation direction.

---

## Tensor Flux Interpretation

The study supports the following architecture:

```text
A-flux is scalar / monopole flow.

h_ij^TT is tensor / quadrupole radiative flow.
```

The scalar \(A\)-flux channel captures mass monopole response.

The TT tensor channel is the proper home for radiative quadrupole response.

This is the conceptual bridge from scalar-flux mechanics to tensor-flux/radiation mechanics.

---

## What This Study Established

This study established:

1. The plus tensor basis:
   $$e_+=\mathrm{diag}(1,-1,0).$$

2. The cross tensor basis:
   $$e_\times{}_{xy}=e_\times{}_{yx}=1.$$

3. Both basis tensors are trace-free.

4. Both are transverse for propagation along \(z\).

5. The plus and cross tensors are orthogonal.

6. A general TT wave has two amplitudes:
   $$h_+,\quad h_\times.$$

7. Scalar breathing is distinct from the TT basis.

8. A \(z\)-propagating TT projection can be extracted from a general spatial tensor.

9. The tensor-flux channel now has a minimal basis.

---

## What This Study Did Not Establish

This study did not derive a tensor wave equation.

It did not derive wave speed.

It did not derive quadrupole source coupling.

It did not derive radiation power.

It did not define a covariant tensor action.

It did not prove that the tensor sector emerges from vacuum microphysics.

It only defines the minimal TT tensor basis needed for a wave sector.

---

## Current Best Interpretation

The current best interpretation is:

```text
Scalar A-flux is the monopole channel.

Tensor h_ij^TT is the candidate quadrupole radiative channel.

The tensor-flux program should now add propagation, source coupling,
and flux/radiation accounting.
```

The next direct script should be:

```text
candidate_tensor_wave_equation.py
```

It should test plane waves:

$$h_+(t,z)=H_+\cos(kz-\omega t),$$

$$h_\times(t,z)=H_\times\cos(kz-\omega t),$$

and require the dispersion relation:

$$\omega^2=c^2k^2.$$

---

## Summary

The tensor-flux basis study establishes the minimal tensor object required for gravitational radiation.

For propagation along \(z\):

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

Both are trace-free and transverse.

Their linear combination gives:

$$h_{ij}^{TT}=h_+e_+ + h_\times e_\times.$$

This begins the tensor-flux program:

```text
scalar A-flux -> monopole channel
tensor TT flux -> quadrupole radiative channel
```
