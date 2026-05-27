# Matter Source Origin Gate 13: Point-Particle Metric Coupling Weak Limit

## Purpose

This proof checks the standard weak-field matter coupling at the point-particle
level.

It is a covariant-matter gate because it starts from the metric line element,
not from an imposed Poisson source.

## Validated Checks

- point-particle action gives kinetic term plus potential -m Phi: passed
- potential energy m Phi gives force -m grad Phi: passed
- with u=-Phi, h00=2u/c^2: passed

## Weak Metric

Use:

```text
g_00 = -(1 + 2 Phi/c^2).
```

For a slow particle:

```text
L = -m c^2 sqrt(1 + 2 Phi/c^2 - v^2/c^2).
```

Expanding to first order in `Phi/c^2` and `v^2/c^2` gives:

```text
L = -m c^2 + (1/2)m v^2 - m Phi.
```

Therefore the potential energy is:

```text
U = m Phi,
```

and the force is:

```text
F = -m grad Phi.
```

## Relation To The Bridge Variable

The earlier geometric lift used:

```text
u = -Phi.
```

With:

```text
h_00 = g_00 - eta_00,
```

one gets:

```text
h_00 = -2 Phi/c^2 = 2u/c^2.
```

## Gate Interpretation

This proves that ordinary matter couples to the weak metric in the way needed
to recover Newtonian motion. It does not yet derive the full vacuum action.
