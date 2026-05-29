# Vacuum Action Origin 46: Scalar Ladder Tensor Rank Obstruction

## Purpose

This proof tests whether a scalar projection/admissibility ladder can supply
the full tensor boundary data needed by a nonlinear metric boundary term.

## Validated Checks

- N scalar ladder rows leave N*(n(n+1)/2-1) tensor components unresolved: passed
- for a 3D boundary, scalar ladder misses 5N tensor directions: passed
- scalar ladder is rank-complete only for a one-component boundary: passed

## Rank Count

An induced metric on an `n`-dimensional boundary has:

```text
n(n+1)/2
```

symmetric components.

An `N`-row scalar ladder supplies:

```text
N
```

scalar conditions.

Full tensor boundary data would require:

```text
N * n(n+1)/2
```

component conditions.

The unresolved rank gap is:

```text
N * (n(n+1)/2 - 1).
```

For a three-dimensional boundary this is:

```text
5N.
```

## Interpretation

The scalar projection ladder cannot by itself determine the full tensor
boundary variation. It is complete only in a one-component boundary sector, or
after a separate theorem supplies tensor-indexed copies of the ladder.
