# candidate_projection_origin_classifier — Analysis Note

## Result

`candidate_projection_origin_classifier.py` records the stable Group 100 statuses:

```text
WEIGHT_FUNCTION_IDENTIFIED:
  w(x)=(1-x^2)^4

TRIAL_FUNCTIONS_IDENTIFIED:
  phi_j=x^(2j)

TEST_FUNCTIONS_IDENTIFIED:
  psi_k=x^(2k)-r_k x^(2k-2)

FORMAL_WEIGHTED_PROJECTION_DERIVED:
  A[k,j]=2∫psi_k phi_j w dx

ROW_TESTS_SIGN_CHANGING:
  psi_k has interior root sqrt((2k-1)/(2k+3))

PHYSICAL_RESIDUAL_NOT_DERIVED

SOURCE_VECTOR_NOT_DERIVED

BOUNDARY_CONDITIONS_NOT_DERIVED

PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED

HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE.
```

The classifier blocks:

```text
projection as field equation;
projection as physical ledger;
projection as Hessian.
```

## Interpretation

This classifier is accurate.

Group 100 upgrades the mathematical origin of `A_N`, but not the physical origin. The hierarchy now has identified formal projection machinery:

```text
weight;
test functions;
trial functions.
```

But the missing physical pieces remain:

```text
residual R[f];
source vector;
boundary conditions;
physical ledger assignment.
```

This is a very clean result.

## Carry-forward status

```text
FORMAL_WEIGHTED_PROJECTION_DERIVED
PROJECTION_MACHINERY_IDENTIFIED
ROW_TESTS_SIGN_CHANGING
PHYSICAL_RESIDUAL_NOT_DERIVED
SOURCE_VECTOR_NOT_DERIVED
BOUNDARY_CONDITIONS_NOT_DERIVED
PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED
HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE
```
