# candidate_constraint_rank_uniqueness_test — Analysis Note

## Result

`candidate_constraint_rank_uniqueness_test.py` checks the constraint matrices for `N=1..4`.

The ranks are full in each case:

```text
N=1: rank(A)=1, rank(A|b)=1, unique=True
N=2: rank(A)=2, rank(A|b)=2, unique=True
N=3: rank(A)=3, rank(A|b)=3, unique=True
N=4: rank(A)=4, rank(A|b)=4, unique=True
```

The determinants are nonzero:

```text
N=1: -1024/45045
N=2: 33554432/34493884425
N=3: -2199023255552/18011555903220004125
N=4: 604130868413987815424/13169813390487483931834385878125
```

## Interpretation

This result strengthens the hierarchy claim.

The profiles found in the previous script are not arbitrary choices from a family of possibilities. For each tested order, the payload-moment constraints are full-rank and force a unique normalized even profile.

That matters because a hierarchy with free coefficients would be much weaker. Free coefficients smell like repair paint. Full-rank uniqueness means the reduced constraints determine the profile.

## What Changed

The status becomes:

```text
unique finite hierarchy through N=4
```

not merely:

```text
some examples found.
```

## What Did Not Change

The rank proof is finite. It checks `N=1..4`, not all `N`.

So the right interpretation is:

```text
strong finite evidence for a hierarchy;
general rank theorem still open.
```

## Steering Consequence

The next useful step is to derive a general determinant, recurrence, or orthogonal-polynomial structure that explains why the rank remains full.
