# candidate_quadratic_payload_obstruction — Analysis Note

## Result

`candidate_quadratic_payload_obstruction.py` computes the quadratic payload moment for generic linear skew:

```text
M2 = ∫ y^2 rho dy = 1024/1155
```

Its derivative with respect to the skew is:

```text
dM2/dc = 0
```

There are no solutions for:

```text
M2 = 0
```

in the linear-skew family.

## Interpretation

This is the strongest obstruction in Group 84.

The dipole problem might be solved by changing the skew. The quadratic problem cannot. Within this compact-support linear-skew family, the quadratic moment is invariant under the skew parameter.

That means local payload obstruction is not merely a bad choice of `c`. It is built into the even part of the exact remainder shape.

This sharply limits what the Group 82/83 exactness family can achieve:

```text
it can handle total charges;
it cannot make the local second moment disappear.
```

## What Changed

The local inertness status moves from “not established” to “obstructed in the tested finite-mode class.”

The exactness route remains useful for integrated neutrality, but it cannot be called locally inert unless a new mechanism is added.

## What Did Not Change

This is not a full no-go theorem for all possible exactness profiles. It is a no-go for the tested compact-support linear-skew family.

A richer shape family with additional parameters may be able to suppress the quadratic moment. But that would be new structure, not a consequence of the Group 83 skew.

## Steering Consequence

The most natural next theorem attempt is:

```text
85_shape_family_payload_suppression_test
```

It should ask whether adding a second shape degree of freedom can satisfy:

```text
weighted total neutrality;
dipole inertness;
quadratic inertness.
```

without becoming repair paint.
