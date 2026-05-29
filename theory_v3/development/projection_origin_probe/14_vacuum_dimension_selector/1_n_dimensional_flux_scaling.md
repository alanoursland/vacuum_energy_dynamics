# Vacuum Dimension Selector 1: N-Dimensional Flux Scaling

## Purpose

This proof restates the radial flux scaling gate inside the dimension selector
folder.

## Validated Checks

- conserved radial flux equals `Q`: passed
- field strength scales as `r^(1-n)`: passed
- in three spatial dimensions the field is inverse-square: passed

## Computation

In `n` spatial dimensions, the area factor is:

```text
A_n(r) = Omega_n r^(n-1).
```

Conserved flux requires:

```text
A_n(r) F(r) = Q.
```

Thus:

```text
F(r) = Q/(Omega_n r^(n-1)).
```

Sympy verifies:

```text
d log(F)/d log(r) = 1 - n.
```

For `n=3` and `Omega_3=4*pi`:

```text
F(r) = Q/(4*pi*r**2).
```

## Interpretation

Inverse-square behavior is not generic. It is the `n=3` member of the
dimension-dependent conserved-flux family.
