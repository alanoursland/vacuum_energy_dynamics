# Covariant Parent Structure Summary

## Purpose

This document summarizes the `08_covariant_parent_structure/` development group.

This group began after the reduced sector program had established a useful architecture:

```text
A_constraint -> scalar/static mass response
A_rad        -> controlled scalar-radiation hazard
kappa        -> trace/interior response
W_i          -> vector/current/frame-dragging response
h_ij^TT      -> tensor/quadrupole/radiative response
```

The goal of group 08 was not to derive the full parent theory.

The goal was to ask:

```text
Can these reduced sectors be organized as the shadow of one deeper
geometric/covariant parent structure?
```

The answer is:

```text
A coherent reduced sector bundle exists.

A covariant parent has not yet been derived.
```

The main blockers are:

```text
gauge structure,
metric/geometric recombination,
gauge-invariant diagnostics,
conservation/source identities.
```

---

## Directory Scope

This group should contain:

```text
candidate_sector_bundle_inventory.py
candidate_sector_bundle_inventory.md

candidate_covariant_parent_requirements.py
candidate_covariant_parent_requirements.md

candidate_constraint_vs_evolution_split.py
candidate_constraint_vs_evolution_split.md

candidate_gauge_structure_requirements.py
candidate_gauge_structure_requirements.md

candidate_metric_geometric_recombination.py
candidate_metric_geometric_recombination.md

candidate_gauge_invariant_diagnostics.py
candidate_gauge_invariant_diagnostics.md

candidate_conservation_identity_requirements.py
candidate_conservation_identity_requirements.md

covariant_parent_structure_summary.md
```

This is a complete group.

It does not solve the parent theory.

It maps the requirements and blockers.

---

## Main Result

The main result is:

```text
The reduced sector architecture is coherent but not covariantly closed.
```

The strongest reduced support exists for:

```text
A_constraint static scalar response
h_ij^TT tensor radiation
```

The weakest or missing parent structures are:

```text
W_i gauge/current identity,
kappa stress/trace identity,
gauge-invariant observables,
metric recombination,
constraint propagation,
Bianchi-like source-geometry identity.
```

This is progress because it prevents overclaiming.

The goblin rule for this group is:

```text
Do not call the cave a castle.
Map the tunnels first.
```

---

## Study 1: Sector Bundle Inventory

Files:

```text
candidate_sector_bundle_inventory.py
candidate_sector_bundle_inventory.md
```

This study inventoried the current reduced sectors:

| Sector | Variable | Role |
|---|---|---|
| scalar constraint | \(A_{\rm constraint}\) | static mass response |
| scalar radiative hazard | \(A_{\rm rad}\) | controlled or absent scalar radiation |
| trace/interior | \(\kappa\) | pressure/stress/trace response candidate |
| vector current | \(W_i\) | frame dragging / current response |
| tensor radiation | \(h_{ij}^{TT}\) | plus/cross gravitational radiation |

A key distinction was recorded:

```text
A moving gravity well is not automatically a scalar gravity wave.
```

A moving source can carry a translated or retarded scalar constraint configuration:

$$
A(x,t)=A_{\rm static}(x-X(t)).
$$

That is different from a free scalar breathing wave with dispersion:

$$
\omega^2=c^2k^2.
$$

Conclusion:

```text
The sector bundle is coherent as a reduced architecture.
```

But it is not yet a parent theory.

---

## Study 2: Covariant Parent Requirements

Files:

```text
candidate_covariant_parent_requirements.py
candidate_covariant_parent_requirements.md
```

This study classified what a parent theory must explain.

It found:

```text
SATISFIED_REDUCED: 2
PARTIAL: 6
MISSING: 3
RISK: 1
```

Strong reduced results:

```text
R1: Static scalar mass response
R6: Tensor TT radiation sector
```

Blocking missing or risky structures:

```text
R8: Gauge structure
R10: Metric/geometric recombination
R11: Conservation identities
R12: Avoid overclaiming GR equivalence
```

Conclusion:

```text
The reduced sector program is coherent but not yet a covariant parent.
```

---

## Study 3: Constraint vs Evolution Split

Files:

```text
candidate_constraint_vs_evolution_split.py
candidate_constraint_vs_evolution_split.md
```

This study classified sectors by equation role:

