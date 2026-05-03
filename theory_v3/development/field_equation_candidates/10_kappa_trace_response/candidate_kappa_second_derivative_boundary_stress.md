# Candidate Kappa Second Derivative Boundary Stress

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final interface theory, not a derived \(\kappa\) source law, and not a proof that the compact profile is physically produced by matter. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_second_derivative_boundary_stress.py
```

The guiding question was:

```text
Does a compact interior kappa profile create hidden boundary stress through
second-derivative or effective-source jumps?
```

The answer is:

```text
The previous C1 compact profile avoids exterior flux but has a second
derivative/effective-source jump at the boundary.

A smoother C2 profile:

  kappa = k0 (1 - r^2/R^2)^3

matches exterior zero through second derivative, keeps boundary flux zero,
and has zero net effective source.

This removes the hidden shell-stress trap at toy level.

But source compatibility remains missing.
```

---

## Why This Study Matters

The previous boundary-layer model showed that a compact interior \(\kappa\) profile can satisfy:

\[
\kappa(R)=0,
\]

\[
\kappa'(R)=0,
\]

and:

\[
F_\kappa(R)=0.
\]

That avoids exterior scalar flux.

But value and first-derivative matching are not always enough.

If \(\kappa''\) or the effective source jumps at the interface, the model may hide a shell source or boundary stress.

This study checks that trap.

---

## C1 Compact Profile

The earlier compact profile was:

\[
\kappa(r)
=
\kappa_0
\left(
1-\frac{r^2}{R^2}
\right)^2.
\]

It satisfies:

\[
\kappa(R)=0,
\]

and:

\[
\kappa'(R)=0.
\]

But the second derivative at the inner boundary is:

\[
\kappa''(R-)
=
\frac{8\kappa_0}{R^2}.
\]

The areal Laplacian at the inner boundary is:

\[
\Delta\kappa(R-)
=
\frac{8\kappa_0}{R^2}.
\]

For exterior:

\[
\kappa_{\rm ext}=0,
\]

we have:

\[
\kappa''(R+)=0,
\]

and:

\[
\Delta\kappa(R+)=0.
\]

Thus the second derivative / effective source jumps at \(R\).

Status:

```text
RISK — may imply boundary layer or hidden interface stress.
```

This means the C1 profile is not smooth enough if hidden shell stress is forbidden.

---

## C2 Smoother Compact Profile

The smoother profile is:

\[
\kappa(r)
=
\kappa_0
\left(
1-\frac{r^2}{R^2}
\right)^3.
\]

At the boundary:

\[
\kappa(R)=0,
\]

\[
\kappa'(R)=0,
\]

\[
\kappa''(R-)=0,
\]

and:

\[
\Delta\kappa(R-)=0.
\]

This profile matches exterior zero through second derivative and effective source.

Status:

```text
DERIVED_REDUCED
```

This removes the hidden second-derivative jump at toy level.

---

## Flux and Charge for the C2 Profile

For the C2 profile, the flux is:

\[
F_\kappa(r)
=
-\frac{24\pi\kappa_0r^3(R^2-r^2)^2}{R^6}.
\]

At the boundary:

\[
F_\kappa(R)=0.
\]

The integrated effective source is:

\[
\int \Delta\kappa\,d^3x=0.
\]

Status:

```text
DERIVED_REDUCED
```

So the C2 profile keeps:

```text
zero boundary flux,
zero net effective source,
zero exterior scalar charge.
```

---

## Regular Center Check

At the center:

\[
\kappa(0)=\kappa_0,
\]

\[
\kappa'(0)=0,
\]

\[
\kappa''(0)
=
-\frac{6\kappa_0}{R^2},
\]

and:

\[
\Delta\kappa(0)
=
-\frac{18\kappa_0}{R^2}.
\]

Status:

```text
DERIVED_REDUCED — source sign / compatibility still needs checking.
```

The C2 profile is regular at the center.

---

## Effective Source Shape

For the C2 profile, the effective source shape is:

\[
S_{\rm eff}
\sim
\Delta\kappa.
\]

The script found:

\[
S_{\rm eff}
=
-\frac{6\kappa_0(-R+r)(R+r)(-3R^2+7r^2)}{R^6}.
\]

This source shape has positive and negative regions so that net charge vanishes.

It resembles a compensated trace source rather than raw positive pressure.

Status:

```text
CONSTRAINED_BY_IDENTITY — must be derived from trace/minimum law.
```

This is the next major problem.

The smoother profile works mathematically, but its implied source is compensated-like.

It is not raw pressure.

---

## Interface Interpretation

The C1 profile:

```text
matches value and first derivative,
but jumps in second derivative / effective source.
```

The C2 profile:

```text
matches value, first derivative, and second derivative,
has zero boundary flux,
has zero net effective source.
```

Interpretation:

```text
if hidden shell stress is forbidden, use at least C2 compact profile,
or derive an allowed boundary layer / interface stress explicitly.
```

Status:

```text
CONSTRAINED_BY_IDENTITY — physical interface derivation missing.
```

---

## Failure Controls

Boundary stress control fails if:

1. \(\kappa''\) jumps and no interface stress accounts for it.
2. \(\Delta\kappa\) jumps and implies an unmodeled shell source.
3. A smoother profile cannot be sourced by matter trace or a shifted minimum.
4. The compensated effective source is inserted by hand.
5. Higher derivative terms in the true action require even higher smoothness.
6. Boundary smoothness hides rather than explains scalar confinement.

These failure controls should remain active.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| C1 profile value / first derivative match | DERIVED_REDUCED |
| C1 profile second derivative jump | RISK |
| C2 profile value / first / second derivative match | DERIVED_REDUCED |
| C2 boundary flux zero | DERIVED_REDUCED |
| C2 net effective source zero | DERIVED_REDUCED |
| C2 source shape derived from matter trace | MISSING |
| physical interface law | MISSING |
| required smoothness from true action | MISSING |

---

## What This Study Established

This study established:

1. The C1 compact profile avoids exterior flux but has a second-derivative jump.
2. The C2 compact profile:
   \[
   \kappa=\kappa_0(1-r^2/R^2)^3
   \]
   removes that jump.
3. The C2 profile has zero boundary flux.
4. The C2 profile has zero net effective source.
5. The C2 profile is regular at the center.
6. Its implied source is compensated-like.
7. Source compatibility remains missing.

---

## What This Study Did Not Establish

This study did not derive the C2 profile.

It did not derive the implied source from pressure, stress trace, or \(\kappa_{\min}\).

It did not derive the physical interface law.

It did not determine the required smoothness from the true \(\kappa\) action.

It did not prove the absence of all hidden boundary stress.

It only showed that a smoother toy compact profile can remove the second-derivative jump.

---

## Current Best Interpretation

The C1 profile is not clean enough if hidden shell stress is forbidden.

The C2 profile is better:

\[
\kappa
=
\kappa_0
\left(
1-\frac{r^2}{R^2}
\right)^3.
\]

It matches exterior zero through second derivative, keeps boundary flux zero, and has zero net effective source.

But this moves the burden to source compatibility.

The implied source is compensated-like and must be derived.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_boundary_layer_source_compatibility.py
```

Purpose:

```text
Check whether plausible pressure / trace / minimum-shift physics can produce
the C2 compact profile.
```

Reason:

```text
C2 compactness works mathematically; now source compatibility is the issue.
```

Expected result:

```text
Classify whether the C2 effective source can be interpreted as:
  raw trace source,
  compensated trace source,
  shifted local minimum,
  boundary/interface source,
  or merely hand-chosen smoothing.
```

---

## Summary

The second-derivative boundary stress check finds:

```text
C1:
  value and flux match,
  second derivative jumps.

C2:
  value, flux, and second derivative match,
  no exterior scalar charge,
  no toy hidden shell stress.
```

But the C2 effective source is compensated-like.

The next goblin gate is source compatibility.
