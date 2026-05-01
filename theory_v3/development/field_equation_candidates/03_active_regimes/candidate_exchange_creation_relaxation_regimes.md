# Candidate Exchange / Creation / Relaxation Regimes

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or field equation. It does not add a formal commitment to the theory.

Its purpose is to classify three possible vacuum-dynamical regimes that have emerged from recent development work:

```text
exchange
creation / destruction
relaxation / fill-in
```

This note is motivated by the negative result of the P3 volume-preservation study and by the reduced exterior mode program.

The P3 study showed that constant local vacuum density does not, by itself, prove that local vacuum exchange conserves energy. Instead, P1 and P3 identify vacuum volume with vacuum energy:

$$E_{\rm vac}=\rho_v V_{\rm vac}.$$

So if a process conserves local vacuum energy, it conserves vacuum volume. But P1-P3 do not by themselves say that every local vacuum process must be conservative.

That leaves open the possibility that there are multiple regimes:

```text
exchange:
  local redistribution of vacuum substance / energy

creation / destruction:
  local or boundary change in total vacuum amount

relaxation / fill-in:
  surrounding vacuum responds to deficits, excesses, or imbalance
```

This note organizes those possibilities without prematurely deciding which are fundamental.

---

## Motivation

The reduced exterior mode program found a clean static exterior structure.

In areal gauge:

$$\kappa=\frac{\ln A+\ln B}{2},$$

and:

$$s=\frac{\ln A-\ln B}{2}.$$

Then:

$$AB=e^{2\kappa}.$$

So:

$$\kappa=0 \quad \Longleftrightarrow \quad AB=1.$$

The source-free exterior gravity toy suggests:

```text
static exterior gravity lives in compensated shear s,
while the source-free exterior suppresses imbalance kappa.
```

In compact form:

$$\kappa=0,\qquad s\neq0.$$

The reduced action toy expressed this as:

$$L =
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s.$$

In that toy:

- \(\kappa\) is suppressed in the source-free exterior.
- \(s\) is sourced by mass.
- reciprocal scaling holds.
- the weak-field exterior profile can be recovered.

But the P3 volume-preservation study revealed that the theory should not simply assume all vacuum processes are conservative exchange. Cosmological expansion, boundary growth, or other non-static processes may involve actual vacuum creation or destruction.

Therefore the theory needs a regime classification.

---

## Regime 1: Exchange

### Informal Definition

Exchange is local redistribution of vacuum substance / energy.

It is conservative in the local bookkeeping sense:

```text
vacuum amount is moved, transferred, or reconfigured,
but not locally created or destroyed.
```

Under P1 and P3:

$$E_{\rm vac}=\rho_v V_{\rm vac}.$$

If exchange conserves local vacuum energy:

$$\delta E_{\rm vac}=0,$$

then because \(\rho_v\) is constant:

$$\rho_v\delta V_{\rm vac}=0,$$

so:

$$\delta V_{\rm vac}=0.$$

Thus local-energy-conserving exchange is volume-preserving.

### Expected Mode Behavior

Exchange is expected to preserve the local trace/volume content of vacuum configuration.

In reduced mode language, this suggests:

$$J_\kappa=0.$$

Then the exterior equilibrium can give:

$$\kappa=0.$$

The active gravitational distortion is then carried by:

$$s.$$

So the exchange regime is naturally associated with:

```text
trace-kernel behavior
volume preservation
kappa suppression
compensated shear
static exterior gravity
```

### Candidate Role in the Theory

Exchange may be the dominant regime for static gravitational exteriors.

In this regime, mass does not create exterior vacuum substance. Instead, it imposes or sources compensated shear in the surrounding vacuum configuration.

The reduced exterior picture is:

$$\kappa=0,$$

and:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

Outside the source:

$$\nabla^2s=0.$$

For spherical mass:

$$s(r)=-\frac{2GM}{rc^2}.$$

Then:

$$A=e^s,$$

$$B=e^{-s},$$

