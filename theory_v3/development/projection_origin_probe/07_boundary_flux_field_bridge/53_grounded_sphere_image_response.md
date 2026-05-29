# Boundary Flux Field Bridge 53: Grounded Sphere Image Response

## Purpose

This report validates the first exact induced-boundary response: a grounded
spherical boundary in the field of an external point source.

## Validated Checks

- Kelvin boundary distance relation: passed
- grounded boundary potential cancellation: passed
- image source strength: passed
- image position: passed
- grounded induced net charge: passed
- distance derivative of induced charge: passed

## Setup

Let an external source `q` sit at distance `d > R` from the center of a grounded
sphere of radius `R`.

The Kelvin image construction places an image source at:

```text
b = R^2/d
```

with strength:

```text
q_img = -(R/d)q.
```

## Boundary Cancellation

For a boundary point `R n`, with `mu=cos(theta)`, SymPy verifies:

```text
|R n - b e_z|^2 = (R^2/d^2)|R n - d e_z|^2.
```

Thus on the sphere:

```text
|R n - b e_z| = (R/d)|R n - d e_z|.
```

The boundary potential numerator is:

```text
q + q_img*d/R = 0.
```

So the sphere is held at zero potential.

## Interpretation

A fixed-potential boundary polarizes. Its induced net charge is:

```text
Q_induced = -(R/d)q.
```

This depends on the external source distance. Therefore fixed-potential
boundaries are not fixed-source-strength boundaries. They are response
conditions, and their induced flux changes with environment.
