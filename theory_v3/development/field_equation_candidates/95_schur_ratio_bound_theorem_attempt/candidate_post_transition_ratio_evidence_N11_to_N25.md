# candidate_post_transition_ratio_evidence_N11_to_N25 — Analysis Note

## Result

`candidate_post_transition_ratio_evidence_N11_to_N25.py` extends exact post-transition evidence through `N=25`.

For every `N=11..25`, the script finds:

```text
alpha_sign = 1
correction_sign = 1
schur_sign = 1
ratio_between_0_1 = True
gap_positive = True
```

It reports:

```text
post-transition failures: []
```

The derived ratios are all very close to `1` from below, including:

```text
N=11:
  ratio = 330317119701783540623243 /
          330317119824310367643531

N=25:
  ratio = 51850677319720290977702525996210646366350833979009305734767604727 /
          51850677319720290977702649451085071420469299186197803847319974903.
```

## Interpretation

This is the strongest finite evidence result of Group 95.

The post-transition pattern from Group 94 survives ten more orders:

```text
N=11..25:
  alpha > 0
  correction > 0
  schur > 0
  0 < correction/alpha < 1
  gap = 1 - correction/alpha > 0.
```

That supports the idea that the post-transition regime is stable. It does not prove it all-order, but it makes the next theorem target more credible.

## What Changed

The post-transition evidence extends from:

```text
N=11..15
```

to:

```text
N=11..25.
```

That is meaningful because the ratios are extremely close to one; small exact sign errors would likely show up if the pattern were fragile.

## What Did Not Change

This is finite evidence. It is not an all-order theorem.

## Carry-forward status

```text
POST_TRANSITION_RATIO_BOUND_SUPPORTED_N11_TO_N25
ALPHA_POSITIVE_N11_TO_N25
CORRECTION_POSITIVE_N11_TO_N25
SCHUR_POSITIVE_N11_TO_N25
GAP_POSITIVE_N11_TO_N25
ALL_ORDER_POST_TRANSITION_SIGN_THEOREMS_OPEN
```