and:

$$AB=1.$$

This is the static exterior exchange-like regime.

---

## Regime 2: Creation / Destruction

### Informal Definition

Creation / destruction is a local or boundary change in total vacuum amount.

It is not conservative in the same bookkeeping sense as exchange.

Creation means:

$$\delta E_{\rm vac}>0,$$

or equivalently, under P3:

$$\delta V_{\rm vac}>0.$$

Destruction means:

$$\delta E_{\rm vac}<0,$$

or:

$$\delta V_{\rm vac}<0.$$

This is not merely redistributing vacuum substance. It changes the local or global vacuum amount.

### Why This Cannot Be Ruled Out Prematurely

The framework already allows or suggests vacuum creation in at least one context: cosmic expansion.

If the universe expands and vacuum is substance-like energy, then either:

1. vacuum amount increases with expansion,
2. vacuum is redistributed from elsewhere,
3. vacuum density changes,
4. or the ontology must explain expansion in another way.

Since P3 says local vacuum density is constant, expansion naturally suggests that vacuum amount can increase, at least globally or at boundaries.

Therefore creation cannot simply be banned.

It must be classified.

### Expected Mode Behavior

Creation / destruction is expected to be traceful.

In reduced mode language, it may source:

$$\kappa.$$

If:

$$J_\kappa\neq0,$$

then a simple reduced equilibrium gives:

$$\kappa=\frac{J_\kappa}{2M_\kappa^2}.$$

Then:

$$AB=e^{2\kappa}.$$

So creation/destruction may break reciprocal scaling.

This is not necessarily a failure if the regime is not supposed to be a static source-free exterior.

It may instead describe:

```text
cosmic expansion
vacuum growth
boundary creation
non-equilibrium vacuum production
traceful relaxation events
```

### Candidate Role in the Theory

Creation / destruction may be relevant for:

- cosmological expansion,
- horizon or boundary effects,
- vacuum formation,
- topology or phase transitions,
- non-static energy injection,
- possible engineering regimes,
- early-universe behavior,
- singularity avoidance or black-hole interiors,
- places where the static exterior assumptions fail.

The key point is:

```text
creation/destruction should not be forced into the exchange category.
```

It may be a different regime with different mode behavior.

---

## Regime 3: Relaxation / Fill-In

### Informal Definition

Relaxation / fill-in is the response of surrounding vacuum to a deficit, excess, or imbalance.

It is not necessarily the original local event. It is the subsequent adjustment.

For example:

```text
a local process creates a vacuum deficit,
surrounding vacuum flows or reconfigures,
the region fills back in,
the configuration smooths toward a lower-energy state.
```

Or:

```text
a boundary creates new vacuum,
neighboring vacuum redistributes burden,
the configuration relaxes toward equilibrium.
```

Relaxation may include exchange-like behavior even if the triggering event involved creation or destruction.

### Expected Mode Behavior

Relaxation may include both sectors:

```text
kappa relaxation:
  suppression or smoothing of trace/imbalance

s propagation:
  compensated shear redistribution
```

In the reduced action toy, relaxation of \(\kappa\) was represented by terms like:

$$K_\kappa|\nabla\kappa|^2+M_\kappa^2\kappa^2.$$

The equation:

$$-2K_\kappa\nabla^2\kappa+2M_\kappa^2\kappa=0$$

has the relaxed source-free solution:

$$\kappa=0$$

under suitable boundary conditions.

Shear propagation was represented by:

$$K_s|\nabla s|^2+\alpha\rho s.$$

This gives:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

So relaxation may be the process by which:

```text
traceful disturbances are damped or balanced,
while compensated shear remains as the stable exterior field.
```

### Candidate Role in the Theory

Relaxation / fill-in may connect exchange and creation/destruction.

It may explain why static exteriors recover the exchange-like compensated regime even if source formation involved traceful events.

A possible story is:

