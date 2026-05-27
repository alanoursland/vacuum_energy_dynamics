# Geometric Field Lift 78: Newtonian Potential Metric Identification

## Purpose

This report validates the standard weak-field metric identification:

```text
g_00 = -(1 + 2 phi).
```

It checks only the Newtonian/slow-particle limit. It does not derive the full
Einstein equations.

## Validated Checks

- Gamma^i_00 = partial_i phi: passed
- slow geodesic acceleration is -grad phi: passed
- attractive radial acceleration: passed
- radial potential is harmonic off source: passed
- scalar bridge sign relation: passed

## Christoffel Term

For a static weak field with spatial inverse metric approximated by
`delta^ij`:

```text
Gamma^i_00 = -1/2 partial_i g_00.
```

Since:

```text
g_00 = -(1+2phi),
```

SymPy verifies:

```text
Gamma^i_00 = partial_i phi.
```

## Slow Geodesic Acceleration

The slow-particle spatial acceleration is:

```text
a^i = -Gamma^i_00 = -partial_i phi.
```

Thus `phi` is the Newtonian potential under this convention.

## Radial Sign Convention

For attraction toward a positive source:

```text
phi(r) = -K/r.
```

Then:

```text
a_r = -dphi/dr = -K/r^2.
```

The positive scalar bridge variable `u=K/r` corresponds to:

```text
phi = -u
```

under this Newtonian acceleration convention.
