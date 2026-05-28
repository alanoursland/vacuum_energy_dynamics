# Torsion Defect Exclusion 26: Torsion-Free Energy Minimum

## Purpose

This proof validates the reduced minimum once the no-source condition holds.

## Validated Checks

- no-source torsion energy is `12 mu tau^2`: passed
- stationary point is `tau = 0`: passed
- second variation is `24 mu`: passed
- energy difference from `tau = 0` is nonnegative when `mu > 0`: passed

## Computation

With:

```text
J_total = 0
```

the reduced torsion energy is:

```text
E_T = 12*mu*tau**2.
```

The variation is:

```text
dE_T/dtau = 24*mu*tau.
```

The second variation is:

```text
d^2E_T/dtau^2 = 24*mu.
```

For `mu > 0`, this is positive.

The energy difference from the torsion-free point is:

```text
E_T(tau)-E_T(0) = 12*mu*tau**2.
```

## Interpretation

With positive stiffness and no torsion source, the torsion-free branch is not
just stationary. It is the unique reduced minimum in this one-mode torsion
sector.
