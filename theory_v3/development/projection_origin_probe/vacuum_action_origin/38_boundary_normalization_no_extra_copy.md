# Vacuum Action Origin 38: Boundary Normalization No-Extra-Copy Gate

## Purpose

This proof applies the count-once source lesson to the boundary action
normalization.

## Validated Checks

- independent boundary normalizations add: passed
- if EH already has target normalization, independent auxiliary copy must vanish: passed
- boundary normalization can be partitioned without changing total: passed
- adding a full auxiliary copy doubles the boundary normalization: passed

## Independent Boundary Normalizations

Let the total weak boundary normalization be:

```text
K_total = K_EH + K_aux.
```

If the EH/GHY branch already carries the target normalization:

```text
K_EH = K_target,
```

then requiring:

```text
K_total = K_target
```

forces:

```text
K_aux = 0.
```

## Partition Route

A safe partition is possible:

```text
K_EH = theta K_target
K_aux = (1-theta) K_target.
```

But then the two pieces are not independent copies; they are a count-once
decomposition of the same boundary normalization.

## Interpretation

Projection/admissibility boundary terms cannot add an extra full boundary
normalization on top of EH/GHY. They must either vanish, stay auxiliary, or be
part of an explicit count-once partition.
