# candidate_weighted_skew_problem — Analysis Note

## Result

`candidate_weighted_skew_problem.py` opens Group 83 as a weighted-skew geometry derivation attempt.

The central question is:

```text
Is c = 3 ell/(2R) forced by weighted exactness geometry?
```

The script imports the Group 82 status correctly:

```text
flat integrated neutrality derived in reduced compact-support class;
local rho remains nonzero;
weighted/geometric neutrality is not automatic;
skew c = 3ell/(2R) restores weighted neutrality as compatibility;
skew must be derived geometrically, not chosen;
payload inertness remains open;
parent divergence identity unproven;
recombination blocked.
```

## Interpretation

This opener sets the correct standard for Group 83. It does not ask whether the skew can cancel the weighted charge. Group 82 already answered that. It asks whether the skew has an origin.

That distinction matters. A coefficient found by solving a residual equation is suspicious if it is merely chosen after seeing the leak. A coefficient forced by the geometry of the pairing is much stronger.

So the group’s real target is not:

```text
find c
```

but:

```text
explain why c must have that value.
```

This is exactly the right follow-up to Group 82.

## What Changed

The project has moved from a compatibility question to an origin question:

```text
Group 82:
  weighted neutrality can be restored if c = 3ell/(2R)

Group 83:
  test whether c = 3ell/(2R) follows from the weighted exactness structure
```

That is a real progress step, not bookkeeping.

## What Did Not Change

The opener correctly preserves the unsolved obligations:

```text
local rho remains nonzero;
payload inertness remains open;
parent divergence remains unproven;
recombination remains blocked.
```

Even a successful skew derivation cannot be spent as local field removal.

## Steering Consequence

The next scripts must derive a structural identity, not just repeat the Group 82 charge calculation. The right object to test is the measure-gradient identity:

```text
Q_mu = ∫ mu rho dy = -∫ mu' J dy
```

under compact endpoint flux.
