# Source Safety Gate 5: Boundary Current Flux Silence

## Purpose

This proof reconstructs the far-zone radial-current witness:

```text
J_r(r) = I/(4*pi*r^2).
```

## Flux Witness

The sphere flux is:

```text
F_J = 4*pi*r^2 J_r.
```

SymPy verifies:

```text
F_J = I.
```

The far-zone current is divergence-free away from the source:

```text
(1/r^2) d/dr [r^2 J_r] = 0.
```

## Result

Zero exterior current flux requires:

```text
I = 0.
```

## Gate Status

This is the current analogue of scalar-tail silence. A residual or boundary
current cannot be silently present in the exterior unless its flux coefficient
vanishes or it is explicitly routed as a non-metric diagnostic object.
