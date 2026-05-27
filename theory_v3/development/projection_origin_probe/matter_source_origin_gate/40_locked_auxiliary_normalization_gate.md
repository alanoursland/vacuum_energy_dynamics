# Matter Source Origin Gate 40: Locked Auxiliary Normalization Gate

## Purpose

This proof checks the case where an auxiliary interval channel is not
independent but is locked to the metric interval.

## Validated Checks

- locked auxiliary interval rescales the matter source coefficient: passed
- weak renormalization is 1 + alpha*lambda/2: passed
- standard normalization is preserved when alpha*lambda=0: passed
- nonzero locked product changes the source normalization: passed

## Setup

Suppose:

```text
zeta = lambda A
A_eff = A + alpha zeta
      = (1 + alpha lambda) A.
```

The matter action is:

```text
S_m = -M sqrt(A_eff).
```

Compared to the standard interval source coefficient, the variation is scaled
by:

```text
sqrt(1 + alpha lambda).
```

For weak `alpha lambda`:

```text
sqrt(1 + alpha lambda) = 1 + alpha lambda/2 + ...
```

## Gate Interpretation

Locking an auxiliary channel to the interval does not make it invisible. It
renormalizes the matter source coefficient unless:

```text
alpha lambda = 0.
```

Any nonzero locked auxiliary coupling must therefore be explicit in the source
normalization.
