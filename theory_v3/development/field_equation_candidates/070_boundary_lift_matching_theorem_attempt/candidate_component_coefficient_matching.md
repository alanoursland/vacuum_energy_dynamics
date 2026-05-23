# candidate_component_coefficient_matching — Result Note

## Result

The script solves the component coefficient matching problem.

Let:

```text
L_boundary =
a_jump*D_jump
+ a_layer*D_layer
+ a_tail*D_tail
```

Then the residual is:

```text
D_jump*a_jump + D_jump
+ D_layer*a_layer + D_layer
+ D_tail*a_tail + D_tail
```

Coefficient equations:

```text
a_jump + 1 = 0
a_layer + 1 = 0
a_tail + 1 = 0
```

Solution:

```text
a_jump = -1
a_layer = -1
a_tail = -1
```

## Main Findings

The exact component coefficient burden is now explicit.

The lift-boundary term must anti-match each boundary component with coefficient `-1`:

```text
L_boundary =
-D_jump
-D_layer
-D_tail
```

The script correctly rejects:

```text
choosing coefficients to cancel the residual.
```

The coefficients must be derived from common boundary/lift geometry.

## Boundary

This is coefficient compatibility, not a geometry theorem.

## Steering Consequence

Proceed to bulk/gauge neutrality. Even perfect boundary coefficient matching does not eliminate `L_bulk` or `L_gauge`.
