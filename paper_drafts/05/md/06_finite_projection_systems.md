# 6. Finite Projection Systems

Fix `R >= 0` and truncation order `N`.  The row basis is

```text
chi_{R,1}, ..., chi_{R,N}.
```

The balanced source basis is

```text
B_{R,1}, ..., B_{R,N},
```

with

```text
B_{R,q}(y) = (1-y)^R [y^q - c_{R,q}].
```

The projection matrix has entries

```text
A^{(R,N)}_{kq}
  = int_0^1 chi_{R,k}(y) B_{R,q}(y) W_R(y) dy,
```

where the verification branch uses a positive pairing weight of the form

```text
W_R(y) = (1-y)^(R+4)y^(-1/2).
```

The precise normalization of `B_{R,q}` changes the matrix by invertible column
operations.  It does not change the structural question: whether the finite
pairing between the two admissible coordinate families is nondegenerate.

Exact symbolic checks verified nonzero determinants over the available grid,
including `R = 0..4` and finite orders through the tested ranges.  These
checks were useful as diagnostics, but determinant data alone is not a proof
strategy.  The next section gives the structural interpretation.

