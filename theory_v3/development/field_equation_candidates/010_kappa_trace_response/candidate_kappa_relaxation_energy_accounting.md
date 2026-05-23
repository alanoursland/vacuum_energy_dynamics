# Candidate Kappa Relaxation Energy Accounting

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final damping law, not a proof of vacuum absorption, and not a license to add breathing radiation as a desired prediction. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_relaxation_energy_accounting.py
```

The guiding question was:

```text
If a kappa breathing/trace response exists, can it be damped or absorbed
consistently rather than becoming long-range scalar radiation?
```

The answer is:

```text
Breathing radiation remains disfavored.

If math forces a trace/breathing response, acceptable forms are:
  constrained non-wave,
  critically damped,
  overdamped,
  strongly absorbed with short attenuation length.
```

But damping requires:

\[
\frac{dE}{dt}=-\Gamma\dot{\kappa}^2,
\]

a positive vacuum sink/accounting term, and preservation of the static \(A\)-constraint.

---

## Why This Study Matters

The previous boundary-flux study allowed damped breathing only as a fallback.

The preferred target remains:

```text
no ordinary breathing radiation.
```

But if \(\kappa\) math forces a trace/breathing response, the theory needs to know whether that response can be absorbed by the vacuum instead of escaping as long-range scalar gravitational radiation.

This script tests whether damping can be written as real energy loss rather than a cosmetic fix.

---

## Undamped Trace Oscillator

The toy undamped trace oscillator is:

\[
\dot{\kappa}=v,
\]

\[
\dot{v}=-\omega_0^2\kappa.
\]

The oscillator energy is:

\[
E=\frac12v^2+\frac12\omega_0^2\kappa^2.
\]

This energy is conserved in the toy oscillator.

Status:

```text
RISK — not acceptable as ordinary long-range scalar channel.
```

If coupled outward, an undamped trace oscillator can support breathing radiation.

---

## Damped Trace Oscillator

The damped toy oscillator is:

\[
\dot{\kappa}=v,
\]

\[
\dot{v}=-\Gamma v-\omega_0^2\kappa.
\]

Using:

\[
E=\frac12v^2+\frac12\omega_0^2\kappa^2,
\]

the script found:

\[
\frac{dE}{dt}=-\Gamma v^2.
\]

Equivalently:

\[
\frac{dE}{dt}=-\Gamma\dot{\kappa}^2.
\]

For:

\[
\Gamma>0,
\]

the energy decreases:

\[
\frac{dE}{dt}\le0.
\]

Status:

```text
DERIVED_REDUCED — sink term still needs ontology.
```

This is the clean mathematical result.

The lost energy must be accounted for as vacuum absorption or dissipation.

---

## Critical Damping Condition

For the toy equation:

\[
\ddot{\kappa}+\Gamma\dot{\kappa}+\omega_0^2\kappa=0,
\]

the critical damping condition is:

\[
\Gamma^2=4\omega_0^2.
\]

Regimes:

```text
Gamma^2 < 4 omega0^2:
  underdamped oscillatory trace response

Gamma^2 = 4 omega0^2:
  critically damped

Gamma^2 > 4 omega0^2:
  overdamped
