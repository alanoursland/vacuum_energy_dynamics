# Vacuum Interval Directional Probe Origin 8: Local Frame Covariance

## Purpose

This proof checks that the reconstructed interval object has the correct
change-of-frame behavior.

## Validated Checks

- interval value is invariant under component/frame relabeling: passed
- determinant transforms by the square of the frame determinant: passed

## Frame Change

Let:

```text
x = P y
Q(x) = x^T H x.
```

The same interval written in the `y` frame is:

```text
Q(y) = y^T H' y
H' = P^T H P.
```

Sympy verifies:

```text
y^T(P^T H P)y = (Py)^T H(Py).
```

It also verifies:

```text
det(H') = det(P)^2 det(H).
```

## Interpretation

Once directional interval probes reconstruct `H`, the recovered object behaves
as a symmetric covariant tensor under local frame changes. This is the correct
transformation behavior for induced metric data.
