# Torsion Defect Exclusion 11: Cancellation Structural Vs Tuned

## Purpose

This proof separates two ways of obtaining `J_total = 0`.

Structural cancellation is an identity. Parameter-tuned cancellation is a
condition that must be justified by an additional mechanism.

## Validated Checks

- identity cancellation vanishes for all source values: passed
- independent-channel cancellation imposes a tuning condition: passed
- a structural relation converts tuned-looking cancellation into an identity: passed

## Structural Cancellation

For paired terms:

```text
J_total = X - X,
```

Sympy verifies:

```text
J_total = 0.
```

## Tuned Cancellation

For independent channels:

```text
J_total = a X + b Y,
```

the cancellation condition is:

```text
b = -a X/Y.
```

This is not an identity unless a separate structural relation is supplied.

With:

```text
Y = X
b = -a,
```

the residual becomes:

```text
0.
```

## Interpretation

The torsion-free branch can be selected by structural cancellation, but not by
unexplained coefficient tuning. A cancellation theorem must identify the
relation that makes `J_total = 0` an identity.
