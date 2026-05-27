# Vacuum Action Origin 22: Connection Trace as Volume Boundary Flux

## Purpose

This report validates the boundary-flux meaning of the contracted connection.

The gate is:

```text
connection trace
  =
  logarithmic derivative of metric volume density.
```

## Validated Checks

- contracted connection is volume log derivative: passed
- volume identity all components: passed
- boundary vector x component is connection-volume flux: passed
- boundary vector transverse components vanish for warped ansatz: passed
- conformal contracted connection volume identity: passed

## Volume Identity

For:

```text
g = diag(A(x), B(x), C(x)),
sqrt(g) = sqrt(A B C),
```

SymPy verifies:

```text
Gamma^a_ac = partial_c log sqrt(g).
```

Equivalently:

```text
Gamma^a_ac = partial_c sqrt(g) / sqrt(g).
```

## Boundary Vector

The EH boundary vector has the form:

```text
V^c = sqrt(g)(g^ab Gamma^c_ab - g^cb Gamma^a_ab).
```

SymPy verifies that for the warped ansatz the only nonzero component is the
`x`-flux component, built from connection coefficients and the volume density.

## Conformal Check

For a conformal volume density:

```text
sqrt(g) = exp(D s),
```

SymPy verifies:

```text
partial_x log sqrt(g) = D s'.
```

## Interpretation

The boundary term in the metric action is a volume/connection flux. This is the
metric version of the scalar boundary-flux pattern: the boundary records how
the local comparison structure changes the volume measure.
