# candidate_geometric_layer_generator_requirements — Result Note

## Result

`candidate_geometric_layer_generator_requirements.py` converts the Group 72 legitimacy burden into explicit generator criteria.

It restates the boundary sum:

```text
B = D_jump + D_layer + D_tail
```

and the ideal boundary anti-match:

```text
L_boundary = -D_jump - D_layer - D_tail
```

which leaves:

```text
L_bulk + L_gauge
```

after ideal boundary cancellation.

## Main Findings

The legal `D_layer` criteria are now explicit. A legitimate geometric layer generator must be:

```text
geometric before coefficient choice;
local to the boundary/layer region;
able to supply D_layer as a boundary component;
not diagnostic transition payload;
not ordinary-source carrying;
not trace carrying;
not mass response;
not repair current;
not active O by label;
compatible with a common boundary object.
```

This is useful because it prevents a layer term from being installed merely because it helps the Group 70 compatibility package.

## Boundary

The script does not derive `D_layer`.

It does not close bulk/gauge lift cleanliness.

It does not prove boundary-lift matching.

## Steering Consequence

Proceed to `candidate_signed_distance_layer_scaffold.py`.

The next test should ask whether a signed-distance layer scaffold can provide useful geometric structure without being mistaken for physical legitimacy.
