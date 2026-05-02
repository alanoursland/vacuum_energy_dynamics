# Candidate A-Channel Static/Dynamic Split

## What This Document Is

This document is a development note for the `07_scalar_constraint_and_radiation_safety/` group.

It is not a final scalar field equation, not a proof of scalar-radiation absence, and not an observational bounds calculation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_A_channel_static_dynamic_split.py
```

The guiding question was:

```text
Can the scalar A channel be split into a safe static/constraint part and a
dangerous radiative part?
```

The answer is yes as an architecture:

```text
A = A_constraint + A_rad
```

where:

```text
A_constraint:
  allowed,
  long-ranged,
  Poisson-like,
  static scalar mass response.

A_rad:
  dangerous unless controlled,
  possible scalar breathing radiation,
  must be zero, suppressed, absorbed, short-ranged, relaxed, or weakly coupled.
```

The intended radiation channel remains:

```text
h_ij^TT:
  active tensor radiation channel.
```

---

## Background

The scalar safety program has established several guardrails:

1. Poisson-like \(A\) supports static exterior gravity.
2. Hyperbolic \(A\) would admit scalar radiation.
3. Conserved monopole and dipole channels do not create ordinary scalar radiation proxies.
4. Binary quadrupoles naturally feed tensor radiation.
5. A scalar quadrupole breathing mode would be an extra non-TT channel if unsuppressed.
6. Scalar breathing may be suppressed by constraint projection, mass gap, damping, vacuum absorption, relaxation, or weak coupling.

This study formalizes the split needed to preserve static scalar gravity without allowing ordinary scalar radiation.

---

## The Split

The proposed decomposition is:

$$
A=A_{\rm constraint}+A_{\rm rad}.
$$

The roles are:

```text
A_constraint:
  Poisson-like scalar mass response.

A_rad:
  possible scalar radiative perturbation.
