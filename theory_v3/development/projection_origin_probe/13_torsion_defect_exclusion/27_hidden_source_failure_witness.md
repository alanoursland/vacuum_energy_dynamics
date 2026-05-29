# Torsion Defect Exclusion 27: Hidden Source Failure Witness

## Purpose

This proof records the failure mode the folder is designed to block.

Any hidden nonzero torsion source makes the torsion-free branch nonstationary.

## Validated Checks

- hidden-source variation is `24 mu tau - J_hidden`: passed
- residual at `tau = 0` is `-J_hidden`: passed
- stationarity at `tau = 0` requires `J_hidden = 0`: passed
- actual stationary torsion is shifted by the hidden source: passed

## Computation

Use:

```text
E_T = 12 mu tau^2 - J_hidden tau.
```

Then:

```text
dE_T/dtau = -J_hidden + 24*mu*tau.
```

At:

```text
tau = 0,
```

the residual is:

```text
-J_hidden.
```

The stationary torsion is:

```text
tau = J_hidden/(24 mu).
```

## Interpretation

A hidden torsion source is incompatible with claiming the pure EH branch. It
must be shown absent, structurally canceled, or routed into a torsion-extended
field branch.
