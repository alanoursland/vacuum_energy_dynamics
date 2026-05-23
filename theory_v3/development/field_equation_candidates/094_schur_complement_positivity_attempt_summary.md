# Group 94 Summary: Schur Complement Positivity Attempt — Updated After Group 93 Patch

## Purpose

Group 94 confirms the patched Group 93 Schur-complement route and refines its positivity mechanism.

Group 93 now successfully derives:

```text
row-sign normalization;
positive row-signed leading pivots through N=30;
Schur-complement pivot identity through N=15.
```

Group 94 independently confirms the Schur identity and asks:

```text
Can row-signed Schur positivity be reduced to a more specific balance or ratio-bound theorem?
```

## Main Result

Group 94 is successful as a confirmation-and-refinement group.

Stable result:

```text
Schur complement pivot identity confirmed through N=15 after the Group 93 patch;

Schur pivots positive through N=15;

two-regime alpha/correction balance pattern supported through N=15;

correction/alpha ratio bound pattern supported through N=15;

all-order Schur positivity theorem remains open;

all-order ratio-bound theorem remains open;

all-order determinant nonzero theorem remains open;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What Changed From the Earlier Group 94 Markdown

The earlier markdown described Group 94 as repairing the failed Group 93 Schur route.

After the patched Group 93 rerun, the better framing is:

```text
Group 93 derives the Schur identity.
Group 94 confirms it and analyzes why the Schur pivots are positive.
```

This is mainly a wording/status-hygiene change. The mathematical content remains valid.

## What We Actually Learned

The Schur decomposition is:

```text
schur_N = alpha_N - correction_N

correction_N = v_row C^(-1) u

schur_N = det(B_N)/det(B_(N-1)).
```

The finite two-regime pattern is:

```text
N=1:
  base positive case.

N=2..10:
  alpha < 0;
  correction < 0;
  |correction| > |alpha|;
  therefore alpha - correction > 0.

N=11..15:
  alpha > 0;
  correction > 0;
  alpha > correction;
  therefore alpha - correction > 0.
```

Equivalently, for:

```text
r_N = correction_N / alpha_N
```

Group 94 supports:

```text
2 <= N <= 10:
  r_N > 1

N >= 11:
  0 < r_N < 1
```

through `N=15`.

## Strategic Interpretation

Group 94 turns the Schur positivity theorem into a sharper inequality target.

The next real theorem target is not vague:

```text
prove all row-signed Schur pivots are positive.
```

It is more specific:

```text
prove the two-regime correction/alpha ratio bounds.
```

Because `2 <= N <= 10` is finite, the main all-order burden is the post-transition bound:

```text
0 < correction_N / alpha_N < 1 for all N >= 11.
```

## Final Status Ledger

```text
Schur_identity:
  CONFIRMED_THROUGH_N15

Schur_pivots:
  POSITIVE_THROUGH_N15

Schur_term_balance:
  TWO_REGIME_PATTERN_SUPPORTED_N1_TO_N15

Schur_ratio_bound:
  SUPPORTED_N2_TO_N15

ratio_pattern:
  r_N > 1 for 2<=N<=10
  0 < r_N < 1 for N=11..15

all_order_Schur_positivity:
  OPEN

all_order_ratio_bound:
  OPEN

all_order_determinant_nonzero:
  OPEN

parent_divergence:
  NOT_PROVEN

recombination:
  BLOCKED
```

## Recommended Next Group

Best next group:

```text
95_schur_ratio_bound_theorem_attempt
```

Purpose:

```text
try to prove or further reduce the post-transition inequality:
  0 < correction_N / alpha_N < 1 for all N >= 11.
```

Other viable routes:

```text
95_biorthogonal_pivot_construction
95_hankel_difference_pivot_analysis
95_all_order_limit_obstruction
95_covariant_payload_suppression_lift
```

## Final Interpretation

Group 94 remains good.

```text
Group 93 fixed the Schur door.
Group 94 checked the hinge and found the race:
before eleven, negative correction wins;
after eleven, positive alpha wins.

Now prove the race cannot flip again.
```
