# candidate_payload_action_minimizer — Analysis Note

## Result

`candidate_payload_action_minimizer.py` defines the reduced low-order payload action:

```text
A(p,q) = M2(p,q)^2 + M4(p,q)^2
```

The action is:

```text
A = 1048576*(1445*p^2 + 714*p*q - 1734*p + 293*q^2 - 21318*q + 533205)/586396035225
```

The gradient has the unique critical point:

```text
p = -12
q = 51
```

At that point:

```text
A = 0
```

The Hessian checks are positive:

```text
Hessian[0,0] = 2097152/405810405

Hessian determinant =
4503599627370496/1189828062725257580625
```

## Interpretation

This is the second major origin result.

The Group 85 profile is not only the unique solution of the moment equations. It is also the zero-action minimizer of the reduced payload action.

That matters because it gives the profile a variational origin inside the reduced model:

```text
minimize low-order payload leakage
```

rather than merely:

```text
solve two equations by hand.
```

Because the action is a sum of squares and reaches zero, the critical point is not just local decoration. It is the global zero of the reduced payload action.

## What Changed

The profile now has two reduced origins:

```text
minimal-degree uniqueness;
zero-action payload minimization.
```

That makes it meaningfully less like repair paint inside the reduced model.

## What Did Not Change

The action is still a reduced finite-mode payload action, not a physical action derived from the parent theory. This is a very important scope boundary.

A future group would need to ask whether:

```text
A = M2^2 + M4^2
```

comes from geometry, energy, entropy, admissibility, or a projection principle.

## Steering Consequence

The next file should explain why the weighted suppression from Group 85 was not a separate miracle. It should follow from the flat moment block under a quadratic measure.
