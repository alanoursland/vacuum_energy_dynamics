# Candidate Scalar Breathing Mode Suppression

## What This Document Is

This document is a development note for the `07_scalar_constraint_and_radiation_safety/` group.

It is not an observational bounds calculation, not a proof that scalar radiation is absent, and not a final scalar-sector field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_scalar_breathing_mode_suppression.py
```

The guiding question was:

```text
If scalar A perturbations can produce non-TT breathing waves, what mechanisms
could make those modes absent, short-ranged, damped, absorbed, relaxed, or
weakly coupled?
```

The answer is a mechanism inventory.

The cleanest target remains:

```text
A_rad = 0
A is constraint-like
h_ij^TT carries ordinary gravitational radiation
```

But a plausible fallback mechanism is:

```text
scalar perturbations may be generated locally, then damp or relax back into
the vacuum minimum before surviving as long-range observable scalar radiation.
```

This preserves the user's vacuum-absorption intuition as a live candidate mechanism, not as an established claim.

---

## Background

The scalar constraint mechanism study distinguished two branches.

The safe branch is:

$$
\nabla^2A=\frac{8\pi G}{c^2}\rho.
$$

This treats \(A\) as a Poisson-like constraint field for scalar/static mass response.

The dangerous branch is:

$$
\Box A=\text{source}.
$$

This would make \(A\) an independent scalar wave field.

If \(A\) propagates freely, it may produce scalar breathing modes. Those modes are not transverse-traceless and would represent an extra radiative channel beyond the intended tensor \(h_{ij}^{TT}\) channel.

This study asks how such breathing modes could be suppressed.

---

## Problem Statement

The theory needs \(A\) for:

```text
scalar mass response,
Newtonian potential,
static exterior field,
weak scalar multipoles.
```

But radiative \(A\) modes could produce:

```text
non-TT scalar breathing waves,
extra gravitational-wave polarization,
extra binary energy loss.
```

The preferred architecture is:

```text
A        -> scalar constraint/static channel
h_ij^TT -> tensor radiation channel
```

So scalar breathing must be:

```text
absent,
short-ranged,
damped,
absorbed,
relaxed,
or weakly coupled.
```

---

## Mechanism 1: Constraint Projection

The split is:

$$
A=A_{\rm constraint}+A_{\rm rad}.
$$

The cleanest mechanism sets:

$$
A_{\rm rad}=0.
$$

Then:

$$
A=A_{\rm constraint}.
$$

The script confirmed:

```text
constraint projection removes scalar radiation by construction.
```

This is the cleanest option because it prevents scalar radiation entirely.

The open problem is deriving the projection from deeper theory rather than imposing it by hand.

---

## Mechanism 2: Massive / Short-Range Scalar Suppression

A massive scalar mode has dispersion:

$$
\frac{\omega^2}{c^2}=k^2+m^2.
$$

Its static Green behavior is Yukawa-like:

$$
a(r)\sim\frac{e^{-mr}}{r}.
$$

If \(m\) is large, scalar breathing modes become short-ranged and are suppressed far away.

The script confirmed:

```text
mass gap creates short-range scalar suppression.
```

This option has a major caution:

```text
the mass gap must suppress radiative scalar breathing without destroying the
long-range static A response needed for ordinary gravity.
```

That may require separating \(A_{\rm constraint}\) from \(A_{\rm rad}\).

---

## Mechanism 3: Damping / Vacuum Absorption

A damped scalar perturbation can have the form:

$$
a(t)=a_0e^{-\gamma t/2}\cos(\omega_0t).
$$

Its envelope is:

$$
a_{\rm env}(t)=a_0e^{-\gamma t/2}.
$$

The script confirmed:

```text
damping gives decaying scalar amplitude.
```

Interpretation:

```text
Scalar perturbations may be generated locally but damp back into the vacuum
minimum instead of surviving as long-range radiation.
```

This captures the vacuum-absorption intuition.

The key requirement is:

```text
damping must remove scalar radiative perturbations without damping away the
static A field that produces Newtonian gravity.
```

---

## Mechanism 4: Relaxation to Vacuum Minimum

A simple scalar vacuum-minimum energy is:

$$
E(a)=\frac12\mu^2a^2.
$$

Then:

$$
\frac{dE}{da}=\mu^2a.
$$

A relaxation law is:

$$
\frac{da}{d\tau}
=
-\Gamma\frac{dE}{da}
=
-\Gamma\mu^2a.
$$

The solution is:

$$
a(\tau)=a_0e^{-\Gamma\mu^2\tau}.
$$

The script confirmed:

```text
relaxation drives scalar perturbation back to minimum.
```

This is another version of vacuum absorption.

It treats scalar perturbations as deviations from a preferred vacuum configuration that relax back toward the minimum.

Again, the open issue is preserving static \(A\)-gravity.

---

## Mechanism 5: Weak Scalar Coupling

Let the scalar source coupling be:

$$
\epsilon_s S.
$$

A schematic amplitude proxy is:

$$
a\sim\frac{\epsilon_sS}{K}.
$$

The power proxy scales as:

$$
P_s\sim\frac{\epsilon_s^2S^2}{K^2}.
$$

The script confirmed:

```text
weak coupling suppresses scalar radiation but needs constraints.
```

This is less clean than constraint projection because scalar radiation still exists.

It would require observational bounds.

---

## Tensor Radiation Remains Active

The suppression mechanisms should target scalar breathing modes, not the tensor \(h_{ij}^{TT}\) channel.

The tensor quadrupole proxy remains:

$$
\dddot Q^2_{\rm proxy}
=
64\Omega^6Q_0^2.
$$

The script confirmed:

```text
tensor quadrupole radiation remains intended active channel.
```

The intended architecture is therefore:

```text
suppress scalar breathing;
preserve tensor plus/cross radiation.
```

---

## Mechanism Classification

The script produced the following classification:

| Mechanism | Scalar radiation status | Risk |
|---|---|---|
| constraint projection | absent | cleanest but must be derived |
| mass gap | short-ranged | must preserve static \(A\) response |
| damping / absorption | decays in time | must not damp static gravity |
| relaxation to minimum | returns to vacuum minimum | needs dynamical law |
| weak coupling | small but nonzero | needs observational bounds |
| unsuppressed scalar wave | present | dangerous |

This table is the main output of the study.

---

## What This Study Established

This study established:

1. Constraint projection removes \(A_{\rm rad}\) directly.
2. A mass gap makes scalar waves short-ranged.
3. Damping or absorption can make scalar perturbations decay.
4. Relaxation can return scalar perturbations to the vacuum minimum.
5. Weak coupling can reduce scalar radiation but requires bounds.
6. Tensor \(h_{ij}^{TT}\) radiation should remain active.
7. The best current target is constraint-like \(A\) plus tensor radiation.

---

## What This Study Did Not Establish

This study did not prove which suppression mechanism nature uses.

It did not derive the constraint projection.

It did not show that scalar perturbations are actually damped.

It did not calculate observational scalar-radiation bounds.

It did not derive a mass gap.

It did not prove that static \(A\)-gravity survives each suppression mechanism.

It only classifies possible safety mechanisms.

---

## Current Best Interpretation

The cleanest option remains:

```text
A_rad = 0
A is constraint-like
```

A plausible fallback is:

```text
vacuum absorption / relaxation
```

where scalar perturbations are generated locally but damp or relax back into the vacuum minimum before becoming long-range observable radiation.

Any such mechanism must preserve static \(A\)-gravity.

That means future models must separate:

```text
static scalar configuration
```

from:

```text
radiative scalar perturbation
```

and suppress only the latter.

---

## Next Development Targets

### 1. Binary Scalar Radiation Guardrail

A direct next script:

```text
candidate_binary_scalar_radiation_guardrail.py
```

Purpose:

```text
Test binary-like source moments and identify which scalar radiation channels
vanish by conservation and which require suppression.
```

### 2. A-Channel Static/Dynamic Split

A later script:

```text
candidate_A_channel_static_dynamic_split.py
```

Purpose:

```text
Formalize A = A_constraint + A_rad and ask which part is allowed to propagate.
```

### 3. Scalar Relaxation / Absorption Model

A later script:

```text
candidate_scalar_relaxation_absorption.py
```

Purpose:

```text
Test damped or relaxational scalar perturbations while preserving static A.
```

---

## Summary

The scalar breathing suppression study keeps the theory from overcommitting.

The cleanest target is still:

$$
A_{\rm rad}=0.
$$

But if scalar perturbations exist, they may still be safe if they are:

```text
short-ranged,
damped,
absorbed,
relaxed,
or weakly coupled.
```

The vacuum-absorption idea is plausible as a candidate mechanism:

```text
scalar perturbations relax back into the vacuum minimum before becoming
long-range scalar breathing radiation.
```

The next stress test is binary scalar radiation.
