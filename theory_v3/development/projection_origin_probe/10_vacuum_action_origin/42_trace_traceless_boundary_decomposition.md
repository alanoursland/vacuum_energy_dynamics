# Vacuum Action Origin 42: Trace-Traceless Boundary Decomposition

## Purpose

This proof sharpens the scalar projection boundary limitation.

Scalar boundary data can see the trace sector. It is blind to traceless
induced-metric variations.

## Validated Checks

- H decomposes into trace plus traceless parts: passed
- trace plus traceless parts reconstruct H: passed
- identity/trace scalar is blind to traceless boundary variation: passed
- traceless boundary variations can be nonzero while scalar trace sees zero: passed

## Decomposition

For a three-dimensional induced metric variation `H`:

```text
H = (tr H / 3) I + H_T
```

with:

```text
tr H_T = 0.
```

SymPy verifies the decomposition and reconstruction.

## Scalar Blindness

For a traceless variation:

```text
T = diag(t1, t2, -t1-t2),
```

the scalar trace pairing is:

```text
tr(I T) = 0.
```

But `T` itself can be nonzero.

## Interpretation

The projection/admissibility scalar can be a trace-sector diagnostic. It does
not determine the traceless/shear boundary data required by the full nonlinear
metric boundary term.
