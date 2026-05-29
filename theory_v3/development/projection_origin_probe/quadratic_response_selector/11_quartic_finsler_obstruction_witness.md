# Quadratic Response Selector 11: Quartic/Finsler Obstruction Witness

## Purpose

This proof constructs an explicit nonquadratic directional response and shows
that it fails the parallelogram gate.

Take

```text
Q(v) = a v1^2 + c v2^2 + eps (v1^2+v2^2)^2.
```

## Validated Checks

- with `eps=0`, the parallelogram residual vanishes: passed
- at `x=(1,0), y=(1,0)`, the residual is:

```text
12*eps
```

## Interpretation

For nonzero `eps`, the response is not metric-quadratic. It may be a valid
higher directional response branch, but it cannot be silently treated as a
single pseudo-Riemannian metric tensor.
