# candidate_row_test_function_structure — Analysis Note

## Result

`candidate_row_test_function_structure.py` analyzes the row test functions:

```text
psi_k(x) = x^(2k-2)[x^2 - r_k]
```

where:

```text
r_k = (2k-1)/(2k+3).
```

It finds:

```text
r_k - 1 = -4/(2k+3)
```

and:

```text
root x_k = sqrt(r_k) = sqrt(2k-1)/sqrt(2k+3).
```

For `k=1..15`, the script reports:

```text
r_k range failures: []
```

so each tested `r_k` lies in `(0,1)`, and each `psi_k` has an interior sign-change root.

## Interpretation

This is a useful structural clue.

The row test functions are not positive basis functions. They are sign-changing test functions with one interior root. That explains why the hierarchy is not a simple positive Gram matrix, and why row-sign behavior and nontrivial determinant signs appeared earlier.

This may also matter for residual reconstruction: the hidden operator/test condition is probably a signed balance condition, not a straightforward positivity projection.

## What It Does Not Prove

The interior root is not a physical boundary condition. It is an algebraic sign-change location. We should not interpret it as a real interface, horizon, shell, or matching surface without a residual/source derivation.

## Carry-forward status

```text
ROW_TEST_FUNCTION_STRUCTURE_DERIVED
R_K_IN_0_1_VERIFIED_K1_TO_K15
ROW_TESTS_SIGN_CHANGING
INTERIOR_TEST_ROOTS_IDENTIFIED
POSITIVE_GRAM_BASIS_INTERPRETATION_BLOCKED
BOUNDARY_CONDITION_NOT_DERIVED
```
