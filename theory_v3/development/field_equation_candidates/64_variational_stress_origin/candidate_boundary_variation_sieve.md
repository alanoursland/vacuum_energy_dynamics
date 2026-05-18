# candidate_boundary_variation_sieve — Result Note

## Result

The script tests endpoint behavior for `eta`.

It finds clean value and slope silence:

```text
f(-1)=0
f(1)=0
f'(-1)=0
f'(1)=0
```

but nonzero second derivatives:

```text
f''(-1) =
-8*(7R^2 + 2Rell + ell^2)/(7R^2 + ell^2)

f''(1) =
8*(7R^2 - 2Rell + ell^2)/(7R^2 + ell^2)
```

## Main Findings

Endpoint value/slope silence is real and useful, but it is not a variational origin.

The boundary behavior helps explain why the profile is well-behaved at the layer edges, but it does not derive the profile, the bulk Euler-Lagrange equation, the stress tensor, the energy-density closure, or the amplitude.

The nonzero endpoint second derivatives keep the curvature/bulk burden visible.

The script correctly rejects:

```text
boundary silence as full variational origin;
slope silence as stress theorem.
```

## Boundary

This is a reduced boundary-variation audit, not a full variational theorem.

## Steering Consequence

Proceed to the route classifier. The simple origin attempts have now failed: scalar Euler-Lagrange, linear closure, amplitude origin, and boundary-only origin.
