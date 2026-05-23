# 91_determinant_sign_pattern_and_nonzero_audit — Plan

## Purpose

Group 91 corrects the theorem target after Group 90.

Group 90 attempted a determinant positivity theorem. The raw pivot-extension result showed the positivity target is false:

```text
N=11:
  det(A_N) < 0
  pivot < 0

N=12:
  det(A_N) > 0
  pivot < 0
```

Therefore the old target:

```text
det(A_N) > 0 for all N
```

is dead.

But the hierarchy does **not** require determinant positivity. It requires only:

```text
det(A_N) != 0
```

so the coefficient system remains invertible.

Group 91 audits the determinant signs and retargets the theorem from positivity to nonzero/invertibility plus sign-pattern analysis.

This is real progress if it makes the sign flip permanent in the archive and prevents future groups from carrying the wrong positivity status.

## Group Name

```text
91_determinant_sign_pattern_and_nonzero_audit
```

## Central Question

```text
After determinant positivity fails at N=11, does nonzero invertibility remain plausible,
and what sign pattern should replace the failed positivity theorem?
```

## Starting State

Imported from Group 90 raw results:

```text
derivative/Sturm-like factorization derived;
Andreief determinant representation derived;
simple Chebyshev fixed-sign route blocked/not established;
Hankel difference structure A=H1-RH0 derived;
det(A_N)>0 through N=10;
det(A_11)<0;
det(A_12)>0;
pivot positivity fails at N=11 and N=12;
det(A_N) nonzero through N=12;
positivity theorem false as stated;
nonzero/invertibility theorem open;
parent divergence identity unproven;
recombination blocked.
```

## New Theorem Target

Replace:

```text
det(A_N)>0 for all N
```

with:

```text
det(A_N) != 0 for all N
```

plus a sign-pattern theorem.

A finite sign pattern to test:

```text
N = 1..10:
  det(A_N)>0
  pivot_N>0

N >= 11 in tested range:
  sign(det(A_N)) = (-1)^N
  pivot_N < 0
```

This pattern is a conjecture unless proven.

## What This Group May Do

Group 91 may:

```text
verify the N=11 positivity counterexample;
compute exact determinant and pivot signs through N=30;
test the finite sign-pattern hypothesis;
verify nonzero determinant through N=30;
confirm profile generation still works after sign flip;
replace positivity statuses with invertibility/sign-pattern statuses;
recommend the next theorem route.
```

## What This Group Must Not Do

Group 91 must not:

```text
claim all-order nonzero theorem from finite checks;
claim sign pattern theorem from finite checks;
revive determinant positivity;
claim all-order local inertness;
claim hierarchy convergence;
claim full covariant geometry;
claim rho(y)=0;
write a parent field equation;
insert B_s/F_zeta;
solve D_layer legitimacy;
construct active O by label;
open recombination.
```

## Recommended Script Batch

```text
candidate_sign_pattern_problem.py
candidate_n11_counterexample_verification.py
candidate_determinant_sign_sequence_N1_to_N30.py
candidate_sign_normalization_hypothesis_test.py
candidate_post_signflip_invertibility_validation.py
candidate_nonzero_theorem_retarget.py
candidate_group_91_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_sign_pattern_problem.py

Open Group 91 as a sign-pattern and nonzero audit.

It should restate:

```text
positivity theorem failed;
nonzero determinant theorem remains open;
statuses must be corrected.
```

### 2. candidate_n11_counterexample_verification.py

Recompute:

```text
det(A_10), det(A_11), det(A_12)
pivot_10, pivot_11, pivot_12
```

Expected:

```text
det(A_10)>0
det(A_11)<0
det(A_12)>0
pivot_10>0
pivot_11<0
pivot_12<0
```

This permanently records the positivity counterexample.

### 3. candidate_determinant_sign_sequence_N1_to_N30.py

Compute exact determinant and pivot signs through `N=30`.

Expected:

```text
det sign:
  + for N=1..10
  (-1)^N for N=11..30

pivot sign:
  + for N=1..10
  - for N=11..30

all determinants nonzero through N=30.
```

### 4. candidate_sign_normalization_hypothesis_test.py

Test the finite normalized determinant pattern:

```text
S_N = det(A_N)                         for N<=10
S_N = (-1)^N det(A_N)                  for N>=11
```

Expected:

```text
S_N > 0 through N=30.
```

This gives a candidate sign-normalized nonzero theorem target, not proof.

### 5. candidate_post_signflip_invertibility_validation.py

Use `N=11` and `N=12` matrices to solve:

```text
A_N a = b_N
```

and verify target residuals vanish.

Expected:

```text
det sign changes do not prevent profile generation;
invertibility is what matters.
```

### 6. candidate_nonzero_theorem_retarget.py

Classify the corrected theorem target:

```text
POSITIVITY_THEOREM_DISPROVEN
NONZERO_DETERMINANT_VERIFIED_N1_TO_N30
SIGN_PATTERN_SUPPORTED_N1_TO_N30
NONZERO_INVERTIBILITY_THEOREM_OPEN
SIGN_PATTERN_THEOREM_OPEN
PROFILE_GENERATION_SURVIVES_SIGN_FLIP
```

### 7. candidate_group_91_status_summary.py

Close the group.

Expected result:

```text
Group 91 retargets determinant work from positivity to nonzero/sign-pattern.
```

## Key Success Criteria

Group 91 must earn these statuses:

```text
DETERMINANT_POSITIVITY_DISPROVEN_BY_N11
DETERMINANT_NONZERO_VERIFIED_N1_TO_N30
SIGN_PATTERN_SUPPORTED_N1_TO_N30
PROFILE_GENERATION_SURVIVES_SIGN_FLIP
ALL_ORDER_NONZERO_THEOREM_OPEN
```

## Safe Handoff Options

Likely next groups:

```text
92_determinant_sign_recurrence_search
92_nonzero_invertibility_theorem_attempt
92_biorthogonal_polynomial_construction
92_all_order_limit_obstruction
92_covariant_payload_suppression_lift
```

Best next group if the sign audit succeeds:

```text
92_determinant_sign_recurrence_search
```

because the sign flip suggests a pivot-sign recurrence or determinant recurrence is the right theorem target.

## Final Interpretation

Group 91 asks:

```text
Did the determinant die,
or only stop being positive?
```

Goblin discipline:

```text
A negative determinant is not a broken lock.
A zero determinant is.
