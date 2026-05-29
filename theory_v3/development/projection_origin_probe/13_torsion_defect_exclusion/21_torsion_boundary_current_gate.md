# Torsion Defect Exclusion 21: Torsion Boundary Current Gate

## Purpose

This proof checks the boundary/current side of a torsion branch.

If torsion has a current or boundary coupling, that coupling requires explicit
boundary conditions or source routing.

## Validated Checks

- torsion boundary term varies to boundary currents: passed
- free torsion-boundary variation requires zero boundary currents: passed
- integrated torsion-current balance requires source or equal boundary current: passed

## Boundary Term

Use:

```text
B_T = C_R tau_R - C_L tau_L.
```

Then:

```text
dB_T/dtau_R = C_R
dB_T/dtau_L = -C_L.
```

Free boundary stationarity gives:

```text
C_R = 0
C_L = 0.
```

## Integrated Balance

For an integrated torsion-current equation:

```text
C_R - C_L = S_int.
```

Sympy records:

```text
S_int = C_R - C_L.
```

In a source-free branch:

```text
C_R = C_L.
```

## Interpretation

Torsion boundary/current data is not automatically covered by the metric
boundary data. If a torsion current exists, it needs boundary conditions,
source terms, or an explicit silence condition.
