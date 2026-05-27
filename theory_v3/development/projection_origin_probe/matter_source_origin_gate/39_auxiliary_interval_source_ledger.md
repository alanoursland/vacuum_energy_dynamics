# Matter Source Origin Gate 39: Auxiliary Interval Source Ledger

## Purpose

This proof checks what happens if an auxiliary residual/projection variable is
allowed to enter the matter interval.

## Validated Checks

- auxiliary interval coupling gives zeta an explicit matter source: passed
- alpha=0 removes matter source from the auxiliary field: passed
- if alpha is nonzero, zeta requires its own source ledger: passed

## Setup

Let:

```text
A_eff = A + alpha zeta
E = F_A A + F_z zeta - M sqrt(A_eff).
```

Then:

```text
dE/dA    = F_A - M/(2 sqrt(A_eff))
dE/dzeta = F_z - alpha M/(2 sqrt(A_eff)).
```

## Consequence

If:

```text
alpha != 0,
```

then `zeta` is explicitly matter-coupled. It is no longer hidden projection
bookkeeping or a neutral residual. It needs its own source ledger.

The decoupled route is:

```text
alpha = 0,
```

which removes the matter source term from the auxiliary variation.

## Gate Interpretation

An auxiliary field can be coupled to the interval only by promoting it to an
explicit matter-coupled physical field. Otherwise it must remain outside the
interval seen by matter.
