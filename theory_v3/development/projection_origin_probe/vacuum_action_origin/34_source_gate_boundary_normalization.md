# Vacuum Action Origin 34: Source-Gate Boundary Normalization

## Purpose

This report imports the concrete output of `matter_source_origin_gate` back
into the vacuum-action chain.

The source gate fixed the weak boundary-flux normalization:

```text
K_A = c^2/(16*pi*G).
```

## Validated Checks

- matter-source gate fixes K_A=c^2/(16*pi*G): passed
- weak proper-time boundary variation gives F=M/(2K): passed
- K_A reproduces F_A=(8*pi*G/c^2)M: passed
- general target flux alpha*M fixes K=1/(2alpha): passed

## Boundary Balance

The weak shared-interval boundary variation has the form:

```text
K F - M/2 = 0.
```

Therefore:

```text
F = M/(2K).
```

The reduced A-sector flux target is:

```text
F_A = (8*pi*G/c^2) M.
```

Solving for `K` gives:

```text
K_A = c^2/(16*pi*G).
```

## Interpretation

This is the concrete handoff from source origin back to action origin. The
nonlinear vacuum action must reduce to this boundary normalization in the weak
A-sector.
