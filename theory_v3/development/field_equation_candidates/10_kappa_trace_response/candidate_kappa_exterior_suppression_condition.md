# Candidate Kappa Exterior Suppression Condition

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final \(\kappa\) source law, not a proof of a parent constraint, and not a completed gauge treatment. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_exterior_suppression_condition.py
```

The guiding question was:

```text
What mechanism forces or permits kappa = 0 in exterior vacuum?
```

The answer is:

```text
Exterior kappa suppression is not automatic.

A massless exterior kappa equation permits:
  kappa = C1/r

unless exterior kappa charge/flux vanishes.
```

Current best policy:

```text
kappa is sourced by trace/pressure inside matter,
exterior source vanishes,
exterior kappa charge/flux vanishes,
kappa_ext = 0 by constraint/projection or derived restoring mechanism.
```

---

## Why This Study Matters

The strongest reconstructed sector is the static spherical exterior.

It requires:

\[
AB=1,
\]

and therefore:

\[
B=\frac{1}{A}.
\]

The reduced relation is:

\[
AB=e^{2\kappa}.
\]

Therefore the exterior Schwarzschild reconstruction requires:

\[
\kappa=0.
\]

So \(\kappa\) cannot be allowed to develop an uncontrolled long-range exterior tail.

---

## Exterior Relation to Schwarzschild Reconstruction

The reduced relation is:

\[
AB=e^{2\kappa}.
\]

Set:

\[
\kappa=0.
\]

Then:

\[
AB=1.
\]

Thus:

\[
B=\frac{1}{A}.
\]

The script classified this as:

```text
DERIVED_REDUCED
```

because it is exactly the reciprocal exterior condition used in the successful static spherical reconstruction.

---

## Suppression Mechanism Inventory

The script tested six possible mechanisms:

| Mechanism | Status |
|---|---|
| Boundary-only suppression | PLAUSIBLE |
| Massive/restoring suppression | PLAUSIBLE |
| Constraint projection | CONSTRAINED_BY_IDENTITY |
| Gauge fixing | RISK |
| Relaxation to vacuum minimum | PLAUSIBLE |
| Compact source support only | PLAUSIBLE |

The preferred current combination is:

```text
compact trace source
+ zero exterior kappa charge/flux
+ constraint projection
```

Optional:

```text
massive/restoring suppression if derived.
```

---

## Boundary-Only Suppression

Mechanism:

```text
S_trace = 0 outside and kappa(infinity)=0.
```

Status:

```text
PLAUSIBLE
```

Reason:

```text
For a massless elliptic kappa equation, exterior vacuum plus boundary conditions
may force kappa=0 if no boundary flux is supplied.
```

Risk:

```text
Boundary-only suppression may fail if interior matching induces a 1/r kappa tail.
```

This risk is real.

The massless exterior test shows why.

---

## Massless Exterior Tail Risk

If the exterior equation is:

\[
\Delta_{\rm areal}\kappa=0,
\]

then:

\[
\kappa_{\rm ext}=C_0+\frac{C_1}{r}.
\]

Boundary condition:

\[
\kappa(\infty)=0
\]

sets:

\[
C_0=0.
\]

But:

\[
\frac{C_1}{r}
\]

remains unless:

\[
C_1=0.
\]

Therefore boundary-only suppression requires no exterior \(\kappa\) flux at the source surface.

Equivalently:

\[
F_{\kappa,\rm ext}
=
4\pi r^2\kappa'
=
0.
\]

The script classified this as:

```text
RISK — must set exterior kappa charge/flux to zero.
```

This is the main result of the study.

---

## Massive / Restoring Suppression

Mechanism:

\[
-K_\kappa\Delta\kappa+m_\kappa^2\kappa=\alpha_\kappa S_{\rm trace}.
\]

In exterior vacuum:

\[
S_{\rm trace}=0.
\]

Then the exterior equation can produce a Yukawa-type decaying solution:

\[
\kappa_{\rm ext}
=
\frac{C e^{-m_\kappa r}}{r}.
\]

Status:

```text
PLAUSIBLE
```

Risk:

```text
m_kappa is a new scale and must be derived or constrained.
```

This mechanism suppresses long-range \(\kappa\), but it may introduce an extra scalar scale or mode.

It cannot be inserted only to hide scalar radiation.

---

## Constraint Projection

Mechanism:

```text
kappa is not an independent exterior degree of freedom.
```

Status:

```text
CONSTRAINED_BY_IDENTITY
```

Reason:

```text
This best protects the static exterior: kappa is allowed as an interior trace
response but projected out in source-free exterior.
```

Symbolically:

```text
S_trace = 0,
Q_kappa = integral S_trace d^3x = 0 for exterior monopole charge,
kappa_ext = 0.
```

Risk:

```text
Requires a parent constraint identity; otherwise it is imposed by hand.
```

This is currently the cleanest exterior-safe policy, but it is not derived.

---

## Gauge Fixing

Mechanism:

```text
exterior areal/static gauge sets kappa = 0.
```

Status:

```text
RISK
```

Reason:

```text
Some kappa behavior may be coordinate-volume artifact in areal/static reductions.
```

Risk:

```text
If kappa is only gauge, interior physical interpretation is weakened.
If it is physical, gauge fixing cannot be the whole mechanism.
```

This cannot be the only answer unless \(\kappa\) is demoted to a gauge-aware diagnostic.

---

## Relaxation to Vacuum Minimum

Mechanism:

\[
\dot{\kappa}=-\Gamma_\kappa\kappa.
\]

or a damped relaxation law.

Status:

```text
PLAUSIBLE
```

Reason:

```text
Vacuum relaxation can drive trace deviations back to kappa=0 after matter/source
support disappears.
```

Risk:

```text
Relaxation law must not introduce propagating scalar radiation or erase static
A_constraint.
```

This is plausible for removing trace deviations, but it does not by itself define the interior source.

---

## Compact Source Support Only

Mechanism:

```text
S_trace has compact support inside matter.
```

Status:

```text
PLAUSIBLE
```

Reason:

```text
Pressure/stress trace vanishes outside matter, so kappa source naturally turns
off in exterior.
```

Risk:

```text
Source compactness alone does not prevent homogeneous exterior tails.
```

This is why exterior charge/flux must also vanish.

---

## Best Current Suppression Policy

The script’s best current policy is:

1. \(\kappa\) source is not raw \(\rho\).
2. Source family is pressure/spatial trace/trace exchange.
3. Exterior source support vanishes in vacuum.
4. Exterior homogeneous \(\kappa\) charge must vanish.
5. Suppression may be by constraint projection, restoring term, or both.
6. Gauge contribution must be separated from physical trace response.

Most conservative exterior condition:

\[
\kappa_{\rm ext}=0,
\]

and:

\[
F_{\kappa,\rm ext}=4\pi r^2\kappa'=0.
\]

This prevents a long-range scalar trace field.

---

## Failure Controls

Exterior suppression fails if:

1. \(\kappa\) has a \(1/r\) exterior tail.
2. \(\kappa\) is sourced by raw density and duplicates \(A\).
3. Restoring mass \(m_\kappa\) is inserted only to hide scalar radiation.
4. Gauge fixing is mistaken for physical suppression.
5. Interior \(\kappa\) matching creates nonzero exterior \(\kappa\) flux.
6. Parent identity does not explain why exterior \(\kappa\) charge vanishes.

These failure controls are now central to group 10.

---

## What This Study Established

This study established:

1. Exterior \(\kappa=0\) is required for the strongest reconstructed exterior sector.
2. A massless exterior \(\kappa\) equation allows a \(1/r\) tail.
3. Boundary condition at infinity alone is not enough.
4. Exterior \(\kappa\)-charge/flux must vanish.
5. Massive/restoring suppression is plausible but introduces a new scale.
6. Constraint projection is the cleanest exterior-safe policy, but requires a parent identity.
7. Gauge fixing alone is risky.
8. Compact source support alone is insufficient.

---

## What This Study Did Not Establish

This study did not derive the parent constraint projection.

It did not derive \(m_\kappa\).

It did not derive a relaxation law.

It did not decide whether \(\kappa\) is physical, gauge, or mixed.

It did not build the interior pressure/trace source model.

It only established the exterior suppression requirements.

---

## Current Best Interpretation

Exterior \(\kappa\) suppression is not automatic.

A massless exterior \(\kappa\) equation permits:

\[
\kappa=\frac{C_1}{r}.
\]

Therefore the best current policy is:

```text
trace/pressure source inside matter,
vanishing exterior source,
vanishing exterior kappa charge/flux,
kappa_ext = 0 by constraint/projection or derived restoring mechanism.
```

---

## Next Development Target

The next script should be:

```text
candidate_kappa_pressure_trace_model.py
```

Purpose:

```text
Build a simple interior pressure/spatial-trace source model.
```

Reason:

```text
After exterior suppression, the next issue is the interior source.
```

Expected result:

```text
A toy model for S_trace based on pressure or spatial stress trace,
with explicit classification of whether it creates exterior kappa charge/flux.
```

---

## Summary

The exterior suppression study gives a hard requirement:

\[
F_{\kappa,\rm ext}=4\pi r^2\kappa'=0.
\]

Without that, a massless exterior \(\kappa\) channel can leak a long-range scalar trace field:

\[
\kappa\sim\frac{1}{r}.
\]

Thus the next interior model must be designed so it does not create forbidden exterior \(\kappa\)-flux.
