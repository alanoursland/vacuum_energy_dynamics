# 2. Endpoint Ladder Closed Status

## Claim

The general endpoint/contact ladder is closed:

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

## SymPy check

The script verifies

```text
Beta(k + 1/2, R + 2) / Beta(k - 1/2, R + 2)
  = (2k - 1)/(2k + 2R + 3).
```

## Ledger status

Closed as a scalar moment/contact ladder. What remains open is not the algebra
of the ladder, but whether a given physical reduction selects a particular
`R` without an extra projection embedding.
