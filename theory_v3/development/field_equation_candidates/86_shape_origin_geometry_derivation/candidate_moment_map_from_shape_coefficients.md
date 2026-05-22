# candidate_moment_map_from_shape_coefficients — Analysis Note

## Result

`candidate_moment_map_from_shape_coefficients.py` derives the moment map for the even polynomial family:

```text
P = 1 + a1 y^2 + a2 y^4 + a3 y^6
```

The key moments are:

```text
M0 = 0

M2 = -1024*(17*a1 + 17*a2 + 9*a3 - 663)/765765

M4 = 2048*(323*a1 + 19*a2 - 21*a3 + 2907)/14549535

M6 = 1024*(209*a1 + 49*a2 + 9*a3 + 969)/4849845
```

## Interpretation

This is a foundational result for Group 86. It turns the shape-origin problem into a linear algebra problem. The payload moments are not mysterious nonlinear responses of the exactness profile. They are linear functions of the even shape coefficients.

That means moment suppression is a projection-like constraint problem:

```text
shape coefficients -> exactness operator -> payload moments
```

The profile is not being guessed blindly. It is being determined by a linear moment map.

## What Changed

The Group 85 profile now has a clearer mathematical context. Instead of merely saying that `p=-12, q=51` works, we now know the even shape coefficients live in a linear payload-moment map, and the profile is a null-condition solution in that map.

## What Did Not Change

This does not yet explain why the physical theory should impose `M2=M4=0`, nor why this polynomial family is the correct physical family. It only shows that, once those reduced conditions are chosen, the coefficient map is explicit and linear.

## Steering Consequence

The natural next move is minimal-degree analysis. If lower-degree shapes fail and quartic succeeds uniquely, then the Group 85 profile becomes the minimal solution of the reduced suppression problem rather than just one convenient solution.
