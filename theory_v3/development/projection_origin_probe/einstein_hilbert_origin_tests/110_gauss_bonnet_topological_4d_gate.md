# Einstein-Hilbert Origin Test 110: Gauss-Bonnet Topological 4D Gate

## Purpose

This report validates the dimensional gate for the Gauss-Bonnet Lovelock term.

It does not prove the full Gauss-Bonnet theorem. It checks the algebraic facts
needed in this proof chain:

```text
D < 4: Gauss-Bonnet vanishes.
D = 4: Gauss-Bonnet density can be nonzero, but its local field variation is topological.
D > 4: Gauss-Bonnet contributes local dynamics.
```

## Validated Checks

- constant-curvature Gauss-Bonnet density: passed
- Gauss-Bonnet field coefficient vanishes in 4D: passed
- 4D Gauss-Bonnet density can be nonzero: passed
- Gauss-Bonnet becomes dynamical above 4D: passed
- Gauss-Bonnet antisymmetric slot exists in 4D: passed
- Gauss-Bonnet antisymmetric slot vanishes below 4D: passed

## Constant-Curvature Density

For constant curvature `K`:

```text
R_abcd R^abcd = 2D(D-1)K^2
R_ab R^ab     = D(D-1)^2 K^2
R             = D(D-1)K
```

SymPy verifies:

```text
R_abcd R^abcd - 4 R_ab R^ab + R^2
  = D(D-1)(D-2)(D-3)K^2.
```

In `D=4`, this density can be nonzero.

## Field-Equation Gate

The constant-curvature Gauss-Bonnet field coefficient contains:

```text
(D-4).
```

Therefore in four dimensions the term is topological: it can affect global or
boundary bookkeeping, but it does not add local second-order metric dynamics.

## Interpretation

In four dimensions, the Einstein-Hilbert term remains the only dynamical
Lovelock correction to the metric equations, aside from the cosmological term.
Gauss-Bonnet is allowed as topology/boundary structure, not as a new local
bulk field equation in this gate.
