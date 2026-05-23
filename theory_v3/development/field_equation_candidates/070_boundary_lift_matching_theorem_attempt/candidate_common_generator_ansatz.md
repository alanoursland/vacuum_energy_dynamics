# candidate_common_generator_ansatz — Result Note

## Result

The script defines a common boundary generator:

```text
B = D_jump + D_layer + D_tail
```

and an anti-match ansatz:

```text
L_boundary = -sigma*(D_jump + D_layer + D_tail)
```

Under this ansatz, the O-free residual becomes:

```text
D_jump + D_layer + D_tail + L_bulk + L_gauge
- sigma*(D_jump + D_layer + D_tail)
```

Equivalently:

```text
L_bulk + L_gauge + (1-sigma)*B
```

## Main Findings

This is a useful compatibility ansatz.

It shows that a common-generator route would reduce the Group 69 matching problem to three remaining burdens:

```text
derive sigma = 1;
derive L_bulk = 0;
derive L_gauge = 0.
```

But the script correctly does not claim the theorem is proven. The sign `sigma` must come from orientation/common geometry, not from convenience.

## Boundary

The ansatz is compatibility structure, not a derived matching theorem.

## Steering Consequence

Proceed to the orientation sign sieve. The next script should derive the required sign condition and preserve that the sign still needs a theorem.
