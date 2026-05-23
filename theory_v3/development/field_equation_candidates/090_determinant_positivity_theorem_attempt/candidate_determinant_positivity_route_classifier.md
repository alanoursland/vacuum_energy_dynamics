# candidate_determinant_positivity_route_classifier — Analysis Note

## Result

`candidate_determinant_positivity_route_classifier.py` records these statuses:

```text
DERIVATIVE_FACTORIZATION_DERIVED
ANDREIEF_REPRESENTATION_DERIVED
SIMPLE_CHEBYSHEV_SIGN_ROUTE_BLOCKED
HANKEL_DIFFERENCE_STRUCTURE_DERIVED
PIVOT_EVIDENCE_EXTENDED_N1_TO_N12
ALL_ORDER_DETERMINANT_THEOREM_NOT_PROVEN
PROOF_TARGET_REFINED
ALL_ORDER_LIMIT_OPEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

But this classifier is partly inconsistent with the raw pivot-extension output.

The raw pivot-extension result shows:

```text
N=11:
  det(A_N)>0? False
  pivot>0? False

N=12:
  det(A_N)>0? True
  pivot>0? False
```

Therefore the classifier status:

```text
PIVOT_EVIDENCE_EXTENDED_N1_TO_N12:
  determinants and pivots positive through N=12
```

is incorrect.

## Interpretation

The classifier needs a status correction before being carried forward.

Correct carry-forward statuses should be:

```text
DERIVATIVE_FACTORIZATION_DERIVED

ANDREIEF_REPRESENTATION_DERIVED

SIMPLE_CHEBYSHEV_SIGN_ROUTE_BLOCKED_OR_UNPROVEN

HANKEL_DIFFERENCE_STRUCTURE_DERIVED

DETERMINANT_POSITIVITY_DISPROVEN_BY_N11

PIVOT_POSITIVITY_DISPROVEN_BY_N11

DETERMINANT_NONZERO_VERIFIED_N1_TO_N12

INVERTIBILITY_THEOREM_OPEN

DETERMINANT_SIGN_PATTERN_OPEN

ALL_ORDER_LIMIT_OPEN

PARENT_DIVERGENCE_UNPROVEN

RECOMBINATION_BLOCKED
```

This is not a minor wording issue. Statuses from classifiers carry forward and affect later results. The positivity failure at `N=11` changes the theorem target.

## What Changed

The determinant route is retargeted.

The project should no longer pursue:

```text
det(A_N)>0 for all N.
```

It should pursue:

```text
det(A_N)!=0 for all N
```

and:

```text
understand determinant sign changes.
```

## What Did Not Change

The derivative, Andreief, and Hankel structures remain useful. The Chebyshev route remains blocked/unproven. Parent divergence and recombination remain blocked.

## Steering Consequence

This classifier should be patched or superseded by the markdown summary before future groups depend on it. The next group should audit sign pattern and nonzero/invertibility rather than positivity.
