# candidate_boundary_selection_rule_probe — Analysis Note

## Result

`candidate_boundary_selection_rule_probe.py` tests formal selection rules against source-vector signature classes.

Important rule summaries:

```text
ENDPOINT_VANISHING_p_ge_1:
  ALL_NEGATIVE: 7
  LEADING_POSITIVE_THEN_NEGATIVE: 11
  MULTI_OR_MIXED_FLIP_1: 9
  MULTI_OR_MIXED_FLIP_0: 1

SMOOTH_ENDPOINT_p_ge_2:
  ALL_NEGATIVE: 6
  LEADING_POSITIVE_THEN_NEGATIVE: 9
  MULTI_OR_MIXED_FLIP_1: 6

CENTER_SUPPRESSED_q_ge_1:
  LEADING_POSITIVE_THEN_NEGATIVE: 13
  MULTI_OR_MIXED_FLIP_1: 13
  MULTI_OR_MIXED_FLIP_0: 1
  ALL_NEGATIVE: 3

BALANCED_p_ge_q:
  ALL_NEGATIVE: 8
  MULTI_OR_MIXED_FLIP_0: 1
  LEADING_POSITIVE_THEN_NEGATIVE: 6

BALANCED_p_ge_q_minus_1:
  ALL_NEGATIVE: 8
  LEADING_POSITIVE_THEN_NEGATIVE: 11
  MULTI_OR_MIXED_FLIP_0: 1

ENDPOINT_CONCENTRATED_q_gt_p_plus_1:
  LEADING_POSITIVE_THEN_NEGATIVE: 2
  MULTI_OR_MIXED_FLIP_1: 13

LOW_Q_q_le_1:
  ALL_NEGATIVE: 8
  LEADING_POSITIVE_THEN_NEGATIVE: 1
  MULTI_OR_MIXED_FLIP_0: 1.
```

Governance records:

```text
balanced rules:
  p>=q and low-q rules favor all-negative/simple signatures

endpoint concentration:
  q>p+1 favors leading-positive/mixed signatures

physical boundary:
  no rule selected physically.
```

## Interpretation

This is the central analytic result of Group 103.

The rule probe shows a clean formal division:

```text
balanced / low-q rules:
  favor all-negative or simple signatures

endpoint-concentrated q>p+1 rules:
  strongly favor leading-positive or multi-flip signatures.
```

The most important negative result is that endpoint vanishing alone is not enough. `p>=1` and `p>=2` still include many leading-positive and mixed cases. The source behavior depends on the balance between `p` and `q`, not just endpoint smoothness.

So the useful selector is not:

```text
make the source vanish at x=1.
```

The better formal selector is something like:

```text
avoid excessive endpoint concentration by requiring p >= q,
p >= q-1,
or low q.
```

## What It Does Not Prove

No formal rule is selected physically.

The rule probe explains trends but does not derive a boundary condition from the postulates or field equations.

## Carry-forward status

```text
BOUNDARY_SELECTION_RULE_PROBE_COMPLETE
BALANCED_RULES_FAVOR_SIMPLE_SIGNATURES
LOW_Q_RULE_FAVORS_ALL_NEGATIVE_SIGNATURES
ENDPOINT_CONCENTRATION_FAVORS_MIXED_SIGNATURES
ENDPOINT_VANISHING_ALONE_NOT_SUFFICIENT
PHYSICAL_BOUNDARY_RULE_NOT_SELECTED
```
