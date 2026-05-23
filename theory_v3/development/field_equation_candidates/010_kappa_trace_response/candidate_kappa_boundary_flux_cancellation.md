# Candidate Kappa Boundary Flux Cancellation

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final \(\kappa\) boundary theory, not a proof of scalar-radiation safety, and not an endorsement of breathing radiation as a desired prediction. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_boundary_flux_cancellation.py
```

The guiding question was:

```text
Does kappa leak through the matter/vacuum boundary?
```

The answer is:

```text
Static exterior safety requires:
  F_kappa(R+) = 0

Massless 1/r tails are rejected.
```

A breathing response is not automatically fatal only if:

```text
it is damped,
absorbed,
massive,
constrained,
or boundary-confined,
```

and does not become ordinary long-range scalar radiation.

The clean target remains:

```text
no ordinary breathing radiation.
```

Damped/absorbed breathing is only a fallback if the math forces a trace response.

---

## Boundary Diagnostic

The boundary diagnostic is:

\[
F_\kappa(R,t)
=
4\pi R^2\partial_r\kappa(R,t).
\]

Exterior safety requires:

\[
F_\kappa(R+,t)=0
\]

for any massless exterior \(\kappa\) channel.

If \(F_\kappa(R+,t)\neq0\), then \(\kappa\) leaks through the boundary into the exterior.

---

## Static Massless Exterior Tail

For a massless exterior tail:

\[
\kappa=\frac{C_1}{r},
\]

the flux is:

\[
F_\kappa
=
4\pi r^2\partial_r\kappa
=
-4\pi C_1.
\]

If:

\[
C_1\neq0,
\]

then exterior flux is nonzero.

Therefore:

\[
\kappa_{\rm ext}=\frac{C_1}{r}
\]

is forbidden unless:

\[
C_1=0.
\]

Status:

```text
RISK — must cancel C1.
```

This is the hard static condition.

---

## Projected Zero-Charge Flux

For the schematic massless Poisson-like equation:

\[
-K_\kappa\Delta\kappa
=
\alpha_\kappa P_0S_{\rm trace},
\]

the exterior flux is proportional to projected charge:

\[
F_\kappa
\sim
-\frac{\alpha_\kappa Q_{\rm proj}}{K_\kappa}.
\]

If:

\[
Q_{\rm proj}
=
\int P_0S_{\rm trace}\,d^3x
=
0,
\]

then:

\[
F_\kappa=0.
\]

Status:

```text
CONSTRAINED_BY_IDENTITY — static/fixed support only.
```

This works for the static monopole.

It does not solve dynamic support, boundary motion, or scalar radiation by itself.

---

## Boundary Matching Condition

Exterior-safe static matching requires:

\[
\kappa(R+)=0,
\]

and:

\[
\partial_r\kappa(R+)=0.
\]

Equivalently:

\[
F_\kappa(R+)=0.
\]

Interior \(\kappa\) may be nonzero only if it is:

```text
confined,
projected,
or matched through a boundary layer with no exterior flux.
```

This permits interior trace response without exterior scalar charge.

Status:

```text
CONSTRAINED_BY_IDENTITY — boundary-layer mechanism missing.
```

---

## Yukawa-Suppressed Exterior Flux

For a Yukawa exterior:

\[
\kappa=\frac{Ce^{-mr}}{r},
\]

the flux is:

\[
F_\kappa
=
-4\pi C(mr+1)e^{-mr}.
\]

This does not make flux identically zero.

It suppresses it with distance.

Status:

```text
PLAUSIBLE — m_k scale missing.
```

This option is acceptable only if:

```text
m_k is derived or constrained,
the mode is not observable long-range,
and the scale is not inserted only to hide scalar radiation.
```

---

## Damped Breathing Boundary Response

A representative damped trace response is:

\[
\kappa_{\rm boundary}(t)
=
A_0e^{-\Gamma t}\cos(\omega_0t).
\]

If \(\Gamma\) is large enough, boundary trace perturbations can be absorbed before becoming long-range scalar radiation.

For a simple oscillator model, critical damping corresponds to:

\[
\Gamma^2=4\omega_0^2.
\]

Status:

```text
PLAUSIBLE — Gamma and energy accounting missing.
```

Important hierarchy:

```text
Preferred:
  no breathing radiation.

