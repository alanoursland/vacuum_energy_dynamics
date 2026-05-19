# candidate_orientation_forcing_test — Result Note

## Result

`candidate_orientation_forcing_test.py` tests the orientation anti-match condition.

It uses:

```text
D_boundary = G
L_boundary = -sigma * G
```

so the residual is:

```text
G * (1 - sigma)
```

Solving the compatibility condition gives:

```text
sigma = 1
```

## Analysis

This is a correct compatibility result. If the boundary and lift sides are the same generator with opposite orientation, the sign parameter must be:

```text
sigma = 1
```

The script also rejects the important false routes:

```text
free sigma;
same orientation;
zero generator.
```

This matters because `sigma = 1` can be obtained in two very different ways:

```text
derived orientation:
  acceptable theorem route;

chosen sign:
  repair paint.
```

Group 71 has not yet derived the orientation. It has only shown the sign a real generator must force.

## Boundary

The sign requirement is derived as compatibility, not as an orientation theorem. The missing theorem is still:

```text
derive opposite orientation from a real boundary/covariant generator.
```

## Unexpected Results

None. The result matches the expected Group 70 compatibility and sharpens the Group 71 theorem burden.

## Steering Consequence

Proceed to component forcing. Even with correct orientation, the generator must still account for jump, layer, and tail components with the correct coefficients.
