# Geometric Field Lift 94: Static Green Solution for `bar h_00`

## Purpose

This report validates the static Green solution for the trace-reversed metric
component in the Newtonian sector.

## Validated Checks

- bar_h00 harmonic off source: passed
- bar_h00 boundary flux: passed
- mass from bar_h00 flux: passed
- bar_h00 relation to scalar bridge: passed
- h00 relation to scalar bridge: passed
- static de Donder operator off source: passed

## de Donder Equation

In de Donder gauge:

```text
G_ab = -1/2 box bar h_ab.
```

For a static source:

```text
-1/2 Delta bar h_00 = 8*pi*G rho.
```

For a point mass `M`, the exterior solution is:

```text
bar h_00 = 4GM/r.
```

## Boundary Flux

SymPy verifies:

```text
-integral partial_n bar h_00 dA = 16*pi*G M.
```

Therefore:

```text
M = [-integral partial_n bar h_00 dA]/(16*pi*G).
```

## Scalar Bridge Relation

With:

```text
u = GM/r,
```

one has:

```text
h_00 = 2u
bar h_00 = 4u.
```
