# candidate_even_quartic_shape_family — Analysis Note

## Result

`candidate_even_quartic_shape_family.py` defines the even quartic shape family:

```text
P = 1 + p y^2 + q y^4
```

with:

```text
Xi = (1-y^2)^3 P
J = -2y(y - 1)^4(y + 1)^4(4p y^2 - p + 5q y^4 - 2q y^2 + 3)
rho = -2(y - 1)^3(y + 1)^3(...)
```

The script verifies:

```text
P is even;
J is odd;
rho is even;
J(-1) = J(1) = 0.
```

## Interpretation

This is a strong structural setup.

The parity result is important because it explains why the even quartic family is a reasonable response to Group 84. The linear-skew profile introduced odd/even imbalance that made dipole behavior difficult. The even quartic profile forces:

```text
J odd;
rho even.
```

That automatically suppresses odd flat moments of `rho` on the symmetric interval.

The compact endpoint flux also remains preserved for all `p,q`, meaning the family does not sacrifice exact flat neutrality while trying to suppress local payload.

## What Changed

The profile family has built-in structural advantages:

```text
endpoint neutrality is automatic;
odd-moment suppression is automatic by parity;
remaining payload work shifts to even moments.
```

That changes the payload-suppression problem from needing to control all low-order probes to needing to control the first few even moments.

## What Did Not Change

The family is still an ansatz. The script proves algebraic admissibility, not physical origin.

It does not prove that nature chooses an even quartic profile. It only proves that this is a regular test family with useful parity.

## Steering Consequence

The next step should solve the even-moment constraints. Since parity gives `M1=M3=...=0`, the real first tests are:

```text
M2 = 0
M4 = 0
```
