# Regimes Summary

## What This Document Is

This document summarizes the `03_regimes/` development group.

This group is a conceptual and observational bridge. It does not define a field equation, prove a theorem, or add a formal postulate. Its purpose is to classify possible vacuum-dynamical regimes and map those regimes onto physical domains where the theory may eventually need different mechanisms.

The two source notes for this group are:

```text
candidate_exchange_creation_relaxation_regimes.md
candidate_regime_map_observations.md
```

The core idea is:

```text
Not all vacuum dynamics should be forced into one conservative-exchange category.
```

Instead, the current development distinguishes:

```text
exchange:
  conservative redistribution of vacuum amount / configuration

creation / destruction:
  net change in vacuum amount

relaxation / fill-in:
  response that smooths, balances, or redistributes after imbalance

mixed regimes:
  combinations of shear-like and traceful behavior
```

This classification protects the static exterior gravity result while leaving room for cosmology, boundaries, collapse, and possible non-equilibrium behavior.

---

## Why a Regime Classification Is Needed

The reduced exterior mechanics branch supports a static compensated exterior structure:

$$
\kappa=0,
$$

with:

$$
s\neq0.
$$

In that branch:

$$
A=e^{\kappa+s},
$$

and:

$$
B=e^{\kappa-s}.
$$

Therefore:

$$
AB=e^{2\kappa}.
$$

So:

$$
\kappa=0\quad\Longleftrightarrow\quad AB=1.
$$

This makes static exterior gravity look like a compensated exchange or relaxation endpoint: the imbalance / trace-like mode is suppressed, while the shear-like mode carries the gravitational field.

However, the framework also treats vacuum as substance-like energy with finite local density. If vacuum amount is tied to volume, then cosmological expansion, boundary growth, collapse, or other non-static processes may not be pure exchange. They may involve net vacuum creation, destruction, or traceful growth.

Therefore the theory needs a way to say:

```text
static exterior gravity may be conservative and compensated,
without forcing every vacuum process everywhere to be conservative exchange.
```

This group provides that classification.

---

## Regime 1: Exchange

Exchange means conservative local redistribution of vacuum substance, amount, or configuration.

In bookkeeping terms, exchange has no net local vacuum amount change:

$$
\delta E_{\rm vac}=0.
$$

If vacuum energy density is constant, then:

$$
E_{\rm vac}=\rho_v V_{\rm vac},
$$

so local conservation of vacuum energy implies:

$$
\delta V_{\rm vac}=0.
$$

In reduced mode language, exchange is expected to be trace-kernel-like. It should not directly source the imbalance mode:

$$
J_\kappa=0.
$$

The exterior can then relax to:

$$
\kappa=0,
$$

while allowing the compensated shear mode:

$$
s\neq0.
$$

This regime is the best current interpretation of static source-free exterior gravity.

In compact language:

```text
Exchange preserves vacuum amount while redistributing configuration.
Static exterior gravity is probably an exchange-like compensated sector.
```

---

## Regime 2: Creation / Destruction

Creation / destruction means a net change in vacuum amount.

Creation corresponds to:

$$
\delta E_{\rm vac}>0,
$$

and, if vacuum density is fixed:

$$
\delta V_{\rm vac}>0.
$$

Destruction corresponds to:

$$
\delta E_{\rm vac}<0,
$$

and:

$$
\delta V_{\rm vac}<0.
$$

This is not just redistribution. It changes the amount of vacuum substance or vacuum volume.

In reduced mode language, creation or destruction may activate a traceful / imbalance sector:

$$
J_\kappa\neq0.
$$

A simple reduced equilibrium with direct \(\kappa\)-sourcing gives:

$$
\kappa=\frac{J_\kappa}{2M_\kappa^2}.
$$

Then:

$$
AB=e^{2\kappa},
$$

so reciprocal compensation is generally broken.

That is not automatically a failure. It means the system is not in the static source-free exterior exchange endpoint.

Possible contexts include:

```text
cosmological expansion,
boundary growth,
vacuum formation,
extreme collapse or sinks,
early-universe behavior,
non-equilibrium vacuum production,
traceful transition events.
```

The current theory does not prove vacuum creation occurs. It only says creation/destruction should not be ruled out prematurely.

---

## Regime 3: Relaxation / Fill-In

Relaxation / fill-in is the response of the surrounding vacuum to a deficit, excess, source, boundary condition, or imbalance.

It is not necessarily the original event. It is the adjustment that follows.

A possible sequence is:

```text
a source or boundary creates imbalance;
the surrounding vacuum reconfigures;
traceful disturbances relax or smooth out;
the static exterior settles into kappa suppression;
compensated shear remains as the stable field.
```

In reduced mechanics, relaxation is represented by terms like:

