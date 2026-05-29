# Vacuum Action Origin 48: Traceless Source Invisibility Under Scalar Ladder

## Purpose

This proof tests whether a scalar ladder can see traceless boundary source
data.

It cannot, if it enters only through trace.

## Validated Checks

- T is traceless: passed
- scalar trace ladder pairing annihilates traceless source: passed
- traceless source can be nonzero while scalar ladder sees zero: passed
- componentwise tensor pairing can detect the traceless source: passed

## Traceless Source

Use:

```text
T = diag(t1, t2, -t1-t2).
```

Then:

```text
tr T = 0.
```

A scalar ladder row coupled through trace gives:

```text
psi_k * tr T = 0.
```

But the tensor source is not zero:

```text
tr(T^2) = t1^2 + t2^2 + (t1+t2)^2.
```

## Interpretation

The projection ladder can support trace-sector admissibility tests. It cannot
test traceless/shear boundary source data unless it is upgraded to a
tensor-valued ladder.
