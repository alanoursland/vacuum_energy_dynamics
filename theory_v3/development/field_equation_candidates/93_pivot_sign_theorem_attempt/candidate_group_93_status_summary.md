# candidate_group_93_status_summary — Analysis Note

## Result

`candidate_group_93_status_summary.py` reports:

```text
row-sign normalization B_N=diag(epsilon)A_N derived;
det(B_N) equals sign-normalized det(A_N);
leading pivots equal pi_N;
leading determinants and pivots of B_N are positive through N=30;
Schur complement pivot identity derived and verified through N=15;
simple strict total positivity route blocked by negative 1x1 entries;
small principal-minor/P-matrix route tested but does not close theorem;
all-order row-signed Schur positivity theorem remains open;
parent divergence identity remains unproven;
recombination remains blocked.
```

The row-sign, leading-minor, total-positivity, and P-matrix claims are supported.

The Schur-complement claim is not supported, because `candidate_schur_complement_pivot_identity.py` failed and did not archive `g93_schur_pivots`.

## Corrected interpretation

Correct Group 93 result:

```text
row-sign normalization derived and verified through N=30;

det(B_N) equals sign-normalized det(A_N) through N=30;

leading determinants and pivots of B_N are positive through N=30;

simple total positivity route blocked by negative entries;

full P-matrix route blocked by small principal minor;

Schur complement pivot identity script failed;

Schur route remains open and requires patch;

all-order leading-minor / pivot positivity remains open;

parent divergence identity remains unproven;

recombination remains blocked.
```

## Carry-forward status

Carry forward:

```text
ROW_SIGN_NORMALIZATION_DERIVED
ROW_SIGNED_LEADING_MINORS_POSITIVE_N1_TO_N30
TOTAL_POSITIVITY_ROUTE_BLOCKED
P_MATRIX_ROUTE_BLOCKED
SCHUR_COMPLEMENT_ROUTE_OPEN_PATCH_REQUIRED
ALL_ORDER_LEADING_MINOR_POSITIVITY_OPEN
```

Do not carry forward:

```text
SCHUR_COMPLEMENT_PIVOT_IDENTITY_DERIVED
```

until the script is patched and rerun.
