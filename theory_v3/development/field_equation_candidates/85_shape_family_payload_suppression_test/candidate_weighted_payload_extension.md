# candidate_weighted_payload_extension — Analysis Note

## Result

`candidate_weighted_payload_extension.py` extends the suppressed profile test to the quadratic measure:

```text
mu = R^2 + 2Rell y + ell^2 y^2
```

For the derived profile:

```text
P = 1 - 12y^2 + 51y^4
```

the weighted moments are:

```text
W0 = 0
W1 = 0
W2 = 0
W3 = 0
W4 = 65536 ell^2 / 323323
```

## Interpretation

This is the second major positive result of Group 85.

The suppressed shape does not only work in the flat moment basis. It also suppresses the weighted local moments through `W3` under the same quadratic measure structure that mattered in Groups 82–83.

That is important because Group 84 showed weighted local probes were still detecting the linear-skew remainder. Group 85 shows those weighted low-order detections are also shape-family dependent.

The remaining obstruction:

```text
W4 = 65536 ell^2 / 323323
```

has a useful interpretation. It is finite-thickness suppressed: it vanishes as:

```text
ell -> 0
```

but remains nonzero for finite layer thickness.

## What Changed

The local payload problem is softened:

```text
linear-skew family:
  W1 and W2 nonzero

even-quartic suppressed family:
  W0 through W3 vanish
```

That is real improvement.

## What Did Not Change

The result is still finite-order only.

The `W4` obstruction means this profile does not provide all-order weighted inertness. It only pushes the first visible weighted moment higher.

## Steering Consequence

The next sharp question is whether there is a hierarchy:

```text
higher-degree shapes kill progressively higher moment blocks
```

or whether the quartic solution is a one-off moment design.
