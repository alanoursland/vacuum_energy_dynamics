# candidate_boundary_lift_decomposition — Result Note

## Result

The script records the roles of each component in the expanded O-free residual.

Boundary terms:

```text
D_jump:
  matching discontinuity / boundary flux burden;
  must vanish or match structurally.

D_layer:
  transition-layer burden;
  diagnostic-only unless derived as physical boundary term.

D_tail:
  exterior tail / far-zone scalar leakage burden;
  must vanish or match structurally.
```

Lift terms:

```text
L_bulk:
  bulk covariant lift mismatch;
  must vanish for pure boundary matching route.

L_boundary:
  lift-induced boundary term;
  only legitimate matching carrier if derived.

L_gauge:
  gauge/reduction mismatch;
  must vanish or be controlled by covariant reduction.
```

## Main Findings

The decomposition is useful because it separates possible theorem targets from possible repair patches.

The key danger terms are:

```text
D_layer;
L_boundary.
```

They could be legitimate if derived from the same boundary/lift geometry. They become repair-like if selected freely to cancel a residual.

The diagnostic transition response cannot be used to supply `D_layer`.

## Boundary

Component roles are identified, but none of the component neutrality theorems are proved.

## Steering Consequence

Proceed to the generic independence no-go. The next script should test whether these terms can cancel generically if they are independent.
