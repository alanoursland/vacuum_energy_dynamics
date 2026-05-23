# 90_determinant_positivity_theorem_attempt — Plan

## Purpose

Group 90 attempts the determinant positivity theorem isolated by Group 89.

Group 89 showed:

```text
closed rational A_N entry formula derived;
det(A_N)>0 verified through N=10;
leading pivots nonzero through N=10;
moment-pairing factorization A_N[k,j]=<t^j,q_k>_mu derived;
profile generation validated through N=10;
all-order determinant theorem remains open.
```

Group 90 now tries to prove or partially prove the all-order determinant theorem.

This group should not merely compute more determinants. It must test proof routes.

The expected honest outcome is probably:

```text
a full all-order determinant theorem is not closed,
but the determinant problem is sharpened:
  derivative factorization derived;
  Andreief determinant representation derived;
  simple Chebyshev/sign-definite determinant route tested and rejected;
  Hankel-difference structure derived;
  pivot evidence extended;
  determinant positivity theorem target becomes more precise.
```

This is real progress if a plausible proof route is tested and either advanced or cleanly blocked.

## Group Name

```text
90_determinant_positivity_theorem_attempt
```

## Central Question

```text
Can det(A_N)>0 be proven for all N from the moment-pairing structure,
or can we identify which proof route fails?
```

## Starting State

Imported from Group 89:

```text
A_N entries have closed rational form;
det(A_N)>0 verified through N=10;
leading pivots nonzero through N=10;
A_N[k,j]=<t^j,q_k>_mu derived;
profile generation works through N=10;
next obstructions/local rho remain;
all-order determinant theorem open;
parent divergence identity unproven;
recombination blocked.
```

## Main Matrix

The hierarchy matrix is:

```text
A_N[k,j] = <t^j, q_k(t)>_mu
```

with:

```text
mu(t) = t^(-1/2)(1-t)^4
q_k(t) = t^k - r_k t^(k-1)
r_k = (2k-1)/(2k+3)
```

and exact entries:

```text
A_N[k,j] =
1536*(4j - 6k + 3)
/
((2k + 3)
 (2j + 2k - 1)
 (2j + 2k + 1)
 (2j + 2k + 3)
 (2j + 2k + 5)
 (2j + 2k + 7)
 (2j + 2k + 9)).
```

## Proof Routes to Test

### Route 1: Derivative/Sturm factorization

Use:

```text
q_k(t) mu(t)
  proportional to
(1-t)^3 d/dt [ t^(k-1/2)(1-t)^2 ].
```

This may connect the determinant to integration-by-parts and orthogonal-polynomial structure.

### Route 2: Andreief determinant representation

Use the identity:

```text
det(A_N)
= 1/N! ∫ det[t_i^j] det[q_k(t_i)] ∏ mu(t_i) dt_i.
```

If both determinants had fixed compatible sign on the ordered simplex, positivity would follow.

### Route 3: Chebyshev/sign-definite route

Test whether:

```text
det[q_k(t_i)]
```

has fixed sign for:

```text
0 < t_1 < ... < t_N < 1.
```

Expected problem:

```text
q_1(t)=t-1/5
```

changes sign, and the determinant ratio appears not sign-definite.

If this route fails, record a controlled obstruction to a simple total-positivity proof.

### Route 4: Hankel difference structure

Rewrite:

```text
A = H1 - R H0
```

where:

```text
H0[k,j]=beta(k+j-1)
H1[k,j]=beta(k+j)
R=diag(r_k)
```

This identifies A as a row-dependent Christoffel/Hankel difference.

### Route 5: Pivot evidence extension

Extend determinant and pivot evidence from N=10 to N=12.

This is not proof, but it checks whether the theorem target remains plausible.

## Desired Outcome

A useful result is:

```text
Derivative factorization derived;
Andreief representation derived;
simple Chebyshev sign proof route rejected or retained;
Hankel difference structure derived;
det(A_N)>0 and pivots >0 extended through N=12;
all-order positivity still open unless proof closes.
```

Expected status:

```text
DETERMINANT_POSITIVITY_THEOREM_NOT_PROVEN
PROOF_ROUTE_REFINED
CHEBYSHEV_SIGN_ROUTE_BLOCKED
PIVOT_EVIDENCE_EXTENDED_N1_TO_N12
MOMENT_PAIRING_THEOREM_TARGET_RETAINED
```