$$
K_\kappa|\nabla\kappa|^2+M_\kappa^2\kappa^2.
$$

The source-free \(\kappa\) equation can relax to:

$$
\kappa=0
$$

under suitable boundary conditions.

Meanwhile, the shear or exact \(A=e^s\) sector can carry the remaining exterior distortion.

Relaxation therefore connects traceful or non-equilibrium source behavior to the compensated exterior endpoint.

---

## Mixed Regimes

Mixed regimes combine shear-like and traceful behavior.

A mixed regime may have:

$$
\kappa\neq0,
$$

and:

$$
s\neq0.
$$

Equivalently:

$$
AB=e^{2\kappa}\neq1.
$$

Mixed regimes are important because they may become the first deviation channel from GR-like static exterior behavior.

For ordinary weak-field exteriors, observations likely require any \(\kappa\)-leak to be extremely small. But in transitions, boundaries, collapse, cosmology, or non-equilibrium regimes, \(\kappa\)-like behavior may be relevant.

---

## Provisional Regime Table

| Regime | Vacuum amount | Reduced mode behavior | Candidate role |
|---|---|---|---|
| Exchange | conserved | \(J_\kappa=0,\ s\neq0\) | static exterior gravity |
| Creation | increases | \(J_\kappa>0\) possible | expansion, boundary growth |
| Destruction | decreases | \(J_\kappa<0\) possible | collapse, deficits, sinks |
| Relaxation / fill-in | response-dependent | \(\kappa\to0\), shear can remain | equilibration after disturbance |
| Mixed | not purely conserved | \(\kappa\neq0,\ s\neq0\) | deviations, transitions, non-equilibrium regimes |

This table is provisional. It is a map for future tests, not a finished theory.

---

## Observational Mapping

### Static Exterior Gravity

Candidate regime:

```text
exchange + relaxation endpoint
```

The reduced exterior should satisfy:

$$
\kappa=0,
$$

and:

$$
s\neq0.
$$

In the weak-field version:

$$
s(r)=-\frac{2GM}{rc^2}.
$$

Then:

$$
A=e^s\approx1-\frac{2GM}{rc^2},
$$

and:

$$
B=e^{-s}\approx1+\frac{2GM}{rc^2}.
$$

In the stronger mechanics branch, the exact source variable is:

$$
A=e^s,
$$

with an areal-flux law that gives:

$$
A=1-\frac{2GM}{rc^2},
$$

and:

$$
B=\frac1A.
$$

This regime must reproduce ordinary weak-field tests, including Newtonian acceleration, gravitational redshift, light deflection, Shapiro delay, and perihelion precession.

A static exterior \(\kappa\)-leak would produce:

$$
AB\neq1,
$$

and could alter PPN-like behavior. This is a likely future constraint channel.

---

### Cosmological Expansion

Candidate regime:

```text
creation / traceful growth
```

If vacuum density is constant and cosmic volume grows, then total vacuum amount may increase. That suggests that expansion may involve vacuum creation, boundary growth, or traceful dynamics rather than compensated exterior shear.

A rough reduced analogue is:

$$
J_\kappa>0.
$$

This is only speculative. The current static reduced theory does not yet contain a cosmological field equation.

A future cosmology must reproduce Hubble expansion, cosmological redshift, large-scale homogeneity and isotropy, CMB constraints, structure formation, and late-time acceleration if relevant.

---

### Gravitational Waves

Candidate regime:

```text
exchange-like dynamic shear propagation
```

The static scalar shear mode \(s\) is not enough for gravitational waves. A future theory needs tensorial, trace-free, propagating degrees of freedom.

A possible interpretation is:

```text
gravity waves are dynamic trace-free vacuum-configuration shear,
not scalar A-flux and not vacuum creation.
```

This group does not build that sector. It only locates where it may belong in the regime map.

A future wave sector must reproduce wave speed, polarizations, binary inspiral energy loss, observed waveforms, and constraints on extra modes or dispersion.

---

### Black Holes, Collapse, and Strong Fields

Candidate regimes:

```text
exchange / relaxation exterior,
possible mixed or boundary regime near horizons,
possible destruction / compression / traceful behavior in interiors.
```

The exterior Schwarzschild-like branch can be viewed as a strong static exterior exchange/relaxation endpoint. But collapse and interiors may require additional regimes.

Future work must address horizon behavior, interiors, singularity avoidance if any, black-hole thermodynamics, photon spheres, shadows, ringdown, and compact-object mergers.

---

### Matter Formation and Boundaries

Candidate regimes:

```text
creation/destruction + relaxation/fill-in
```

Matter may impose a boundary or interface constraint on vacuum configuration. The source or interface may involve traceful behavior, while the exterior relaxes into compensated shear.

The desired story is:

