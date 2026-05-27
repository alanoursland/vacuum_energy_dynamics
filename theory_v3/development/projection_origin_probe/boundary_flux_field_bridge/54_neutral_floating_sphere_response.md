# Boundary Flux Field Bridge 54: Neutral Floating Sphere Response

## Purpose

This report validates the fixed-total-flux counterpart of the grounded sphere:
a neutral floating sphere in the field of an external point source.

## Validated Checks

- neutral compensating central charge: passed
- net induced charge vanishes: passed
- floating boundary potential: passed
- induced dipole moment: passed
- floating potential equals external center potential: passed
- dipole distance scaling: passed

## Construction

The grounded image response uses:

```text
q_img = -(R/d)q
b = R^2/d.
```

To keep the induced net charge zero, add a central compensating source:

```text
q_center = -q_img = (R/d)q.
```

Then:

```text
q_img + q_center = 0.
```

## Floating Boundary Potential

The source plus image pair gives zero boundary potential. The central source
adds a constant over the sphere:

```text
u_boundary = q_center/(4*pi*R) = q/(4*pi*d).
```

This is exactly the external source potential at the sphere center.

## Induced Dipole

The induced dipole moment is:

```text
p_induced = q_img*b = -q R^3/d^2.
```

The neutral floating sphere has no induced monopole, but it does have an
induced dipole response.

## Interpretation

Fixed total flux and fixed potential are different boundary hypotheses:

```text
grounded fixed potential -> induced net charge changes
neutral floating sphere -> net induced charge stays zero, dipole polarizes
```

This is the first exact proof that finite boundaries can carry induced
multipole structure even when their total flux is fixed.
