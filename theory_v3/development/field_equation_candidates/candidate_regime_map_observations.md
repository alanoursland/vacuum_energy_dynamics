# Candidate Regime Map to Observations

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or field equation. It does not add a formal commitment to the theory.

Its purpose is to map the current candidate vacuum-dynamical regimes to observational domains.

The regimes are:

```text
exchange
creation / destruction
relaxation / fill-in
mixed regimes
```

The goal is to ask:

```text
Where might each regime appear in the real universe?
What must each regime reproduce?
What observations could contradict the assignment?
```

This document follows from:

```text
candidate_exchange_creation_relaxation_regimes.md
candidate_exchange_creation_distinction_test.py
candidate_exchange_creation_distinction_lab_report.md
reduced_exterior_mode_program_summary.md
candidate_reduced_exterior_action.md
candidate_areal_gauge_kappa_condition.md
```

The central caution is that the reduced theory is not yet a full covariant theory. This map is provisional.

---

## Current Reduced Picture

In the static spherical areal-gauge exterior, the reduced modes are:

$$\kappa=\frac{\ln A+\ln B}{2},$$

and:

$$s=\frac{\ln A-\ln B}{2}.$$

Then:

$$AB=e^{2\kappa}.$$

So:

$$\kappa=0\quad\Longleftrightarrow\quad AB=1.$$

The reduced exterior program suggests that static exterior gravity is described by:

$$\kappa=0,$$

with:

$$s\neq0.$$

The shear/source-law toy gives:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

For a spherical source of mass \(M\):

$$s(r)=-\frac{2GM}{rc^2}.$$

Then:

$$A=e^s\approx1-\frac{2GM}{rc^2},$$

and:

$$B=e^{-s}\approx1+\frac{2GM}{rc^2}.$$

This reproduces the weak-field exterior behavior while preserving:

$$AB=1.$$

The exchange/creation distinction test classified reduced operators as:

```text
exchange:
  J_kappa = 0
  shear active
  AB = 1

creation/destruction:
  J_kappa != 0
  traceful
  AB != 1 generically

relaxation:
  tends to suppress kappa
  can leave shear if maintained by source/boundary data
```

This document maps those regimes to possible observational domains.

---

## Regime Summary

| Regime | Reduced behavior | Possible physical role | Observational domain |
|---|---|---|---|
| Exchange | \(J_\kappa=0,\ s\neq0\) | conservative redistribution / compensated shear | static exterior gravity |
| Relaxation / fill-in | \(\kappa\to0\) | vacuum rebalancing after disturbance | static settling, exterior equilibrium |
| Creation | \(J_\kappa>0\) possible | net vacuum amount increase | cosmological expansion, boundary growth |
| Destruction | \(J_\kappa<0\) possible | net vacuum amount decrease | collapse, sinks, extreme interiors |
| Mixed | \(J_\kappa\neq0,\ s\neq0\) | shear plus traceful leakage | deviations, transitions, non-equilibrium regimes |

This table is not a claim that each assignment is correct. It is a candidate map for future testing.

---

## Domain 1: Static Exterior Gravity

### Candidate Regime

```text
exchange + relaxation endpoint
```

### Reduced Description

Static exterior gravity is currently the best-developed regime.

The reduced picture is:

$$\kappa=0,$$

and:

$$s\neq0.$$

Mass sources the shear mode:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

Outside the source:

$$\nabla^2s=0.$$

For spherical mass:

$$s(r)=-\frac{2GM}{rc^2}.$$

The metric factors are:

$$A=e^s,$$

and:

$$B=e^{-s}.$$

So:

$$AB=1.$$

### What This Must Reproduce

This regime must reproduce the observed weak-field tests of gravity.

At minimum, it must match:

```text
Newtonian acceleration
gravitational redshift
light deflection
Shapiro delay
perihelion precession in the weak-field limit
gamma_v = 1 / PPN gamma = 1 behavior
```

The current reduced chain directly supports the weak-field exterior coefficients:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

This is necessary for GR-like weak-field recovery.

### Possible Contradictions

This assignment would be challenged if the theory predicts a detectable \(\kappa\)-leak in ordinary static weak-field exterior gravity.

A \(\kappa\)-leak would mean:

