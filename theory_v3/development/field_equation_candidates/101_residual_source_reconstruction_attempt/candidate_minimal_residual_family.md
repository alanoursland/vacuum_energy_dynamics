# candidate_minimal_residual_family — Analysis Note

## Result

`candidate_minimal_residual_family.py` defines the formal residual family:

```text
R_S[f](x) = f(x) - S(x).
```

The projected equations are:

```text
2∫psi_k(x)[f_N(x)-S(x)]w(x)dx = 0.
```

Equivalently:

```text
A c = b(S)
```

with source vector:

```text
b_k(S)=2∫psi_k(x)S(x)w(x)dx.
```

The script explicitly warns:

```text
S(x) is not yet a physical source, mass density, burden ledger, or exchange term.
```

## Interpretation

This is the second major success of Group 101.

It derives the minimal formal equation compatible with the projection matrix. If `A` projects the unknown profile `f_N`, then any system of the form `A c = b` can be understood as matching the test projections of `f_N` to the test projections of some formal target/source profile `S`.

This is a useful reconstruction:

```text
A c = b(S)
```

now has a clean formal meaning.

## What It Does Not Prove

The residual family is intentionally minimal and formal. It does not identify `S(x)` with matter, mass, curvature energy, vacuum substance exchange, interface smoothing, or total burden.

The physical work is still missing:

```text
What chooses S(x)?
What domain/boundary problem requires this projection?
What physical ledger, if any, does S belong to?
```

## Carry-forward status

```text
MINIMAL_RESIDUAL_FAMILY_FORMAL
SOURCE_VECTOR_FORMULA_DERIVED
A_C_EQUALS_BS_FORMAL_SYSTEM_DERIVED
S_AS_PHYSICAL_SOURCE_NOT_LICENSED
BOUNDARY_CONDITIONS_NOT_DERIVED
ORDINARY_MATTER_SEPARATION_NOT_DERIVED
```
