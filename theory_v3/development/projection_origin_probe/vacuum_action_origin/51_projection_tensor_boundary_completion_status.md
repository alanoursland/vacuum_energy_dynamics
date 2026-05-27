# Vacuum Action Origin: Projection Tensor Boundary Completion Status After Proofs 46-50

## Purpose

This report answers the immediate question left by the EH/GHY normalization
batch:

```text
does the scalar projection ladder produce tensor boundary data beyond the trace
sector?
```

## Proofs Completed

Proof `46` proves the scalar ladder tensor rank obstruction:

```text
rank gap = N * (n(n+1)/2 - 1).
```

For a three-dimensional boundary:

```text
rank gap = 5N.
```

Proof `47` proves the tensor-valued completion condition:

```text
scalar ladder rank = N
tensor-valued ladder rank = N*m.
```

Full tensor boundary data requires tensor-indexed ladder copies or an
equivalent tensor map.

Proof `48` proves traceless source invisibility under scalar trace pairing:

```text
tr T = 0
psi_k tr T = 0
```

even when `T` is nonzero.

Proof `49` proves componentwise boundary momentum is required:

```text
p_ij = s_ij.
```

Trace-only terms do not supply off-diagonal/shear boundary momentum.

Proof `50` packages the decision table:

```text
scalar diagnostic;
explicit scalar boundary field;
tensor-valued extension;
count-once tensor partition.
```

## Current Result

The scalar projection ladder does not derive the full nonlinear GHY boundary
term.

Its current supported roles are:

```text
1. scalar trace-sector admissibility diagnostic;
2. scalar seed of boundary flux;
3. explicit scalar boundary field if promoted;
4. part of a tensor boundary theorem only if a tensor-valued extension is
   independently derived.
```

## Consequence

This resolves the immediate projection-to-GHY question negatively in the
current formalism:

```text
projection ladder alone -> not full tensor GHY.
```

The EH/GHY action remains selected by the geometric/action gates, while the
projection ladder remains auxiliary unless future work derives tensor-valued
projection rows.

## Remaining Gap

The next action-origin targets are now outside the scalar projection ladder:

```text
1. derive tensor-valued boundary data from vacuum interval/comparison
   structure;
2. derive torsion-source absence;
3. derive dimension 3+1;
4. derive Lambda branch selection or relaxation.
```
