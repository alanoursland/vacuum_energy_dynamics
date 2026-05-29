# Matter Source Origin Gate 11: Zero-Monopole Auxiliary Source Silence

## Purpose

This proof records the allowed way an auxiliary source-like object can remain
safe in the A-sector:

```text
it may have internal shape,
but its ordinary mass monopole must vanish.
```

## Validated Checks

- chosen auxiliary source has zero radial monopole: passed
- auxiliary source is not pointwise zero and has nonzero shape moment: passed
- zero-monopole auxiliary source gives no exterior A flux shift: passed
- adding the auxiliary source leaves enclosed ordinary mass unchanged: passed

## Witness

Use the compact interior shape:

```text
H(r) = r^2 - (3/5)R^2.
```

It is not zero as a function. Its higher shape moment is:

```text
4*pi integral_0^R H r^4 dr = 16*pi*R**7/175.
```

But its radial monopole vanishes:

```text
4*pi integral_0^R H r^2 dr = 0.
```

Therefore adding `epsilon H` to an A-sector source produces no exterior mass
flux shift:

```text
Delta F_A = (8*pi*G/c^2) epsilon integral H dV = 0.
```

## Gate Interpretation

This gives a precise safety condition for any residual or projection-derived
source candidate: it may only enter the A-sector without changing ordinary
mass if its routed monopole is zero. Otherwise it duplicates or shifts the
ordinary source ledger.
