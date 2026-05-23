# candidate_ratio_route_simplification_audit — Analysis Note

## Result

`candidate_ratio_route_simplification_audit.py` classifies the Group 95 result.

Stable statuses:

```text
RATIO_BOUND_EQUIVALENCE_DERIVED

POST_TRANSITION_RATIO_BOUND_SUPPORTED_N11_TO_N25

SCHUR_GAP_POSITIVE_N11_TO_N25

RATIO_ROUTE_IS_REPACKAGING_PLUS_GAP_TARGET

ALL_ORDER_RATIO_BOUND_THEOREM_OPEN

ALL_ORDER_SCHUR_POSITIVITY_THEOREM_OPEN

ALL_ORDER_DETERMINANT_NONZERO_OPEN

PARENT_DIVERGENCE_UNPROVEN

RECOMBINATION_BLOCKED
```

The governance section says:

```text
ratio equivalence:
  derived

post-transition evidence:
  extended through N=25

route simplification:
  ratio route mostly repackages Schur positivity as gap positivity under alpha>0
```

The unresolved obligations are:

```text
prove alpha_N > 0 for N>=11;
prove correction_N > 0 for N>=11;
prove gap_N = schur_N/alpha_N > 0 for N>=11.
```

## Interpretation

This classifier is accurate.

Group 95 did not prove the ratio theorem. It clarified what the ratio theorem actually asks for.

The ratio route is useful as a bookkeeping and targeting device, but not as an independent proof route unless the gap/sign conditions are easier to prove structurally.

The strongest next target is probably:

```text
post-transition alpha/correction/gap sign theorem
```

with special attention to the parity structure revealed by the gap probe.

## What Changed

The theorem path is now clearer:

```text
ratio bound
-> alpha positive + correction positive + gap positive
-> maybe parity-split gap positivity.
```

## What Did Not Change

All all-order theorem claims remain open. Parent divergence remains unproven. Recombination remains blocked.

## Carry-forward status

```text
RATIO_ROUTE_IS_REPACKAGING_PLUS_GAP_TARGET
POST_TRANSITION_ALPHA_SIGN_OPEN
POST_TRANSITION_CORRECTION_SIGN_OPEN
POST_TRANSITION_GAP_SIGN_OPEN
ALL_ORDER_RATIO_BOUND_THEOREM_OPEN
```
