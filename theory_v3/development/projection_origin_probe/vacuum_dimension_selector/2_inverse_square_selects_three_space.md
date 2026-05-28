# Vacuum Dimension Selector 2: Inverse-Square Selects Three Space

## Purpose

This proof solves the dimension selected by exact inverse-square radial field
strength under the conserved-flux gate.

## Validated Checks

- conserved-flux exponent is `1-n`: passed
- inverse-square exponent is `-2`: passed
- solving `1-n=-2` gives `n=3`: passed
- adding one time channel gives `D=4`: passed

## Computation

From proof `1`:

```text
F(r) ~ r^(1-n).
```

Exact inverse-square behavior requires:

```text
1 - n = -2.
```

Sympy solves:

```text
n = 3.
```

With one time channel:

```text
D = n + 1 = 4.
```

## Interpretation

This is a conditional selector. It selects three spatial dimensions if exact
long-range inverse-square flux is treated as a fundamental physical target.
