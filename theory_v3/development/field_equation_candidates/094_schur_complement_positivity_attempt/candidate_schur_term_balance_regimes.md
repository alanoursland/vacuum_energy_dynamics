# candidate_schur_term_balance_regimes — Updated Analysis Note

## Result

`candidate_schur_term_balance_regimes.py` decomposes:

```text
schur_N = alpha_N - correction_N.
```

It finds no regime failures through `N=15`.

The finite pattern is:

```text
N=1:
  base case;
  alpha_sign = 1;
  correction_sign = 0;
  schur_sign = 1.

N=2..10:
  alpha_sign = -1;
  correction_sign = -1;
  correction dominates;
  schur_sign = 1.

N=11..15:
  alpha_sign = 1;
  correction_sign = 1;
  alpha dominates;
  schur_sign = 1.
```

## Interpretation

This markdown does not need a mathematical correction. The result is exactly as expected.

The important point is that Schur positivity is no longer just a table of positive pivots. It has a visible two-regime mechanism:

```text
before N=11:
  negative correction overpowers negative alpha;

after N=11:
  positive alpha outruns positive correction.
```

This is a real structural refinement.

## Carry-forward status

```text
TWO_REGIME_SCHUR_BALANCE_SUPPORTED_N1_TO_N15
ALL_ORDER_DOMINANCE_RULE_OPEN
```
