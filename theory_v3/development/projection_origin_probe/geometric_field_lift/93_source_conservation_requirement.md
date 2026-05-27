# Geometric Field Lift 93: Source Conservation Requirement

## Purpose

This report validates the source-conservation requirement in the linearized
geometric field equation.

## Validated Checks

- field-equation divergence requires source conservation: passed

## Field Equation

Let:

```text
G_ab = kappa T_ab.
```

The linearized Bianchi identity gives:

```text
partial^a G_ab = 0.
```

Taking the divergence of the field equation therefore gives:

```text
0 = kappa partial^a T_ab.
```

For nonzero `kappa`:

```text
partial^a T_ab = 0.
```

## Interpretation

The geometric lift imposes a conservation law on admissible sources. This is a
stronger structural requirement than the scalar bridge alone.
