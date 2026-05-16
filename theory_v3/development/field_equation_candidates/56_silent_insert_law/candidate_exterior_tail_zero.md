# candidate_exterior_tail_zero — Result Note

## Result

The script links the charge-neutral profile to reduced exterior scalar silence.

It uses:

```text
C1 = k*Q
phi_ext = C0 + k*Q/r
```

and verifies:

```text
C0=0 and Q=0 -> phi_ext=0
```

## Main Findings

This gives a clean reduced exterior silence condition. If the net scalar charge vanishes and the exterior scalar offset is fixed to zero, the exterior one-over-r tail vanishes.

The result connects Group 56's charge-neutral construction to the Group 54 exterior scalar-silence surface.

The script also keeps the two required conditions visible:

```text
Q = 0
C0 = 0
```

Neither can be dropped. Zero charge alone leaves a possible constant offset; zero offset alone would not kill a nonzero charge tail.

## Boundary

This is reduced exterior tail logic, not full covariant boundary closure. It does not prove why `Q=0` and `C0=0` hold in the theory, and it does not license insertion.

## Steering Consequence

The route should next test no-shell matching. Exterior silence is not enough if the interior profile leaves a derivative jump at the boundary.
