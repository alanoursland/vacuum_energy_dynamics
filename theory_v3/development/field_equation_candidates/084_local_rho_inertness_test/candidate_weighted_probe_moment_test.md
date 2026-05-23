# candidate_weighted_probe_moment_test — Analysis Note

## Result

`candidate_weighted_probe_moment_test.py` computes weighted low-order moments using:

```text
mu = R^2 + 2Rell*y + ell^2*y^2
```

The moments are:

```text
W0 = 0
W1 = 512ell*(13R^2 + 2ell^2)/(5005R)
W2 = 1024*(13R^2 + 12ell^2)/15015
```

## Interpretation

This result is even more damaging to the idea that weighted neutrality implies local inertness.

Group 83 successfully derived the skew that makes the weighted total charge vanish:

```text
W0 = 0
```

But the weighted local probes remain nonzero:

```text
W1 != 0
W2 != 0
```

So even after using the geometry-paid skew, the measure-weighted local payload channels still see the remainder.

This distinguishes two levels of weighted success:

```text
weighted total neutrality;
weighted local inertness.
```

Group 83 gave the first. Group 84 shows it does not give the second.

## What Changed

The result upgrades the payload concern from flat-only to measure-aware.

The obstruction is not an artifact of using flat probes after a weighted derivation. Even the same measure that Group 83 used to derive the skew still detects local moments once multiplied by `y` and `y^2`.

## What Did Not Change

Weighted total neutrality remains valid and important.

But it should now be described as:

```text
weighted monopole neutrality
```

not:

```text
weighted payload inertness.
```

## Steering Consequence

This result increases pressure on the shape family or on a projection/inertness interpretation. If the theory requires local payload silence, the current linear-skew exactness family does not provide it.
