# candidate_closure_inventory — Result Note

## Result

The script inventories the reduced stress-energy variables for the source-independent stress-only transition response.

It defines:

```text
eta = (y^2-1)^2*(-2Rell + y*(7R^2+ell^2))/(7R^2+ell^2)

p_r = p0*eta^2

p_t = p_r + r*p_r'/2

P = p_r + 2p_t
```

and the two diagnostics:

```text
trace diagnostic:
  T = -u + P

active-mass diagnostic:
  A = u + P
```

## Main Findings

The important object is:

```text
P = p_r + 2p_t
```

Both trace accounting and active-mass accounting depend on this same pressure sum.

That means `u` cannot be chosen independently of the transition stress. The energy-density closure has to account for `P`, or the candidate remains unlicensed.

The inventory also confirms that the tangential closure is still reduced:

```text
p_t = p_r + r*p_r'/2
```

It is not a covariant stress tensor and not a Bianchi identity.

## Boundary

This is inventory only. It does not solve stress-energy accounting.

## Steering Consequence

The next step is to test the one-parameter closure family:

```text
u = gamma*P
```

to see whether trace-free and active-mass-neutral requirements can be satisfied together.
