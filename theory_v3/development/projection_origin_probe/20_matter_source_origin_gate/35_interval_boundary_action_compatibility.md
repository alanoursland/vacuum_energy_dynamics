# Matter Source Origin Gate 35: Interval Boundary Action Compatibility

## Purpose

This proof checks compatibility between two reduced descriptions:

```text
proper-time/interval matter coupling
boundary source coupling
```

It does not fix the full normalization of the gravitational action. It checks
that the weak boundary source has the expected linear dependence on the local
interval component.

## Validated Checks

- proper-time boundary variation gives leading coefficient -M/2: passed
- linearized proper-time source is proportional to -M A/2 up to constants: passed
- boundary source coefficient can be matched to flux normalization: passed

## Proper-Time Boundary Source

For a static boundary particle or shell:

```text
S_m = -M sqrt(A(R)).
```

The variation coefficient is:

```text
dS_m/dA = -M/(2 sqrt(A)).
```

Near:

```text
A = 1 + epsilon,
```

this becomes:

```text
dS_m/dA = -M/2 + O(epsilon).
```

Thus the leading weak boundary source is equivalent, up to constants, to:

```text
S_m,lin = -(M/2) A(R).
```

## Gate Interpretation

The reduced boundary source used in the A-sector flux proofs is compatible
with weak proper-time matter coupling. Matching the exact coefficient requires
the gravitational action normalization, which belongs to the action-origin
chain.
