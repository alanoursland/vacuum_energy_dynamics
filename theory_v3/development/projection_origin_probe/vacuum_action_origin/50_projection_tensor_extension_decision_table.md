# Vacuum Action Origin 50: Projection Tensor Extension Decision Table

## Purpose

This proof packages the scalar-versus-tensor projection boundary decision into
a small rank table.

## Validated Checks

- tensor-basis flag increases rank by N*(m-1): passed
- rank gap vanishes only when tensor basis is supplied or m=1: passed
- decision table separates scalar diagnostic, promoted scalar, and tensor partition roles: passed

## Rank Rule

Let:

```text
N = number of projection rows
m = number of boundary tensor components.
```

With no tensor basis, the rank is:

```text
N.
```

With a tensor basis, the rank is:

```text
N*m.
```

The rank gap is:

```text
N*(m-1)*(1-has_tensor_basis).
```

For a 3D induced boundary metric, `m=6`.

## Decision Table For m=6

| has_tensor_basis | has_partition | promoted_scalar | rank_gap | status |
|---:|---:|---:|---:|---|
| 0 | 0 | 0 | `5*N` | auxiliary scalar diagnostic |
| 0 | 0 | 1 | `5*N` | explicit scalar boundary field only |
| 0 | 1 | 0 | `5*N` | auxiliary scalar diagnostic |
| 0 | 1 | 1 | `5*N` | explicit scalar boundary field only |
| 1 | 0 | 0 | `0` | tensor data present; normalization still needs routing |
| 1 | 0 | 1 | `0` | tensor data present; normalization still needs routing |
| 1 | 1 | 0 | `0` | candidate tensor boundary partition |
| 1 | 1 | 1 | `0` | candidate tensor boundary partition |

## Interpretation

The projection ladder can stay auxiliary as a scalar diagnostic, be promoted to
an explicit scalar boundary field, or become part of a tensor boundary theorem
only if a tensor-valued extension and count-once normalization partition are
supplied.
