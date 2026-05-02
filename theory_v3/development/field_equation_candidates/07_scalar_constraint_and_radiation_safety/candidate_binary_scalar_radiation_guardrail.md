# Candidate Binary Scalar Radiation Guardrail

## What This Document Is

This document is a development note for the `07_scalar_constraint_and_radiation_safety/` group.

It is not a binary waveform model, not an observational bounds calculation, and not a final scalar-sector field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_binary_scalar_radiation_guardrail.py
```

The guiding question was:

```text
For a binary-like source, which scalar radiation channels are killed by
conservation, and which remain dangerous?
```

The answer is:

```text
Conservation protects scalar monopole and dipole channels.

A binary naturally has a time-varying quadrupole, which should feed tensor
h_ij^TT radiation.

A scalar quadrupole breathing channel would still be dangerous unless absent,
suppressed, absorbed, short-ranged, or weakly coupled.
```

This is a key group-07 guardrail.

---

## Background

The scalar safety program is trying to preserve the architecture:

```text
A        -> scalar monopole/Newtonian/static response
h_ij^TT -> tensor quadrupole/radiative response
```

The previous suppression study identified possible ways to prevent unwanted scalar breathing radiation:

```text
constraint projection,
mass gap,
damping / vacuum absorption,
relaxation to vacuum minimum,
weak scalar coupling.
```

The binary case is an important stress test because binaries naturally have time-varying quadrupole moments. If the scalar \(A\) channel responds radiatively to quadrupole structure, the theory could produce an extra scalar breathing polarization or extra energy loss.

This script asks what conservation laws protect and what they do not protect.

---

## Binary Setup

The script modeled an equal-mass circular binary with positions:

$$
x_1=
\begin{pmatrix}
a\cos(\Omega t)\\
a\sin(\Omega t)\\
0
\end{pmatrix},
$$

and:

$$
x_2=-x_1.
$$

The total mass is:

$$
M=2m.
$$

The mass dipole is:

$$
D=mx_1+mx_2=0.
$$

The script confirmed:

```text
center of mass dipole vanishes for equal circular binary.
```

This gives a clean test case for monopole, dipole, and quadrupole source channels.

---

## Monopole and Dipole Controls

The total mass is constant:

$$
M=2m.
$$

Therefore:

$$
\dot M=0.
$$

The dipole is zero:

$$
D=0.
$$

Therefore:

$$
\ddot D=0.
$$

The script confirmed:

```text
binary total mass is conserved;
binary center-of-mass dipole has zero second derivative.
```

Thus ordinary scalar monopole and dipole radiation proxies are killed by conservation.

This is good news.

It means the scalar channel is not automatically radiating through the lowest source moments.

---

## Binary Trace-Free Quadrupole

The script computed the trace-free quadrupole tensor:

$$Q_{ij}^{TF}.$$

For the equal-mass circular binary, it found:

$$
Q_{TF}
=
\begin{pmatrix}
\frac{2a^2m(3\cos^2(\Omega t)-1)}{3}
&
a^2m\sin(2\Omega t)
&
0
\\
a^2m\sin(2\Omega t)
&
\frac{2a^2m(3\sin^2(\Omega t)-1)}{3}
&
0
\\
0 & 0 & -\frac{2a^2m}{3}
\end{pmatrix}.
$$

The trace is:

$$
\mathrm{Tr}(Q_{TF})=0.
$$

The script confirmed:

```text
binary quadrupole is trace-free.
```

This is exactly the kind of source object that belongs to the tensor \(h_{ij}^{TT}\) radiation channel.

---

## Plus and Cross Projections

For propagation along the \(z\)-axis, the plus and cross quadrupole projections are:

$$
Q_+=\frac{Q_{xx}-Q_{yy}}{2},
$$

and:

$$
Q_\times=Q_{xy}.
$$

The script found:

$$
Q_+=a^2m\cos(2\Omega t),
$$

and:

$$
Q_\times=a^2m\sin(2\Omega t).
$$

It confirmed:

```text
binary has time-varying plus projection;
binary has time-varying cross projection.
```

Thus a circular binary naturally sources both tensor polarizations.

This is the intended radiation path.

---

## Tensor Quadrupole Radiation Proxy

The third derivatives are:

$$
\dddot Q_+
=
8\Omega^3a^2m\sin(2\Omega t),
$$

and:

$$
\dddot Q_\times
=
-8\Omega^3a^2m\cos(2\Omega t).
$$

The tensor quadrupole radiation proxy is:

$$
\dddot Q_+^2+\dddot Q_\times^2
=
64\Omega^6a^4m^2.
$$

The script confirmed:

```text
binary time-varying quadrupole supports tensor radiation proxy.
```

This is the good channel.

A binary should radiate through \(h_{ij}^{TT}\).

---

## Scalar Breathing Danger From Quadrupole

The script then introduced a generic scalar breathing amplitude:

$$
B(t)=B_0\cos(2\Omega t).
$$

The derivative proxy is:

$$
\dot B^2=
4B_0^2\Omega^2\sin^2(2\Omega t).
$$

The breathing-mode matrix is:

$$
H_{\rm breathing}
=
\begin{pmatrix}
B(t) & 0 & 0\\
0 & B(t) & 0\\
0 & 0 & 0
\end{pmatrix}.
$$

Its trace is:

$$
2B_0\cos(2\Omega t).
$$

Therefore it is non-TT.

The script confirmed:

```text
scalar breathing would be a non-TT extra channel.
```

This is the remaining danger.

Conservation kills scalar monopole and dipole radiation, but it does not automatically kill a scalar quadrupole breathing channel.

---

## Guardrail Classification

The binary source-moment result is:

1. Scalar monopole radiation is killed by mass conservation.
2. Scalar dipole radiation is killed by center-of-mass conservation.
3. Tensor quadrupole radiation is active and intended.
4. Scalar quadrupole breathing radiation is dangerous if unsuppressed.

The required safety condition is:

```text
B_scalar_quadrupole = 0
```

or:

```text
B_scalar_quadrupole is massive / damped / absorbed / weakly coupled.
```

This is the main guardrail.

---

## What This Study Established

This study established:

1. An equal-mass circular binary has conserved total mass.
2. Its center-of-mass dipole vanishes.
3. Scalar monopole radiation is killed by mass conservation.
4. Scalar dipole radiation is killed by center-of-mass conservation.
5. The binary has a time-varying trace-free quadrupole.
6. The quadrupole projects into plus and cross tensor channels.
7. Tensor quadrupole radiation is active and intended.
8. Scalar quadrupole breathing would be an extra non-TT channel if unsuppressed.

---

## What This Study Did Not Establish

This study did not compute a full binary waveform.

It did not calculate observational bounds.

It did not derive scalar suppression.

It did not prove \(B_{\rm scalar}=0\).

It did not decide whether scalar breathing is constrained, massive, damped, absorbed, or weakly coupled.

It only identifies the remaining scalar-radiation danger in binary systems.

---

## Current Best Interpretation

The current best interpretation is:

```text
Conservation laws protect scalar monopole and dipole channels.

