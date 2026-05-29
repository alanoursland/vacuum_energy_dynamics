# Boundary Flux Field Bridge 56: Green-Matrix Reduced Action

## Purpose

This report packages the reduced-action sign in a finite two-source Green
matrix model.

## Validated Checks

- two-source reduced Green action: passed
- negative reduced cross term: passed
- Green matrix inverse-square attractive derivative: passed
- stationary equation component 1: passed
- stationary equation component 2: passed

## Reduced Action

Let:

```text
J = [Q1,Q2]^T
Gmat = [[S1,G],[G,S2]]
```

where `S1` and `S2` are self terms and `G` is the cross Green term.

The stationary source-coupled reduced action is:

```text
E_red = -1/2 J^T Gmat J.
```

SymPy verifies:

```text
E_red
  =
  -1/2(S1 Q1^2 + 2G Q1Q2 + S2 Q2^2).
```

Therefore the cross term is:

```text
E_cross = -G Q1Q2.
```

## Separation Dependence

If:

```text
G(d)=K/d,
```

then:

```text
E_cross(d) = -K Q1Q2/d
```

and:

```text
F_d = -dE/dd = -K Q1Q2/d^2.
```

For positive same-sign sources, this is attractive.

## Interpretation

The attractive sign is not a property of the positive strain matrix alone. It
comes from eliminating the field in the source-coupled action.