$$\kappa\neq0,$$

so:

$$AB=e^{2\kappa}\neq1.$$

That could alter light deflection, Shapiro delay, or PPN \(\gamma\)-like behavior.

Therefore ordinary solar-system constraints likely require that any static exterior \(\kappa\)-leak be extremely small.

### Development Status

This is the strongest current regime assignment.

The reduced forge work supports it, but a full covariant derivation is still missing.

---

## Domain 2: Cosmological Expansion

### Candidate Regime

```text
creation / traceful growth
```

### Motivation

If vacuum is energy-substance and local vacuum density remains constant, then cosmic expansion raises an immediate question.

If space expands while vacuum density remains constant, then total vacuum amount may increase.

That suggests possible vacuum creation, boundary growth, or global traceful expansion.

This would not be the same as static exterior exchange.

### Possible Reduced Description

In reduced language, expansion may involve a trace/conformal sector rather than pure compensated shear.

A rough symbolic association is:

$$J_\kappa>0$$

or a cosmological analogue of a positive traceful source.

This would correspond to increasing vacuum amount or expanding spatial volume.

### What This Must Reproduce

Any cosmological version of the theory must reproduce or explain:

```text
observed cosmic expansion
Hubble law
cosmological redshift
large-scale homogeneity and isotropy
CMB constraints
structure formation constraints
observed acceleration / dark-energy-like behavior
```

The current reduced static exterior theory does not yet do this.

### Possible Contradictions

This regime assignment would fail if traceful vacuum creation cannot reproduce the observed expansion history, or if it predicts unacceptable variation in local vacuum density, local gravitational behavior, or conservation laws.

It would also fail if the theory predicts a local expansion/creation effect in bound systems where observations show none.

### Development Status

Speculative.

The regime classification keeps the door open to creation, but no cosmological field equation has been developed.

---

## Domain 3: Gravitational Waves

### Candidate Regime

```text
exchange-like propagation / trace-free shear dynamics
```

### Motivation

In GR, gravitational waves are transverse, propagating metric disturbances with trace-free character in appropriate gauges.

Within the current reduced ontology, this suggests that gravitational waves may belong to a dynamic shear/exchange-like regime rather than a creation regime.

A tentative mapping is:

```text
gravitational waves = propagating compensated shear of vacuum configuration
```

### Possible Reduced Description

The static exterior mode \(s\) is not enough to describe gravitational waves.

A future dynamic generalization would need tensorial shear modes, not just one radial shear mode.

The analogue might be:

```text
trace-free vacuum configuration waves
```

with no net vacuum amount creation.

### What This Must Reproduce

The theory must reproduce:

```text
wave speed c
transverse polarizations or whatever modified polarizations are predicted
binary inspiral energy loss
observed gravitational waveforms
agreement with LIGO/Virgo/KAGRA constraints
constraints on extra polarizations
constraints on graviton mass or dispersion
```

### Possible Contradictions

This regime would be challenged if the theory predicts extra scalar/traceful wave modes that are already ruled out, or if it predicts wave speeds or dispersion inconsistent with observation.

If creation/destruction modes can propagate as traceful waves, those must be constrained.

### Development Status

Not developed.

This is an obvious future target once the static reduced theory is better organized.

---

## Domain 4: Black Holes, Collapse, and Strong Fields

### Candidate Regimes

```text
exchange / relaxation exterior
mixed regime near horizon
possible destruction, compression, or boundary regime in interior
```

### Motivation

Static exterior black-hole geometry may be close to the exchange/relaxation exterior regime.

However, collapse, horizons, and interiors may involve regimes not captured by the weak-field static exterior toy.

Possible candidates include:

```text
strong relaxation
traceful compression
vacuum destruction or deficit
boundary-layer behavior
mixed shear + kappa dynamics
```

### What This Must Reproduce

The theory must eventually address:

```text
Schwarzschild exterior
horizon behavior
black-hole thermodynamics
orbital dynamics near compact objects
gravitational wave ringdown
black-hole shadow observations
binary merger observations
singularity or interior behavior
```

### Possible Contradictions

The theory would be challenged if its strong-field exterior deviates from observations of black-hole or neutron-star systems beyond allowed limits.

