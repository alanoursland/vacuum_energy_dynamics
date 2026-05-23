# Candidate No Extra Polarization Policy

## What This Document Is

This document is a development note for the `07_scalar_constraint_and_radiation_safety/` group.

It is not an observational analysis, not a final polarization theorem, and not a complete radiation theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_no_extra_polarization_policy.py
```

The guiding question was:

```text
What long-range gravitational radiation modes should the theory allow by
default, and what modes must be controlled?
```

The answer is:

```text
Ordinary long-range gravitational radiation should be TT-only for now:
  h_plus
  h_cross

Extra scalar/vector polarizations are not allowed unless separately derived
and suppressed/constrained.
```

This policy protects the scalar \(A\) channel from becoming an unwanted scalar-radiation theory.

---

## Background

The group-07 studies established the scalar safety architecture:

$$
A=A_{\rm constraint}+A_{\rm rad}.
$$

The safe component is:

```text
A_constraint:
  long-ranged,
  Poisson-like,
  scalar/static mass response.
```

The dangerous component is:

```text
A_rad:
  possible scalar breathing radiation,
  dangerous unless absent/suppressed/absorbed/massive/weak.
```

The intended radiation channel remains:

$$
h_{ij}^{TT}.
$$

This study turns that architecture into an explicit polarization policy.

---

## Policy Statement

The ordinary long-range radiation claim is:

```text
allowed:
  h_plus
  h_cross
```

Dangerous extra modes are:

```text
scalar breathing,
scalar longitudinal,
unsuppressed vector modes.
```

The policy is:

```text
Extra modes must be absent, projected out, damped, absorbed,
massive/short-ranged, weakly coupled, or observationally constrained.
```

Equivalently:

```text
Do not claim extra radiation polarizations by accident.
```

---

## Allowed TT Plus/Cross Modes

For propagation along \(z\), the TT tensor mode is:

$$
H_{TT}
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

Its trace is:

$$
\mathrm{Tr}(H_{TT})=0.
$$

For wave vector:

$$
k^i=(0,0,k),
$$

the transversality condition is:

$$
k^iH_{ij}=0.
$$

The script confirmed:

```text
plus/cross modes are trace-free;
plus/cross modes are transverse for z propagation.
```

Thus \(h_+\) and \(h_\times\) are the allowed ordinary long-range radiation modes.

---

## Scalar Breathing Is an Extra Non-TT Mode

A scalar breathing mode can be written:

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

$$
2b.
$$

For propagation along \(z\), this mode can be transverse:

$$
k^iH_{ij}=0.
$$

But it is not traceless.

The script confirmed:

```text
breathing mode may be transverse;
breathing mode is not traceless;
breathing mode must be suppressed unless deliberately allowed.
```

This matters because a transverse mode is not necessarily a TT tensor mode.

The breathing mode is a scalar polarization and would be an extra radiation channel.

---

## Scalar Longitudinal Is an Extra Non-TT Mode

A longitudinal scalar mode can be written:

$$
H_{\rm longitudinal}
=
\begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & \ell
\end{pmatrix}.
$$

Its trace is:

$$
\ell.
$$

For propagation along \(z\):

$$
k^iH_{ij}
=
(0,0,\ell k).
$$

So it is not transverse.

The script confirmed:

```text
longitudinal mode is not transverse;
longitudinal mode is not allowed as ordinary radiation.
```

Thus scalar longitudinal radiation must be projected out or suppressed.

---

## Vector-Like Modes Are a Separate Sector

The vector/current sector candidate is:

$$
W_i=(V_x,V_y,V_z).
$$

This sector may be needed for frame dragging, mass currents, and angular momentum effects.

But it is not the ordinary TT radiation channel.

The script confirmed:

```text
vector modes are outside current allowed radiation set.
```

This does not mean vector physics is impossible or irrelevant.

It means:

```text
long-range vector radiation requires separate derivation and constraints.
```

The default radiation claim remains tensor TT only.

---

## Allowed / Controlled Mode Policy

The script produced the following policy table:

| Mode | Status | Required condition |
|---|---|---|
| \(h_+\) | allowed | TT tensor radiation |
| \(h_\times\) | allowed | TT tensor radiation |
| scalar breathing | controlled | zero / suppressed / absorbed / massive / weak |
| scalar longitudinal | controlled | projected out / suppressed |
| vector radiation | controlled | separate derivation and constraints |

This is the main result.

---

## A_rad Suppression Flags

For the scalar radiative component \(A_{\rm rad}\), the allowed safety flags are:

```text
absent
projected_out
damped_absorbed
relaxes_to_minimum
massive_short_ranged
weakly_coupled
observationally_constrained
```

The unsafe flag is:

```text
unsuppressed_massless_scalar_wave
```

The script confirmed:

```text
A_rad requires explicit safety flag.
```

This is a useful bookkeeping rule for future studies.

Whenever \(A_{\rm rad}\) appears, it must be marked with a safety mechanism.

---

## What This Study Established

This study established:

1. \(h_+\) and \(h_\times\) are allowed ordinary long-range radiation modes.
2. Scalar breathing is non-TT and must be controlled.
3. Scalar longitudinal radiation is non-TT and must be controlled.
4. Vector radiation is outside the current ordinary radiation channel.
5. \(A_{\rm rad}\) must carry a suppression or absence flag.
6. The theory’s ordinary radiation claim should remain TT-only for now.

---

## What This Study Did Not Establish

This study did not prove observational consistency.

It did not derive the polarization content from a covariant parent theory.

It did not rule out all possible extra modes in all regimes.

It did not derive a scalar suppression mechanism.

It did not derive a vector radiation sector.

It only establishes a safe policy for the current theory architecture.

---

## Current Best Interpretation

The current radiation policy is:

```text
Ordinary long-range gravitational radiation = h_plus + h_cross.
```

Extra scalar/vector polarizations are not allowed unless separately derived and suppressed or constrained.

This protects the scalar \(A\) channel from becoming an unwanted scalar-radiation theory.

---

## Relationship to the Group-07 Goal

The goal of group 07 was:

```text
Keep A as the scalar/static mass-response channel while preventing unwanted
scalar radiation.
```

This policy completes that goal at the architecture level.

It does not prove the final mechanism, but it establishes the rule that future mechanisms must satisfy.

---

## Next File

The next file should be the group summary:

```text
scalar_constraint_and_radiation_safety_summary.md
```

That summary should close the group with:

```text
A_constraint is allowed.
A_rad is dangerous unless controlled.
h_ij^TT remains the ordinary radiation channel.
No extra long-range polarizations are allowed by default.
```

---

## Summary

The no-extra-polarization policy establishes the final group-07 safety rule:

```text
Ordinary long-range gravitational radiation is TT-only:
  h_plus
  h_cross
```

Scalar breathing, scalar longitudinal, and unsuppressed vector radiation are controlled modes.

The scalar \(A\) channel survives as static/constraint-like mass response, not as an ordinary long-range scalar radiation field.
