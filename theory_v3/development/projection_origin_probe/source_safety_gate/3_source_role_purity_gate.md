# Source Safety Gate 3: Ordinary Source Role-Purity

## Purpose

This proof formalizes the ordinary-source count-once condition:

```text
i_A + i_Bs + i_zeta + i_kappa = 1.
```

It then isolates the ordinary A-sector route:

```text
i_A = 1
i_Bs = i_zeta = i_kappa = 0.
```

## Symbolic Setup

The source duplication/missing-entry load is:

```text
S_source * (i_A + i_Bs + i_zeta + i_kappa - 1).
```

## Exhaustive Binary Check

| i_A | i_Bs | i_zeta | i_kappa | source_error | status | role |
|---:|---:|---:|---:|---:|---|---|
| 0 | 0 | 0 | 0 | -1 | missing source | source disappears |
| 0 | 0 | 0 | 1 | 0 | count-once | single non-A route; not ordinary A-source |
| 0 | 0 | 1 | 0 | 0 | count-once | single non-A route; not ordinary A-source |
| 0 | 0 | 1 | 1 | 1 | duplicate source | ordinary source duplicated |
| 0 | 1 | 0 | 0 | 0 | count-once | single non-A route; not ordinary A-source |
| 0 | 1 | 0 | 1 | 1 | duplicate source | ordinary source duplicated |
| 0 | 1 | 1 | 0 | 1 | duplicate source | ordinary source duplicated |
| 0 | 1 | 1 | 1 | 2 | duplicate source | ordinary source duplicated |
| 1 | 0 | 0 | 0 | 0 | count-once | ordinary A-only source route |
| 1 | 0 | 0 | 1 | 1 | duplicate source | ordinary source duplicated |
| 1 | 0 | 1 | 0 | 1 | duplicate source | ordinary source duplicated |
| 1 | 0 | 1 | 1 | 2 | duplicate source | ordinary source duplicated |
| 1 | 1 | 0 | 0 | 1 | duplicate source | ordinary source duplicated |
| 1 | 1 | 0 | 1 | 2 | duplicate source | ordinary source duplicated |
| 1 | 1 | 1 | 0 | 2 | duplicate source | ordinary source duplicated |
| 1 | 1 | 1 | 1 | 3 | duplicate source | ordinary source duplicated |

## Result

There are four count-once placements at pure incidence level. Only one is the
ordinary A-sector source route:

```text
(i_A, i_Bs, i_zeta, i_kappa) = (1, 0, 0, 0).
```

Routes with more than one active incidence duplicate the ordinary source.
Routes with no active incidence lose the ordinary source.

## Gate Status

This proves role-purity as bookkeeping. It does not derive why matter enters
the A-sector; it states the condition a clean matter-source theorem must meet.