```text
matter imposes a constraint;
local imbalance or burden appears;
vacuum relaxes;
source-free exterior settles into kappa=0;
A or s carries the exterior field.
```

This is not yet formalized. It must eventually explain why mass sources the correct coefficient and why ordinary matter obeys equivalence-principle constraints.

---

### Laboratory and Solar-System Deviations

Candidate regime:

```text
small mixed regime / kappa-leak constraints
```

A small nonzero \(\kappa\) would give:

$$
A=e^{\kappa+s},
$$

and:

$$
B=e^{\kappa-s}.
$$

Then:

$$
AB=e^{2\kappa}.
$$

This could modify weak-field observables such as light deflection, Shapiro delay, perihelion precession, gravitational redshift, or PPN \(\gamma\)-like behavior.

Because solar-system constraints are strong, ordinary weak-field \(\kappa\)-leak must likely be very small.

This is the most concrete recommended next quantitative test.

---

## Pressure Points

The regime map creates several ways for the theory to fail.

### 1. Static exterior \(\kappa\)-leak

If the theory generically predicts \(\kappa\neq0\) in ordinary weak-field static exteriors, it may conflict with precision tests.

### 2. Wrong shear or flux coefficient

If the theory cannot derive the coefficient:

$$
-\frac{2GM}{rc^2},
$$

or the equivalent exact areal-flux normalization, it fails the weak-field entry test.

### 3. Gauge fragility

If predictions depend on arbitrary coordinate choices rather than gauge-fixed or geometric structures, the model is not physically well-posed.

### 4. Cosmological creation without observational fit

If vacuum creation is used for expansion, it must reproduce observed expansion history and structure constraints.

### 5. Unwanted extra modes

Traceful creation/destruction modes must not appear where observations rule them out.

### 6. Equivalence-principle violations

If matter-vacuum coupling varies by composition in ordinary regimes, the theory faces strong constraints.

---

## Current Best Interpretation

The current best regime interpretation is:

```text
Static exterior gravity:
  exchange / relaxation endpoint
  kappa suppressed
  compensated shear or A-flux remains

Cosmological expansion:
  possible creation / traceful growth
  not yet modeled

Gravitational waves:
  future dynamic tensor-shear sector
  not scalar A-flux alone

Black holes and collapse:
  exchange-like exterior plus possible mixed/interior regimes

Laboratory deviations:
  small kappa-leak is the first likely test channel
```

This keeps the theory from overclaiming that all vacuum dynamics are conservative exchange, while preserving the static exterior compensation result.

---

## Recommended Next Work

The immediate next technical target is:

```text
candidate_kappa_leak_deviation.py
```

Purpose:

```text
Compute weak-field observable consequences of a small nonzero kappa mode.
```

Test:

$$
\kappa(r)=\varepsilon_\kappa(r),
$$

with a standard weak shear or exact \(A\)-flux background.

Then compare:

$$
A=e^{\kappa+s},
$$

and:

$$
B=e^{\kappa-s}
$$

to GR-like weak-field expectations.

After that, possible next notes include:

```text
candidate_cosmic_vacuum_creation.md
candidate_exchange_creation_principle.md
candidate_dynamic_shear_wave_sector.md
```

But the safest order is:

```text
1. Finish reduced static exterior mechanics.
2. Quantify kappa-leak deviations.
3. Compare deviations to weak-field observational constraints.
4. Only then develop cosmology / creation.
5. Later develop tensor waves and strong-field regimes.
```

---

## One-Paragraph Summary

The `03_regimes/` group introduces a provisional classification of vacuum dynamics into exchange, creation/destruction, relaxation/fill-in, and mixed regimes. Exchange is conservative redistribution and is the best current interpretation of static exterior gravity after relaxation: \(\kappa=0\) while compensated shear or \(A=e^s\) carries the field. Creation/destruction allows net vacuum amount change and may be relevant to cosmology, boundary growth, collapse, or other non-static regimes, but it is not yet formalized. Relaxation/fill-in explains how traceful disturbances or source-interface effects may settle into compensated exterior behavior. The observational map identifies static weak-field gravity as the entry test, small \(\kappa\)-leak as the first likely deviation channel, cosmology as a possible creation regime, and gravitational waves as requiring a future tensorial shear sector.

---

## Status Snapshot

```text
Best-developed regime:
  static exterior exchange / relaxation endpoint

Core exterior condition:
  kappa = 0

Metric consequence:
  AB = 1

Remaining exterior field:
  compensated shear s, or exact A = exp(s)

Traceful regime candidate:
  creation / destruction, possibly kappa-like

Bridge regime:
  relaxation / fill-in

First deviation channel:
  small nonzero kappa leak

Main caveat:
  regime classification is conceptual and not yet derived from a full field equation

Best next script:
  candidate_kappa_leak_deviation.py
```
