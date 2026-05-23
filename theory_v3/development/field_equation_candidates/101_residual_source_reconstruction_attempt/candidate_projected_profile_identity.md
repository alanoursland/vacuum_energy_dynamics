# candidate_projected_profile_identity — Analysis Note

## Result

`candidate_projected_profile_identity.py` verifies:

```text
Σ_j A[k,j] c_j = 2∫psi_k(x) f_N(x) w(x) dx
```

where:

```text
f_N(x) = Σ_j c_j x^(2j).
```

The script reports:

```text
identity failures for N<=6: []
```

Governance records:

```text
matrix action:
  A maps coefficients to weighted test projections of f_N

residual interpretation:
  supports formal residual family R[f]=f-S.
```

## Interpretation

This is the first major success of Group 101.

Group 100 derived each matrix entry as a projection. Group 101 now derives the action of the matrix on a coefficient vector:

```text
A c
```

is the vector of weighted projections of the finite profile `f_N`.

That tells us what the matrix does.

It does not merely encode abstract coefficients; it applies the sign-changing row tests to a finite even-power profile.

## What It Does Not Prove

This is not yet a physical residual. The identity says what `A` does to `f_N`; it does not say why the physical equation should require those projections to match a particular source.

## Carry-forward status

```text
PROJECTED_PROFILE_IDENTITY_DERIVED
A_MAPS_COEFFICIENTS_TO_WEIGHTED_TEST_PROJECTIONS
FORMAL_RESIDUAL_FAMILY_SUPPORTED
PHYSICAL_RESIDUAL_NOT_DERIVED
```
