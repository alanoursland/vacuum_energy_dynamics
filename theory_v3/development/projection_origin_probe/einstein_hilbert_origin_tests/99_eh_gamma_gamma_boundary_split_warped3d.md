# Einstein-Hilbert Origin Test 99: EH/Gamma-Gamma Boundary Split

## Purpose

This report validates the Einstein-Hilbert split into a quadratic connection
density plus a boundary divergence on a controlled nonlinear metric:

```text
g = diag(A(x), B(x), C(x)).
```

## Validated Checks

- EH density equals Gamma-Gamma density plus boundary divergence: passed
- nonzero Gamma-Gamma density: passed
- boundary vector only has x component for this ansatz: passed

## Identity Tested

SymPy verifies:

```text
sqrt(g) R
  =
  sqrt(g) g^ab(
    Gamma^c_ad Gamma^d_bc
    - Gamma^c_ab Gamma^d_cd
  )
  + partial_c V^c,
```

where:

```text
V^c =
  sqrt(g)(
    g^ab Gamma^c_ab
    - g^cb Gamma^a_ab
  ).
```

For the tested metric, the Gamma-Gamma density is nonzero:

```text
sqrt(g) B'(x) C'(x) / [2 A(x) B(x) C(x)].
```

## Interpretation

This is the first nonlinear action-origin bridge:

```text
Einstein-Hilbert curvature action
  =
  quadratic connection-strain action
  + boundary bookkeeping.
```

It supports treating the connection as the nonlinear geometric strain object,
while keeping boundary terms explicit.
