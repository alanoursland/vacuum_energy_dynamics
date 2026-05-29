# Matter Source Origin Gate 9: Weak-Limit Newtonian Source Match

## Purpose

This proof checks the source normalization against the Newtonian weak-field
limit.

## Validated Checks

- A=1+2Phi/c^2 maps Poisson to Delta A=8*pi*G*rho/c^2: passed
- Phi=-GM/r maps to A=1-2GM/(c^2 r): passed
- linearized normalization matches u=-Phi, h00=2u, bar_h00=4u: passed

## Newtonian Match

Use the weak-field relation:

```text
A = 1 + 2 Phi/c^2.
```

If:

```text
Delta Phi = 4*pi*G rho,
```

then:

```text
Delta A = 2 Delta Phi/c^2
        = 8*pi*G rho/c^2.
```

This matches the reduced A-sector source law.

## Exterior

For:

```text
Phi = -GM/r,
```

the A-field is:

```text
A = 1 - 2GM/(c^2 r).
```

## Gate Interpretation

The reduced A-sector source normalization is not arbitrary inside the current
chain. It is the weak-limit normalization required by ordinary Newtonian
gravity. This still does not prove the full covariant matter action, but it
anchors the reduced source coefficient.
