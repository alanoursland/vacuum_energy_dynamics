# Group 100 Summary: Moment Projection Derivation Attempt

## Purpose

Group 100 followed the strongest clue from Group 099.

Group 099 showed:

```text
beta_moment(s) = 2 ∫_0^1 x^(2s)(1-x^2)^4 dx.
```

Group 100 asked whether the full hierarchy matrix `A_N` could be derived as a formal weighted projection matrix.

## Main Result

Group 100 succeeds.

It derives the formal projection representation:

```text
A[k,j] = 2 ∫_0^1 psi_k(x) phi_j(x) (1-x^2)^4 dx
```

with:

```text
phi_j(x) = x^(2j)

psi_k(x) = x^(2k) - ((2k-1)/(2k+3)) x^(2k-2).
```

The projection equality is verified with no failures for `k,j=1..7`.

## What We Actually Learned

The hierarchy is no longer merely “moment-like.”

It has explicit projection machinery:

```text
weight:
  w(x) = (1-x^2)^4

trial basis:
  phi_j(x) = x^(2j)

test functions:
  psi_k(x) = x^(2k) - r_k x^(2k-2)

row ratio:
  r_k = (2k-1)/(2k+3).
```

This upgrades the mathematical origin status:

```text
old:
  MOMENT_PROJECTION_ORIGIN_PLAUSIBLE_BUT_UNDERDERIVED

new:
  FORMAL_WEIGHTED_PROJECTION_DERIVED
```

But the physical origin is still not derived.

## Script-Level Analysis

### 1. Projection Derivation Problem

The opener defines the exact test/trial projection target and correctly blocks interpreting the projection as a field equation or burden ledger.

### 2. Weighted Moment Identity

The script confirms:

```text
beta_moment(s)=2∫_0^1 x^(2s)(1-x^2)^4 dx
```

with no exact sample failures for `n=1..10`.

### 3. Test/Trial Projection Derivation

The script verifies:

```text
A[k,j]=2∫_0^1 psi_k phi_j w dx
```

with no failures for `k,j=1..7`.

This is the central result of the group.

### 4. Row Test Function Structure

The script shows:

```text
psi_k(x)=x^(2k-2)[x^2-r_k]
r_k=(2k-1)/(2k+3)
r_k-1=-4/(2k+3)
```

and finds no failures for:

```text
0 < r_k < 1
```

through `k=15`.

So each row test has one interior sign-change root:

```text
x_k = sqrt((2k-1)/(2k+3)).
```

This explains why the projection is not a positive Gram/Hessian structure.

### 5. Projection Origin Classifier

The classifier records:

```text
WEIGHT_FUNCTION_IDENTIFIED
TRIAL_FUNCTIONS_IDENTIFIED
TEST_FUNCTIONS_IDENTIFIED
FORMAL_WEIGHTED_PROJECTION_DERIVED
ROW_TESTS_SIGN_CHANGING
PHYSICAL_RESIDUAL_NOT_DERIVED
SOURCE_VECTOR_NOT_DERIVED
BOUNDARY_CONDITIONS_NOT_DERIVED
PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED
HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE
```

### 6. Group Status Summary

The final summary is accurate and recommends:

```text
101_residual_source_reconstruction_attempt
```

or:

```text
101_difference_numerator_factorization_attempt.
```

## Final Status Ledger

```text
weight_function:
  IDENTIFIED_AS_(1-x^2)^4

trial_functions:
  IDENTIFIED_AS_x^(2j)

test_functions:
  IDENTIFIED_AS_x^(2k)-r_k*x^(2k-2)

row_ratio:
  r_k=(2k-1)/(2k+3)

formal_projection:
  DERIVED

projection_equality:
  VERIFIED_KJ_1_TO_7

row_tests:
  SIGN_CHANGING

interior_roots:
  IDENTIFIED

positive_Gram_interpretation:
  BLOCKED

naive_Hessian_interpretation:
  NOT_LICENSED

physical_residual:
  NOT_DERIVED

source_vector:
  NOT_DERIVED

boundary_conditions:
  NOT_DERIVED

physical_ledger_assignment:
  DEFERRED

hierarchy_role:
  AUXILIARY_ADMISSIBILITY_CANDIDATE

parent_equation:
  NOT_READY

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 100 rejects:

```text
projection representation as field equation;
projection representation as J_curv;
projection representation as H_exch;
projection representation as total burden;
projection representation as source law;
projection representation as physical boundary condition;
projection representation as symmetric Hessian/positive Gram matrix.
```

## Strategic Interpretation

Group 100 is important.

It shows that the hierarchy has a formal projection origin. That makes the hierarchy less mysterious and gives the next physical bridge a concrete target:

```text
find the residual equation whose projection against psi_k produces this matrix.
```

The next group should probably ask:

```text
What residual R[f] and source vector b_k produce A c = b?
```

That is the step from formal projection machinery toward physical origin.

## Recommended Next Group

Best next group:

```text
101_residual_source_reconstruction_attempt
```

Purpose:

```text
try to reconstruct a candidate residual equation, source vector, and boundary/domain interpretation behind the projection.
```

Alternative:

```text
101_difference_numerator_factorization_attempt
```

if the project wants to continue the auxiliary admissibility proof trail.

## Final Interpretation

Group 100 found the loom.

```text
The matrix is woven from a weight,
a trial basis,
and sign-changing row tests.

But the weaver is still missing.

Next goblin hunt:
find the residual that pulled the threads.
```
