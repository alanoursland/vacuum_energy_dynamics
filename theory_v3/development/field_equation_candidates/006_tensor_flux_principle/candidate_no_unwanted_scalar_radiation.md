# Candidate No Unwanted Scalar Radiation

## What This Document Is

This document is a guardrail note for the tensor-flux program.

It is not an observational bounds calculation, not a full radiation theory, and not a derivation of scalar-sector dynamics. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_no_unwanted_scalar_radiation.py
```

The guiding question was:

```text
If the theory contains a scalar A channel, how do we prevent it from becoming
an unwanted scalar-radiation theory?
```

The answer is architectural:

```text
A should remain the scalar monopole/Newtonian/static response channel.

h_ij^TT should carry the ordinary quadrupole radiative channel.

Scalar radiation must be absent, constrained, or suppressed.
```

This is a critical guardrail because the tensor-flux program only works if tensor radiation is not polluted by a large extra scalar breathing mode.

---

## Background

The current tensor-flux architecture separates:

```text
A        -> scalar monopole/Newtonian channel
h_ij^TT -> tensor quadrupole/radiative channel
```

The scalar branch already succeeded as:

```text
Newtonian potential,
static spherical mass response,
weak scalar multipoles,
monopole A-flux.
```

But it failed as a complete gravity theory because scalar \(A\) cannot produce TT gravitational waves.

The danger is different now:

```text
If A is allowed to radiate strongly, binaries may emit extra scalar radiation.
```

That would create extra breathing polarization or extra energy loss outside the intended tensor quadrupole channel.

The guardrail target is:

```text
ordinary radiation lives in h_ij^TT.
A remains static, constrained, nonradiative, or strongly suppressed in radiation zones.
```

---

## Monopole Scalar Radiation Control

The scalar monopole source is total mass:

$$M(t).$$

For an isolated source with conserved total mass:

$$M(t)=M_0.$$

Then:

$$\dot M=0,$$

and:

$$\ddot M=0.$$

The script confirmed:

```text
conserved total mass gives no scalar monopole radiation.
```

This matches the usual expectation that isolated systems do not radiate monopole gravitational waves.

In this program, the monopole belongs to the scalar \(A\)-flux channel, but conserved monopole mass is static.

---

## Dipole Scalar Radiation Control

The mass dipole is:

$$D(t).$$

For center-of-mass motion with constant velocity:

$$D(t)=D_0+Vt.$$

Then:

$$\ddot D=0.$$

The script confirmed:

```text
constant-velocity center-of-mass dipole gives no dipole radiation proxy.
```

This prevents ordinary center-of-mass translation from becoming scalar dipole radiation.

Thus the scalar monopole and scalar dipole channels are naturally quiet under conservation assumptions.

---

## Scalar Breathing Quadrupole Is Not TT

A scalar breathing mode can be represented as:

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

Therefore it is a scalar trace mode, not a transverse-traceless tensor mode.

The script confirmed:

```text
breathing mode is scalar trace mode, not TT.
```

This is important because a scalar breathing mode would be an extra polarization, distinct from the intended plus/cross tensor polarizations.

---

## Scalar Breathing Energy Danger

The script compared a scalar breathing derivative proxy:

$$
\frac12B^2\omega^2
$$

to the tensor plus/cross derivative proxy:

$$
\frac12\omega^2(H_+^2+H_\times^2).
$$

If \(B\) is not suppressed, scalar breathing radiation would add an extra radiative channel.

That means the theory must choose one of the following:

```text
A is not radiative;
A radiation is absent by constraint;
A breathing modes are massive/short-ranged;
A radiation couples only to channels that vanish for isolated binaries;
A radiation exists but is tightly observationally constrained.
```

The clean target for the current program is:

```text
A handles static/scalar mass response.
h_ij^TT handles radiation.
```

---

## Architectural Suppression Options

The script listed several possible ways to avoid unwanted scalar radiation:

1. \(A\) is constrained or instantaneous in the radiation zone, not a propagating wave.
2. \(A\) has no independent radiative degree of freedom.
3. Scalar radiation couples only to nonconserved monopole/dipole channels, which vanish for isolated binaries.
4. Scalar breathing mode is massive or short-ranged and suppressed.
5. Scalar radiation exists but is observationally constrained.

The cleanest target is currently:

```text
A is the static/scalar mass-response channel.
h_ij^TT is the radiative quadrupole channel.
```

This is not yet derived. It is the architecture the theory should try to realize.

---

## Tensor Quadrupole Remains Intended Radiation Channel

The tensor quadrupole proxy is:

$$Q_+=Q_0\cos(2\Omega t),$$

and:

$$Q_\times=Q_0\sin(2\Omega t).$$

The third-derivative squared proxy is:

$$
\dddot Q_+^2+\dddot Q_\times^2
=
64\Omega^6Q_0^2.
$$

The script confirmed:

```text
time-varying quadrupole supports tensor radiation proxy.
```

This keeps ordinary radiation assigned to the tensor \(h_{ij}^{TT}\) sector.

---

## What This Study Established

This study established:

1. Conserved total mass gives no scalar monopole radiation.
2. Constant-velocity center-of-mass dipole gives no scalar dipole radiation.
3. Scalar breathing radiation is not TT radiation.
4. If scalar breathing radiation exists unsuppressed, it is an extra channel.
5. A viable architecture should keep ordinary radiation in \(h_{ij}^{TT}\).
6. \(A\) should remain scalar/static/constraint-like unless scalar radiation is deliberately added and tightly constrained.

---

## What This Study Did Not Establish

This study did not derive the scalar-sector constraint.

It did not prove that \(A\) is nonradiative.

It did not compute observational bounds on scalar breathing modes.

It did not derive a scalar mass term.

It did not decide whether scalar radiation is impossible or merely suppressed.

It only establishes the guardrail requirement:

```text
avoid large unwanted scalar radiation.
```

---

## Current Best Interpretation

The current best interpretation is:

```text
A is the scalar monopole/Newtonian/static response channel.

h_ij^TT is the tensor quadrupole/radiative response channel.

Scalar radiation must be absent, constrained, or suppressed.
```

This protects the tensor-flux program from accidentally becoming a scalar-radiation theory.

---

## Next Development Targets

### 1. Tensor Action / Stiffness

A direct next script:

```text
candidate_tensor_action_stiffness.py
```

Purpose:

```text
Ask whether a tensor action can generate the wave equation and identify the
stiffness normalization required for the tensor channel.
```

### 2. Scalar Constraint Mechanism

A later script:

```text
candidate_scalar_constraint_mechanism.py
```

Purpose:

```text
Explore whether A is elliptic/constraint-like rather than radiative in the
ordinary radiation zone.
```

### 3. Scalar Breathing Suppression

A later script:

```text
candidate_scalar_breathing_suppression.py
```

Purpose:

```text
Model massive, short-range, or weakly coupled scalar breathing modes.
```

---

## Summary

The no-unwanted-scalar-radiation study establishes a key guardrail.

The scalar \(A\) channel can safely carry static monopole/Newtonian response if:

```text
monopole radiation vanishes by mass conservation,
dipole radiation vanishes by center-of-mass conservation,
scalar breathing radiation is absent or suppressed.
```

The intended radiative channel remains:

$$h_{ij}^{TT}.$$

The next step is to explore a tensor action/stiffness model for that channel.
