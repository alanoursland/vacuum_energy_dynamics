# candidate_profile_generation_under_invertibility — Analysis Note

## Result

`candidate_profile_generation_under_invertibility.py` generates hierarchy profiles through `N=10` using determinant-valid matrices.

For every tested order:

```text
target residuals zero = True
```

The known profiles through `N=6` are recovered and the hierarchy extends through `N=10`.

The next obstructions remain nonzero:

```text
N=7:
M16 = 137438953472/7950790858725

N=8:
M18 = 1099511627776/3931491379552789

N=9:
M20 = 35184372088832/3928510572687519

N=10:
M22 = 774056185954304/30854363619467526915
```

The local value also remains nonzero in every tested case, for example:

```text
N=10:
rho(0) = -12471030/38953
```

## Interpretation

This result extends the hierarchy in the strongest practical way so far.

Group 87 established profiles through `N=4`. Group 88 formula validation extended to `N=6`. Group 89 confirms that determinant-valid matrices generate exact target-suppressing profiles through `N=10`.

So the hierarchy is not brittle under extension.

But the same script preserves the core obstruction:

```text
the target moment block is killed;
the next moment remains;
rho(0) remains nonzero.
```

That is the recurring signature of the hierarchy.

## What Changed

The finite hierarchy is now validated through a much larger range:

```text
N=1..10.
```

That is strong finite evidence for the coefficient generator and determinant gate.

## What Did Not Change

The hierarchy remains finite-order suppression, not local inertness.

Increasing `N` keeps pushing the obstruction outward. It has not removed the obstruction.

## Steering Consequence

The next useful question is not whether `N=11` works. The next useful question is why all tested `N` work, and what happens in the limit.
