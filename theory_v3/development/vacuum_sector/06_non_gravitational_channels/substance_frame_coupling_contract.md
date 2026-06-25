# Substance-Frame Coupling Contract

## Claim

A vacuum substance frame is not by itself a prediction of preferred-frame
forces, clock anisotropy, calibration drift, or Lorentz-violating signals. A
detectable channel requires an explicit coupling operator.

## Scope

This contract covers non-gravitational channels that use a vacuum-frame
variable, such as a unit timelike direction:

```text
u^a
```

The contract does not license insertion of `u^a` into the closed gravitational
field equations. That route belongs to the residual-gate ledger.

## Silent Frame Rule

With no coupling:

```text
beta_frame = 0
Delta O_frame = 0
```

The frame can remain part of the ontology without producing preferred-frame
observables.

## Coupled Channel Schema

A simple calibration-anisotropy placeholder is:

```text
Delta O_frame = beta_frame * cos(theta)^2
```

where `theta` is the apparatus orientation relative to the frame. The symbolic
sensitivity is:

```text
d(Delta O_frame)/d theta = -2 * beta_frame * sin(theta) * cos(theta)
```

This is a schema only. It does not derive `beta_frame`, the apparatus coupling
operator, or any source/exchange ledger.

## Metric Quarantine

Use the split:

```text
Delta_metric = epsilon_g * Delta O_frame
```

For a non-gravitational channel:

```text
epsilon_g = 0
```

unless the claim is explicitly returned to the residual-gate ledger.

## Required Bounds Route

Any nonzero frame-sensitive coupling must be checked against:

```text
preferred-frame bounds
anisotropy bounds
Lorentz-violation bounds
clock or matter-calibration bounds
source/exchange bookkeeping
```

No frame coupling is live before that sieve.

## Current Classification

The VacuumForge contract records:

```text
derivation: substance_frame_coupling_contract_023
obligation satisfied: substance_frame_coupling_contract_required_022
new obligation: substance_frame_bounds_sieve_required_023
```

Current conclusion:

```text
No substance-frame coupling route is live.
```

The ontology may contain a frame without predicting a preferred-frame signal.
Observable channels require a coupling operator, source ledger, metric
quarantine, and bounds sieve.
