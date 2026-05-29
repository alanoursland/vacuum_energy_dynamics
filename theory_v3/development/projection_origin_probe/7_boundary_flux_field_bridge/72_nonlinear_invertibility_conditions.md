# Boundary Flux Field Bridge 72: Nonlinear Invertibility Conditions

## Purpose

This report validates when the radial nonlinear flux law is monotone and
therefore locally invertible.

## Validated Checks

- flux derivative formulas verified for p=1..7: passed
- negative nonlinear coefficient critical points verified for p=2..6: passed

## Polynomial Flux Law

For:

```text
Phi_p(z)=1/2 z + alpha/(2p) z^p,
```

the flux-field relation has the scalar form:

```text
F_p(y)=y + alpha y^(2p-1).
```

SymPy verifies:

```text
p=1: dF/dy = alpha + 1
p=2: dF/dy = 3*alpha*y**2 + 1
p=3: dF/dy = 5*alpha*y**4 + 1
p=4: dF/dy = 7*alpha*y**6 + 1
p=5: dF/dy = 9*alpha*y**8 + 1
p=6: dF/dy = 11*alpha*y**10 + 1
p=7: dF/dy = 13*alpha*y**12 + 1
```

For:

```text
alpha >= 0, y >= 0,
```

this derivative is positive, so the flux law is monotone.

## Negative Coefficient Failure

For a negative nonlinear coefficient, write:

```text
F_p(y)=y - beta y^(2p-1), beta>0.
```

Then monotonicity fails at finite positive `y`:

```text
p=2: ycrit = sqrt(3)/(3*sqrt(beta))
p=3: ycrit = 5**(3/4)/(5*beta**(1/4))
p=4: ycrit = 7**(5/6)/(7*beta**(1/6))
p=5: ycrit = 3**(3/4)/(3*beta**(1/8))
p=6: ycrit = 11**(9/10)/(11*beta**(1/10))
```

## Interpretation

Nonlinear scalar bridge candidates should preserve monotone flux-field
inversion at least in the physical field range. Positive polynomial nonlinear
coefficients pass this basic stability/invertibility test.
