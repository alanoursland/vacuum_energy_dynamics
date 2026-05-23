# candidate_recurrence_candidate_holdout_test — Analysis Note

## Result

`candidate_recurrence_candidate_holdout_test.py` repeats the recurrence search with explicit training and holdout ranges.

The data split is:

```text
Training ratios:
  N=2..13

Holdout ratios:
  N=14..30
```

The result is:

```text
training candidates count = 0
passing holdout candidates = []
```

Governance records:

```text
no bounded candidate passed holdout;
bounded search only;
structural proof still required.
```

## Interpretation

This confirms the previous recurrence search result.

The issue is not that a candidate fit the training data but failed holdout. No candidate was found even in the bounded training search. So there is no degree-`<=4` rational ratio recurrence to carry forward.

This is a stronger negative result than a failed holdout alone.

## What Changed

The recurrence-search branch now has a controlled obstruction:

```text
LOW_DEGREE_RATIONAL_RECURRENCE_NOT_ESTABLISHED
```

or more specifically:

```text
NO_DEGREE_LE_4_RATIONAL_RATIO_CANDIDATE_FOUND_IN_TRAINING_RANGE
```

## What Did Not Change

This is still a bounded search. It does not rule out all recurrence structures.

## Steering Consequence

The next group should not just raise the degree a little and keep fitting. The better next route is structural:

```text
pivot sign theorem attempt;
biorthogonal pivot construction;
Hankel difference pivot analysis.
```