If \(\kappa\)-suppression fails outside compact objects in a way that changes photon spheres, orbital precession, or ringdown spectra, observations may constrain or rule out the model.

### Development Status

Not developed.

Strong fields are beyond the current reduced weak-field program.

---

## Domain 5: Matter Formation and Boundaries

### Candidate Regimes

```text
creation/destruction + relaxation/fill-in
```

### Motivation

If mass is a constraint on vacuum configuration, then matter formation or matter-vacuum interaction may involve boundary behavior.

A mass may not simply “exchange” with vacuum. It may impose a constraint, deficit, burden, or interface condition.

The exterior field may then be the relaxation/fill-in response of the surrounding vacuum.

### Possible Reduced Description

A possible sequence is:

```text
matter imposes boundary/interface constraint
local imbalance or burden appears
vacuum relaxes
static exterior settles into kappa=0 with shear s
```

In this picture, the source interior or interface may involve traceful behavior, while the source-free exterior is compensated.

### What This Must Reproduce

The theory must eventually explain:

```text
why mass sources shear s
why exterior kappa is suppressed
why the source coefficient is GM
why inertial mass equals gravitational source strength
how local matter-vacuum interaction conserves or redistributes energy
```

### Possible Contradictions

If the theory predicts composition-dependent gravitational coupling, violations of equivalence principle constraints may rule it out.

If different matter types source different shear coefficients in ordinary conditions, the theory must explain why this is not observed.

### Development Status

Conceptual only.

Mass-as-constraint is not yet formalized.

---

## Domain 6: Laboratory and Solar-System Deviation Tests

### Candidate Regime

```text
small mixed regime / kappa-leak constraints
```

### Motivation

A major possible prediction channel is imperfect \(\kappa\)-suppression.

If a mostly exchange-like gravitational field has a small traceful leakage:

$$\kappa=\varepsilon_\kappa(r),$$

then:

$$AB=e^{2\varepsilon_\kappa(r)}.$$

This could produce deviations from GR-like weak-field predictions.

### Possible Observables

Potential observable channels include:

```text
PPN gamma deviations
light deflection anomalies
Shapiro delay deviations
perihelion precession deviations
clock redshift anomalies
fifth-force-like effects
environment-dependent gravitational response
composition-dependent coupling if source interface differs by matter type
```

### Possible Contradictions

Solar-system constraints are very strong. Any ordinary weak-field \(\kappa\)-leak must likely be extremely small.

This makes \(\kappa\)-leak a useful future prediction channel but also a dangerous one.

### Development Status

Not yet tested.

A possible script:

```text
candidate_kappa_leak_deviation.py
```

should compute the weak-field consequences of:

$$\kappa(r)\neq0$$

with:

$$s(r)\approx-\frac{2GM}{rc^2}.$$

---

## Domain 7: Spacetime Engineering

### Candidate Regimes

```text
controlled exchange
controlled relaxation
possibly controlled creation/destruction
```

### Motivation

If the theory eventually identifies real controllable vacuum modes, then spacetime engineering would depend on which regime can be manipulated.

The speculative mapping is:

```text
exchange control:
  shape compensated shear without changing vacuum amount

relaxation control:
  set boundary conditions or influence fill-in response

creation/destruction control:
  change local vacuum amount or traceful mode content
```

### What Would Need to Be True

For this to be physical rather than metaphorical, the theory would need:

```text
a real covariant field equation
identified controllable source terms
energy bookkeeping
stability analysis
observational consistency
laboratory-accessible coupling mechanisms
```

### Possible Contradictions

If all controllable matter-vacuum interactions are far too weak, or if vacuum modes cannot be independently manipulated, the engineering angle may remain only philosophical.

If creation/destruction requires cosmological-scale boundary conditions, laboratory engineering may be impossible.

### Development Status

Speculative.

Useful as a long-term motivation, not as a current formal claim.

---

## Observational Triage

The most important domains to address first are:

### 1. Static Weak-Field Gravity

This is the entry requirement.

The theory must reproduce GR-like weak-field behavior.

The reduced exterior program currently supports this at toy level.

### 2. Gauge and Covariance

The reduced variables must be embedded into a gauge-aware or covariant formulation.

Without this, observational predictions remain gauge-fragile.

