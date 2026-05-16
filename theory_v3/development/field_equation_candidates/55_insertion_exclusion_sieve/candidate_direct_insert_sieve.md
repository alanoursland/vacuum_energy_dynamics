# candidate_direct_insert_sieve — Result Note

## Result

The direct insertion sieve produces a useful symbolic obstruction diagnostic.

It defines a direct insertion load:

```text
L = C1*a_C + J*a_J + Q_trace*a_Q + S_M*a_S + T_zeta*a_T
```

and checks special cases:

```text
silent/no-direct-load case = 0
trace direct load = T_zeta
source direct load = S_M
boundary direct load = C1 + J
mass direct load = Q_trace
```

The trace, source, boundary, and mass direct-load cases are all rejected.

## Main Findings

This is a strong insertion-family exclusion result. A direct insertion route that creates trace load, ordinary source load, boundary/scalar load, shell load, or mass charge before theorem support is unsafe.

The only route that survives this sieve is the no-direct-load route:

```text
all direct load coefficients zero
```

But that is not insertion. It is only a silent/inert theorem target.

The script also rejects hiding load inside coefficients. That matters because an insertion law cannot smuggle source or boundary content through parameter names.

## Boundary

The load diagnostic is not a field equation. The no-direct-load case is not an insertion law. It does not prove safety.

## Steering Consequence

Direct physical insertion is not admissible. Any future surviving route must be silent/inert with no forbidden direct trace/source/boundary/mass load.
