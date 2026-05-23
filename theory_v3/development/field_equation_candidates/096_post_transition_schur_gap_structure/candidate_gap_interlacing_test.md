# candidate_gap_interlacing_test — Analysis Note

## Result

`candidate_gap_interlacing_test.py` tests the zig-zag/interlacing structure of the gap sequence.

It reports:

```text
odd->even increase failures: []
even->odd decrease failures: []
even peak bracket failures: []
```

Governance records:

```text
gap interlacing:
  supported through N=30

structure target:
  interlacing may explain one-step monotonicity failures.
```

## Interpretation

This result explains the apparent contradiction between Group 95 and Group 96.

Group 95 found that one-step monotonicity fails. Group 96 shows why:

```text
odd -> even:
  gap increases

even -> odd:
  gap decreases
```

So the gap sequence zig-zags. The even terms act as local peaks between neighboring odd terms in the tested range.

That means the failure of one-step monotonicity was not noise. It was evidence of interlacing structure.

## What Changed

The post-transition gap now has a plausible finite structure:

```text
within each parity branch:
  gap decreases

between branches:
  gap zig-zags / interlaces
```

This is a much sharper theorem target than simple positivity.

## What Did Not Change

Interlacing alone does not prove gap positivity. It needs base positivity and branch behavior.

## Carry-forward status

```text
GAP_INTERLACING_SUPPORTED_N11_TO_N30
ODD_TO_EVEN_GAP_INCREASE_SUPPORTED_N11_TO_N30
EVEN_TO_ODD_GAP_DECREASE_SUPPORTED_N11_TO_N30
EVEN_PEAK_BRACKET_SUPPORTED_N11_TO_N30
ALL_ORDER_INTERLACING_THEOREM_OPEN
```