```text
A_constraint -> constraint / elliptic
A_rad        -> absent or controlled
kappa        -> relaxation / interior response
W_i          -> vector response, equation type TBD
h_ij^TT      -> evolution / hyperbolic
gauge modes  -> nonphysical / to be projected
source identities -> constraint identities
```

It found:

```text
SATISFIED_REDUCED: 2
PARTIAL: 3
MISSING: 2
```

Missing blockers:

```text
gauge structure
conservation identities
```

Conclusion:

```text
The equation-type split is clearer, but the parent theory still lacks gauge
and conservation structure.
```

---

## Study 4: Gauge Structure Requirements

Files:

```text
candidate_gauge_structure_requirements.py
candidate_gauge_structure_requirements.md
```

This study asked what gauge structure the parent must provide.

It found:

```text
SATISFIED_REDUCED: 1
PARTIAL: 4
MISSING: 3
```

Strongest reduced gauge support:

```text
TT plus/cross basis
```

Missing blockers:

```text
Vector W_i gauge behavior
Gauge-invariant observable set
Coordinate recombination map
```

Conclusion:

```text
Gauge structure is still a parent-theory blocker.
```

---

## Study 5: Metric / Geometric Recombination

Files:

```text
candidate_metric_geometric_recombination.py
candidate_metric_geometric_recombination.md
```

This study proposed a schematic weak-field recombination map:

```text
A_constraint -> g_tt / lapse
kappa        -> spatial trace / volume response
W_i          -> g_ti / shift
h_ij^TT      -> spatial TT radiation
```

It found:

```text
SATISFIED_REDUCED: 2
PARTIAL: 3
MISSING: 2
```

The map exists, but the parent derivation does not.

Main risks:

```text
A_rad could double-count scalar trace/lapse perturbations.
kappa could double-count coordinate volume changes.
W_i could double-count shift gauge.
A_constraint and kappa may mix in non-static or non-areal gauges.
Source coupling may be inconsistent without conservation identities.
```

Conclusion:

```text
A recombination map exists, but it is not yet a covariant parent.
```

---

## Study 6: Gauge-Invariant Diagnostics

Files:

```text
candidate_gauge_invariant_diagnostics.py
candidate_gauge_invariant_diagnostics.md
```

This study classified diagnostic safety.

It found:

```text
SAFE_INVARIANT: 1
SAFE_GAUGE_FIXED: 3
GAUGE_AWARE: 2
MISSING: 3
RISK: 1
```

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

Conclusion:

```text
Some reduced diagnostics are safe, but the parent observable set is missing.
```

---

## Study 7: Conservation Identity Requirements

Files:

```text
candidate_conservation_identity_requirements.py
candidate_conservation_identity_requirements.md
```

This was the hardest check.

It found:

```text
SATISFIED_REDUCED: 0
PARTIAL: 4
MISSING: 4
```

Partial support:

```text
mass continuity assumptions,
quadrupole source structure,
tensor radiation energy scaling,
no-source exterior policy.
```

Missing identities:

```text
current/W_i identity,
kappa stress/trace identity,
constraint propagation,
Bianchi-like geometric identity.
```

Conclusion:

```text
Conservation/source identities are not solved.
```

This is a hard blocker for a covariant parent.

---

## Current Best Architecture

The current reduced architecture is:

### Scalar Static Sector

Variable:

$$
A_{\rm constraint}.
$$

Role:

```text
static scalar mass response,
Newtonian potential,
lapse / g_tt slot,
constraint-like field.
```

Status:

```text
strong reduced support.
```

### Scalar Radiative Hazard

Variable:

$$
A_{\rm rad}.
$$

Role:

```text
possible scalar breathing radiation.
```

Status:

```text
absent or controlled by policy.
```

Allowed only if:

```text
projected out,
damped,
absorbed,
relaxed,
massive/short-ranged,
weakly coupled,
or observationally constrained.
```

### Trace / Interior Sector

Variable:

$$
\kappa.
$$

Role:

```text
trace/volume/interior matter response candidate.
```

Status:

```text
useful reduced diagnostic,
not yet parent-derived,
gauge-aware.
```

### Vector / Current Sector

Variable:

$$
W_i.
$$

Role:

```text
frame dragging,
mass current,
angular momentum response.
```

Status:

```text
needed but underdeveloped.
```

