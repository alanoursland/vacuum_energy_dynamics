# candidate_minimal_degree_obstruction — Analysis Note

## Result

`candidate_minimal_degree_obstruction.py` tests lower-degree even shapes.

For the constant shape:

```text
M2 = 1024/1155
M4 = 2048/5005
```

so degree 0 cannot suppress the first nontrivial even payload moments.

For the even quadratic shape:

```text
P = 1 + p y^2
```

the moments are:

```text
M2 = -1024*(p - 39)/45045
M4 = 2048*(p + 9)/45045
```

Killing `M2` requires:

```text
p = 39
```

but then:

```text
M4 = 32768/15015
```

There is no simultaneous degree-2 solution for:

```text
M2 = 0
M4 = 0
```

## Interpretation

This is one of the core origin results. It shows that the quartic profile from Group 85 is not an unnecessarily complicated choice inside the normalized even polynomial hierarchy. Lower degrees fail the `M2/M4` target.

So the quartic profile is not just a more decorative key. It is the first available key shape that can turn both low-order even tumblers.

## What Changed

The status of the quartic profile strengthens from:

```text
a profile that works
```

to:

```text
the minimal even normalized degree capable of meeting the M2/M4 suppression target.
```

That is a real origin statement inside the reduced model.

## What Did Not Change

This minimality depends on the chosen target:

```text
suppress M2 and M4.
```

It does not prove that those are the fundamental physical constraints. It proves that, given those reduced payload constraints, degree 4 is minimal.

## Steering Consequence

Now that degree 4 is justified as minimal, the next question is whether the quartic solution is unique. The results show it is.
