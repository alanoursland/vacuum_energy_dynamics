# candidate_structural_matching_route — Result Note

## Result

The script identifies the retained non-generic structural route.

Route conditions:

```text
L_bulk = 0
L_gauge = 0
L_boundary = -(D_jump + D_layer + D_tail)
```

Under those conditions:

```text
matched residual = 0
```

## Main Findings

This is the constructive result of Group 69.

The route is not:

```text
choose L_boundary to cancel the boundary burden.
```

The route is:

```text
derive L_boundary from the same geometry as the boundary terms.
```

That distinction is the whole goblin hinge.

The retained theorem target is:

```text
boundary-lift matching theorem.
```

This theorem would need to show that the covariant-lift boundary contribution and the boundary divergence contribution are not independent. They must arise from one shared boundary/covariant structure.

Open obligations:

```text
derive L_boundary from the same geometry as the boundary sum;
derive L_bulk = 0;
derive L_gauge = 0.
```

## Boundary

The matched residual is a compatibility result, not a theorem. The script shows what would work, not that the theory supplies it.

## Steering Consequence

Proceed to repair rejection. The next script should reject the same-looking relations when they are chosen freely rather than derived.
