# 4. Species count import gate

## Claim

Stress additivity does not determine how many species exist.

## Check

For three independent species the source ledger is additive:

```text
T_3 = m1 + m2 + m3
T_2 + m3 = m1 + m2 + m3
T_3 - (T_2 + m3) = 0
```

But no algebraic condition here fixes `N`, the number of species.

## Status

Universal metric coupling is compatible with arbitrary species number; species
existence and classification remain external to stress variation.
