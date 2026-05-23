# candidate_interlacing_difference_signs — Analysis Note

## Result

`candidate_interlacing_difference_signs.py` tests exact even-peak interlacing differences:

```text
gap_(N+1) - gap_N > 0
gap_(N+1) - gap_(N+2) > 0
```

for odd `N`.

It reports:

```text
left failures: []
right failures: []
bracket failures: []
```

Displayed checkpoints all have positive signs, including:

```text
N=11, even=12, next=13:
  left_sign = 1
  right_sign = 1

N=33, even=34, next=35:
  left_sign = 1
  right_sign = 1.
```

Governance records:

```text
interlacing differences:
  positive through N=35.
```

## Interpretation

This is the second major successful result of Group 97.

Group 96 found a zig-zag pattern. Group 97 turns that into exact difference positivity:

```text
even gap term is larger than the odd term before it;
even gap term is larger than the odd term after it.
```

So the even terms are local peaks in the tested post-transition gap sequence.

This explains why simple one-step monotonicity fails:

```text
odd -> even:
  gap rises

even -> odd:
  gap falls.
```

The failure is not disorder. It is interlacing.

## Carry-forward status

```text
INTERLACING_LEFT_DIFFERENCES_POSITIVE_THROUGH_N35
INTERLACING_RIGHT_DIFFERENCES_POSITIVE_THROUGH_N35
EVEN_PEAK_INTERLACING_SUPPORTED_THROUGH_N35
ALL_ORDER_INTERLACING_DIFFERENCE_POSITIVITY_OPEN
```
