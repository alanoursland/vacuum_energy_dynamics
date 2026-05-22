# Group 90 Summary: Determinant Positivity Theorem Attempt

## Purpose

Group 90 attempted to prove the determinant positivity theorem isolated after Group 89.

Group 89 had shown:

```text
closed rational A_N entry formula derived;
det(A_N)>0 verified through N=10;
leading pivots nonzero through N=10;
moment-pairing factorization A_N[k,j]=<t^j,q_k>_mu derived;
profile generation validated through N=10;
all-order determinant theorem open.
```

Group 90 asked:

```text
Can det(A_N)>0 be proven for all N from the moment-pairing structure?
```

The answer is:

```text
no. Positivity is false as stated.
```

But the more important hierarchy condition:

```text
det(A_N) != 0
```

remains open and survives through the tested range.

## Main Result

Group 90 is complete, but its generated classifier and status summary need correction.

Correct stable result:

```text
derivative/Sturm-like factorization derived;

Andreief determinant representation derived;

simple Chebyshev fixed-sign route blocked or not established;

Hankel difference structure A=H1-RH0 derived;

det(A_N)>0 through N=10;

det(A_11)<0;

det(A_12)>0;

pivot positivity fails at N=11 and N=12;

det(A_N) remains nonzero through N=12;

all-order determinant positivity theorem is disproven as stated;

all-order determinant nonzero/invertibility theorem remains open;

determinant sign-pattern theorem is now required;

all-order limit/convergence remains open;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What We Actually Learned

Group 90 makes real progress because it breaks a false theorem target.

Before Group 90, the tempting target was:

```text
prove det(A_N)>0 for all N.
```

After Group 90, the raw determinant extension shows:

```text
N=11:
  det(A_N)<0
  pivot<0
```

So positivity cannot be the all-order theorem.

The correct target is now:

```text
prove det(A_N) != 0 for all N
```

and understand the sign pattern.

That is a major status correction.

## Script-Level Analysis

### 1. Determinant Positivity Problem

The opener correctly frames Group 90 as a theorem attempt, not another finite-check group.

It imports the Group 89 state correctly and warns that finite determinant evidence cannot prove an all-order theorem.

That warning turned out to be crucial.

### 2. Derivative Factorization

The row object has the derivative structure:

```text
q_k(t) mu(t)
=
-1/(k+3/2) (1-t)^3 d/dt[t^(k-1/2)(1-t)^2].
```

This is a valid structural result.

Interpretation:

```text
the determinant rows are connected to a weighted derivative/Sturm-like operator.
```

This remains useful for a future nonzero/invertibility proof.

### 3. Andreief Representation

The determinant admits an Andreief representation:

```text
det(A_N)
=
1/N! ∫ det[t_i^j] det[q_k(t_i)] ∏ mu(t_i) dt_i.
```

For `N=2`:

```text
det[q]/Vandermonde
=
(35*t1*t2 - 7*t1 - 7*t2 + 3)/35.
```

Interpretation:

```text
positivity would require controlling the sign/integral behavior of the q determinant.
```

This representation is valid, but not by itself a positivity proof.

### 4. Chebyshev Sign Route Test

The test shows:

```text
q1(t)=t-1/5
```

with:

```text
q1(1/10)=-1/10
q1(9/10)=7/10.
```

So the simplest fixed-sign route fails or is at least not established.

There is a nuance: the two printed samples for the `N=2` quotient are both positive, so those samples do not prove sign variation of the quotient. But the naive Chebyshev route is still not established, and the `q1` sign change blocks the simplest basis-level positivity story.

### 5. Hankel Difference Structure

The matrix decomposes as:

```text
A = H1 - R H0
```

where:

```text
H0[k,j]=beta(k+j-1)
H1[k,j]=beta(k+j)
R=diag((2k-1)/(2k+3)).
```

The script verifies:

```text
H1 - R H0 - A = 0
```

for `N=4`.

Interpretation:

```text
A is a row-dependent Hankel/Christoffel difference,
not a plain positive Hankel Gram matrix.
```

This explains why determinant positivity is nontrivial and why a simple Gram proof does not work.

### 6. Pivot Evidence Extension N1 to N12

This is the decisive script.

The raw results show:

```text
N=1..10:
  det(A_N)>0
  pivot>0

