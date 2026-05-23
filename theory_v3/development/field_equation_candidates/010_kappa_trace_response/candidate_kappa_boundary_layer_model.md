# Candidate Kappa Boundary Layer Model

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a derived matter/vacuum interface theory, not a final \(\kappa\) source law, and not a proof that the boundary layer is physically realized. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_boundary_layer_model.py
```

The guiding question was:

```text
Can interior kappa exist while exterior kappa and exterior flux vanish?
```

The answer is:

```text
Yes, as a toy boundary-control model.

A compact interior profile can allow:
  interior kappa response,
  kappa(R)=0,
  kappa'(R)=0,
  F_kappa(R)=0,
  exterior kappa=0.
```

This supports the idea that \(\kappa\) can be an interior, non-propagating trace relaxation variable rather than a breathing wave.

The next trap is hidden boundary stress from second-derivative behavior.

---

## Why This Study Matters

The non-inertial \(\kappa\) relaxation model says:

```text
kappa is not a wave,
kappa is a non-inertial trace/volume relaxation coordinate,
matter trace shifts the local vacuum-curvature minimum,
kappa relaxes toward that minimum,
there is no independent kappa momentum channel.
```

That model still needs a boundary mechanism.

If interior \(\kappa\) exists but exterior \(\kappa\) must vanish, the interface must not export scalar charge or scalar flux.

This study tests a simple compact profile.

---

## Boundary Requirements

Exterior-safe boundary conditions are:

\[
\kappa(R+)=0,
\]

and:

\[
\partial_r\kappa(R+)=0.
\]

The flux diagnostic is:

\[
F_\kappa(R)
=
4\pi R^2\partial_r\kappa(R).
\]

Exterior safety requires:

\[
F_\kappa(R)=0.
\]

---

## Toy Compact Interior Profile

The toy compact interior profile is:

\[
\kappa(r)
=
\kappa_0
\left(
1-\frac{r^2}{R^2}
\right)^2.
\]

The boundary values are:

\[
\kappa(R)=0,
\]

and:

\[
\kappa'(R)=0.
\]

The center values are:

\[
\kappa(0)=\kappa_0,
\]

and:

\[
\kappa'(0)=0.
\]

Status:

```text
DERIVED_REDUCED
```

This profile is smooth enough to match to exterior \(\kappa=0\) in value and first derivative.

---

## Boundary Flux Diagnostic

For the toy profile, the flux diagnostic is:

\[
F_\kappa(r)
=
4\pi r^2\kappa'(r).
\]

The script found:

\[
F_\kappa(r)
=
\frac{16\pi\kappa_0r^3(-R^2+r^2)}{R^4}.
\]

At the boundary:

\[
F_\kappa(R)=0.
\]

Status:

```text
DERIVED_REDUCED
```

So this compact profile exports no boundary flux.

---

## Exterior Extension

Define:

\[
\kappa_{\rm ext}(r>R)=0.
\]

The interior profile satisfies:

\[
\kappa(R-)=0,
\]

and:

\[
\kappa'(R-)=0.
\]

The exterior satisfies:

\[
\kappa(R+)=0,
\]

and:

\[
\kappa'(R+)=0.
\]

Therefore there is no jump in value or first derivative.

Status:

```text
CONSTRAINED_BY_IDENTITY — second derivative / stress layer not yet checked.
```

This is good, but not enough.

A hidden shell source may appear if second derivatives or implied stress terms jump badly.

---

## Effective Source Implied by Profile

For a schematic elliptic operator:

\[
\Delta_{\rm areal}\kappa
=
\kappa''
+
\frac{2}{r}\kappa',
\]

the toy profile implies:

\[
\Delta\kappa
=
\frac{4\kappa_0(-3R^2+5r^2)}{R^4}.
\]

Status:

```text
DERIVED_REDUCED — source law not derived.
```

This is the effective source shape required to support the boundary-confined profile.

It has not been derived from pressure or trace exchange.

---

## Effective Source Integral

The integrated effective source is:

\[
4\pi\int_0^R r^2\Delta\kappa\,dr.
\]

The script found:

\[
4\pi\int_0^R r^2\Delta\kappa\,dr=0.
\]

By the divergence theorem this equals the boundary flux.

Since boundary flux is zero, the integrated source is zero.

Status:

```text
DERIVED_REDUCED
```

This matches the zero-charge projection idea.

---

## Boundary-Layer Interpretation

The toy profile shows a possible pattern:

```text
kappa can be nonzero inside matter,
kappa can relax to zero at the boundary,
kappa' can also vanish at the boundary,
exterior kappa can be identically zero.
```

Interpretation:

```text
trace/volume response is interior-confined,
no scalar charge is exported,
no exterior breathing field is launched.
```

Status:

```text
CONSTRAINED_BY_IDENTITY — interface physics missing.
```

The profile is chosen, not derived.

---

## Compatibility With Non-Inertial Relaxation

The profile is compatible with non-inertial relaxation if:

```text
kappa_min(r) is nonzero inside matter,
kappa_min(R)=0,
kappa_min'(R)=0,
exterior kappa_min=0.
```

Then \(\kappa\) can relax locally toward \(\kappa_{\min}\) without carrying momentum through the boundary.

This realizes:

```text
local trace relaxation,
no propagating breathing wave.
```

Status:

```text
PLAUSIBLE — kappa_min source law missing.
```

---

## Failure Controls

The boundary-layer model fails if:

1. \(\kappa'(R+)\) is nonzero and exports flux.
2. The profile requires an unphysical shell source at \(R\).
3. A second derivative jump creates hidden boundary stress.
4. The chosen profile cannot be produced by trace/pressure source.
5. Boundary confinement is inserted only to hide scalar radiation.
6. Non-inertial relaxation secretly includes a second-order wave channel.

The next failure control is the second-derivative/interface stress check.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| compact profile \(\kappa=\kappa_0(1-r^2/R^2)^2\) | PLAUSIBLE toy model |
| \(\kappa(R)=0\) | DERIVED_REDUCED |
| \(\kappa'(R)=0\) | DERIVED_REDUCED |
| boundary flux \(F_\kappa(R)=0\) | DERIVED_REDUCED |
| exterior \(\kappa=0\) extension | CONSTRAINED_BY_IDENTITY |
| effective source integral zero | DERIVED_REDUCED |
| source/interface derivation | MISSING |
| hidden boundary stress check | MISSING |

---

## What This Study Established

This study established:

1. A compact interior \(\kappa\) profile can be nonzero inside matter.
2. It can satisfy:
   \[
   \kappa(R)=0.
   \]
3. It can satisfy:
   \[
   \kappa'(R)=0.
   \]
4. Therefore:
   \[
   F_\kappa(R)=0.
   \]
5. Exterior \(\kappa=0\) can be matched without a value or first-derivative jump.
6. The effective source integral is zero.
7. This supports interior-confined trace relaxation.

---

## What This Study Did Not Establish

This study did not derive the profile.

It did not derive the interface physics.

It did not derive \(S_{\rm trace}\).

It did not prove source compatibility.

It did not check second-derivative stress.

It did not prove that no shell layer appears.

It only showed that boundary-confined \(\kappa\) is structurally possible.

---

## Current Best Interpretation

A toy compact \(\kappa\) profile can allow:

```text
interior kappa response,
kappa(R)=0,
kappa'(R)=0,
F_kappa(R)=0,
exterior kappa=0.
```

This supports the idea that \(\kappa\) can be an interior, non-propagating trace relaxation variable rather than a breathing wave.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_second_derivative_boundary_stress.py
```

Purpose:

```text
Check hidden shell/boundary stress from derivative jumps.
```

Reason:

```text
Value and flux match, but second derivative/interface stress is the next trap.
```

Expected result:

```text
Classify whether the compact profile creates hidden boundary stress,
whether higher smoothness is needed, or whether the interface source must be
derived explicitly.
```

---

## Summary

The boundary-layer model passes the first goblin gate:

\[
\kappa(R)=0,
\qquad
\kappa'(R)=0,
\qquad
F_\kappa(R)=0.
\]

It allows interior \(\kappa\) without exterior scalar leakage.

The next goblin gate is:

```text
does kappa'' create a hidden shell or boundary stress?
```
