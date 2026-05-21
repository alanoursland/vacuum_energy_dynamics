# candidate_gauge_neutrality_test — Result Note

## Result

`candidate_gauge_neutrality_test.py` tests the independent gauge-neutrality route.

It factors the gauge residue as:

```text
L_gauge = G_gauge * i_gauge
```

The gauge-parameter variation diagnostic is also:

```text
G_gauge * i_gauge
```

Solving:

```text
L_gauge = 0
```

gives:

```text
i_gauge = 0
```

The active gauge case leaves:

```text
G_gauge
```

## Main Findings

The result is again compatibility, not theorem.

Gauge residue may vanish only if the gauge dependence is proven pure, inert, or absent. Setting `i_gauge = 0` by assignment does not prove gauge neutrality.

The script correctly rejects:

```text
assigned gauge removal;
active gauge residue.
```

## Boundary

Gauge neutrality is not derived. It remains an open theorem target.

## Steering Consequence

Proceed to shared lift identity. The next route is to test whether bulk and gauge residues can be paired by one lawful lift structure rather than independently set to zero.