They do not automatically protect against scalar quadrupole breathing.

Therefore A must be constraint-like, or scalar breathing must be suppressed.
```

The intended radiative channel remains:

$$
h_{ij}^{TT}.
$$

---

## Next Development Target

The next script should be:

```text
candidate_A_channel_static_dynamic_split.py
```

Purpose:

```text
Formalize A = A_constraint + A_rad and ask which part is allowed to exist
in ordinary exterior/radiation zones.
```

The expected safe architecture is:

```text
A_constraint:
  allowed,
  Poisson-like,
  static/scalar mass response.

A_rad:
  zero, projected out, damped, absorbed, massive, or weakly coupled.

h_ij^TT:
  active tensor radiation channel.
```

---

## Summary

The binary scalar-radiation guardrail shows that binaries are safe at monopole and dipole order:

$$
\dot M=0,
$$

and:

$$
\ddot D=0.
$$

But binaries naturally have a time-varying quadrupole:

$$
Q_+=a^2m\cos(2\Omega t),
$$

$$
Q_\times=a^2m\sin(2\Omega t).
$$

That quadrupole should feed tensor radiation:

$$
h_{ij}^{TT}.
$$

If a scalar breathing quadrupole exists, it is an extra non-TT channel and must be suppressed.

The next step is to formalize the static/dynamic split of \(A\).
