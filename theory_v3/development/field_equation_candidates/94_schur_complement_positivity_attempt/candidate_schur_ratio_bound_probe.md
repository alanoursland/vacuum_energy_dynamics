# candidate_schur_ratio_bound_probe — Updated Analysis Note

## Result

`candidate_schur_ratio_bound_probe.py` probes:

```text
r_N = correction_N / alpha_N.
```

The finite pattern is confirmed through `N=15`:

```text
N=2..10:
  r_N > 1

N=11..15:
  0 < r_N < 1
```

The script reports:

```text
ratio failures: []
```

Examples include:

```text
N=2:
  r_N = 17

N=10:
  r_N = 46298598011025272857 / 46297928803580948505

N=11:
  r_N = 330317119701783540623243 / 330317119824310367643531

N=15:
  r_N = 1239990394325203866716465211610424707 /
        1239990394325306407609128140108916099.
```

## Interpretation

This remains the sharpest theorem-target refinement in Group 94.

The all-order Schur positivity problem can now be approached through a specific two-regime ratio-bound target:

```text
prove r_N > 1 for 2 <= N <= 10;
prove 0 < r_N < 1 for N >= 11.
```

Since the first range is finite, the real all-order burden is mostly the post-transition inequality:

```text
0 < r_N < 1 for all N >= 11.
```

## Carry-forward status

```text
SCHUR_RATIO_BOUND_SUPPORTED_N2_TO_N15
POST_TRANSITION_RATIO_BOUND_OPEN
ALL_ORDER_RATIO_BOUND_THEOREM_OPEN
```
