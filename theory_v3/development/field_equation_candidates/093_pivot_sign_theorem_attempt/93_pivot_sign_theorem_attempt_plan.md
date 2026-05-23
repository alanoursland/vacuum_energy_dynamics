# 93_pivot_sign_theorem_attempt — Plan

## Purpose

Group 93 attempts to recast the Group 92 sign-normalized pivot theorem as a structural leading-minor / Schur-complement theorem.

Group 92 established the corrected target:

```text
D_N = det(A_N)
p_N = D_N/D_(N-1)
pi_N = p_N for N<=10, pi_N=-p_N for N>=11
pi_N > 0 through N=30
```

Group 93 defines a row-signed matrix:

```text
epsilon_k = +1 for k<=10, -1 for k>=11
B_N[k,j] = epsilon_k A_N[k,j]
```

Then:

```text
det(B_N) = sign-normalized det(A_N)
det(B_N)/det(B_(N-1)) = pi_N
```

So the theorem target becomes:

```text
all leading pivots / leading Schur complements of B_N are positive.
```

## Desired Results

```text
ROW_SIGN_NORMALIZATION_DERIVED
SIGN_NORMALIZED_LEADING_MINORS_POSITIVE_N1_TO_N30
SIGN_NORMALIZED_PIVOTS_POSITIVE_N1_TO_N30
SCHUR_COMPLEMENT_PIVOT_IDENTITY_DERIVED
TOTAL_POSITIVITY_ROUTE_BLOCKED
PRINCIPAL_MINOR_ROUTE_TESTED_SMALL_N
ALL_ORDER_PIVOT_SIGN_THEOREM_OPEN
ALL_ORDER_NONZERO_DETERMINANT_THEOREM_OPEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

## Scripts

```text
candidate_pivot_sign_theorem_problem.py
candidate_row_sign_normalized_matrix.py
candidate_schur_complement_pivot_identity.py
candidate_total_positivity_obstruction.py
candidate_principal_minor_route_test.py
candidate_positive_leading_minor_table.py
candidate_pivot_sign_route_classifier.py
candidate_group_93_status_summary.py
order.txt
```

## Must Not Do

Do not revive raw determinant positivity, claim all-order pivot positivity from finite checks, claim local inertness, write a parent field equation, or open recombination.
