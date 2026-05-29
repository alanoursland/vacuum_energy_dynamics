# Vacuum Dimension Selector 5: Flux Dimension Gate Status

## Purpose

This report summarizes the first dimension-selector proof batch.

## Proofs Completed

Proof `1` validates conserved flux scaling:

```text
F(r) ~ r^(1-n).
```

Proof `2` validates the inverse-square selector:

```text
1-n = -2 -> n = 3.
```

Proof `3` validates dimension-dependent Green-function classes:

```text
n=1: linear
n=2: logarithmic
n>2: r^(2-n).
```

Proof `4` validates the dependency:

```text
n = 1 - target_exp.
```

## Current Result

The flux gate conditionally selects:

```text
n = 3
```

if exact long-range inverse-square behavior is accepted as a fundamental
target.

## Remaining Gap

This is not yet an ontology derivation. The next proofs must add the time
channel:

```text
n=3 plus one universal clock/propagation channel -> D=4.
```
