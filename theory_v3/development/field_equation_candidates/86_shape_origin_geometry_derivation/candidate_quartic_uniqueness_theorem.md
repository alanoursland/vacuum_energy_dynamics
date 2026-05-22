# candidate_quartic_uniqueness_theorem — Analysis Note

## Result

`candidate_quartic_uniqueness_theorem.py` solves the normalized even quartic system:

```text
P = 1 + p y^2 + q y^4
```

with:

```text
M2 = -1024*(p + q - 39)/45045
M4 = 2048*(17*p + q + 153)/765765
```

Solving:

```text
M2 = 0
M4 = 0
```

gives the unique solution:

```text
p = -12
q = 51
```

so:

```text
P(y) = 1 - 12y^2 + 51y^4
```

and at the solution:

```text
M2 = 0
M4 = 0
```

## Interpretation

This is the main uniqueness theorem of Group 86.

Together with the minimal-degree obstruction, it means:

```text
Among normalized even polynomial shapes, degree 4 is the first degree that can suppress M2 and M4,
and at that degree the successful profile is unique.
```

That is much stronger than Group 85’s moment-fit status.

The profile is not arbitrary inside the reduced shape hierarchy. It is forced once the reduced requirements are:

```text
P(0)=1;
P even;
degree <= 4;
M2 = 0;
M4 = 0.
```

## What Changed

The status should move from `shape origin open` to `minimal-degree reduced origin derived`, with strict scope.

## What Did Not Change

This is not yet a physical geometry derivation. The theorem does not explain why the real system should choose the normalized even quartic family or the `M2/M4` payload constraints.

It proves uniqueness inside the reduced problem.

## Steering Consequence

The next result should test whether this same profile also has a variational interpretation, not just a constraint-solving interpretation.
