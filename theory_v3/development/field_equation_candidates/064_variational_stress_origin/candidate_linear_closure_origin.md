# candidate_linear_closure_origin — Result Note

## Result

The script tests a linear energy-density closure:

```text
u = a p_r + b p_t
```

with diagnostics:

```text
T = -u + p_r + 2p_t
A = u + p_r + 2p_t
```

It finds:

```text
trace-free linear closure:
  a=1
  b=2

active-mass-neutral linear closure:
  a=-1
  b=-2

simultaneous linear closure:
  []
```

## Main Findings

The linear closure route reproduces the Group 62 trace/mass obstruction.

A trace-free closure exists:

```text
u = p_r + 2p_t
```

An active-mass-neutral closure exists:

```text
u = -(p_r + 2p_t)
```

But no constant linear coefficients close both diagnostics simultaneously.

This means the linear stress-origin route does not solve the obstruction. It merely restates it in a broader closure form.

## Boundary

This is reduced closure algebra. It does not rule out nonlinear, tensor, constrained, or covariant stress origins.

## Steering Consequence

Proceed to amplitude origin. Even if a future closure principle existed, the amplitude `p_free` still needs a physical origin.
