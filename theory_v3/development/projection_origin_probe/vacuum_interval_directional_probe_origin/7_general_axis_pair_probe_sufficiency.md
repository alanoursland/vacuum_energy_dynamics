# Vacuum Interval Directional Probe Origin 7: General Axis-Pair Probe Sufficiency

## Purpose

This proof generalizes the finite probe reconstruction from the first batch.

The axis-plus-pair probe set:

```text
Q(e_i)
Q(e_i+e_j), i < j
```

contains exactly enough data to reconstruct a symmetric bilinear form in the
finite dimensions used by the bridge.

## Validated Dimensions

- n=1: 1 probes for 1 components: passed
- n=2: 3 probes for 3 components: passed
- n=3: 6 probes for 6 components: passed
- n=4: 10 probes for 10 components: passed
- n=5: 15 probes for 15 components: passed

## Reconstruction Formula

For every dimension checked:

```text
h_ii = Q(e_i)
h_ij = (Q(e_i+e_j)-Q(e_i)-Q(e_j))/2, i < j.
```

The probe count is:

```text
n + n(n-1)/2 = n(n+1)/2.
```

This equals the number of independent components of a symmetric `n x n`
tensor.

## Interpretation

The selector does not need an arbitrary continuum of interval comparisons. A
finite local frame and its pairwise sums are enough to recover the symmetric
metric-like data in the dimensions relevant to the field-lift chain.