Missing:

```text
gauge behavior,
source equation,
frame-dragging observable,
current conservation identity.
```

### Tensor Radiation Sector

Variable:

$$
h_{ij}^{TT}.
$$

Role:

```text
ordinary long-range gravitational radiation,
plus/cross modes,
quadrupole tensor flux.
```

Status:

```text
strong reduced support.
```

Missing:

```text
covariant derivation,
parent gauge projection,
source conservation,
radiation reaction.
```

---

## What Group 08 Established

Group 08 established:

1. The reduced sector bundle is coherent.
2. \(A_{\rm constraint}\) and \(h_{ij}^{TT}\) are the strongest pillars.
3. \(A_{\rm rad}\) remains a controlled hazard.
4. \(\kappa\) is useful but gauge-aware and source-law incomplete.
5. \(W_i\) is necessary but missing gauge/current structure.
6. A weak-field recombination map exists.
7. Gauge-invariant diagnostics are only partially available.
8. Conservation identities are not solved.
9. The parent theory is not yet covariantly closed.

---

## What Group 08 Did Not Establish

Group 08 did not derive:

```text
a covariant action,
gauge transformations,
metric recombination from first principles,
stress-energy coupling,
Bianchi-like identities,
constraint propagation,
W_i dynamics,
kappa source law,
curvature-like observables.
```

It also did not prove equivalence to GR.

It only mapped the parent-structure gap.

---

## Current Best Claim

The strongest safe claim after group 08 is:

```text
The theory has a coherent reduced sector architecture, but not yet a closed
covariant parent.
```

The strongest reduced sectors are:

```text
A_constraint static scalar response
h_ij^TT tensor radiation
```

The major unresolved parent requirements are:

```text
gauge structure,
metric recombination,
invariant diagnostics,
conservation/source identities.
```

---

## Why This Group Should End Here

This group has done what it needed to do.

It identified the parent-theory blockers:

```text
gauge,
recombination,
observables,
conservation.
```

Continuing inside the same group would start a new project: actually attempting to build one of those missing structures.

That should be group 09.

---

## Recommended Group 09 Options

### Option 1: Vector Current and Frame Dragging

```text
09_vector_current_frame_dragging
```

Reason:

```text
W_i is repeatedly identified as necessary and underdeveloped.
```

Goal:

```text
derive or test a vector current sector tied to frame-dragging observables.
```

### Option 2: Conservation and Source Coupling

```text
09_conservation_source_coupling
```

Reason:

```text
conservation identities are the hardest parent-theory blocker.
```

Goal:

```text
derive continuity/current/stress/quadrupole compatibility identities.
```

### Option 3: Gauge and Observable Diagnostics

```text
09_gauge_observable_structure
```

Reason:

```text
gauge-invariant diagnostics are missing.
```

Goal:

```text
construct safe observables and distinguish physical modes from coordinate
artifacts.
```

### Option 4: Covariant Parent Attempt

```text
09_covariant_parent_attempt
```

Reason:

```text
try to assemble a parent action/equation structure.
```

Risk:

```text
may be too early because W_i, kappa, and conservation identities are still weak.
```

---

## Recommended Next Group

The best next group is probably:

```text
09_vector_current_frame_dragging
```

Why?

Because \(W_i\) appears repeatedly as a missing piece:

```text
gauge behavior missing,
source identity missing,
frame-dragging observable missing,
equation type TBD.
```

It is concrete enough to study.

It also fills a known physical gap:

```text
rotation / frame dragging / mass current response.
```

A good first script would be:

```text
candidate_vector_frame_dragging_observable.py
```

Purpose:

```text
distinguish raw W_i from physical frame-dragging diagnostics such as curls,
precession-like quantities, or gravitomagnetic analogues.
```

---

## Closing Summary

The `08_covariant_parent_structure/` group is a parent-theory audit.

It concludes:

```text
Reduced sector architecture: coherent.
Covariant parent: not yet derived.
```

The reduced theory currently has two strong pillars:

```text
A_constraint
h_ij^TT
```

and three underdeveloped sectors:

```text
A_rad
kappa
W_i
```

The parent-theory blockers are:

```text
gauge structure,
metric recombination,
invariant diagnostics,
conservation identities.
```

This is not a failure.

It is the map of what must be built next.
