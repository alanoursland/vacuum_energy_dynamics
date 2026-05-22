# candidate_skew_inertness_tradeoff_test — Analysis Note

## Result

`candidate_skew_inertness_tradeoff_test.py` compares the generic linear-skew conditions.

For generic `c`:

```text
M1 = -1024c/3465
```

and:

```text
weighted total = -1024ell*(2R c - 3ell)/3465
```

The weighted-neutrality solution is:

```text
c = 3ell/(2R)
```

The output reports no generic `c` solution for dipole inertness because of the nonzero assumption on `c`; algebraically the dipole inertness condition is:

```text
c = 0
```

Thus the two conditions are:

```text
weighted neutrality: c = 3ell/(2R)
dipole inertness: c = 0
```

They are compatible only in the thin/flat case:

```text
ell = 0
```

## Interpretation

This is the central tradeoff result of Group 84.

The same skew that Group 83 derived to fix weighted total neutrality creates or preserves dipole sensitivity. That means the linear-skew family cannot simultaneously satisfy:

```text
weighted total neutrality
```

and:

```text
dipole inertness
```

for finite `ell/R`.

This is an important structural obstruction. It shows that the problem is not just “we picked the wrong value of c.” There is no single linear skew value that solves both finite-thickness weighted neutrality and dipole silence, except in the degenerate thin/flat limit.

## What Changed

The local inertness problem is now sharper than “M1 happens to be nonzero after the Group 83 skew.”

It is:

```text
weighted neutrality and dipole inertness impose different skew requirements.
```

That is a true route tension.

## What Did Not Change

The result is still within the linear-skew compact-support family. A richer family might add another degree of freedom that can satisfy both constraints.

But this family cannot.

## Steering Consequence

The next technical move, if staying on exactness, should probably be a richer shape-family test. The minimal linear skew has too few degrees of freedom to satisfy weighted neutrality and low-order local inertness simultaneously.