N=11:
  det(A_N)>0? False
  pivot>0? False

N=12:
  det(A_N)>0? True
  pivot>0? False
```

Thus:

```text
det(A_11)<0
pivot_11<0
pivot_12<0.
```

The governance lines in the script incorrectly say:

```text
det(A_N)>0 through N=12
pivots positive through N=12
```

Those lines should not be carried forward.

Correct interpretation:

```text
positivity fails at N=11;
nonzero determinant survives through N=12.
```

### 7. Determinant Positivity Route Classifier

The classifier incorrectly records:

```text
PIVOT_EVIDENCE_EXTENDED_N1_TO_N12:
  determinants and pivots positive through N=12.
```

That status must be corrected.

Replacement statuses:

```text
DETERMINANT_POSITIVITY_DISPROVEN_BY_N11
PIVOT_POSITIVITY_DISPROVEN_BY_N11
DETERMINANT_NONZERO_VERIFIED_N1_TO_N12
INVERTIBILITY_THEOREM_OPEN
DETERMINANT_SIGN_PATTERN_OPEN
```

### 8. Group Status Summary

The generated status summary also incorrectly says determinant and pivot positivity evidence extended through `N=12`.

The corrected group summary is this document.

## Final Status Ledger

```text
derivative_factorization:
  DERIVED

Andreief_representation:
  DERIVED

simple_Chebyshev_sign_route:
  BLOCKED_OR_NOT_ESTABLISHED

Hankel_difference_structure:
  DERIVED
  A = H1 - R H0

determinant_positivity:
  TRUE_THROUGH_N10
  FALSE_AT_N11
  TRUE_AGAIN_AT_N12

pivot_positivity:
  TRUE_THROUGH_N10
  FALSE_AT_N11
  FALSE_AT_N12

determinant_nonzero:
  VERIFIED_THROUGH_N12

all_order_positivity_theorem:
  DISPROVEN_AS_STATED

all_order_nonzero_theorem:
  OPEN

determinant_sign_pattern:
  OPEN

all_order_limit:
  OPEN

parent_divergence:
  NOT_PROVEN

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 90 rejects:

```text
all-order determinant positivity;
finite evidence as theorem;
simple Chebyshev fixed-sign proof;
A as plain positive Hankel Gram matrix;
determinant positivity as hierarchy requirement;
parent equation jump;
recombination opening.
```

## Strategic Interpretation

Group 90 is unexpectedly valuable.

It does not prove the positivity theorem. It kills the positivity theorem.

That prevents future groups from chasing the wrong theorem. The hierarchy only needs invertibility, not positivity, so the route is not dead. But it must be retargeted.

The right theorem target is now:

```text
det(A_N) != 0 for all N
```

plus:

```text
determinant sign-pattern / pivot sign-pattern.
```

## Recommended Next Group

Best next group:

```text
91_determinant_sign_pattern_and_nonzero_audit
```

Purpose:

```text
verify the N=11 sign flip;
separate positivity, nonzero invertibility, and sign-pattern claims;
test determinant signs through a wider range using the closed rational matrix;
decide whether the nonzero theorem remains plausible and what proof route is appropriate.
```

Second-best route:

```text
91_hierarchy_recurrence_search
```

Purpose:

```text
derive a determinant or pivot recurrence that explains the sign flip.
```

Third route:

```text
91_biorthogonal_polynomial_construction
```

but only after retargeting it to nonzero/sign-regularity rather than positivity.

## Commit Warning

Do not carry forward the generated Group 90 classifier/status summary unchanged.

The archive-facing statuses should be corrected before future groups depend on them.

## Final Interpretation

Group 90 found the painted door.

```text
The positivity goblin died at N=11.
The invertibility goblin survived.
The determinant did not vanish;
it changed its grin.

Now we stop asking for a positive determinant
and ask why the determinant keeps refusing zero.
```
