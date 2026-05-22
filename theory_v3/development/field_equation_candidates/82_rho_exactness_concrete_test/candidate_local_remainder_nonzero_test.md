# candidate_local_remainder_nonzero_test — Analysis Note

## Result

`candidate_local_remainder_nonzero_test.py` shows that the compact-support exact remainder is locally nonzero:

```text
rho = -6*(y - 1)^3*(y + 1)^3*(3*y - 1)*(3*y + 1)
rho(0) = -6
rho identically zero? False
```

The roots are:

```text
y = -1, -1/3, 1/3, 1
```

## Interpretation

This is not a failure of the exactness route. It is the diagnostic that tells us exactly what kind of success exactness achieved.

The exact form gives a redistribution pattern. It creates local positive and negative structure whose flat integral cancels. The local nonzero result means `rho` is not gone; it has been organized.

That distinction is crucial:

```text
global neutrality is not local absence.
```

This matters because a field equation normally cares about local residuals unless there is a reason they are gauge, exact-boundary, inert, or unobservable. So local nonzero `rho` cannot be ignored.

## Conceptual Consequence

This result splits the next theory burden into two possible paths:

```text
1. Prove local nonzero rho is physically inert.
2. Prove only integrated/weighted neutrality is needed for the target.
```

The first path needs a no-payload or gauge-inertness theorem. The second path needs the field-equation target to be global/boundary-integrated rather than local.

If the intended boundary-lift cancellation is local, this script is a serious obstruction. If the intended cancellation is integrated over a boundary layer, this script is acceptable but still requires correct measure handling.

## Boundary

The script should not be read as disproving exactness. It proves exactness is insufficient for local removal.

## Steering Consequence

Future status should say:

```text
rho exactness gives global flat neutrality, but local residual remains active unless separately inert.
```