## What This Group May Do

Group 90 may:

```text
derive derivative factorization;
derive Andreief determinant representation;
test sign-definiteness of q determinant;
derive Hankel difference structure;
extend exact determinant/pivot checks;
classify proof routes and next theorem target.
```

## What This Group Must Not Do

Group 90 must not:

```text
claim all-order determinant positivity from finite checks;
claim all-order local inertness;
claim hierarchy convergence;
claim full covariant geometry;
claim rho(y)=0;
erase next moments;
adopt an axiom;
write a parent field equation;
insert B_s/F_zeta;
solve D_layer legitimacy;
construct active O by label;
open recombination.
```

## Recommended Script Batch

```text
candidate_determinant_positivity_problem.py
candidate_derivative_factorization.py
candidate_andreief_representation.py
candidate_chebyshev_sign_route_test.py
candidate_hankel_difference_structure.py
candidate_pivot_evidence_extension_N1_to_N12.py
candidate_determinant_positivity_route_classifier.py
candidate_group_90_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_determinant_positivity_problem.py

Open Group 90 as a determinant positivity theorem attempt.

### 2. candidate_derivative_factorization.py

Derive:

```text
q_k(t) mu(t)
= -1/(k+3/2) (1-t)^3 d/dt[t^(k-1/2)(1-t)^2]
```

up to the exact coefficient convention.

This gives a Sturm/derivative structure behind the row constraints.

### 3. candidate_andreief_representation.py

Derive the Andreief determinant representation:

```text
det(A_N)
= 1/N! ∫ det[t_i^j] det[q_k(t_i)] ∏ mu(t_i) dt_i.
```

This gives a possible positivity route.

### 4. candidate_chebyshev_sign_route_test.py

Test whether the determinant of the `q_k` system is sign-definite.

Expected result:

```text
simple Chebyshev/sign route fails or remains unproven;
q determinant has sign complications.
```

This is valuable because it blocks a false easy proof.

### 5. candidate_hankel_difference_structure.py

Derive:

```text
A = H1 - R H0
```

and verify against the closed entry formula.

Interpretation:

```text
A is a row-dependent Hankel/Christoffel difference,
not a standard positive Hankel Gram matrix.
```

### 6. candidate_pivot_evidence_extension_N1_to_N12.py

Compute exact determinants and pivots through N=12.

Expected:

```text
all positive/nonzero.
```

This extends Group 89 evidence.

### 7. candidate_determinant_positivity_route_classifier.py

Classify:

```text
DERIVATIVE_FACTORIZATION_DERIVED
ANDREIEF_REPRESENTATION_DERIVED
SIMPLE_CHEBYSHEV_ROUTE_BLOCKED_OR_UNPROVEN
HANKEL_DIFFERENCE_STRUCTURE_DERIVED
PIVOT_EVIDENCE_EXTENDED_N1_TO_N12
ALL_ORDER_DETERMINANT_THEOREM_OPEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

### 8. candidate_group_90_status_summary.py

Close the group.

Expected result:

```text
determinant positivity not proven,
but proof target is sharpened and one naive proof route is rejected.
```

## Key Success Criteria

Group 90 must earn at least one of these:

```text
a real all-order proof;
or a sharper structural theorem target;
or a clear obstruction to a plausible proof route.
```

If no all-order proof is found, the group is still useful if it records:

```text
which proof routes failed and what theorem remains.
```

## Safe Handoff Options

Likely next groups:

```text
91_hierarchy_recurrence_search
91_biorthogonal_polynomial_construction
91_total_positivity_alternative_test
91_all_order_limit_obstruction
91_covariant_payload_suppression_lift
```

If Chebyshev route fails but derivative/Hankel structure remains promising, the best next group is probably:

```text
91_biorthogonal_polynomial_construction
```

or:

```text
91_hierarchy_recurrence_search
```

## Final Interpretation

Group 90 asks:

```text
Can the determinant goblin be killed,
or only named more precisely?
```

Goblin discipline:

```text
A failed proof route is not failure
if it keeps us from worshipping a painted door.
```
