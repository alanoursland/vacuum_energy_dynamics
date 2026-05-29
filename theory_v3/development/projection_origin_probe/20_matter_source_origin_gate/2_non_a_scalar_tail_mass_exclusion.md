# Matter Source Origin Gate 2: Non-A Scalar Tail Mass Exclusion

## Purpose

This proof records the reduced scalar-tail gate that protects the ordinary
A-sector mass channel from duplication by non-A sectors.

## Validated Checks

- C0 + C1/r is source-free outside the boundary: passed
- scalar 1/r tail carries flux -4*pi*C1: passed
- zero C1 removes any flux-proportional scalar mass shift: passed
- nonzero C1 is a nonzero far-zone flux witness: passed

## Exterior Scalar Tail

For a source-free radial scalar exterior:

```text
phi(r) = C0 + C1/r,
```

SymPy verifies:

```text
(1/r^2) d/dr [r^2 phi'] = 0.
```

The far-zone flux is:

```text
F_phi = 4*pi*r^2 phi'
      = -4*pi*C1.
```

## Gate Interpretation

A nonzero `C1` is a source-like exterior tail. If a non-A sector is supposed
to remain source-neutral, it must satisfy:

```text
C1 = 0.
```

If the constant mode is also not an allowed background shift, then:

```text
C0 = 0.
```

This proof does not exclude all scalar fields. It excludes unlicensed scalar
mass tails in sectors that are supposed to be neutral.
