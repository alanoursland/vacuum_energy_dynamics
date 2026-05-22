# candidate_formula_validation_N1_to_N6 — Analysis Note

## Result

`candidate_formula_validation_N1_to_N6.py` validates the Beta formula through `N=6`.

It reproduces the known profiles through `N=4` and extends the hierarchy to `N=5` and `N=6`.

The new generated profiles are:

```text
N=5:
P_5(t) =
1 + (9297/19)t
  - (143106/19)t^2
  + (753250/19)t^3
  - (1526625/19)t^4
  + (1050525/19)t^5
```

and:

```text
N=6:
P_6(t) =
1 - (20079/314)t
  + (443325/314)t^2
  - (1645075/157)t^3
  + (5302650/157)t^4
  - (15197595/314)t^5
  + (7960645/314)t^6.
```

For `N=1..6`, the formula-difference checks are zero and the target moments are killed.

## Interpretation

This is the main validation result.

The Beta formula is not merely a symbolic restatement of the known `N=1..4` results. It generates new hierarchy members `N=5` and `N=6`, and those profiles satisfy the target moment constraints exactly.

That is a meaningful strengthening of the hierarchy.

The pattern is now supported in two ways:

```text
structurally, by the Beta linear system;
computationally, by exact validation through N=6.
```

## What Changed

Group 87 gave finite evidence through `N=4`. Group 88 extends that evidence through `N=6` using the formula, not by ad hoc direct solving.

The hierarchy is now better understood as an exact finite-N construction.

## What Did Not Change

`N=1..6` is still finite. This does not prove all-order existence, convergence, or local inertness.

The script correctly rejects:

```text
N=1..6 validation as all-order proof.
```

## Steering Consequence

Now that the formula is validated beyond the known cases, the next hard problem is no longer “does the formula work on examples?” It is:

```text
does the determinant stay nonzero?
```

or:

```text
what recurrence/orthogonal-polynomial structure explains the coefficients?
```
