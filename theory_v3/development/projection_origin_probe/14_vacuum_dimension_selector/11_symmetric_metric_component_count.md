# Vacuum Dimension Selector 11: Symmetric Metric Component Count

## Purpose

This proof records the component count for a symmetric rank-2 field.

## Validated Checks

- symmetric rank-2 field in `D=4` has `10` components: passed
- symmetric induced metric on a `3`-dimensional hypersurface has `6`
  components: passed

## Computation

For a symmetric rank-2 tensor:

```text
N_sym(z) = z(z+1)/2.
```

Thus:

```text
N_sym(4) = 10.0000000000000
N_sym(3) = 6.00000000000000
```

## Interpretation

This is a counting proof only. It supports the metric lift bookkeeping but does
not by itself force a metric ontology.
