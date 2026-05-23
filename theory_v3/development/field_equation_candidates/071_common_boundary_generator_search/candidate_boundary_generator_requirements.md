# candidate_boundary_generator_requirements — Result Note

## Result

`candidate_boundary_generator_requirements.py` converts the Group 70 compatibility package into explicit generator requirements.

It defines:

```text
B = D_jump + D_layer + D_tail
D_boundary = +B
L_boundary = -B
```

and shows that ideal boundary anti-match leaves:

```text
L_bulk + L_gauge
```

as the remaining O-free residual.

## Analysis

This is the right requirements ledger. It draws the distinction between a boundary sum and a boundary generator:

```text
B alone is the boundary sum, not the origin of the sum.
```

That distinction is essential. A legal generator must exist before signs and coefficients are chosen. It must produce the boundary-side and lift-side terms as opposite orientations of the same object, and it must account for jump, layer, and tail components without importing the old diagnostic transition response as a physical term.

The residual result is also important. Even perfect boundary anti-match does not close the parent divergence identity. It only reduces the target to bulk/gauge lift cleanliness:

```text
L_bulk = 0
L_gauge = 0
```

or a lawful shared lift identity that explains their cancellation.

## Boundary

The script establishes criteria, not a theorem. It does not prove that any real generator satisfies the criteria.

## Unexpected Results

None. The output is expected and useful.

## Steering Consequence

Proceed to orientation testing. The next question is whether an opposite-orientation object can force `sigma = 1` rather than merely allow it.
