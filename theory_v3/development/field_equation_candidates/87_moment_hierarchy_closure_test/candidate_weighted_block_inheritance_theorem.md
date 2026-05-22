# candidate_weighted_block_inheritance_theorem — Analysis Note

## Result

`candidate_weighted_block_inheritance_theorem.py` derives the weighted block inheritance rule for the quadratic measure:

```text
mu = R^2 + 2Rell y + ell^2 y^2
```

The moment relation is:

```text
Wn = R^2 M_n + 2Rell M_(n+1) + ell^2 M_(n+2)
```

So if a profile kills the flat block:

```text
M0..M(2N+1) = 0
```

then it automatically kills the weighted block:

```text
W0..W(2N-1) = 0.
```

The script demonstrates this explicitly through the `N=4` block, where `W0..W7` vanish under the corresponding flat moment block.

## Interpretation

This result explains why the hierarchy matters under weighted geometry.

The hierarchy is not only flat-moment suppression. Because the measure is quadratic, weighted suppression follows from the flat block with a two-moment shift.

That means higher-order flat suppression automatically buys higher-order weighted suppression. The weighted structure is not an independent tuning problem at each order.

This is an important structural simplification.

## What Changed

The route now has a clear inheritance law:

```text
flat block suppression -> quadratic weighted block suppression.
```

This gives the finite hierarchy more physical relevance because it survives the same type of measure weighting used in earlier groups.

## What Did Not Change

The inheritance is finite and measure-specific.

A cubic or higher-order measure would require a larger flat block. And the result does not prove all weighted moments vanish.

## Steering Consequence

Any future hierarchy formula should track both:

```text
flat block length;
measure degree;
inherited weighted block length.
```

This is likely where a covariant lift will eventually need to generalize the result.
