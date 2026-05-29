# 1. `r_k` Closed Status

## Claim

The original coefficient is closed as a moment-kernel/admissibility coefficient:

```text
r_k = (2k - 1)/(2k + 3).
```

## SymPy check

For the base moment functional

```text
C_0[P] = ∫_0^1 P(y) (1-y)y^(-1/2) dy,
```

the monomial ratio is

```text
Beta(k + 1/2, 2) / Beta(k - 1/2, 2)
  = (2k - 1)/(2k + 3).
```

## Ledger status

Closed. This coefficient no longer needs to be treated as mysterious or
speculative. It is the `R=0` scalar boundary/admissibility moment coefficient.
