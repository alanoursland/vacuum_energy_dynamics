# Vacuum Dimension Selector 21: Boundary Dimension Relation

## Purpose

This proof separates two boundary counts that are easy to confuse.

## Validated Checks

- in `D=4`, one-clock spatial slices have dimension `3`: passed
- in `D=4`, spacetime boundary hypersurfaces have dimension `3`: passed
- in `D=4`, spatial boundary surfaces have dimension `2`: passed

## Computation

```text
spatial slice dimension = D - 1
spacetime boundary hypersurface dimension = D - 1
spatial boundary surface dimension = D - 2
```

At `D=4`:

```text
spatial slice dimension = 3
spacetime boundary hypersurface dimension = 3
spatial boundary surface dimension = 2
```

## Interpretation

The induced-metric boundary bookkeeping used by the action bridge concerns a
spacetime boundary hypersurface, not merely a two-dimensional spatial sphere.
