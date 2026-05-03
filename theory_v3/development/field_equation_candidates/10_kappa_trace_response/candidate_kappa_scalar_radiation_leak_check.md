# Candidate Kappa Scalar Radiation Leak Check

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final dynamical law for \(\kappa\), not a proof of scalar-radiation safety, and not a complete relaxation/energy-accounting model. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_scalar_radiation_leak_check.py
```

The guiding question was:

```text
Does kappa create a scalar radiation channel even if its static exterior
monopole charge is projected away?
```

The answer is:

```text
Projection removes static monopole leakage, but not automatically scalar
radiation.
```

Safe \(\kappa\) policies are:

```text
elliptic / constrained,
relaxational / non-wave,
massive / restoring only if derived and controlled.
```

Rejected:

```text
ordinary massless hyperbolic kappa.
```

Important nuance:

```text
A breathing/trace response is not automatically fatal if it is short-lived,
strongly damped, critically damped, massive, confined, or absorbed back into
the vacuum before becoming long-range radiation.
```

But ordinary long-range scalar radiation remains disallowed unless separately derived and observationally controlled.

---

## Why This Study Matters

The projection identity:

\[
P_0S=S-\langle S\rangle
\]

removes static monopole \(\kappa\)-charge:

\[
\int P_0S\,d^3x=0.
\]

That prevents the exterior massless monopole tail:

\[
\kappa_{\rm ext}\sim\frac{1}{r}.
\]

But that is a static result.

A time-dependent trace sector could still radiate if \(\kappa\) obeys a wave equation.

So scalar-radiation safety requires a dynamical check.

---

## Dynamics Options

The script tested four \(\kappa\) dynamics options:

| Dynamics option | Status |
|---|---|
| Elliptic constrained \(\kappa\) | CONSTRAINED_BY_IDENTITY |
| Hyperbolic massless \(\kappa\) | REJECTED |
| Massive/restoring \(\kappa\) | PLAUSIBLE |
| Relaxational \(\kappa\) | PLAUSIBLE |

Current best dynamical policy:

```text
kappa should be elliptic/constrained or relaxational, not massless hyperbolic.
```

Open:

```text
parent constraint propagation,
relaxation energy accounting,
massive scalar scale if used.
```

---

## D1: Elliptic Constrained Kappa

Equation type:

\[
\mathcal{L}_\kappa\kappa=\alpha_\kappa P_0S_{\rm trace}
\]

with no independent time evolution.

There is no term of the form:

\[
\Box\kappa.
\]

Radiation behavior:

```text
No independent propagating scalar wave by construction.
```

Status:

```text
CONSTRAINED_BY_IDENTITY
```

Risk:

```text
Requires parent constraint identity and consistent time-dependent support/projection.
```

This remains the safest \(\kappa\) interpretation.

---

## D2: Hyperbolic Massless Kappa

Equation type:

\[
\Box\kappa=\alpha_\kappa P_0S_{\rm trace}.
\]

In vacuum:

\[
\Box\kappa=0.
\]

Plane-wave modes obey:

\[
\omega^2=c^2k^2.
\]

Even if the monopole source is projected out, time-dependent trace structure can excite propagating scalar modes.

Status:

```text
REJECTED
```

Reason:

```text
would create ordinary long-range breathing/trace gravitational radiation.
```

This is not acceptable as a final unsuppressed channel.

---

## D3: Massive / Restoring Kappa

Equation type:

\[
(\Box-m_\kappa^2)\kappa=\alpha_\kappa P_0S_{\rm trace},
\]

or in static/restoring form:

\[
(-\Delta+m_\kappa^2)\kappa=\text{source}.
\]

Schematic dispersion:

\[
\omega^2=c^2k^2+m_\kappa^2.
\]

Radiation behavior:

```text
Suppresses long-range low-frequency propagation if m_kappa is large enough
or if kappa is not freely radiative in the relevant regime.
```

Status:

```text
PLAUSIBLE
```

Risk:

```text
Introduces m_kappa and possible massive scalar mode.
```

This option could support a short-range breathing response, but only if the scale is derived or constrained.

---

## D4: Relaxational Kappa

Equation type:

\[
\dot{\kappa}=-\Gamma_\kappa\kappa+\text{source/projection}.
\]

For the homogeneous relaxation law:

\[
\dot{\kappa}=-\Gamma\kappa,
\]

the solution is:

\[
\kappa(t)=\kappa_0e^{-\Gamma t}.
\]

Radiation behavior:

```text
Non-wave relaxation can absorb trace perturbations back to vacuum minimum.
```

Status:

```text
PLAUSIBLE
```

Risk:

```text
Needs energy accounting and must not erase static A_constraint.
```

This option matches the intuition that scalar/breathing disturbances may be absorbed by the vacuum.

---

## Breathing Response Is Not Automatically Fatal

The project’s previous rule was:

```text
ordinary long-range radiation is TT-only unless extra modes are separately
derived and controlled.
```

That still holds.

But a transient breathing response could be allowed if it satisfies all of:

```text
not freely massless,
not long-range,
not independently conserved as escaping radiation,
not excited by ordinary distant binaries at observable strength,
absorbed/damped/projected before becoming an external wave channel,
does not alter the static A constraint.
```

Possible safe breathing regimes:

| Breathing behavior | Status |
|---|---|
| massless long-range scalar wave | REJECTED |
| massive short-range trace response | PLAUSIBLE if scale derived |
| overdamped relaxation | PLAUSIBLE if energy accounted |
| critically damped vacuum absorption | PLAUSIBLE if damping law derived |
| constrained non-radiative response | CURRENT BEST |

This gives a failure-softening path:

```text
If the math forces a breathing trace response, it may be acceptable if the
vacuum rapidly absorbs it.
```

But it cannot remain an ordinary massless propagating scalar gravity wave.

---

## Time-Dependent Projection Warning

Projection:

\[
P_0S=S-\langle S\rangle_{\rm support}
\]

is clean in the static fixed-support case.

For time-dependent sources:

```text
support V(t),
average <S(t)>,
moving boundary terms,
time-dependent projection operator.
```

These can introduce extra terms.

Therefore scalar-radiation safety requires more than static zero charge.

Need one or more of:

```text
time-dependent constraint propagation,
boundary flux cancellation,
relaxation law with energy accounting,
critical damping / absorption law.
```

Status:

```text
RISK — dynamic support/projection not solved.
```

---

## Failure Controls

\(\kappa\) scalar-radiation safety fails if:

1. \(\Box\kappa\) appears as an ordinary massless wave equation.
2. Time-dependent projected sources radiate trace waves.
3. Relaxation violates energy/source accounting.
4. Massive \(\kappa\) introduces an observable fifth/scalar mode unintentionally.
5. Projection is static only and does not propagate consistently.
6. \(\kappa\) suppression erases the static \(A\) constraint.
7. Breathing response is long-range and weakly damped.

---

## What This Study Established

This study established:

1. Static projection is not enough to prove scalar-radiation safety.
2. Ordinary massless hyperbolic \(\kappa\) is rejected.
3. Elliptic/constrained \(\kappa\) is structurally safe.
4. Massive/restoring \(\kappa\) is plausible but introduces a scale.
5. Relaxational \(\kappa\) is plausible but requires energy accounting.
6. A short-lived or critically damped breathing response is not automatically fatal.
7. The next issue is boundary/dynamic flux cancellation.

---

## What This Study Did Not Establish

This study did not derive the parent constraint identity.

It did not derive \(\Gamma_\kappa\).

It did not derive \(m_\kappa\).

It did not derive relaxation energy accounting.

It did not solve time-dependent support projection.

It did not prove absence of scalar radiation.

It only classified safe and unsafe \(\kappa\) dynamics.

---

## Current Best Interpretation

Projection removes static monopole leakage, but not automatically scalar radiation.

Safe \(\kappa\) policies:

```text
elliptic/constrained,
relaxational/non-wave,
massive/restoring only if derived and controlled.
```

Rejected:

```text
ordinary massless hyperbolic kappa.
```

Allowed as a possible future escape hatch:

```text
short-lived, strongly damped, or critically damped breathing response absorbed
by the vacuum.
```

---

## Next Development Target

The next script should be:

```text
candidate_kappa_boundary_flux_cancellation.py
```

Purpose:

```text
Test exterior flux cancellation at the static or moving matter boundary.
```

Reason:

```text
Static projection removes monopole charge; next check is boundary flux.
```

Given the breathing-response possibility, the next script should also track:

```text
damped boundary leakage,
critical damping,
whether any trace pulse can escape to infinity.
```

---

## Summary

The \(\kappa\) scalar-radiation leak check does not forbid all breathing behavior.

It forbids ordinary long-range massless breathing radiation.

A short-lived, damped, or vacuum-absorbed trace response remains possible.

The next goblin door is boundary flux:

\[
F_\kappa(R,t)
=
4\pi R^2\partial_r\kappa(R,t).
\]

If that flux vanishes or is absorbed, \(\kappa\) may remain an interior/constrained trace response rather than a radiative scalar gravity channel.
