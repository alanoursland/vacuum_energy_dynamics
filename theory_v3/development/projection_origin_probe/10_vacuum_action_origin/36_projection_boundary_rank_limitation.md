# Vacuum Action Origin 36: Projection Boundary Rank Limitation

## Purpose

This proof records a guardrail for the projection-to-GHY handoff.

The original projection/admissibility defect is scalar. A full nonlinear
metric boundary variation is not scalar.

## Validated Checks

- symmetric induced metric in n dimensions has n(n+1)/2 components: passed
- 3D induced metric boundary variation has five more components than scalar flux: passed
- scalar boundary flux can match only a one-component boundary sector: passed

## Component Count

An induced metric on an `n`-dimensional boundary has:

```text
n(n+1)/2
```

independent symmetric components.

The scalar projection boundary defect has one component.

For a three-dimensional boundary:

```text
n(n+1)/2 = 6.
```

So a scalar boundary defect is short by:

```text
5
```

components.

## Interpretation

The projection/admissibility boundary defect can be a scalar seed or reduced
sector of boundary flux. It cannot by itself be the full nonlinear GHY
variation unless additional tensor structure is derived.
