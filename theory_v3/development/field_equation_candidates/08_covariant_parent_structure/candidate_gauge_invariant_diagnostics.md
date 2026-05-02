# Candidate Gauge-Invariant Diagnostics

## What This Document Is

This document is a development note for the `08_covariant_parent_structure/` group.

It is not a full construction of gauge invariants, not a parent theory, and not an observational analysis. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_gauge_invariant_diagnostics.py
```

The guiding question was:

```text
Which current diagnostics are invariant, safe only after gauge fixing,
gauge-aware, missing, or risky?
```

The answer is:

```text
Some diagnostics are safe in reduced settings:
  areal radius R,
  normalized static A,
  TT strain.

Several are gauge-aware or missing:
  AB/kappa_areal,
  kappa response,
  W_i frame-dragging observable,
  curvature-like parent diagnostics,
  conservation identities.
```

The next blocker is:

```text
conservation / source-geometry compatibility.
```

---

## Method Note

This script used diagnostic-specific status categories:

```text
SAFE_INVARIANT
SAFE_GAUGE_FIXED
GAUGE_AWARE
MISSING
RISK
```

The status counts were:

```text
SAFE_INVARIANT: 1
SAFE_GAUGE_FIXED: 3
GAUGE_AWARE: 2
MISSING: 3
RISK: 1
```

This is useful because it does not flatten everything into “pass” or “fail.”

It tells us which quantities can be used safely now and which ones need parent structure before being treated as observables.

---

## Diagnostic Inventory

### Areal Radius R

Status:

```text
SAFE_INVARIANT
```

Use:

```text
Spherical reduction anchor; area of symmetry sphere is 4*pi*R^2.
```

Condition:

```text
Valid in spherical/orbit-space reduction where symmetry spheres exist.
```

Risk:

```text
Not available as a global scalar in arbitrary nonspherical geometries.
```

This is currently the safest scalar diagnostic in the spherical sector.

It is geometric because it is tied to sphere area.

---

### Lapse A with Asymptotic Normalization

Status:

```text
SAFE_GAUGE_FIXED
```

Use:

```text
Static scalar potential / redshift diagnostic.
```

Condition:

```text
Requires static slicing and normalization A -> 1 at infinity.
```

Risk:

```text
Time reparameterization can change unnormalized lapse.
```

The scalar \(A\) channel is safe only after boundary normalization and slicing assumptions are clear.

This fits earlier exterior work, but it is not automatically gauge invariant in arbitrary settings.

---

### AB or kappa_areal

Status:

```text
GAUGE_AWARE
```

Use:

```text
Areal-gauge compensation diagnostic; kappa = 1/2 ln(AB).
```

Condition:

```text
Safe only after areal radius and static/diagonal form are specified.
```

Risk:

```text
Can include coordinate artifacts outside its gauge-aware domain.
```

This is an important caution.

\(\kappa_{\rm areal}\) is useful, but it should not be treated as a full spacetime scalar without additional structure.

---

### Orbit-Space Gradient |grad R|²

Status:

```text
SAFE_GAUGE_FIXED
```

Use:

```text
Gauge-aware spherical diagnostic replacing raw radial B.
```

Condition:

```text
Requires orbit-space formulation and areal-radius scalar R.
```

Risk:

```text
Still belongs to spherical reduction, not a full arbitrary-spacetime invariant
by itself.
```

This is safer than raw \(B\), because it uses the areal-radius scalar and orbit-space geometry.

But it remains a spherical-reduction diagnostic.

---

### TT Strain h_ij^TT

Status:

```text
SAFE_GAUGE_FIXED
```

Use:

```text
Far-zone tensor radiation; plus/cross polarizations.
```

Condition:

```text
Requires TT projection / far-zone wave gauge.
```

Risk:

```text
Parent derivation of TT projection still needed.
```

This is one of the safest radiative diagnostics.

But the parent theory still needs to derive the TT projection and its physical mode count.

---

### Frame-Dragging Observable from W_i

Status:

```text
MISSING
```

Use:

```text
Physical vector/current observable, e.g. rotation of local inertial frames.
```

Condition:

```text
Need gauge-invariant curl/frame-dragging diagnostic.
```

Risk:

```text
Raw W_i may be shift gauge rather than physical frame dragging.
```

This is a major missing diagnostic.

The vector sector should not be compared to observation through raw \(W_i\).

It needs a frame-dragging observable.

---

### kappa Interior Response

Status:

```text
GAUGE_AWARE
```

Use:

```text
Trace/interior matter response diagnostic.
```

Condition:

```text
Requires gauge-fixed or invariant definition of trace/volume response.
```

Risk:

```text
May double-count coordinate volume changes.
```

This reinforces the earlier caution.

\(\kappa\) is useful as a reduced diagnostic, but it is not automatically a parent-level observable.

---

### A_rad Scalar Radiation Amplitude

Status:

```text
RISK
```

Use:

```text
Potential scalar breathing radiation diagnostic.
```

Condition:

```text
Allowed only if explicitly controlled, suppressed, or observationally
constrained.
```

Risk:

```text
Unsuppressed A_rad creates forbidden extra scalar radiation.
```

This remains a controlled hazard.

Do not treat raw \(A_{\rm rad}\) as an allowed physical radiation observable.

---

### Curvature-Like Diagnostics

Status:

```text
MISSING
```

Use:

```text
Gauge-invariant parent-level observables.
```

Condition:

```text
Need construction from parent metric/vacuum geometry.
```

Risk:

```text
Without curvature-like diagnostics, comparisons may rely on gauge variables.
```

This is a major missing piece for a covariant parent.

Eventually, the theory needs curvature-like or invariant geometric diagnostics.

---

### Conserved Flux / Source Identities

Status:

```text
MISSING
```

Use:

```text
Check source-geometry compatibility.
```

Condition:

```text
Need Bianchi-like or continuity identities.
```

Risk:

```text
Source couplings may be inconsistent across sectors.
```

This is now the next blocker.

The sector sources must not be independent hand-assigned rules.

They need compatibility identities.

---

## Diagnostic Safety Table

The script produced this table:

| Diagnostic | Status | Use |
|---|---|---|
| Areal radius \(R\) | SAFE_INVARIANT | Spherical reduction anchor; area of symmetry sphere is \(4\pi R^2\). |
| Lapse \(A\) with asymptotic normalization | SAFE_GAUGE_FIXED | Static scalar potential / redshift diagnostic. |
| \(AB\) or \(\kappa_{\rm areal}\) | GAUGE_AWARE | Areal-gauge compensation diagnostic. |
| Orbit-space gradient \(|\nabla R|^2\) | SAFE_GAUGE_FIXED | Gauge-aware spherical diagnostic replacing raw radial \(B\). |
| TT strain \(h_{ij}^{TT}\) | SAFE_GAUGE_FIXED | Far-zone tensor radiation; plus/cross polarizations. |
| Frame-dragging observable from \(W_i\) | MISSING | Physical vector/current observable. |
| \(\kappa\) interior response | GAUGE_AWARE | Trace/interior matter response diagnostic. |
| \(A_{\rm rad}\) scalar radiation amplitude | RISK | Potential scalar breathing radiation diagnostic. |
| Curvature-like diagnostics | MISSING | Gauge-invariant parent-level observables. |
| Conserved flux/source identities | MISSING | Check source-geometry compatibility. |

This table is the main output.

---

## Safe Comparison Policy

The script proposed this policy.

Use safely now:

```text
areal radius R in spherical reduction,
asymptotically normalized static A,
TT strain in TT/far-zone gauge.
```

Use with gauge warnings:

```text
AB / kappa_areal,
kappa interior response,
orbit-space |grad R|^2 outside spherical context.
```

Do not use as physical observables yet:

```text
raw W_i,
raw A_rad,
raw coordinate trace.
```

This is a strong practical rule for future notes.

---

## What This Study Established

This study established:

1. Areal radius \(R\) is safe in spherical reduction.
2. Static \(A\) is safe after asymptotic normalization.
3. TT strain is safe in TT/far-zone gauge.
4. \(AB / \kappa_{\rm areal}\) is gauge-aware, not fully invariant.
5. \(\kappa\) interior response is gauge-aware.
6. Raw \(W_i\) is missing a frame-dragging observable.
7. Raw \(A_{\rm rad}\) is risky.
8. Curvature-like parent diagnostics are missing.
9. Conservation/source identities are missing.

---

## What This Study Did Not Establish

This study did not construct full gauge invariants.

It did not derive curvature-like diagnostics.

It did not derive \(W_i\)'s observable content.

It did not derive conservation identities.

It did not solve \(\kappa\)'s physical/gauge status.

It only classified diagnostic safety.

---

## Current Best Interpretation

Some diagnostics are safe in reduced settings:

```text
areal radius R,
normalized static A,
TT strain.
```

Several are gauge-aware or missing:

```text
AB/kappa_areal,
kappa response,
W_i frame-dragging observable,
curvature-like parent diagnostics,
conservation identities.
```

The next bottleneck is source-geometry compatibility.

---

## Next Development Target

The next script should be:

```text
candidate_conservation_identity_requirements.py
```

Purpose:

```text
Identify what conservation or Bianchi-like identities the parent theory must
supply so sector source couplings do not contradict one another.
```

Reason:

```text
Diagnostics expose another blocker: source-geometry compatibility.
```

A sector theory cannot become a parent theory unless its sources are mutually consistent.

---

## Summary

The gauge-invariant diagnostics study gives the current safe-use rule:

```text
Use R, normalized static A, and TT strain carefully.
Treat AB/kappa_areal and kappa as gauge-aware.
Do not treat raw W_i, raw A_rad, or raw coordinate trace as physical observables.
```

The next missing structure is conservation identity support.