```text
matter formation, boundary effects, or cosmological processes may create local imbalance;
surrounding vacuum relaxes;
the static exterior settles into kappa=0 with shear s carrying the field.
```

This would allow local creation/destruction in some regimes without ruining static exterior gravity.

---

## Proposed Regime Table

| Regime | Local energy change? | Vacuum volume change? | Expected reduced mode | Possible context |
|---|---:|---:|---|---|
| Exchange | No net local change | No net local change | \(J_\kappa=0,\ s\neq0\) | static exterior gravity |
| Creation | Positive net change | Positive net change | \(J_\kappa\neq0\) possible | expansion, boundary growth |
| Destruction | Negative net change | Negative net change | \(J_\kappa\neq0\) possible | collapse, deficits, sinks |
| Relaxation / fill-in | response-dependent | response-dependent | \(\kappa\to0,\ s\) propagates | equilibration after disturbance |

This table is provisional.

It should guide future tests rather than act as a formal classification.

---

## Relationship to P1 and P3

P1 says vacuum is energy.

P3 says local vacuum energy density is finite and constant.

Together:

$$E_{\rm vac}=\rho_v V_{\rm vac}.$$

This means vacuum energy and vacuum volume are not independent.

But this does not decide whether a local process is conservative.

For exchange:

$$\delta E_{\rm vac}=0
\quad\Longleftrightarrow\quad
\delta V_{\rm vac}=0.$$

For creation/destruction:

$$\delta E_{\rm vac}\neq0
\quad\Longleftrightarrow\quad
\delta V_{\rm vac}\neq0.$$

So P1 and P3 give the conversion between energy and volume. They do not alone classify the process.

The missing theory content is the regime rule:

```text
when is a local vacuum process exchange,
when is it creation/destruction,
and how does relaxation respond?
```

---

## Relationship to P5

P5 says the vacuum seeks minimum energy.

This may eventually constrain relaxation.

A strengthened interpretation might say:

```text
In static equilibrium, the vacuum relaxes away local trace/imbalance modes
unless maintained by a source or boundary condition.
```

That would support exterior \(\kappa\)-suppression.

But P5 as currently understood may not be enough to forbid creation/destruction in all regimes.

A safer interpretation is:

```text
P5 governs relaxation behavior,
not necessarily the existence or nonexistence of creation events.
```

This lets P5 explain why static exteriors settle into balanced configurations without ruling out cosmological vacuum creation.

---

## Relationship to P6

P6 concerns vacuum exchange in gradients.

This note suggests that P6 may need sharper language.

Possible distinction:

```text
P6-exchange:
  conservative redistribution in a gradient;
  likely relevant to static gravity and falling bodies.

P6-creation/destruction:
  traceful vacuum amount change;
  possibly relevant to expansion or boundary dynamics.

P6-relaxation:
  response of surrounding vacuum to imbalance.
```

This may eventually require either:

1. revising P6,
2. adding a new Exchange-Creation Separation principle,
3. or deriving the distinction from a deeper variational structure.

---

## Relationship to the Reduced Exterior Program

The reduced exterior program can be interpreted as studying the static exchange/relaxation endpoint.

In that endpoint:

$$\kappa=0,$$

and:

$$s\neq0.$$

Mass sources shear:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

But the source-free exterior suppresses trace imbalance:

$$\kappa=0.$$

This does not require all vacuum dynamics everywhere to be exchange-like.

It only requires that static source-free exterior equilibrium lands in the compensated regime.

That is an important distinction.

---

## Relationship to Cosmological Expansion

Cosmological expansion may require vacuum creation, boundary creation, or global vacuum amount growth.

If so, then expansion belongs to a different regime than static exterior gravity.

Possible cosmological interpretation:

```text
expansion is traceful vacuum growth,
not compensated exterior shear.
```

In reduced language, expansion may involve a \(\kappa\)-like or conformal sector rather than pure shear.

This could eventually connect:

```text
static gravity -> shear / exchange regime
cosmic expansion -> trace / creation regime
```

