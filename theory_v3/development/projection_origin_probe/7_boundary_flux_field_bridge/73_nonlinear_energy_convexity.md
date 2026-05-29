# Boundary Flux Field Bridge 73: Nonlinear Energy Convexity

## Purpose

This report validates convexity conditions for nonlinear scalar strain
densities:

```text
W(g) = 1/2 |g|^2 + alpha/(2p)|g|^(2p).
```

## Validated Checks

- radial and tangential Hessian eigenvalues verified for p=1..5: passed

## Hessian Eigenvalues

At a point where `|g|=g`, the Hessian has tangential and radial eigenvalues:

```text
p=1: tangential=alpha + 1, radial=alpha + 1
p=2: tangential=alpha*g**2 + 1, radial=3*alpha*g**2 + 1
p=3: tangential=alpha*g**4 + 1, radial=5*alpha*g**4 + 1
p=4: tangential=alpha*g**6 + 1, radial=7*alpha*g**6 + 1
p=5: tangential=alpha*g**8 + 1, radial=9*alpha*g**8 + 1
```

Thus for:

```text
alpha >= 0,
```

both eigenvalues are positive.

## Interpretation

Positive polynomial nonlinear coefficients preserve convexity of the scalar
strain density. Negative coefficients can destabilize the energy and match the
invertibility failures found in proof `72`.
