# candidate_charge_neutral_source — Result Note

## Result

The script constructs a nontrivial internal profile with zero net scalar charge:

```text
rho(r) = rho0*(1 - 5*r^2/(3*R^2))
```

It verifies:

```text
integral_0^R r^2*rho(r) dr = 0
```

and confirms nontriviality:

```text
rho(R/2) = 7*rho0/12
```

## Main Findings

This is important reduced progress. The script shows that silent exterior charge does not require the internal profile to vanish identically.

The internal profile can be nonzero while carrying no net exterior scalar charge. That provides an actual reduced route for “silent/inert” behavior rather than merely demanding the scalar channel be empty.

The result remains diagnostic. Zero net scalar charge does not prove source no-double-counting, source admissibility, full boundary neutrality, or physical insertion.

## Boundary

The profile is not an inserted matter source. It is not a source theorem. It does not prove that ordinary source load is protected.

## Steering Consequence

The next check should connect zero net charge to exterior tail silence. The profile has `Q=0`; the exterior scalar should vanish only if the constant offset is also zero.
