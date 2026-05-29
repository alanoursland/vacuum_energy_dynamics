# Synthesis Proof 23: `y=x^2` Pairing Structure

## Purpose

This report rewrites the balanced projection pairing using:

```text
y = x^2.
```

## Validated Checks

- psi_k becomes y^(k-1)(y-r_k): passed
- balanced sources become (1-y)^R(y^q-c): passed
- full y-pairing integrand verified: passed
- balancing coefficient beta/product form: passed

## Transformed Objects

The row tests become:

```text
psi_k(y) = y^k - ((2k-1)/(2k+3)) y^(k-1)
         = y^(k-1)(y-r_k).
```

Balanced sources become:

```text
B_(R,q)(y) = (1-y)^R (y^q - c_(R,q)).
```

The pairing becomes:

```text
integral_0^1 psi_k(x) B_(R,q)(x) a^4 dx

= 1/2 integral_0^1
    psi_k(y) (y^q-c_(R,q)) (1-y)^(R+4) y^(-1/2) dy.
```

So the problem is a Jacobi-type weighted polynomial pairing on `[0,1]`.

## Balancing Coefficient

The balancing coefficient is:

```text
c_(R,q)
  =
  B(q+1/2, R+2) / B(1/2, R+2)
```

or equivalently:

```text
c_(R,q)
  =
  (1/2)_q / (R+5/2)_q.
```

This is the `y`-variable form of the admissibility condition:

```text
integral_0^1 a B_(R,q) dx = 0.
```
