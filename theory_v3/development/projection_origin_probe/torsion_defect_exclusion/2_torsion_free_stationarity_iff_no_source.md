# Torsion Defect Exclusion 2: Torsion-Free Stationarity Iff No Source

## Purpose

This proof records the exact no-source condition for the torsion-free branch.

## Validated Checks

- torsion variation is `24 mu tau - J_total`: passed
- residual at `tau = 0` is `-J_total`: passed
- stationarity at `tau = 0` requires `J_total = 0`: passed
- stationary torsion is `J_total/(24 mu)`: passed

## Computation

Use:

```text
E_T = 12 mu tau^2 - J_total tau.
```

Then:

```text
dE_T/dtau = -J_total + 24*mu*tau.
```

At the torsion-free branch:

```text
(dE_T/dtau)|tau=0 = -J_total.
```

Thus:

```text
tau = 0 is stationary iff J_total = 0.
```

## Interpretation

Torsion-free geometry is not a default consequence of metric data. It is a
source selector. A hidden nonzero `J_total` makes the torsion-free branch
nonstationary.
