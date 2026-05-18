# candidate_covariant_lift_requirement — Result Note

## Result

The original script failed before recording its marker.

Failure:

```text
IndexError: list index out of range
```

Cause:

```text
sp.solve(sp.Eq(D_cov, D_reduced), L_error)
```

was called on an equation that does not contain `L_error`, so SymPy returned no solution.

## Required Script Fix

The intended relation is:

```text
D_cov = D_reduced + L_error
```

The exact-lift condition is:

```text
D_cov = D_reduced
```

Combining those gives:

```text
L_error = 0
```

The corrected solve should be something like:

```python
lift_required = sp.solve(sp.Eq(D_reduced + L_error, D_reduced), L_error)[0]
```

or simply:

```python
lift_required = sp.Integer(0)
```

## Conceptual Result

With the corrected logic, the result should be:

```text
covariant lift required;
exact lift condition is L_error=0;
no covariant lift theorem is proved here;
reduced divergence balance is not a parent conservation identity.
```

## Boundary

This script should remain a requirement/obstruction record, not a proof of covariant conservation.

## Steering Consequence

Rerun the patched `candidate_covariant_lift_requirement.py`, then rerun downstream scripts if clean archive dependency satisfaction is desired.