This is speculative, but it is consistent with the current classification.

---

## Relationship to Spacetime Engineering

If these regimes are real, then possible spacetime engineering would depend on which regimes can be controlled.

Exchange control would mean controlling redistribution:

```text
shape shear,
redirect compensated modes,
alter local gravitational configuration.
```

Creation/destruction control would be much more dramatic:

```text
change local vacuum amount,
source traceful modes,
possibly affect expansion-like behavior.
```

Relaxation control would mean influencing how vacuum fills in or rebalances:

```text
set boundary conditions,
shape recovery pathways,
control whether imbalance becomes shear or traceful growth.
```

This is far beyond the current formal theory.

But the classification helps state what would have to be controlled.

---

## Current Best Interpretation

The current best interpretation is:

```text
Static exterior gravity is probably an exchange/relaxation endpoint:
  kappa is suppressed,
  shear remains.

Cosmic expansion may involve creation:
  vacuum amount changes,
  trace/conformal modes may be active.

Relaxation/fill-in connects them:
  disturbances or creation events may settle into compensated configurations.
```

This avoids overconstraining the ontology.

It lets the theory recover GR-like exterior behavior without prematurely forbidding vacuum creation in other regimes.

---

## What This Note Establishes

This note establishes a candidate classification:

1. Exchange is conservative local redistribution.
2. Creation/destruction is local or boundary change in total vacuum amount.
3. Relaxation/fill-in is the vacuum response to imbalance.
4. P1 and P3 relate vacuum energy and volume but do not classify the process.
5. Static exterior gravity likely belongs to the exchange/relaxation endpoint.
6. Cosmological expansion may belong to the creation regime.
7. The theory should not forbid creation/destruction merely to make static gravity easier.
8. The next formal task is to define these regimes mathematically.

---

## What This Note Does Not Establish

This note does not prove that vacuum creation occurs.

It does not prove that cosmological expansion is vacuum creation.

It does not prove that static gravity is purely exchange.

It does not derive the exchange/creation distinction from existing postulates.

It does not specify a field equation for creation/destruction.

It does not quantify relaxation/fill-in.

It does not connect the regimes to observations.

It only defines a candidate conceptual classification.

---

## Next Development Targets

Possible next artifacts:

```text
candidate_exchange_creation_distinction_test.py
```

Purpose:

```text
Test formal operator definitions of exchange, creation/destruction, and relaxation.
```

Possible categories:

```text
exchange operator:
  delta E_local = 0
  delta V_local = 0
  trace-kernel expected

creation operator:
  delta E_local > 0
  delta V_local > 0
  traceful mode allowed

destruction operator:
  delta E_local < 0
  delta V_local < 0
  traceful mode allowed

relaxation operator:
  decreases configuration energy
  may drive kappa -> 0
```

Another possible artifact:

```text
candidate_regime_map_observations.md
```

Purpose:

```text
Map each regime to observational domains:
static gravity, cosmology, waves, collapse, laboratory constraints.
```

Another possible artifact:

```text
candidate_cosmic_vacuum_creation.md
```

Purpose:

```text
Explore whether cosmological expansion can be represented as traceful vacuum creation.
```

---

## Summary

The theory should not prematurely collapse all vacuum dynamics into conservative exchange.

A better classification is:

```text
exchange:
  conservative redistribution

creation / destruction:
  net change in vacuum amount

relaxation / fill-in:
  response that smooths, balances, or redistributes after imbalance
```

P1 and P3 identify vacuum energy with vacuum volume:

$$E_{\rm vac}=\rho_v V_{\rm vac}.$$

They do not, by themselves, say which processes conserve \(E_{\rm vac}\) and which change it.

This means local creation/destruction may be possible in some regimes, especially if the theory needs to describe cosmological expansion or boundary growth.

Static exterior gravity can still be an exchange/relaxation endpoint where:

$$\kappa=0,$$

and:

$$s\neq0.$$

The next task is to formalize the regime distinction and test it against observations.