### 3. Solar-System Deviations

Any \(\kappa\)-leak or traceful exterior deviation must be constrained.

This is likely the first route to falsifiability.

### 4. Cosmology

Vacuum creation may be relevant here, but the theory is not ready for a full cosmology until the regime distinction is formalized.

### 5. Gravitational Waves and Strong Fields

These are essential eventually, but they require a dynamic tensorial version of the theory.

---

## Candidate Falsification / Pressure Points

The following would pressure or falsify parts of the candidate map.

### Pressure Point 1: Static Exterior Kappa Leak

If the theory generically predicts:

$$\kappa\neq0$$

in ordinary static exteriors, then it may conflict with weak-field tests unless the leak is tightly suppressed.

### Pressure Point 2: Wrong Shear Coefficient

If the theory cannot derive:

$$s(r)=-\frac{2GM}{rc^2},$$

or the equivalent weak-field coefficient, then it fails the entry test.

### Pressure Point 3: Non-Covariant Dependence

If predictions depend on arbitrary radial coordinate choices rather than gauge-fixed or invariant quantities, the theory is not physically well-posed.

### Pressure Point 4: Cosmological Creation Without Observational Fit

If vacuum creation is used to explain expansion, it must reproduce the observed expansion history and structure constraints.

### Pressure Point 5: Unwanted Extra Modes

If traceful creation/destruction modes propagate in contexts where observations rule them out, the theory must suppress or eliminate them.

### Pressure Point 6: Equivalence Principle Violations

If matter-vacuum coupling depends on composition in ordinary regimes, the theory faces strong constraints.

---

## What This Map Suggests

The regime map suggests that the theory should not try to force one vacuum process to explain every domain.

Instead:

```text
static exterior gravity:
  exchange / relaxation endpoint

cosmological expansion:
  possible creation / traceful growth

gravitational waves:
  dynamic shear propagation

black holes / collapse:
  strong relaxation, boundary, or mixed regimes

engineering:
  only possible if one or more regimes can be controlled
```

This is more flexible than assuming all vacuum dynamics are conservative exchange.

It also creates more ways for the theory to be wrong, which is good.

---

## Recommended Next Work

### Next Script: Kappa-Leak Deviations

```text
candidate_kappa_leak_deviation.py
```

Purpose:

```text
Compute weak-field consequences of a small nonzero kappa mode.
```

Test:

$$\kappa(r)=\varepsilon_\kappa(r),$$

with:

$$s(r)=-\frac{2GM}{rc^2}.$$

Then:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Compare the weak-field coefficients to GR-like expectations.

This would identify the first quantitative deviation channel.

### Next Conceptual Note: Cosmological Vacuum Creation

```text
candidate_cosmic_vacuum_creation.md
```

Purpose:

```text
Explore whether expansion should be modeled as traceful vacuum creation,
and what conservation/bookkeeping constraints would be required.
```

This should come after the static weak-field deviation map is clearer.

### Next Foundation Note: Regime Principle

```text
candidate_exchange_creation_principle.md
```

Purpose:

```text
Decide whether exchange/creation separation should remain a candidate
classification or become a formal postulate candidate.
```

This should wait until more observational mapping is done.

---

## Current Best Roadmap

A sensible order is:

```text
1. Finish reduced static exterior program.
2. Quantify kappa-leak deviations.
3. Map deviations to weak-field observational constraints.
4. Only then move to cosmology / creation.
5. Later develop dynamic shear / gravitational waves.
6. Later develop strong fields and black holes.
```

This keeps the theory anchored to the best-tested regime first.

---

## Summary

The current candidate regime map is:

```text
Exchange:
  conservative redistribution,
  trace-kernel,
  static exterior shear,
  GR-like weak-field recovery.

Relaxation / fill-in:
  imbalance suppression,
  kappa -> 0,
  static exterior equilibrium.

Creation / destruction:
  traceful vacuum amount change,
  possible cosmology or boundary regime,
  may source kappa.

Mixed regimes:
  shear plus traceful leakage,
  possible deviation channel.
```

The most important next quantitative question is:

```text
If kappa is small but nonzero, what observable deviations appear?
```

That question should be tested before the theory moves too far into cosmology or engineering speculation.
