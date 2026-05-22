# candidate_weighted_measure_neutrality_test — Analysis Note

## Result

`candidate_weighted_measure_neutrality_test.py` tests the exact remainder under a geometric measure:

```text
mu = R^2 + 2*R*ell*y + ell^2*y^2
```

The flat charge remains:

```text
0
```

but the weighted charge is:

```text
1024*ell^2/1155
```

## Interpretation

This is the most important obstruction found by Group 82.

Flat exactness does not survive the first nontrivial geometric measure automatically. That means the flat integral theorem is not enough for geometric/covariant lift cleanliness.

The weighted charge being proportional to:

```text
ell^2
```

is suggestive. It says the obstruction appears at finite layer thickness / curvature-measure order. In the thin-layer limit:

```text
ell -> 0
```

the weighted obstruction would vanish, but Group 82 does not prove that such a limit is legitimate or sufficient. If finite-thickness layer structure matters physically, this weighted charge is a real leftover.

## Conceptual Consequence

This result prevents a major overclaim:

```text
rho exact => rho harmless
```

The better statement is:

```text
rho exact => flat neutral, but measure-sensitive neutrality requires additional structure.
```

This is especially important because earlier boundary/layer work had already shown that flat neutrality and weighted neutrality can diverge. Group 82 confirms that the same issue appears inside the rho exactness route.

## Boundary

The result does not kill exactness. It says exactness must be measure-compatible.

## Steering Consequence

The next useful target is not another generic exactness audit. It is:

```text
derive measure-compatible skew from geometry
```

or prove that the relevant physical pairing uses the flat measure rather than `mu`.
