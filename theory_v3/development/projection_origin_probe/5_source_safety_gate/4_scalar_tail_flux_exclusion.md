# Source Safety Gate 4: Scalar-Tail Flux Exclusion

## Purpose

This proof reconstructs the reduced scalar-tail witness used in the archive.
It applies to a source-free exterior scalar profile:

```text
phi(r) = C0 + C1/r.
```

## Source-Free Exterior Check

SymPy verifies:

```text
(1/r^2) d/dr [r^2 phi'(r)] = 0.
```

So `C0 + C1/r` is the general spherical source-free harmonic tail.

## Flux Witness

The sphere flux is:

```text
F_phi = 4*pi*r^2 phi'(r).
```

SymPy gives:

```text
F_phi = -4*pi*C1.
```

## Result

Zero exterior scalar flux requires:

```text
C1 = 0.
```

If ordinary exterior scalar silence also forbids a constant scalar offset, then:

```text
C0 = 0
C1 = 0.
```

## Gate Status

This is a reduced scalar-tail exclusion witness. It does not by itself prove
that every residual scalar sector is absent; it states the exterior tail a
successful source-safety theorem must eliminate or route as non-metric.
