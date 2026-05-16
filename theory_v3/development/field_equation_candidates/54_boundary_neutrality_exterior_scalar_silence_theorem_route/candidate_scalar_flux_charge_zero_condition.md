# candidate_scalar_flux_charge_zero_condition — Result Note

## Result

This script derives the reduced scalar flux / charge condition for the exterior one-over-r tail.

For:

```text
phi_tail = C1/r
```

it computes:

```text
F_phi = 4*pi*r^2*phi' = -4*pi*C1
```

and therefore, under the script's sign convention:

```text
q_phi = -F_phi/(4*pi) = C1
```

The zero-charge condition gives:

```text
C1=0 -> F_phi=0
```

## Main Findings

This connects the zero-tail condition from the Laplace script to a scalar charge condition. The one-over-r coefficient `C1` is not harmless bookkeeping; it is the scalar charge coefficient up to sign convention.

The reduced exterior silence route therefore requires:

```text
C1=0,
equivalently zero scalar charge / zero scalar flux.
```

This is still conditional. The script identifies the necessary condition; it does not derive why the theory enforces it.

## Boundary

The flux calculation is not insertion support. It does not prove boundary neutrality and does not prove zero scalar charge.

## Steering Consequence

Any future boundary theorem must explain the origin of `C1=0`: source absence, matching neutrality, constraint, postulate, or some derived scalar-charge conservation/neutrality condition. It cannot simply set `C1` to zero by wish.
