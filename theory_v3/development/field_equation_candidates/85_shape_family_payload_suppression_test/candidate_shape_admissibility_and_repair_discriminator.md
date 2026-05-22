# candidate_shape_admissibility_and_repair_discriminator — Analysis Note

## Result

`candidate_shape_admissibility_and_repair_discriminator.py` tests regularity and repair status for the derived profile.

The profile is:

```text
P(y) = 51y^4 - 12y^2 + 1
```

Using:

```text
t = y^2
P(t) = 51t^2 - 12t + 1
```

the minimum occurs at:

```text
t* = 2/17
```

with:

```text
P_min = 5/17
```

and endpoint values:

```text
P(0) = 1
P(1) = 40
```

So `P` is positive on the tested interval.

The script classifies:

```text
inside_reduced_moment_problem: NOT_REPAIR
relative_to_Group84: STRENGTHENED
relative_to_full_theory: NOT_CLOSED
local_rho_status: NONZERO
higher_moment_status: OPEN
parent_status: BLOCKED
```

## Interpretation

This result matters because a moment-suppression profile could have been mathematically effective but physically ugly. It is not. The profile is regular and positive on the interval.

Also, note a correction relative to the plan expectation: the actual minimum is:

```text
5/17
```

not the earlier guessed value. That is not a problem. It is a cleaner result and confirms positivity.

The repair status is nuanced and correct:

```text
not repair inside the reduced moment problem;
not full theory because shape origin is not derived.
```

The coefficients are not arbitrary inside this reduced problem. They follow uniquely from the moment constraints. But the moment constraints themselves are still a design target unless a future group derives them from geometry, a variational principle, or a physical payload criterion.

## What Changed

The derived profile is admissible as a regular mathematical object. That removes one possible failure mode.

## What Did Not Change

The shape is still not physically explained.

This is now the central open question:

```text
Who carved P(y) = 1 - 12y^2 + 51y^4?
```

If the answer is “we chose it to kill moments,” then it is still a designed suppression profile. If the answer is “it follows from a geometry/variational/minimal-energy condition,” then the route becomes much stronger.

## Steering Consequence

The best next group is probably:

```text
86_shape_origin_geometry_derivation
```

because the shape is effective and regular; now its origin is the limiting issue.