Allowed only if forced:
  damped / absorbed / critically damped trace response.

Rejected:
  persistent massless breathing radiation.
```

This is a fallback, not a goal.

---

## Dynamic Boundary Warning

For moving or time-dependent support:

\[
R=R(t),
\]

\[
S_{\rm trace}=S_{\rm trace}(r,t),
\]

\[
\langle S_{\rm trace}\rangle_V=\langle S_{\rm trace}\rangle_V(t).
\]

The projection can create boundary terms:

\[
\frac{d}{dt}
\int_{V(t)}
P_0S\,d^3x.
\]

Even if the instantaneous charge is zero, boundary motion may create effective flux terms unless the constraint propagates consistently.

Status:

```text
RISK — constraint propagation needed.
```

This is not solved.

---

## Classification

The script produced this classification:

| Boundary behavior | Status |
|---|---|
| massless \(1/r\) tail | REJECTED / RISK |
| projected zero-charge static flux | CONSTRAINED_BY_IDENTITY |
| \(\kappa(R+)=0\) and \(\kappa'(R+)=0\) | CONSTRAINED_BY_IDENTITY |
| Yukawa suppressed exterior | PLAUSIBLE if \(m_\kappa\) derived |
| damped / critically damped breathing | PLAUSIBLE if \(\Gamma\) and energy accounting derived |
| moving support projection | RISK / unresolved |

---

## Failure Controls

Boundary flux cancellation fails if:

1. \(F_\kappa(R+)\neq0\) in a massless exterior.
2. \(\kappa\) has a persistent \(1/r\) tail.
3. Damped breathing response carries energy to infinity before absorption.
4. \(\Gamma\) is inserted by hand only to hide scalar radiation.
5. Yukawa scale \(m_\kappa\) is inserted by hand only to hide scalar radiation.
6. Moving support creates uncancelled flux terms.
7. Suppression interferes with static \(A\)-sector gravity.

These controls remain active.

---

## What This Study Established

This study established:

1. Static exterior safety requires:
   \[
   F_\kappa(R+)=0.
   \]

2. A massless \(1/r\) exterior \(\kappa\) tail has nonzero flux.

3. Projected zero charge cancels static monopole flux.

4. Exterior-safe matching requires:
   \[
   \kappa(R+)=0,
   \qquad
   \kappa'(R+)=0.
   \]

5. Yukawa suppression is possible but introduces a scale.

6. Damped breathing response is possible only as a controlled fallback.

7. Dynamic boundary support remains unresolved.

---

## What This Study Did Not Establish

This study did not derive boundary flux cancellation from a parent identity.

It did not derive a boundary-layer model.

It did not derive \(m_\kappa\).

It did not derive \(\Gamma\).

It did not prove energy consistency.

It did not prove that trace/breathing perturbations are always absorbed.

It only identified the boundary-flux conditions.

---

## Current Best Interpretation

The cleanest target remains:

```text
no ordinary breathing radiation.
```

Static exterior safety requires:

\[
F_\kappa(R+)=0.
\]

Massless \(1/r\) tails are rejected.

If the math forces a breathing response, it is not automatically fatal only if it is:

```text
damped,
absorbed,
massive,
constrained,
or boundary-confined,
```

and does not become ordinary long-range scalar radiation.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_relaxation_energy_accounting.py
```

Purpose:

```text
Test whether damping / absorption can conserve or dissipate energy consistently.
```

Reason:

```text
A damped breathing fallback requires energy accounting.
```

Expected result:

```text
Either relaxation is a controlled sink into vacuum minimum,
or it is rejected as an ad hoc scalar-radiation hiding mechanism.
```

---

## Summary

Boundary flux cancellation says:

\[
F_\kappa(R+,t)=0
\]

is the clean exterior condition.

Breathing response remains disfavored.

But if the math forces it, the acceptable version is:

```text
short-lived,
damped,
absorbed,
energy-accounted,
not long-range.
```

The next check is energy accounting.
