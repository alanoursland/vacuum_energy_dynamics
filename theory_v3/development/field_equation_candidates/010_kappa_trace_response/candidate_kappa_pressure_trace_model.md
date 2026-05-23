# Candidate Kappa Pressure Trace Model

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final \(\kappa\) source law, not a GR interior solution, and not a completed pressure/stress coupling. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_pressure_trace_model.py
```

The guiding question was:

```text
If kappa is sourced by pressure or spatial stress trace, does an interior matter
body generate forbidden exterior kappa charge?
```

The answer is:

```text
A raw pressure/spatial-trace source is plausible for the interior, but dangerous
for the exterior.

For positive pressure:
  Q_kappa = integral 3p d^3x != 0

A massless kappa equation would then produce:
  kappa_ext ~ 1/r

Therefore raw pressure trace cannot be the final unscreened kappa source.
```

Needed:

```text
compensated / zero-charge trace constraint,
massive / restoring suppression,
or parent projection that removes exterior kappa charge.
```

---

## Why This Study Matters

The previous exterior-suppression study found that exterior \(\kappa=0\) is required for the reconstructed static exterior.

A massless exterior equation permits:

\[
\kappa_{\rm ext}=\frac{C_1}{r}.
\]

Therefore any interior \(\kappa\) source must not generate a forbidden exterior monopole charge.

This study tests whether the obvious pressure/stress trace source does that.

It does.

That is the key finding.

---

## Toy Source Model

The toy pressure profile is:

\[
p(r)=p_0\left(1-\frac{r^2}{R^2}\right).
\]

This is regular at the origin and vanishes at the surface:

\[
p(R)=0.
\]

The spatial trace source is:

\[
S_{\rm trace}=3p.
\]

Therefore:

\[
S_{\rm trace}
=
3p_0\left(1-\frac{r^2}{R^2}\right).
\]

Status:

```text
PLAUSIBLE — not derived from hydrostatic equilibrium.
```

This is only a toy model.

---

## Integrated Trace Charge

The integrated \(\kappa\)-trace charge is:

\[
Q_\kappa
=
4\pi
\int_0^R
r^2S_{\rm trace}\,dr.
\]

For the toy source:

\[
Q_\kappa
=
\frac{8\pi R^3p_0}{5}.
\]

For:

\[
p_0>0,
\]

this is nonzero.

Status:

```text
RISK — massless kappa would leak outside.
```

This is the main result of the run.

---

## Massless Exterior Flux Consequence

For a schematic massless equation:

\[
-K_\kappa\Delta\kappa
=
\alpha_\kappa S_{\rm trace},
\]

the exterior flux is proportional to the integrated trace charge:

\[
F_\kappa
\sim
-\frac{\alpha_\kappa Q_\kappa}{K_\kappa}.
\]

The exterior tail is:

\[
\kappa_{\rm ext}
\sim
\frac{\alpha_\kappa Q_\kappa}{4\pi K_\kappa r}.
\]

Thus positive pressure trace generically creates exterior leakage.

Status:

```text
RISK — requires projection, screening, or zero-charge construction.
```

---

## Zero-Charge Requirement

To preserve exterior:

\[
\kappa_{\rm ext}=0
\]

with massless \(\kappa\), the integrated trace charge must vanish:

\[
Q_\kappa
=
\int S_{\rm trace}\,d^3x
=
0.
\]

But for ordinary positive pressure:

\[
\int 3p\,d^3x>0.
\]

Therefore a raw pressure-trace Poisson law is not exterior-safe.

Needed:

```text
constraint projection that removes monopole kappa charge,
or restoring/massive suppression,
or source defined as compensated trace exchange with zero net charge.
```

---

## Compensated Trace Source Option

The script tested a compensated source:

\[
S_{\rm comp}
=
S_{\rm trace}
-
\langle S_{\rm trace}\rangle.
\]

For the toy pressure profile:

\[
\langle S_{\rm trace}\rangle
=
\frac{6p_0}{5}.
\]

So:

\[
S_{\rm comp}
=
\frac{9p_0}{5}
-
\frac{3p_0r^2}{R^2}.
\]

The integrated compensated charge is:

\[
Q_{\rm comp}=0.
\]

Status:

```text
CONSTRAINED_BY_IDENTITY — needs parent identity.
```

This removes monopole \(\kappa\)-charge by construction.

But it must be derived from a parent constraint, not inserted arbitrarily.

---

## Massive / Restoring Trace Response Option

If \(\kappa\) has a restoring or mass scale:

\[
(-\Delta+m_\kappa^2)\kappa
=
\text{source},
\]

then the exterior tail is Yukawa-suppressed:

\[
\kappa_{\rm ext}
\sim
\frac{\alpha_\kappa Q\,e^{-m_\kappa r}}
{4\pi K_\kappa r}.
\]

This allows nonzero integrated trace charge but avoids a long-range \(1/r\) leak.

Status:

```text
PLAUSIBLE — new scale m_kappa missing.
```

This option is viable only if \(m_\kappa\) is derived or constrained.

---

## Classification

The script produced this classification:

| Model | Status |
|---|---|
| \(S_{\rm trace}=3p\) | PLAUSIBLE interior source |
| integrated \(Q_\kappa\) from positive pressure | RISK / nonzero |
| massless \(\kappa\) with \(Q_\kappa\neq0\) | RISK / exterior \(1/r\) leak |
| compensated trace source | CONSTRAINED_BY_IDENTITY if parent-derived |
| massive/restoring \(\kappa\) | PLAUSIBLE if \(m_\kappa\) derived |
| raw pressure Poisson law as final equation | REJECTED unless screened/projected |

---

## What This Study Established

This study established:

1. \(S_{\rm trace}=3p\) is a plausible interior source candidate.
2. For positive pressure, the integrated trace charge is nonzero:
   \[
   Q_\kappa=\frac{8\pi R^3p_0}{5}.
   \]
3. A massless pressure-sourced \(\kappa\) equation leaks outside as:
   \[
   \kappa_{\rm ext}\sim\frac{1}{r}.
   \]
4. Raw pressure trace cannot be the final unscreened source law.
5. A compensated trace source can remove the monopole charge.
6. A massive/restoring response can suppress long-range leakage.
7. Both compensation and restoring suppression require derivation.

---

## What This Study Did Not Establish

This study did not derive the pressure profile from hydrostatic equilibrium.

It did not derive the compensated source from a parent identity.

It did not derive \(m_\kappa\).

It did not decide whether \(\kappa\) is physical, gauge, or mixed.

It did not solve scalar radiation leakage.

It only showed that raw pressure trace is not exterior-safe.

---

## Current Best Interpretation

A raw pressure/spatial-trace source is plausible for the interior but dangerous for the exterior.

For positive pressure:

\[
Q_\kappa
=
\int 3p\,d^3x
\neq0.
\]

A massless \(\kappa\) equation would then produce:

\[
\kappa_{\rm ext}\sim\frac{1}{r}.
\]

Therefore raw pressure trace cannot be the final unscreened \(\kappa\) source.

The immediate next issue is compensation/projection.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_compensated_trace_constraint.py
```

Purpose:

```text
Test zero-net-trace source construction.
```

Reason:

```text
Raw pressure source creates nonzero kappa charge; compensation/projection is the
immediate issue.
```

Expected result:

```text
A compensated trace source can remove exterior monopole leakage, but only counts
as legitimate if a parent constraint explains the subtraction.
```

---

## Summary

The pressure-trace model gives a hard warning.

The natural interior source:

\[
S_{\rm trace}=3p
\]

creates:

\[
Q_\kappa\neq0.
\]

For a massless \(\kappa\) equation, that creates an exterior scalar trace tail:

\[
\kappa_{\rm ext}\sim\frac{1}{r}.
\]

So the next goblin door is a zero-charge constraint.
