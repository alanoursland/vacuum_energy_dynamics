# candidate_ratio_gap_structure_probe — Analysis Note

## Result

`candidate_ratio_gap_structure_probe.py` studies:

```text
gap_N = 1 - r_N = schur_N / alpha_N
```

for `N=11..25`.

It reports:

```text
positive gap failures: []
```

So:

```text
gap_N > 0
```

holds through `N=25`.

However, simple monotonicity is not established. The script reports multiple failures for both:

```text
gap decreasing
ratio increasing
```

The failures occur in an alternating pattern:

```text
gap decreasing failures:
  (11,12), (13,14), (15,16), ..., (23,24)

ratio increasing failures:
  (11,12), (13,14), (15,16), ..., (23,24)
```

## Interpretation

This is the most useful negative result in Group 95.

The gap is positive through `N=25`, but it is not simply decreasing across every step. The ratio is not simply increasing across every step either.

That blocks a tempting easy proof route:

```text
show the gap is positive at N=11 and monotonically decreases to zero.
```

The gap does not behave that simply.

But the failure pattern is also suggestive. The monotonicity failures occur across odd-to-even transitions:

```text
11 -> 12
13 -> 14
15 -> 16
...
```

This hints that the gap/ratio may have parity-split structure. The next theorem attempt should consider even and odd subsequences separately instead of looking for one-step monotonicity.

## What Changed

The proof target is refined again.

Old possible route:

```text
prove simple monotonic gap/ratio behavior.
```

Corrected route:

```text
gap positivity remains live;
simple one-step monotonicity is not established;
parity-split gap structure may be the next target.
```

## What Did Not Change

Gap positivity remains supported through `N=25`.

## Carry-forward status

```text
SCHUR_GAP_POSITIVE_N11_TO_N25
SIMPLE_GAP_MONOTONICITY_NOT_ESTABLISHED
SIMPLE_RATIO_MONOTONICITY_NOT_ESTABLISHED
PARITY_SPLIT_GAP_STRUCTURE_SUGGESTED
```
