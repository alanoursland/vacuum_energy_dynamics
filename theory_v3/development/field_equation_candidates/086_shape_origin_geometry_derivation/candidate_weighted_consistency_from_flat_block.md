# candidate_weighted_consistency_from_flat_block — Analysis Note

## Result

`candidate_weighted_consistency_from_flat_block.py` shows how weighted moments relate to flat moments under the quadratic measure:

```text
mu = R^2 + 2Rell y + ell^2 y^2
```

The formulas are:

```text
W0 = R^2 M0 + 2Rell M1 + ell^2 M2

W1 = R^2 M1 + 2Rell M2 + ell^2 M3

W2 = R^2 M2 + 2Rell M3 + ell^2 M4

W3 = R^2 M3 + 2Rell M4 + ell^2 M5
```

Therefore, if:

```text
M0 = M1 = M2 = M3 = M4 = M5 = 0
```

then:

```text
W0 = W1 = W2 = W3 = 0.
```

## Interpretation

This result explains why the Group 85 weighted suppression worked.

It was not a separate tuning miracle. Under a quadratic measure, each weighted moment through `W3` is built from a three-term window of flat moments. Killing the flat block `M0..M5` automatically kills `W0..W3`.

That is a clean structural result.

## What Changed

The weighted success from Group 85 should now be interpreted as a consequence of the flat moment block, not an independent coincidence.

This strengthens the route because it shows:

```text
flat finite-mode suppression implies weighted finite-mode suppression
```

for the tested quadratic measure and moment range.

## What Did Not Change

The result is finite-order.

It does not imply all weighted moments vanish. In fact, Group 85 found:

```text
W4 != 0.
```

The formula also depends on the measure being quadratic. A higher-order measure would require a larger flat moment block.

## Steering Consequence

This naturally points toward a moment hierarchy question:

```text
Can higher-degree profiles kill larger flat moment blocks,
and thereby kill larger weighted blocks for higher-order measures?
```

That is probably the most direct next technical route.
