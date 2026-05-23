# Group 95 Summary: Schur Ratio Bound Theorem Attempt

## Purpose

Group 95 attempted to sharpen the Group 94 Schur ratio-bound target.

Group 94 had found a finite post-transition pattern:

```text
r_N = correction_N / alpha_N

0 < r_N < 1
```

for `N=11..15`.

Group 95 asked:

```text
Is the ratio bound a new proof handle,
or is it just Schur positivity rewritten?
```

## Main Result

Group 95 is successful as a theorem-target clarification group.

Stable result:

```text
ratio-bound equivalence derived;

for alpha_N > 0,
  0 < correction_N/alpha_N < 1
is equivalent to:
  correction_N > 0
  schur_N = alpha_N - correction_N > 0;

post-transition ratio-bound evidence extended through N=25;

alpha_N, correction_N, schur_N, ratio_N, and gap_N are positive/in-range through N=25;

Schur gap g_N = 1-r_N = schur_N/alpha_N is positive through N=25;

simple gap monotonicity is not established;

simple ratio monotonicity is not established;

ratio route is mostly a repackaging of Schur positivity as gap positivity under alpha_N > 0;

all-order ratio-bound theorem remains open;

all-order Schur positivity theorem remains open;

all-order determinant nonzero theorem remains open;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What We Actually Learned

The most important result is the equivalence:

```text
1 - correction/alpha = (alpha - correction)/alpha = schur/alpha.
```

Therefore, in the post-transition regime where `alpha > 0`:

```text
0 < correction/alpha < 1
```

does not avoid Schur positivity. It asks for:

```text
correction > 0
schur > 0.
```

So the ratio route is not an independent shortcut. It is a useful reformulation only if the gap:

```text
gap_N = schur_N / alpha_N
```

is easier to prove positive.

## Script-Level Analysis

### 1. Ratio Bound Problem

The opener correctly frames the group as an attempt to test whether the ratio bound reduces to exact sign/gap conditions.

It also preserves the boundaries:

```text
finite evidence is not theorem;
raw determinant positivity remains false;
parent equation jump forbidden.
```

### 2. Ratio Bound Equivalence

The script proves symbolically:

```text
1 - correction/alpha = schur/alpha.
```

It also finds:

```text
finite equivalence failures N=11..25: []
```

Interpretation:

```text
the ratio route is equivalent to correction positivity plus Schur/gap positivity under alpha>0.
```

### 3. Post-Transition Ratio Evidence N11 to N25

The script extends exact post-transition evidence from `N=15` to `N=25`.

For every `N=11..25`:

```text
alpha_sign = 1;
correction_sign = 1;
schur_sign = 1;
ratio_between_0_1 = True;
gap_positive = True.
```

There are:

```text
post-transition failures: []
```

Interpretation:

```text
the post-transition regime remains stable through N=25.
```

### 4. Ratio Gap Structure Probe

The script confirms:

```text
positive gap failures: []
```

but finds monotonicity failures:

```text
gap decreasing failures:
  (11,12), (13,14), ..., (23,24)

ratio increasing failures:
  (11,12), (13,14), ..., (23,24).
```

Interpretation:

```text
gap positivity remains supported,
but simple one-step monotonicity is not the proof.
```

The alternating failure pattern suggests a possible parity-split structure.

### 5. Ratio Route Simplification Audit

The classifier records:

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

This is accurate.

### 6. Group Status Summary

The final generated summary is mostly correct. The human interpretation should add the monotonicity obstruction from the gap probe:

```text
simple gap monotonicity is not established;
simple ratio monotonicity is not established.
```

## Final Status Ledger

```text
ratio_bound_equivalence:
  DERIVED

post_transition_ratio_bound:
  SUPPORTED_N11_TO_N25

post_transition_alpha:
  POSITIVE_N11_TO_N25

post_transition_correction:
  POSITIVE_N11_TO_N25

post_transition_schur:
  POSITIVE_N11_TO_N25

Schur_gap:
  POSITIVE_N11_TO_N25

simple_gap_monotonicity:
  NOT_ESTABLISHED

simple_ratio_monotonicity:
  NOT_ESTABLISHED

ratio_route:
  REPACKAGING_PLUS_GAP_TARGET

all_order_ratio_bound:
  OPEN

all_order_Schur_positivity:
  OPEN

all_order_determinant_nonzero:
  OPEN

parent_divergence:
  NOT_PROVEN

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 95 rejects:

```text
ratio route as independent proof of Schur positivity;
finite N=25 evidence as all-order theorem;
simple one-step monotonic gap proof;
simple one-step monotonic ratio proof;
raw determinant positivity revival;
parent equation jump;
recombination opening.
```

## Strategic Interpretation

Group 95 is useful because it prevents a false sense of progress.

The ratio bound looked like a sharper theorem target, and it still is useful. But it is not a separate door. It is the same Schur door with a smaller keyhole.

The real post-transition theorem target is now:

```text
prove alpha_N > 0,
prove correction_N > 0,
prove gap_N = schur_N/alpha_N > 0,
for all N >= 11.
```

Since simple monotonicity failed, the next route should probably test parity-split gap structure or attack the signs of alpha, correction, and gap directly.

## Recommended Next Group

Best next group:

```text
96_post_transition_schur_gap_structure
```

Purpose:

```text
test whether gap_N has separate even/odd monotonic or positivity structure after N=11.
```

Alternative:

```text
96_alpha_correction_sign_theorem_attempt
```

Purpose:

```text
try to prove alpha_N>0 and correction_N>0 post-transition.
```

My recommendation is:

```text
96_post_transition_schur_gap_structure
```

because Group 95 found a clear clue: monotonicity fails exactly on alternating transitions, suggesting parity structure.

## Final Interpretation

Group 95 found out what kind of key the ratio is.

```text
The ratio key does not open a new door.
It points to the same Schur lock.

But the scratches on the key are useful:
the gap stays positive through twenty-five,
yet it wiggles by parity.

Next goblin move:
split the footprints into even and odd trails.
```