```

Cleanest fallback if breathing is forced:

```text
critical / overdamped,
not underdamped propagating.
```

Status:

```text
CONSTRAINED_BY_IDENTITY — Gamma and omega0 not derived.
```

---

## Relaxation Sink Balance

The damping power lost from the \(\kappa\) oscillator is:

\[
P_{\rm loss}=\Gamma\dot{\kappa}^2.
\]

The vacuum balance must include a sink term:

\[
\Gamma_{\rm relax}=P_{\rm loss},
\]

or an equivalent positive-definite absorption term.

Without this, damping is just a hand-wave.

Status:

```text
CONSTRAINED_BY_IDENTITY — vacuum energy sink not derived.
```

This is the main ontology requirement.

---

## Static A-Constraint Guard

Relaxation must not erase static scalar gravity.

Allowed:

```text
damp kappa trace/breathing deviations,
absorb scalar radiative trace perturbations.
```

Not allowed:

```text
damp the static A_constraint mass field,
remove areal flux,
alter A = 1 - 2GM/(c^2 r).
```

Therefore relaxation must act on:

\[
\kappa_{\rm rad}
\]

or trace deviation, not on:

\[
A_{\rm constraint}.
\]

Status:

```text
CONSTRAINED_BY_IDENTITY — sector split must be explicit.
```

This guardrail is essential.

---

## Safe Versus Unsafe Breathing

The script classified breathing/trace behavior as follows:

| Breathing / trace behavior | Status |
|---|---|
| no breathing mode | preferred / cleanest |
| constrained non-propagating trace response | acceptable if parent identity derived |
| critically damped local trace response | plausible fallback if energy-accounted |
| overdamped relaxation | plausible fallback if energy-accounted |
| underdamped but rapidly absorbed | risky, requires attenuation length |
| massless long-range breathing radiation | rejected |
| damping inserted only to hide scalar waves | rejected |

Status:

```text
CONSTRAINED_BY_IDENTITY — breathing is fallback, not goal.
```

This is the correct hierarchy.

---

## Attenuation Length Criterion

For a disturbance moving with characteristic speed \(c\) and damping \(\Gamma\), the attenuation length is:

\[
L_{\rm att}\sim\frac{c}{\Gamma}.
\]

To avoid long-range breathing radiation:

\[
L_{\rm att}
\]

must be short compared with observational propagation scales, or the mode must be non-propagating/constrained.

Status:

```text
PLAUSIBLE — Gamma not derived.
```

This gives a future phenomenological bound if damping is used.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| undamped \(\kappa\) oscillator | RISK |
| damped oscillator energy loss | DERIVED_REDUCED |
| critical damping condition | CONSTRAINED_BY_IDENTITY |
| positive vacuum sink term | CONSTRAINED_BY_IDENTITY / MISSING ontology |
| \(A\)-sector preservation guard | CONSTRAINED_BY_IDENTITY |
| attenuation length criterion | PLAUSIBLE |
| final relaxation law | MISSING |

---

## What This Study Established

This study established:

1. An undamped trace oscillator is dangerous.
2. Damping gives definite energy loss:
   \[
   \frac{dE}{dt}=-\Gamma\dot{\kappa}^2.
   \]
3. Critical damping occurs at:
   \[
   \Gamma^2=4\omega_0^2.
   \]
4. Any damping requires a positive vacuum sink.
5. Relaxation must not affect the static \(A\)-constraint.
6. Breathing is a fallback, not a goal.
7. The next hard target is parent balance.

---

## What This Study Did Not Establish

This study did not derive \(\Gamma\).

It did not derive \(\omega_0\).

It did not derive the vacuum sink term.

It did not derive the attenuation length.

It did not prove that breathing is absent.

It did not prove that breathing, if present, is safely absorbed.

It only established the accounting conditions.

---

## Current Best Interpretation

Breathing radiation remains disfavored.

If math forces a trace/breathing response, acceptable forms are:

```text
constrained non-wave,
critically damped,
overdamped,
strongly absorbed with short attenuation length.
```

But damping requires:

```text
dE/dt = -Gamma kappa_dot^2,
positive vacuum sink/accounting,
preservation of static A_constraint.
```

---

## Next Development Target

The next script should be:

```text
candidate_kappa_projection_parent_balance.py
```

Purpose:

```text
Connect P_0, F_kappa=0, and relaxation sink to vacuum-substance balance.
```

Reason:

```text
relaxation and projection both need the parent balance identity.
```

Expected result:

```text
Either a coherent parent balance template exists, or projection/relaxation remain
formal controls rather than derived ontology.
```

---

## Summary

Damping is not a decorative patch.

If used, it must be an energy-accounted sink:

\[
P_{\rm loss}=\Gamma\dot{\kappa}^2.
\]

The cleanest path is still no breathing mode.

The fallback path is constrained or damped trace response.

The missing goblin jewel is the parent balance identity.
