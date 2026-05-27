# Vacuum Interval Directional Probe Origin 11: Boundary Source Full-Tensor Coupling

## Purpose

This proof checks the action/source side of the directional selector.

If boundary data includes shear/traceless components, a trace-only source
coupling cannot use that information. A full tensor coupling can.

## Validated Checks

- full tensor coupling sees diagonal shear: passed
- trace-only coupling is blind to diagonal shear: passed
- full tensor coupling sees off-diagonal shear: passed
- trace-only coupling is blind to off-diagonal shear: passed

## Diagonal Shear Test

Let:

```text
delta h = [[eps,0],[0,-eps]]
T = [[s,0],[0,-s]]
```

The full contraction gives:

```text
T^ab delta h_ab = 2*eps*s
```

The trace-only coupling gives:

```text
tau tr(delta h) = 0
```

## Off-Diagonal Shear Test

Let:

```text
delta h = [[0,eta],[eta,0]]
T = [[0,off],[off,0]]
```

The full contraction gives:

```text
T^ab delta h_ab = 2*eta*off
```

The trace-only coupling gives:

```text
tau tr(delta h) = 0
```

## Interpretation

Directional interval probes supply tensor data only if the boundary/source
action has a place to use tensor data. A scalar trace coupling is insufficient;
the relevant coupling must be of the form:

```text
T^ab delta h_ab
```

or an equivalent full-tensor boundary pairing.
