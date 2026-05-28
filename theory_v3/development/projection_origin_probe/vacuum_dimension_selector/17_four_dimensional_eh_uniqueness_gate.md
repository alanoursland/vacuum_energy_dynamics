# Vacuum Dimension Selector 17: Four-Dimensional EH Uniqueness Gate

## Purpose

This proof isolates the Lovelock consequence of `D=4`.

## Validated Checks

- `p=0` cosmological term is allowed: passed
- `p=1` Einstein-Hilbert term is dynamical: passed
- `p=2` Gauss-Bonnet term is topological: passed
- `p>=3` Lovelock terms vanish in four dimensions: passed
- the only dynamical curvature Lovelock order in `D=4` is `p=1`: passed

## Computation

```text
D = 4
statuses = {0: 'dynamical', 1: 'dynamical', 2: 'topological', 3: 'vanishes', 4: 'vanishes', 5: 'vanishes'}
dynamical curvature orders = [1]
```

## Interpretation

Under the assumptions of locality, diffeomorphism invariance, metric variables,
and second-order Lovelock field equations, four dimensions select the
Einstein-Hilbert curvature term as the unique local dynamical curvature term.
The cosmological term remains separately allowed.
