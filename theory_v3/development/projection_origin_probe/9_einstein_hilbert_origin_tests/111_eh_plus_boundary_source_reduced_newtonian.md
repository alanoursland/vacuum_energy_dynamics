# Einstein-Hilbert Origin Test 111: EH Boundary Source Reduced Newtonian Sector

## Purpose

This report validates the reduced-action Newtonian interaction using the
Einstein-Hilbert linearized source normalization.

## Validated Checks

- EH trace-reversed static source coefficient: passed
- trace-reversed boundary flux: passed
- metric potential conversion: passed
- trace-reversed Green solution: passed
- reduced action cross prefactor: passed
- EH reduced Newtonian interaction: passed
- EH reduced Newtonian force sign: passed

## Trace-Reversed Variable

Let:

```text
B = bar h_00 = -4 Phi = 4u.
```

The static Newtonian-sector quadratic/source energy can be written:

```text
E[B] = 1/2 c <B, -Delta B> - alpha <rho, B>
```

with:

```text
c = 1/(64*pi*G)
alpha = 1/4.
```

SymPy verifies:

```text
alpha/c = 16*pi*G.
```

So:

```text
-Delta B = 16*pi*G rho.
```

## Boundary Flux

For a point mass exterior:

```text
B = 4GM/r,
```

the boundary flux is:

```text
- integral partial_n B dA = 16*pi*G M.
```

This is the trace-reversed metric version of the scalar boundary flux.

## Reduced Interaction

Eliminating `B` from the quadratic/source energy gives:

```text
E_cross = -G M1 M2/d.
```

The separation derivative is:

```text
F_d = -dE/dd = -G M1 M2/d^2.
```

## Interpretation

The Einstein-Hilbert weak-field source coupling reproduces the same attractive
reduced interaction found in the scalar boundary-flux bridge, with the standard
metric normalization.
