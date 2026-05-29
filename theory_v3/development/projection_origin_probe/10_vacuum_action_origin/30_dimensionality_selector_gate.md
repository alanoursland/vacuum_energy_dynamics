# Vacuum Action Origin 30: Dimensionality Selector Gate

## Purpose

This report validates two independent dimensionality selectors already present
in the proof chain.

It does not derive dimensionality from the vacuum ontology. It records what the
existing gates select if their physical criteria are accepted.

## Validated Checks

- inverse-square field selects three spatial dimensions: passed
- inverse-square plus one time dimension gives D=4: passed
- two massless spin-2 polarizations select D=4: passed
- spin-2 dof in D=3: passed
- spin-2 dof in D=4: passed
- spin-2 dof in D=5: passed
- 4D Lovelock status gate: passed

## Boundary-Flux Selector

In `n` spatial dimensions, a monopole field strength scales as:

```text
F(r) ~ r^(1-n).
```

The inverse-square law requires:

```text
1 - n = -2.
```

SymPy verifies:

```text
n = 3.
```

With one propagation time dimension:

```text
D = n + 1 = 4.
```

## Spin-2 Selector

The number of massless spin-2 degrees of freedom in `D` spacetime dimensions is:

```text
D(D-3)/2.
```

Setting this equal to two gives the positive integer solution:

```text
D = 4.
```

## Lovelock Gate in Four Dimensions

In `D=4`:

```text
p=0: cosmological
p=1: Einstein-Hilbert dynamical
p=2: Gauss-Bonnet topological
p>=3: vanishes.
```

## Interpretation

The folder has not proved why the vacuum must have three spatial dimensions.
But the already established physical targets converge on four spacetime
dimensions:

```text
inverse-square boundary flux -> 3 space + 1 time
two spin-2 polarizations     -> 4 spacetime
4D Lovelock gate             -> EH as unique dynamical local metric action.
```
