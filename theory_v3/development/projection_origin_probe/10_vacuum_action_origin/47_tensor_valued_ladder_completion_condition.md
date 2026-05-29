# Vacuum Action Origin 47: Tensor-Valued Ladder Completion Condition

## Purpose

This proof states the condition under which the projection ladder could become
full boundary tensor data.

It must carry a tensor basis, not only scalar rows.

## Validated Checks

- N ladder rows times m tensor basis elements supply N*m component conditions: passed
- scalar ladder lacks N*(m-1) component conditions when m>1: passed
- basis sizes 1, 3, and 6 give the expected rank gaps: passed
- tensor-valued data may be partitioned only count-once: passed

## Scalar Versus Tensor-Valued Ladder

Let:

```text
N = number of ladder rows
m = number of independent boundary tensor components.
```

A scalar ladder has rank:

```text
N.
```

A tensor-valued ladder of the form:

```text
psi_k(x) E_A
```

with `A=1,...,m` has rank:

```text
N*m.
```

The scalar rank gap is:

```text
N*(m-1).
```

For a three-dimensional induced metric, `m=6`, so the gap is:

```text
5N.
```

## Interpretation

The current projection ladder is scalar. To derive GHY-like tensor boundary
data, the theory must supply a tensor-valued extension or an independent map
from the scalar ladder to all boundary tensor components.
