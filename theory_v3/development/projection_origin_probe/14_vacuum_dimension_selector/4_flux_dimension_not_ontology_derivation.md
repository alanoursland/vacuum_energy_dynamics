# Vacuum Dimension Selector 4: Flux Dimension Is Not Ontology Derivation

## Purpose

This proof marks the dependency of the flux selector.

Conserved flux plus a target field exponent selects a dimension. It does not
by itself prove why that exponent is fundamental.

## Validated Checks

- general target exponent solves to `n = 1-target_exp`: passed
- inverse-square target selects `n=3`: passed
- a different target exponent would select a different dimension: passed

## General Selector

Conserved radial flux gives:

```text
F(r) ~ r^(1-n).
```

If the target exponent is:

```text
F(r) ~ r^target_exp,
```

then:

```text
1 - n = target_exp
```

so:

```text
n = 1 - target_exp.
```

For inverse-square:

```text
target_exp = -2 -> n = 3.
```

For inverse-cube:

```text
target_exp = -3 -> n = 4.
```

## Interpretation

The flux gate selects `n=3` only after exact inverse-square behavior is
accepted as a physical target. The dimension selector still needs an ontology
reason why that target is fundamental.
