# candidate_sign_normalized_pivot_sequence — Analysis Note

## Result

`candidate_sign_normalized_pivot_sequence.py` computes the sign-normalized pivots:

```text
pi_N = p_N   for N <= 10
pi_N = -p_N  for N >= 11
```

The script verifies:

```text
normalization failures through N=30: []
```

and every reported normalized pivot sign is:

```text
pi_sign = +1
```

for:

```text
N=1..30.
```

The first examples are:

```text
N=1:
  pi_N = 512/225225

N=2:
  pi_N = 8192/5360355

N=10:
  pi_N = 342634211494068224/148779328325489141800078233675

N=11:
  pi_N = 62733735434387456/1745087425296664138166337601411125
```

## Interpretation

This is the best positive result in Group 92.

Raw pivot positivity is false after `N=10`, but sign-normalized pivot positivity is supported through `N=30`.

So the corrected all-order theorem target is:

```text
pi_N > 0 for all N.
```

That is cleaner than tracking alternating determinant signs directly.

## What Changed

The determinant sign-pattern theorem now has a compact equivalent target:

```text
prove sign-normalized pivots are positive.
```

This is a better theorem target than raw determinant sign.

## What Did Not Change

The result is finite evidence.

It does not prove:

```text
pi_N > 0 for all N.
```

It also does not explain why the sign transition occurs at `N=11`.

## Steering Consequence

The next question is whether the normalized pivots obey a simple recurrence. The group tests that next, and the answer appears to be no under the bounded search.
