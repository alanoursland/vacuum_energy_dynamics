# Vacuum Dimension Selector 16: Lovelock Order Dimension Table

## Purpose

This proof records the dimension status of Lovelock densities.

## Rule Checked

For Lovelock order `p` in spacetime dimension `D`:

```text
D < 2p  -> term vanishes
D = 2p  -> term is topological
D > 2p  -> term can be dynamical
```

## Validated Table

| D | p=0 | p=1 | p=2 | p=3 |
|---:|---|---|---|---|
| 2 | dynamical | topological | vanishes | vanishes |
| 3 | dynamical | dynamical | vanishes | vanishes |
| 4 | dynamical | dynamical | topological | vanishes |
| 5 | dynamical | dynamical | dynamical | vanishes |
| 6 | dynamical | dynamical | dynamical | topological |
| 7 | dynamical | dynamical | dynamical | dynamical |

## Interpretation

This table is a standard action-classification gate. It does not derive the
Einstein-Hilbert action, but it identifies which Lovelock terms can carry local
dynamics in each dimension.
