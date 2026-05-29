# Matter Source Origin Gate 41: Boundary Flux Normalization Bridge

## Purpose

This proof links the weak proper-time boundary source coefficient to the
reduced A-sector flux ledger.

## Validated Checks

- linearized proper-time boundary variation gives F=M/(2K): passed
- target flux alpha*M fixes K=1/(2*alpha): passed
- with K=1/(2*alpha), boundary variation recovers F=alpha*M: passed
- for alpha=8*pi*G/c^2, K=c^2/(16*pi*G): passed

## Linearized Boundary Variation

From weak proper-time coupling, the matter boundary variation contributes:

```text
-M/2.
```

Let the vacuum boundary flux coefficient be:

```text
K F.
```

Stationarity gives:

```text
K F - M/2 = 0.
```

Therefore:

```text
F = M/(2K).
```

To match a target flux:

```text
F = alpha M,
```

one needs:

```text
K = 1/(2 alpha).
```

For the A-sector:

```text
alpha = 8*pi*G/c^2,
```

so:

```text
K = c^2/(16*pi*G).
```

## Gate Interpretation

The weak interval boundary source and A-sector flux ledger are compatible once
the vacuum action normalization is fixed. This is a bridge to the
vacuum-action-origin folder, not an independent derivation of the nonlinear
action.
