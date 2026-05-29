# Geometric Field Lift 96: Linearized Action Reduced Source Sign

## Purpose

This report validates that the scalar reduced-action attraction mechanism lifts
with the correct coefficient to the linearized trace-reversed Newtonian sector.

## Validated Checks

- trace-reversed field equation coefficient: passed
- bar_h00 Green field from M2: passed
- reduced action cross prefactor: passed
- Newtonian reduced cross energy: passed
- Newtonian attractive separation derivative: passed
- Newtonian energy from scalar reduced action normalization: passed

## Trace-Reversed Variable

Let:

```text
B = bar h_00
A = -Delta.
```

Use the static quadratic/source action:

```text
E[B] =
  (1/(128*pi*G)) <B,A B>
  - (1/4)<rho,B>.
```

Equivalently:

```text
c = 1/(64*pi*G)
alpha = 1/4
E = 1/2 c <B,A B> - alpha<rho,B>.
```

The field equation is:

```text
A B = (alpha/c) rho = 16*pi*G rho.
```

This matches:

```text
-1/2 Delta bar h_00 = 8*pi*G rho.
```

## Reduced Interaction

The reduced cross term is:

```text
E_cross = -(alpha^2/c) M1 M2 G(d),
```

where:

```text
G(d)=1/(4*pi*d).
```

SymPy verifies:

```text
E_cross = -G M1 M2/d.
```

Therefore:

```text
F_d = -dE/dd = -G M1 M2/d^2.
```

## Scalar Bridge Normalization

With:

```text
Q_i = 4*pi*G M_i,
```

the scalar reduced action:

```text
-Q1 Q2/(4*pi*d)
```

becomes the Newtonian energy after dividing by `4*pi*G`.

## Interpretation

The reduced-action attraction mechanism is not only scalar. With the correct
linearized-gravity normalization, it reproduces the Newtonian interaction
energy and force sign.
