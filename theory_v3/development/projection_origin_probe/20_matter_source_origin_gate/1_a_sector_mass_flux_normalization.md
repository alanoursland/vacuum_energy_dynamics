# Matter Source Origin Gate 1: A-Sector Mass Flux Normalization

## Purpose

This proof isolates the ordinary reduced mass channel already present in the
archive:

```text
Delta_areal A = (8*pi*G/c^2) rho.
```

It verifies that the exterior A-sector solution carries exactly one ordinary
mass parameter through boundary flux.

## Validated Checks

- A_ext is source-free under the areal radial Laplacian: passed
- A-sector flux equals 8*pi*G*M/c^2: passed
- A-sector flux recovers exactly one mass M: passed
- 1/r exterior coefficient is fixed by boundary flux: passed

## Exterior Solution

Use:

```text
A_ext(r) = 1 - 2GM/(c^2 r).
```

SymPy verifies:

```text
(1/r^2) d/dr [r^2 A_ext'] = 0
```

for `r > R`, so the exterior is source-free.

## Flux Normalization

The A-sector flux is:

```text
F_A = 4*pi*r^2 A_ext'
    = 8*pi*G*M/c^2.
```

Therefore the reduced mass ledger:

```text
M_A = (c^2/(8*pi*G)) F_A
```

returns:

```text
M_A = M.
```

## Gate Interpretation

This is the ordinary mass channel. Any later residual, projection, trace, or
boundary object must not add an independent copy of this same mass unless a new
source-routing theorem explicitly allows it.
