# Group 91 Summary: Determinant Sign Pattern and Nonzero Audit

## Purpose

Group 91 corrected the determinant theorem target after Group 90.

Group 90 disproved determinant positivity as stated:

```text
det(A_11)<0.
```

But the hierarchy only requires:

```text
det(A_N) != 0
```

not positivity.

Group 91 asked:

```text
After determinant positivity fails at N=11, does nonzero invertibility remain plausible,
and what sign pattern should replace the failed positivity theorem?
```

## Main Result

Group 91 is complete.

Stable result:

```text
N=11 determinant positivity counterexample verified;

determinant positivity theorem disproven;

pivot positivity theorem disproven;

determinant nonzero verified through N=30;

sign pattern supported through N=30:
  positive determinant for N=1..10;
  sign(det(A_N))=(-1)^N for N=11..30;
  pivot sign negative for N=11..30;

sign-normalized determinant positive through N=30;

N=11 and N=12 profile generation survives sign flip;

nonzero/invertibility theorem remains open;

determinant sign-pattern theorem remains open;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What We Actually Learned

Group 91 is valuable because it stops a false theorem from carrying forward.

The determinant branch now has the correct structure:

```text
positivity:
  false

nonzero:
  supported through N=30, still unproven all-order

sign pattern:
  supported through N=30, still unproven all-order

profile generation:
  survives the first sign flip
```

That is much better than the post-Group-90 ambiguity.

## Script-Level Analysis

### 1. Sign Pattern Problem

The opener correctly retargets the determinant work:

```text
det(A_N)>0 for all N is false;
det(A_N)!=0 for all N remains the relevant hierarchy theorem.
```

It also records the key conceptual correction:

```text
profile generation needs invertibility, not positivity.
```

### 2. N11 Counterexample Verification

The script recomputes `N=10,11,12`.

It finds:

```text
N=10:
  det sign = +1
  pivot sign = +1

N=11:
  det sign = -1
  pivot sign = -1

N=12:
  det sign = +1
  pivot sign = -1
```

So:

```text
N=11 positivity counterexample = True.
```

Interpretation:

```text
determinant positivity and pivot positivity are both disproven.
```

### 3. Determinant Sign Sequence N1 to N30

The script computes determinant and pivot signs through `N=30`.

It finds:

```text
mismatches = []
zero failures = []
```

against the tested pattern:

```text
N=1..10:
  det_sign = +1
  pivot_sign = +1

N=11..30:
  det_sign = (-1)^N
  pivot_sign = -1
```

Interpretation:

```text
nonzero determinant and corrected sign pattern are strongly supported through N=30.
```

### 4. Sign Normalization Hypothesis Test

The script defines:

```text
S_N = det(A_N)        for N<=10
S_N = (-1)^N det(A_N) for N>=11.
```

It finds:

```text
S_N > 0
```

for every:

```text
N=1..30.
```

Interpretation:

```text
raw positivity is false, but sign-normalized positivity is supported through N=30.
```

### 5. Post-Signflip Invertibility Validation

The script solves the hierarchy systems at `N=11` and `N=12`.

It finds:

```text
N=11:
  det_sign = -1
  residuals_zero = True

N=12:
  det_sign = +1
  residuals_zero = True.
```

Interpretation:

```text
the sign flip does not block profile generation.
```

This confirms that invertibility, not positivity, is the key condition.

### 6. Nonzero Theorem Retarget

The retargeting classifier records the corrected statuses:

```text
POSITIVITY_THEOREM_DISPROVEN_BY_N11
PIVOT_POSITIVITY_DISPROVEN_BY_N11
DETERMINANT_NONZERO_VERIFIED_N1_TO_N30
SIGN_PATTERN_SUPPORTED_N1_TO_N30
SIGN_NORMALIZATION_SUPPORTED_N1_TO_N30
PROFILE_GENERATION_SURVIVES_SIGN_FLIP
NONZERO_INVERTIBILITY_THEOREM_OPEN
SIGN_PATTERN_THEOREM_OPEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

This is the correct carry-forward state.

### 7. Group Status Summary

The final summary is conceptually sound and should supersede any older positivity wording from Group 90.

## Final Status Ledger

```text
determinant_positivity:
  DISPROVEN_BY_N11

pivot_positivity:
  DISPROVEN_BY_N11

determinant_nonzero:
  VERIFIED_THROUGH_N30

sign_pattern:
  SUPPORTED_THROUGH_N30

raw_det_signs:
  N=1..10: +
  N=11..30: (-1)^N

pivot_signs:
  N=1..10: +
  N=11..30: -

sign_normalized_determinant:
  POSITIVE_THROUGH_N30

profile_generation_after_sign_flip:
  SURVIVES_N11_N12

all_order_nonzero_theorem:
  OPEN

all_order_sign_pattern_theorem:
  OPEN

parent_divergence:
  NOT_PROVEN

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 91 rejects:

```text
determinant positivity as all-order theorem;
pivot positivity as all-order theorem;
negative determinant as singularity;
finite nonzero evidence as proof;
finite sign pattern as proof;
parent equation jump;
recombination opening.
```

## Strategic Interpretation

Group 91 is a cleanup group, but it is not mere bookkeeping.

It protects the theory search from a false theorem. That is high-value progress.

The determinant branch now has a better theorem target:

```text
prove det(A_N)!=0 for all N
```

and a more specific conjectural sign law:

```text
det(A_N)>0 for N<=10;
sign(det(A_N))=(-1)^N for N>=11.
```

The next work should explain the sign transition at `N=11`.

## Recommended Next Group

Best next group:

```text
92_determinant_sign_recurrence_search
```

Purpose:

```text
derive a recurrence for determinant signs, pivots, or sign-normalized determinants.
```

Other viable routes:

```text
92_nonzero_invertibility_theorem_attempt
92_biorthogonal_polynomial_construction
92_all_order_limit_obstruction
92_covariant_payload_suppression_lift
```

My recommendation is:

```text
92_determinant_sign_recurrence_search
```

because Group 91 provides a clear finite sign pattern that now needs a recurrence or theorem.

## Final Interpretation

Group 91 sorted the coins after the false glimmer.

```text
The positive coin was fake.
The nonzero coin is still real.
The sign flip is not a collapse;
it is a pattern.

Now we need the recurrence that tells us why the goblin changes masks at eleven.
```
