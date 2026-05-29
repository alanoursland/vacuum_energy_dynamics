# GR Boundary Reduction Measurement — proof chain plan

## Purpose

This folder completes the comparison scaffold from
`gr_boundary_reduction_comparison` by asking whether the contact-class integer

```text
R_GR
```

is actually determined by the weak-field GR/Newtonian scalar boundary reduction.

The answer this folder tests is deliberately conservative:

```text
Weak-field GR fixes the physical scalar boundary ledger: Poisson equation,
finite Gauss flux, and exterior 1/r asymptotics.  It does not by itself fix the
projection contact-class integer R until a boundary-defining variable, field
normalization, and moment/test pairing are chosen.
```

Thus the folder distinguishes three statements:

1. **Physical GR scalar ledger:** fixed by weak-field GR.
2. **Projection moment class R:** fixed only after a chosen compactified
   projection embedding.
3. **Projection-origin match:** if the GR scalar ledger is embedded using the
   same admissibility functional as the original projection problem, then it
   lands in the observed `R=0` class, but that is an embedding/normalization
   choice rather than a direct consequence of Poisson + Gauss flux alone.

## Strategy

The proof chain first verifies the GR/Newtonian scalar boundary data: exterior
harmonicity, conserved flux, and finite-flux asymptotics.  It then proves that
these data do not determine the compactified moment weight.  The same physical
finite-flux exterior can be represented with different boundary variables,
field rescalings, and test-pairing weights.  Those choices shift the apparent
contact exponent and therefore shift the ladder index `R`.

The invariant projection comparison is not the raw physical flux alone.  It is
the pushed-forward moment functional

```text
C_R[P] = ∫_0^1 P(y) (1-y)^(R+1) y^(-1/2) dy.
```

The original projection problem used `R=0`, giving

```text
r_(0,k) = (2k - 1)/(2k + 3).
```

Weak-field GR is compatible with this class, but GR's scalar boundary ledger
alone does not force that representation.

## Proof batches

### Batch A: physical scalar GR ledger

Scripts 1–4 check the ordinary weak-field scalar facts: radial Poisson,
exterior `1/r`, conserved Gauss flux, and finite-flux exponent.

### Batch B: compactification and variable-dependence

Scripts 5–9 show that endpoint contact order and moment weights depend on the
chosen boundary variable and field/test normalization.  This prevents `R` from
being read directly from finite flux alone.

### Batch C: projection ladder measurement

Scripts 10–14 verify the `C_R` ladder, the `R=0` projection class, and the
explicit difference between `R=0` and `R=1`.

### Batch D: status and interpretation

Scripts 15–20 state the measurement result: `R_GR` is not an invariantly
specified output of weak-field GR alone.  It becomes `R=0` only after adopting
the projection embedding used by the original admissibility ladder.  Matching
that class is GR-compatible scalar reduction, not a novel boundary condition;
ontology work, if any, remains upstream.
