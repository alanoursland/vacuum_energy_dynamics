# candidate_component_forcing_test — Result Note

## Result

`candidate_component_forcing_test.py` solves the component anti-match compatibility condition.

With:

```text
L_boundary =
  a_jump  * D_jump
+ a_layer * D_layer
+ a_tail  * D_tail
```

the residual is:

```text
D_jump*(a_jump + 1)
+ D_layer*(a_layer + 1)
+ D_tail*(a_tail + 1)
```

Setting independent component coefficients to zero gives:

```text
a_jump = -1
a_layer = -1
a_tail = -1
```

## Analysis

This is the correct component-level compatibility package.

The output also exposes the sharpest component risk:

```text
a_layer = -1
```

The layer component cannot be allowed to smuggle in the old diagnostic transition response. The script correctly treats the all-component anti-match as retained only if the generator covers jump, layer, and tail as one legitimate boundary object.

The rejected patterns are useful:

```text
missing layer -> residual = D_layer
jump only -> residual = D_layer + D_tail
same sign -> residual = 2*D_jump + 2*D_layer + 2*D_tail
```

These show why partial boundary matching is not enough for parent divergence closure.

## Boundary

The coefficient solution is compatibility, not a geometry theorem. The script does not prove that one shared boundary/lift geometry forces these coefficients.

## Unexpected Results

None. The output is expected.

## Steering Consequence

The next major blocker is not the algebraic coefficient package. It is component legitimacy, especially `D_layer`, and then the remaining bulk/gauge lift terms.
