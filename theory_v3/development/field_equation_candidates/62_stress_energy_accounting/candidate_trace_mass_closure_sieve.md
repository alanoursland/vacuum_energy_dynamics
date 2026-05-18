# candidate_trace_mass_closure_sieve — Result Note

## Result

The script tests the one-parameter closure family:

```text
u = gamma*P
```

It obtains:

```text
T = -u + P = P*(1-gamma)
A = u + P = P*(gamma+1)
```

Therefore:

```text
trace-free closure:
  gamma = 1

active-mass-neutral closure:
  gamma = -1

simultaneous closure:
  P = 0
```

## Main Findings

This confirms and sharpens the Group 61 tension.

Trace-free and active-mass-neutral closure require incompatible choices of `gamma` unless the pressure sum vanishes:

```text
P = p_r + 2p_t = 0
```

So a one-parameter closure cannot provide both properties for a nonzero `P`.

This kills the tempting move:

```text
choose u=P and call it safe
```

because that only closes trace, not active mass.

It also kills:

```text
choose u=-P and call it safe
```

because that only closes active mass, not trace.

## Boundary

This is reduced algebra. It is not a stress-energy theorem.

## Steering Consequence

The next check must determine whether `P` is actually zero for the closure-supported layer. If not, simultaneous trace/mass closure is obstructed.