```

The safety requirement is:

```text
A_rad = 0
```

or:

```text
A_rad is suppressed / absorbed / short-ranged / relaxed / weakly coupled.
```

The script confirmed:

```text
A split defined.
```

---

## Static Exterior Survives if A_rad = 0

Set:

$$
A_{\rm rad}=0.
$$

Then:

$$
A=A_{\rm constraint}.
$$

For the static exterior mass solution:

$$
A_{\rm constraint}=1-\frac{2GM}{c^2r}.
$$

The radial Laplacian outside the source is:

$$
\nabla^2 A=0.
$$

The script confirmed:

```text
static A gravity survives A_rad=0.
```

This is the most important safety result.

Removing radiative \(A\) does not remove the static scalar field needed for Newtonian / exterior gravity.

---

## Unsuppressed A_rad Is Dangerous

If:

$$
A_{\rm rad}=H\cos(kz-\omega t),
$$

then the scalar wave operator gives:

$$
\Box A_{\rm rad}
=
\frac{H}{c^2}(c^2k^2-\omega^2)\cos(kz-\omega t).
$$

Dividing by \(A_{\rm rad}\):

$$
\frac{\Box A_{\rm rad}}{A_{\rm rad}}
=
k^2-\frac{\omega^2}{c^2}.
$$

If \(A_{\rm rad}\) obeys:

$$
\Box A_{\rm rad}=0,
$$

then it propagates when:

$$
\omega^2=c^2k^2.
$$

The script confirmed:

```text
unsuppressed A_rad would be scalar radiation.
```

This is the danger branch.

---

## Damped / Absorbed A_rad Option

A damped scalar radiative component can have the form:

$$
A_{\rm rad}(t)=H e^{-\gamma t/2}\cos(\omega_0t).
$$

The envelope is:

$$
H e^{-\gamma t/2}.
$$

This represents vacuum absorption or damping of scalar perturbations.

The script confirmed:

```text
damped A_rad decays over time.
```

Interpretation:

```text
Scalar perturbations may be generated locally, but the vacuum absorbs or
damps them before they survive as long-range scalar breathing radiation.
```

This is a candidate mechanism, not an established claim.

---

## Massive / Short-Ranged A_rad Option

A massive static scalar perturbation has Yukawa-like behavior:

$$
A_{\rm rad}\sim\frac{Ce^{-mr}}{r}.
$$

For large \(m\), or large \(r\), this is exponentially suppressed.

The script confirmed:

```text
massive A_rad can be short-ranged while A_constraint remains long-ranged.
```

The caution is critical:

```text
A_constraint must remain long-ranged.
```

A mass gap can only be applied to the dangerous radiative component, not to the static scalar field that produces ordinary gravity.

---

## Relaxational A_rad Option

A relaxational scalar component may obey:

$$
\frac{dA_{\rm rad}}{d\tau}
=
-\Gamma\mu^2A_{\rm rad}.
$$

Then:

$$
A_{\rm rad}(\tau)=A_0e^{-\Gamma\mu^2\tau}.
$$

The script confirmed:

```text
relaxational A_rad returns to scalar vacuum minimum.
```

This formalizes the vacuum-relaxation idea:

```text
scalar perturbations can be pulled back toward the minimum scalar vacuum
configuration.
```

Again, this must not erase the static constraint field.

---

## Tensor Channel Remains Active

The intended radiation channel is still tensorial.

For a quadrupole source:

$$
Q_+=Q_0\cos(2\Omega t),
$$

and:

$$
Q_\times=Q_0\sin(2\Omega t).
$$

The tensor radiation proxy is:

$$
64\Omega^6Q_0^2.
$$

The script confirmed:

```text
h_ij^TT tensor radiation remains active.
```

Thus scalar suppression must target \(A_{\rm rad}\), not tensor radiation.

---

## Safe Architecture Matrix

The script produced this safety matrix:

| Component | Status | Role | Safety requirement |
|---|---|---|---|
| \(A_{\rm constraint}\) | allowed | static scalar gravity | long-ranged Poisson response |
| \(A_{\rm rad}\) | dangerous unless controlled | scalar breathing | zero / suppressed / absorbed / short-ranged / weak |
| \(h_{ij}^{TT}\) | active | tensor radiation | remains unsuppressed |

This is the main output of the study.

---

## What This Study Established

This study established:

1. \(A\) can be split into:
   $$A_{\rm constraint}+A_{\rm rad}.$$

2. \(A_{\rm constraint}\) preserves static scalar gravity.

3. Unsuppressed \(A_{\rm rad}\) is dangerous scalar radiation.

4. \(A_{\rm rad}\) can be removed, damped, massive, relaxed, or weakly coupled.

5. Suppression must not destroy \(A_{\rm constraint}\).

6. \(h_{ij}^{TT}\) remains the intended active radiation channel.

---

## What This Study Did Not Establish

This study did not derive the split from first principles.

It did not prove \(A_{\rm rad}=0\).

It did not prove that damping, absorption, relaxation, mass gap, or weak coupling actually occurs.

It did not calculate observational limits.

It did not derive a covariant scalar constraint.

It only establishes the safe architecture.

---

## Current Best Interpretation

The safest current scalar architecture is:

```text
A = A_constraint
A_rad = 0
```

A fallback architecture allows \(A_{\rm rad}\) but suppresses it:

```text
damped / absorbed / massive / relaxed / weakly coupled
```

In all cases:

```text
A_constraint must preserve static gravity.
h_ij^TT must carry ordinary radiation.
```

---

## Next Development Target

The next script should be:

```text
candidate_no_extra_polarization_policy.py
```

Purpose:

```text
Make the gravitational-radiation polarization commitment explicit:
ordinary long-range radiation should contain plus/cross tensor modes, not an
unsuppressed scalar breathing mode.
```

The expected policy is:

```text
Allowed:
  h_plus,
  h_cross.

Forbidden or suppressed:
  scalar breathing,
  unsuppressed vector radiation,
  unsuppressed longitudinal scalar modes.
```

---

## Summary

The A-channel static/dynamic split study formalizes the scalar safety architecture:

$$
A=A_{\rm constraint}+A_{\rm rad}.
$$

The safe target is:

$$
A_{\rm rad}=0.
$$

The fallback target is:

```text
A_rad exists but is damped, absorbed, massive, relaxed, or weakly coupled.
```

The static scalar field survives:

$$
A_{\rm constraint}=1-\frac{2GM}{c^2r}.
$$

The radiative channel remains:

$$
h_{ij}^{TT}.
$$

This gives the next group-07 guardrail: no extra unsuppressed polarizations.
