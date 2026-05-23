# Group 96 Summary: Post-Transition Schur Gap Structure

## Purpose

Group 96 followed the main clue from Group 95.

Group 95 showed:

```text
gap_N = 1 - r_N = schur_N / alpha_N
```

is positive through `N=25`, but simple one-step monotonicity failed on alternating transitions.

Group 96 asked:

```text
Does the post-transition Schur gap have parity-split structure?
```

## Main Result

Group 96 is successful as a structure-finding group.

Stable result:

```text
post-transition gap positivity and ratio bound extended through N=30;

odd/even gap and ratio branches isolated;

odd gap branch decreases through N=30;

even gap branch decreases through N=30;

odd ratio branch increases through N=30;

even ratio branch increases through N=30;

gap interlacing / zig-zag structure supported through N=30;

simple one-step monotonicity remains blocked;

all-order parity gap theorem remains open;

all-order ratio-bound theorem remains open;

all-order Schur positivity theorem remains open;

all-order determinant nonzero theorem remains open;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What We Actually Learned

Group 96 explains the Group 95 monotonicity failure.

The gap sequence is not simply monotone one step at a time. Instead, it behaves like two interlaced monotone subsequences:

```text
odd branch:
  gap_11, gap_13, gap_15, ...
  decreases

even branch:
  gap_12, gap_14, gap_16, ...
  decreases
```

The ratio behaves oppositely:

```text
odd branch:
  ratio_11, ratio_13, ratio_15, ...
  increases

even branch:
  ratio_12, ratio_14, ratio_16, ...
  increases
```

The interlacing test also passes:

```text
odd -> even:
  gap increases

even -> odd:
  gap decreases

even terms act as local peaks between neighboring odd terms.
```

This converts the failed one-step monotonicity route into a more precise parity-branch theorem target.

## Script-Level Analysis

### 1. Gap Structure Problem

The opener correctly imports the Group 95 clue:

```text
simple monotonicity failed on alternating transitions.
```

It opens the right test:

```text
split odd/even branches and test interlacing.
```

### 2. Parity Gap Sequence Probe

The script extends post-transition evidence through `N=30`.

It reports:

```text
positive/range failures: []
```

and isolates odd/even branches.

Interpretation:

```text
gap positivity and ratio bounds remain stable through N=30.
```

### 3. Parity Monotonicity Test

The script reports:

```text
odd gap decreasing failures: []
even gap decreasing failures: []
odd ratio increasing failures: []
even ratio increasing failures: []
```

Interpretation:

```text
parity-branch monotonicity is strongly supported through N=30.
```

### 4. Gap Interlacing Test

The script reports:

```text
odd->even increase failures: []
even->odd decrease failures: []
even peak bracket failures: []
```

Interpretation:

```text
the gap has a clean zig-zag/interlacing pattern through N=30.
```

### 5. Parity Theorem Target Classifier

The classifier correctly preserves:

```text
all-order parity theorem open;
all-order ratio-bound theorem open;
all-order Schur positivity theorem open;
all-order determinant nonzero open.
```

It should be read with the stronger human interpretation that parity monotonicity and interlacing were supported, not merely tested.

### 6. Group Status Summary

The generated summary is safe and correct, but conservative. The interpretation should explicitly carry forward the positive parity findings.

## Final Status Ledger

```text
post_transition_gap:
  POSITIVE_N11_TO_N30

post_transition_ratio_bound:
  SUPPORTED_N11_TO_N30

odd_gap_branch:
  DECREASING_N11_TO_N29

even_gap_branch:
  DECREASING_N12_TO_N30

odd_ratio_branch:
  INCREASING_N11_TO_N29

even_ratio_branch:
  INCREASING_N12_TO_N30

gap_interlacing:
  SUPPORTED_N11_TO_N30

simple_one_step_monotonicity:
  BLOCKED

all_order_parity_gap_theorem:
  OPEN

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

Group 96 rejects:

```text
finite parity evidence as theorem;
finite interlacing evidence as theorem;
restoring simple one-step monotonicity;
gap positivity from interlacing alone;
parent equation jump;
recombination opening.
```

## Strategic Interpretation

Group 96 is a strong progress group.

It takes a failure from Group 95 and turns it into structure. The gap was not failing monotonicity randomly. It was hiding an even/odd split.

The next theorem attempt should not return to unsplit monotonicity. It should attack the parity-split structure directly.

## Recommended Next Group

Best next group:

```text
97_parity_gap_theorem_attempt
```

Purpose:

```text
try to prove or reduce:
  odd gap branch decreasing;
  even gap branch decreasing;
  odd ratio branch increasing;
  even ratio branch increasing;
  gap interlacing.
```

Alternative:

```text
97_even_odd_schur_asymptotic_probe
```

if the direct theorem attempt is too hard.

## Final Interpretation

Group 96 found the goblin trail.

```text
The footprints did not march in one line.
They alternated left, right, left, right.

Sorted by foot,
each trail behaves.

Now the theorem hunt has a shape.
```
